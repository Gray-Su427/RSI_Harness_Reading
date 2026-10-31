# AGENTS.md — Reading 仓库工作契约

> 本文件是本项目**阅读与核验**工作的操作规程，对人类组员与 AI 助手共同生效。
> 本仓库只负责论文链接与阅读笔记；综述写作规则在写作仓库 `../RSI_Harness_Writing/AGENTS.md`。
> 规则与课程要求冲突时，以课程要求为准，并立即修订本文件。

---

## 0. TL;DR — 五条不可违反的规则

1. **入库前必须核验 arXiv ID 真实存在。** 幻觉出来的文献比没有文献更有害。
2. **未核验的 venue 一律标 `venue_verified: false`**，禁止把 preprint 说成会议论文。
3. **精读笔记必须使用第 4 节的完整 Schema。** 字段缺失的笔记不允许进入分类归纳。
4. **E 轴（递归深度）以作者自己的界定为准**，不得由我们代为拔高或贬低。
5. **"论文声称"与"我们判断"必须显式区分**，用 `【原文】` 与 `【本组判断】` 前缀标注。

---

## 1. 项目定位

### 1.1 课程背景

| 项 | 内容 |
|---|---|
| 课程 | 递归自我改进（Recursive Self-Improvement, RSI）专题 |
| 教师 | 程龚 教授 |
| 助教 | 陈乔晟 |
| 本组方向 | **Harness — 智能体架构、工具与脚手架自进化** |

RSI 的核心定义（课程界定）：**改进后的系统能够继续参与下一轮改进**，从而形成"评估—更新—再评估"的循环。

### 1.2 本方向的核心问题

> 系统能否修改**产生行为**、乃至产生**"下一次改进"**的程序结构？

三个同层次的方向中（模型自进化 / 数据自进化 / **Harness 自进化**），本方向最靠外层——它不改参数、不改数据，改的是**把参数和数据组织起来的那个程序**。

### 1.3 本仓库的交付物

| 课次 | 交付物 | 位置 |
|---|---|---|
| 第一次课 | 泛读卡片 ≥15 篇 | `notes/skim/` |
| 第一次课 | 领域地图 + 选题边界 | 写作仓库 `group/domain-map.md` |
| 第二次课 | 完整 Schema 精读笔记 ≥5 篇 | `notes/deep/` |
| 第二次课 | 方法比较表 + 分类体系 | 写作仓库 `group/` |

> 综述报告为**个人独立撰写**，在写作仓库的 `report/` 或各自本地仓库中完成。

---

## 2. 目录与命名规范

### 2.1 目录结构

```
RSI_Harness_Reading/
├── AGENTS.md              ← 本文件（阅读契约）
├── README.md              ← 项目说明 + 进度看板
├── .gitignore
│
├── midterm/               中期汇报材料（README.md 为索引，按 p1/p2/p3/p4 分目录）
│
├── refs/                  文献元数据（唯一数据源）
│   ├── README.md          ← 字段说明
│   ├── verified.csv       ← 已核验论文（17 篇，venue_verified 全为 false）
│   ├── pool.csv           ← 泛读候选池（表头）
│   ├── refs.bib           ← BibTeX；写作仓库经 sync_refs.py 同步
│   └── pdfs/              ← PDF 缓存（.gitignore 忽略）
│
├── notes/
│   ├── README.md          ← 泛读/精读操作指引
│   ├── TEMPLATE.md        ← 笔记 Schema 唯一副本
│   ├── AXES.md            ← 五轴定义唯一副本
│   ├── skim/              ← 泛读卡片
│   └── deep/              ← 精读笔记
│
└── scripts/
    └── fetch_pdfs.py      ← 按 CSV 批量下载 PDF（零依赖）
```

### 2.2 命名规则

| 对象 | 规则 | 示例 |
|---|---|---|
| 论文主键 ID | `arxiv-<YYMM>.<NNNNN>` | `arxiv-2606.09498` |
| 无 arXiv 的论文 | `venue-<年份>-<短slug>` | `venue-2025-iclr-adas` |
| 笔记文件名 | `<ID>.md` | `notes/deep/arxiv-2505.22954.md` |

**ID 一经分配不可变更。** 即使 venue 后来被核验，ID 也不改——改的是 `venue` 字段。

---

## 3. 两阶段阅读工作流

### 阶段一 · 泛读（第一次课）

