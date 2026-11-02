# P3 · CP4 一致性校对清单

> 负责人：P3（szh）｜建档：2026-11-01｜**执行时点：2026-11-02（汇报当天）上午**
> 规则（`midpre-checkpoint.md` §7.5）：**CP4 只看一致性**——数字、论文 ID、术语、链接、计时；**不再加新内容**。
> 用法：从 §1 到 §6 逐项打勾；§7 是别人的文件，**只登记不代改**。
> ⏱ 倒计时：T = 2026-11-02（周一）；Q&A 6 条待确认必须在 **11-01 晚**闭环，否则汇报时不能说「我们」。

---

## 1. 数字（以 `refs/verified.csv` 与 P1 统计为准）

| # | 正确值 | 出处 | 常见错法 |
|---|---|---|---|
| 1.1 | **19 篇**入库、19 张 skim | `p1/stats.md` §1；`p1/funnel.md` §1 | 写成 17 篇（P4 `risk.md` R1/R4 仍是旧数） |
| 1.2 | **4 / 19 = 21%** 有可核验录用 | `p1/stats.md` §2 | 说成「文献池已核验」 |
| 1.3 | **0 / 12**：2026 年 12 篇无录用记录 | 同上 | 只说 63% 加速，不提 0 篇 |
| 1.4 | 149 检索 → 约 50 标题筛查 → 2 新增 → 19 池 → 19 skim → 7 精读候选 → **0 已精读** | `p1/funnel.md` §1 | 把 149 说成「读了 149 篇」 |
| 1.5 | **9 篇**核心样本（7 精读 + SICA、MGM） | `p2/classification.md` §1 | 说成「19 篇分类」 |
| 1.6 | 主 A 值：`code` **6** / `control-flow` 1 / `tool` 1 / `memory` 1 | 同上计数行 | 说 7/9（把 ADAS 记成 code） |
| 1.7 | E 轴：可落位 **3** + 候选 1 + **待精读 5** + `co-evolution` 0 | 同上；`p2/findings.md` §2 | ❌「递归深度集中在 one-shot / iterative」 |
| 1.8 | `co-evolution` / `evaluator` / `context` 主值均为 **0** | 同上 | 说「evaluator 有 DGM」（DGM 的评测固定） |
| 1.9 | B：external 6 / failure 2 / self 1；D：empirical 7 / formal-safety 1 / none 1 | 同上 | 把 D 轴 `none` 忽略掉 |
| 1.10 | RHO：0.59→0.78、0.71→0.76、0.29→0.37；最偏好 0.78 vs 测试最高 0.85；agent calls 103 / 41 / 320 | `notes/skim/arxiv-2606.05922.md` | 把 0.85 说成 RHO 的成绩 |
| 1.11 | SEVerA：97.0% / 66.0% / 52.6%；1.9–2.5× slowdown；18.2 s/instance | `notes/skim/arxiv-2603.25111.md` | 说「零违规 = 安全」 |
| 1.12 | DGM：SWE-bench 20.0%→50.0%；约 $22,000 / 2 周 | `p2/classification.md` ③ | 把 50.0% 说成全量 SWE-bench |
| 1.13 | 7 篇、2/2/2/1、D1–D14 | `p4/plan.md` §2–§3 | 说「四周」或「每人两篇」 |
| 1.14 | 计时 **280 s = 4:40** | `deck-outline.md` | 按 10 分钟版排练 |

## 2. 论文 ID 与 venue（最容易出错，逐条核）

**可以说会议/期刊的只有 4 篇：**

| ID | 写法 | 备注 |
|---|---|---|
| `arxiv-2310.02304` | STOP，COLM 2024（Spotlight） | `venue_verified: true` |
| `arxiv-2408.08435` | ADAS，ICLR 2025 | 精读以 ICLR 版为准，不用 arXiv v1 |
| `arxiv-2505.22954` | DGM，ICLR 2026 | `year` 记 2025（首发年） |
| `arxiv-2507.21046` | Gao 等，TMLR 2026 | 种子综述，不作证据 |

