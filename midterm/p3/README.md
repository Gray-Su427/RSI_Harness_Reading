# P3 交付索引（边界、叙事与整合）

> 负责人：P3（szh）｜准备：2026-11-01｜**汇报日：2026-11-02（周一）**｜状态：CP3 定稿候选，Q&A 确认截止 11-02 上午
>
> 本目录只放 P3 的中期材料。论文元数据以 [`../../refs/verified.csv`](../../refs/verified.csv) 为准；五轴以 [`../../notes/AXES.md`](../../notes/AXES.md) 为准；P3 **没有**修改 CSV，也没有修改 `AXES.md`。

---

## 0. 关键时点

| 时点 | 日期 | 要做什么 |
|---|---|---|
| T−1（今天） | **2026-11-01** | 完成计时排练 ≤4:40；四人确认 Q&A（还差 6 条）；P1 处理 CSV 7 组建议 |
| T（汇报当天） | **2026-11-02（周一）** | 上午按 [`cp4-checklist.md`](cp4-checklist.md) 走一遍 CP4；只改一致性，不加内容 |
| D1 | 2026-11-03（周二） | 启动 7 篇完整 Schema 精读 |
| D1–D14 | 2026-11-03 – 11-16 | 两周：D7 七篇草稿、D9 补附录与成本、D11 交叉核对、D14 证据与争议定稿 |

> ⚠️ 课程 PPT 曾写「10 分钟报告 + 5 分钟提问」。本 deck 按你确认的 **5 分钟（≤4:40）** 做；若实际给 10 分钟，把 backup 的两页转正、每页多讲 30 秒即可，不用重做。

---

## 1. 交付物

| 文件 | 内容 | 对应 CP3 要求 | 状态 |
|---|---|---|---|
| [`narrative.md`](narrative.md) | 1 句核心结论 + 3 句叙事 + 17 条数字锚点 + 8 条禁用表述 | 3 句叙事 | ✅ 定稿候选 |
| [`deck-outline.md`](deck-outline.md) | 6 页逐页内容、计时（280 s）、逐页讲稿 | 6 页 deck 骨架 | ✅ 定稿候选 |
| [`deck-rsi-midterm.pptx`](deck-rsi-midterm.pptx) | 16:9 deck：6 页正文 + 2 页 backup，含讲稿与【论据】备注；标题 30 / 正文 12–14 | deck 成品 | ✅ 可放映 |
| [`make_deck.py`](make_deck.py) | deck 生成脚本（可复现） | 复现 | ✅ 可运行 |
| [`rho-brief.md`](rho-brief.md) | RHO 讲述级五问卡 | P3 认领论文 | ✅ 讲述级 |
| [`severa-brief.md`](severa-brief.md) | SEVerA 讲述级五问卡 | P3 认领论文 | ✅ 讲述级 |
| [`cp4-checklist.md`](cp4-checklist.md) | CP4 一致性校对清单（数字/ID/术语/计时/链接/backup） | CP4 | ✅ 待汇报当天执行 |
| [`qa-signoff.md`](qa-signoff.md) | 8 条 Q&A 确认状态；Q5/Q6 定稿；预判追问 5 条 | 8 个 Q&A | 🟡 2/8 已确认 |

**未完成 / 不在 P3 范围**：`notes/deep/` 完整 Schema（中期后）、`refs/verified.csv` 的轴字段更正（P1）、`p1`/`p2`/`p4` 正文修订（各自负责人）。

---

## 2. 五条口径（评审时先看这五条）

1. **样本是 9 篇，不是 19 篇**：7 篇精读名单 + 2 篇泛读补充（SICA、MGM）。19 篇是全池，只用于「规模 / 时效 / 可信度」三个数字。
2. **E 轴只认作者自我界定**：能落位的只有 3 篇（STOP=`iterative`、DGM=`full-rsi` 仅代码层、RHO=`one-shot`）+ SICA 候选；5 篇待精读。**不写「递归深度集中在 one-shot / iterative」**。
3. **A 轴记主值（次值）**：计数只按主值。DGM 的次值是 `tool/prompt/context`，**不含 `evaluator`**。
4. **边界工作保留，不硬归类**：AlphaEvolve（任务算法）、SEVerA（Learn 改权重）、Harness≠Benefit（测量）三篇保留并标注，不作 harness RSI 的正面证据。
5. **【原文】与【本组判断】分开**：五问卡逐条引作者原话；我们的推论与防火墙表述一律标【本组判断】。

---

## 3. 需要四人各确认一件事

| 人 | 需要确认 | 位置 |
|---|---|---|
| P1（xyc） | Q&A ①② 的定稿；§7 的 7 条 CSV 更正建议 | [`qa-signoff.md`](qa-signoff.md) §2、[`cp4-checklist.md`](cp4-checklist.md) §7 |
| P2（zyc） | Q&A ③④；deck 第 3 页图注与灰带表述 | [`deck-outline.md`](deck-outline.md) P3 |
| P3（szh） | Q&A ⑤⑥（已确认）、全文核对 | [`qa-signoff.md`](qa-signoff.md) §3 |
| P4（zgj） | Q&A ⑦⑧ 确认；复核 P3 已代改的 `plan.md` T/D1–D14、`risk.md` R1/R4、`qa.md` Q1/Q2 | [`cp4-checklist.md`](cp4-checklist.md) §7 |

> 未确认前，主讲人不得用「我们」口径；deck 第 7 页页脚已标注这一点。

---

## 4. 复现

```bash
cd midterm/p3
python make_deck.py        # 重新生成 deck-rsi-midterm.pptx（需 python-pptx + Pillow）
```

- 依赖：Python 3.10+、`python-pptx`（1.0.2 已验证）、`lxml`；中文字体 **Microsoft YaHei**。
- 图：`../p2/taxonomy-ae.png`（300 dpi，P2 生成；本目录不复制、不修改）。
- 改 deck 的顺序：先改 [`narrative.md`](narrative.md) 与 [`deck-outline.md`](deck-outline.md) → 再改 `make_deck.py` → 重跑 → 用 PowerPoint 检查 8 页。

---

## 5. 变更记录

| 日期 | 改动 | 原因 |
|---|---|---|
| 2026-11-01 | 建立本目录：叙事、6 页 deck（pptx + 脚本 + 大纲）、RHO/SEVerA 五问卡、CP4 清单、Q&A 确认表 | CP3 交付 |
| 2026-11-01 | 叙事第 2 句按 P2 口径修正（取消「递归深度集中」） | `p2/README.md` §3 口径提醒 |
| 2026-11-01 | 写入汇报日 T = 2026-11-02，D1–D14 = 11-03 – 11-16；deck 页脚与第 6 页排期同步 | T 确认 |
| 2026-11-02 | deck 可读性重排：标题 30、正文 12–14、大数字 32–34；屏幕文字减约 1/3，论据移入讲稿备注；第 3 页图放宽到 8.7 英寸 | 投影后排可读 |

---

## 6. 相关文件

- 分工与 Checkpoint：[`../../midpre-checkpoint.md`](../../midpre-checkpoint.md)
- P1 数据：[`../p1/`](../p1/)｜P2 分类：[`../p2/`](../p2/)｜P4 计划：[`../p4/`](../p4/)
- 五轴定义：[`../../notes/AXES.md`](../../notes/AXES.md)｜笔记模板：[`../../notes/TEMPLATE.md`](../../notes/TEMPLATE.md)
- 已核验论文：[`../../refs/verified.csv`](../../refs/verified.csv)
