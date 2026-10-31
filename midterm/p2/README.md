# P2 交付索引（分类体系与图）

> 负责人：P2（zyc）｜日期：2026-10-31｜状态：**CP2 工作稿已交，待组内评审/冻结**
>
> 本目录只放 P2 的中期材料；论文元数据以 [`../../refs/verified.csv`](../../refs/verified.csv) 为准，轴定义以 [`../../notes/AXES.md`](../../notes/AXES.md) 为准。P2 **没有**修改 CSV，也没有修改 `AXES.md`。

## 1. 交付物

| 文件 | 内容 | 对应 CP2 要求 | 状态 |
|---|---|---|---|
| [`axes-overview.md`](axes-overview.md) | 五轴速览表（5 行） | 五轴表 5 行 | ✅ 工作稿 |
| [`classification.md`](classification.md) | 9 篇分类总表 + 逐篇依据 + E 轴原话 + CSV 回填建议 | 分类总表 7–9 篇 | ✅ 工作稿 |
| [`taxonomy-ae.png`](taxonomy-ae.png) | A×E 体系图，300 dpi，放 deck | A×E 图 7–9 个点 | ✅ 工作稿 |
| [`taxonomy-ae.svg`](taxonomy-ae.svg) | 同上，矢量版（文字转路径） | 备份 / 缩放 | ✅ 工作稿 |
| [`taxonomy-ae.md`](taxonomy-ae.md) | 图注、30 秒读图、图不主张什么、deck 用法、复现 | 图的说明 | ✅ 工作稿 |
| [`findings.md`](findings.md) | 3 条初步发现：密集区、空白、反例 | 2–3 条发现 | ✅ 工作稿 |
| [`dgm-brief.md`](dgm-brief.md) | DGM 讲述级五问卡 | P2 认领论文 | ✅ 讲述级 |
| [`alphaevolve-brief.md`](alphaevolve-brief.md) | AlphaEvolve 讲述级五问卡 | P2 认领论文 | ✅ 讲述级 |
| [`make_taxonomy_ae.py`](make_taxonomy_ae.py) | 图的可复现生成脚本 | 复现 | ✅ 可运行 |

**未完成 / 不在 P2 范围**：完整 Schema 精读（`notes/deep/`）、venue 核验、`refs/verified.csv` 回填、deck 合并。以上分别由 P1 / P3 / P4 负责或中期后完成。

## 2. 五条口径（评审时先看这五条）

1. **样本是 9 篇，不是 17 篇**：7 篇 P4 精读名单（STOP、ADAS、DGM、AlphaEvolve、RHO、SEVerA、Harness≠Benefit）+ 2 篇 P2 泛读补充（SICA、MGM）。图与表都只覆盖这 9 篇。
2. **E 轴以作者自我界定为准**：找不到作者原话就记「待精读」/ `unknown`，不按「多轮循环」推断 `iterative`。目前 5/9 在待精读带。
3. **A 轴记主值（次值）**：总表与图只按主值计数；次值写在括号里。DGM 的次值是 `tool/prompt/context`，**不是 `evaluator`**。
4. **边界工作保留，不强行归类**：AlphaEvolve 改任务算法、SEVerA 跨界到模型层、Harness≠Benefit 是测量研究；三篇都保留并标注边界，不作为 harness RSI 的正面证据。
5. **【原文】与【本组判断】分开**：五问卡逐条引用作者原话；我们的推论、口径冲突、CSV 建议都标【本组判断】。

## 3. 给 P3 的三句话（可直接改写成 deck 叙事）

1. **现状**：9 篇里 6 篇的主 A 值是 `code`，「改代码」是共识；但 E 轴只有 3 篇能找到作者明确界定（STOP=`iterative`、DGM=`full-rsi`、RHO=`one-shot`），SICA 是 `full-rsi` 候选，**5 篇待精读**。
2. **缺口**：`co-evolution` 为 0，`evaluator` / `context` 作为主值为 0，`formal-safety` 只有 SEVerA；**高递归与高保证的格点基本是空白，不是已被占领**。
3. **计划**：精读优先补 5 篇的 E 轴原话，统一 STOP / RHO / DGM 的 CSV 口径，再用 7 篇验证「递归深度是否被高估、验证独立性是否被低估」。

