# notes/ — 笔记

## 两级笔记

| 目录 | 用途 | 粒度 | 时长上限 |
|---|---|---|---|
| `skim/` | 泛读卡片。回答"这篇在做什么" | 一段话 + 几条标签 | 15 分钟 |
| `deep/` | 精读笔记。回答"这篇凭什么算 RSI，证据链是否站得住" | 严格按 [`TEMPLATE.md`](TEMPLATE.md) Schema | 不限 |

**不要在 skim 目录写长笔记，也不要在 deep 目录写三行摘要。**

---

## 命名规则

```
notes/skim/arxiv-2606.09498.md
notes/deep/arxiv-2505.22954.md
```

文件名 = 论文主键 ID = CSV 中的 `id` 字段。**ID 一经分配不可变更。**

无 arXiv 的论文用 `venue-<年份>-<短slug>`，例如 `venue-2025-iclr-selfrefine`。

---

## 泛读流程（第一次课）

### 阅读路径

每篇按此顺序，**不要跳步**：

1. 标题 + 摘要
2. 引言中的贡献列表（Contribution / We make the following contributions）
3. 方法总览图 / 系统框图
4. 实验设置表——只看 benchmark 和主指标
5. 结论 + 局限

### 筛选门槛

满足 **≥3 条**才建卡片：

- [ ] 直接涉及"修改 agent / harness / scaffold 自身结构"
- [ ] 有明确的自我改进循环或更新算子
- [ ] 有可量化的自我改进效果
- [ ] 2023 年及以后
- [ ] 有一定影响力或被多篇工作引用

### skim 卡片模板

```markdown
---
id: arxiv-XXXX.XXXXX
title: ""
authors: ""
year: 2026
venue: ""
venue_verified: false
industry: false
role: pool
read_status: skim
read_date: 2026-XX-XX
---

**一句话**：这篇做了什么（不含评价）

**改进对象**：（prompt / 控制流 / 代码 / 工具 / 记忆 / 评测器 / 上下文）

**改进信号**：（自偏好 / 外部验证 / 人类反馈 / 失败轨迹）

**递归深度**：（one-shot / iterative / full-rsi / co-evolution）＋ 作者原话

**可复现性**：代码开源？archive 公开？

**是否入选精读**：是 / 否——理由

**可疑之处**：
```

### 泛读产出

- `skim/` 卡片 ≥ **15** 篇
- `../README.md` 中写出领域地图与选题边界
- `../refs/pool.csv` 中每条的 arXiv ID 均已核验

---

## 精读流程（第二次课）

### 阅读顺序

**先方法 → 再实验 → 最后附录。**

附录常藏两样关键东西：**成本核算**与**消融实验**。这两项直接对应争议 Q3。

### 为什么必须用统一 Schema

分类体系只有在所有笔记用**同一套字段**记录的前提下才能归纳出来。
字段不齐的笔记无法参与比较，等于白读。

Schema 见 [`TEMPLATE.md`](TEMPLATE.md)，🔴 标记为必填。

### 精读产出

- 完整 Schema 笔记 **≥5** 篇
- 方法比较表（见 `../synthesis/evidence.md` 的表头设计）
- 分类体系每条轴都有 **≥2 篇**论文作为例证

---

## 与其他文件的关系

| 你在做的事 | 同步更新 |
|---|---|
| 新论文入库 | `../refs/pool.csv` → 通过核验后 `../refs/verified.csv` |
| 完成 skim | CSV 的 `read_status` → `skim` |
| 完成 deep | CSV 的 `read_status` → `deep`，补齐全部 `axis_*` 字段 |
| 发现新争议 | `../synthesis/open-questions.md` |
| 修改分类轴 | `../synthesis/taxonomy.md` 的**修订记录表**（必填） |
| 下载 PDF | `python ../scripts/fetch_pdfs.py` |

---

## 相关文件

- Schema 模板：[`TEMPLATE.md`](TEMPLATE.md)
- 工作契约：[`../AGENTS.md`](../AGENTS.md) §4
- 质量门禁：[`../AGENTS.md`](../AGENTS.md) §6
