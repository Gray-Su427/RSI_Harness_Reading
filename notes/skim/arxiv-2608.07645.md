---
id: arxiv-2608.07645
title: "Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution"
authors: "Liu, Liu, Yan, Tresp, Ma"
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: false
org: ""
role: harness-core
read_status: skim
read_date: 2026-10-13
---

**一句话**：在 DGM/HGM 的 archive 树搜索框架上，把"单条失败轨迹"驱动的自我修改拆成三个算子——clonal mutation、reaction-norm mutation（用同一 agent 在多任务上的轨迹做对比）、cross-lineage hybridization（用另一 lineage 的 agent 在同一任务上的轨迹做对比）——并声称在相同预算下比 HGM 收敛更好。

**改进对象**：**代码**（agent scaffold 的源码本体，主要贡献）；改进的**不是参数也不是数据**。三个算子都直接消费 archive 里已有的 trajectory，不新增评估。

**改进信号**：**失败轨迹**（ΦCM 用单条失败；ΦRM 用多任务轨迹对比以区分 genotype 缺陷与任务偶然；ΦCH 用跨 lineage 同任务轨迹对比）+ **外部验证**（r(a,τ) ∈ {0,1} 来自 benchmark 通过与否）。

**搜索算子**：**evolutionary**（archive lineage tree + Thompson sampling 决定评估/扩展预算分配 + 加权采样选择三个突变算子）。

**递归深度**：`iterative`（archive 树上反复展开）——但作者**未给出"本工作是否构成 recursive self-improvement"的显式自我界定**。原文最接近的两处（逐字照抄）：

> Self-improving coding agents that iteratively rewrite their own source code have demonstrated impressive performance on coding tasks.

> Since recursive self-improvement ultimately edits the agent's own codebase, it is tempting to view self-evolution as another coding task.

第二句出自附录 F.2，是**作者在反驳一个直觉**，不是自我声明。按 AGENTS.md 第 5 节规则，此处不得代作者拔高。

**主要实验**：benchmark：SWE-bench Verified-60、Polyglot-60（另测 SWE-bench Pro / Multilingual 做迁移）；主指标 pass rate。200 次 φ-evaluations + 24 次 Φ-expansions，backbone Qwen3.6-35B-A3B，同预算同初始 scaffold：SWE-bench Verified 68.3→**78.3**（HGM 73.3）；Polyglot 50.8→**93.2**（HGM 77.9）。迁移：Qwen 上evolve的 scaffold 到 DeepSeek 平均 70.8%（HGM 65.0%，初始 47.5%）；Polyglot-60→SWE-bench Pro 26.7%（HGM 13.3%）。消融：w/o ΦRM 79.7，w/o ΦCH 74.6。基线：HGM、DGM（模拟中）、oracle。算力开销：**报告了**（CPU wall-clock 96.11h / 40.14h，8×NVIDIA H100；另有 Figure 6 的 token 成本分布）。理论侧给出 additive fitness landscape 下的 Proposition 1（ΦRM/ΦCH 的 effective fix probability 严格高于 ΦCM），但该结论依赖"比较证据是 sound 的"这一假设。

**可复现性**：代码开源（`https://github.com/RealLcz/MGM`，项目页 `https://reallcz.github.io/MGM/`）；**archive 是否公开，原文未见说明**。

**是否入选精读**：**是**——它是 DGM/HGM 家族里少数明确把 archive 的"证据利用率"当作一等研究对象的 2026 工作，与 DGM/MGM 作者团队不重叠，可作独立证据（见 `refs/verified.csv` note）；且同时具备形式化命题 + 消融 + 迁移实验，适合支撑"harness 自进化的增益来自何处"这一争议。

**可疑之处**：① 标题用 "Recursive Self-Improving"，但正文只在附录 F.2 顺带提到该词，**未说明本文相对 DGM 在递归深度上有何增量**——需查证作者是否认为改进了"改进器本身"。② 迁移实验把 60-task subset 上的优势外推到完整 Polyglot-225（96.89%），subset 选择的代表性质疑。③ Proposition 1 依赖 sound comparative evidence 的假设，该假设在真实 LLM editor 上不可检验。④ 原文自述 seed 多样性有限（"limited seed diversity leave residual uncertainty"），主实验未报告随机重启方差。（以上均为**泛读初步判断，待精读确认**。）