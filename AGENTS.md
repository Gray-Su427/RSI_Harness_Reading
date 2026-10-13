# AGENTS.md — Harness 自进化综述项目操作规程

> 本文件是本项目对**人类组员**与**AI 助手**共同生效的工作契约。
> 任何在本目录下的写入操作，必须遵守本文件。规则与课程要求冲突时，以课程要求为准，并立即修订本文件。

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

### 1.3 考核硬指标（来自课程 PPT 第 12–13 页）

| 课次 | 交付物 | 硬性指标 |
|---|---|---|
| 第一次 | 泛读调研 | 领域地图 + 选题边界 |
| 第二次 | 精读分类 | **≥5 篇**核心论文；其中 **≥1 篇**经典/高质量同行评审、**≥1 篇** 2025–2026 新工作、**≥1 篇**工业界（或产学合作）；形成分类体系 |
| 第三次 | 汇总与展示 | PPT 草稿 + 综述摘要：**1 句**核心结论 + **1 个**分类体系 + **≥3 条**主要证据（每条附 **≥2 篇**参考文献）+ **2–3 个**争议结论/开放问题 |
| 汇报 | 口头 | **10 分钟**报告 + **5 分钟**提问 |
| 寒假 | 综述报告 | **个人独立**撰写 |

> ⚠️ 综述报告为个人独立撰写。本目录的产出是**共享的调研素材与方法论**，不是报告成稿。

---

## 2. 目录与命名规范

### 2.1 目录结构

```
RSI_Harness_Review/
├── AGENTS.md              ← 本文件（工作契约）
├── README.md              ← 项目说明 + 进度看板 + 1 句核心结论
├── .gitignore
│
├── refs/                  文献元数据（唯一数据源）
│   ├── README.md          ← 字段说明
│   ├── verified.csv       ← 已核验论文（17 篇，venue_verified 全为 false）
│   ├── pool.csv           ← 泛读候选池（表头）
│   └── refs.bib           ← BibTeX；LaTeX 经 \bibliography{../refs/refs} 引用
│
├── notes/
│   ├── README.md          ← 泛读/精读操作指引
│   ├── TEMPLATE.md        ← 笔记 Schema 唯一副本
│   ├── skim/              ← 泛读卡片
│   └── deep/              ← 精读笔记
│
├── synthesis/             综合产出
│   ├── taxonomy.md        ← 分类体系（五轴，含修订记录）
│   ├── evidence.md        ← 证据链
│   └── open-questions.md  ← 争议/开放问题
│
├── slides/                汇报 PPT 大纲
│
├── scripts/
│   └── fetch_pdfs.py      ← 按 CSV 批量下载 PDF（零依赖）
│
└── report/                LaTeX 综述报告骨架（英文，article + natbib）
    ├── main.tex  preamble.tex  Makefile  build.bat
    ├── sections/          00-abstract … 06-conclusion
    └── tables/            comparison.tex
```

> 综述报告为**个人独立撰写**。`report/` 只是共享骨架，不是成稿。

### 2.2 命名规则

| 对象 | 规则 | 示例 |
|---|---|---|
| 论文主键 ID | `arxiv-<YYMM>.<NNNNN>` | `arxiv-2606.09498` |
| 无 arXiv 的论文 | `venue-<年份>-<短slug>` | `venue-2025-iclr-adas` |
| 笔记文件名 | `<ID>.md` | `notes/deep/arxiv-2505.22954.md` |
| 证据条目 | `E1` / `E2` / `E3` | |
| 争议条目 | `Q1` / `Q2` / `Q3` | |

**ID 一经分配不可变更。** 即使 venue 后来被核验，ID 也不改——改的是 `venue` 字段。

---

## 3. 三阶段工作流

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

**产出**：`notes/skim/` 卡片 + `README.md` 中的领域地图雏形。

---

### 阶段二 · 精读（第二次课）

**目标**：从"这篇做了什么"转向"这篇凭什么算 RSI，以及它的证据链是否站得住"。

**精读必须产出**：
1. 完整的第 4 节 Schema 笔记
2. **方法比较表**：把精读的 5+ 篇放进同一张表，逐列对比
3. **分类体系的实证支撑**：每一条分类轴都要有 ≥2 篇论文作为例证

