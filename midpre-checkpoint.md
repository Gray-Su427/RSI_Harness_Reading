# 中期汇报准备：分工与 Checkpoint

> **用途**：4 人共用。每人先看「人员表」和「状态看板」，再只看自己的 section。
>
> **汇报时长**：5 分钟；**形式**：一人主讲（主讲人待定）。
> ⚠️ 课程 PPT 暂定每组 10 分钟报告 + 5 分钟提问；若本次为同一场次，以实际通知为准，计时目标相应调整。
>
> **本文件只管材料准备，不管讲解分工。**
>
> **数字以 `refs/verified.csv` 为准。**

---

## 0. 人员表

| 代号 | 姓名 | 角色 | 主要交付 |
|---|---|---|---|
| **P1** | xyc | 数据与文献池 | 种子综述、venue 核验、结构统计、筛选流程图 |
| **P2** | zyc | 分类体系与图 | 五轴表、分类总表、A×E 体系图 |
| **P3** | szh | 边界、叙事与整合 | 领域地图、3 句叙事、6 页 deck |
| **P4** | zgj | 精读计划与风险 | 7 篇名单、排期、风险清单、Q&A |

> CP0 记录：2026-10-31 姓名已填（xyc / zyc / szh / zgj）；全员已确认认领各自任务（P3／szh 记录）。
> CP1 记录（2026-11-01）：19 篇入库、4 篇 venue 已核验、统计与筛选流程图齐，P3 验收通过。
> CP2 记录（2026-11-01）：P2 交付 9 篇分类表、A×E 图、3 条发现、2 张五问卡，P3 评审通过并冻结。
> CP3 记录（2026-11-01）：P3 交付叙事、6 页 deck、RHO/SEVerA 五问卡、CP4 清单；Q&A 已确认 2/8。
> T 记录（2026-11-01）：**汇报日 T = 2026-11-02（周一）**；CP4 当天上午执行；D1–D14 = **2026-11-03 – 11-16**（D1 = T+1）。
> 时长口径（2026-11-01）：中期汇报 **5 分钟（≤4:40）**；课程 PPT 的 10 分钟版用于第三次课。

---

## 1. 状态看板

| CP | 名称 | 负责人 | 建议时点 | 状态 | 完成日期 |
|---|---|---|---|---|---|
| **CP0** | 分工确认 | P3（szh） | 立刻 | ✅ 通过 | 2026-10-31 |
| **CP1** | 数据冻结 | P1（xyc） | 汇报前 2 天 | ✅ 通过 | 2026-11-01（P3 验收） |
| **CP2** | 体系冻结 | P2（zyc） | 汇报前 2 天 | ✅ 通过 | 2026-11-01（P3 评审） |
| **CP3** | 叙事与计划冻结 | P3（szh） + P4（zgj） | 汇报前 1 天 | 🟡 材料已齐，待 Q&A 确认 | 2026-11-01 提交 |
| **CP4** | 最终校对 | P3（szh） | **2026-11-02 上午** | 🟡 清单已建，当天执行 | 2026-11-01（清单） |

状态说明：`⬜ 未开始` / `🟡 进行中` / `✅ 通过` / `❌ 退回`

---

## 2. P1（xyc） · 数据与文献池

### 负责工作

- [x] 补两篇种子综述：检索、核验 arXiv ID、入 `refs/pool.csv`、做 skim 卡 → [`midterm/p1/venue-verification.md`](midterm/p1/venue-verification.md) §3、`notes/skim/`
- [x] 核验 4 篇 seed 的 venue：STOP、ADAS、DGM、SICA → 3 篇 `true`、SICA 为 preprint（[`midterm/p1/venue-verification.md`](midterm/p1/venue-verification.md) §1）
- [x] 维护 `refs/verified.csv` 的 `year` / `venue` / `industry` / `role` 字段 → 19 行，`venue_verified` 4 篇 `true`
- [x] 做 17 + 2 篇结构统计：年份、venue、industry、role 四个分布 → [`midterm/p1/stats.md`](midterm/p1/stats.md)
- [x] 做筛选流程图（flow diagram）：检索 → 19 核验 → 19 skim → 7 精读候选 → [`midterm/p1/screening-flow.md`](midterm/p1/screening-flow.md)

### 认领论文

