# P1 · 论文五问卡：ADAS

> 负责人：P1（xyc）｜人员代号：P1 = xyc｜P2 = zyc｜P3 = szh｜P4 = zgj
> 本卡为中期数据核对卡，不是精读笔记；精读产出见 `notes/deep/`。

## 文献与核对范围

- **论文**：Automated Design of Agentic Systems（ADAS）
- **ID**：`arxiv-2408.08435`；2024；查阅版本：arXiv v2（2025-03-02）+ ICLR 2025 正式版条目。
- **来源**：[arXiv 摘要](https://arxiv.org/abs/2408.08435) · [ICLR 2025 论文集](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36b7acf6f6010652b3f2a433774a66fe-Abstract-Conference.html) · 项目页 [shengranhu.com/ADAS](https://shengranhu.com/ADAS) · 泛读卡 [`../../notes/skim/arxiv-2408.08435.md`](../../notes/skim/arxiv-2408.08435.md)。
- **访问日期**：2026-10-31。
- **核对状态**：已核对摘要与 venue 官方论文集；**实验表、消融与成本未逐页核对**。
- **Venue**：**ICLR 2025（Conference）**，`venue_verified: true`，证据见 [`venue-verification.md`](venue-verification.md) §2.2。精读以 ICLR 2025 正式版为准，不用 arXiv v1。

## 1. 一句话贡献

【原文】

> We present a simple yet effective algorithm named Meta Agent Search to demonstrate this idea, where a meta agent iteratively programs interesting new agents based on an ever-growing archive of previous discoveries.

【本组判断】贡献是把 harness 的一个子空间（agent 的代码化设计）变成搜索问题。它改的是 **target agent**，不是搜索器。

## 2. 改什么 —— A 轴

【原文】

> Given that programming languages are Turing Complete, this approach theoretically enables the learning of any possible agentic system: including novel prompts, tool use, workflows, and combinations thereof.

【本组判断】主值 `control-flow`（工作流/编排结构），次值 `code`（改动以代码落地）。不记 `prompt`、`tool`：被搜索的单位是「整个 agent 程序」，不是单独的提示词或工具定义。

## 3. 凭什么改 —— B 轴

【原文】以 coding / science / math 三类任务上的 benchmark 分数筛选新 agent，并以跨领域、跨模型迁移后仍优于手工设计作为核心证据。

【本组判断】记 `external-verifier`。待查项：archive 选择所用分数与报告 SOTA 的分数是否同一批任务。

## 4. 递归到哪层 —— E 轴

【原文，摘要】循环描述只到「迭代」：

> a meta agent iteratively programs interesting new agents based on an ever-growing archive of previous discoveries

作者**未对「是否属于 RSI」作任何自我界定**（既未宣称 RSI，也未像 STOP 那样声明「不算完整 RSI」）。

【本组判断】按 [`../../notes/AXES.md`](../../notes/AXES.md) §E，作者未界定时不得代下结论。可记录的描述是：改进器（meta agent）在搜索中固定，被改进的是它产出的 target agent；archive 让前代产物参与下一轮，参与方式是「作为元 agent 的上下文」，不是「成为改进器」。

**已登记的口径冲突（交 P2／CP2，P1 不擅自改 CSV）**：CSV 现记 `axis_e_recursiveness = one-shot`，而 AXES.md 对该值的定义是「改进产物不参与下一轮」，ADAS 的 archive 使前代产物进入下一轮取样，严格按定义更接近 `iterative`。
两种处理均可辩护：①「参与」指成为改进器 → `one-shot`；②「参与」指进入下一轮搜索 → `iterative`。
**处理方式**：由 P2 先明确 AXES.md 中「参与」的主语，再决定 ADAS 与 DGM 的取值；在此之前记录统一用中性表述「单层搜索、改进器固定」。

## 5. 最可疑的一点

【本组判断】

1. **改进器固定即天花板固定**：元 agent 的能力决定它能写出多好的 agent；论文未回答「元 agent 自身能否被改进」。这是 DGM 相对 ADAS 的增量，也是 `full-rsi` 判据的分界。
2. **「Turing 完备 ⇒ 能学会任何 agent 系统」是可能性论证，不是经验结论**：只说明表达力，不说明可达性与效率（需要多少预算）。引用时必须保留「理论上」。
3. **证据独立性**：ADAS（Hu, Lu, Clune）与 DGM（Zhang, Hu, Lu, Lange, Clune）作者高度重叠、问题设定相近、结论互相支持，按 `AGENTS.md` §6 应合并为一条证据，不可当两条独立证据凑 Gate 2。
4. **迁移结论的对照范围**：摘要称发明的 agent 跨领域、跨模型仍优，但未说明基线是否同预算；此类结论易被预算差解释（争议 Q3）。

## 6. 已核对事实与出处

| 事实 | 出处 | 状态 |
|---|---|---|
| 搜索方式：meta agent 在 archive 上迭代编程 | 摘要 | 已核对（摘要层） |
| 被改对象：agent 以代码定义 | 摘要 | 已核对（摘要层） |
| 实验域：coding / science / math | 摘要 | 已核对（摘要层） |
| 主结论：超越手工设计 agent，且可迁移 | 摘要 | 已核对（摘要层，无具体数字） |
| 理论主张：Turing 完备 ⇒ 理论上可学任意 agent 系统 | 摘要 | 已核对（摘要层） |
| 主结果数字、基线设置、是否同预算 | 正文表格（未读） | **待核对** |
| archive 选择规则与验证/报告集隔离 | 正文（未读） | **待核对** |
| Venue = ICLR 2025 Conference | ICLR 2025 论文集 | 已核对 |

## 7. 中期后精读待办

- [ ] 回查 archive 选择规则与验证集/报告集隔离（Q2）。
- [ ] 补齐主结果数字、基线设置与同预算情况（Q3）。
- [ ] 确认 ICLR 2025 正式版与 arXiv v1 的差异（尤其附录消融）。
- [ ] 与 STOP 对照：两者都固定改进器，但 STOP 的改进器改自己、ADAS 改产物——该差别写入证据链。
- [ ] 把 E 轴口径冲突提交 P2；确认后由 P1 更新 CSV（ID 不变）。
- [ ] 完成 `notes/deep/arxiv-2408.08435.md` 的完整 Schema。