**阅读顺序建议**：先读方法，再读实验，最后读附录。附录常藏关键的成本核算与消融。

---

### 阶段三 · 汇总（第三次课）

**目标**：把文献列表变成论证。

**产出物构建顺序**（不要跳步）：
1. 先写 `open-questions.md`（争议）→ 因为争议决定了综述的立场
2. 再写 `evidence.md`（证据链）→ 每条证据必须能独立站住
3. 再写 `taxonomy.md` → 用证据反推分类轴，而不是先定轴再填人
4. 最后写 `README.md` 的 1 句核心结论 → 它必须被上面三份文件同时支撑

---

## 4. 论文笔记 Schema

**Schema 唯一副本：[`notes/TEMPLATE.md`](notes/TEMPLATE.md)。** 本节只给概览，字段含义与填写要点以 TEMPLATE.md 为准。

`notes/deep/` 下每篇笔记必须使用 TEMPLATE.md 的完整结构。标 🔴 的字段为必填，缺失则该笔记不进入分类归纳。

| 分组 | 字段 | 说明 |
|---|---|---|
| 标识 | 🔴 `id` `title` `authors` `year` `venue` `venue_verified` `industry` `org` | `id` 与文件名、CSV 主键三处一致 |
| 五轴 | 🔴 `axis_a_object` … `axis_e_recursiveness` | 见第 5 节；E 轴须引作者原话 |
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

## 5. 分类体系（**待验证假设，尚未定稿**）

> ⚠️ **以下五轴是我们的工作假设，不是既有共识。**
> 精读阶段的任务之一就是**用论文推翻或修正它**。如果某轴无法覆盖 ≥80% 的论文，或需要大量 `other` 才能塞下，就该改轴。
> 每次修改请在文末的"修订记录"中留痕。
>
> 📄 **完整定义、分类总表与修订记录：[`synthesis/taxonomy.md`](synthesis/taxonomy.md)**（唯一副本）。
> 本节仅保留速查；两者若有冲突，以 `synthesis/taxonomy.md` 为准。

### 轴 A · 改进对象（改的是什么）

| 值 | 含义 | 典型代表 |
|---|---|---|
| `prompt` | 系统提示 / 指令模板 | Self-Refine, OPRO 系 |
| `control-flow` | 控制流、agent 拓扑、多智能体编排 | ADAS, AFlow |
| `code` | agent 自身的源代码本体 | STOP, SICA, DGM, MGM |
| `tool` | 工具的定义、新增、剪枝 | 工具创建 / 工具选择类 |
| `memory` | 记忆、技能库、长期档案 | Voyager, 结构化记忆类 |
| `evaluator` | 评测器 / 验证器本身 | DGM 的经验验证器 |
| `context` | 上下文组织与轨迹生成策略 | harness-in-the-loop 类 |

> 🔍 **反例预警**：一篇论文可能同时命中多值（如 DGM 同时改 `code` 与 `evaluator`）。
> 规则：**取该工作的主要贡献所对应的值**为必填，其余以次要值追加，用列表形式保存。
> 不要为了"纯粹"而强行归入单值——归类冲突本身就是分类体系的诊断信号，记入第 9 节"待核实项"。

### 轴 B · 改进信号（改进的依据从哪来）

| 值 | 含义 | 风险 |
|---|---|---|
| `self-preference` | 系统自评 / 自偏好，无外部真值 | 循环论证风险最高 |
| `external-verifier` | 可执行验证：单元测试、benchmark 分数 | 需检查验证集是否泄漏 |
| `human` | 人类反馈 | 难以规模化，与 RSI 的自举特性有张力 |
| `failure-trajectory` | 从失败轨迹中提取改进 | 依赖失败的选择偏差 |

### 轴 C · 搜索算子（怎么搜）

| 值 | 含义 |
|---|---|
| `refine` | 迭代精修（逐轮改写，无种群） |
| `evolutionary` | 进化搜索 / 遗传算法 / 种群 + 选择 |
| `textual-gradient` | 文本梯度（自然语言反馈作为"梯度"） |
| `tree-search` | 树搜索 / 分支探索 |
| `meta-optimizer` | 元学习得到的优化器 |