### ⚠️ 对 P3 现有叙事的一句修正

`midpre-checkpoint.md` 的 P3 草稿写「递归深度集中在 `one-shot` / `iterative`」。按 P2 当前材料，这句话**不成立**：能落位的只有 3 篇，分别落在 `one-shot`、`iterative`、`full-rsi` 三档；另有 5 篇作者未自我界定。建议改成：

> 「已能落位的 3 篇分别落在 one-shot、iterative、full-rsi，另有 5 篇待精读；递归深度不是集中，而是**大面积未界定**。」

## 4. 已知口径冲突（交 P1 / P3，不在 P2 私改）

| 论文 | CSV 现值 | P2 表 / 卡 | 处理建议 |
|---|---|---|---|
| STOP | `axis_e_recursiveness = one-shot` | `iterative`（作者只否认 full RSI） | P1 核验后统一，或在 `note` 说明口径 |
| RHO | `axis_e_recursiveness = iterative` | `one-shot`（作者明确单轮、不声称累积） | **建议 P1 更正为 `one-shot`** |
| DGM | `axis_a_object = code;evaluator` | `code`（archive/父代选择/评测固定） | **建议 P1 更正为 `code`**，次值写 `tool;prompt;context` |
| ADAS | `axis_a_object` 未定主值 | 表暂记 `control-flow` 主、`code` 次 | P1 / P2 精读后裁定；`AXES.md` 与 skim 卡口径冲突 |
| SICA | `axis_b_signal = failure-trajectory`；`axis_c_search = evolutionary` | `external-verifier`；`refine` | 据 skim 卡：benchmark + utility，archive argmax 单支；建议 P1 核验后更正 |
| SICA | `axis_e_recursiveness = iterative` | `full-rsi`（候选） | P2 精读裁定；暂保留候选标记 |
| AlphaEvolve | `axis_e_recursiveness = one-shot` | `待精读` / `unknown` | 建议改 `unknown`，note 写「产物层 iterative、harness 层不递归」 |
| MGM | `axis_e_recursiveness = iterative` | `待精读` / `unknown` | 正文无自我界定，标题不足以上升 |
| 全部 9 篇 | `venue_verified = false` | 未改 | DGM 的 ICLR 2026 仅据原 skim 卡/PDF 页眉自述，未独立核验；AlphaEvolve 是白皮书 |

> 完整逐条建议见 [`classification.md`](classification.md) §4。**P2 不直接改 CSV**；P1 决定是否写入并在 `note` 留痕。

## 5. 复现与检查

```bash
# 重新生成图（需要 matplotlib；中文字体优先 Microsoft YaHei）
cd midterm/p2
python make_taxonomy_ae.py
```

- 输出：`taxonomy-ae.png`（300 dpi）、`taxonomy-ae.svg`（文字转路径）。
- 改图顺序：先改 `classification.md` 的总表/依据 → 再改脚本 `PAPERS` / `A_LABELS` → 重跑 → 更新 `taxonomy-ae.md` 的计数。
- 检查清单：9 个点是否都在；DGM/STOP/RHO/SEVerA 是否标注；5 个待精读是否在灰带；`co-evolution` / `evaluator` / `context` 是否为空；颜色是否按 `industry` 字段。

## 6. 变更记录

| 日期 | 改动 | 原因 |
|---|---|---|
| 2026-10-31 | 建立 `axes-overview.md`、`classification.md`、`taxonomy-ae.*`、`findings.md` | CP2 首版 |
| 2026-10-31 | 新增 `dgm-brief.md`、`alphaevolve-brief.md` | P2 认领论文的讲述级五问卡 |
| 2026-10-31 | 新增本索引 | 按 `midterm/README.md` 要求索引新文件 |
