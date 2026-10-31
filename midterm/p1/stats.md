# P1 · 19 篇文献池结构统计

> 负责人：P1（xyc）｜统计日期：**2026-10-31**｜数据源：[`../../refs/verified.csv`](../../refs/verified.csv)（19 行）
> 生成方式：`python` 读 CSV 直接计数（`csv.DictReader`），**没有手工抄数**。任何人重跑都能得到同一组数字。
> 口径：`year` 记 arXiv/首发年（不记会议年，见 [`venue-verification.md`](venue-verification.md) §2.3）；`industry` 按「署名含企业机构」；`role` 为四类枚举。

---

## 1. 年份分布（n = 19）

| 年份 | 篇数 | 占比 | 论文 |
|---|---|---|---|
| 2023 | 1 | 5.3% | STOP |
| 2024 | 1 | 5.3% | ADAS |
| 2025 | 5 | 26.3% | SICA、DGM、AlphaEvolve、2508.07407、2507.21046 |
| 2026 | 12 | 63.2% | Self-Harness、RHI、Code as Harness、MGM、RHO、Harness≠Benefit、SEVerA、2607.13104、2610.00093、2603.25681、2607.07663、DCRI |
| **合计** | **19** | 100% | |

**结论**：2026 年一篇顶三年。但「新」不等于「已被检验」——**这 12 篇 2026 工作里，0 篇有可核验的录用记录**（见 §2）。

---

## 2. venue 分布（n = 19）

| 类型 | 篇数 | 占比 | 明细 |
|---|---|---|---|
| 已核验的同行评审（会议/期刊） | **4** | 21.1% | COLM 2024（STOP，Spotlight）· ICLR 2025（ADAS）· ICLR 2026（DGM）· TMLR 2026（2507.21046） |
| arXiv preprint | **14** | 73.7% | 其余全部 |
| Preprints.org 预印本 | **1** | 5.3% | DCRI（`venue-2026-dcri-survey`） |
| **合计** | **19** | 100% | |

**关键交叉事实**：4 篇已核验的都是 **2023–2025** 的工作；**2026 年的 12 篇，录用状态全部未知**。
**口径约束**：「2026 年明显加速」与「2026 年的工作尚未经同行评审确认」必须同时成立，前者来自本节，后者来自 §2。

> 与 CP0 时点的对比：当时 17 篇的 `venue_verified` **全为 false**；本轮把 3 篇 seed + 1 篇综述核成 `true`，
> 但仍只占 21%。所以 Gate 2 的「同行评审」项**现在可以从「无」变成「有」**（STOP / ADAS 任一即可），
> 而「全部核验」不是 CP1 的目标，也不应承诺。

---

## 3. industry 分布（n = 19）

| 取值 | 篇数 | 占比 | 论文 |
|---|---|---|---|
| `true`（署名含企业机构） | **11** | 57.9% | STOP、SICA、DGM、SEVerA、Code as Harness、RHO、Harness≠Benefit、RHI、AlphaEvolve、2610.00093、DCRI |
| `false` | **8** | 42.1% | ADAS、Self-Harness（上海 AI Lab 属国家实验室）、MGM、2507.21046、2508.07407、2603.25681、2607.07663、2607.13104 |
| **合计** | **19** | 100% | |

⚠️ **`industry: true` ≠ 可作 Gate 2 的工业界实证**。11 篇里有 3 篇没有自我改进效果证据：

| 不可作实证 | 原因 |
|---|---|
| Code as Agent Harness（Meta 等） | 综述/立场文，无方法无实验 |
| Safety in Self-Evolving Agents（Alibaba/OPPO/Rakuten） | 综述 |
| DCRI（JD Future Academy） | 综述，且未同行评审 |

→ **实际可用于 Gate 2 工业界项的只有 8 篇**（STOP、SICA、DGM、SEVerA、RHO、Harness≠Benefit、RHI、AlphaEvolve）。

---

## 4. role 分布（n = 19）

| role | 篇数 | 占比 | 说明 |
|---|---|---|---|
| `seed` 课程种子 | 4 | 21.1% | STOP、ADAS、SICA、DGM |
| `harness-core` 直接命中 harness 自进化 | 7 | 36.8% | Self-Harness、RHI、Code as Harness、MGM、RHO、Harness≠Benefit、SEVerA |
| `industry` 工业界应用面 | 1 | 5.3% | AlphaEvolve |
| `survey` 综述 | 7 | 36.8% | 2507.21046、2508.07407、2603.25681、2607.07663、2607.13104、2610.00093、DCRI |
| **合计** | **19** | 100% | |

**交叉表（role × industry）**：

| role | industry=true | industry=false | 小计 |
|---|---|---|---|
| seed | 3（STOP、SICA、DGM） | 1（ADAS） | 4 |
| harness-core | 5（RHI、Code as Harness、RHO、Harness≠Benefit、SEVerA） | 2（Self-Harness、MGM） | 7 |
| industry | 1（AlphaEvolve） | 0 | 1 |
| survey | 2（2610.00093、DCRI） | 5 | 7 |
| **合计** | **11** | **8** | **19** |

**结论**：综述占 36.8%，意味着**每 3 篇就有 1 篇不能进 evidence 文件**；`harness-core` 7 篇是全部可用的「直接命中」样本，恰好等于 P4 冻结的精读数（7 篇里有 4 篇进了精读名单，另 3 篇因综述性质或证据重叠被排除）。

---

## 5. 本轮相对 CP0 的元数据变更（留痕）

| 变更 | 涉及 ID | 依据 |
|---|---|---|
| `venue_verified: false → true` | `2310.02304`、`2408.08435`、`2505.22954` | 会议官网 accepted papers / 论文集（见 venue-verification.md） |
| 新增（含 `true`） | `2507.21046`（TMLR 2026） | arXiv HTML 的 OpenReview 标注 + ML Anthology TMLR 2026 索引 |
| 新增（`false`） | `venue-2026-dcri-survey` | Preprints.org 预印本，非同行评审 |
| **标题更正** | `2603.25111` | 旧记 “SEVerA: Verified Self-Evolving Agents”；**arXiv v3（2026-10-15）实为 “SEVerA: Verified Synthesis of Self-Evolving Agents”** |
| 备注更正 | `2605.18747` | 旧 note 称「PDF 实列 52 位作者」，arXiv 元数据为 **42 位**，与 CSV 一致；该说法撤下 |
| 备注补充 | `2606.05922`、`2603.25681` | 作者自述 EMNLP 2026 Findings / TMLR 录用，**未取得第三方核验，venue 仍记 arXiv preprint** |
| 备注补充 | `2606.09498`、`2607.15524`、`2608.07645`、`2605.30621` | 补代码链接与作者自述的循环边界 |

> 以上改动均可由 `git diff refs/verified.csv` 复核；**没有改动任何 `axis_*` 列**——五轴属于 P2/CP2，本轮不越界。
