# 分类体系（五轴，待验证）

> ⚠️ **状态：工作假设，尚未定稿。**
>
> 这五轴是本组自己提出的，**不是既有共识**。精读阶段的任务之一就是**用论文推翻或修正它**。
>
> **判定该轴是否成立的标准**：
> - 某轴无法覆盖 **≥80%** 的精读论文 → 该轴有问题
> - 某轴需要塞进大量 `other` 才能容纳 → 该轴粒度不对
> - 某两轴高度相关（无法独立赋值）→ 考虑合并
>
> **每次修改请在文末「修订记录」留痕。**

---

## 选轴的思路

分类体系要服务于两个用途：

1. **描述**——这批工作彼此在哪些方面不同
2. **诊断**——能否看出趋势、空白、或争议集中在哪里

因此轴要**正交**：每篇论文在每条轴上都能独立赋值，不依赖其他轴。
如果填 A 轴时必须先看 B 轴，说明这两轴不独立。

---

## 轴 A · 改进对象（改的是什么）

被修改的 harness 组件。

| 值 | 含义 | 典型代表 |
|---|---|---|
| `prompt` | 系统提示 / 指令模板 | Self-Refine、OPRO 谱系 |
| `control-flow` | 控制流、agent 拓扑、多智能体编排 | ADAS、AFlow |
| `code` | agent 自身的源代码本体 | STOP、SICA、DGM、MGM |
| `tool` | 工具的定义、新增、剪枝、选择 | 工具创建 / 工具选择类 |
| `memory` | 记忆、技能库、长期档案 | Voyager 谱系 |
| `evaluator` | 评测器 / 验证器本身 | DGM 的经验验证器 |
| `context` | 上下文组织与轨迹生成策略 | harness-in-the-loop 类 |

### 🔍 反例预警

**一篇论文可能同时命中多值。**

例：DGM 同时改 `code`（自修改代码库）与 `evaluator`（经验验证器）。

**规则**：
- 必填 = 该工作**主要贡献**所对应的值
- 次要值追加，用列表形式保存
- **不要**为了"纯粹"而强行归入单值

**归类冲突本身就是分类体系的诊断信号**——若某篇频繁触发冲突，记入待核实项。

---

## 轴 B · 改进信号（改进的依据从哪来）

| 值 | 含义 | 主要风险 |
|---|---|---|
| `self-preference` | 系统自评 / 自偏好，无外部真值 | 循环论证风险最高 |
| `external-verifier` | 可执行验证：单元测试、benchmark 分数 | 需检查验证集是否泄漏 |
| `human` | 人类反馈 | 难以规模化，与 RSI 的自举特性存在张力 |
| `failure-trajectory` | 从失败轨迹中提取改进 | 依赖失败样本的选择偏差 |

### 🔍 关键追问

> **验证信号是否独立于被优化对象？**

若 harness 既生成改进、又验证改进，且两者来自同一模型，则构成循环论证。
这直接对应争议 **Q2**。

参见 RHO（`arxiv-2606.05922`）——它用自偏好替代真值验证，等于**承认外部验证在部署场景中不可得**。
那么它引入的是自治，还是把循环论证写得更优雅？

---

## 轴 C · 搜索算子（怎么搜）

| 值 | 含义 |
|---|---|
| `refine` | 迭代精修（逐轮改写，无种群） |
| `evolutionary` | 进化搜索 / 遗传算法 / 种群 + 选择 |
| `textual-gradient` | 文本梯度（自然语言反馈充当"梯度"） |
| `tree-search` | 树搜索 / 分支探索 |
| `meta-optimizer` | 元学习得到的优化器 |

### 📌 范围说明

本轴**刻意不含** `prompt` 类工作（OPRO / Self-Refine 的文本梯度搜索）。

理由：那条线属于**提示优化**而非 **harness 自进化**——改进产物不参与下一轮改进，
不满足 RSI 的递归定义。若组员认为应纳入，在修订记录中说明并扩轴。

---

## 轴 D · 保证强度

| 值 | 含义 |
|---|---|
| `none` | 无保证，纯经验报告 |
| `empirical` | 有经验性筛选（只保留分数提升的变体） |
| `formal` | 有形式化 / 可验证保证 |
| `formal-safety` | 有显式安全约束与证明 |

