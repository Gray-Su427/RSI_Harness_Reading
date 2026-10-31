---
id: venue-2026-dcri-survey
title: "Data-Centric Recursive Improvement for Foundation Models: A Survey"
authors: "Zou, Chen, Kwok, et al."
year: 2026
venue: "Preprints (Preprints.org)"
venue_verified: false
industry: true
org: "JD Future Academy + HKUST (Guangzhou) + UCLA + University of Cambridge 等 8 家"
role: survey
read_status: skim
read_date: 2026-10-31
---

> **来源**：[Preprints.org 记录](https://www.preprints.org/manuscript/202609.0154)（DOI `10.20944/preprints202609.0154`）· [OpenReview](https://openreview.net/forum?id=zGqv8Jsh4Y) · [论文 PDF](https://github.com/zoezou2015/Awesome-Data-Centric-Recursive-Improvement/blob/main/paper/dcri_survey_2026.pdf) · [companion repo](https://github.com/zoezou2015/Awesome-Data-Centric-Recursive-Improvement)。
> **arXiv 核验**：`ti:"Data-Centric Recursive Improvement"` 命中 **0** 条；`all:"data-centric recursive"` 仅命中 2 条无关工作（`2609.36675` Gödel Forest、`2610.15782` RSI-Nav）。**本篇无 arXiv 版本**，故按命名规范用 `venue-2026-<slug>`，不走 `arxiv-` 前缀。
> 访问日期：2026-10-31。逐字引文来自其 companion repo（README 声明由论文源文件生成，章节与计数与论文一致）；**PDF 正文尚未逐页核对**，凡引文均标注来源层级。

**一句话**：把「数据」当成递归改进的更新对象，用「评测信号 → 编排决策 → 执行更新」三段闭环（外加一段可靠性审计）综述 300 篇 2020–2026 的工作，核心机制命名为 **data–evaluation co-evolution**。

**领域地图贡献**：

1. **明确站在「数据层」而非「harness 层」**。companion repo 开篇的框架是：

> Evaluation is not a report card, and data is not a fixed input. Evaluation produces diagnostic signals, **orchestration** decides whether and how those signals should be trusted and used, and **execution** updates mutable data-related objects that shape the next round of training, adaptation, retrieval, or memory.

这句话的**更新对象是被数据塑造的东西**（训练语料、检索库、记忆、后训练数据），不是组织这些数据的程序。按课程三层划分（Model / Data / Harness），它属于 **Data 层**——**本组方向之外**。它对本选题的价值因此不是「证据」，而是**边界的反面参照**：说明「递归」这个词在数据层同样成立，因此选题边界必须写明 harness 层的不可替代性。

2. **三段循环 + 一段审计的分节结构**（章节标题与计数可在 repo 目录中核对）：

| 环节 | 章节 | 收录数 |
|---|---|---|
| 开篇 | 1. Introduction | 16 |
| 评测信号（what signal） | 2. Evaluation Signals | 65 |
| 编排决策（who decides） | 3. Orchestration Decisions | 70 |
| 执行机制（what object） | 4. Execution Mechanisms（含 4.5 Context and Memory as Data-Centric Adaptation） | 159 |
| 失败模式 | 5. Failure Modes of Data–Evaluation Co-Evolution | 25 |
| 未来方向 | 6. Future Directions | 57 |

> 计数按章节计，同一篇可在多节重复出现，故六节之和（392）大于「300 cited works」——引用其数字时须说明口径。

3. **两处与本组五轴直接可对话的设计**：
   - §3.3 标题为 *Representative Adaptive Data-Orchestration Systems and Their **Recursive Boundaries***——它显式讨论「递归到哪里为止」，与我们的 E 轴同题；但其判据是「数据更新能否反馈到下一轮的编排决策」，不是「改进器本身是否被改进」。
   - §5.2 *Dependent or Exposed Feedback Signals* 与 §5.4 *Data-Support Loss under Recursive Generation*（含 model collapse 一支）分别对应我们的 **B 轴独立性**与**递归的失效模式**，可作为争议 Q2 的外部佐证（**仅作背景**，按 `AGENTS.md` §7.3 标注 `via`，不进 evidence 文件）。

**改进对象**：数据侧对象——训练/后训练数据、检索库、记忆、评测信号本身。映射到我们的 A 轴只有 `memory` 与 `context` 两值可部分对应，**`code` / `control-flow` 基本不覆盖**。这正是它能用来划边界的证据。

**改进信号**：以 benchmark 分数、LLM/MLLM judge、偏好比较、环境结果为信号（§2.1 六类：Benchmark Scores / Failure Clusters / Verifier Labels / Preference Comparisons / Judge Rationales / Environment Outcomes），并在 §5.2 专门讨论信号被污染或与优化目标耦合的情形。

**递归深度**：**原文未见四级分级**；有「recursive boundaries」这一概念化讨论（§3.3），但没有可落表的取值。按 [`../AXES.md`](../AXES.md) 规则不代作者下结论，CSV 的 E 轴留空，精读时回查 §3.3 原文表述。

**可复现性**：综述，无实验；companion repo 的 300 条阅读列表按论文小节组织，可逐条回溯。

**是否入选精读**：否——不在 P4 冻结的 7 篇名单内，也不提供可检验的自我改进效果。用途仅限两处：① 领域地图中标注 Data 层的边界；② 选题边界说明中回答「为什么不把数据自进化纳入」。

**可疑之处**：
1. **未同行评审**：Preprints.org 预印本 + OpenReview 记录，`venue_verified: false`。作者阵容（JD Future Academy + 7 家高校/院所，16 位作者）与 300 篇的体量不构成质量证据。
2. **覆盖面偏多模态**：从章节条目看，图像/视频生成、MLLM 评测、reward model 占比较大，与「harness 自进化」重叠的实际条目很少（仅 Ornith-1.5 一类 self-scaffolding 工作被提到）。
3. **企业署名**：JD Future Academy 属企业机构，按本组口径 `industry: true`；但它是综述、**不得充当 Gate 2 的工业界实证项**（同 `arxiv-2605.18747`、`arxiv-2610.00093` 的处理）。
4. **引文层级**：本卡逐字引文来自 companion repo 而非 PDF 正文，若写作时直接引用，须先打开 PDF 核对页码与措辞。
