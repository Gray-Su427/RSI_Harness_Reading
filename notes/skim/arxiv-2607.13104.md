---
id: arxiv-2607.13104
title: "Self-Improvements in Modern Agentic Systems: A Survey"
authors: "Ren, Chen, Guo, et al."
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: false
org: ""
role: survey
read_status: skim
read_date: 2026-10-13
---

**一句话**：把 2023–2026 年的自我改进 agent 工作按"改模型参数还是改 scaffold"分成两条主路径，并在一个统一形式化（$A_t=(\theta_t,\Sigma_t)$）下给出分类、评测与开放方向。

**领域地图贡献**：顶层二分 **foundation model improvement（θ）** vs **scaffolding improvement（Σ）**；论文自称在此基础上"separating what is updated from where the improvement signals originate"。FM 侧三个子类：`Intrinsic Generative Demonstrations` / `Intrinsic Evaluative Feedback` / `Extrinsic Exploratory Experience`（含 `Grounded Task Environments`、`Simulated Proxy Environments`）。Scaffold 侧四个组件：`Prompt`（下分 `Scalar-Feedback Optimization` / `Qualitative-Feedback Refinement` / `Population-Based Evolution` / `Textual Gradient Optimization`）、`Memory`（`Object` / `Structure` / `Processing`）、`Tool`（`Dynamic Tool Routing` / `Iterative Tool Refinement` / `Autonomous Tool Creation`）、`Full Scaffolding`。

**关键定义**：

> where pt denotes structured prompts or system instructions, mt denotes memory mechanisms and their retrieval and update policies, Tt denotes the set of external tools together with their invocation interfaces, and gt denotes additional control logic such as routing, scheduling, or safety constraints.

> we formalize self-improvement in foundation-model-based agents (SI-FMA) as a process of persistent, endogenous adaptation.

> Foundation model improvement realizes self-improvement through self-induced learning in parameter space, whereas scaffolding improvement realizes self-improvement through direct self-modification in execution space.

术语上它明确把 scaffold 与 agent harness 对齐：

> such an operational scaffold is often also referred to as an agent harness ... while this survey uses the term scaffold to emphasize the modifiable structures surrounding the foundation model.

**递归深度的处理**：**原文未见分级**。最接近的表述有两处，都只到"二分 + 自指性"这一层：§3.2 的 "Two modes of self-reference in SI-FMA"；§6.4 的自指式 $\Sigma_{t+1}=I_{\Sigma_t}(\Sigma_t;S_t)$，注为

> IΣt highlights that the improver can evolve together with the agent it improves.

以及 Takeaway：

> Full scaffolding improvement is the category most closely related to recursive self-improvement, because it treats the agent's own source code and operational logic as mutable substrates. While achieving truly open-ended recursive self-improvement remains a grand challenge, current systems successfully operationalize this concept as bounded, verifiable loops.

**覆盖范围**：覆盖 FM 侧与 scaffold 侧全部，§6.4 `Full Scaffolding` 明确收录了 STOP、ADAS、DGM、Gödel Agent、AlphaEvolve、ShinkaEvolve、Live-SWE-Agent、Huxley-Gödel Machine、Continual Harness、Auto-Harness、AgentDevel、JudgeFlow、The Red Queen Gödel Machine——即"改程序而非改参数"的工作。安全小节专门讨论 "The Critic as Governed Infrastructure" 与 layered gating。

**对本选题的价值**：① 它给出 $\Sigma=(p,m,T,g)$ 的分解，其中 `g`（routing/scheduling/safety constraints）正是我们的 `control-flow` 轴，可作为轴定义的外部依据；② "full scaffolding = 最接近 RSI 且只做到 bounded, verifiable loops"这句，可与我们 STOP/DGM 的 E 轴结论互证；③ 它把 scaffold 与 harness 明确划等号，佐证我们选题的术语合法性。**不同点**：它的顶层轴是"参数 vs 非参数"，比我们的 A 轴粗一档；它完全没有"谁验证/闭环程度"这一轴（对应我们的 B 轴只以"信号来源"粗略触及），也没有 D 轴保证强度、E 轴递归分级。

**是否入选精读**：否——它是"广度型"框架，价值在于给我们 A/B/C 轴提供外部参照与术语，不提供可检验的机制细节；且本文的 `Full Scaffolding` 一节已可直接当索引用。

**可疑之处**：① 全文未见对"递归深度"的可操作分级，若要引它支撑 E 轴须谨慎；② 图 1/图 2 中出现 `Continual Harness`、`Harness Updating Is Not Harness Benefit` 同类工作的引用痕迹，但正文未展开，无法据此判断该综述立场；⚠️ 未核实其对 2026 年 harness 子方向工作的取舍是否系统；③ 其 signal 分类（intrinsic/extrinsic）与我们 B 轴不是同一套划分，不可直接互译。