**目标**：建立领域地图，划定选题边界。判断标准是"我能不能用两句话说清这篇在做什么"，不是"我记住了多少"。

**读取路径**（每篇 ≤15 分钟）：
1. 标题 + 摘要
2. 引言的贡献列表（Contribution/Bullet）
3. 方法总览图 / 系统框图
4. 实验设置表（只看 benchmark 和主指标）
5. 结论 + 局限

**筛选门槛**（满足 ≥3 条才进 `notes/skim/`）：
- [ ] 直接涉及"修改 agent/harness/scaffold 自身结构"
- [ ] 有明确的自我改进循环或更新算子
- [ ] 有可量化的自我改进效果
- [ ] 2023 年以后
- [ ] 有一定影响力或被多篇工作引用

**产出**：`notes/skim/` 卡片 + 领域地图与选题边界（写作仓库 `group/domain-map.md`）。

---

### 阶段二 · 精读（第二次课）

**目标**：从"这篇做了什么"转向"这篇凭什么算 RSI，以及它的证据链是否站得住"。

**精读必须产出**：
1. 完整的第 4 节 Schema 笔记
2. **方法比较表**：把精读的 5+ 篇放进同一张表，逐列对比（写作仓库 `group/evidence.md`）
3. **分类体系的实证支撑**：每一条分类轴都要有 ≥2 篇论文作为例证（写作仓库 `group/taxonomy.md`）

**阅读顺序建议**：先读方法，再读实验，最后读附录。附录常藏关键的成本核算与消融。

---

## 4. 论文笔记 Schema

**Schema 唯一副本：[`notes/TEMPLATE.md`](notes/TEMPLATE.md)。** 本节只给概览，字段含义与填写要点以 TEMPLATE.md 为准。

`notes/deep/` 下每篇笔记必须使用 TEMPLATE.md 的完整结构。标 🔴 的字段为必填，缺失则该笔记不进入分类归纳。

| 分组 | 字段 | 说明 |
|---|---|---|
| 标识 | 🔴 `id` `title` `authors` `year` `venue` `venue_verified` `industry` `org` | `id` 与文件名、CSV 主键三处一致 |
| 五轴 | 🔴 `axis_a_object` … `axis_e_recursiveness` | 见 [`notes/AXES.md`](notes/AXES.md)；E 轴须引作者原话 |
| 证据 | 🔴 `has_baseline_comparison` `reports_compute_cost` | 设为必填是为了强制回答争议 Q3 |
| 复现 | `reproducible` | `true` / `false` / `unknown` |

正文固定 9 节：一句话贡献 → 问题设定与 harness 定义 → 改进对象与更新算子 →
验证信号与搜索机制 → 实验设置与主要结果 → 局限与作者自述风险 → 本组评注 →
与其他论文的关系 → 待核实项。

两条写作纪律：

- 第 2、6 节必须用 `【原文】` / `【本组判断】` 前缀区分作者说法与我们的判断
- 第 6 节中作者对自身局限的声明（如 STOP 的"这不算完整 RSI"）**原文照抄**，不得转述

字段释义与常见填错见 [`notes/TEMPLATE.md`](notes/TEMPLATE.md)。

---

## 5. 分类体系（五轴，**待验证假设**）

> ⚠️ **五轴是工作假设，不是既有共识。**
> 精读阶段的任务之一就是**用论文推翻或修正它**。
>
> 📄 **完整定义、反例预警与修订记录：[`notes/AXES.md`](notes/AXES.md)**（唯一副本）。
> 本节仅保留速查。

| 轴 | 问题 | 取值 |
|---|---|---|
| **A** 改进对象 | 改的是什么？ | `prompt` / `control-flow` / `code` / `tool` / `memory` / `evaluator` / `context` |
| **B** 改进信号 | 依据从哪来？ | `self-preference` / `external-verifier` / `human` / `failure-trajectory` |
| **C** 搜索算子 | 怎么搜？ | `refine` / `evolutionary` / `textual-gradient` / `tree-search` / `meta-optimizer` |
| **D** 保证强度 | 有什么保证？ | `none` / `empirical` / `formal` / `formal-safety` |
| **E** 递归深度 | 递归到哪一层？ | `one-shot` / `iterative` / `full-rsi` / `co-evolution` |

**判定某轴是否成立**：
- 某轴无法覆盖 **≥80%** 的精读论文 → 该轴有问题
- 某轴需要塞进大量 `other` 才能容纳 → 该轴粒度不对
- 某两轴高度相关（无法独立赋值）→ 考虑合并

