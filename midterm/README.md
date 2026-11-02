# 中期汇报材料

> 维护：P3（szh）｜更新：2026-11-01
> 本目录存放中期汇报相关材料；论文元数据与阅读笔记仍在仓库根目录的 `refs/`、`notes/`。

---

## 1. 人员

| 代号 | 姓名 | 角色 |
|---|---|---|
| P1 | xyc | 数据与文献池 |
| P2 | zyc | 分类体系与图 |
| P3 | szh | 边界、叙事与整合；本目录维护 |
| P4 | zgj | 精读计划与风险 |

---

## 2. CP 状态（快照）

| CP | 状态 | 负责人 | 说明 |
|---|---|---|---|
| CP0 | ✅ 通过（2026-10-31） | P3（szh） | 姓名已填；全员已确认认领 |
| CP1 | ✅ 通过（2026-11-01） | P1（xyc） | 19 篇入库、4 篇 venue 已核验、统计/筛选流程图/data brief 齐 |
| CP2 | ✅ 通过（2026-11-01） | P2（zyc） | 9 篇分类表、A×E 图、3 条发现、2 张五问卡 |
| CP3 | 🟡 材料已齐，待 Q&A 确认 | P3（szh） + P4（zgj） | 叙事、6 页 deck、7 篇名单、排期、4 风险、8 Q&A（2/8 已确认） |
| CP4 | 🟡 清单已建，11-02 上午执行 | P3（szh） | 一致性校对清单已建；只查数字/ID/术语/计时 |

> 2026-10-31：P1（xyc）、P2（zyc）、P3（szh）、P4（zgj）已确认认领各自任务（P3 记录）。
> 2026-11-01：CP1 验收通过（venue 核验 4/19、19 篇统计、筛选流程图、data brief、STOP/ADAS 五问卡）；CP2 评审通过并冻结（P3 评审：E 轴按 P2 口径修正）。
> 2026-11-01：P3 交付叙事、6 页 deck（pptx）、RHO/SEVerA 五问卡、CP4 清单、Q&A 确认表（Q5/Q6 已确认）。
> 2026-11-01：**汇报日确定为 2026-11-02（周一）**；CP4 当天上午执行，D1–D14 = 2026-11-03 – 11-16。
> 2026-11-01：汇报时长按 **5 分钟（≤4:40）** 定稿；课程 PPT 的 10 分钟版留给第三次课，两者不混用。
> 状态以 [`../midpre-checkpoint.md`](../midpre-checkpoint.md) 为准；本表只是快照。CP1/CP2 状态由 P3 验收后同步，负责人如有异议在 CP4 会上直接改。

---

## 3. 文件索引

> P4 文件由 P4（zgj）的提交包复制并入；仓库内以本目录版本为准。

| 文件 | 内容 | 负责人 | 状态 |
|---|---|---|---|
| [`p1/venue-verification.md`](p1/venue-verification.md) | 4 篇 seed + 2 篇新增综述的 venue 核验结论与来源 | P1（xyc） | ✅ CP1 证据 |
| [`p1/stats.md`](p1/stats.md) | 19 篇年份 / venue / industry / role 四张分布表 | P1（xyc） | ✅ |
| [`p1/screening-flow.md`](p1/screening-flow.md) | 149 → 约 50 → 2 → 19 → 19 → 7 → 0 的筛选流程图与检索日志 | P1（xyc） | ✅ |
| [`p1/data-brief.md`](p1/data-brief.md) | 3 个数字 + 1 个判断 | P1（xyc） | ✅ |
| [`p1/paper-brief-stop.md`](p1/paper-brief-stop.md) | STOP 讲述级五问卡 | P1（xyc） | 讲述级 |
| [`p1/paper-brief-adas.md`](p1/paper-brief-adas.md) | ADAS 讲述级五问卡 | P1（xyc） | 讲述级 |
| [`p2/README.md`](p2/README.md) | P2 交付索引、五条口径、口径冲突、复现 | P2（zyc） | ✅ CP2 已冻结 |
| [`p2/axes-overview.md`](p2/axes-overview.md) | 五轴速览表（5 行） | P2（zyc） | ✅ |
| [`p2/classification.md`](p2/classification.md) | 9 篇分类总表 + 逐篇依据 + E 轴原话 + CSV 建议 | P2（zyc） | ✅ |
| [`p2/taxonomy-ae.png`](p2/taxonomy-ae.png) | A×E 体系图（300 dpi） | P2（zyc） | ✅ |
| [`p2/taxonomy-ae.svg`](p2/taxonomy-ae.svg) | A×E 体系图（矢量，文字转路径） | P2（zyc） | ✅ |
| [`p2/taxonomy-ae.md`](p2/taxonomy-ae.md) | 图注、30 秒读图、图不主张什么、deck 用法 | P2（zyc） | ✅ |
| [`p2/findings.md`](p2/findings.md) | 3 条初步发现（密集区、空白、反例） | P2（zyc） | ✅ |
| [`p2/dgm-brief.md`](p2/dgm-brief.md) | DGM 讲述级五问卡 | P2（zyc） | 讲述级 |
| [`p2/alphaevolve-brief.md`](p2/alphaevolve-brief.md) | AlphaEvolve 讲述级五问卡 | P2（zyc） | 讲述级 |
| [`p2/make_taxonomy_ae.py`](p2/make_taxonomy_ae.py) | A×E 图生成脚本 | P2（zyc） | 可运行 |
| [`p3/README.md`](p3/README.md) | P3 交付索引、五条口径、待确认事项、复现 | P3（szh） | ✅ CP3 定稿候选 |
| [`p3/narrative.md`](p3/narrative.md) | 1 句核心结论 + 3 句叙事 + 数字锚点 + 禁用表述 | P3（szh） | ✅ |
| [`p3/deck-outline.md`](p3/deck-outline.md) | 6 页逐页内容、280 s 计时、逐页讲稿 | P3（szh） | ✅ |
| [`p3/deck-rsi-midterm.pptx`](p3/deck-rsi-midterm.pptx) | 16:9 deck：6 页正文 + 2 页 backup，含备注 | P3（szh） | ✅ 可放映 |
| [`p3/make_deck.py`](p3/make_deck.py) | deck 生成脚本 | P3（szh） | 可运行 |
| [`p3/rho-brief.md`](p3/rho-brief.md) | RHO 讲述级五问卡 | P3（szh） | 讲述级 |
| [`p3/severa-brief.md`](p3/severa-brief.md) | SEVerA 讲述级五问卡 | P3（szh） | 讲述级 |
| [`p3/cp4-checklist.md`](p3/cp4-checklist.md) | CP4 一致性校对清单 + 待他人处理 7 组 CSV / 3 处过期表述 | P3（szh） | ✅ 待当天执行 |
| [`p3/qa-signoff.md`](p3/qa-signoff.md) | 8 条 Q&A 确认状态；Q5/Q6 定稿；预判追问 5 条 | P3（szh） | 🟡 2/8 已确认 |
| [`p4/plan.md`](p4/plan.md) | 7 篇名单、2/2/2/1 分工、两周排期、T 与 D1–D14 | P4（zgj） | ✅ 定稿候选（11-01 更新） |
| [`p4/risk.md`](p4/risk.md) | 四项风险 + 进程风险补充（R1/R4 已关闭） | P4（zgj） | ✅ 11-01 更新 |
| [`p4/qa.md`](p4/qa.md) | 8 个 Q&A（约 20 秒/条） | P4（zgj）代拟 | 🟡 2/8 已确认 |
| [`p4/p4-paper-brief.md`](p4/p4-paper-brief.md) | P4 论文五问准备卡 | P4（zgj） | 讲述级 |
| [`../midpre-checkpoint.md`](../midpre-checkpoint.md) | 分工与 CP 看板（仓库根目录） | P3（szh） | 🟡（CP0/CP1/CP2 ✅；CP3 待 Q&A；CP4 待当天） |

