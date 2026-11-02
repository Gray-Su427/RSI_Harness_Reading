# refs/ — 文献元数据

本目录是项目内**唯一的文献数据源**。笔记与写作仓库中的每一条引用都必须能追溯到这里。

## 文件

| 文件 | 作用 | 维护方式 |
|---|---|---|
| `verified.csv` | **已核验**论文的元数据（当前 19 篇） | 手工维护 |
| `pool.csv` | 泛读候选池，**尚未**核验/筛选的全集 | 泛读阶段持续追加 |
| `refs.bib` | BibTeX 库，供写作仓库引用 | **由 Zotero 导出**，勿手写 |

> `refs.bib` 已提供引导版本（19 条，由 `verified.csv` 构造）。
> 按 `AGENTS.md` §7.4，最终应由 Zotero 管理并导出到本目录。
> 写作仓库通过 `scripts/sync_refs.py` 生成本地快照，不手改快照。

> ⚠️ **`fetch_pdfs.py` 目前只能解析 19 条中的 18 条**：`venue-2026-dcri-survey` 没有 arXiv ID，
> 脚本的 arXiv / Semantic Scholar / OpenAlex 三路解析都会失败（`--dry-run` 实测为「失败 1」）。
> 该条的 PDF 需手动取：[Preprints.org](https://www.preprints.org/manuscript/202609.0154) 或
> [GitHub 上的 PDF](https://github.com/zoezou2015/Awesome-Data-Centric-Recursive-Improvement/blob/main/paper/dcri_survey_2026.pdf)。
> 这是**预期失败**，不是脚本坏了；`_missing.csv` 里会如实记录。

---

## `verified.csv` 字段说明

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | 文本 | **主键**，与笔记文件名一致。`arxiv-<YYMM>.<NNNNN>` 或 `venue-<年份>-<slug>` |
| `title` | 文本 | 原文标题，**不要翻译** |
| `authors` | 文本 | 前 3 位作者 + `et al.` |
| `year` | 整数 | 发表/发布年份 |
| `venue` | 文本 | 会议全称，或 `arXiv preprint` |
| `venue_verified` | `true`/`false` | **仅当**经 DBLP / OpenReview / 会议官网确认后填 `true` |
| `industry` | `true`/`false` | 是否工业界（或产学合作） |
| `org` | 文本 | 机构。非空便于按机构聚类分析 |
| `role` | 枚举 | `seed` 课程种子 / `harness-core` 直接命中 / `industry` 工业界 / `survey` 综述 |
| `axis_a_object` | 列表 | 改进对象。`;` 分隔多值 |
| `axis_b_signal` | 列表 | 改进信号。`;` 分隔 |
| `axis_c_search` | 列表 | 搜索算子。`;` 分隔 |
| `axis_d_guarantee` | 枚举 | `none` / `empirical` / `formal` / `formal-safety` |
| `axis_e_recursiveness` | 枚举 | `one-shot` / `iterative` / `full-rsi` / `co-evolution` |
| `source_url` | URL | 实际检索到的页面 URL（核验凭证） |
| `read_status` | 枚举 | `pool` / `skim` / `deep` |
| `note` | 文本 | 自由备注，`;` 内为同一备注内的分隔符 |

### ⚠️ 关于 `venue_verified`

**当前 19 篇中 4 篇为 `true`，15 篇为 `false`（2026-10-31 更新）。**

已核验的 4 条（证据见 [`../midterm/p1/venue-verification.md`](../midterm/p1/venue-verification.md)）：

- `arxiv-2310.02304` STOP — **COLM 2024（Spotlight）**，来源 COLM 2024 Accepted Papers 页
- `arxiv-2408.08435` ADAS — **ICLR 2025（Conference）**，来源 proceedings.iclr.cc 正式条目
- `arxiv-2505.22954` DGM — **ICLR 2026（Conference）**，来源 proceedings.iclr.cc 正式条目
- `arxiv-2507.21046` Gao 等综述 — **TMLR 2026**，来源 arXiv HTML 的 OpenReview 标注 + ML Anthology TMLR 2026 索引

仍为 `false` 的 15 条中，有两条**作者自述已录用但本组未取得第三方证据**，一律不升级：

- `arxiv-2606.05922` RHO — arXiv 注释自述 “Accepted to EMNLP 2026 (Findings)”
- `arxiv-2603.25681` — arXiv 注释自述 “Accepted by TMLR”

另有两条特殊情形：

- `arxiv-2504.15228` SICA — 注释写 “Submitted as a preprint to NeurIPS 2025”，**投稿不等于录用**，保持 `arXiv preprint`
- `venue-2026-dcri-survey` — **无 arXiv 版本**（题名检索 0 命中），Preprints.org 预印本，按 `venue-<年份>-<slug>` 命名

核验方法见 `AGENTS.md` §7.1。**不要根据作者或机构的过往发表记录推断会议。**
本轮 DBLP 三个入口均被人机验证拦截，改用会议官网/官方论文集，这一限制已记入 venue-verification.md §0。

> 📌 `pool.csv` 目前与 `verified.csv` 内容相同（19 条）。
> 历史上两表是同步维护的镜像；**升入 `verified.csv` 前必须完成 arXiv ID 核验**这一规则不变。
> 若后续加入未核验候选，只写 `pool.csv`，不要污染 `verified.csv`。

### ⚠️ 关于 `axis_*` 字段

这五轴是**待验证假设**，见 `AGENTS.md` §5 与 `notes/AXES.md`。

CSV 中的取值只填了摘要可支撑的部分；**未精读的论文保持为空**，不要提前填满。
空值不是遗漏，是"尚未判断"的诚实标记。

---

## `pool.csv` 字段说明

泛读候选池，结构同上但允许更松。追加时**至少**填：

`id` · `title` · `year` · `source_url` · `read_status=pool`

其余字段可在升为 skim / deep 时补齐。升入 `verified.csv` 前必须完成 arXiv ID 核验。

---

## 多值字段约定

用 **分号 `;`** 分隔，例：

```
control-flow;code
```

CSV 字段内的**逗号**必须用双引号包裹（标准 CSV 转义）：

```
"Zhang, Hu, Lu, Lange, Clune"
```

---

## Excel 打开乱码？

文件为 **UTF-8 无 BOM**。用 VS Code / Excel 均可，Excel 请在导入时显式选择"UTF-8"。
若确需 BOM，Python 侧请用 `encoding="utf-8-sig"` 读取（`scripts/fetch_pdfs.py` 已兼容）。

---

## 相关文件

- 字段规则全文：[`../AGENTS.md`](../AGENTS.md) §7
- 五轴定义：[`../notes/AXES.md`](../notes/AXES.md)
- PDF 下载脚本：[`../scripts/fetch_pdfs.py`](../scripts/fetch_pdfs.py)
