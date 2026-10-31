# P1 · 四篇 seed 的 venue 核验结论

> 负责人：P1（xyc）｜核验日期：**2026-10-31**｜状态：**CP1 证据文件**
> 口径依据：[`../../AGENTS.md`](../../AGENTS.md) §7.1；结论同步写入 [`../../refs/verified.csv`](../../refs/verified.csv) 的 `venue` / `venue_verified` / `note` 三列。

## 0. 核验方法与一处限制

- **优先级**：会议官网 / 会议论文集 > OpenReview > DBLP。
- ⚠️ **DBLP 本次不可用**：`dblp.org`、`dblp.uni-trier.de`、`dblp.dagstuhl.de` 三个入口均返回 Anubis 人机验证页（HTTP 202），脚本与浏览器均无法取回条目。**因此本轮没有一条 DBLP 证据**，改用「会议官方 accepted papers 页」与「会议官方论文集（proceedings.iclr.cc）」——这两类均属 §7.1 认可的核验渠道，且比 DBLP 更接近一手。
- **OpenReview 直连同样被人机验证拦截**（forum/pdf 均跳转 `/challenge`）；仅在能读到 OpenReview 页面元数据（如 arXiv HTML 首页标注的 forum id）时作为辅助证据，不单独作为 `true` 的依据。
- 判定为 `true` 的最低要求：**在会议官方页面/论文集中看到标题与作者同时匹配**。

## 1. 结论总表

| ID | 论文 | PPT 声称 | 核验结论 | `venue_verified` |
|---|---|---|---|---|
| `arxiv-2310.02304` | STOP | COLM 2024 | **COLM 2024（Spotlight）** | ✅ `true` |
| `arxiv-2408.08435` | ADAS | ICLR 2025 | **ICLR 2025（Conference）** | ✅ `true` |
| `arxiv-2505.22954` | DGM | ICLR 2026 | **ICLR 2026（Conference）** | ✅ `true` |
| `arxiv-2504.15228` | SICA | 未标 | **arXiv preprint**（仅自述投稿 NeurIPS 2025） | ❌ `false` |

> 另：本轮补入的两篇种子综述中，`arxiv-2507.21046` 核为 **TMLR 2026**（`venue_verified: true`），
> `venue-2026-dcri-survey` 为 Preprints.org 预印本（`false`）。详见 §3。

## 2. 逐篇证据

### 2.1 STOP → COLM 2024（Spotlight）