**修改分类轴必须留修订记录**（[`notes/AXES.md`](notes/AXES.md) 文末）。

---

## 6. 质量门禁

**提交前逐项自检。任一项不通过则不允许进入下一阶段。**

### Gate 1 · 泛读结束（第一次课）

- [ ] 已读两篇种子综述的摘要、引言、分类图、结论
- [ ] `notes/skim/` 卡片 ≥ 15 篇
- [ ] 领域地图与选题边界已写入写作仓库 `group/domain-map.md`
- [ ] 论文池中每一条的 arXiv ID 都经过核验

### Gate 2 · 精读结束（第二次课）

**硬指标（缺一不可）**：

- [ ] 完整 Schema 精读笔记 **≥5 篇**
- [ ] 其中 **≥1 篇**经典或高质量**同行评审**论文（非 preprint）
- [ ] 其中 **≥1 篇** **2025–2026** 新工作
- [ ] 其中 **≥1 篇工业界**（或产学合作）研究——`industry: true` 且 `org` 非空
      （现有 **10 篇**候选，见 §8.3；口径为"署名含企业机构"，国家实验室不算）
- [ ] 方法比较表完成（所有精读论文在同一张表内对比）
- [ ] 分类体系有 **≥2 篇**论文作为每条轴的例证
- [ ] 每条 `axis_e_recursiveness` 均附**作者原话**佐证

### 证据的独立性检验

> 常见的凑数方式：把 `DGM` 和 `MGM` 当作两条证据。
> 这两篇的作者团队高度重叠、问题设定相近、结论互相支持，**只能算一条证据**。
> 判定标准：**作者重叠 + 问题设定重叠 + 结论重叠 → 同一族，计为一条**。

---

## 7. 引用与核验规则

### 7.1 核验流程

新增任何论文到 `refs/pool.csv` 前，**必须**完成：

1. 在 arXiv / DBLP / OpenReview / Semantic Scholar 中**实际检索到该条目**
2. 记录可点击的 URL
3. venue 一栏按实际状态填写：
   - 仅有 preprint → `arXiv preprint` + `venue_verified: false`
   - 已被录用 → 填会议全称 + `venue_verified: true` + 记录来源 URL

### 7.2 绝对禁止

- ❌ 根据作者/机构的过往发表记录**推断**会议
- ❌ 把 arXiv preprint 标注为会议论文
- ❌ 引用未实际读过的论文来支撑论点
- ❌ 凭记忆填写 arXiv ID

### 7.3 允许但必须标注

- ✅ 引用综述中的引用（但需标注 `via: <综述ID>`，且**不能**作为主要证据）
- ✅ 引用尚未精读的 skim 论文（仅用于背景铺垫，不进 evidence 文件）

### 7.4 BibTeX

统一由 Zotero 管理并导出到 `refs/refs.bib`。手写 BibTeX 字段错误率高，不建议。

> 当前 `refs/refs.bib` 已提供**引导版本**（17 条，由 `verified.csv` 构造）。
> 写作仓库用 `scripts/sync_refs.py` 生成本地快照，不要手改快照。

### 7.5 PDF 获取

```bash
python scripts/fetch_pdfs.py --dry-run      # 只解析来源，不下载
python scripts/fetch_pdfs.py                # 下载 refs/verified.csv 全部
python scripts/fetch_pdfs.py --only arxiv-2505.22954
```

多源回退：arXiv 直连 → Semantic Scholar → OpenAlex。
产出 `refs/pdfs/_manifest.csv`（记录每篇**实际来源 URL** 与 sha1）与 `_missing.csv`（失败清单）。

> ⚠️ PDF 默认**不入版本库**（`.gitignore` 忽略 `*.pdf`）。
> 该脚本**不会**修改 CSV 的 `venue_verified` —— venue 仍需人工按 7.1 核验。

---

## 8. 种子论文池（已核验）

