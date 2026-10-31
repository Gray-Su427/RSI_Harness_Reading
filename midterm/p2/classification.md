# 分类总表（9 篇核心论文）

> 负责人：P2（zyc）｜日期：2026-10-31｜状态：CP2 工作稿，待精读确认
>
> 口径：7 篇精读候选（P4 名单）+ 2 篇泛读补充（SICA、MGM）；E 轴以作者自我界定为准；A 轴记「主值（次值）」。
> 数据源：[`refs/verified.csv`](../../refs/verified.csv)、[`notes/skim/`](../../notes/skim/)；原文核对仅限 P2 认领的 DGM、AlphaEvolve，其余标「据 skim 卡，待精读复核」。

## 1. 总表

| # | 论文（ID） | 组内角色 | A 主值（次值） | B 信号 | C 算子 | D 保证 | E 暂定 |
|---|---|---|---|---|---|---|---|
| 1 | STOP `arxiv-2310.02304` | 7 篇精读（P1） | `code`（`prompt/context`） | `external-verifier` | `refine` + `evolutionary` | `empirical` | `iterative` |
| 2 | ADAS `arxiv-2408.08435` | 7 篇精读（P1） | `control-flow`（`code`） | `external-verifier` | `evolutionary` | `empirical` | **待精读** |
| 3 | DGM `arxiv-2505.22954` | 7 篇精读（P2） | `code`（`tool/prompt/context`；**不含 `evaluator`**） | `external-verifier` | `evolutionary` | `empirical` | `full-rsi` |
| 4 | AlphaEvolve `arxiv-2506.13131` | 7 篇精读（P2，边界） | `code`（任务算法，非 harness 自身） | `external-verifier` | `evolutionary` | `empirical` | **待精读** |
| 5 | RHO `arxiv-2606.05922` | 7 篇精读（P3） | `tool`（`memory/prompt`） | `self-preference` | `textual-gradient` + `refine` | `empirical` | `one-shot` |
| 6 | SEVerA `arxiv-2603.25111` | 7 篇精读（P3，跨界） | `code`（`control-flow`；Learn 另改权重） | `external-verifier`（形式化） | `tree-search` + `meta-optimizer` | `formal-safety` | **待精读** |
| 7 | Harness≠Benefit `arxiv-2605.30621` | 7 篇精读（P4） | `memory`（`prompt`） | `failure-trajectory`（生成）+ `external-verifier`（测量） | `refine`（沿用协议） | `none`（测量研究） | **待精读** |
| 8 | SICA `arxiv-2504.15228` | 泛读补充（P2） | `code`（`tool/prompt`） | `external-verifier` | `refine` | `empirical` | `full-rsi`（候选） |
| 9 | MGM `arxiv-2608.07645` | 泛读补充（P2） | `code` | `failure-trajectory`（主）+ `external-verifier`（次） | `evolutionary` | `empirical` | **待精读** |

**计数（主值）**：A = code 6 / control-flow 1 / tool 1 / memory 1；B = external-verifier 6 / failure-trajectory 2 / self-preference 1；D = empirical 7 / formal-safety 1 / none 1；E = one-shot 1 / iterative 1 / full-rsi 1（+1 候选）/ co-evolution 0 / 待精读 5。C 轴多值，不单列合计。

> **读表**：DGM、AlphaEvolve 的 A–D 已回原文核对；其余 7 篇的 A–D 来自 skim 卡，标「据 skim 卡，待精读复核」。E 轴 5 篇（ADAS、AlphaEvolve、SEVerA、Harness≠Benefit、MGM）没有作者自我界定，统一标「待精读」，**不按轮数推断**。

## 2. 逐篇依据与待核

### ① STOP `arxiv-2310.02304`

- **A**：据 skim 卡，`code` 为主，`prompt/context` 为次；被改进的 improver 是一段 Python scaffolding 程序。
- **E**：作者原话「Since the language models themselves are not altered, this is not full recursive self-improvement.」→ 只能确认「不是 full-rsi」；机制上改进后的 improver 进入下一轮，故本表暂记 `iterative`。**CSV 记 `one-shot`，与本表冲突**，待 P1 按作者原话与迭代机制统一。
- **B/C/D**：meta-utility 外部评分；seed 为 best-of-N refine，LM 可提出 beam/GA/SA/tree 等策略，整体记 `refine + evolutionary`；按 meta-utility 保留最优，`empirical`。
- **待核**：COLM 2024 仅页眉自述，`venue_verified: false`；无同算力随机搜索基线；成本只有渐近式。

### ② ADAS `arxiv-2408.08435`

