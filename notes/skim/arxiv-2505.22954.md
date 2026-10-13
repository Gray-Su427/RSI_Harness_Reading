---
id: arxiv-2505.22954
title: "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents"
authors: "Zhang, Hu, Lu, Lange, Clune"
year: 2025
venue: "ICLR 2026 ⚠️未核验(来源:课程PPT)"
venue_verified: false
industry: true
org: "Sakana AI"
role: seed
read_status: skim
read_date: 2026-10-13
---

**一句话**：让 coding agent 编辑自己的代码库来自我修改，从 archive 中按"性能正比 / 子代数反比"选择父代并分支出新 agent，用 coding benchmark 实测筛选，形成一棵不断增长的 agent 树。

**改进对象**：**代码**（主要贡献——改进对象就是 agent 自身的 code repository）；次要涉及 **工具**（自造编辑工具）、**prompt**、**上下文管理**（长上下文窗口管理、peer-review 机制）。**不是评测器**——archive 维护与父代选择由外部固定。（泛读初步判断，待精读确认）

**改进信号**：**外部验证**——每个新 agent 在 coding benchmark 上量化评测（分阶段：10 题 → 50/60 题 → 200 题）；同时叠加 open-endedness 驱动的 archive 探索。（泛读初步判断，待精读确认）

**搜索算子**：`evolutionary`——种群 + archive + 父代选择（性能 ∝ 1/子代数）+ 自修改突变；无显式交叉算子，父代靠分析自身 benchmark 日志自行提出下一个 feature。（泛读初步判断，待精读确认）

**递归深度**：`full-rsi`（作者明确宣称自改进指向"改进自己的 codebase"）。作者原话：

> "We introduce the Darwin Gödel Machine (DGM), a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks."

> "By improving its own capabilities through this loop, the DGM becomes better at both solving coding tasks and making future self-improvements."

⚠️ 作者同时给出明确边界（见可疑之处）：archive/父代选择过程固定、FM 权重冻结。

**主要实验**：
- benchmark：SWE-bench Verified（60 题 / 200 题分阶段子集）、Polyglot（全量 + 50 题子集）。80 iterations，1 iteration 产生 1 个新 agent，SWE-bench 并行 2、Polyglot 并行 4。自我修改阶段用 Claude 3.5 Sonnet (New)；评测阶段 SWE-bench 用 Claude 3.5 Sonnet (New)、Polyglot 用 o3-mini。
- 主指标与结果：SWE-bench **20.0% → 50.0%**（60 题子集）；Polyglot 14.0% → 38.0%（50 题子集），全量 Polyglot **14.2% → 30.7%**。作者称最优 DGM agent 与 checked open-source human-designed SoTA 相当，但**仍不及闭源 SoTA**。
- 基线：DGM w/o self-improve（即固定 meta agent，作者明说"replicates the approach of ADAS"）；DGM w/o open-ended exploration（无 archive，只沿最新可用版本自修改）；checked open-source SoTA；Aider（Polyglot）。
- 算力开销：**已报告**——SWE-bench 单次 run ≈ **$22,000**、约 **2 周**；两个基线各 ≈ **$10,000**；Polyglot（o3-mini，60 题）≈ **$5**。

**可复现性**：代码与完整 agent logs 声明开源（`https://github.com/jennyzzt/dgm`），Reproducibility Statement 承诺公开"完整 archive lineage of self-modifications (diffs, prompts, and configs)"及评测 harness。⚠️ 注意其时态为 "We will open-source"。

**是否入选精读**：是——同时占"工业界"与"2025–2026 新工作"两项硬指标；是 STOP→ADAS→DGM 主线的最新一环，也是唯一明确宣称"改进自改能力"的工作。

**可疑之处**：
1. ⚠️ **"full-rsi" 自我宣称有明确作者自设的边界**，必须照抄进精读笔记：
   > "Currently, the open-ended exploration process (i.e., archive maintenance, parent selection) is fixed and not modifiable by the DGM, which we leave as an avenue for future work."
   作者还写明 FM 权重冻结、"Our framework envisions agents that can rewrite their own training scripts ... However, we do not show that in this paper"。即：**改进器的选择机制本身不可自改**。
2. ⚠️ **Reproducibility Statement 用 "We will open-source"**，archive 与完整 logs 是否已实际发布 ⚠️ 未核实（关联争议 Q5）。
3. ⚠️ **独立性检验警告**：DGM 与 ADAS（arxiv-2408.08435）作者重叠（Shengran Hu, Cong Lu, Jeff Clune），且 DGM 自己的基线之一就是 ADAS。按 AGENTS.md 的"作者重叠 + 问题设定重叠 + 结论重叠 → 同一族"标准，**这两篇只能算一条证据**。DGM 内部相对独立的是 DGM w/o open-ended exploration 这一消融。
4. 基线不完全对称：`DGM w/o open-ended exploration` 仍保留"最近一个能编辑代码的版本"，因此该消融只隔离了 archive 的作用，未隔离选择策略。
5. ⚠️ `ICLR 2026` 只见于 txt 页眉 "Published as a conference paper at ICLR 2026"（arXiv v3，2026-03-12），属自述，需 OpenReview 独立核验。
6. 成本为估算值（"estimated cost"），非账单实测；作者亦承认高分 agent 推理成本更高且与性能不严格相关。