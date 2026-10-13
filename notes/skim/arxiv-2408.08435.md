---
id: arxiv-2408.08435
title: "Automated Design of Agentic Systems"
authors: "Hu, Lu, Clune"
year: 2024
venue: "ICLR 2025 ⚠️未核验(来源:课程PPT)"
venue_verified: false
industry: false
org: "University of British Columbia + Vector Institute"
role: seed
read_status: skim
read_date: 2026-10-13
---

**一句话**：把"自动化设计 agentic 系统（ADAS）"形式化为「搜索空间 + 搜索算法 + 评测函数」三元组，并提出 Meta Agent Search——一个固定的 meta agent 依据不断增长的 agent archive，迭代地用代码编写出新的 agent 并实测其性能。

**改进对象**：**代码**（主要贡献——在完整 agent 代码空间搜索，理论上覆盖 prompts、tool use、workflows 及其组合）；次要涉及 **控制流**、**工具**、**prompt**（这些都包含在代码空间内，非独立轴）。（泛读初步判断，待精读确认）

**改进信号**：**外部验证**——候选 agent 在 held-out test set 上跑 accuracy / F1 得分，数值结果进 archive。（泛读初步判断，待精读确认）

**搜索算子**：archive-based 的开放域搜索（novelty / "interestingness" 由 meta agent 用自然语言判断），无遗传算子、无显式交叉；作者自述"the design of the search algorithm is relatively simple"。更接近 evolutionary / novelty search 而非严格遗传算法。（泛读初步判断，待精读确认）

**递归深度**：**未找到作者自我界定**。全文检索 "recursi" 只有一处命中，且出现在参考文献条目（引用 STOP）。作者从未自称该系统构成 recursive self-improvement。

**主要实验**：
- benchmark：ARC（grid ≤5×5 的 Public Training Set Easy，val 20 / test 60，25 iterations，meta agent 用 GPT-4，被测 agent 与基线用 GPT-3.5）；DROP、MGSM、MMLU、GPQA（各域独立搜索，30 iterations，meta agent GPT-4 / 被测 GPT-3.5）。
- 主指标与结果（test accuracy，95% bootstrap CI）：DROP F1 79.4±0.8（COT 64.2±0.9，**+13.6/100**）；MGSM 53.4±3.5（COT 28.0±3.1，**+14.4%**）；MMLU 69.6±3.2（最佳基线 67.6±3.2，OPRO）；GPQA 34.6±3.2（最佳基线 32.9±3.2，OPRO）。跨模型：ARC 上 Dynamic Memory and Refinement Agent 在 GPT-4 达 37.0±5.3、Claude-Sonnet 48.3±5.7。跨域迁移：GSM8K +25.9%、GSM-Hard +13.2%。
- 基线：COT、COT-SC、Self-Refine、LLM-Debate、Step-back Abstraction、Quality-Diversity（简化版 Go-Explore）、Role Assignment、OPRO；另有 empty-initialization 变体。
- 算力开销：**已报告**——ARC 单次搜索+评测 ≈ **$500**（OpenAI API），推理与解题域单次 ≈ **$300**（Appendix J）。

**可复现性**：代码开源（`https://github.com/ShengranHu/ADAS`）。archive：**原文未见完整 archive 的发布说明**（archive 只是算法内部组件）。

**是否入选精读**：是——ADAS 是本子方向的定义性工作，也是 STOP 之后 harness 自进化谱系的关键中间节点。

**可疑之处**：
1. ⚠️ **E 轴无作者自我界定**，需要外部文献来定位（不可代作者下判断）。
2. ⚠️ **SICA（arxiv-2504.15228）明确批评 ADAS "not self-improving"**，理由是 meta-agent 与 target-agent 分离且 meta-agent 固定 —— 但这是 **SICA 作者的判断，不是 ADAS 作者的判断**，引用时必须标注来源。
3. novelty 判据由同一个 LLM 主观给出（Figure 1 的 "Refine until novel and error-free"），是否构成 Q2 意义上的循环论证，需精读核查其与 test set 是否隔离。
4. MMLU / GPQA 上提升幅度很小且 95% CI 大量重叠，作者自述 "the gap is smaller"。
5. meta agent 用 GPT-4、被测 agent 用 GPT-3.5 的**不对称设置**，跨论文比较时需注意。
6. ⚠️ `ICLR 2025` 只见于 txt 页眉 "Published as a conference paper at ICLR 2025"，属自述，仍需 OpenReview 独立核验。
7. 作者机构为 UBC / Vector Institute / Canada CIFAR AI Chair，无企业署名，`industry` 维持 `false`；`org` 已于 2026-10-13 补入 CSV 与本卡片 frontmatter。