**只能写 arXiv preprint 的：** SICA（自述投 NeurIPS 2025）、AlphaEvolve（白皮书）、Self-Harness、RHSI、Code as Agent Harness、MGM、RHO、Harness≠Benefit、SEVerA、以及全部 5 篇综述（DCRI 为 Preprints.org）。

**专项检查：**

- [ ] SEVerA 标题用 v3 全称 **"Verified Synthesis of Self-Evolving Agents"**（旧卡少一个 Synthesis）
- [ ] 不把 DGM 的 `org` 写成只有 Sakana AI（原文含 UBC + Vector，待 P1 补）
- [ ] 不把 RHO/MGM 的作者自述录用（EMNLP Findings / 未核验）写成已录用
- [ ] 不把 Meta 的 Code as Agent Harness、Alibaba 的 Safety survey 当工业界**实证**

## 3. 术语与轴标签

- [ ] `harness` / `scaffold` / `trajectory` / `archive` 不硬译
- [ ] 轴值统一用代码体：`one-shot`、`iterative`、`full-rsi`、`co-evolution`、`self-preference`、`formal-safety`
- [ ] A 轴一律写「主值（次值）」，不写「主 / 次都要算」
- [ ] 「灰带」「待精读」「未自我界定」是同一件事的三种说法，**同一页只用一种**
- [ ] 区分 `self-evolving`（作者用词）与 RSI（本组定义）：前者不自动等于后者
- [ ] 不写「DGM 实现完整 RSI」——补「仅在代码层，archive / 父代选择固定」

## 4. 计时与页数

- [ ] 7 页正文 + 3 页 backup，正文 280 s
- [ ] 每页预算：20 / 35 / 60 / 40 / 40 / 55 / 30
- [ ] 完整计时排练 ≥1 次，记录实际用时；超时先砍 P2 右栏，再砍 P4 的 ADAS 脚注
- [ ] 投影距离下标题 30 pt、关键句 15–18 pt、表格/脚注 9–12.5 pt 可读；现场用 PowerPoint 预览确认
- [ ] 5 分钟口径已在 `RSI_Harness_Writing/group/slides/outline.md` 顶部标注（10 分钟版是第三次课用，不要混）

## 5. 链接

- [ ] 所有 arXiv 链接为 `https://arxiv.org/abs/<id>` 且可打开
- [ ] 引用仓库链接指向 `Gray-Su427/RSI_Harness_Reading`
- [ ] deck 内图片路径在打包后仍可显示（pptx 已内嵌图片，无需外链）
- [ ] backup 页的 `p3/qa-signoff.md`、`p2/classification.md` 路径存在于仓库

## 6. Backup 就绪

- [ ] B1：8 条 Q&A（`RSI-Harness-中期汇报-2026-11-02.pptx` 第 8 页）
- [ ] B2：9 篇分类总表（第 9 页）
- [ ] B3：149→50→2→19 漏斗、4 篇录用、关键数字（第 10 页）
- [ ] 备选：`p2/classification.md` §3 的 E 轴原话表（提问「作者到底怎么说的」时用）
- [ ] 现场能在 3 秒内翻到最后三页

---

## 7. 待他人处理（P3 只登记，不代改）

> 以下都在别人的文件里，按仓库分工由本人改；P3 在 CP4 会议上逐条点掉。

### P1（`refs/verified.csv`，7 组；完整 20 条见 `p2/classification.md` §4）

| 论文 | 字段 | 现值 | 建议 |
|---|---|---|---|
| RHO | `axis_e_recursiveness` | `iterative` | **`one-shot`**（作者明确单轮） |
| STOP | `axis_e_recursiveness` | `one-shot` | `iterative`，或保留 + `note` 说明口径 |
| DGM | `axis_a_object` | `code;evaluator` | **`code`**（次值 `tool;prompt;context`） |
| DGM | `org` | `Sakana AI` | 补 UBC + Vector Institute |
| ADAS | `axis_e_recursiveness` | `one-shot` | `unknown`（无作者界定） |
| AlphaEvolve / MGM | `axis_e_recursiveness` | `one-shot` / `iterative` | `unknown` |
| SICA | `axis_b_signal` / `axis_c_search` / `axis_e_recursiveness` | `failure-trajectory` / `evolutionary` / `iterative` | `external-verifier` / `refine` / `full-rsi`（候选）或加 note |

