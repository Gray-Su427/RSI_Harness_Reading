---
id: arxiv-2603.25681
title: "Self-Improvement of Large Language Models: A Technical Overview and Future Outlook"
authors: "Yang, Xerri, Park, et al."
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: false
org: ""
role: survey
read_status: skim
read_date: 2026-10-13
---

**一句话**：这篇综述用**系统级（system-level）**视角把 LLM self-improvement 建模为闭环生命周期 **Data Acquisition → Data Selection → Model Optimization → Inference Refinement**，外加贯穿全程的 **Autonomous Evaluation** 层，逐阶段（§2–§6）组织既有技术，并在 §7–§10 讨论挑战、风险、应用与展望。

**领域地图贡献**：主轴是**生命周期五阶段**，而非改进对象。关键的二次分类：§4 Model Optimization 三范式 `Direct Optimization` / `Self-Generated Optimization (SGO)` / `Self-Evolving Optimization`（递进轴，对我们最有用）；§5 Inference Refinement 四类（Figure 7）`Decoding Strategies` / `Reasoning-Based Improvement` / **`Agentic System-Based Improvement`** / `Test-Time Training`；§5.4 再分四子类 **Prompts / Memory / Tooling / Workflow and System Evolution**——我们的 harness 工作全部落在最后一类。

**关键定义**（§1，逐字）：

> We define self-improvement of LLMs as a learning paradigm in which a model iteratively enhances its own capabilities without continuous human-in-the-loop supervision.

> **Autonomy**: ... "Self" does not imply the absence of external components; auxiliary modules such as teacher models, verifiers, critics, reward models, or automated evaluators may still be used. The key requirement is that the learning loop itself is fully automated once deployed. **Continuity**: self-improvement is not a one-off refinement. It is an iterative, self-reinforcing process in which outputs or experiences from earlier stages are reused to generate stronger supervision signals for subsequent updates.

harness / 编排改进被明确放在 **Self-Evolving Optimization** 一档：

> Self-evolving optimization goes beyond updating the model's parameters: the very algorithm that performs the update is itself improved, together with the architecture and agent-level scaffolding, thereby extending the unit of improvement from a single model's weights to the whole agentic system.

> This enables test-time self-improvement not by altering the model's internal generation dynamics, but by evolving the system that governs how and where reasoning occurs.

**风险分类**：§8 / Figure 11 四维（逐字）：`(i) Loss of Control`（含 oversight loss、deceptive alignment）、`(ii) High-Stakes Harm`（individual harm、systemic failure）、`(iii) Social and Ethical Risks`（social disruption、ethical breakdown）、`(iv) Misuse Risks`（unintended damage、deliberate misuse）。**这是通用 LLM 安全分类，不是 harness 风险分类。** 其中对我们最有攻击性的一句：

> An evaluation that reads as safe therefore cannot certify that the self-improvement system is actually safe.

**覆盖范围**：**明确覆盖 harness / 编排控制流**。§5.4.4「Workflow and System Evolution」逐字举出 **MASS、ADAS (Hu et al., 2025c)、AFlow (Zhang et al., 2025e)、AgentSquare、Darwin Gödel Machine**，机制为 "evolutionary searches over populations of archived workflows or a search over the space of agent programs"；§4.4 另举 Gödel Agent、Huxley-Gödel Machine、ASL、SAGE、EvolveR、Agent-R1；§5.4.1 Prompts 覆盖 EvoPrompt、AlphaEvolve、ProRefine。该子节称这一族 "generally do not allow for self-evolution during inference"，任务分布大变需重开优化阶段——**这是对本方向的直接争议材料**。§5.4.4 末提到 HyperAgents 把 task agent 与 meta agent 合并为单一可自修改程序，使系统 "improves not only its task performance but also its own ability to improve itself"——**最接近 E 轴 `full-rsi` 的表述，但作者未设为独立分类维度**。

**对本选题的价值**：它提供**现成的上位坐标系**——轴 A 可定位为 §5.4.1–§5.4.4 四子类；轴 E 可定位为 §4.2/§4.3/§4.4 三范式递进，作者原话即 "the unit of improvement grows from a single set of weights to an entire agentic system"。最关键的边界判断是作者**显式对置模型路线与 agent 路线**：

> model self-improvement mainly focuses on improving the model's internal capabilities through data, optimization, and refinement, whereas self-evolving agents emphasize interactive systems that use tools, environments, memory, and feedback to adapt their behavior over time. Therefore, agent-based self-improvement is most naturally connected to inference-time improvement.

即**本综述主体（§2–§6）是"改参数"路线，harness 自进化只是 §5.4.4 的一个子类**——这正是我们把 harness 单列为第三轴时最该引用的边界声明。成熟度判断亦可引："self-evolving optimization, though the most open-ended, is still the least mature."

**是否入选精读**：否（作为综述）；但 §4.4、§5.4.4 是**逐篇抽取 harness 工作清单**的高价值来源，且直接支撑本综述"为何单列 harness 轴"的论证。

**可疑之处**：🔴 **venue 存疑（需下一轮联网核验）**——txt 每页页眉均写 "Published in Transactions on Machine Learning Research (09/2026)"，并给出 OpenReview 链接 `https://openreview.net/forum?id=7Sc51w6mIC`；本轮按规则仍记 `arXiv preprint` / `venue_verified: false`，但很可能是已录用 TMLR，下次核验优先查该 forum。⚠️ 未核实——页眉写法是否可能为模板残留，本轮不做判断；§5.4.4 表格（含 ADAS、AFlow、AlphaEvolve 等行，列含义未读）能否用于方法比较；§4.5.1 与 §7 含成本讨论（"the marginal cost of each additional unit of improvement keeps rising"），**与争议 Q3 直接相关但本轮未精读**，需下一轮确认是否给出可引成本口径；作者对"递归深度"无正式分类轴，勿把我们的 E 轴说成它的分类。
