---
id: arxiv-2310.02304
title: "Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation"
authors: "Zelikman, Lorch, Mackey, Kalai"
year: 2023
venue: "COLM 2024 ⚠️未核验(来源:课程PPT)"
venue_verified: false
industry: true
org: "Stanford University + Microsoft Research + OpenAI"
role: seed
read_status: skim
read_date: 2026-10-13
---

**一句话**：用一个 LM 驱动的 seed improver（scaffolding 程序）反复改进这个 improver 自身的代码，在一组算法型下游任务上以 meta-utility 衡量改进效果，并统计 LM 绕过 sandbox 的频率。

**改进对象**：**代码**（主要贡献——被改进的 improver 本身就是一段 Python scaffolding 程序）；次要涉及 **prompt/上下文**（utility 以"可调用函数 + 描述字符串"两种形式拼进 seed prompt）。（泛读初步判断，待精读确认）

**改进信号**：**外部验证**——meta-utility û(I) = 在下游任务集合 D 上求平均 utility（Algorithm 1），不是自评。（泛读初步判断，待精读确认）

**搜索算子**：seed 本身是 best-of-N 的 refine；但 LM 自己提出并实现的策略横跨 beam search、遗传算法、simulated annealing、tree search（Figure 1），故整体更接近 evolutionary。（泛读初步判断，待精读确认）

**递归深度**：`iterative`——作者明确声明**不是** full RSI。作者原话：

> "Since the language models themselves are not altered, this is not full recursive self-improvement."

> "We refer to this problem as recursively self-improving code generation, which is inspired by but not completely a Recursively Self-Improving (RSI) system, as the underlying LM remains unchanged."

Ethics Statement 里还有第三处同样限定："STOP does not alter the black-box LM and hence is not full RSI."

**主要实验**：
- benchmark：LPN with noise（10-bit，M=20 训练实例，Mtest=50 独立测试实例）；迁移到 5 个新任务（String Grid Dist.、Mod. Quad. Assign.、3SAT、Maxcut、Parity w/o Noise）。
- 主指标与结果：test meta-utility。GPT-4 上 1–3 轮持续提升；**GPT-3.5 与 Mixtral 上性能退化**。迁移表：3SAT 0%→75.1%、Maxcut 58.7%→74.2%、Parity w/o Noise 59.3%→81.7%、String Grid 44.3%→56.7%、Mod. Quad. 20.6%→22.1%（û(I_0)→û(I_T)）。
- 基线：chain-of-thought（57.7%±3.0%，计错误 49.6%±3.5%）、greedy iterative improver（64.2%±0.9%）。
- 算力开销：**部分报告**——只给渐近式 O((budget_u + budget_L) * budget_û)，**未给美元/GPU 金额**。

**可复现性**：代码开源（`https://github.com/microsoft/stop`），使用公开模型 gpt-4-0314 / gpt-3.5-turbo-0613 / Mixtral-8x7B-Instruct-v0.1。archive：**原文未见公开 evolution archive 的说明**（只给了最终 improver 的代码，Appendix H）。

**是否入选精读**：是——Harness 自进化方向的两篇奠基工作之一；作者亲手给出"不算完整 RSI"的限定，是 E 轴反例的原始出处；且带有明确的负结果（GPT-3.5/Mixtral 退化）。

**可疑之处**：
1. ✅ **作者机构已更正**：txt 首页署名为 Stanford University / Microsoft Research / OpenAI（"Work done while at Microsoft Research New England"），**没有出现 Meta FAIR 或 UW-Madison**。`verified.csv` 与本卡片 frontmatter 的 `org` 原记 `Meta FAIR + UW-Madison`，属错误数据，已于 2026-10-13 按 PDF 署名更正；`AGENTS.md` §8.1 未列 org，无残留冲突。
2. ⚠️ `COLM 2024` 只见于 txt 每页页眉 "Published as a conference paper at COLM 2024"，属自述，仍需 DBLP/OpenReview 独立核验。
3. 每轮只保留单个 best improver，作者自述这"likely imposes a bias"；**未跑同算力随机采样/暴力搜索基线**，增益是否来自选择偏差（争议 Q1）需精读核查。
4. 成本只有渐近式，无实际金额，Q3 成本核算在本篇无法闭环。
5. 负面结论（GPT-3.5、Mixtral 退化）意味着结论强依赖特定闭源模型，作者自述"unlikely that STOP would consistently work with any open-source LM at the time of writing"。