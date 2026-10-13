---
id: arxiv-2606.05922
title: "Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference"
authors: "Pan, Liu, Lin, et al."
year: 2026
venue: "arXiv preprint"
venue_verified: false
industry: true
org: "Microsoft Research Asia + City University of Hong Kong"
role: harness-core
read_status: skim
read_date: 2026-10-13
---

**一句话**：提出 RHO——只用 agent 部署期产生的**无标注历史 trajectory**（经 DPP 选 coreset、并行 group rollout、self-validation/self-consistency 诊断、best-of-N 生成候选 harness）做**单轮**回溯式 harness 优化，全程不使用验证集打分。

**改进对象**：**工具 + 记忆/技能 + prompt**（全文改为 Skills+Tools；harness 被物化为一个目录：instructions/skills 的 markdown + tools 的可执行脚本）。主要贡献是"覆盖完整 harness 而不只是 memory"。可归入轴 A 的 `tool` / `memory` / `prompt` 多值。

**改进信号**：**自偏好（self-preference）**——用 agent 自己的 pairwise 排序 `rank(t, τ_new, τ_old)` 选最优候选，并**只有在 S_j > 0 时才接受更新**（Algorithm 1 第 15 行："return h_j* if S_j* > 0, else h_0"）。诊断信号来自 self-validation（单条 trajectory 内的自检）+ self-consistency（G 条并行 trajectory 之间的不一致性）。

**搜索算子**：**textual-gradient**（把结构化 JSON 的 rank_val / rank_con 输出当作"自然语言反馈"生成 harness 更新）+ refine 式的 best-of-N 采样。无种群/无遗传算子。

**递归深度**：`one-shot`（**单轮回溯**，作者明确说明不声称多轮可累积）——作者未使用 "recursive self-improvement" 一词，也**未给出该词意义上的自我界定**。最接近的两处（逐字照抄）：

> We evaluated a single retrospective optimization round and make no claim that gains compound or even remain monotonic across multiple rounds; studying iterative, multi-pass RHO over sequential trajectory batches is future work.

> after an agent is deployed, we aim to continually evolve its harness by learning from past experiences, which in turn improves its performance on future tasks.

第二句是**研究目标**表述（引言），不是已实现的能力声明。按规则不得代作者升格为 `iterative`。

**如何防止自评循环论证**：作者承认机制**不是完美排序器**。原文逐字：

> What the mechanism reliably guarantees is safety rather than perfect ranking. Because an update is deployed only when the agent prefers it over the current harness (Sj > 0), the deployed harness never fell below the vanilla baseline on any benchmark

并且**主动报告了反例**：

> the most preferred harness does not invariably coincide with the highest-scoring candidate on the test set... on SWE-Bench Pro a less-preferred candidate in fact reached 0.85, above the chosen one's 0.78.

另外：group rollout 用**固定 baseline rollout**作参照（"using the group as a baseline in place of a learned value model"），coreset 用 DPP 在"难度 + 多样性"上取平衡；诊断信号做了消融（Table 4：去掉 self-consistency SWE Pro 0.78→0.56）。局限中承认的唯一一条与自评安全直接相关：trajectory 可能被注入对抗内容，"harness updates distilled from compromised trajectories could entrench such behavior"。Ethics 段亦承认"This can amplify mistaken preferences... if the evaluator prefers them"，并建议保留审计日志与人工审批。⚠️ 未核实：这是否已足够构成"验证信号独立于被优化对象"的回答。

**主要实验**：benchmark：SWE-Bench Pro / Terminal-Bench 2 / GAIA-2（held-out pass rate）。Base = Codex CLI agent + GPT-5.5。RHO：0.59→**0.78**（SWE Pro，+19pp）、0.71→0.76（TB2）、0.29→0.37（GAIA-2）。vs Meta-Harness（需真值标签的 validation-feedback 优化器）：单轮 0.62、10 轮 0.80。算力开销：**报告了**（agent calls：RHO 103 (1.0×)，Meta-Harness 1 轮 41 (0.4×)，10 轮 320 (3.1×)）。超参：coreset k=10，并行 trajectory G=3，候选 N=3，θ=0.7。

**可复现性**：代码开源（`https://github.com/wbopan/retro-harness`，项目页 `https://paper-rho.wenbo.io`）；Reproducibility Statement 称每次 run 持久化 prompts / trajectories / diagnoses / candidate harnesses / harness diffs / scores。

**是否入选精读**：**是**——B 轴 `self-preference` 的唯一正面样本，且作者主动报告了自偏好排序失灵的案例，对争议 Q2（验证器循环论证）是必读；同时它是产学合作（Microsoft Research Asia + CityU HK），`industry` 已于 2026-10-13 改判为 `true`，`org` 同步补入 CSV 与本卡片 frontmatter。

**可疑之处**：① E 轴为单轮，作者只把多轮列为 future work，需查证是否有附录实验。② 消融 n=1（作者自述 n=2 复跑），统计效力弱。③ "graders are used solely for held-out evaluation"——trajectory/test 划分由 benchmark 人工切分而来，**这套划分在真实部署中并不存在**，与作者自己的 motivation 有张力。④ TB2 上 "the generated scripts are never executed"，收益来自 instructions 文本而非工具，说明"改进对象"随 benchmark 漂移。⑤ ⚠️ 未核实：自偏好排序的绝对准确性未被独立评测器复评。（以上为**泛读初步判断，待精读确认**。）