> 完整依据见 `p2/classification.md` §4（20 条建议）。

> 2026-11-01 进度：**P4 三个文件的过期表述已由 P3 代改**（下表标 ✅，改后口径与 deck P7 的风险一行、B1 的 Q&A 一致）；**P1 的 7 组 CSV 与仓库文档 17→19 仍未执行**（P1 会上定）。

### P4（3 处过期表述）—— ✅ 已改，2026-11-01

| 文件 | 原现文 | 改为 | 状态 |
|---|---|---|---|
| `p4/plan.md` §1 | 「汇报日期尚未提供…D1 待确认」 | T = **2026-11-02**；D1–D14 = **2026-11-03 – 11-16** | ✅ |
| `p4/plan.md` §4 | 「日期由 P3（szh）确认」 | 已映射：T−2=10-31、T−1=11-01、T=11-02 | ✅ |
| `p4/risk.md` R1 | 「CSV 中 17 篇…均为 `false`」 | 19 篇、4 篇 `true`；标题改「已关闭」 | ✅ |
| `p4/risk.md` R4 | 「当前 CSV 仍为 17 篇…尚未核验」 | 19 篇，两篇已入库；标题改「已关闭」 | ✅ |
| `p4/qa.md` Q1 | 「同行评审项仍待 venue 核验」 | 已由 STOP / ADAS / DGM 满足 | ✅ |

> 另：`p4/risk.md` 的「四行摘要」表已加状态列（R1/R4 已关闭、R2/R3 仍开放）、进程风险已改 T=11-02；`p4/qa.md` Q2 改为直接报 19 篇，供稿状态补 2/8。以上均在两文件末尾留了修订记录。

### P2（联动）

- 若 P1 采纳 §7 的 CSV 更正，`p2/classification.md` §4 的「建议」列应标为「已采纳」，图不需重画（图按 P2 口径，不按 CSV）。

### P1（仓库文档里的旧数字，17 → 19）

> 提问环节若有人翻仓库，会看到「17 篇」与 deck 的「19 篇」不一致，属于可信度风险。以下都是 P1 维护的文档，P3 不代改。

| 文件 | 行 | 现文 | 改为 |
|---|---|---|---|
| `RSI_Harness_Reading/README.md` | 51、84、99、143 | 「17 篇」「当前 17 篇全部为 `false`」 | 19 篇；4 篇 `true` |
| `RSI_Harness_Reading/refs/README.md` | 9、43 | 「当前 17 篇」「全部为 `false`」 | 19 篇；4 篇 `true` |
| `RSI_Harness_Reading/AGENTS.md` | 65、265 | 「17 篇，venue_verified 全为 false」 | 加一行注：2026-10-31 已扩到 19 篇、4 篇 `true`（历史表述保留） |

### P3（已完成）

- [x] `narrative.md` 第 2 句已按 P2 修正（不写「集中」）
- [x] deck 第 3 页灰带表述与 `taxonomy-ae.md` §2 一致
- [x] Q5 / Q6 已确认（`qa-signoff.md`）

---

## 8. 校对签字

> CP4 会议：**2026-11-02（周一）上午**，≤20 分钟；只回答「过了没有、差什么、谁补」。

| 人 | 检查范围 | 结论 | 日期 |
|---|---|---|---|
| P1（xyc） | §1、§2、§7 CSV 与仓库文档 |  |  |
| P2（zyc） | §1 分类数字、§3 轴标签 |  |  |
| P3（szh） | 全文（初校） | 通过 | 2026-11-01 |
| P4（zgj） | §4 计时、§7 风险与 Q&A |  |  |