| 类型 | 论文 |
|---|---|
| 精读 | STOP `arxiv-2310.02304`、ADAS `arxiv-2408.08435` |
| skim | 5 篇综述 + 2 篇种子综述 |

### 交付物

- 更新后的 `refs/pool.csv`、`refs/verified.csv`
- 2 张新 skim 卡
- 结构统计表
- 筛选流程图（flow diagram）：[`midterm/p1/screening-flow.md`](midterm/p1/screening-flow.md)
- 一页 data brief：**3 个数字 + 1 个判断**

### 交给

- 元数据 → **P2**
- 统计与流程图 → **P3**

### 对应 Checkpoint

**CP1 · 数据冻结**

---

## 3. P2（zyc） · 分类体系与图

### 负责工作

- [x] 把 `notes/AXES.md` 压缩成 5 行五轴速览表 → [`midterm/p2/axes-overview.md`](midterm/p2/axes-overview.md)
- [x] 填分类总表：7–9 篇核心论文，空格标「待精读」 → [`midterm/p2/classification.md`](midterm/p2/classification.md)（9 篇）
- [x] 画 **A×E 体系图** → [`midterm/p2/taxonomy-ae.png`](midterm/p2/taxonomy-ae.png) / [`taxonomy-ae.svg`](midterm/p2/taxonomy-ae.svg)
  - 横轴：A 改进对象（prompt / control-flow / code / tool / memory / evaluator / context）
  - 纵轴：E 递归深度（one-shot / iterative / full-rsi / co-evolution）
  - 点：7–9 篇核心论文，不要 17 篇全标（9 个点）
  - 颜色：工业界 / 学术界
  - 标注：DGM、STOP、RHO、SEVerA
  - 空格：写「待精读」，不要猜（5 篇置于底部灰带）
- [x] 写 2–3 条初步发现：密集区、空白、反例 → [`midterm/p2/findings.md`](midterm/p2/findings.md)

### 认领论文

| 类型 | 论文 |
|---|---|
| 精读 | DGM `arxiv-2505.22954`、AlphaEvolve `arxiv-2506.13131` |
| skim | SICA `arxiv-2504.15228`、MGM `arxiv-2608.07645` |

> STOP / ADAS 的细节找 P1 要 brief。

### 交付物

- 五轴速览表 → `midterm/p2/axes-overview.md`
- 分类总表（9 篇）→ `midterm/p2/classification.md`
- `taxonomy-ae` 图 → `midterm/p2/taxonomy-ae.png` / `.svg`；说明见 `taxonomy-ae.md`
- `findings.md`：3 条判断，每条一句话
- P2 认领论文五问卡 → `dgm-brief.md`、`alphaevolve-brief.md`
- 交付索引与口径 → `midterm/p2/README.md`

> **给 P3 的口径提醒**：E 轴 5/9 待精读，不能写「递归深度集中在 `one-shot` / `iterative`」；能落位的 3 篇分别落在 `one-shot`、`iterative`、`full-rsi`。详见 `midterm/p2/README.md` §3。

### 交给

**P3**（图与发现，用于叙事和 deck）

### 对应 Checkpoint

**CP2 · 体系冻结**

---

## 4. P3（szh） · 边界、叙事与整合

### 负责工作

- [x] 填领域地图：RSI 定义、三层定位、纳入/不纳入、2023–2026 时间线 → 写作仓库 `group/domain-map.md`（中期定稿）
- [x] 写 **3 句叙事线** → [`midterm/p3/narrative.md`](midterm/p3/narrative.md)（定稿候选，已按 P2 口径修正）：
  1. **现状**：19 篇入库文献中 **12 篇（63%）** 出自 2026，但 2026 年的 12 篇中 **0 篇**有可核验录用记录；4/19 有录用，且全是 2023–2025 的工作。
  2. **缺口**：9 篇核心样本中「改什么」已有共识（主 A 值 `code` **6/9**），但 E 轴**大面积未界定**——仅 3 篇可落位（STOP=`iterative`、DGM=`full-rsi` 仅代码层、RHO=`one-shot`），5 篇待精读；`co-evolution` / `evaluator` / `context` 三个格点为 0，`formal-safety` 只有 SEVerA，`self-preference` 只有 RHO（作者自报最偏好 0.78 ≠ 测试最高 0.85）。
  3. **计划**：用 7 篇精读（2/2/2/1，D1–D14）验证「递归深度是否被高估、验证独立性是否被低估」，形成 3 条证据和 2–3 个争议。
