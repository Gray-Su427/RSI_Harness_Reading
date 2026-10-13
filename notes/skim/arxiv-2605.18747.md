---
id: arxiv-2605.18747
title: "Code as Agent Harness"
authors: "Ning, Tieu, Fu, et al."
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: true
org: "University of Illinois Urbana-Champaign + Meta + Stanford University"
role: harness-core
read_status: skim
read_date: 2026-10-13
---

**一句话**：综述与立场文，提出「code as agent harness」这一统一视角——把 code 从「agent 生成的产物」重构为 agent 的运行基底（可执行、可验证、有状态），并围绕 harness interface / harness mechanisms / scaling harness 三层给出分类与五个应用域。

**改进对象**：本篇为综述，**不提出自己的改进方法**，故不填 A 轴取值。其贡献在于**定义 A 轴的取值空间**：harness interface（code for reasoning / acting / environment modeling）、harness mechanisms（planning、memory、tool use、feedback-driven control 与 optimization）、scaling harness（多 agent 共享 code 产物）。（分类参照，非本篇判断。泛读初步判断，待精读确认）

**改进信号**：未找到——本文不做实验，仅在 §5.2.3 讨论 harness 变异应带的 "change contract"（须声明目标失败模式、预测收益、须保持的不变量、可证伪的评测、回滚方式）。

**搜索算子**：未找到——同上，本文不提出搜索算法。

**递归深度**：**未找到作者自我界定**（本文是综述，不主张自身构成 recursive self-improvement，也未对"何种 harness 演进算 full-rsi"给出界定）。但 §5.2.3 "Self-Evolving Harnesses without Regression" 一节对该问题有定性表述，逐字原话：

> "The harder problem is whether a harness can improve itself without overfitting, weakening safety, increasing cost, hiding failures, or regressing on rare but important tasks."

> "The goal is not a harness that changes often, but one that changes only when it can justify the change."

**主要实验**：无。本文为 survey，全文无自建 benchmark、无主指标、无基线。（泛读初步判断，待精读确认）

**可复现性**：本文无代码与实验。作者提供一个持续维护的论文清单仓库：`https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers`（摘要页脚）。该仓库可作为后续扩充论文池的来源，但本次未打开核对。

**是否入选精读**：否——无方法、无实验，属概念框架长文，泛读已足够交代其框架定义与分类结构。**但不可作为证据**：其价值在于为 A 轴提供定义与分类参照，以及 §5.2.3 的论述可直接用于本组 Q1/Q4。

**可疑之处**：
1. 作者数与规模：原文列出 52 位作者（UIUC / Meta / Stanford），远超给定元数据所写的 "42 位作者" 与 `et al.`；⚠️ 未核实具体人数口径，本次未改动 CSV。
2. 全文自述贡献为三条（conceptual framing / taxonomy and synthesis / applications and future agenda），无任何实验性主张，故 A/B/C/D 四轴均无法从本文取值——**若精读把它当作 harness 自进化的例证会误用**。
3. §5.2.3 点名的 harness 自进化工作（AutoHarness、MetaHarness、Agentic Harness Engineering，以及优化 prompt/context/workflow 的一批工作）**不在本项目现有 verified.csv 中**，是下一步扩充论文池的候选来源。
4. 该节同时主张 "separating improvements in the harness from improvements in the base model"，与本项目争议 Q1 同向，可作为二手支撑引用，但按 AGENTS.md §7.3 不得作主要证据。
5. `venue_verified` 为 false；UIUC/Meta/Stanford 联合投稿，是否已有会议版本 ⚠️ 未核实。
