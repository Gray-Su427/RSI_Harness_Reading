---
id: arxiv-2610.00093
title: "Safety in Self-Evolving Agents: A Survey"
authors: "Chen, Feng, Ma, et al."
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: true
org: "Zhejiang University + OPPO Research Institute + Alibaba Group + Rakuten Group"
role: survey
read_status: skim
read_date: 2026-10-13
---

**一句话**：这篇综述提出 **SAVER** 框架，把 self-evolving agent 的安全问题组织成一条状态迁移链 `S × A → V → E → R`，外侧叠加 selection semantics（为何选这个更新）与 feedback semantics（响应如何反塑后续选择），逐章综述记忆、工作流、工具、多智能体、模型侧状态的安全机制与评测。

**领域地图贡献**：不按模块或生命周期切分，而**以"一次可复用影响的落笔—迁移"为最小分析单元**：

> `Substrate` locates where reusable influence resides, `Adaptation` identifies the operation that transforms it, `Violation` characterizes which safety attributes are compromised, `Exposure` determines where and to whom the failure becomes observable, and `Response` evaluates whether the influence can be contained, repaired, or revoked.

`Substrate` 按 §3.1–§3.8 分 8 个 carrier：Prompt/Context、Long-Term Memory、Retrieval & Knowledge、Tool/API/Interface、Skill & Procedure、Workflow/Planner/Topology、External Artifacts & Shared State、Model State。`Adaptation` 为 7 个操作族——"the seven families in Section 4: `add, abstract, activate, modify, forget, propagate, or migrate`"。作者强调这是**分析顺序**而非必须时序："The relation S×A→V→E→R is an order of analysis, not a mandatory chronology of harm."

**关键定义**（§2）：

> We call an agent self-evolving when its own observations, actions, feedback, or execution traces update such reusable state inside the agent loop or runtime, thereby changing later behavior.

> Takeaway 2.1. **Utility Does Not Authorize Promotion.** A locally successful update has evidence of usefulness, not permission for broader reuse.
> Takeaway 2.2. **Storage and Activation Require Separate Authority.** Permission to retain an object does not determine what it may later influence.

**风险分类**：图 1 的六个 violation family（逐字标签）：`Provenance Loss`、`Authority Escalation`、`Purpose Failure`、`Integrity Failures`、`Safety Regression`、`Incomplete Rollback`；四个 response stage：`Preventive Governance`、`Transition & Activation`、`Monitoring & Containment`、`Recovery & Contestability`。两条核心 Takeaway 逐字：

> Takeaway 1.1. **Legitimate State Can Become Unsafe Through Reuse.** Unsafe influence need not begin as harmful content. Adaptation can broaden the persistence, authority, or scope of otherwise legitimate state beyond the conditions under which it was valid.
> Takeaway 10.2. **A Recovery Claim Must State Its Scope.** Local containment establishes that an event was stopped; lifecycle recovery requires evidence about the state left behind.

**覆盖范围**：覆盖 memory、tools & skills、workflow/planner/topology、multi-agent、model-side adaptation、external artifacts。**"harness"在本文中只作状态载体与信任边界出现**（所引 *When Context Gets Root*「Privilege escalation in LLM harnesses」、HarnessSafe「safety across persistent carriers in agent harnesses」都在测 harness 如何**承载/搬运**风险状态）；§3.7 确实覆盖编排控制流——"Planner state, delegation edges, retry policies, approval requirements, and orchestration templates determine where a task goes, who may act, and how much work may be spent." 但 §1 只把 `workflow rules` / `architectural components` 列为可复用 state 的一种。⚠️ 全文检索未见任何"改进 harness 自身"的工作被纳入机制综述。

**对本选题的价值**：它把我们的争议 **Q4** 从直觉升级为可引用框架——"经验沉淀为可复用状态 → 过去成为未来原因"正是其 S×A 视角。它同时**划出我们的选题边界**：本综述把 workflow/编排当**风险载体**，我们把它当**被改进的对象**，这个对立可作为综述的区分点。最尖锐的质疑是 Takeaway 2.1——任何 harness 演化的"局部成功即推广"都落在它的 promotion 缺口里，直接支撑争议 Q1/Q2。它对递归深度不作分类，**不能替代 E 轴**。

**是否入选精读**：否——安全视角的领域地图，不含自我改进效果的可量化证据，且不覆盖 harness-as-object。定位为**争议 Q4 的引用来源 + 边界对照文献**。

**可疑之处**：✅ 作者单位含 Zhejiang University（牵头）、OPPO Research Institute、Alibaba Group、Rakuten Group，`industry` 已于 2026-10-13 按产学合作口径改判为 `true`，`org` 同步补入 CSV 与本卡片 frontmatter；各机构在综述中的具体角色未逐一核实；`selection semantics` / `feedback semantics` 未被编号为 Takeaway，是否算正式分类维度待查；图 1 六个 violation family 与正文 §5 小节标题（§5.1、§5.3、§5.4、§5.6）**不完全一一对应**，family 清单的规范出处未确认；图中的计数（Memory 201、Workflow 224 等）是否为去重后论文计数未逐项确认；附录 A 的 evidence-tier rules 决定各 SAVER 结论的证据强度，引用前必读。
