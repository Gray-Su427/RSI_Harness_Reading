# P1 · 筛选流程图（screening flow diagram）

> 负责人：P1（xyc）｜日期：2026-10-31（术语更正 2026-11-02）｜数据源：[`../../refs/verified.csv`](../../refs/verified.csv)
> 原则：只报实际做过的数量。检索命中数 ≠ 阅读数 ≠ 入库数，三层分开记录。

## 0. 术语说明

本图是**流程图（flow diagram）**，不是漏斗图（funnel chart）。理由两条：

1. **口径不同**：①—③ 是「本轮检索」的计数，④ 起是「文献池」的计数；同一张 funnel chart 要求各阶段是同一总体的逐级收窄，这里不是。
2. **数量非单调**：②约 50 → ③2 是收窄，但 ④又**并入 17 篇既有文献**变成 19，比 ③ 大。funnel chart 定义上要求单调递减，因此本图必须画成带合并节点的流程图。

> 原文件名 `funnel.md` 已按审核意见更名为 `screening-flow.md`；仓库内引用同步更新。

## 1. 阶段与数量

| 阶段 | 数量 | 口径 / 依据 |
|---|---|---|
| ① 检索命中 | **149 条**（去重约 147） | 6 条 arXiv API 查询的 `totalResults` 之和 + 1 条网络精确检索（见 §3）。命中记录数，不是读过的篇数 |
| ② 标题层筛查 | **约 50 条** | 只看了标题与日期：137 条的结果集按提交时间取前 40 条，其余查询结果全看 |
| ③ 本轮新增候选 | **2 条** | `arxiv-2507.21046`（唯一题名精确命中）+ `venue-2026-dcri-survey`（arXiv 无，经网络检索定位到 Preprints.org） |
| ④ 已核验文献池 | **19 篇** | CP0 基线 17 篇（2026-10-12 核验）**与 ③ 合并**后的总数 |
| ⑤ 泛读卡 | **19 篇** | `notes/skim/` 17 张旧卡 + 2 张新卡 |
| ⑥ 精读候选 | **7 篇** | P4（zgj）冻结名单，见 [`../p4/plan.md`](../p4/plan.md) §2 |
| ⑦ 完整 Schema 精读 | **0 篇** | 中期后进行，当前不得记为已完成 |

**两个比率**：

- 文献池 → 精读候选：**19 → 7，36.8%**
- 精读候选 → 已精读：**0 / 7**（CP1 时点状态）

## 2. 流程图

```mermaid
flowchart TD
    A["① 检索命中 149 条<br/>6 条 arXiv 查询 + 1 条网络检索"] --> B["② 标题层筛查 约 50 条<br/>只看标题与日期"]
    B --> C["③ 本轮新增候选 2 条"]
    P["CP0 既有文献池 17 篇<br/>（2026-10-12 核验）"] --> D
    C --> D["④ 已核验文献池 19 篇"]
    D --> E["⑤ 泛读卡 19 篇"]
    E --> F["⑥ 精读候选 7 篇"]
    F --> G["⑦ 完整 Schema 精读 0 篇<br/>（中期后进行）"]
    style A fill:#eef,stroke:#557
    style P fill:#f5f5f5,stroke:#999
    style D fill:#efe,stroke:#575
    style F fill:#ffe,stroke:#a85
    style G fill:#fee,stroke:#a55
```

纯文本版（不能渲染 mermaid 时使用）：

```
① 检索命中 149 ──> ② 标题筛查 ~50 ──> ③ 本轮新增 2 ─┐
                                                      ├──> ④ 文献池 19 ──> ⑤ 泛读卡 19 ──> ⑥ 精读 7 ──> ⑦ 已精读 0
CP0 既有池 17 ───────────────────────────────────────┘
```

## 3. 检索日志（可复核）

| # | 查询式 | 渠道 | `totalResults` | 处理 |
|---|---|---|---|---|
| 1 | `ti:"Survey of Self-Evolving Agents"` | arXiv API | 1 | ✅ 命中 `2507.21046`，入库 |
| 2 | `ti:"Data-Centric Recursive Improvement"` | arXiv API | 0 | ❌ 无 arXiv 版本，转网络检索（#7） |
| 3 | `all:"data-centric recursive"` | arXiv API | 2 | 均为无关工作：`2609.36675`（Gödel Forest，方法）、`2610.15782`（RSI-Nav，导航），不入库 |
| 4 | `ti:"data-centric recursive"` | arXiv API | 2 | 同上，交叉确认 |
| 5 | `ti:"self-evolving agents"` | arXiv API | 137 | 按提交日期降序取前 40 条看标题，用于确认「是否另有同名综述」；未发现第二篇题名匹配 |
| 6 | `abs:"recursive self-improvement" AND abs:"survey"` | arXiv API | 7 | 与既有 5 篇综述重复或为邻近主题，无新增 |
| 7 | `"Data-Centric Recursive Improvement for Foundation Models"` | Web 检索 | — | ✅ 定位到 Preprints.org（DOI `10.20944/preprints202609.0154`）、GitHub companion repo、Google Scholar 记录 |

> 检索日期统一为 **2026-10-31**。查询式可重放：
> `https://export.arxiv.org/api/query?search_query=<查询式>&max_results=40`

## 4. 与 CP1 标准的对照

`midpre-checkpoint.md` 的 CP1 标准写「检索 → 19 核验 → 19 skim → 7 精读候选」。对应关系：

| CP1 说法 | 本文件 | 是否一致 |
|---|---|---|
| 19 核验 | ④ 已核验文献池 = 19 | ✅ |
| 19 skim | ⑤ 泛读卡 = 19 | ✅ |
| 7 精读候选 | ⑥ = 7 | ✅ |
| 「检索」（未给数） | ① 149 / ② ~50 / ③ 2 | ✅ 补上具体口径，未把 149 说成「读了 149 篇」 |

## 5. 口径说明

149 是查询命中数，不是阅读数；真正进入人工判断的是约 50 条标题，最终 2 条新增与 17 篇既有文献合并为 19 篇池。
任何引用这组数字的场合都须保留「①—③ 属检索口径、④ 起属文献池口径」这一区分，否则会与 ④ 的 19 篇冲突。
