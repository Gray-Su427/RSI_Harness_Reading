#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_pdfs.py — 按 CSV 批量下载论文 PDF

零依赖，仅用 Python 3 标准库。

多源回退链：
    1. arXiv 直连         https://arxiv.org/pdf/<id>      （最快最可靠）
    2. Semantic Scholar   按 arXiv ID 查 openAccessPdf
    3. Semantic Scholar   按标题查 openAccessPdf
    4. OpenAlex           按标题查 best_oa_location.pdf_url

产出：
    refs/pdfs/<id>__<slug>.pdf
    refs/pdfs/_manifest.csv   每篇的实际来源 URL / 状态 / sha1
    refs/pdfs/_missing.csv    全部来源都失败的条目

用法：
    python scripts/fetch_pdfs.py --dry-run      # 只解析，不下载
    python scripts/fetch_pdfs.py                # 下载 verified.csv 全部
    python scripts/fetch_pdfs.py --only arxiv-2505.22954 arxiv-2606.09498
    python scripts/fetch_pdfs.py --csv refs/pool.csv --out refs/pdfs-pool

注意：
    - arXiv 官方要求请求间隔 >= 3s，脚本已内置节流；请勿用并发绕过
    - 已存在的文件默认跳过（幂等），--force 可强制重下
    - 本脚本【不会】修改 CSV 中的 venue_verified 字段
