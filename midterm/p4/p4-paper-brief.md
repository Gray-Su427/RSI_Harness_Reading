# P4 · 讲述级五问准备卡

> 负责人：P4（zgj）｜人员代号：P1 = xyc｜P2 = zyc｜P3 = szh｜P4 = zgj

## 文献与核对范围

- **论文**：Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents
- **ID**：`arxiv-2605.30621`；2026；本次查阅版本 v1（2026-05-28）。
- **来源**：[arXiv 摘要](https://arxiv.org/abs/2605.30621)、[HTML 原文](https://arxiv.org/html/2605.30621v1)、[仓库原 skim 卡](https://github.com/Gray-Su427/RSI_Harness_Reading/blob/main/notes/skim/arxiv-2605.30621.md)。访问日期：2026-10-30。
- **状态**：中期讲述准备卡；已核对摘要与正文 §3—6，尚未完成附录、代码运行及完整 Schema 精读。
- **Venue**：`arXiv preprint`，`venue_verified: false`，沿用 CSV（P1／xyc 维护）；本文企业署名含 Amazon，原文首页可核对。

## 1. 一句话贡献

【原文】作者把 harness 自进化拆成“产出有用更新”的 **harness-updating** 与“实际利用更新获益”的 **harness-benefit**，独立改变 evolver 和 task-solving agent 的模型，研究它们是否随基础解题能力变化。

【本组判断】其价值是拆解测量混杂：端到端涨分本身无法说明是更新器更好，还是使用更新的 agent 更强。

## 2. 改什么？——A 轴

【原文，§3.1、§4.1】固定模型权重，更新外部 harness。SWE-bench Verified、SkillsBench 更新 skills；MCP-Atlas 更新 skills、prompts、memories。工具接口与执行策略等保持固定。

【本组判断】这是测量研究，不是新更新算法。记录 A 轴时应说明“被测协议的可编辑对象”；按 [`notes/AXES.md`](https://github.com/Gray-Su427/RSI_Harness_Reading/blob/main/notes/AXES.md)，skills 首先是 `memory`（技能库）的典型内容；若具体 skill 以可执行脚本形式存在，再叠加 `tool`。提交 P2（zyc）确认，不能一律记为 `tool` 或 `code`。

## 3. 凭什么改？——B 轴

【原文，§3.1—3.2】evolver 依据 agent 执行任务的 evidence（任务、trajectory、输出）生成并应用更新。最终测量主要使用各 benchmark 的 pass rate。

【本组判断】需要分开记录“生成更新所用反馈”和“测量收益所用评分”。执行证据可能包含成功与失败，不宜未经附录核对便把 B 轴压成唯一的 `failure-trajectory`，也不能把最终外部评分直接说成更新时的反馈。

## 4. 递归到哪层？——E 轴及作者原话

【原文，§3.2】

> Starting from an initial harness H0, the protocol iterates for T steps. At each step, the agent runs on a batch of tasks, collects execution evidence, and the evolver updates the harness for the next step.

【原文，§3.1，数学符号按文本转写】

> we keep f fixed and only update editable components of Ht

【本组判断】正文明确存在更新 harness 参与后续任务的迭代协议；目前核对内容未给出作者对本组 E 轴的自我归类。保留“迭代更新协议”这一描述，正式 E 字段先记 `unknown`／待核实，不由固定权重或多轮循环直接推出 `full-rsi`。

## 5. 最可疑的一点

【本组判断】“更强 evolver 的增益相近”是否稳健，仍取决于任务、锚定模型集合、prompt 和预算设置。小差距不等于统计上证明能力相同，更不能推广成“改进更新器没有价值”。后续重点核查：

1. `Δ_update` 对固定 anchor agents 取均值；不同 agent 上的优劣是否被平均抵消？
2. `Δ_benefit` 对固定 anchor evolvers 取最大值；是否有多重选择带来的乐观偏差，是否报告独立确认与不确定性？
3. §3 的最终 harness 记法与 §4.1 的 in-situ 流式评分如何衔接？后者是每个任务先评分，再用其证据更新，不能口头描述为“最终 harness 在独立测试集上的分数”。
4. 相同 evolution budget 和 turn limit 控制了哪些资源？是否仍有 token、API 单价、时间差异？

## 关键证据：用于讲述，不越过适用范围

| 项目 | 原文位置与结果 | 允许的讲述范围 |
|---|---|---|
| 实验覆盖 | §4.1：3 个 benchmark；agent 侧 6 个模型，evolver 侧 7 个模型 | 不是完整 7×7 全模型配对；两侧分析分别采用固定 anchor 集合 |
| Updating | §4.2、Fig. 3：任一 benchmark 中最优与最差 evolver 的 `Δ_update` 相差至多 3.1pp | 指本实验聚合指标差距，不能说所有更新同样好 |
| Benefit | §4.3、Table 1：SWE 中 Qwen3-235B 为 +19.3pp，Qwen3-32B 为 +4.4pp，Opus 4.6 为 +2.6pp | 指所选 evolver 集合上的最大增益；不是最终绝对分数排名 |
| 激活失败 | §4.3、Table 2：Qwen3-32B skill-load rate 0.251，Opus 4.6 为 0.957 | 仅该 SkillsBench 诊断设置，不推广为所有任务的失败率 |
| 遵循失败 | §4.3、Table 3：Qwen3-32B 的阶段 adherence 0.52→0.13，Opus 4.6 为 0.89→0.80 | 来自 LLM judge 的轨迹诊断，附录中 judge 稳健性待核查 |

其中 **pp 为百分点**，与相对百分比提升不同。

## 代码与复现核对更新

原 skim 卡写“PDF 抽取丢失代码 URL”。本次 arXiv 摘要及 HTML 已明确链接到：

- [A-EVO-Lab/a-evolve · release/harness-evolution](https://github.com/A-EVO-Lab/a-evolve/tree/release/harness-evolution)
- 本次 GitHub API 已返回该分支目录，含 README、`pyproject.toml`、`agent_evolve`、`scripts`、`seed_workspaces`、`tests`。

**核对结果**：代码链接和对应分支可访问。尚未核对完整日志／archive、依赖安装、API 可用性或运行结果，因此不能标记“已复现”。建议将链接交给 P1（xyc）及原 skim 卡维护者更新来源记录。

## 可直接口述的约 30 秒版本

这篇研究提醒我们，把 harness 改了和 agent 因此获益是两回事。作者分开更换更新器与解题模型，在三个 benchmark 中发现，更新器之间的平均增益差距较小，而使用者收益并不随基础能力单调增加。弱模型可能不加载、也可能不遵循新 skill。因此我们会分别检查更新质量、使用能力和测量设置，而不只看最后涨了多少分。

## 中期后精读待办

- [ ] 按完整 TEMPLATE 补齐九节与必填字段，加入正式版本和章节定位。
- [ ] 回查 Appendix B 的任务流、预算、prompt、初始 harness 与实现细节。
- [ ] 回查 Appendix C／D 的完整配对表、随机性、judge 配置和统计不确定性。
- [ ] 检查公开代码、配置与日志如何对应论文；记录 commit 和实际运行状态。
- [ ] 将可支持的测量论点交 P3（szh），成本／复现缺口交风险表；E、A、B 不确定项交 P2（zyc）。