- **A**：`AXES.md` 把 ADAS 列为 `control-flow` 的典型代表；skim 卡却记 `code` 为主（因为 meta-agent 在完整 agent 代码空间搜索）。**主值口径冲突**；CP2 暂按 `control-flow` 主、`code` 次，待精读裁定。
- **E**：未找到作者自我界定；meta-agent 固定，target agent 进 archive。本表记 **`待精读`**，不把「多轮搜索」直接写成 `iterative`。CSV 记 `one-shot`，不作为最终结论。
- **B/C/D**：held-out test accuracy / F1；archive-based open-ended search，暂记 `evolutionary`（CSV 记 `tree-search`）；按分数保留，`empirical`。
- **待核**：SICA 批评 ADAS「not self-improving」是 SICA 作者判断，不是 ADAS 自述；ICLR 2025 仅页眉自述，`venue_verified: false`。

### ③ DGM `arxiv-2505.22954`

- **A**：原文定义「we define self-improvement as a coding task that involves modifying the design of an agent's own components (i.e., its own code, which does not include the open-ended exploration process described in the next paragraph).」→ `code`；archive/父代选择/评测固定，**不是 `evaluator`**；次要 `tool/prompt/context`（编辑工具、长上下文、peer-review）。
- **E**：原文「iteratively modifies its own code (thereby also improving its ability to modify its own codebase)」→ `full-rsi`；边界「archive maintenance, parent selection is fixed and not modifiable」+ frozen FM weights → full-rsi 只在代码层，不在模型层。
- **B/C/D**：coding benchmark pass rate；archive + 父代选择 + 自修改，`evolutionary`；经验验证，无形式化证明。
- **结果口径**：SWE-bench **20.0% → 50.0%**（最终强候选在 200 题子集；分阶段 10 → 60 → 200）；Polyglot 50 题子集 **14.0% → 38.0%**、全量 **14.2% → 30.7%**。主数字是 best agent vs base agent，不是均值；每个 benchmark 单次 run。
- **成本**：约 **$22,000 / 2 周**；两个 baseline 各约 **$10,000**（§E.1）。
- **交 P1**：CSV 的 A 轴 `code;evaluator` 建议改为 `code`（次值 `tool;prompt;context`）；`org` 建议补 University of British Columbia + Vector Institute（原文署名含），不只 Sakana AI。

### ④ AlphaEvolve `arxiv-2506.13131`

- **A**：`code`，但改的是**任务算法**，不是 AlphaEvolve 自身 pipeline；prompt 模板、LLM ensemble、program database、evaluator 都是固定外壳 → **边界对照，不算 harness 自进化证据**。
- **E**：未找到 RSI 自我界定；讨论段「increase the efficiency of its own infrastructure and of (future versions of) its base LLMs... feedback loops ... on the order of months」是基础设施/未来模型，且未完成 → **`待精读`**；若强行分层，产物层 iterative、harness 层 one-shot，但不填入 E。
- **B/C/D**：code execution + automatic evaluator；LLM-guided diff + program database + MAP-Elites/island，`evolutionary`；`empirical`。
- **成本**：部分报告，约 100 compute-hours / 次评测，无整轮总成本；白皮书非同行评审；无代码/program database 公开声明。
- **用途**：工业级「强外部 evaluator + 进化搜索」参照；不据此宣称 harness RSI。

### ⑤ RHO `arxiv-2606.05922`

- **A**：harness = instructions/skills markdown + tools scripts；`tool` 主、`memory/prompt` 次；CSV 记 `prompt;control-flow;tool`，主值待 P3 精读统一。
- **E**：作者原话「We evaluated a single retrospective optimization round and make no claim that gains compound or even remain monotonic across multiple rounds...」→ `one-shot`；**CSV 记 `iterative`，建议 P1 更正**。
- **B/C/D**：self-preference（pairwise rank + self-validation/consistency）；`textual-gradient + refine`；接受门控 `S_j > 0`，`empirical`，不是形式化保证；作者主动报告「最偏好 ≠ 测试最高」反例。
- **用途**：B 轴 `self-preference` 唯一正面样本；争议 Q2 必读。

### ⑥ SEVerA `arxiv-2603.25111`

- **A**：`code` 主、`control-flow` 次；Search 合成 parametric agent program，Learn 用 GRPO 微调权重 → **跨界到模型层**，不算纯 harness。
- **E**：未找到 RSI 自我界定；作者称 `self-evolving`，但未界定是否满足本组 RSI 定义 → **`待精读`**。
- **B/C/D**：Dafny 形式化验证器 + held-out loss；CEGIS `tree-search` + GRPO `meta-optimizer`；`formal-safety`（Theorem 5.4 功能正确性；资源无感知，原文自陈不覆盖 LLM calls / token / wall-clock）。
- **用途**：D 轴 `formal-safety` 唯一例证；争议 Q4 必读；不要把「零违规」扩展为所有行为安全。

