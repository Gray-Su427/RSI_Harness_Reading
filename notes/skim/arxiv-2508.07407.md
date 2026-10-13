---
id: arxiv-2508.07407
title: "A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems"
authors: "Fang, Peng, Zhang, et al."
year: 2025
venue: "arXiv preprint"
venue_verified: false
industry: false
org: ""
role: survey
read_status: skim
read_date: 2026-10-13
---

**一句话**：提出一个由 `System Inputs / Agent System / Environment / Optimisers` 四要素构成的统一反馈循环框架，系统综述单 agent、多 agent 与领域特化的 agent 进化优化技术，并附评测与安全讨论。

**领域地图贡献**：两条正交的分类线。①**范式演进线（Table 1，四段）**：`MOP (Model Offline Pretraining)` → `MOA (Model Online Adaptation)` → `MAO (Multi-Agent Orchestration)` → `MASE (Multi-Agent Self-Evolving)`，作者说这条线"steadily reduced the degree of manual configuration"。②**技术方向线（Figure 2，三分）**：`Single-Agent Optimisation` / `Multi-Agent Optimisation` / `Domain-specific Optimisation`。优化器本身被形式化为二元组 `(S, H)`：

> (1) search space (S): This defines the set of agent configurations that can be explored and optimised. ... (2) optimisation algorithm (H): This specifies the strategy used to explore S and select or generate candidate configurations.

**关键定义**：

> Self-evolving AI agents are autonomous systems that continuously and systematically optimise their internal components through interaction with environments, with the goal of adapting to changing tasks, contexts and resources while preserving safety and enhancing performance.

> Three Laws of Self-Evolving AI Agents — I. Endure (Safety Adaptation) ... II. Excel (Performance Preservation) ... III. Evolve (Autonomous Evolution)

另给出 MAS 与 agent topology 的定义（topology 即 "the structural configuration that defines how agents are connected and communicate within the system"）。

**递归深度的处理**：**原文未见分级**。它有一条 MOP→MOA→MAO→MASE 的四段"人工配置度递减"轴，但那是**自主性/工程化程度**的时间轴，不是"改进产物是否参与下一轮改进"的递归深度轴。全文未出现对 recursive self-improvement 的分级讨论（"recursi" 一词仅出现于无关的 "recursive summarisation"）。

**覆盖范围**：改进对象覆盖 LLM、prompt、memory、tool、workflow/topology、agent 间 communication。§5 `Multi-Agent Optimisation` 明确把编排控制流当作搜索对象：

> This evolution reframes workflow design as a search problem over three interconnected spaces: the structural space of possible agent topologies, the semantic space of agent roles and instructions, and the capability space of LLM backbones.

§5 沿四个维度推进：手工设计 → prompt-level（固定拓扑下） → topology optimisation → unified → LLM-backbone optimisation；Figure 6 给出优化空间（`Text / Code / Graph / Distribution`）、方法（`LLM / Tree Search / RL / Gradient`）、目标（`Accuracy / Efficiency / Safety`）。列入的编排类工作含 ADAS、AFlow、ScoreFlow、MAS-GPT、AutoFlow、MaAS 等。**它通篇不使用 scaffold / harness 作为术语**（"Harnessing" 只出现在参考文献题名里）。

**对本选题的价值**：① 它的 MOP→MAO→MASE 轴给我们的 A 轴提供了"人工配置度"这一正交维度——同一个改进对象可以处在不同自主性档位；② `(S, H)` 分解提示我们的 A 轴（改什么）与 C 轴（怎么搜）最好正交使用，与我们的轴设计一致；③ `Three Laws` 为我们的 D 轴（保证强度）提供了一个规范表述，但它只规定"应当"，不提供分类取值，无法直接落表；④ 它印证 `Multi-Agent Optimisation` 已是独立成熟子领域，可作为我们 harness 自进化选题的上游脉络。

**是否入选精读**：否——它对 harness 只作"workflow/topology 是可优化对象"的组件级处理，没有任何以 harness 为中心的话语，也没有信号独立性/成本核算的讨论，作为领域地图足够，作为分类框架不够锐利。

**可疑之处**：① 它把并发工作 Gao et al. (2025b) 的 "what/when/how to evolve" 三维列为对照，说明该领域已有至少两套并行框架，我们若采用五轴需说明为何不并轴；⚠️ 未核实 Gao et al. 2025b 的具体内容；② 该综述 v2 时间为 2025-08，**2026 年的 harness 子方向工作几乎不可能被覆盖**，引用它时须标注这一时间边界；⚠️ 未核实其对 AlphaEvolve / DGM 类工作的处理深度。