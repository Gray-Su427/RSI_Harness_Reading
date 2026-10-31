# 五轴速览表（CP2 · 5 行）

> 负责人：P2（zyc）｜日期：2026-10-31｜来源：[`../../notes/AXES.md`](../../notes/AXES.md)
>
> 本表是 `AXES.md` 的压缩速览，**不替代原文**；轴定义、反例预警与修订记录以 `AXES.md` 为准。
> 统计口径：本组 9 篇核心论文（7 篇精读候选 + 2 篇泛读补充）；A/B 按主值计数；C 轴允许多值，故合计可 >9。

| 轴 | 一句话问题 | 取值 | 本组 9 篇暂定分布 | 填写规则 / 反例预警 |
|---|---|---|---|---|
| **A** 改进对象 | 改的是 harness 的哪一块？ | `prompt` / `control-flow` / `code` / `tool` / `memory` / `evaluator` / `context` | `code` 6；`control-flow` 1；`tool` 1；`memory` 1；`prompt` 0；`evaluator` 0；`context` 0 | 必填=主要贡献；次要值追加。DGM 同时改代码与工具/上下文，但**不改 `evaluator`**；不要把「代码里包含控制流」都记成 `control-flow`。 |
| **B** 改进信号 | 改进依据从哪来？ | `self-preference` / `external-verifier` / `human` / `failure-trajectory` | `external-verifier` 6；`failure-trajectory` 2；`self-preference` 1；`human` 0 | 追问「验证信号是否独立于被优化对象」。RHO 是 `self-preference` 唯一正面样本；Harness≠Benefit 的「生成更新用执行证据」与「测量收益用 pass rate」要分开记。 |
| **C** 搜索算子 | 怎么搜候选？ | `refine` / `evolutionary` / `textual-gradient` / `tree-search` / `meta-optimizer` | `evolutionary` 5；`refine` 4；`textual-gradient` 1；`tree-search` 1；`meta-optimizer` 1（多值，合计 >9） | 按实际搜索机制，不按论文自称。刻意不含纯 prompt 优化（OPRO / Self-Refine 谱系）；SEVerA 的 CEGIS 记 `tree-search`，GRPO 记 `meta-optimizer`。 |
| **D** 保证强度 | 有什么保证？ | `none` / `empirical` / `formal` / `formal-safety` | `empirical` 7；`none` 1；`formal-safety` 1；`formal` 0 | `empirical`=只保留分数/偏好提升的变体；`formal-safety` 需把规格、假设、资源边界一起写。SEVerA 保证功能正确性，不覆盖 token/时间/调用成本。 |
| **E** 递归深度 | 递归到哪一层？ | `one-shot` / `iterative` / `full-rsi` / `co-evolution` | `one-shot` 1；`iterative` 1；`full-rsi` 1（+1 候选）；`co-evolution` 0；**待精读 5** | **以作者自我界定为准**；找不到写「待精读」，不按轮数升级。STOP 原文「not full RSI」；DGM 明确 full-rsi；RHO 明确单轮；SICA 自称 fully self-improving，记候选。 |

## 读表提示

- **A 轴过宽的风险**：`code` 吞下 6/9，可能把「代码本体」「代码实现的控制流」「代码实现的工具」混在一起。精读后若要拆轴，按 `AXES.md` 的修订记录流程走，不在这里私改。
- **E 轴是最大缺口**：9 篇里只有 3 篇能在 E 轴找到作者明确界定（STOP、DGM、RHO），另有 SICA 为 `full-rsi` 候选；其余 5 篇只能记「待精读」。这不是我们没读，而是作者没有用 RSI 框架自我界定。
- **D 轴不是质量排名**：`formal-safety` 只在 SEVerA 出现，不等于它「最好」；它的规格由人给出、资源无感知。
- **B 轴独立性**：`external-verifier` 占 6/9，但「外部」不等于「独立」；要查验证集是否与搜索集隔离（争议 Q1/Q2）。

## 与 `AXES.md` 的关系

本表只做压缩，不修改任何轴定义。若精读后发现轴需要修订，按 `notes/AXES.md` 文末「修订记录」留痕；P2 的初步建议见 [`findings.md`](findings.md) §4。
