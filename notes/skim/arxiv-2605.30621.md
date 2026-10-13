---
id: arxiv-2605.30621
title: "Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents"
authors: "Lin, Wu, Wang"
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: true
org: "Pennsylvania State University + UC Santa Cruz + Amazon + Emory University + UIUC + Northeastern University"
role: harness-core
read_status: skim
read_date: 2026-10-13
---

**一句话**：这篇**不提出新方法**，而是用受控的实证测量把 harness 自进化拆成两种能力——harness-updating（evolver 能否产出有用的更新）与 harness-benefit（task-solving agent 能否真正吃到更新）——并证明前者对基础能力"平"、后者对基础能力"非单调"（中档模型收益最大）。

**改进对象**：作者沿用**既有** harness 自进化协议（skills；MCP-Atlas 额外含 prompts 与 append-only memories；tools 目录与评测文件只读），自己**不发明新的改进算子**——只是把 evolver 模型与 agent 模型解耦做笛卡尔积式配对测量。因此本栏是"被测系统的改进对象"，非本文贡献对象。

**改进信号**：**失败轨迹 / 执行证据**（协议要求 evolver 从 execution evidence D_t 产出更新；具体诊断信号由被测的既有自进化系统决定，原文未指定单一机制）。本文**不使用**自偏好，也未做成本核算式诊断。

**搜索算子**：fix-solve 的多轮 solve-evolve 循环（后述），但**本文不提出新搜索算子**；文中把 meta-optimizer 式的 proposal 归给被引的既有工作。

**递归深度**：协议层面是 `iterative`（循环 T 步），但作者**未使用 "recursive self-improvement" 一词，也未对自己测量的循环做该词意义上的自我界定**。循环的原文定义（逐字照抄）：

> Starting from an initial harness H0, the protocol iterates for T steps. At each step, the agent runs on a batch of tasks, collects execution evidence, and the evolver updates the harness for the next step.

> This loop repeats for T steps, producing the final harness HT.

且作者明确把"权重不变、只改外部 harness"作为前提：**"we keep f fixed and only update editable components of Ht"**。按规则不得代作者判为 `full-rsi`。

**主要实验**：benchmark：SWE-bench Verified、MCP-Atlas、SkillsBench；7 个 LLM（agent 侧 6 个，evolver 侧多含最小的 Qwen3.5-9B），主指标 pass rate 与三个自定义量：base capability M_base(f)、harness-updating Δ_update(e)（锚定 agent 集上的平均配对增益）、harness-benefit Δ_benefit(f)（锚定 evolver 集上的最大配对增益）。关键数字：Δ_update 在任一 benchmark 上最强与最弱 evolver 相差**至多 3.1pp**，无模型跨 benchmark 全胜，Qwen3.5-9B 在 SB 上反而最高（3.8pp）；同一 agent 下七个 evolver 的跨度**至多 5.1pp**，而 Opus 与 Qwen3-235B 的基础能力差 36.0pp。Δ_benefit 非单调：SWE 上 Qwen3-235B 峰值 19.3pp，Qwen3-32B 仅 4.4pp，Opus 4.6 仅 2.6pp；MCP 上峰值移到 GPT-OSS-120B 7.0pp。弱档两种失效模式：harness activation failure（Qwen3-32B skill 加载率 0.251 vs 强档 ≈0.96）与 harness adherence failure（加载后 adherence 从 0.52 漂到 0.13，强档 0.89→0.80）。算力开销：**原文未见具体开销数字**（仅说明所有 agent–evolver 配对"share the same evolution budget β and per-task turn limit"，β 数值未在正文给出）。

**可复现性**：摘要称 "Our source code is publicly available at here."，但 PDF 抽取文本中该链接为空（超链接地址丢失）——**仓库 URL ⚠️ 未核实**。

**是否入选精读**：**是**——这是争议 Q1 的核心证据，且方法论上罕见地把"能更新"与"有收益"分别测量。若其 Δ_update 的"平坦"结论成立，则本领域大量论文的 evolver 侧创新空间有限；同时它为 E 轴提供了一个反例式的定位（明确固定权重、只改 harness）。

**可疑之处**：① **本文的 Δ_update 是否等于"选择偏差"尚未排除**——"最强 vs 最弱 evolver 只差 3.1pp"也可能来自所有 evolver 产出的 skill 都近乎同等平庸；需要读原文如何构造 evolver prompt 与初始 harness（`H0`、evolver system prompt 固定）。② evolver 与 agent 共用同一 system prompt 族，是否对 evolver 不利。③ 未评估 parametric fine-tuning（作者自述），故其结论只对"非参数 harness"成立——这与 DGM/MGM 类（改代码、不改权重）恰好重合，泛化到本方向时需说明。④ 未报算力与随机种子数。（以上为**泛读初步判断，待精读确认**。）