---
id: arxiv-2506.13131
title: "AlphaEvolve: A coding agent for scientific and algorithmic discovery"
authors: "Novikov, Vũ, Eisenberger, et al."
year: 2025
venue: "arXiv preprint"
venue_verified: false
industry: true
org: "Google DeepMind"
role: industry
read_status: skim
read_date: 2026-10-13
---

**一句话**：发布 AlphaEvolve，一个进化式 coding agent——用 LLM 生成代码 diff 做变异、以 program database 保留候选、由一个或多个 evaluator 自动打分反馈来演化整个代码文件（而非单个函数），并展示其在 Google 内部计算栈优化与数学/CS 构造性发现上的应用。

**改进对象**：**代码**（被改进的对象是"算法/程序"本身，可长达数百行、跨函数与组件）。需注意：AlphaEvolve 的**自身 pipeline（prompt 模板、LLM ensemble、program database、evaluator 集）不是改进对象**——它被当作固定的外壳，被改进的是任务算法。（主要贡献为 code。泛读初步判断，待精读确认）

**改进信号**：外部验证（代码执行 + 自动 evaluator，可多指标；原文称 "grounded using code execution and automatic evaluation"，并称这使其 "avoid any incorrect suggestions from the base LLM"）。原文明言不支持需手工实验的领域。（泛读初步判断，待精读确认）

**搜索算子**：evolutionary（LLM 引导变异 + program database + evaluator 打分后选择/父代采样；异步 asyncio pipeline、Gemini 2.0 Flash/Pro ensemble 平衡吞吐与质量）。（泛读初步判断，待精读确认）

**递归深度**：**未找到作者自我界定**——本文为白皮书，通篇未自称 recursive self-improvement，也未把 AlphaEvolve 归入任何 RSI 框架。全文仅在讨论部分出现与"改进自身"最接近的表述，逐字原话：

> "Beyond distillation, it is also intriguing that AlphaEvolve can make practical discoveries that increase the efficiency of its own infrastructure and of (future versions of) its base LLMs. Currently, the gains are moderate and the feedback loops for improving the next version of AlphaEvolve are on the order of months."

注意这段指的是**基础设施与未来版本 base LLM 的效率**，且把"把增益蒸馏回下一代 base model"明确列为"a natural next step"（未做）。按本组五轴，被改进的是产物（算法）而非改进器本身，应记 `iterative`。（泛读初步判断，待精读确认）

**主要实验**：无统一 benchmark——为多案例研究。案例包括：Google 集群调度启发式（数据中心计算栈）、TPU 电路设计的功能等价化简、Gemini 训练用的 Pallas kernel 优化，以及 4×4 复矩阵相乘——找到需 48 次标量乘的算法，作者称这是该设定下 56 年来首次超越 Strassen 算法。主指标：各案例自身的 wall-clock / 吞吐 / 标量乘数等；基线：FunSearch 及既有人工或启发式方案。算力开销：**部分报告**——原文称 "the sample efficiency of AlphaEvolve makes it feasible to spend on the order of 100 compute-hours to evaluate any new solution"，并讨论了异步并行对进化速率的影响；但未给出整轮搜索的总成本。⚠️ 各案例的具体数值本次未逐一抄录，未核实。

**可复现性**：代码开源？原文未见说明（白皮书全文未见代码仓库或开放获取入口的声明）。archive / program database 公开？未见说明。

**是否入选精读**：是——Gate 2 要求 ≥1 篇工业界研究，本篇是唯一工业界候选（Google DeepMind）。其价值在于提供"被改进对象为代码 + 强外部 evaluator + 完整进化搜索"这一工业级参照系，可用于反驳"harness 自进化只是概念演示"的印象。

**可疑之处**：
1. 🔴 **白皮书，非同行评审**（原文自称 "In this white paper"），方法学细节与实验充分性无法按同行标准核查。
2. 🔴 无统一 benchmark 与统一主指标，各案例不可横向比较；跨论文比较本篇增益基本不可行。
3. 未报告搜索总成本，仅给单次评测的量级（~100 compute-hours）与定性讨论 → 争议 Q3（成本核算）在本篇无法直接回答。
4. 无论文代码、无 program database 公开声明 → Q5 可复现性最差的一篇。
5. E 轴需记 `未找到作者自我界定`；其"改进自身基础设施"的表述易被后人误读为 self-improvement，精读时不得拔高（按 AGENTS.md §5 反例预警）。
6. 各案例的具体效果数字（如调度恢复的算力利用率百分比）⚠️ 未核实，需精读时补全后才能进 evidence.md。
7. 是否已发表于正式场合（白皮书在 Google DeepMind 站点有版本）⚠️ 未核实。