> **核验时间：2026-10-12。** 全部通过 arXiv 实际检索确认存在。
> `venue` 一栏中，标注 ⚠️ 的表示**来自课程 PPT，尚未独立核验录用状态**——入库前请按 7.1 复核。
>
> ✅ **泛读进度（2026-10-13）**：17 篇全部完成泛读卡片，见 `notes/skim/`（17 个 `.md`）。
> 卡片中的作者原话已逐条回查 PDF 核实。
> 泛读同时发现并更正了 3 处元数据错误（STOP 机构、SEVerA 标题、8 篇 `industry` 口径），
> 均已在 `verified.csv` 的 `note` 字段留痕。
> ⚠️ **`axis_*` 五列仍保持泛读前的原样**——泛读判断只写在卡片里且标注"待精读确认"，
> 按 §7.1 纪律，未经精读不填 CSV。
>
> 📄 **机器可读版本：[`refs/verified.csv`](refs/verified.csv)**（17 行）。
> 下表是它的人类可读镜像；**以 CSV 为准**，两者若有冲突改 CSV。
> 所有条目的 `venue_verified` 当前**均为 `false`**。

### 8.1 课程指定的四篇种子

| ID | 标题 | 作者 | 年份 | Venue | 满足指标 |
|---|---|---|---|---|---|
| `arxiv-2310.02304` | Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation | Zelikman, Lorch, Mackey, Kalai | 2023 | ⚠️ COLM 2024 | 经典同行评审 |
| `arxiv-2408.08435` | Automated Design of Agentic Systems | Hu, Lu, Clune | 2024 | ⚠️ ICLR 2025 | 经典同行评审 |
| `arxiv-2504.15228` | A Self-Improving Coding Agent | Robeyns, Szummer, Aitchison | 2025 | ⚠️ 2025 | — |
| `arxiv-2505.22954` | Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents | Zhang, Hu, Lu, Lange, Clune | 2025 | ⚠️ ICLR 2026 | 工业界（Sakana AI） |

### 8.2 直接命中"Harness 自进化"的 2025–2026 工作

| ID | 标题 | 作者 | 年份 | 要点 |
|---|---|---|---|---|
| `arxiv-2606.09498` | Self-Harness: Harnesses That Improve Themselves | Zhang, Zhang, Li, Zhang, Chen, Zhang, Bai, Hu | 2026 | harness 设计是**模型特定**的；上海人工智能实验室（国家实验室，**不算工业界**） |
| `arxiv-2607.15524` | Recursive Harness Self-Improvement | Lee, Xu, Seely, Lee, Zaharia, Tang | 2026 | harness-in-the-loop；Sakana AI / UC Berkeley；自称 recursive 但只完成递归循环前半段 |
| `arxiv-2605.18747` | Code as Agent Harness | Ning, Tieu, Fu, …(52 位作者) | 2026 | 概念统一框架：**代码即 harness**；UIUC / Meta / Stanford；综述立场文，无方法无实验 |
| `arxiv-2608.07645` | Mendel Gödel Machine | Liu, Liu, Yan, Tresp, Ma | 2026 | 用 archive 中**多条轨迹**做比较进化 |
| `arxiv-2606.05922` | Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference (RHO) | Pan, Liu, Lin, … | 2026 | **无需标注验证集**，仅用历史轨迹自监督优化 harness |
| `arxiv-2605.30621` | Harness Updating Is Not Harness Benefit | Lin, Wu, Wang | 2026 | 🔴 **争议核心**：能更新 ≠ 有收益 |
| `arxiv-2603.25111` | SEVerA: Verified Synthesis of Self-Evolving Agents | Banerjee, Xu, Ie, Zhang, Peng, Lin, Singh | 2026 | 给自进化 agent 程序的形式化安全保证 |

### 8.3 工业界 / 应用面

> **口径（2026-10-13 修订）**：`industry: true` = 作者署名中**含企业机构**，
> 按 Gate 2「工业界**或产学合作**」判定。
> **国家实验室与高校联合体不算**（如上海人工智能实验室 → `industry: false`）。