### 轴 D · 保证强度

| 值 | 含义 |
|---|---|
| `none` | 无保证，纯经验报告 |
| `empirical` | 有经验性筛选（只保留分数提升的变体） |
| `formal` | 有形式化/可验证保证 |
| `formal-safety` | 有显式安全约束与证明 |

### 轴 E · 递归深度（**本方向最关键的轴**）

这一轴直接对应 RSI 的定义，必须逐篇引用作者的自我界定。

| 值 | 含义 |
|---|---|
| `one-shot` | 单次改进，改进产物不参与下一轮 |
| `iterative` | 改进后的系统参与下一轮改进 |
| `full-rsi` | 改进的不只是产物，**改进器本身也被改进** |
| `co-evolution` | harness 与模型互为对方的数据生成源 |

> 🔍 **反例预警（必须记入笔记）**：
> - **STOP** 的作者**自己声明**"由于语言模型未被改变，这不属于完整的递归自我改进"。
>   → 我们必须照抄这个限定，**不得**因为它常被后人归入 RSI 就拔高。
> - **DGM** 明确宣称它改进了"改进自身代码库的能力" → 属 `full-rsi`。
> - `co-evolution` 是 2026 年新出现的表述（如 harness-in-the-loop），需确认它是否只是 `iterative` 的重新包装。

### 修订记录

| 日期 | 改动 | 原因 |
|---|---|---|
| 2026-10-12 | 建立五轴初稿 | 立项 |

---

## 6. 质量门禁

**提交前逐项自检。任一项不通过则不允许进入下一阶段。**

### Gate 1 · 泛读结束（第一次课）

- [ ] 已读两篇种子综述的摘要、引言、分类图、结论
- [ ] `notes/skim/` 卡片 ≥ 15 篇
- [ ] `README.md` 中已写出领域地图与选题边界
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

### Gate 3 · 汇总结束（第三次课）

- [ ] `README.md` 写出了**1 句**核心结论（不是一段）
- [ ] `taxonomy.md` 分类体系可用**一张图**讲清（若需要多张，说明还没想清楚）
- [ ] `evidence.md` 有 **≥3 条**证据
- [ ] 每条证据附 **≥2 篇**参考文献，且两篇**互相独立**（不能是同一团队连续工作）
- [ ] `open-questions.md` 有 **2–3 个**争议/开放问题
- [ ] 每个争议都有支撑文献，且能回答"如果我错了会怎样"
- [ ] PPT 草稿控制在 **10 分钟**内（建议 12–15 页）

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
- ✅ 引用尚未精读的 skim 论文（仅用于背景铺垫，不进 evidence.md）

### 7.4 BibTeX

统一由 Zotero 管理并导出到 `refs/refs.bib`。手写 BibTeX 字段错误率高，不建议。

> 当前 `refs/refs.bib` 已提供**引导版本**（17 条，由 `verified.csv` 构造），
> 目的是让 `report/` 能立即编译。文件头部有醒目注释说明核验后需同步更新。

### 7.5 PDF 获取

```bash
python scripts/fetch_pdfs.py --dry-run      # 只解析来源，不下载
python scripts/fetch_pdfs.py                # 下载 refs/verified.csv 全部
python scripts/fetch_pdfs.py --only arxiv-2505.22954
```

多源回退：arXiv 直连 → Semantic Scholar → OpenAlex。
产出 `_manifest.csv`（记录每篇**实际来源 URL** 与 sha1）与 `_missing.csv`（失败清单）。

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

> 这一组是本选题的核心弹药，2026 年该子方向已形成规模。

