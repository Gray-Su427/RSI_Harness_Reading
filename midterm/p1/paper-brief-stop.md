# P1 · 论文五问卡：STOP

> 负责人：P1（xyc）｜人员代号：P1 = xyc｜P2 = zyc｜P3 = szh｜P4 = zgj
> 本卡为中期数据核对卡，不是精读笔记；精读产出见 `notes/deep/`。

## 文献与核对范围

- **论文**：Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation
- **ID**：`arxiv-2310.02304`；2023；查阅版本：arXiv v3（2024-08-16）。
- **来源**：[arXiv 摘要](https://arxiv.org/abs/2310.02304) · [COLM 2024 Accepted Papers](https://colmweb.org/2024/AcceptedPapers.html) · [OpenReview（COLM 2024）](https://openreview.net/forum?id=46Zgqo4QIU) · 泛读卡 [`../../notes/skim/arxiv-2310.02304.md`](../../notes/skim/arxiv-2310.02304.md)。
- **访问日期**：2026-10-31。
- **核对状态**：已核对摘要与 venue 官方收录页；**正文表格、附录与成本核算未逐页核对**。
- **Venue**：**COLM 2024（Spotlight）**，`venue_verified: true`，证据见 [`venue-verification.md`](venue-verification.md) §2.1。

## 1. 一句话贡献

【原文】

> In this work, we use a language-model-infused scaffolding program to improve itself. We start with a seed "improver" that improves an input program according to a given utility function by querying an LM several times and returning the best solution. We then run this seed improver to improve itself.

【本组判断】贡献是把「改进改进器」落成可跑的最小闭环：改进器本身是一个能读写程序的程序，因此自改在工程上就是把自己的源码作为输入。DGM / MGM / SICA 的自修改代码路线可视为该闭环的放大。

## 2. 改什么 —— A 轴

【原文】被改的是改进器自身的源代码；语言模型与权重不变。候选策略由 LM 在搜索中提出：

> A variety of self-improvement strategies are proposed by the language model, including beam search, genetic algorithms, and simulated annealing.

【本组判断】主值 `code`，次值 `control-flow`（三类策略本质是搜索控制流）。不记 `prompt`：prompt 只是 LM 调用参数，不是优化对象。

## 3. 凭什么改 —— B 轴

【原文】依据给定效用函数对候选程序打分并取更优者。

【本组判断】记 `external-verifier`。待查项：**效用函数与论文报告的下游指标是否同一套**；若同源，则「外部」仅是形式独立。

## 4. 递归到哪层 —— E 轴及作者原话

【原文，摘要末段】——引用时必须原文照抄，不得改写：

> Since the language models themselves are not altered, this is not full recursive self-improvement.

【原文，同段】

> Nonetheless, it demonstrates that a modern language model, GPT-4 in our experiments, is capable of writing code that can call itself to improve itself.

【本组判断】作者已自行排除「full RSI」，理由为底层模型未变。按 [`../../notes/AXES.md`](../../notes/AXES.md) §E 记 `one-shot`：一次自改后，改进产物可继续改进下游程序，但无证据表明它被再次喂回自身形成多轮。

## 5. 最可疑的一点

【本组判断】

1. **效用函数独立性**：若挑选新版本用的效用函数与报告提升的下游指标同源，「改进」可能是对评测集的过拟合。摘要未说明隔离方式（对应争议 Q2）。
2. **样本与显著性**：摘要仅称 "a small set of downstream tasks" 与 "significantly better"，未给任务数、提升幅度、重复次数。中期只可记录「作者报告在少量任务上显著更优」。
3. **沙箱逃逸**：作者统计生成代码绕过沙箱的频率。这既是安全证据，也说明改进器输出属不可信代码；与 SEVerA（形式化规约兜底）构成对照。

## 6. 已核对事实与出处

| 事实 | 出处 | 状态 |
|---|---|---|
| 闭环形式：seed improver 改进自身 | 摘要 | 已核对（摘要层） |
| 策略来源：beam search / 遗传算法 / 模拟退火 | 摘要 | 已核对（摘要层） |
| 作者自陈 "not full recursive self-improvement" | 摘要 | 已核对（摘要层） |
| 实验模型为 GPT-4 | 摘要 | 已核对（摘要层） |
| 评估过沙箱逃逸频率 | 摘要 | 已核对（摘要层） |
| 任务数、提升幅度、重复次数、预算 | 正文表格（未读） | **待核对** |
| 效用函数与下游评测的隔离方式 | 正文（未读） | **待核对** |
| Venue = COLM 2024 Spotlight | COLM 2024 Accepted Papers | 已核对 |

## 7. 中期后精读待办

- [ ] 回查效用函数与下游评测的隔离方式（对应 Q2），记录章节/表格位置。
- [ ] 补齐任务数、提升幅度、重复次数与预算设置；区分作者实测与本组估算。
- [ ] 读附录：沙箱逃逸的统计口径与阈值。
- [ ] 与 ADAS 对照：两者改进器（seed improver vs meta agent）是否都在搜索中被固定。
- [ ] 完成 `notes/deep/arxiv-2310.02304.md` 的完整 Schema（九节 + 必填字段）。
