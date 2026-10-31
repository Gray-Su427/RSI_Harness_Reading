# P2 · 讲述级五问准备卡 — DGM

> 负责人：P2（zyc）｜人员代号：P1 = xyc｜P2 = zyc｜P3 = szh｜P4 = zgj
> 状态：CP2 讲述级准备卡，**不是**完整 Schema 精读；已核对摘要、§1、§3、§4、§6、§E.1，尚未逐项核对全部附录与代码运行。

## 文献与核对范围

- **论文**：Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents
- **ID**：`arxiv-2505.22954`；2025；本次查阅 arXiv HTML **v3**（访问 2026-10-31）。
- **来源**：[arXiv 摘要](https://arxiv.org/abs/2505.22954)、[HTML v3](https://arxiv.org/html/2505.22954v3)、[代码仓库](https://github.com/jennyzzt/dgm)、仓库原 skim 卡 [`notes/skim/arxiv-2505.22954.md`](../../notes/skim/arxiv-2505.22954.md)。
- **Venue**：CSV 记 `arXiv preprint`、`venue_verified: false`；ICLR 2026 仅据原 skim 卡所记的 PDF 页眉自述，未按 AGENTS §7.1 独立核验，**不得**在 deck 中说「ICLR 2026 论文」。
- **作者 / 机构**：Jenny Zhang、Shengran Hu、Cong Lu、Robert Lange、Jeff Clune；UBC + Vector Institute + Sakana AI（CSV 的 `org` 目前只写 Sakana AI，建议 P1 补全）。
- **核对边界**：主数字来自论文正文与 §E.1；成本为作者 **estimated cost**，不是账单实测；未运行代码、未复核 archive 日志。

## 1. 一句话贡献

【原文，Abstract】

> We introduce the Darwin Gödel Machine (DGM), a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks.

【本组判断】DGM 的关键不是「又做了一个 coding agent」，而是把 **meta-agent 与 target-agent 合并成同一个可修改的 codebase**，再用 archive + 父代选择维持开放式探索。它证明了「代码层自修改 + benchmark 筛选」可以持续涨分；但没有证明模型层自修改，也没有证明探索机制本身可自改。

## 2. 改什么？——A 轴

【原文，§3】

> Therefore, we define self-improvement as a coding task that involves modifying the design of an agent’s own components (i.e., its own code, which does not include the open-ended exploration process described in the next paragraph).

【原文，§3】

> Currently, the open-ended exploration process (i.e., archive maintenance, parent selection) is fixed and not modifiable by the DGM, which we leave as an avenue for future work.

【原文，§1】

> Empirically, the DGM automatically improves its coding capabilities (e.g., better code editing tools, long-context window management, peer-review mechanisms) ...

【本组判断】A 轴主值是 **`code`**：改进对象是 agent 自己的 Python codebase，工具、prompt、上下文管理都是代码层实现出来的次要对象。**不是 `evaluator`**——archive 维护、父代选择、benchmark 评测都是固定外壳；这是本卡要纠正的最重要一处 CSV 口径（CSV 现为 `code;evaluator`）。

## 3. 凭什么改？——B 轴

【原文，§3】

> Each selected parent analyzes its own benchmark evaluation logs, proposes the next feature to implement, and receives this proposal as a problem statement to execute.

【原文，§3】

> Each newly generated agent is quantitatively evaluated on a chosen coding benchmark to estimate its coding abilities. Only agents that compile successfully and retain the ability to edit a given codebase are added to the DGM archive ...

【本组判断】B 轴主值是 **`external-verifier`**：候选是否进入 archive，由 coding benchmark 的通过率决定，不由 agent 自评或 LLM judge 决定。父代确实会读自己的 benchmark 日志来提出下一个 feature，但这是**生成更新的输入**，不是**接受更新的判据**；不要因此把 B 记成 `failure-trajectory`。分阶段评测（10 → 50/60 → 200 题）是为了省算力，不改变「外部 benchmark 筛选」这一性质。

## 4. 递归到哪层？——E 轴及作者原话

【原文，Abstract】

> ... iteratively modifies its own code (thereby also improving its ability to modify its own codebase) ...

【原文，§6】

> Our framework envisions agents that can rewrite their own training scripts (including training a new foundation model (FM)). However, we do not show that in this paper, as training FMs is computationally intensive and would introduce substantial additional complexity, which we leave as future work.

【原文，§6】

> Since this version of the DGM is mainly powered by FMs, it is inherently limited by the capabilities of the underlying FM.

【本组判断】E 轴记 **`full-rsi`**，但必须加限定：**只在 agent codebase 层**。理由是作者明确说「改进自己改代码的能力」，且改进后的 agent 继续进入下一轮；但 archive/父代选择固定、FM 权重冻结，所以**不是模型层 RSI，也不是 `co-evolution`**。在 deck 中建议说「在本组 9 篇中，DGM 是唯一明确宣称代码层 full-rsi 的工作」，不要说「DGM 实现了完整 RSI」。

## 5. 最可疑的一点

【本组判断】**「coding benchmark 涨分 = 自改进能力变强」是作者的关键假设，也是全文最需要追问的地方。** 作者自己在 §3 写明：

> A key assumption is that an increase in performance on coding benchmarks indicates better coding capabilities, and hence better ability to self-modify and self-improve.

这等于把「自改进」定义成「改代码」这一 coding task，再用 coding benchmark 同时充当**目标**与**自改进能力的代理指标**。因此：
- benchmark 涨分能证明「更会解这些 coding 题」，不能直接证明「更会改进自己」；后者需要单独测量「改进器在后续轮次中的改进效率」。
- 主数字是 **best agent vs base agent**，不是多次运行均值；DGM 的随机性、父代选择、评测子集都会影响最优点。
- 成本不对称：DGM 单次 SWE-bench run 约 **$22,000**，两个 baseline 各约 **$10,000**；没有同算力的随机搜索 / 无 archive 对照，不能排除「多花算力」本身带来部分增益。
- `full-rsi` 的边界由作者自己划定：archive/父代选择不可改、FM 冻结；这使「改进器本身被改进」只在代码层成立。

## 关键证据：用于讲述，不越过适用范围

| 项目 | 原文位置与结果 | 允许的讲述范围 |
|---|---|---|
| 规模 | §4.1：80 iterations，每轮生成 1 个新 agent；SWE-bench 并行 2、Polyglot 并行 4 | 不是 80 次独立重跑；是 1 次开放式搜索的 80 轮 |
| SWE-bench | Abstract / §4.4：**20.0% → 50.0%**（最终强候选在 200 题子集；分阶段 10 → 60 → 200） | 指该 200 题子集上的 best agent；不是全量 SWE-bench 均值 |
| Polyglot | Abstract：**14.2% → 30.7%**（全量）；§4.4：50 题子集 **14.0% → 38.0%** | 全量与子集要分开说，不能混用 |
| 消融 | §4.3：DGM w/o self-improve（固定 meta-agent，作者称复现 ADAS 思路）、DGM w/o open-ended exploration（无 archive）均低于 DGM | 支持「自修改 + archive 都重要」，但不是同算力对照 |
| 跨模型 / 跨 benchmark | §4.4：SWE→Polyglot 28.9% vs 初始 14.2%；Polyglot→SWE 24.5% vs 初始 20.0% | 支持「学到的能力可迁移」，不等于通用智能 |
| 成本 | §E.1：SWE-bench 单次约 **USD 22,000 / 2 周**；两个 baseline 各约 **USD 10,000**；Polyglot 便宜得多 | 作者 **estimated cost**；不能当精确账单，也不能说「所有实验都这个价」 |
| 复现 | 摘要给出 `github.com/jennyzzt/dgm`；Reproducibility Statement 承诺完整 archive lineage | 代码链接存在 ≠ 已复现；本次未运行、未核对 commit 与日志 |

## 可直接口述的约 30 秒版本

DGM 把「改进器」和「被改进的 agent」合成同一个代码库，让 agent 改自己的代码，再用 coding benchmark 筛选，靠 archive 保留一些暂时不最优、但可能通往后续突破的版本。它在 SWE-bench 上从 20% 涨到 50%，Polyglot 全量从 14.2% 涨到 30.7%，但代价是单次 SWE-bench 约 2.2 万美元，baseline 约 1 万。作者明确说 archive 和父代选择固定、模型权重冻结，所以这是**代码层的 full-rsi**，不是完整 RSI。我们最想追问的是：benchmark 涨分，是否真的等于「更会改进自己」。

## 分类落位与交 P1 的 CSV 更正

| 字段 | 本卡结论 | 说明 |
|---|---|---|
| `axis_a_object` | `code`（次值 `tool;prompt;context`） | **不是 `evaluator`**；archive/父代选择/评测固定 |
| `axis_b_signal` | `external-verifier` | benchmark 通过率决定是否入 archive |
| `axis_c_search` | `evolutionary` | archive + 父代选择 + 自修改突变；无显式交叉 |
| `axis_d_guarantee` | `empirical` | 无形式化保证；靠 benchmark 经验筛选 |
| `axis_e_recursiveness` | `full-rsi` | 代码层；须附作者原话与两条边界 |
| `org` | `Sakana AI + University of British Columbia + Vector Institute` | 原文署名含三家 |

> P2 不直接改 [`refs/verified.csv`](../../refs/verified.csv)；以上由 P1（xyc）核验后决定是否写入，并在 `note` 留痕。

## 中期后精读待办

- [ ] 按完整 TEMPLATE 补齐九节与必填字段，逐条核对 §C 的 archive / 父代选择 / 自修改 prompt。
- [ ] 更正原 skim 卡：SWE-bench 的 50.0% 是最终强候选在 **200 题子集**上的结果，不是 60 题子集；§4.2 / §E.2 可核对。
- [ ] 复核 §E.1 成本表与 §A 的稳定性实验（Polyglot 三次运行的 mean 40.7%、sd 2.3% 具体设置）。
- [ ] 核对 `github.com/jennyzzt/dgm` 的 commit、archive 日志、评测脚本与实际可运行状态；不要只凭链接标「可复现」。
- [ ] 把「benchmark 涨分 vs 自改进能力」的测量问题写成争议 Q，交 P3（szh）用于叙事。
- [ ] 与 ADAS 的作者重叠 / 基线关系做独立性检验（AGENTS §6）：DGM 与 ADAS 只能算同一族的一条证据。
- [ ] venue 核验：查 OpenReview / DBLP 的 ICLR 2026 录用记录；未核验前保持 `venue_verified: false`。