- [x] 合并 6 页 deck，检查数字、论文 ID、轴标签、术语一致性 → [`midterm/p3/deck-rsi-midterm.pptx`](midterm/p3/deck-rsi-midterm.pptx)（6 页正文 + 2 页 backup，280 s）、[`deck-outline.md`](midterm/p3/deck-outline.md)、[`make_deck.py`](midterm/p3/make_deck.py)
- [x] 组织全员做一次最终校对 → 清单 [`midterm/p3/cp4-checklist.md`](midterm/p3/cp4-checklist.md)；Q&A 状态 [`qa-signoff.md`](midterm/p3/qa-signoff.md)（2/8 已确认）

> ⚠️ 旧草稿的「递归深度集中在 `one-shot` / `iterative`」**已作废**：能落位的只有 3 篇，分属三档；5 篇无作者自我界定。deck 与报告一律用上面的第 2 句。
>
> 🗓 时间点已定：T = **2026-11-02**；D1–D14 = **2026-11-03 – 11-16**；排练截止 11-01 晚，CP4 在 11-02 上午。

### 认领论文

| 类型 | 论文 |
|---|---|
| 精读 | RHO `arxiv-2606.05922`、SEVerA `arxiv-2603.25111` |
| skim | Self-Harness `arxiv-2606.09498`、RHSI `arxiv-2607.15524`、Code as Agent Harness `arxiv-2605.18747` |

### 交付物

- 领域地图 → 写作仓库 `group/domain-map.md`（✅ 中期定稿）
- `narrative.md`：3 句话 → [`midterm/p3/narrative.md`](midterm/p3/narrative.md)（✅）
- `deck`：6 页 → [`midterm/p3/deck-rsi-midterm.pptx`](midterm/p3/deck-rsi-midterm.pptx)（✅ 6 页正文 + 2 页 backup，280 s）
- 一致性校对清单 → [`midterm/p3/cp4-checklist.md`](midterm/p3/cp4-checklist.md)（✅ 待当天执行）

### 交给

**全员**（deck 校对）

### 对应 Checkpoint

**CP0、CP3、CP4**

---

## 5. P4（zgj） · 精读计划与风险

### 负责工作

- [x] 定 7 篇精读名单（见下表）→ [`midterm/p4/plan.md`](midterm/p4/plan.md) §2
- [x] 做 2/2/2/1 分工 + 两周排期 → [`midterm/p4/plan.md`](midterm/p4/plan.md) §3（D1 待 T 确认）
- [x] 写风险清单：
  - venue 未核验（R1，已由 CP1 关闭）
  - 算力成本未报告（R2，仍开放）
  - 复现性差（R3，仍开放）
  - 两篇种子综述待补（R4，已由 CP1 关闭）
- [x] 汇总 8 个 Q&A：全员各供 2 个，P4 合并成一页 → [`midterm/p4/qa.md`](midterm/p4/qa.md)（**2/8 已确认**，见 [`midterm/p3/qa-signoff.md`](midterm/p3/qa-signoff.md)）

### 认领论文

| 类型 | 论文 |
|---|---|
| 精读 | Harness Updating Is Not Harness Benefit `arxiv-2605.30621` |

### 7 篇精读名单

| 论文 | 精读负责人 | 覆盖指标 |
|---|---|---|
| STOP `arxiv-2310.02304` | P1 | 经典 / 同行评审候选 |
| ADAS `arxiv-2408.08435` | P1 | 经典 / 控制流 |
| DGM `arxiv-2505.22954` | P2 | 工业界 / `full-rsi` |
| AlphaEvolve `arxiv-2506.13131` | P2 | 工业界 / 2025 |
| RHO `arxiv-2606.05922` | P3 | 2026 / `self-preference` |
| SEVerA `arxiv-2603.25111` | P3 | 2026 / `formal-safety` |
| Harness ≠ Benefit `arxiv-2605.30621` | P4 | 2026 / 争议 Q1 |

### 交付物

- `plan.md`：7 篇名单 + 分工 + 两周排期（✅ 2026-11-01 补 T=11-02、D1–D14=11-03 – 11-16）
- `risk.md`：4 条风险 + 应对（✅ 2026-11-01 R1/R4 关闭，R2/R3 仍开放）
- `qa.md`：8 个问题 + 20 秒答案（🟡 2/8 已确认；Q1/Q2 已按 CP1 结果改写）

