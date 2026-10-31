# P2 · 三条初步发现（CP2）

> 负责人：P2（zyc）｜日期：2026-10-31｜每条先给一句话判断，再给支撑与反例。
> 数据：9 篇核心论文（7 篇精读候选 + 2 篇泛读补充），分类见 [`classification.md`](classification.md)，图见 [`taxonomy-ae.svg`](taxonomy-ae.svg)。

## 发现 1 · 密集区：A 轴高度集中在 `code`，但 E 轴并不集中

**一句话：9 篇里 6 篇的主 A 值是 `code`，但只有 3 篇能在 E 轴找到作者明确界定（STOP=`iterative`、DGM=`full-rsi`、RHO=`one-shot`；SICA 为 `full-rsi` 候选），5 篇只能记「待精读」——「改什么」有共识，「递归到哪层」没有。**

支撑：

- A 轴主值：`code` 6（STOP、DGM、AlphaEvolve、SEVerA、SICA、MGM）、`control-flow` 1（ADAS）、`tool` 1（RHO）、`memory` 1（Harness≠Benefit）。
- E 轴：明确界定 3 + 候选 1；待精读 5（ADAS、AlphaEvolve、SEVerA、Harness≠Benefit、MGM）。
- 图中 `code` 列从 `full-rsi` 一直延伸到「待精读」带，说明同一改进对象可以对应不同递归深度；A 轴不能替代 E 轴。

反例 / 边界：

- AlphaEvolve 的 A 也是 `code`，但改的是任务算法，不是 harness 自身；把它算进「code 密集区」会高估 harness 自进化的样本量。
- ADAS 的 A 主值有 `control-flow` / `code` 两种读法；若改记 `code`，密集区会变成 7/9，说明 A 轴粒度需要精读后复核。

对 P3 的用法：

- 可说：「本组样本的共识在改进对象（代码），不在递归深度；E 轴 5/9 没有作者界定。」
- 不要说：「9 篇都在做 code 自进化」——AlphaEvolve 是边界对照。

## 发现 2 · 空白：高递归与高保证的格点基本是空的

**一句话：`co-evolution` 行没有完成闭环的样本，`evaluator` / `context` 两列没有主值样本，`full-rsi` 只有 DGM 明确宣称，`formal-safety` 只有 SEVerA——高递归、高保证的区域是空白，不是已被占领。**

支撑：

- E 轴：`co-evolution` 0；`full-rsi` 1（DGM）+ 1 候选（SICA）；`one-shot` 1（RHO）；`iterative` 1（STOP）；待精读 5。
- A 轴：`evaluator` 0、`context` 0；DGM 的 evaluator/archive/parent selection 是固定边界，不是改进对象。
- D 轴：`formal-safety` 1（SEVerA）；`empirical` 7；`none` 1。
- B 轴：`external-verifier` 6（主值）；`self-preference` 1（RHO）；`failure-trajectory` 2（Harness≠Benefit、MGM）。

反例 / 边界：

- RHSI（`arxiv-2607.15524`）自称 recursive / co-evolution，但作者明确说只做「递归循环的前半段」，所以不填入 `co-evolution`；这是「声称」与「完成」的差别。
- SEVerA 的 `formal-safety` 只覆盖功能正确性，不覆盖 LLM calls / token / wall-clock；不能把「零违规」扩展为「安全」。
- RHO 的 `self-preference` 是唯一正面样本，但作者自己报告「最偏好 ≠ 测试最高」；它不是「验证独立性」的解决方案。

对 P3 的用法：

- 可说：「空白比密集区更有信息量：`co-evolution`、`evaluator`、`context` 都还没有稳定样本。」
- 不要说：「DGM 已经实现完整 RSI」——DGM 的 archive/父代选择固定、FM 权重冻结，`full-rsi` 只在代码层。

## 发现 3 · 反例：三篇边界工作说明五轴只能「标注」，不能「强行单值」

**一句话：AlphaEvolve（改任务算法而非 harness）、Harness≠Benefit（测量研究，A/B 不是其贡献）、SEVerA（Learn 改权重，跨界到模型层）三篇说明五轴对边界工作只能做标注；同时 STOP/RHO 的 CSV 标签与作者原话冲突，第一版分类必须保留「待精读」和「边界」标记。**

支撑：

- **AlphaEvolve**：A=`code`，但对象是任务算法；pipeline（prompt、LLM ensemble、program database、evaluator）固定；E 无 RSI 自我界定 → 边界对照，不作 harness 自进化证据。
- **Harness≠Benefit**：A/B 记录的是被测协议（skills / prompts / memories），不是本文提出的方法；C 沿用 solve-evolve；D=`none`；E 协议 T 步迭代但作者未自我界定 → 测量研究，不能当方法论文。
- **SEVerA**：Search 合成程序（`code` / `control-flow`），Learn 用 GRPO 改权重 → 跨界到模型层；D=`formal-safety` 但资源无感知；E 未界定。
- **CSV 冲突**：STOP `one-shot` vs 作者「not full RSI」+ 迭代机制；RHO `iterative` vs 作者「single round, no claim of compounding」；DGM `code;evaluator` vs 原文「archive/parent selection fixed」。这些不是笔误，而是「轴的定义口径」没有统一。

反例 / 边界：

- 如果为了凑「7–9 篇都是 harness RSI」而把 AlphaEvolve、Harness≠Benefit、SEVerA 强行归入，会直接违反 AGENTS §9「不替作者下结论」。
- 反过来，如果因为边界工作就删掉它们，会失去工业对照、测量效度和形式化保证三条重要证据；正确做法是保留并标注「边界」。

对 P3 的用法：

- 可说：「我们的分类不是把 9 篇压成 9 个标签，而是标出 3 篇边界和 5 个待精读；这本身就是中期结论。」
- 不要说：「9 篇都是同质样本，可以直接统计分布」——当前分布是工作假设，不是最终统计。

## 4. 轴修订建议（只提议，不擅自改）

> 按 `AGENTS.md` §9.6，修改分类轴必须留修订记录；以下只是 P2 的提议，供精读后讨论。

1. **A 轴 `code` 可能过宽**：6/9 落在 `code`，而 `code` 同时承载控制流、工具、prompt。建议精读后讨论是否增加「改动载体 vs 改动功能」子字段，或把 `code` 拆成 `code-body` / `code-defined-flow`；在未修订前，表中保留主值/次值。
2. **E 轴需要「作者是否自我界定」的显式字段**：当前 5/9 只能记「待精读」，说明 E 轴不能只靠机制观察。建议在精读笔记中固定追问「作者是否声称改进了改进器本身？」并逐字摘录；找不到就记 `unknown`。
3. **D 轴 `empirical` 过宽**：7/9 都是 `empirical`，但它同时覆盖「benchmark 筛选」「自偏好门控」「测量研究」。建议精读后讨论是否区分「经验筛选」与「仅经验报告」；在未修订前，用 note 说明。

## 5. 给 P3 的一句话总结

**本组 9 篇的共识是「改代码」，分歧是「递归到哪层」；高递归（`full-rsi` / `co-evolution`）和高保证（`formal-safety`）都还是单点或空白，5/9 的 E 轴需要作者原话才能落位。**