| ID | 标题 | 作者 | 年份 | 要点 |
|---|---|---|---|---|
| `arxiv-2606.09498` | Self-Harness: Harnesses That Improve Themselves | Zhang, Zhang, Li, Zhang, Chen, Zhang, Bai, Hu | 2026 | 提出 harness 设计是**模型特定**的；机构为上海人工智能实验室（国家实验室，**不算工业界**） |
| `arxiv-2607.15524` | Recursive Harness Self-Improvement | Lee, Xu, Seely, Lee, Zaharia, Tang | 2026 | harness-in-the-loop；机构为 **Sakana AI** / UC Berkeley（非 Spark，已据 PDF 更正）；自称 recursive 但只完成递归循环前半段 |
| `arxiv-2605.18747` | Code as Agent Harness | Ning, Tieu, Fu, …(52 位作者，已据 PDF 更正) | 2026 | 概念统一框架：**代码即 harness**；UIUC / Meta / Stanford；**综述立场文，无方法无实验** |
| `arxiv-2608.07645` | Mendel Gödel Machine | Liu, Liu, Yan, Tresp, Ma | 2026 | 用 archive 中**多条轨迹**做比较进化，改进单轨迹突变 |
| `arxiv-2606.05922` | Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference (RHO) | Pan, Liu, Lin, … | 2026 | **无需标注验证集**，仅用历史轨迹自监督优化 harness |
| `arxiv-2605.30621` | Harness Updating Is Not Harness Benefit | Lin, Wu, Wang | 2026 | 🔴 **争议核心**：能更新 ≠ 有收益 |
| `arxiv-2603.25111` | SEVerA: Verified Synthesis of Self-Evolving Agents | Banerjee, Xu, Ie, Zhang, Peng, Lin, Singh | 2026 | 给自进化 agent 程序的形式化安全保证 |

### 8.3 工业界 / 应用面

> **口径（2026-10-13 修订）**：`industry: true` = 作者署名中**含企业机构**，
> 按 Gate 2「工业界**或产学合作**」判定。
> **国家实验室与高校联合体不算**（如上海人工智能实验室 → `industry: false`）。
> 全部 17 篇的署名机构已逐篇核对 PDF 首页，下表即审计结果。

| ID | 标题 | 企业署名 | 年份 | 要点 |
|---|---|---|---|---|
| `arxiv-2506.13131` | AlphaEvolve: A coding agent for scientific and algorithmic discovery | **Google DeepMind** | 2025 | 🔴 **工业界首选**；进化式编码 agent，优化数据中心调度与数学问题；白皮书非同行评审 |
| `arxiv-2505.22954` | Darwin Gödel Machine | **Sakana AI** | 2025 | 工业界 × 学术界（UBC / Vector）；唯一明确宣称"改进自改能力"的工作 |
| `arxiv-2607.15524` | Recursive Harness Self-Improvement | **Sakana AI** + UC Berkeley | 2026 | 2026 新工作；自称 recursive 但只完成递归循环前半段，`co-evolution` 界定未决 |
| `arxiv-2603.25111` | SEVerA: Verified Self-Evolving Agents | **Google** + UIUC | 2026 | 唯一提供形式化保证的工作；自陈"保证不覆盖计算成本" |
| `arxiv-2606.05922` | Evolving Agents in the Dark (RHO) | **Microsoft Research Asia** + CityU HK | 2026 | B 轴 `self-preference` 唯一正面样本；Q2 必读 |
| `arxiv-2605.30621` | Harness Updating Is Not Harness Benefit | **Amazon** + Penn State 等 | 2026 | 争议 Q1 核心实证；把"能更新"与"有收益"分开测量 |
| `arxiv-2310.02304` | STOP | **Microsoft Research** + OpenAI + Stanford | 2023 | 作者亲手声明"不算完整 RSI"，E 轴反例原始出处 |
| `arxiv-2504.15228` | A Self-Improving Coding Agent (SICA) | **iGent AI** + Bristol | 2025 | 首个把 meta agent = target agent 落到完整 codebase |
| `arxiv-2605.18747` | Code as Agent Harness | **Meta** + UIUC + Stanford | 2026 | 概念框架长文，无方法无实验，不作证据 |
| `arxiv-2610.00093` | Safety in Self-Evolving Agents | **Alibaba** + **OPPO** + **Rakuten** + ZJU | 2026 | Q4 的引用来源；把编排当**风险载体**而非改进对象 |