### 交给

**P3**（计划与风险，用于叙事和 deck）

### 对应 Checkpoint

**CP3（计划部分）**

---

## 6. 交接关系

```
P1 ──元数据──→ P2
 │               │
 │──统计/流程图──→ P3 ←──图/发现── P2
                  ↑
                  │──计划/风险── P4
```

- P3 合并后，全员校对一遍。
- 数字和论文 ID 以 P1 的 `refs/verified.csv` 为准。
- 有冲突时，以仓库文件为准，不以聊天记录为准。

---

## 7. Checkpoint 规则

1. **不通过不进下一阶段。** CP1 没过，不做 CP2；CP2 没过，不合并 deck。
2. **负责人在状态看板里更新状态和日期。**
3. **变更写进「变更记录」**，不要私改分工。
4. **每个 CP 会议不超过 20 分钟**，只回答「过了没有、差什么、谁补」。
5. **CP4 只看一致性**：数字、论文 ID、术语、链接、计时；不再加新内容。

### 各 CP 的通过标准

| CP | 通过标准 |
|---|---|
| **CP0** | 4 人姓名填好；每人认领任务；无悬空工作 |
| **CP1** | 2 篇种子综述入库；4 篇 seed venue 有结论；19 篇统计与 CSV 一致；流程图各阶段数字对得上 |
| **CP2** | 五轴表 5 行；分类总表 7–9 篇；A×E 图 7–9 个点；3 条发现各有支撑 |
| **CP3** | 3 句叙事；6 页 deck 骨架；7 篇名单 + 2/2/2/1 分工 + 两周排期；4 条风险；8 个 Q&A |
| **CP4** | 数字、论文 ID、术语一致；计时 ≤ 4:40；链接全部通过；backup 页就绪 |

---

## 8. 变更记录

| 日期 | 改动 | 原因 |
|---|---|---|
| 2026-10-30 | 建立分工与 Checkpoint | 中期汇报准备 |
| 2026-10-31 | 填入四人姓名（xyc / zyc / szh / zgj）；同步 P4 计划与风险文件 | CP0 姓名确认 |
| 2026-10-31 | CP0 通过：全员确认认领任务 | P3（szh）记录 |
| 2026-10-31 | CP2 工作稿提交：五轴表、9 篇分类表、A×E 图、3 条发现、DGM/AlphaEvolve 五问卡；CP2 置 🟡 待评审 | P2（zyc）完成 CP2 交付 |
| 2026-11-01 | CP1 验收通过：19 篇入库、4 篇 venue 核验、统计/流程图/data brief、STOP/ADAS 卡齐 | P1 交付完成，P3 验收 |
| 2026-11-01 | CP2 评审通过并冻结：9 篇分类、A×E 图、3 条发现均可用；E 轴按 P2 口径修正 | P3 评审 |
| 2026-11-01 | CP3 材料提交：叙事 3 句、6 页 deck（pptx + 脚本 + 大纲）、RHO/SEVerA 五问卡、CP4 清单、Q&A 确认表 | P3（szh）完成 CP3 交付；Q&A 2/8 已确认 |
| 2026-11-01 | 汇报时长定为 5 分钟（≤4:40）；10 分钟版留给第三次课 | P3 决断，避免两套计时混用 |
| 2026-11-01 | 汇报日 T 确定为 **2026-11-02**；D1–D14 映射为 11-03 – 11-16；CP4 置「当天上午执行」 | 时间点确认 |
| 2026-11-02 | 术语更正：「漏斗 / funnel」→「筛选流程图 / flow diagram」；`midterm/p1/funnel.md` 更名为 `screening-flow.md`，全仓引用同步 | 人工审核：该图是流程图，且 ③2→④19 数量上升，不满足 funnel chart 的单调递减定义 |

---

## 9. 备注

- 本文件放在 **Reading 仓库**，组员都能看到；材料不用都进仓库，交给 P3 汇总即可。
- 中期前目标是「材料齐、判断清、计划具体」，不是「读完 7 篇」。
- 精读的完整 Schema 在中期后做；中期前每篇按「讲述级 5 问」准备即可：
  1. 一句话贡献
  2. 改什么（A 轴）
  3. 凭什么改（B 轴）
  4. 递归到哪一层（E 轴，作者原话）
  5. 最可疑的一点
