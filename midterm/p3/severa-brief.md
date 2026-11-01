# P3 · SEVerA 讲述级五问卡

> 负责人：P3（szh）｜日期：2026-11-01｜论文：`arxiv-2603.25111`｜状态：**讲述级，不是完整 Schema**
> 依据：[`../../notes/skim/arxiv-2603.25111.md`](../../notes/skim/arxiv-2603.25111.md)（2026-10-13 泛读卡，原话已回查 PDF）+ [`../p2/classification.md`](../p2/classification.md) ⑥
> ⚠️ **标题更正**：arXiv v3（2026-10-15）实为 **"SEVerA: Verified Synthesis of Self-Evolving Agents"**，旧卡写的 "Verified Self-Evolving Agents" 已过时（P1 已在 `verified.csv` 更正）。deck 与报告一律用新标题。

---

## 问 1 · 一句话贡献

**用一阶逻辑给每次生成模型调用声明局部 contract（FGGM），把底层模型包进带已验证 fallback 的 rejection sampler，再据此构造 Search / Verify / Learn 三阶段，使自进化 agent 程序在任意输入、任意参数取值下满足行为规格。**

【原文】Theorem 5.4（soundness）：「any agent returned satisfies the behavioral specification for all inputs and all parameter values」。

【原文】四类任务零违规：HumanEvalDafny **97.0%**（最佳基线 86.9%）、GSM-Symbolic **66.0%**（最佳 constrained-decoding 44.7%）、τ²-bench airline **52.6%**（Qwen3-8B）、constrained symbolic regression。

## 问 2 · 改什么（A 轴）

`code`（主）｜`control-flow`（次）。

【本组判断】**Search 改程序结构，Learn 用 GRPO 微调嵌入模型的权重**——后半段跨界到模型层。所以它**不能整体算作 harness 更新**，在 deck 里按"跨界对照"讲，与 AlphaEvolve 的"任务算法对照"、Harness≠Benefit 的"测量对照"并列。

## 问 3 · 凭什么改（B 轴）

`external-verifier`，且是**形式化验证器**（Dafny 内建 verifier），不是 benchmark 分数。

【原文】硬约束 (Φ, Ψ) 由用户以一阶逻辑给出；grader 不参与选择，只由 soft loss L 在数据集 D 上排序候选。搜索算子是 CEGIS 循环（planner 提案 → verify → 失败则回传错误信息）。

## 问 4 · 递归到哪一层（E 轴，作者原话）

`unknown` / **待精读**。

【原文】全文**未出现** "recursive self-improvement" 的自我声明；最接近的是框架图对闭环的描述：「After tuning, SEVerA maintains a pool of verified fine-tuned agents and uses their execution traces on D to generate new candidates via step (1).」

【本组判断】作者自称 "self-evolving"，指的是"程序被合成 + 参数被微调"，**是否满足本组 RSI 定义（改进产物参与下一轮改进）原文未界定**。按 `AGENTS.md` §9.4，这里只能记 `unknown`，不因循环结构升格为 `full-rsi` 或 `iterative`。

## 问 5 · 最可疑的一点

【本组判断】**"零违规"有一半来自问题设定，而不是方法本身**：

1. **规格是人先给的**（退款政策、符号界、AST 等价）。没有用户规格的域完全落空——所以它是"给定规格下的正确性"，不是"安全性"。
2. **资源无感知**——作者自陈（逐字）：「One current limitation is that the formulation is resource-unaware: behavioral specifications constrain functional correctness but do not account for computational resources such as LLM calls, token usage, or wall-clock budget.」→ 这正是 Q3（成本核算）在形式化工作里的对应缺口。
3. **代价是真实的**：「a modest 1.9–2.5× slowdown relative to the LLM baseline」，全管线 18.2 s/instance。作者同时反驳"约束有代价"的直觉（约束反而剪枝、提升质量），两种说法需要精读时对齐实验条件。
4. **τ²-bench 的对比有跨规模混淆**：Qwen3-8B 对 Agent-C + Claude Sonnet 4.5。
5. **代码链接未核实**：原文称 "The code is available on github."，但抽取文本丢失了具体 URL；`reproducible` 应记 `unknown`，不能写 `true`。

## 给 deck 的一句话

**SEVerA 是目前唯一给出形式化保证的工作，但它的保证是"给定规格下的功能正确性"，作者自己写明：不覆盖 LLM 调用、token 与时间预算。**

## 汇报时不要说

- ❌「SEVerA 解决了自进化 agent 的安全问题」——只覆盖功能规格，且规格由人给。
- ❌「SEVerA 是 harness 自进化」——Learn 阶段改权重，属模型层。
- ❌「零违规说明它更安全」——零违规是"满足规格"，不是"没有风险"。

## 精读要补的三件事

1. Theorem 5.4 的归纳范围：训练分布 vs 任意参数，是否真的对"所有参数取值"成立。
2. 代码 URL 与 license（本轮未核实）。
3. Learn 阶段的 GRPO 更新是否仍受 contract 保护（原文称 "for all parameter values"，需看证明细节）。