> ⚠️ 其中 `arxiv-2605.18747`（Meta）与 `arxiv-2610.00093`（Alibaba/OPPO/Rakuten）虽为产学合作，
> 但均为综述、无自我改进效果证据，**不可充当 Gate 2 的工业界实证项**。
> Gate 2 的工业界硬指标有 8 个可用的方法论文候选，且**不再依赖 venue 尚未核验的 DGM**。

### 8.4 综述类（用于建立地图，不作为主要证据）

| ID | 标题 | 年份 |
|---|---|---|
| `arxiv-2607.13104` | Self-Improvements in Modern Agentic Systems: A Survey | 2026 |
| `arxiv-2508.07407` | A Comprehensive Survey of Self-Evolving AI Agents | 2025 |
| `arxiv-2610.00093` | 🔴 Safety in Self-Evolving Agents: A Survey | 2026 |
| `arxiv-2603.25681` | Self-Improvement of Large Language Models: A Technical Overview and Future Outlook | 2026 |
| `arxiv-2607.07663` | Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops | 2026 |

> 课程 PPT 第 8 页推荐的另两篇综述（*A Survey of Self-Evolving Agents*、*Data-Centric Recursive Improvement for Foundation Models*）未给出 arXiv ID，需自行检索后补入。

### 8.5 论文池扩充方向（本轮未做，留待后续）

以下方向尚未系统检索，建议下一轮补齐：

- 提示 / 系统提示自优化（OPRO、Self-Refine 谱系）
- 工具自创建与自选择（tool creation / tool pruning）
- 记忆与技能库自进化（Voyager 谱系）
- 多智能体拓扑搜索（AFlow、GPTSwarm 系）
- LLM 驱动的进化搜索（EvoPrompt 系）
- 自进化 agent 的安全与对齐

---

## 9. 争议与开放问题池（初步）

> 课程要求 2–3 个。此处为**候选**，第三次课前需收敛到 2–3 个并给出证据。
>
> 📄 **完整条目、收敛指引与取舍逻辑：[`synthesis/open-questions.md`](synthesis/open-questions.md)**（唯一副本）。
> 下面的摘要仅供快速查阅。

### Q1 · 测量效度：自我改进的增益是真的吗？

**支撑**：`arxiv-2605.30621`（Harness Updating Is Not Harness Benefit）明确提出"harness 更新"与"harness 收益"应当解耦。
**质疑路径**：多试几次总会挑出更好的那个——增益是否来自**选择偏差**？harness 是否在验证集上过拟合？
**如果我错了会怎样**：若增益可复现，则整个领域的核心叙事成立，本综述的价值在于方法分类。

### Q2 · 验证器的循环论证

**问题**：harness 既生成改进、又验证改进。**验证信号是否独立于被优化对象？**
**相关轴**：B 轴的 `self-preference` 与 `external-verifier` 之别。
**支撑**：RHO（`arxiv-2606.05922`）用自偏好替代真值验证，等于承认外部验证在部署中不可得——那么它引入的是自治还是循环论证？
**可检验方式**：查证是否有工作做了"用独立评测器复评自评结果"的实验。

### Q3 · 成本核算缺失

**问题**：报告的自我改进增益，**是否扣除了搜索算力**？
**可检验方式**：逐篇检查 `reports_compute_cost` 字段（Schema 中已设为必填）。同算力下的强基线——简单提示搜索、暴力采样、随机架构采样——能否追平？

### Q4 · 可控性与爆炸半径

**支撑**：`arxiv-2610.00093`（Safety in Self-Evolving Agents）指出，一旦经验沉淀为可复用状态（工具定义、技能、工作流），过去的事件就成为未来的原因。
**张力**：SEVerA（`arxiv-2603.25111`）的形式化保证 vs. 多数工作的经验性筛选——保证的代价是什么，收益是什么？

### Q5 · 可复现性

本方向工作普遍**不公开** harness 完整代码与 evolution archive。这使得跨论文比较面临"我们的 harness 和你的 harness 是否可比"的根本问题。

---

## 10. AI 助手行为红线

给在本目录中工作的 AI 助手的强制约束：

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

*最后更新：2026-10-13*
