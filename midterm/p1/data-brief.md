# P1 · 数据 brief：3 个数字 + 1 个判断

> 负责人：P1（xyc）｜日期：2026-10-31
> 配套：[`stats.md`](stats.md)（四张分布表）· [`funnel.md`](funnel.md)（漏斗与检索日志）· [`venue-verification.md`](venue-verification.md)（venue 核验证据）

---

## 三个数字

### ① 4 / 19 = 21%：有可核验正式发表记录的文献

- 4 条 `venue_verified: true`：STOP（COLM 2024 Spotlight）、ADAS（ICLR 2025）、DGM（ICLR 2026）、Gao 综述（TMLR 2026）。
- 2026 年的 12 篇中 **0 篇**有可核验的录用记录。
- 对比 CP0 时点：**0 / 17**。

**数据依据**：`venue_verified` 列计数；逐条来源见 [`venue-verification.md`](venue-verification.md)。
**对 Gate 2 的含义**：「≥1 篇经典/同行评审」现可由 STOP 或 ADAS 满足；但不能表述为「文献池已核验」。

### ② 12 / 19 = 63%：2026 年文献占比

| 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|
| 1 | 1 | 5 | **12** |

**数据依据**：`year` 列计数（`year` 记首发年，DGM 记 2025）。
**约束**：这是「领域在 2026 年加速」的唯一量化支撑，须与数字①同时出现，否则会得出相反结论。

### ③ 7 / 19 = 37%：综述占比

- role 分布：survey 7、harness-core 7、seed 4、industry 1。
- 11 条 `industry: true` 中 3 条是综述（Code as Agent Harness、Safety in Self-Evolving Agents、DCRI），**可作 Gate 2 工业界实证的为 8 条**。

**数据依据**：`role` 与 `industry` 列交叉计数。
**含义**：`harness-core` 的 7 条是本组唯一可直接支撑分类的样本；综述只能用于领域地图。

---

## 一个判断

> **池子的宽度已经够用，厚度不够；继续扩池的边际收益低于把 7 篇做透。**

理由：

1. **扩池不解决证据问题**：本轮新增 2 篇均为综述（其中 1 篇未同行评审），不进 evidence；`ti:"Data-Centric Recursive Improvement"` 已确认 arXiv 为 0 命中。
2. **可核验性不会自动改善**：2026 年 12 篇全部无录用记录，只能等会议放榜或作者更新，不能靠再检索补足。
3. **缺口在深读**：`harness-core` 仅 7 篇，P4 已排 4 篇进精读；风险不在篇数，而在同口径的成本与基线记录缺失（对应 `risk.md` 的 R2）。

**由此确定的数据维护动作**：

- CP1 通过后冻结文献池；新增只接受「精读过程中被引出、且能核验 ID」的条目。
- 「4/19 已核验」记为进度，「8 篇工业界实证」记为上限，均不记为已完成。

---

## 复核方式

```bash
python -c "import csv;rows=list(csv.DictReader(open('refs/verified.csv',encoding='utf-8')));print(len(rows), sum(r['venue_verified']=='true' for r in rows), sum(r['year']=='2026' for r in rows), sum(r['role']=='survey' for r in rows), sum(r['industry']=='true' for r in rows))"
```

预期输出：`19 4 12 7 11`。

---

## 口径与限制

1. **DBLP 本轮不可用**：三个入口均被人机验证拦截，venue 核验改用会议官网 accepted papers 页与官方论文集；无任何一条 DBLP 证据（见 [`venue-verification.md`](venue-verification.md) §0）。
2. **2 条为作者自述录用、未经第三方核验**（RHO → EMNLP 2026 Findings；`2603.25681` → TMLR），CSV 保持 `venue_verified: false`。
3. **`industry` 口径为「署名含企业机构」**，不等于有工业级实证；国家实验室（上海 AI Lab）不算。
4. **`year` 记首发年**，DGM 记 2025 而非 ICLR 2026。
