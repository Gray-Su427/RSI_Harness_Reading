# A×E 体系图说明（CP2）

> 负责人：P2（zyc）｜日期：2026-10-31｜状态：CP2 工作稿，待组内评审
>
> 图文件：[`taxonomy-ae.png`](taxonomy-ae.png)（300 dpi，放 deck）｜[`taxonomy-ae.svg`](taxonomy-ae.svg)（矢量，文字已转路径）
> 生成脚本：[`make_taxonomy_ae.py`](make_taxonomy_ae.py)｜数据源：[`classification.md`](classification.md) §1

## 1. 图注（可直接放进 deck）

**图 1 · Harness 自进化的 A×E 体系图。** 横轴为 A 轴「改进对象」的七个取值，括号内是 9 篇核心论文中按主值计数的篇数；纵轴为 E 轴「递归深度」，底部灰色带为「E 未找到作者自我界定」的待精读区。橙色表示工业界 / 产学合作（`industry: true`），蓝色表示学术界；圆点为 7 篇精读候选，菱点为 2 篇泛读补充；虚线外圈表示待精读、边界或候选状态。点的纵向位置只在有作者明确界定 E 时给出，**不按论文轮数推断**。

## 2. 30 秒读图

1. **先看密集区**：`code` 列有 6/9，说明「改代码」是本组样本的共同点；但同一列从 `full-rsi` 一直延伸到「待精读」带，说明**改什么**与**递归到哪层**是两件事。
2. **再看空白**：`co-evolution` 行为空，`evaluator`、`context` 两列为空；`formal-safety` 只有 SEVerA 一个点。空白本身就是中期结论，不要补点。
3. **最后看底部灰带**：5 篇（ADAS、AlphaEvolve、SEVerA、Harness≠Benefit、MGM）没有作者对 E 轴的自我界定，统一放在「待精读」，**不等于 `one-shot`，也不等于低递归**。
4. **边界点**：AlphaEvolve 改的是任务算法，不是 harness 自身；SEVerA 的 Learn 阶段改模型权重，跨界到模型层；Harness≠Benefit 是测量研究，A/B 记的是被测协议而非本文贡献。三点都保留，但不当成 harness RSI 的正面证据。

## 3. 三条可直接口述的读数

- **读数 1（密集）**：9 篇里 6 篇主 A 值是 `code`；但只有 3 篇能在 E 轴找到作者明确界定（STOP=`iterative`、DGM=`full-rsi`、RHO=`one-shot`），另有 SICA 为 `full-rsi` 候选。**共识在改进对象，不在递归深度。**
- **读数 2（空白）**：`co-evolution` 0 篇；`evaluator`、`context` 作为主值 0 篇；`full-rsi` 只有 DGM 明确宣称，`formal-safety` 只有 SEVerA。**高递归与高保证的格点基本是空的。**
- **读数 3（边界）**：AlphaEvolve、SEVerA、Harness≠Benefit 三篇说明五轴对边界工作只能「标注」，不能「强行单值」；图中用虚线外圈和文字注记保留其边界身份。

## 4. 这张图不主张什么

- **不是完整文献地图**：n=9，来自 P4 的 7 篇精读名单 + P2 的 2 篇泛读补充，存在选择偏差；不能据此估计整个领域的分布。
- **不是质量排名**：纵轴高不代表更好；`full-rsi` 只在代码层，`formal-safety` 只覆盖功能正确性。
- **不是最终 E 标签**：底部灰带是「作者未自我界定」，不是「我们判定为低递归」；精读找到原话后才移动点位。
- **不是精确坐标**：同一格内的点做了少量横向偏移以免重叠；A 轴计数只按主值，次值未在图中展开。
- **不把 DGM 说成模型层 RSI**：DGM 的 FM 权重冻结、archive/父代选择固定，`full-rsi` 只在 agent codebase 层。
- **不把 AlphaEvolve 说成 harness 自进化**：它优化任务算法与基础设施，pipeline 本身不是改进对象。

## 5. deck 用法建议

- **一页只讲一件事**：先让听众看 `code` 列的密度，再让他们看底部灰带；不要在同一页塞五轴定义。
- **建议讲稿**：「我们把 9 篇放在同一张 A×E 图上。改代码是共识，6/9；但递归到哪层没有共识，5/9 连作者自己的界定都找不到。我们没有替作者填，而是把它们放在底部灰带。空白处——共进化、评测器、上下文——目前没有稳定样本。」
- **互动点**：如果听众问「为什么 AlphaEvolve 不算 harness RSI」，指向 `code` 列底部灰带旁的「边界：任务算法」注记，再补一句「它的 prompt、LLM ensemble、program database、evaluator 都是固定外壳」。
- **备份页**：把 [`classification.md`](classification.md) §3 的 E 轴原话表作为 backup，现场只引用，不展开。

## 6. 复现

```bash
cd midterm/p2
python make_taxonomy_ae.py
```

依赖：Python 3 + `matplotlib`；中文字体优先 `Microsoft YaHei`，缺失时回退 `Noto Sans SC` / `SimHei`。脚本输出 `taxonomy-ae.png`（300 dpi）与 `taxonomy-ae.svg`（`svg.fonttype = "path"`，避免换机字体错位）。

**改图顺序**：先改 [`classification.md`](classification.md) 的总表与依据 → 再改脚本里的 `PAPERS` / `A_LABELS` → 重跑脚本 → 更新本说明的计数与图注。不要只改图不改表。

## 7. 版本

| 日期 | 版本 | 改动 |
|---|---|---|
| 2026-10-31 | v0.1 | 首版：9 篇、7 个 A 取值、4 个 E 层级 + 待精读带；DGM/STOP/RHO/SEVerA 标注 |
