# P4 · 七篇精读计划与两周排期

编制日期：2026-10-30｜负责人：P4（zgj）｜交接对象：P3（szh）｜状态：CP3 预备稿，待 CP1／CP2 通过及各组员确认后冻结。

> 人员代号：P1 = xyc｜P2 = zyc｜P3 = szh｜P4 = zgj

## 1. 目标与时间口径

【本组判断】围绕“递归深度是否被高估、验证独立性是否被低估”，用七篇候选检查改进对象、反馈来源、递归声明与收益证据，最终形成三条可追溯证据和两至三个争议。

- **中期前**：冻结七篇名单、2/2/2/1 分工、两周排期、四项风险、八个 Q&A；七篇各准备一张“讲述级五问”卡（P1—P3 各 2 张、P4 1 张），由 P4（zgj）汇总。
- **中期后两周**：完成完整 Schema 精读、方法比较与证据交叉检查，并形成 Gate 3 的 ≥3 条证据与 2—3 个争议。不得把计划中的精读写成已完成。
- 汇报日期尚未提供。以下以中期汇报后首个工作日为 **D1**，D1—D14 为连续两周；P3（szh）确认汇报日期后整体映射至日历，不擅自假定具体日期。若 T 对应课程第三次课的 10 分钟报告，计时目标按 §4 单独调整。
- CP1／CP2／CP3／CP4 为中期前材料门禁；下表 D7、D14 为中期后阅读里程碑，两者不混用。CP1 未闭环时的补做安排见 §4，不把补做写成常规排期。

## 2. 固定名单与 2/2/2/1 分工

