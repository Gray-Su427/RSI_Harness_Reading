---
id: arxiv-2603.25111
title: "SEVerA: Verified Self-Evolving Agents"
authors: "Banerjee, Xu, Ie, Zhang, Peng, Lin, Singh"
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: true
org: "University of Illinois Urbana-Champaign + Google"
role: harness-core
read_status: skim
read_date: 2026-10-13
---

**一句话**：提出 FGGM（Formally Guarded Generative Models）——用一阶逻辑为每次生成模型调用声明局部 contract，并把底层模型包进带**已验证 fallback** 的 rejection sampler；据此构造 SEVerA 三阶段框架（Search / Verify / Learn），使自进化 agent 程序在**任意输入、任意参数取值**下满足行为规格。

**改进对象**：**代码 + 参数**（planner LLM 合成 parametric agent program；Learn 阶段再用 GRPO 类梯度方法微调其中嵌入的模型参数）。注意：本文改的是"agent 程序本体 + 模型权重"，不是本文方向严格意义上的 harness/scaffold 层——但它正是本方向轴 A 中 `code` 值的极端形态。

**改进信号**：**外部验证**，且是**形式化验证器**（Dafny 内建 verifier）而非 benchmark 分数。硬约束 (Φ, Ψ) 由用户以一阶逻辑给出；grader 不参与选择，只由 soft loss L 在数据集 D 上排序候选。

**搜索算子**：**tree-search / CEGIS 循环**（planner LLM 提案 → verify → 失败则回传错误信息给 planner）+ 外部 meta-optimizer（Learn 阶段的 GRPO 类梯度优化）。合成侧的算子是 CEGIS，不是种群进化。

**保证具体是什么**：Theorem 5.4 soundness——"any agent returned satisfies the behavioral specification for all inputs and all parameter values"；Theorem 5.5 给出充分条件：存在被验证的 agent 满足硬约束且 task loss 不大于任何**用初始参数**的无约束生成模型，并在无约束模型违反规格时严格改进。四类任务实测零违规：HumanEvalDafny 97.0%（最佳基线 86.9%）、GSM-Symbolic 66.0%（最佳 constrained-decoding 基线 44.7%）、τ²-bench airline 52.6%（Qwen3-8B；文中称超过用 Claude Sonnet 4.5 的 Agent-C）、constrained symbolic regression。

**代价（trade-off）**：原文明确写了三点。① 时间开销："on Dafny and GSM-Symbolic the full pipeline introduces a modest 1.9–2.5× slowdown relative to the LLM baseline, attributable to the verification and rejection-sampling steps"；全文管线"takes 18.2 s per instance"；在 τ²-bench 上反而快于 Agent-C。② 作者**反驳了"约束有代价"的直觉**："formal behavioral constraints not only guarantee correctness but also prune the space of candidate programs, steering synthesis toward higher-quality agents"。③ 作者自陈的**局限是资源无感知**（逐字照抄）：

> One current limitation is that the formulation is resource-unaware: behavioral specifications constrain functional correctness but do not account for computational resources such as LLM calls, token usage, or wall-clock budget.

即保证只覆盖**功能正确性**，不覆盖**计算成本**。这正是争议 Q3（成本核算）在形式化工作里的对应缺口。

**递归深度**：**未找到作者自我界定**——全文未出现 "recursive self-improvement" 的自我声明。最接近的是框架图对闭环的描述（逐字照抄）：

> After tuning, SEVerA maintains a pool of verified fine-tuned agents and uses their execution traces on D to generate new candidates via step (1). All agents in the pool are valid candidate solutions, and the one with the lowest L on D is returned.

以及自陈定位："We introduce SEVerA: the first self-evolving agent synthesis algorithm with verifiable guarantees."——注意这里的 "self-evolving" 指"程序被合成 + 参数被微调"，**是否满足本项目的 RSI 定义（改进产物参与下一轮改进）原文未界定**，不得代为判定。

**主要实验**：benchmark：constrained symbolic regression、Dafny 不变量生成、GSM-Symbolic、τ²-bench（policy-compliant agentic tool use）。主指标：task 效用 + **constraint violations 计数（全为 0）**。基线：无约束自进化框架、最佳 constrained-decoding 方法、PySR、LLM-SR、Agent-C。算力开销：**报告了**（1.9–2.5× slowdown、18.2 s/instance）。

**可复现性**：论文称 "The code is available on github."，抽取文本中同样**丢失了具体 URL —— ⚠️ 未核实**。规格语言 Dafny 公开，理论上第三方可复现。

**是否入选精读**：**是**——它是本方向唯一提供 `formal`（甚至 `formal-safety`）保证的工作，是轴 D 上端唯一的例证；其"零违规 + 不降性能"的说法若成立，会重新定义 Q4（可控性与爆炸半径）的争论基线；且其"保证不覆盖计算成本"的自我限定可直接用于 Q3。

**可疑之处**：① 与本选题的**契合度存疑**：Learn 阶段改的是**模型权重**（GRPO），按课程三分法更接近"模型自进化"而非"harness 自进化"；Search 阶段改的才是程序结构。需在精读中明确它究竟归属哪一轴，或作为跨界对照。② 形式化规格由**人先验给出**（退款政策、符号界、AST 等价），因此"零违规"部分来自问题设定而非方法；不含用户规格的域完全落空。③ 闭环是 CEGIS 外循环，但每次重合成都重新走完整验证，L=`Learn` 阶段的参数更新是否受 contract 保护原文说是（"for all parameter values"），但 induction 范围（训练分布 vs 任意参数）需查 Theorem 5.4 全文。④ τ²-bench airline 用 Qwen3-8B 对比"Agent-C + Claude Sonnet 4.5"的对比有跨规模混淆。（以上为**泛读初步判断，待精读确认**。）