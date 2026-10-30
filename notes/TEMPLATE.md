# 精读笔记 Schema 模板

复制本文件到 `notes/deep/<id>.md` 后填写。**文件名 = `<id>.md`，`<id>` = CSV 中的 `id` 字段。**

🔴 = 必填。字段缺失的笔记**不允许**进入分类归纳。

---

## 完整模板

````markdown
---
id: arxiv-XXXX.XXXXX              # 🔴 主键，与文件名一致
title: ""                         # 🔴 原文标题，不要翻译
authors: ["", "", ""]             # 🔴 前 3 位 + et al.
year: 2026                        # 🔴
venue: "arXiv preprint"           # 🔴 已录用则填会议全称
venue_verified: false             # 🔴 true 仅当经 DBLP/OpenReview/会议官网确认
venue_verified_source: ""         # 核验来源 URL
industry: false                   # 🔴 true 则 org 必填
org: ""                           # 🔴 机构
code_url: ""                      # 代码仓库，无则留空并注明"未公开"
read_status: deep                 # 🔴 skim | deep
read_date: 2026-XX-XX

# ── 五轴分类（取值见 ../notes/AXES.md）──
axis_a_object: []                 # 🔴 prompt|control-flow|code|tool|memory|evaluator|context
axis_b_signal: []                 # 🔴 self-preference|external-verifier|human|failure-trajectory
axis_c_search: []                 # 🔴 refine|evolutionary|textual-gradient|tree-search|meta-optimizer
axis_d_guarantee: ""              # 🔴 none|empirical|formal|formal-safety
axis_e_recursiveness: ""          # 🔴 one-shot|iterative|full-rsi|co-evolution（须引作者原话）

# ── 证据强度 ──
has_baseline_comparison: false    # 🔴 是否有强 baseline 对照
reports_compute_cost: false       # 🔴 是否报告搜索算力开销
reproducible: unknown             # true|false|unknown
---

## 1. 一句话贡献
用一句中文说清它做了什么，不含评价。

## 2. 问题设定与 harness 定义
【原文】作者如何定义被改进的对象？边界画在哪里？
【本组判断】这个定义是否覆盖了"产生下一次改进的程序"？

## 3. 改进对象与更新算子
- 改什么：
- 更新算子的形式：
- 谁来提出改动（同一个模型？另一个模型？人类？）：

## 4. 验证信号与搜索机制
- 信号从哪来：
- 搜索空间有多大：
- **如何防止好运气被当成改进？**（关键，务必回答）

## 5. 实验设置与主要结果
- benchmark：
- 基线：          ← **特别注意基线是否同算力**
- 主结果：
- 算力开销：      ← 若论文未报告，写"未报告"
- 最重要的消融：

## 6. 局限与作者自述风险
【原文】作者自己承认了什么？
如有"这不算完整 RSI"之类声明，**原文照抄**，不要转述。

## 7. 本组评注
- 可信度：高 / 中 / 低，理由
- 可复现性：
- 与工业实践的距离：

## 8. 与其他论文的关系
列出具体的 ID，并标明关系类型：

| 关系 | 论文 ID | 说明 |
|---|---|---|
| 前驱 | | |
| 同族 | | |
| 支持 | | |
| 反驳 | | |

## 9. 待核实项
读完仍不确定、下一轮要查的问题。
````

---

## 字段填写要点

### `venue_verified`

**只在实际查证过之后才填 `true`。** 核验渠道优先级：

1. [OpenReview](https://openreview.net/) — ICLR / NeurIPS 录用状态
2. [DBLP](https://dblp.org/) — 最广的 CS 会议覆盖
3. 会议官网 accepted papers 列表

**禁止**根据作者或机构的过往发表记录推断会议。

### `axis_e_recursiveness`

**本项目最关键、也最容易出错的字段。**

必须引用**作者自己的界定**。典型的坑：

> STOP 的作者**明确声明**"由于语言模型未被改变，这不属于完整的递归自我改进"。
> 但该文在后续文献中常被归入 RSI。
> → 照抄作者的限定，**不得**因为它常被归入 RSI 就拔高。

若论文中找不到作者的自我界定，写 `unknown` 并记入第 9 节，**不要**替作者下结论。

### `reports_compute_cost`

设为必填是为了强制思考**争议 Q3（成本核算缺失）**：

> 报告的自我改进增益，是否扣除了搜索算力？同等算力下的简单基线能否追平？

若论文只报告最终性能、不报告搜索开销，填 `false` —— 这个 `false` 本身就是一条证据。

### `has_baseline_comparison`

若基线是"默认脚手架"而非"同算力下的强搜索方法"，填 `false`。
追问自己：**作者是否与一个公平的对手比较过？**

---

## 相关文件

- 分类轴取值：[`AXES.md`](AXES.md)
- 完整工作契约：[`../AGENTS.md`](../AGENTS.md)
- 泛读流程：[`README.md`](README.md)