论文标题、年份、机构及状态以 [refs/verified.csv](https://github.com/Gray-Su427/RSI_Harness_Reading/blob/main/refs/verified.csv) 为准。以下“用途／追问”是阅读任务，不是精读结论。

| 负责人 | 论文及 ID | 年份 | 覆盖用途 | 精读必须回答的问题 |
|---|---|---|---|---|
| P1（xyc，2 篇） | [STOP](https://arxiv.org/abs/2310.02304) · `arxiv-2310.02304` | 2023 | 经典、同行评审候选 | 自修改了什么？如何保留作者“不属于 full RSI”的限定？是否有同预算搜索基线？ |
| P1（xyc，2 篇） | [ADAS](https://arxiv.org/abs/2408.08435) · `arxiv-2408.08435` | 2024 | 经典、agent 代码与控制流搜索 | meta-agent 是否固定？更新的是 target-agent 还是改进器？搜索验证与最终测试是否隔离？ |
| P2（zyc，2 篇） | [DGM](https://arxiv.org/abs/2505.22954) · `arxiv-2505.22954` | 2025 | 工业界、自改能力声明 | “改进自改能力”有哪些实验支持？固定的 archive／父代选择限制了什么？ |
| P2（zyc，2 篇） | [AlphaEvolve](https://arxiv.org/abs/2506.13131) · `arxiv-2506.13131` | 2025 | 工业界、进化搜索边界对照 | 改进任务算法和改进自身 harness 有何区别？总搜索成本与案例证据是否公开？ |
| P3（szh，2 篇） | [RHO](https://arxiv.org/abs/2606.05922) · `arxiv-2606.05922` | 2026 | 新工作、`self-preference` | 单轮结果能否支撑持续自进化？自偏好选择与独立测试是否一致？ |
| P3（szh，2 篇） | [SEVerA](https://arxiv.org/abs/2603.25111) · `arxiv-2603.25111` | 2026 | 新工作、形式化保证边界 | Search 与 Learn 分别改程序还是权重？保证的假设、规格范围与资源限制是什么？ |
| P4（zgj，1 篇） | [Harness Updating Is Not Harness Benefit](https://arxiv.org/abs/2605.30621) · `arxiv-2605.30621` | 2026 | 新工作、争议 Q1（测量效度） | 能生成更新与能利用更新如何分离？均值／最大值聚合与预算设置如何影响结论？ |

### 指标覆盖与判定规则

1. 七篇为既定精读目标，课程精读硬门槛为至少五篇完整 Schema；不能以“五篇足够”为由直接取消其余两篇。
2. 同行评审项优先由 STOP／ADAS 覆盖，但当前 CSV 中 `venue_verified` 均为 `false`，**尚不能宣布该指标达标**。P1（xyc）独立核验录用来源后再更新。
3. 新工作已在名单中覆盖 2025—2026；年份按 CSV，不把 DGM 的会议年份当作论文年份。
4. 工业界项优先核查 DGM、AlphaEvolve；“署名含企业机构”按 CSV 的 `industry`／`org` 口径，实证与可复现性另行判断。
5. AlphaEvolve 为任务算法搜索对照，SEVerA 为程序／权重交叉对照；选入阅读不等于认定其都是严格的 harness RSI 正例。
6. 七篇不等于七条独立证据。ADAS／DGM 有作者及研究谱系关联，P1（xyc）、P2（zyc）联合检查问题和结论重叠，保守合并重复证据。

## 3. 两周排期

建议每人预留：每篇方法和实验阅读约 2—3 小时、附录与证据核对约 1—2 小时，组内交叉核对约 1 小时。此为排期估算，D1 按实际可用时间确认。

| 时间 | P1（xyc） | P2（zyc） | P3（szh） | P4（zgj） | 当阶段可检查产出 |
|---|---|---|---|---|---|
| D1—D2 | STOP 方法；回查 STOP 版本／链接 | DGM 方法与自修改闭环 | RHO 方法与单轮限定 | P4 论文 §3—4 回查；核对能力指标 | 进入 Schema §2—4；回查版本／链接；校准各组可用时间（CP1 未闭环则先补 seed surveys／venue） |
| D3—D4 | STOP 实验、成本与附录 | DGM 基线、成本与固定机制 | RHO 自偏好与 held-out 测试 | 核对两类收益、聚合方式、预算与代码入口 | 首轮四篇 Schema 草稿；每项主张有章节／图表定位 |
| D5—D6 | ADAS 方法与实验 | AlphaEvolve 方法及案例 | SEVerA Search／Verify／Learn | 完成 P4 Schema 草稿；整理共同追问 | 余下三篇 Schema 草稿；风险缺项清单 |
| D7 | 联合核对 STOP／ADAS 与 DGM 的边界 | 核对 DGM 与算法搜索的差别 | 核对递归声明和形式化保证 | 汇总进度与缺失项 | **第一周里程碑：七篇均有草稿；缺失项有负责人和补齐时间** |
| D8—D9 | 补 ADAS 附录与数据划分 | 补 AlphaEvolve 总成本及开放材料 | 补 SEVerA 假设与资源限制 | 检查 P4 论文 in-situ 评估及统计问题 | 七篇完整 Schema 待审版，不能用推测补空格 |
| D10—D11 | 复核 P2 的边界及原话 | 复核 P1 的方法及谱系重叠 | 复核 P4 的测量与推断 | 复核 P3 的验证与成本范围 | 交叉审阅记录；A—E、基线、成本、复现状态可追溯 |
| D12—D13 | 提交经典方法证据 | 汇总方法比较表 | 整合分类与争议 | 汇总成本／复现缺口及证据独立性 | 三条证据与两至三个争议草案；Gate 2：每轴至少两篇例证；Gate 3：每条证据至少两篇独立文献并附反面证据 |
| D14 | 全员核对出处与限定 | 全员核对出处与限定 | 汇总最终材料；启动 deck 制作与彩排 | 检查阅读计划闭环 | **第二周里程碑：目标七篇精读交付；核验 Gate 2 与 Gate 3；若第三次课紧接 D14，deck 制作／彩排另排缓冲，未达项实名登记** |

### 统一交付格式

- 中期前五问：一句话贡献；A 改什么；B 凭什么改；E 递归到哪层及作者原话；最可疑的一点。
- 中期后：使用仓库 [notes/TEMPLATE.md](https://github.com/Gray-Su427/RSI_Harness_Reading/blob/main/notes/TEMPLATE.md) 完整 Schema，文件为 `notes/deep/<ID>.md`。本交付包的准备卡不替代正式精读笔记。
- 证据验收（Gate 3）：≥3 条证据；每条 ≥2 篇独立文献（作者／问题／结论三重检验），每条附反面证据；争议从写作仓库 `group/open-questions.md` 的 5 个候选中收敛到 2—3 个。分类覆盖（Gate 2）另按“每条轴 ≥2 篇例证”验收，两者不能互相替代。
- 交接文件：写作仓库 `RSI_Harness_Writing/group/evidence.md`、`open-questions.md`、`taxonomy.md`（与 reading 同级）。
- 每篇摘录：主结果及基线、模型与任务划分、预算／成本、作者限定、公开材料；记录章节、表图或附录位置。
- E 轴无作者自我界定时写 `unknown`／“待精读”，保留循环描述，不凭论文标题或循环次数升级为 `full-rsi`。
- 成本按“完整报告／部分报告／未找到”区分；代码按“链接可访问／可运行／结果已复现”区分。

## 4. 中期前交接及确认

设中期汇报日为 T。以下为建议执行时点，日期由 P3（szh）确认。

| 时点 | P4（zgj）的动作 | 依赖与输出 |
|---|---|---|
| T−2 天 | 对齐名单和当前元数据；将冲突交给 P1（xyc）／P2（zyc） | CP1 后核对数字（Q&A 的 17／19 以 CP1 后 CSV 为准）；CP2 后核对分类，保留待精读标签 |
| T−1 天 | 提交本计划、[risk.md](risk.md)、[qa.md](qa.md) 和 [P4 准备卡](p4-paper-brief.md) | P3（szh）用于 CP3 的计划、风险和 backup 页 |
| T−1 天 | 请 P1（xyc）／P2（zyc）／P3（szh）／P4（zgj）各确认对应两条 Q&A | 目前为 P4（zgj）代拟八条，不能写成全员已供稿 |
| T 当天 | 校对论文 ID、术语、来源链接和发言计时 | 按 CP4 只修一致性；当前按 checkpoint 5 分钟设 ≤4:40；若 T 为第三次课 10 分钟报告，另按 10 分钟排 |

### 已识别的口径冲突（交负责人核实）

- CSV 把 RHO 标为 `iterative`，skim 卡引用作者“只评估单轮、未声称多轮累积”的限定。P3（szh）回查原文，P1（xyc）在确认后维护 CSV；冻结前不据此统计递归深度。
- STOP 的 CSV 为 `one-shot`，skim 卡有不同工作标签；AlphaEvolve 也有 CSV／skim 标签差异。P1（xyc）、P2（zyc）核对定义与原话，不直接沿用任一标签为最终结论。
- DGM 的 CSV 含 `evaluator`，skim 卡认为评测及选择机制固定。P2（zyc）查明可编辑边界后交 P1（xyc）更新。
- SEVerA 的 Search 涉及程序结构、Learn 涉及权重；P3（szh）明示跨界范围，不把整个方法归为纯 harness 更新。

### CP1 未闭环时的处理

若 T−2 的 CP1 未通过（venue 或两篇种子综述未闭环），D1—D2 先补 CP1 缺项，再进入 Schema；不按原排期直接跳到 D3。CP1 通过是启动 D1—D14 的前置条件；未通过时保留 CP1 未通过状态并记录阻塞原因。

### P4 提交自检

- [x] 七篇名单、ID、2/2/2/1 分工与两周排期已写明（P1=xyc，P2=zyc，P3=szh，P4=zgj）。
- [x] 四项风险含负责人、应对及退出条件。
- [x] 八条约二十秒 Q&A 与 P4（zgj）五问准备卡已拟好。
- [ ] P1—P3 各提交 2 张讲述级五问卡（P4 已交 1 张）。
- [ ] P3（szh）确认 T 与四人实际可用时间，并校准排期。
- [ ] 四人确认各两条 Q&A；P3（szh）审阅计划与 deck 口径。
- [ ] P3（szh）／P4（zgj）按实际验收结果更新远端 CP3 状态及日期。

## 5. 来源

访问日期：2026-10-30。除 P4 论文另有原文核对外，其余论文的阅读追问基于仓库元数据与 skim 卡，不标作本次完成的原文精读结论。

- [中期分工与 Checkpoint](https://github.com/Gray-Su427/RSI_Harness_Reading/blob/main/midpre-checkpoint.md)
- [阅读契约 AGENTS.md](https://github.com/Gray-Su427/RSI_Harness_Reading/blob/main/AGENTS.md)
- [五轴定义](https://github.com/Gray-Su427/RSI_Harness_Reading/blob/main/notes/AXES.md)
- [七篇及其余文献 skim 卡目录](https://github.com/Gray-Su427/RSI_Harness_Reading/tree/main/notes/skim)
- 写作仓库（本地，与 reading 同级）：`RSI_Harness_Writing/group/evidence.md`、`open-questions.md`、`taxonomy.md`

## 6. 修订记录

| 日期 | 改动 | 原因 |
|---|---|---|
| 2026-10-31 | 填入 P1—P4 姓名；统一“每篇五问”与 Gate 2／Gate 3 验收口径；补 CP1 未闭环时的补做安排与进程风险 | 按评审意见修订，供 CP3 复审 |