### 🔍 追问

> **保证的代价是什么？**

SEVerA（`arxiv-2603.25111`）提供形式化安全保证，多数工作只做经验性筛选。
后者是否更"有效"？前者是否因为约束太紧而只在窄场景成立？

参见争议 **Q4**。

---

## 轴 E · 递归深度（本方向最关键的轴）

**这一轴直接对应 RSI 的定义**：改进后的系统能够继续参与下一轮改进。

| 值 | 含义 |
|---|---|
| `one-shot` | 单次改进，改进产物不参与下一轮 |
| `iterative` | 改进后的系统参与下一轮改进 |
| `full-rsi` | 改进的不只是产物，**改进器本身也被改进** |
| `co-evolution` | harness 与模型互为对方的数据生成源 |

### 🔍 反例预警（必须记入笔记）

**STOP（`arxiv-2310.02304`）**
作者**自己声明**："由于语言模型本身未被改变，这不属于完整的递归自我改进。"
→ 必须**原文照抄**这个限定。**不得**因为该文在后续文献中常被归入 RSI 就拔高。

**DGM（`arxiv-2505.22954`）**
明确宣称改进了"改进自身代码库的能力" → `full-rsi`。

**`co-evolution`（2026 年新表述）**
如 harness-in-the-loop 类工作（`arxiv-2607.15524`）——
需在精读中确认：它是**真正的共进化**，还是 `iterative` 的重新包装？

### 📌 填写规则

- 找不到作者的自我界定 → 填 `unknown`，记入笔记第 9 节，**不要替作者下结论**
- 这一轴**必须**附作者原话佐证（`AGENTS.md` Gate 2 要求）

---

## 分类总表（待填充）

精读阶段完成后，用此表呈现分类结果。

| 论文 ID | A 改进对象 | B 信号 | C 搜索 | D 保证 | E 递归 | 工业界 |
|---|---|---|---|---|---|---|
| `arxiv-2310.02304` STOP | code | external-verifier | refine; evolutionary | empirical | one-shot | — |
| `arxiv-2408.08435` ADAS | control-flow; code | external-verifier | tree-search | empirical | one-shot | — |
| `arxiv-2504.15228` SICA | code | failure-trajectory | evolutionary | empirical | iterative | — |
| `arxiv-2505.22954` DGM | code; evaluator | external-verifier | evolutionary | empirical | **full-rsi** | ✅ |
| `arxiv-2506.13131` AlphaEvolve | code | external-verifier | evolutionary | empirical | one-shot | ✅ |
| `arxiv-2608.07645` MGM | code | — | evolutionary | empirical | iterative | — |
| `arxiv-2606.05922` RHO | prompt; control-flow; tool | **self-preference** | — | — | iterative | — |
| `arxiv-2603.25111` SEVerA | code; control-flow | external-verifier | — | **formal-safety** | — | — |
| `arxiv-2607.15524` | context | — | — | — | co-evolution | — |

> **留空的格子 = 尚未精读，不是"无"。**
> 每完成一篇精读就补一行；精读完成后重新审视这张表——若某列几乎全空，该轴可能该删。

---

## 后续待扩展的方向

以下子领域尚未纳入样本，扩池时补齐：

- 提示 / 系统提示自优化（OPRO、Self-Refine 谱系）
- 工具自创建与自选择
- 记忆与技能库自进化（Voyager 谱系）
- 多智能体拓扑搜索（AFlow、GPTSwarm 系）
- LLM 驱动的进化搜索（EvoPrompt 系）
- 自进化 agent 的安全与对齐

---

## 修订记录

| 日期 | 改动 | 原因 |
|---|---|---|
| 2026-10-12 | 从 `AGENTS.md` §5 迁出，建立五轴初稿 | 立项 |

---

## 相关文件

- Schema 中对应字段：[`../notes/TEMPLATE.md`](../notes/TEMPLATE.md)
- 候选争议：[`open-questions.md`](open-questions.md)
- 论文元数据：[`../refs/verified.csv`](../refs/verified.csv)
