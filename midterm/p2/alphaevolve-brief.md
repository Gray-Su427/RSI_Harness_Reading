# P2 · 讲述级五问准备卡 — AlphaEvolve

> 负责人：P2（zyc）｜人员代号：P1 = xyc｜P2 = zyc｜P3 = szh｜P4 = zgj
> 状态：CP2 讲述级准备卡，**不是**完整 Schema 精读；已核对摘要、§1、§2、§3.1—3.3、§6，尚未核对全部附录与各案例数值。

## 文献与核对范围

- **论文**：AlphaEvolve: A coding agent for scientific and algorithmic discovery
- **ID**：`arxiv-2506.13131`；2025；本次查阅 arXiv HTML **v1**（2025-06-16，访问 2026-10-31）。
- **来源**：[arXiv 摘要](https://arxiv.org/abs/2506.13131)、[HTML v1](https://arxiv.org/html/2506.13131v1)、仓库原 skim 卡 [`notes/skim/arxiv-2506.13131.md`](../../notes/skim/arxiv-2506.13131.md)。
- **Venue**：`arXiv preprint`，`venue_verified: false`；原文自称 **white paper**，非同行评审，许可为 CC BY-NC-ND 4.0。
- **作者 / 机构**：Alexander Novikov、Ngân Vũ、Marvin Eisenberger 等；Google DeepMind；`industry: true`。
- **核对边界**：主数字来自正文 §3；成本只报告「单次评测约 100 compute-hours」，**没有整轮总成本**；未找到代码 / program database 的公开声明。

## 1. 一句话贡献

【原文，Abstract】

> In this white paper, we present AlphaEvolve, an evolutionary coding agent that substantially enhances capabilities of state-of-the-art LLMs on highly challenging tasks such as tackling open scientific problems or optimizing critical pieces of computational infrastructure.

【本组判断】AlphaEvolve 的贡献是「把 LLM 代码生成、program database、自动 evaluator 组合成可扩展的进化式 coding agent」，并在数学构造与 Google 计算栈上给出真实案例。它是**工业级参照系**，不是 harness 自进化的证据：被进化的是任务算法，不是 AlphaEvolve 自己的 pipeline。

## 2. 改什么？——A 轴

【原文，§1】

> It represents the candidates (for example, new mathematical objects or practical heuristics) as algorithms and uses a set of LLMs to generate, critique, and evolve a pool of such algorithms. The LLM-directed evolution process is grounded using code execution and automatic evaluation.

【原文，§2.1】

> Any user-provided code inside such evolution blocks serves as the initial solution to be improved by AlphaEvolve, and the rest of the code forms a skeleton that ties the evolved pieces together ...

【本组判断】A 轴记 **`code`**，但必须标注**边界**：改的是用户指定的任务算法 / 启发式 / 内核代码，**不是** AlphaEvolve 自身的 prompt 模板、LLM ensemble、program database、evaluator 或调度 pipeline。它们都是固定外壳，由人提供或配置。**因此 AlphaEvolve 不能算「harness 改自己」的正面样本。**

> **注意**：§2.2 有一个可选的 **meta prompt evolution**，让 LLM 在额外的 prompt-generation 步骤里共进化提示词。它仍然服务于任务搜索，作者没有把它界定为「改进器自改」，也没有用它做 RSI 声明；A 轴仍以 `code` 为主值，不因它改记 `prompt`，边界判定不变。

## 3. 凭什么改？——B 轴

【原文，§1】

> This evaluation mechanism allows AlphaEvolve to avoid any incorrect suggestions from the base LLM ...

【原文，§2.4】

> To track AlphaEvolve’s progress and to select which ideas to propagate in future generations, each new solution proposed by the LLMs is automatically evaluated.

【本组判断】B 轴主值是 **`external-verifier`**：代码执行 + 用户提供的 `evaluate` 函数给出标量分数，program database 按分数与多样性保留候选。可选机制里有 **LLM-generated feedback**（例如给「程序简洁性」打分），但它是 evaluator 的补充，不是主判据；不能因此把 B 记成 `self-preference`。作者也明确说，**最大限制是只能处理能设计自动 evaluator 的问题**（§6）。

## 4. 递归到哪层？——E 轴及作者原话

【原文，§6】

> Beyond distillation, it is also intriguing that AlphaEvolve can make practical discoveries that increase the efficiency of its own infrastructure and of (future versions of) its base LLMs. Currently, the gains are moderate and the feedback loops for improving the next version of AlphaEvolve are on the order of months.

【原文，§6】

> The main limitation of AlphaEvolve is that it handles problems for which it is possible to devise an automated evaluator.

【本组判断】E 轴记 **`待精读`**，不填 `one-shot`，也不填 `iterative`：
- 全文没有出现 AlphaEvolve 对「recursive self-improvement」的自我界定，也没有说自己改进了「改进器本身」。
- 最接近的「改进自身基础设施 / 未来 base LLM」是**产物层**的间接效果：kernel 优化让 Gemini 训练快 1%，但把增益蒸馏回下一代模型被作者列为 **next step**，没有完成。
- 若强行分层：任务算法层是 iterative（多代进化），harness 层是 one-shot（pipeline 不变）；但按本组「以作者自我界定为准」的规则，**不把这个分层填进 E 字段**。

## 5. 最可疑的一点

【本组判断】**这是一篇白皮书，不是可横向比较的实证论文；它的案例很强，但证据结构不支持「AlphaEvolve 是 RSI」的推论。**

1. **白皮书 + 无统一 benchmark**：各案例的主指标不同（标量乘法数、wall-clock、吞吐、面积/功耗），不能加总成一个「AlphaEvolve 提升 X%」的说法。
2. **案例选择偏差**：数学部分是 50+ 个开放问题，报告「75% 复现最佳已知、20% 超过 SOTA」；但问题由作者与合作者挑选，失败案例与调参成本没有系统报告。
3. **成本只报单次评测**：约 100 compute-hours / 次评测，没有整轮搜索总成本；无法回答争议 Q3「同算力下是否仍优」。
4. **可复现性最弱**：未找到代码、program database、完整 prompt / evaluator 配置的公开声明；白皮书也没有同行评审。
5. **「改进自身基础设施」不是闭环**：kernel 优化确实部署并让 Gemini 训练快 1%，但 AlphaEvolve 本身没有因此自动变强；作者说反馈周期以**月**计，且蒸馏是未来工作。
6. **evaluator 由人设计**：自动 evaluator 是优势，也是边界；对需要手工实验的领域不适用。LLM-generated feedback 还可能引入与任务目标不一致的偏好。

## 关键证据：用于讲述，不越过适用范围

| 项目 | 原文位置与结果 | 允许的讲述范围 |
|---|---|---|
| 4×4 复矩阵乘法 | §3.1：找到 **48 次标量乘法**的算法；此前 Strassen 递归为 49，56 年未破 | 仅该设定（复数域、4×4、可递归）；不是所有矩阵乘法 |
| 矩阵乘法总览 | §3.1 / Table 2：在 **14 个**矩阵乘法目标上改进 SOTA | 是作者实验范围内的 14 个目标，不是全部 |
| 数学问题 | §3.2：50+ 个开放问题；约 **75%** 复现最佳已知，约 **20%** 超过 SOTA | 问题集由作者挑选；百分比不是领域总体命中率 |
| 数据中心调度 | §3.3.1：部署后平均回收 **0.7%** 的 fleet-wide compute | 是 Google 生产环境指标，不能外推到其他集群 |
| Gemini kernel | §3.3.2：平均 **23%** kernel speedup，Gemini 整体训练时间 **1%** 下降；已部署 | 是特定 kernel / 输入分布；1% 是整体训练时间 |
| TPU 电路 | §3.3.3：功能等价的 RTL 简化，经 TPU 设计师验证，集成到 upcoming TPU | 是单个电路模块；不是「AlphaEvolve 会设计芯片」 |
| 成本 | §2.4：单次评测约 **100 compute-hours**；未给整轮总成本 | 只能说「作者报告了单次评测量级」，不能说「总成本 100 小时」 |
| 消融 | §4：No evolution / No context / No meta prompt 均变差 | 支持各组件有用；具体数值本次未逐一抄录，待精读 |

## 可直接口述的约 30 秒版本

AlphaEvolve 是 Google DeepMind 的进化式 coding agent：LLM 提出代码 diff，program database 保留候选，自动 evaluator 打分，循环进化。它在 4×4 复矩阵乘法上找到 48 次标量乘法的算法，打破 Strassen 49 次、56 年的纪录；在 Google 的数据中心调度、Gemini kernel、TPU 电路上也有生产或工程案例（调度与 kernel 已部署）。但它进化的是**任务算法**，不是自己的 pipeline；作者没有说它是 RSI，也没有给出整轮成本，未见到代码公开声明。我们把它当作工业级「强 evaluator + 进化搜索」的参照，而不是 harness 自进化的证据。

## 边界判定与分类落位

| 字段 | 本卡结论 | 说明 |
|---|---|---|
| `axis_a_object` | `code`（边界：任务算法） | pipeline 固定；不是 harness 自改 |
| `axis_b_signal` | `external-verifier` | 代码执行 + 自动 evaluator；LLM feedback 为补充 |
| `axis_c_search` | `evolutionary` | LLM-guided diff + program database + MAP-Elites / island |
| `axis_d_guarantee` | `empirical` | 案例验证；无形式化保证 |
| `axis_e_recursiveness` | `待精读` / `unknown` | 无 RSI 自我界定；不填 `one-shot` |
| `industry` / `org` | `true` / `Google DeepMind` | CSV 已正确 |
| 成本 | 部分报告 | 单次评测 ~100 compute-hours；无整轮总成本 |

> P2 不直接改 [`refs/verified.csv`](../../refs/verified.csv)；建议 P1 把 `axis_e_recursiveness` 从 `one-shot` 改为 `unknown`（或保留 `one-shot` + note 说明「产物层 iterative、harness 层不递归」），并在 `note` 记录「白皮书、无 RSI 自我界定、非 harness 自改」。

## 中期后精读待办

- [ ] 按完整 TEMPLATE 补齐九节与必填字段，逐项核对 §2.2—2.5 的 prompt / database / evaluator 细节。
- [ ] 抄录 §3 各案例的完整数值与实验设置；区分「已部署」「模拟器」「单次实验」。
- [ ] 核对 §4 消融的具体数字与 §B 的数学问题清单，确认 75% / 20% 的分母。
- [ ] 查代码、program database、prompt / evaluator 配置是否公开；没有就明确写 `reproducible: false/unknown`。
- [ ] 把「白皮书证据强度」与「工业部署案例」分开写，交 P3（szh）用于争议 Q3 / Q5。
- [ ] 与 DGM 的 `full-rsi` 对照：说明「改任务算法」与「改改进器」的边界，防止 deck 把两者都算作 harness RSI。