---

## 4. 待办

- [x] P2（zyc）提交 2 张讲述级五问卡（DGM、AlphaEvolve）；P4 已交 1 张。
- [x] P1（xyc）提交 STOP / ADAS 2 张；P3（szh）提交 RHO / SEVerA 2 张（[`p3/rho-brief.md`](p3/rho-brief.md)、[`p3/severa-brief.md`](p3/severa-brief.md)）。
- [x] P3（szh）确认 T：**2026-11-02（周一）**；时长 5 分钟（≤4:40）。四人实际可用时间回填后校准 D1–D14（2026-11-03 – 11-16）。
- [ ] 四人各确认两条 Q&A（已确认 **2/8**：Q5、Q6 由 P3 定稿，见 [`p3/qa-signoff.md`](p3/qa-signoff.md)）；**截止 11-01 晚**。P3 审阅计划与 deck 口径已完成（[`p3/deck-outline.md`](p3/deck-outline.md)）。
- [x] CP2 评审：P3 已检查 9 篇表、A×E 图、3 条发现；「递归深度集中在 one-shot / iterative」已在 [`p3/narrative.md`](p3/narrative.md) 改为「大面积未界定」（3 篇可落位 + 5 篇待精读）。
- [x] CP1 闭环：两篇种子综述已入库（19 篇）、4 篇 venue 已核验；CP1/CP2 冻结，D1—D14 待 T 确认后启动。
- [x] P4 三处过期表述（`plan.md` T/D1–D14、`risk.md` R1/R4、`qa.md` Q1/Q2）已由 P3 代改（2026-11-01，见 [`p3/cp4-checklist.md`](p3/cp4-checklist.md) §7）。
- [ ] P1 处理 7 组 CSV 轴字段建议（完整 20 条见 `p2/classification.md` §4）与仓库文档 17→19（清单见 [`p3/cp4-checklist.md`](p3/cp4-checklist.md) §7）。
- [ ] CP1—CP4 状态变化时更新 [`../midpre-checkpoint.md`](../midpre-checkpoint.md) 的状态与日期。

---

## 5. 目录约定

- `p1/`、`p2/`、`p3/`、`p4/`：各负责人中期材料；不要把别人的文件移进自己的目录。
- 论文元数据只在 [`../refs/verified.csv`](../refs/verified.csv)；笔记只在 `../notes/`；本目录只放汇报材料与索引。
- 新增文件后在本文“文件索引”补一行。
- 引用论文用仓库 ID（如 `arxiv-2605.30621`），不要另起编号。

---

## 6. 相关文件

- [分工与 Checkpoint](../midpre-checkpoint.md)
- [五轴定义](../notes/AXES.md)
- [笔记模板](../notes/TEMPLATE.md)
- [已核验论文](../refs/verified.csv)