### ⑦ Harness≠Benefit `arxiv-2605.30621`

- **A**：被测协议改 skills（`memory` 主）、MCP-Atlas 另含 prompts（`prompt` 次）；tools 只读；**A/B 记录的是被测协议，不是本文贡献**。
- **B**：evolver 用 execution evidence（`failure-trajectory` 主）；最终测量用 benchmark pass rate（`external-verifier` 次）；不要把测量分数当成更新时反馈。
- **C/D**：沿用 fix-solve 多轮 solve-evolve，`refine`（非本文贡献）；`none`（测量研究，不提供改进保证）。
- **E**：协议 T 步迭代，但作者未用 RSI 一词、未自我界定 → **`待精读`**；不因「多轮」写成 `iterative`。
- **用途**：争议 Q1 核心证据；「能更新 ≠ 有收益」。

### ⑧ SICA `arxiv-2504.15228`

- **A**：`code` 主、`tool/prompt` 次；操作完整 Python codebase。
- **E**：作者原话「our self-improving coding agent is fully self-improving (i.e. there is no distinction between the meta and target agent), and it operates over the agent's full Python codebase.」→ 作者自称 fully self-improving；按 AXES 字面可判 `full-rsi`，但 skim 卡保守记 `iterative`；本表记 **`full-rsi`（候选）**，待精读裁定。
- **B/C/D**：benchmark + utility；`refine`（archive argmax，单支）；`empirical`。
- **待核**：增益构成含文件编辑/成本优化；AIME/GPQA 几乎无提升；无同算力随机搜索基线；15 轮约 $7,000。

### ⑨ MGM `arxiv-2608.07645`

- **A**：`code`；B `failure-trajectory` 主 + `external-verifier` 次；C `evolutionary`；D `empirical` + Proposition 1（依赖 sound comparative evidence 假设，非系统级 formal）。
- **E**：标题用 `Recursive Self-Improving`，但正文未给出「本工作是否构成 RSI」的显式自我界定；附录 F.2 那句是在反驳直觉 → **`待精读`**，不按标题升级。
- **待核**：与 DGM 作者不重叠，可作独立证据；但迁移实验用 60-task subset 外推完整 Polyglot；seed 多样性有限。

## 3. E 轴作者原话（Gate 2 用）

| 论文 | E 暂定 | 作者原话（逐字） | 位置 / 说明 |
|---|---|---|---|
| STOP | `iterative` | “Since the language models themselves are not altered, this is not full recursive self-improvement.” | 作者明确否认 full RSI；机制为改进后的 improver 进入下一轮 |
| ADAS | **待精读** | 未找到作者自我界定；全文 “recursi” 仅出现在参考文献（引用 STOP） | 不能把 meta-agent 固定的多轮搜索写成 `iterative` |
| DGM | `full-rsi` | “iteratively modifies its own code (thereby also improving its ability to modify its own codebase)” | 摘要；边界见 “archive maintenance, parent selection is fixed” |
| AlphaEvolve | **待精读** | 未找到 RSI 自我界定；最接近：“...increase the efficiency of its own infrastructure and of (future versions of) its base LLMs. Currently, the gains are moderate and the feedback loops ... are on the order of months.” | 讨论段；基础设施/未来模型，非已完成 harness 闭环 |
| RHO | `one-shot` | “We evaluated a single retrospective optimization round and make no claim that gains compound or even remain monotonic across multiple rounds...” | 作者明确单轮 |
| SEVerA | **待精读** | 未找到 “recursive self-improvement” 自我声明；最接近：“After tuning, SEVerA maintains a pool of verified fine-tuned agents and uses their execution traces on D to generate new candidates...” | “self-evolving” ≠ 本组 RSI 定义 |
| Harness≠Benefit | **待精读** | “Starting from an initial harness H0, the protocol iterates for T steps...”; “we keep f fixed and only update editable components of Ht” | 协议迭代，但作者未用 RSI 一词、未自我界定 |
| SICA | `full-rsi`（候选） | “our self-improving coding agent is fully self-improving (i.e. there is no distinction between the meta and target agent), and it operates over the agent's full Python codebase.” | 作者自称 fully self-improving；full-rsi 口径待精读裁定 |
| MGM | **待精读** | “Self-improving coding agents that iteratively rewrite their own source code...”; 附录 F.2 “Since recursive self-improvement ultimately edits the agent's own codebase, it is tempting to view self-evolution as another coding task.” | 第二句是反驳直觉，不是自我声明；标题不足以上升 |

