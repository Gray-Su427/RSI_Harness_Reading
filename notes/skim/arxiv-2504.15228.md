---
id: arxiv-2504.15228
title: "A Self-Improving Coding Agent"
authors: "Robeyns, Szummer, Aitchison"
year: 2025
venue: "arXiv preprint"
venue_verified: false
industry: true
org: "iGent AI + University of Bristol"
role: seed
read_status: skim
read_date: 2026-10-13
---

**一句话**：让一个只配备基础编码工具（开关文件、执行 shell、子 agent 调用、异步 overseer）的 agent system 编辑自己的完整 Python 代码库，并从 archive 中挑出"当前最好的自己"充当下一轮的 meta-agent，迭代 15 轮。

**改进对象**：**代码**（主要贡献——操作对象是 agent 的完整 Python codebase，而非单个 forward 函数）；次要涉及 **工具**（agent 自造 diff/range 编辑工具、AST symbol locator）与 **prompt**（作者明说改代码即包含调自己的 prompt）。（泛读初步判断，待精读确认）

**改进信号**：**外部验证**——benchmark 准确率 + 作者自定义 utility U（score 0.5 / cost 0.25 / time 0.25 加权，超时 τ=0.5 罚分）。非自评。（泛读初步判断，待精读确认）

**搜索算子**：`refine`——每轮仅从 archive 中取 argmax 的单个 agent 做一次 meta-improvement，无种群、无交叉、无 mutation 算子；失败迭代保留在 archive 里作为"反面教材"。（泛读初步判断，待精读确认）

**递归深度**：`iterative`（按本组轴定义保守取值；**作者自称 "fully self-improving"**）。作者原话：

> "In contrast, our self-improving coding agent is fully self-improving (i.e. there is no distinction between the meta and target agent), and it operates over the agent's full Python codebase."

以及作者对 ADAS 的对照（说明其"自指"主张的所指）：

> "ADAS has a fixed meta-agent, so does not select the meta-agent from the archive (the archive in ADAS is an archive of target-agents, not meta-agents)."

⚠️ 但作者自述"fully self-improving"仅指 meta/target 不分离，**并未改进模型权重**——见可疑之处。

**主要实验**：
- benchmark：SWE-Bench Verified 固定随机 50 题子集；LiveCodeBench 50 题；两个自建 synthetic benchmark（file editing、symbol navigation）。另有一组 AIME 2024 + GPQA Diamond。
- 主指标与结果（16 行 Table 1，iteration 0 → 15）：SWE-Bv **0.17 → 0.53**，LiveCodeBench 0.65 → 0.71，File editing 0.82 → 0.96，Symbol navigation 0.35 → 0.43。**AIME/GPQA 组几乎无提升**（agent system 平均 76%，而 o3-mini 单模型即 87% / 79%）。
- 基线：iteration 0 的 base agent（无同算力的随机搜索/暴力采样对照）。模型：Sonnet 3.5 (v2) 为主，reasoning agent 用 o3-mini。
- 算力开销：**已报告**——15 轮总 API 成本约 **$7,000**；每 problem 平均 $1.58–$2.70、时间 103.9–151.4 s。

**可复现性**：代码开源（`https://github.com/MaximeRobeyns/self_improving_coding_agent`），标准 Python 实现、无领域专用语言。archive：**原文未见公开 archive 的说明**。

**是否入选精读**：是——首个把"meta agent = target agent"落到完整 codebase 上的工作，且作者对 ADAS / Gödel Agent / STOP 三家的定位清晰，是分类体系的锚点之一。

**可疑之处**：
1. ⚠️ **E 轴存在口径落差**：作者原话用 "fully self-improving"，但本组 `full-rsi` 要求"改进器本身也被改进"。作者同时明确写出边界——Safety 段："there seem to be limits to what can be achieved with such purely scaffolding based systems ... which do not modify the model weights"，并说 "If the system updated the model weights as well as the scaffolding, we would expect that the risks of recursively self-improving systems would be higher." 精读时需决定 `iterative` vs `full-rsi`，**不得单凭 "fully self-improving" 一词拔高**。
2. ⚠️ 作者自述 path dependency："the initial feature ideas would often heavily influence later feature ideas as variations on the same theme"，即单次 run 的结果高度依赖起始 agent 的"品味"。
3. ⚠️ **增益构成存疑**（直接关联争议 Q3）：作者自述 "much of the initial improvement we report arises from features speeding up file editing and agent cost, which are not traditionally reflected to the same degree in SWE-Bench numbers."
4. Abstract 的 "17% to 53%" 是最优迭代 vs 第 0 迭代的差值，**不是均值**；Table 1 显示中途有回退（如 iteration 13 掉到 0.27）。原文未见多次独立 run 的方差报告。
5. SWE-bench 只用 50 题随机子集，且 timeout 设为 300 s，作者自述初始分"perhaps be lower than expected"。
6. venue：txt 首页标 "Preprint."，无会议名；`verified.csv` 的 `arXiv preprint` 与原文一致，无需核验。
7. 机构为 iGent AI + University of Bristol，含企业署名（iGent AI），`industry` 已于 2026-10-13 改判为 `true`；`org` 同步补入 CSV 与本卡片 frontmatter。