"""

import argparse
import csv
import hashlib
import io
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

# Windows 控制台默认 GBK，输出中文会抛 UnicodeEncodeError
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

UA = "RSI-Harness-Review/1.0 (course literature review; contact: set-your-email@example.edu)"

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

ARXIV_MIN_INTERVAL = 3.0   # arXiv 官方要求
API_MIN_INTERVAL = 1.1     # 公共 API 保守限速

STOPWORDS = {
    "a", "an", "the", "of", "for", "and", "or", "to", "in", "on", "with",
    "is", "are", "via", "using", "towards", "toward", "from", "by", "as",
}


# ────────────────────────────── 工具函数 ──────────────────────────────

def slugify(title, maxlen=60):
    """从标题生成文件名友好的短 slug。"""
    words = re.sub(r"[^0-9A-Za-z\s]+", " ", title or "").split()
    keep = [w for w in words if w.lower() not in STOPWORDS] or words
    out = "_".join(keep)
    out = re.sub(r"_+", "_", out).strip("_")
    return (out[:maxlen].rstrip("_") or "untitled")


def strip_version(arxiv_id):
    """2606.09498v3 -> 2606.09498"""
    return re.sub(r"v\d+$", "", arxiv_id.strip())


def parse_id(pid):
    """返回 ('arxiv', '2606.09498') 或 ('other', pid) 或 (None, None)"""
    pid = (pid or "").strip()
    m = re.match(r"^arxiv[-_/](.+)$", pid, re.I)
    if m:
        return "arxiv", strip_version(m.group(1))
    # 裸的 arXiv 样式 ID 也尝试识别
    if re.match(r"^\d{4}\.\d{4,5}$", pid):
        return "arxiv", pid
    return ("other", pid) if pid else (None, None)


def http_get(url, timeout=30):
    """返回 bytes；失败抛异常。"""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def http_get_json(url, timeout=30):
    raw = http_get(url, timeout=timeout)
    return json.loads(raw.decode("utf-8", errors="replace"))


class Throttle:
    """按 host 限速。"""

    def __init__(self):
        self.last = {}

    def wait(self, host, interval):
        prev = self.last.get(host)
        now = time.monotonic()
        if prev is not None:
            gap = now - prev
            if gap < interval:
                time.sleep(interval - gap)
        self.last[host] = time.monotonic()


THROTTLE = Throttle()


def fetch_with_retry(url, timeout, attempts=3, base_delay=2.0, arxiv=False):
    """带指数退避的下载。返回 bytes 或抛最后一次异常。"""
    host = urllib.parse.urlparse(url).netloc
    interval = ARXIV_MIN_INTERVAL if arxiv else API_MIN_INTERVAL
    last_err = None
    for i in range(attempts):
        THROTTLE.wait(host, interval)
        try:
            return http_get(url, timeout=timeout)
        except urllib.error.HTTPError as e:
            last_err = e
            # 4xx（除 429）不重试
            if e.code != 429 and 400 <= e.code < 500:
                raise
        except Exception as e:
            last_err = e
        if i < attempts - 1:
            delay = base_delay * (2 ** i) + random.uniform(0, 0.8)
            print("      重试 {}/{}（{}s 后）：{}".format(
                i + 1, attempts, round(delay, 1), type(last_err).__name__))
            time.sleep(delay)
    raise last_err


def is_pdf(data):
    """校验 magic bytes —— 服务器常在 200 响应里返回 HTML 错误页。"""
    return data[:5] == b"%PDF-"


def safe_write(path, data):
    tmp = path + ".part"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)


# ──────────────────────────── 各来源解析 ────────────────────────────

def resolve_arxiv_direct(rec):
    kind, aid = parse_id(rec.get("id", ""))
    if kind != "arxiv":
        return None
    return ("https://arxiv.org/pdf/" + aid, "arxiv", True)


def resolve_semantic_scholar(rec, _cache={}):
    kind, aid = parse_id(rec.get("id", ""))
    title = (rec.get("title") or "").strip()
    base = "https://api.semanticscholar.org/graph/v1/paper"

    queries = []
    if kind == "arxiv":
        queries.append("{}/arXiv:{}?fields=openAccessPdf".format(base, urllib.parse.quote(aid)))
    if title:
        queries.append("{}/search?query={}&fields=title,openAccessPdf".format(
            base, urllib.parse.quote(title)))
        queries.append("{}/search/match?query={}&fields=title,openAccessPdf".format(
            base, urllib.parse.quote(title)))

    for q in queries:
        try:
            if q in _cache:
                doc = _cache[q]
            else:
                doc = http_get_json(q, timeout=25)
                _cache[q] = doc
            pdf = doc.get("openAccessPdf") if isinstance(doc, dict) else None
            if isinstance(pdf, dict) and pdf.get("url"):
                return (pdf["url"], "semantic-scholar", False)
        except urllib.error.HTTPError as e:
            if e.code in (429, 404):
                continue
        except Exception:
            continue
    return None


def resolve_openalex(rec):
    title = (rec.get("title") or "").strip()
    if not title:
        return None
    url = ("https://api.openalex.org/works?filter=title.search:{}&per-page=3".format(
        urllib.parse.quote(title)))
    try:
        doc = http_get_json(url, timeout=25)
    except Exception:
        return None
    for work in (doc.get("results") or []):
        loc = work.get("best_oa_location") or {}
        if loc.get("pdf_url"):
            return (loc["pdf_url"], "openalex", False)
    return None


RESOLVERS = [
    ("arxiv", resolve_arxiv_direct),
    ("semantic-scholar", resolve_semantic_scholar),
    ("openalex", resolve_openalex),
]


# ────────────────────────────── 主流程 ──────────────────────────────

def load_csv(path):
    # utf-8-sig 兼容带 BOM 的 Excel 导出
    with io.open(path, "r", encoding="utf-8-sig", newline="") as f:
        rows = [r for r in csv.DictReader(f) if (r.get("id") or "").strip()]
    return rows


def target_name(rec):
    return "{}__{}.pdf".format(rec["id"].strip(), slugify(rec.get("title", "")))


def main():
    ap = argparse.ArgumentParser(
        description="按 CSV 批量下载论文 PDF（零依赖）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("用法：")[-1] if __doc__ else None,
    )
    ap.add_argument("--csv", default=os.path.join(REPO, "refs", "verified.csv"),
                    help="CSV 路径（默认 refs/verified.csv）")
    ap.add_argument("--out", default=None,
                    help="PDF 输出目录（默认 <csv 同级>/pdfs）")
    ap.add_argument("--only", nargs="+", metavar="ID", help="只处理指定 ID")
    ap.add_argument("--dry-run", action="store_true", help="只解析来源，不下载")
    ap.add_argument("--force", action="store_true", help="已存在也重新下载")
    ap.add_argument("--timeout", type=int, default=60, help="单次请求超时秒数（默认 60）")
    ap.add_argument("--max-mb", type=int, default=50, help="单文件大小上限 MB（默认 50）")
    args = ap.parse_args()

    csv_path = os.path.abspath(args.csv)
    if not os.path.isfile(csv_path):
        sys.exit("找不到 CSV：{}".format(csv_path))

    out_dir = os.path.abspath(args.out) if args.out else \
        os.path.join(os.path.dirname(csv_path), "pdfs")
    if not args.dry_run:
        os.makedirs(out_dir, exist_ok=True)

    rows = load_csv(csv_path)
    if args.only:
        wanted = {x.strip() for x in args.only}
        rows = [r for r in rows if r["id"].strip() in wanted]
        if not rows:
            sys.exit("指定 ID 在 CSV 中均未找到：{}".format(", ".join(sorted(wanted))))

    print("CSV      : {}（{} 条）".format(csv_path, len(rows)))
    print("输出目录 : {}".format(out_dir))
    if args.dry_run:
        print("模式     : DRY-RUN，只解析来源不下载\n")
    else:
        print("限速     : arXiv >= {}s / API >= {}s\n".format(ARXIV_MIN_INTERVAL, API_MIN_INTERVAL))

    manifest, missing = [], []
    stats = {"skipped": 0, "ok": 0, "fail": 0}

    for i, rec in enumerate(rows, 1):
        pid = rec["id"].strip()
        title = rec.get("title", "")
        year = rec.get("year", "")
        fname = target_name(rec)
        fpath = os.path.join(out_dir, fname)
        prefix = "[{}/{}] {}".format(i, len(rows), pid)

        print("{}\n   {}".format(prefix, (title or "")[:88]))

        if os.path.exists(fpath) and not args.force:
            size = os.path.getsize(fpath)
            print("   ⏭  已存在（{:.1f} MB），跳过".format(size / 1e6))
            stats["skipped"] += 1
            manifest.append({
                "id": pid, "title": title, "year": year, "status": "skipped",
                "source": "local", "url": "", "file": fname,
                "bytes": size, "sha1": "", "fetched_at": "",
            })
            continue

        if args.dry_run:
            resolved = None
            for sname, fn in RESOLVERS:
                try:
                    resolved = fn(rec)
                except Exception as e:
                    print("   · {} 解析异常：{}".format(sname, type(e).__name__))
                    continue
                if resolved:
                    print("   → 将尝试 {}：{}".format(resolved[1], resolved[0]))
                    break
            if resolved:
                stats["ok"] += 1
                manifest.append({
                    "id": pid, "title": title, "year": year, "status": "resolved",
                    "source": resolved[1], "url": resolved[0], "file": fname,
                    "bytes": "", "sha1": "", "fetched_at": "",
                })
            else:
                print("   ✗ 所有来源均未解析到 PDF URL")
                stats["fail"] += 1
                missing.append({"id": pid, "title": title, "year": year,
                                "reason": "no-pdf-url"})
            continue

        got = None
        reasons = []
        for sname, fn in RESOLVERS:
            try:
                resolved = fn(rec)
            except Exception as e:
                reasons.append("{}:{}".format(sname, type(e).__name__))
                continue
            if not resolved:
                reasons.append("{}:no-url".format(sname))
                continue
            url, src, is_arxiv = resolved
            try:
                data = fetch_with_retry(url, args.timeout, arxiv=is_arxiv)
            except Exception as e:
                reasons.append("{}:{}".format(src, type(e).__name__))
                print("   ✗ {} 下载失败：{}".format(src, e))
                continue

            if not is_pdf(data):
                reasons.append("{}:not-a-pdf".format(src))
                print("   ✗ {} 返回的不是 PDF（{} 字节，可能是错误页）".format(src, len(data)))
                continue
            if len(data) > args.max_mb * 1024 * 1024:
                reasons.append("{}:too-large".format(src))
                print("   ✗ {} 文件超过 {} MB 上限".format(src, args.max_mb))
                continue

            safe_write(fpath, data)
            digest = hashlib.sha1(data).hexdigest()
            print("   ✅ {}（{:.1f} MB）  来源: {}  sha1: {}"
                  .format(fname, len(data) / 1e6, src, digest[:12]))
            stats["ok"] += 1
            manifest.append({
                "id": pid, "title": title, "year": year, "status": "ok",
                "source": src, "url": url, "file": fname,
                "bytes": len(data), "sha1": digest,
                "fetched_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            })
            got = True
            break

        if not got:
            print("   ❌ 全部来源失败：{}".format("; ".join(reasons) or "unknown"))
            stats["fail"] += 1
            missing.append({"id": pid, "title": title, "year": year,
                            "reason": "; ".join(reasons) or "unknown"})

    # ── 输出清单 ──
    if not args.dry_run:
        mpath = os.path.join(out_dir, "_manifest.csv")
        cols = ["id", "title", "year", "status", "source", "url", "file", "bytes", "sha1", "fetched_at"]
        new = [m for m in manifest if m["status"] == "ok"]
        old = []
        if os.path.exists(mpath):
            with io.open(mpath, "r", encoding="utf-8-sig", newline="") as f:
                old = list(csv.DictReader(f))
        merged = {m["id"]: m for m in old}
        merged.update({m["id"]: m for m in new})
        with io.open(mpath, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            for m in merged.values():
                w.writerow({k: m.get(k, "") for k in cols})
        print("\n清单已写入: {}".format(mpath))

        if missing:
            xpath = os.path.join(out_dir, "_missing.csv")
            with io.open(xpath, "w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["id", "title", "year", "reason"])
                w.writeheader()
                w.writerows(missing)
            print("失败清单: {}（{} 条）".format(xpath, len(missing)))
            print("  → 这些多半没有开放获取版本，建议走机构订阅手动下载，")
            print("    或在 notes/skim/ 标注为「PDF 未获取，已读摘要」。")

    print("\n" + "─" * 52)
    print("完成：成功 {} · 跳过 {} · 失败 {}".format(
        stats["ok"], stats["skipped"], stats["fail"]))
    if not args.dry_run and stats["ok"]:
        print("PDF 已下载到 {}（不入版本库，见 .gitignore）".format(out_dir))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n已中断。已下载的文件保留，可重新运行续传。")
        sys.exit(130)