## 4. 交 P1 的 CSV 回填 / 更正建议

> P2 不直接改 `refs/verified.csv`；以下建议由 P1 核验后决定是否写入，并在 `note` 字段留痕。

| 论文 | 字段 | 现值 | 建议 | 依据 | 优先级 |
|---|---|---|---|---|---|
| DGM | `axis_a_object` | `code;evaluator` | `code`（次值 `tool;prompt;context`） | 原文明确 archive/父代选择/评测固定；self-improvement 只含 own code | 高 |
| DGM | `org` | `Sakana AI` | `Sakana AI + University of British Columbia + Vector Institute` | 原文署名 | 中 |
| RHO | `axis_e_recursiveness` | `iterative` | `one-shot` | 作者明确单轮、不声称累积 | 高 |
| STOP | `axis_e_recursiveness` | `one-shot` | `iterative`（或保留 `one-shot` + note 说明口径） | 作者只否认 full RSI；改进后的 improver 进入下一轮 | 中 |
| ADAS | `axis_e_recursiveness` | `one-shot` | `unknown`（待精读） | 未找到作者自我界定 | 中 |
| ADAS | `axis_c_search` | `tree-search` | `evolutionary`（待精读） | archive-based open-ended search | 低 |
| AlphaEvolve | `axis_e_recursiveness` | `one-shot` | `unknown`（边界：产物层 iterative，harness 层不递归） | 无 RSI 自我界定 | 中 |
| SEVerA | `axis_e_recursiveness` | 空 | `unknown`（待精读） | 无 RSI 自我界定 | 中 |
| SEVerA | `axis_c_search` | 空 | `tree-search; meta-optimizer` | CEGIS + GRPO | 中 |
| Harness≠Benefit | `axis_a_object` | 空 | `memory`（主）；`prompt`（次） | skills 更新；MCP-Atlas 另含 prompts | 中 |
| Harness≠Benefit | `axis_b_signal` | 空 | `failure-trajectory`（主）；`external-verifier`（测量） | execution evidence + pass rate | 中 |
| Harness≠Benefit | `axis_d_guarantee` | 空 | `none` | 测量研究 | 低 |
| Harness≠Benefit | `axis_e_recursiveness` | 空 | `unknown`（待精读） | 协议 T 步迭代但无自我界定 | 中 |
| SICA | `axis_b_signal` | `failure-trajectory` | `external-verifier` | benchmark 准确率 + utility；非自评 | 中 |
| SICA | `axis_c_search` | `evolutionary` | `refine` | 每轮 archive argmax 单支，无种群/交叉 | 中 |
| SICA | `axis_e_recursiveness` | `iterative` | `full-rsi`（候选）或保留 `iterative` + note | 作者自称 fully self-improving | 中 |
| MGM | `axis_b_signal` | 空 | `failure-trajectory`（主）；`external-verifier`（次） | 多条轨迹比较 + benchmark | 中 |
| MGM | `axis_e_recursiveness` | `iterative` | `unknown`（待精读） | 正文无自我界定 | 中 |
| RHO | `axis_a_object` | `prompt;control-flow;tool` | `tool`（主）；`memory/prompt`（次） | harness = instructions/skills + tools scripts | 中 |
| RHO | `axis_c_search` | 空 | `textual-gradient; refine` | 文本梯度 + 单轮 refine | 低 |
| RHO | `axis_d_guarantee` | 空 | `empirical` | 接受门控 `S_j > 0`，非形式化 | 低 |
| Harness≠Benefit | `axis_c_search` | 空 | `refine` | 沿用 solve-evolve 协议，非本文贡献 | 低 |

## 5. 待精读 / 需 P3 确认

- **E 轴 5 篇**（ADAS、AlphaEvolve、SEVerA、Harness≠Benefit、MGM）需要作者原话；P3 的精读笔记要补。
- **A 轴 ADAS 主值**（`control-flow` vs `code`）需要 P1/P2 精读统一。
- **RHO 的 A 轴主值**（`tool` vs `prompt`）需要 P3 精读统一。
- **SICA 的 `full-rsi` 口径**需要 P2 精读裁定。
- 图上的「待精读」带不是 `one-shot`；P3 在 deck 中不要把 5 篇说成「低递归」。

## 6. 来源

- `refs/verified.csv`（2026-10-31 读取）
- `notes/skim/*.md`（17 篇，2026-10-13）
- DGM：arXiv HTML v3，§1/§3/§4/§E.1，访问 2026-10-31
- AlphaEvolve：arXiv HTML v1，§1/§2/§3.1/§3.3/§6，访问 2026-10-31
- `notes/AXES.md`、`notes/TEMPLATE.md`、`midpre-checkpoint.md`
