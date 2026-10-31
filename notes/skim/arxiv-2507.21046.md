---
id: arxiv-2507.21046
title: "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence"
authors: "Gao, Geng, Hua, et al."
year: 2025
venue: "TMLR 2026"
venue_verified: true
industry: false
org: "Carnegie Mellon University + Shanghai Jiao Tong University + Princeton University + Tsinghua University 等 16 家"
role: survey
read_status: skim
read_date: 2026-10-31
---

> **来源**：[arXiv 摘要](https://arxiv.org/abs/2507.21046) · [HTML 全文 v4](https://arxiv.org/html/2507.21046v4) · [ML Anthology / TMLR 记录](https://mlanthology.org/tmlr/2026/gao2026tmlr-survey/) · [OpenReview](https://openreview.net/forum?id=CTr3bovS5F)。
> 查阅版本：v4（2026-01-16）。访问日期：2026-10-31。
> 课程 PPT 把本篇列为 2026 年种子综述；实为 **arXiv 2025-07 首发、TMLR 2026（01/2026）发表**，年份按 arXiv 记 2025。

**一句话**：以「改什么（what）/ 何时改（when）/ 怎么改（how）/ 在哪改（where）」四问搭一套自进化 agent 的分类框架，并单列评测体系（adaptivity / retention / generalization / efficiency / safety 与 static / short-horizon / long-horizon 三档），覆盖 2022–2025 的代表性系统。

**领域地图贡献**：

1. **形式化定义 agent system**（§2.1）：

> We define a (multi-)agent system as Π = (Γ, {ψ_i}, {C_i}, {W_i}). The architecture Γ determines the control flow of the agent system or collaborative structures between multiple agents. It is typically represented as a sequence of nodes (N_1, N_2, …) organized by graph or code structures.

其中 `ψ_i` 是底层 LLM/MLLM、`C_i` 是上下文（prompt `P_i` 与 memory `M_i`）、`W_i` 是工具/API 集合，策略 `θ_i = (ψ_i, C_i)`。**这条定义把「控制流 + prompt + memory + tools」拆成了四个可分别寻址的字段**，与我们的 A 轴（prompt / control-flow / tool / memory）几乎一一对应，是本组五轴最直接的外部对照。

2. **四维分类**（Figure 2 / Figure 3）：
   - What：model（policy、experience）、context（memory、prompt）、tools（发现与创建、迭代精炼、管理选择）、architecture（单 agent 的 LLM-invoking node 与 autonomous-agent 优化；多 agent 的 workflow 与 multi-autonomous-agent 优化）。
   - When：intra-test-time（ICL / SFT / RL）与 inter-test-time（ICL / SFT / RL）。
   - How：reward-based（textual feedback、internal / external / implicit reward）、imitation & demonstration、population-based / evolutionary；横切维度为 online/offline、on/off-policy、reward granularity。
   - Where：通用域（memory mechanism、**model-agent co-evolution**、curriculum-driven training）与专用域（coding、GUI、finance、medical、education）。

3. **把「自主性的位置」当作定义标准**（§1）：

> we define self-evolution not merely by the algorithms used, but by the locus of autonomy.

这是一个与我们 E 轴不同但可对话的判据：它问「谁在决定更新」，我们问「改进产物是否参与下一轮改进」。**两者不可互相替代**，精读时需在笔记第 9 节记录这一口径差。

**改进对象**：作为综述，它覆盖 A 轴全部七值中的六类（prompt / control-flow / code / tool / memory / context），但**不把 evaluator 单列**——评测在 §7 被处理成「度量自进化的外部标尺」，而不是「可被自进化的对象」。这是我们 D/B 轴（验证信号独立性）和它的一处结构性缺口。

**改进信号**：§5.1 把信号分为 textual feedback 与 scalar reward（internal / external / implicit），并在 §7.1.6 讨论 self-directedness 与评测之间的 trade-off；**未使用 `self-preference` / `external-verifier` 这类术语**，也没有「验证信号是否独立于被优化对象」的显式判别标准。

**递归深度**：**原文未见本组 E 轴式的四级分级**。它最近的表述是 §6.1 的 `Model-Agent Co-Evolution`（模型与 agent 互相提供进化压力）与 §4 的 intra/inter-test-time 划分——前者接近我们 `co-evolution` 的含义，后者是「何时更新」而非「更新到哪一层」。按 [`../AXES.md`](../AXES.md) 的规则，本节不代作者下结论，E 轴在 CSV 中留空，精读时回查 §6.1 原文。

**可复现性**：综述，无实验；附 GitHub 阅读列表 [CharlesQ9/Self-Evolving-Agents](https://github.com/CharlesQ9/Self-Evolving-Agents)。

**是否入选精读**：否——中期精读名单已由 P4（zgj）冻结为 7 篇，且该篇不提供可检验的自我改进效果。它的作用是**领域地图与五轴的外部校验**：A 轴的四个字段、四问框架、评测五目标，都应在写作仓库 `group/domain-map.md` 与 `group/taxonomy.md` 中被引用或反驳。

**可疑之处**：
1. 自称 "the first systematic and comprehensive survey"，但与 `arxiv-2508.07407`、`arxiv-2607.13104` 三篇同期综述的框架几乎正交（四问 / 四要素反馈环 / 更新算子），说明该领域**尚无共识分类**；我们引用它时必须说明「选用哪一套、为什么」。
2. §2.1 的 `θ_i = (ψ_i, C_i)` 把工具 `W_i` 排除在策略参数之外，等于把 tool 变化当成动作空间变化而非参数变化——这一处理会影响 A 轴 `tool` 与 `code` 的边界判定，精读时需回查其理由。
3. 时间线（Figure 4）止于 2025，**不含 2026 年的 harness 自进化工作**（DGM v3、RHO、SEVerA、RHI 等），引用时须标注时间边界。
4. `venue_verified: true` 的依据是：arXiv HTML 首页标注 "Reviewed on OpenReview: forum?id=CTr3bovS5F"，且 ML Anthology 的 TMLR 2026 索引收录该条（OpenReview 直连被浏览器验证拦截，未人工打开 forum 页）。
