# P3 · RHO 讲述级五问卡

> 负责人：P3（szh）｜日期：2026-11-01｜论文：`arxiv-2606.05922`｜状态：**讲述级，不是完整 Schema**
> 依据：[`../../notes/skim/arxiv-2606.05922.md`](../../notes/skim/arxiv-2606.05922.md)（2026-10-13 泛读卡，原话已回查 PDF）+ [`../p2/classification.md`](../p2/classification.md) ⑤
> 口径：`【原文】`= 作者原话；`【本组判断】`= 我们的归纳。E 轴只认作者自我界定。

---

## 问 1 · 一句话贡献

**提出 RHO：只用 agent 部署期产生的无标注 trajectory 做单轮回溯式 harness 优化**——DPP 选 coreset、并行 group rollout、self-validation / self-consistency 诊断，best-of-N 生成候选 harness，全程不使用验证集打分。

【原文】主结果：SWE-Bench Pro **0.59 → 0.78（+19pp）**，Terminal-Bench 2 **0.71 → 0.76**，GAIA-2 **0.29 → 0.37**（held-out pass rate；base = Codex CLI + GPT-5.5）。

## 问 2 · 改什么（A 轴）

`tool`（主）｜`memory` / `prompt`（次）。

【原文】harness 被物化为一个目录：instructions / skills 的 markdown + tools 的可执行脚本。
【本组判断】CSV 现记 `prompt;control-flow;tool`，主值建议统一为 `tool`——它改的载体是**工具脚本 + 技能文本**，不是控制流拓扑。

## 问 3 · 凭什么改（B 轴）

`self-preference`（本组 9 篇里唯一正面样本）。

【原文】用 agent 自己的 pairwise 排序 `rank(t, τ_new, τ_old)` 选最优候选，且 **only when S_j > 0** 才接受更新：「return h_j* if S_j* > 0, else h_0」；诊断信号来自 self-validation + self-consistency（G 条并行 trajectory 的不一致）。

## 问 4 · 递归到哪一层（E 轴，作者原话）

`one-shot`。

【原文】「We evaluated a single retrospective optimization round and make no claim that gains compound or even remain monotonic across multiple rounds; studying iterative, multi-pass RHO over sequential trajectory batches is future work.」

【本组判断】作者全文**未使用** "recursive self-improvement" 一词，也**未给出**该词意义上的自我界定。引言里 "continually evolve its harness" 是**研究目标**，不是已实现的能力声明，不得代作者升格为 `iterative`。
⚠️ **CSV 冲突**：`refs/verified.csv` 记 `axis_e_recursiveness = iterative`，建议 P1 更正为 `one-shot`（见 [`cp4-checklist.md`](cp4-checklist.md) §C）。

## 问 5 · 最可疑的一点

【本组判断】**作者自己报告了自偏好失效的案例，这恰好是它最有价值的地方**：

【原文】「the most preferred harness does not invariably coincide with the highest-scoring candidate on the test set... on SWE-Bench Pro a less-preferred candidate in fact reached 0.85, above the chosen one's 0.78.」

其余四个可疑点：

1. **消融效力弱**：n=1（作者自述 n=2 复跑）；去掉 self-consistency 后 SWE Pro 0.78 → 0.56，但单次运行不足以支撑因果结论。
2. **trajectory / test 的划分是 benchmark 人工切的**，真实部署不存在这条边界——与作者"部署场景无真值"的 motivation 有张力。
3. **TB2 上生成的脚本从未被执行**，收益来自 instructions 文本；说明"改进对象"会随 benchmark 漂移（A 轴不稳定）。
4. **成本可比性**：RHO 103 agent calls（1.0×）vs Meta-Harness 单轮 41（0.4×）/ 十轮 320（3.1×）——**唯一一组同口径成本**，应作为 Q3 的正面样本；但只覆盖 agent calls，不含美元/时延。

> 作者自陈的安全边界（Q2 用）：「What the mechanism reliably guarantees is safety rather than perfect ranking.」——即 **不劣于基线**，不是"验证独立"。

## 给 deck 的一句话

**RHO 把验证从"人工标注"换成了"自己的偏好"，代价是作者自己承认：最偏好的方案不一定是测试最高的那个（0.78 vs 0.85）。**

## 汇报时不要说

- ❌「RHO 证明了自偏好可以替代真值验证」——它证明的是单轮不劣于基线。
- ❌「RHO 是迭代式自改进」——作者明确单轮，且不声称累积。
- ❌「RHO 覆盖了完整 harness」——它覆盖 instructions/skills/tools 三类，不含 evaluator 与 control-flow。

## 精读要补的三件事

1. 附录是否有多轮实验（作者说 future work，需确认无隐藏结果）。
2. 自偏好排序与 held-out 分数的一致率（是否给过相关系数）。
3. coreset / group rollout 的算力是否计入 103 calls（口径定义）。
