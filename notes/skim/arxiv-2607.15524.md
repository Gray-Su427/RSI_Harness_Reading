---
id: arxiv-2607.15524
title: "Recursive Harness Self-Improvement"
authors: "Lee, Xu, Seely, Lee, Zaharia, Tang"
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: true
org: "Sakana AI + UC Berkeley"
role: harness-core
read_status: skim
read_date: 2026-10-13
---

**一句话**：提出 RHI，把 harness 表示为 agent loop 的 prompt 级规范（roles / instructions / contracts / hops），用「当前 harness 与其自身前一版」的成对比较反馈迭代精修，在 30 个合成 ML 研究任务上使 high reasoning effort 的 agent 胜过 xhigh/max/ultracode 等更强 test-time-scaling 设置，并降低至多 60% 推理成本。

**改进对象**：prompt（prompt 级 harness 规范，非可执行代码）＋控制流/多智能体编排（contracts 规定 agent 间通信，hops 决定 orchestrator–subagent workflow 的控制流）。主要贡献：**prompt 级 harness 整体的迭代精修**。（泛读初步判断，待精读确认）

**改进信号**：自偏好。作者刻意用 pairwise LLM-as-a-judge，评测提示 x_eval 只进入 evaluator、不直接提供给 harness optimizer，optimizer 只看自己历次修订诱导出的偏好历史。（泛读初步判断，待精读确认）

**搜索算子**：refine —— 原文自述以 "trajectory-local self-comparison" 取代昂贵的种群级 harness 搜索。（泛读初步判断，待精读确认）

**递归深度**：作者**明确自称** recursive self-improvement（§3.2 末），逐字原话：

> "In this sense, RHI performs recursive self-improvement: each harness is optimized using the preference history induced by its own previous revisions without directly observing the evaluation prompt 𝑥eval."

但作者同时把整体图景限定为 model–harness co-evolution，并把本工作划为该递归循环的**前半段**（§1）：

> "This work focuses on the first half of this recursive loop: for a fixed foundation model, how to improve the harness to generate higher-quality execution traces."

且结论中把后半段（把轨迹内化进未来模型）列为未来工作：

> "Future work will complete the second half of the loop by investigating how the resulting execution traces can be effectively internalized into future foundation models."

因此按本组五轴应记为 `iterative`（作者自称 recursive，但闭环的另一半未实现）；`co-evolution` 是作者用来命名「模型—harness 共演化」这一范式的名词，而非本文已完成的机制。（泛读初步判断，待精读确认）

**主要实验**：benchmark：30 个自建 synthetic、开放式机器学习研究任务（量化金融 / 机器人 / 药学），每题要求生成含标准化交付物的完整 code repository。主指标：pairwise LLM-as-a-judge 胜场（2 个 judge × 3 seeds，30 题取均值）；以更高 reasoning effort 设置 xhigh / max / ultracode 为 test-time-scaling 基线。后端：sonnet-4.6、opus-4.7、opus-4.8。结果：三者上 high+RHI 的胜场均高于对应的更强 scaling 设置；opus-4.8 上相对 ultracode 基线推理成本降低至多 60%。算力开销：**部分报告**——给了归一化 output-token 与 cache read/write 用量随迭代的曲线（sonnet-4.6 output-token 1.71→1.86 基本持平，opus-4.8 为 1.42→1.81），但搜索过程本身消耗的算力未见单独核算，⚠️ 未核实是否有总成本表。

**可复现性**：代码开源？原文未见说明（未见代码链接或开源声明）。archive 公开？未见说明（附录 B 给出单个任务上 H_x(i) 的迭代演化示例，附录 C 给出 harness optimizer 的 system/user prompt）。

**是否入选精读**：是——本组"harness 定义为 prompt 级规范"的代表，且其"只做 few-shot 迭代、不做种群搜索"的取舍与 Self-Harness（持续迭代 + 回归门控）构成可对照的两种设计；同时是争议 Q2（自偏好 vs 循环论证）的典型样本。

**可疑之处**：
1. ✅ **`industry` 字段已更正**：原文作者单位为 Sakana AI 与 UC Berkeley（Hyunin Lee 等 6 人，含 Matei Zaharia），属产学合作。`verified.csv` 与本卡片 frontmatter 原记 `industry: false`，已于 2026-10-13 按 PDF 署名改判为 `true`，`org` 补为 `Sakana AI + UC Berkeley`。这同时使 Gate 2「≥1 篇工业界或产学合作」不再依赖 venue 尚未核验的 DGM。
2. 🔴 `co-evolution` 无作者对本方法的明确界定：本篇主张的是 model–harness co-evolution 这一**范式**，并自认只完成递归循环的前半段。因此 `co-evolution` 是否只是 `iterative` 的重新包装，仍未解决（AGENTS.md §5 反例预警未消）。
3. 全部评测依赖 LLM-as-a-judge 成对比较，无可执行 verifier；且 x_eval 与被评模型同源，循环论证风险未排除 —— 直接命中 Q2。
4. 30 个任务为作者自建 synthetic 集合；「benchmark verifiability 的界定」由外部研究者协助澄清（见致谢 Hyunjoon Jung），该集合的外部效度需在精读时查证。
5. 论断 2（增益并非来自更长输出）在 opus-4.7 上被作者自己判为 inconclusive（跨度数仅 2 轮）。
6. 结论段无独立的 Limitations 小节；散见的限制声明（如单一 system-level harness 覆盖广任务分布的局限）需精读时汇总。
