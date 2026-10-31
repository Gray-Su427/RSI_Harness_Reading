# 中期汇报材料

> 维护：P3（szh）｜更新：2026-10-31
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
| CP0 | ✅ 通过（2026-10-31） | P3（szh） | 姓名已填；全员已确认认领；Q&A 答复待确认 |
| CP1 | ⬜ 未开始 | P1（xyc） | 种子综述、venue、统计、漏斗 |
| CP2 | 🟡 P2 已交，待评审 | P2（zyc） | 五轴表、分类总表、A×E 图、3 条发现、2 张五问卡 |
| CP3 | ⬜ 未开始 | P3（szh） + P4（zgj） | 7 篇名单、排期、4 风险、8 Q&A |
| CP4 | ⬜ 未开始 | P3（szh） | 最终一致性校对 |

> 2026-10-31：P1（xyc）、P2（zyc）、P3（szh）、P4（zgj）已确认认领各自任务（P3 记录）。
> 2026-10-31：P2（zyc）已交 CP2 工作稿（9 篇分类表、A×E 图、3 条发现、DGM/AlphaEvolve 五问卡）；CP2 仍为 🟡，待组内评审/冻结。
> 状态以 [`../midpre-checkpoint.md`](../midpre-checkpoint.md) 为准；本表只是快照。

---

## 3. 文件索引

> P4 文件由 P4（zgj）的提交包复制并入；仓库内以本目录版本为准。

| 文件 | 内容 | 负责人 | 状态 |
|---|---|---|---|
| [`p4/plan.md`](p4/plan.md) | 7 篇名单、2/2/2/1 分工、两周排期 | P4（zgj） | CP3 预备稿 |
| [`p4/risk.md`](p4/risk.md) | 四项风险 + 进程风险补充 | P4（zgj） | 初稿 |
| [`p4/qa.md`](p4/qa.md) | 8 个 Q&A（约 20 秒/条） | P4（zgj）代拟 | 待四人确认 |
| [`p4/p4-paper-brief.md`](p4/p4-paper-brief.md) | P4 论文五问准备卡 | P4（zgj） | 讲述级 |
| [`p2/README.md`](p2/README.md) | P2 交付索引、五条口径、口径冲突、复现 | P2（zyc） | CP2 工作稿 |
| [`p2/axes-overview.md`](p2/axes-overview.md) | 五轴速览表（5 行） | P2（zyc） | CP2 工作稿 |
| [`p2/classification.md`](p2/classification.md) | 9 篇分类总表 + 逐篇依据 + E 轴原话 + CSV 建议 | P2（zyc） | CP2 工作稿 |
| [`p2/taxonomy-ae.png`](p2/taxonomy-ae.png) | A×E 体系图（300 dpi） | P2（zyc） | CP2 工作稿 |
| [`p2/taxonomy-ae.svg`](p2/taxonomy-ae.svg) | A×E 体系图（矢量） | P2（zyc） | CP2 工作稿 |
| [`p2/taxonomy-ae.md`](p2/taxonomy-ae.md) | 图注、30 秒读图、deck 用法、复现 | P2（zyc） | CP2 工作稿 |
| [`p2/findings.md`](p2/findings.md) | 3 条初步发现（密集区、空白、反例） | P2（zyc） | CP2 工作稿 |
| [`p2/dgm-brief.md`](p2/dgm-brief.md) | DGM 讲述级五问卡 | P2（zyc） | 讲述级 |
| [`p2/alphaevolve-brief.md`](p2/alphaevolve-brief.md) | AlphaEvolve 讲述级五问卡 | P2（zyc） | 讲述级 |
| [`p2/make_taxonomy_ae.py`](p2/make_taxonomy_ae.py) | A×E 图生成脚本 | P2（zyc） | 可运行 |
| [`../midpre-checkpoint.md`](../midpre-checkpoint.md) | 分工与 CP 看板（仓库根目录） | P3（szh） | 🟡（CP0 ✅；CP2 已交待评审；CP1/CP3/CP4 待办） |

---

## 4. 待办

- [x] P2（zyc）提交 2 张讲述级五问卡（DGM、AlphaEvolve）；P4 已交 1 张。
- [ ] P1（xyc）提交 STOP / ADAS 2 张；P3（szh）提交 RHO / SEVerA 2 张。
- [ ] P3（szh）确认 T 与四人实际可用时间，并校准 D1—D14。
- [ ] 四人各确认两条 Q&A 答复；P3（szh）审阅计划与 deck 口径。
- [ ] CP2 评审：四人检查 9 篇表、A×E 图、3 条发现与 P3 叙事口径；P3 需修正「递归深度集中在 one-shot/iterative」的表述（5/9 待精读，不能算集中）。
- [ ] CP1／CP2 冻结后再启动 D1—D14；CP1 未闭环先补 venue 与两篇种子综述。
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