- **来源**：[COLM 2024 Accepted Papers](https://colmweb.org/2024/AcceptedPapers.html)（访问 2026-10-31）
- **页面原文**（列表项）：

> 🔦 Spotlight [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://openreview.net/forum?id=46Zgqo4QIU)
> _Eric Zelikman, Eliana Lorch, Lester Mackey, Adam Tauman Kalai_

- **旁证**：arXiv `2310.02304` 的 comments 字段为 “Published as a conference paper at COLM 2024”。
- **判定**：标题、四位作者、Spotlight 标记三者同时匹配 → `venue: COLM 2024`，`venue_verified: true`。
- **口径提示**：COLM 2024 的官方列表把全部 accepted papers 托管在 OpenReview，故 forum 链接是官方入口，不是二手来源。

### 2.2 ADAS → ICLR 2025（Conference）

- **来源**：[ICLR 2025 论文集条目](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36b7acf6f6010652b3f2a433774a66fe-Abstract-Conference.html)（访问 2026-10-31）
- **页面原文**：

> **Automated Design of Agentic Systems**
> Shengran Hu, Cong Lu, Jeff Clune
> International Conference on Learning Representations 2025 (ICLR 2025) — Conference

- **判定**：标题与三位作者完全匹配，且被标为 Conference 轨（非 Workshop）→ `venue: ICLR 2025`，`venue_verified: true`。
- **附带信息**：该条有正式 PDF（`...-Paper-Conference.pdf`），可作为精读的**版本基准**——精读时应以 ICLR 2025 版而非 arXiv v1 为准。

### 2.3 DGM → ICLR 2026（Conference）

- **来源**：[ICLR 2026 论文集条目](https://proceedings.iclr.cc/paper_files/paper/2026/hash/aa5f5e6eb6f613ec412f1d948dfa21a5-Abstract-Conference.html)（访问 2026-10-31）
- **页面原文**：

> **Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents**
> Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune
> International Conference on Learning Representations 2026 (ICLR 2026) — Conference

- **判定**：五人作者全匹配 → `venue: ICLR 2026`，`venue_verified: true`。
- ⚠️ **两条须同时写入记录的口径**：
  1. **年份**：`year = 2025` 指 arXiv 首发年（2025-05-29）；ICLR 2026 是**发表会议**，不是论文年份。按 P4 计划 §2.3「不把 DGM 的会议年份当作论文年份」，CSV 的 `year` 保持 2025。
  2. **指标归属**：DGM 同时被用来占「工业界」与「2025–2026 新工作」两项硬指标，但它与 MGM（`arxiv-2608.07645`）属同一研究谱系，**只能算一条证据**（见 `AGENTS.md` §6「证据的独立性检验」）。
- 版本提示：arXiv 已到 v3（2026-03-12），与 ICLR 2026 正式版可能存在差异；精读时以论文集 PDF 为准并记录版本。

### 2.4 SICA → 仍是 preprint（PPT 未标 venue，核验后维持 `false`）

- **arXiv `2504.15228` comments 字段**（原文）：

> Submitted as a preprint to NeurIPS 2025

- **OpenReview 检索**：`NeurIPS.cc/2025/Conference` 分会以 “Self-Improving Coding Agent” 检索返回 0 条。
- **第三方标注**：ResearchGate 该条标注为 “Preprints and early-stage research may not have been peer reviewed yet”。
- **判定**：**没有录用证据**。「投稿」不等于「录用」，且 arXiv 注释本身用词是 submitted → `venue: arXiv preprint`，`venue_verified: false`。
- **影响**：SICA 不能用于 Gate 2 的「同行评审」项；该项由 STOP（COLM 2024）/ ADAS（ICLR 2025）覆盖。

## 3. 两篇种子综述的 venue

| ID | venue | 证据 | `venue_verified` |
|---|---|---|---|
| `arxiv-2507.21046` | **TMLR 2026** | ① arXiv HTML 首页标注 “Reviewed on OpenReview: forum?id=CTr3bovS5F”；② [ML Anthology TMLR 2026 索引](https://mlanthology.org/tmlr/2026/gao2026tmlr-survey/) 收录，作者列表一致；③ arXiv comments 写 “Transactions on Machine Learning Research (01/2026)” | ✅ `true`（三级互证，但 OpenReview forum 页未能人工打开） |
| `venue-2026-dcri-survey` | **Preprints (Preprints.org)** | Preprints.org 记录 DOI `10.20944/preprints202609.0154`；companion repo 的 BibTeX 为 `@article{202609.0154, journal={Preprints}}`；arXiv 无此条（题名检索 0 命中） | ❌ `false`（预印本服务器，非同行评审） |

## 4. 对 CP1 通过标准的回应

| CP1 标准 | 本轮结果 |
|---|---|
| 2 篇种子综述入库 | ✅ 已入 `refs/pool.csv` 与 `refs/verified.csv`（19 条） |
| 4 篇 seed venue 有结论 | ✅ 3 篇 `true` + 1 篇 `false`，证据可点击 |
| 19 篇统计与 CSV 一致 | ✅ 见 [`stats.md`](stats.md)，由脚本对 CSV 直接计数 |
| 漏斗数字对得上 | ✅ 见 [`funnel.md`](funnel.md) |

## 5. 未闭环项（移交）

1. **DBLP 复核**：待网络环境允许时，用 DBLP 对上述 4 条做二次确认（尤其 COLM 2024 的 DBLP 条目名）。
2. **OPENREVIEW 直连**：TMLR 2026 的 forum 页未能人工打开，若 CP4 需要「链接全部通过」，请把该链接标为「受浏览器验证限制」而非「404」。
3. **2603.25681（TMLR 自述）**：作者称 “Accepted by TMLR and awarded the Survey Certification”，本组未取得索引证据，**保持 `venue_verified: false`**，交付 P3 决定对外材料是否提及。
4. **RHO（EMNLP 2026 Findings 自述）**：同上，保持 `false`；若 11 月 ACL Anthology 出条目，由 P1 回填。
5. **PDF 抓取**：`python scripts/fetch_pdfs.py --dry-run` 实测「成功 18 / 失败 1」——失败的是
   `venue-2026-dcri-survey`（无 arXiv ID，脚本三路解析均不支持）。这是预期行为，PDF 需手动下载，
   已写入 [`../../refs/README.md`](../../refs/README.md)。若要自动化，需给脚本加「CSV 直连 PDF URL」分支，属 P1 后续可选项。