| ID | 标题 | 企业署名 | 年份 | 要点 |
|---|---|---|---|---|
| `arxiv-2506.13131` | AlphaEvolve | **Google DeepMind** | 2025 | 🔴 **工业界首选**；进化式编码 agent；白皮书非同行评审 |
| `arxiv-2505.22954` | Darwin Gödel Machine | **Sakana AI** | 2025 | 工业界 × 学术界；唯一明确宣称"改进自改能力" |
| `arxiv-2607.15524` | Recursive Harness Self-Improvement | **Sakana AI** + UC Berkeley | 2026 | 2026 新工作；`co-evolution` 界定未决 |
| `arxiv-2603.25111` | SEVerA | **Google** + UIUC | 2026 | 唯一提供形式化保证；自陈"保证不覆盖计算成本" |
| `arxiv-2606.05922` | RHO | **Microsoft Research Asia** + CityU HK | 2026 | B 轴 `self-preference` 唯一正面样本 |
| `arxiv-2605.30621` | Harness Updating Is Not Harness Benefit | **Amazon** + Penn State 等 | 2026 | 争议 Q1 核心实证 |
| `arxiv-2310.02304` | STOP | **Microsoft Research** + OpenAI + Stanford | 2023 | 作者声明"不算完整 RSI" |
| `arxiv-2504.15228` | SICA | **iGent AI** + Bristol | 2025 | 首个把 meta agent = target agent 落到完整 codebase |
| `arxiv-2605.18747` | Code as Agent Harness | **Meta** + UIUC + Stanford | 2026 | 概念框架长文，不作证据 |
| `arxiv-2610.00093` | Safety in Self-Evolving Agents | **Alibaba** + **OPPO** + **Rakuten** + ZJU | 2026 | 把编排当**风险载体**而非改进对象 |

> ⚠️ `arxiv-2605.18747`（Meta）与 `arxiv-2610.00093`（Alibaba/OPPO/Rakuten）虽为产学合作，
> 但均为综述、无自我改进效果证据，**不可充当 Gate 2 的工业界实证项**。

### 8.4 综述类（用于建立地图，不作为主要证据）

| ID | 标题 | 年份 |
|---|---|---|
| `arxiv-2607.13104` | Self-Improvements in Modern Agentic Systems: A Survey | 2026 |
| `arxiv-2508.07407` | A Comprehensive Survey of Self-Evolving AI Agents | 2025 |
| `arxiv-2610.00093` | 🔴 Safety in Self-Evolving Agents: A Survey | 2026 |
| `arxiv-2603.25681` | Self-Improvement of Large Language Models: A Technical Overview and Future Outlook | 2026 |
| `arxiv-2607.07663` | Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops | 2026 |

> 课程 PPT 第 8 页推荐的另两篇综述（*A Survey of Self-Evolving Agents*、*Data-Centric Recursive Improvement for Foundation Models*）未给出 arXiv ID，需自行检索后补入。

### 8.5 论文池扩充方向

- 提示 / 系统提示自优化（OPRO、Self-Refine 谱系）
- 工具自创建与自选择（tool creation / tool pruning）
- 记忆与技能库自进化（Voyager 谱系）
- 多智能体拓扑搜索（AFlow、GPTSwarm 系）
- LLM 驱动的进化搜索（EvoPrompt 系）
- 自进化 agent 的安全与对齐

---

## 9. AI 助手行为红线

给在本仓库中工作的 AI 助手的强制约束：

1. **绝不生成未核验的文献条目。** 如果不确定某 arXiv ID 是否存在，**说不确定**，而不是编一个。
2. **绝不填补 venue。** 不知道就写 `arXiv preprint` + `venue_verified: false`。
3. **区分引用与检索。** 只有实际调用检索工具获得的结果，才能写入笔记；凭记忆写的一律标注 `⚠️ 未核验`。
4. **不替作者下结论。** 关于"这算不算 RSI"，必须先找作者原话；找不到就记入"待核实项"。
5. **不扩大样本。** 要求精读 5 篇时不要顺手写 15 篇深度分析——那会让精读流于形式。
6. **发现与本文件冲突时，提出建议而非擅自修改。** 修改分类轴必须留修订记录。
7. **中文写作，术语保留英文原词**（harness、scaffold、trajectory、archive 等不做硬译，避免歧义）。

---

## 附录 · 快速命令

```bash
# 检索 arXiv（本项目 MCP 工具示例）
search_arxiv("harness self-improvement agent", max_results=10)

# 核验某条 arXiv ID 是否存在
search_arxiv("Darwin Godel Machine", max_results=1)

# 查看某篇的完整信息
search_arxiv("Self-Harness", max_results=1)
```

**检索渠道速查**：
- arXiv：https://arxiv.org/
- Semantic Scholar：https://www.semanticscholar.org/
- DBLP：https://dblp.org/ （**venue 核验首选**）
- OpenReview：https://openreview.net/ （**ICLR/NeurIPS 录用状态核验首选**）
- Google Scholar：https://scholar.google.com/
- Connected Papers：https://www.connectedpapers.com/

---

*最后更新：2026-10-30*
