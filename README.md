# Review of Recursive Self-Improvement: Harness — Reading

RSI 专题课程 · 小组综述项目 · 方向：**Harness 自进化**

> 本仓库只负责**论文链接与阅读笔记**，通过 GitHub 做远程共享。
> 综述写作、分类论证、PPT 与 LaTeX 报告在本地写作仓库 `../RSI_Harness_Writing/`，
> 不在本仓库中。

---

## 1. 方向定位

递归自我改进（RSI）的核心定义：改进后的系统能够继续参与下一轮改进，形成"评估—更新—再评估"的循环。

RSI 研究通常分三个层次：

| 层次 | 改什么 | 是否属于本组 |
|---|---|---|
| Model | 模型参数与训练过程 | ✗ |
| Data | 数据、经验及其生产管线 | ✗ |
| **Harness** | **智能体架构、工具与脚手架** | ✅ **本组** |

**本方向的核心问题**：系统能否修改产生行为、乃至产生"下一次改进"的那个程序结构？

三个层次中 Harness 最靠外层——它不改参数、不改数据，改的是把参数和数据组织起来的那个程序。

---

## 2. 这个仓库放什么

| 目录 / 文件 | 内容 |
|---|---|
| `refs/verified.csv` | 已核验论文的元数据（唯一数据源） |
| `refs/pool.csv` | 泛读候选池 |
| `refs/refs.bib` | BibTeX 库，供写作仓库引用 |
| `refs/pdfs/` | 论文 PDF 缓存（不入版本库） |
| `notes/TEMPLATE.md` | 精读笔记 Schema |
| `notes/AXES.md` | 五轴分类定义（笔记字段的唯一依据） |
| `notes/skim/` | 泛读卡片 |
| `notes/deep/` | 精读笔记 |
| `scripts/fetch_pdfs.py` | 按 CSV 批量下载 PDF |

**不放**：分类结果论证、证据链、开放问题、PPT、LaTeX 报告。这些在写作仓库。

---

## 3. 进度看板

| 阶段 | 交付物 | 状态 | 位置 |
|---|---|---|---|
| 第一次课 | 泛读卡片 ≥15 篇 | ✅ 17 篇 | `notes/skim/` |
| 第一次课 | 两篇种子综述 | ⬜ 未补 | 需自行检索 arXiv ID |
| 第一次课 | 领域地图 + 选题边界 | ⬜ 未开始 | 写作仓库 `group/domain-map.md` |
| 第二次课 | 精读笔记 ≥5 篇 | ⬜ 0 篇 | `notes/deep/` |
| 第二次课 | 方法比较表 | ⬜ 未开始 | 写作仓库 `group/evidence.md` |
| 第二次课 | 分类体系 | ⬜ 初稿 | 写作仓库 `group/taxonomy.md` |
| 全程 | venue 核验 | ⬜ 0/17 | `refs/verified.csv` |

### 硬指标自检（第二次课）

- [ ] 完整 Schema 精读笔记 ≥ **5** 篇
- [ ] 其中 ≥ **1** 篇经典 / 高质量同行评审
- [ ] 其中 ≥ **1** 篇 **2025–2026** 新工作
- [ ] 其中 ≥ **1** 篇工业界（或产学合作）
- [ ] 方法比较表完成
- [ ] 分类体系每条轴有 ≥ **2** 篇例证
- [ ] 每条 `axis_e_recursiveness` 附**作者原话**

详细规则见 [`AGENTS.md`](AGENTS.md) 第 6 节。

### 当前精读候选

| ID | 论文 | 角色 | 状态 |
|---|---|---|---|
| `arxiv-2310.02304` | STOP | 经典 / 工业界 | skim |
| `arxiv-2408.08435` | ADAS | 经典 / 控制流 | skim |
| `arxiv-2505.22954` | DGM | 工业界 / full-rsi | skim |
| `arxiv-2506.13131` | AlphaEvolve | 工业界 / 进化搜索 | skim |
| `arxiv-2606.05922` | RHO | 2026 / self-preference | skim |
| `arxiv-2603.25111` | SEVerA | 2026 / formal-safety | skim |
| `arxiv-2605.30621` | Harness Updating Is Not Harness Benefit | 2026 / 争议 Q1 | skim |

> 全部 17 篇的状态以 [`refs/verified.csv`](refs/verified.csv) 的 `read_status` 为准。

---

## 4. 目录导航

```
.
├── AGENTS.md          🔴 工作契约：阅读流程、Schema、质量门禁、AI 红线
├── README.md          ← 你在这里
├── .gitignore
│
├── refs/              文献元数据
│   ├── verified.csv   已核验论文（17 篇）
│   ├── pool.csv       泛读候选池
│   ├── refs.bib       BibTeX
│   └── pdfs/          PDF 缓存（不入库）
│
├── notes/             笔记
│   ├── TEMPLATE.md    精读 Schema 模板
│   ├── AXES.md        五轴定义
│   ├── skim/          泛读卡片
│   └── deep/          精读笔记
│
└── scripts/
    └── fetch_pdfs.py  按 CSV 批量下载论文 PDF
```

---

## 5. 快速上手

```bash
# 1. 下载已核验论文的 PDF（先 dry-run 看解析结果）
python scripts/fetch_pdfs.py --dry-run
python scripts/fetch_pdfs.py

# 2. 泛读：按 notes/README.md 的 5 步路径读，在 notes/skim/ 建卡片

# 3. 精读：复制 notes/TEMPLATE.md 到 notes/deep/<id>.md
```

写作仓库（本地）的编译与写作流程见 `../RSI_Harness_Writing/README.md`。

### 检索渠道

| 用途 | 渠道 |
|---|---|
| venue / 录用状态核验 | [DBLP](https://dblp.org/) · [OpenReview](https://openreview.net/) |
| 文献检索 | [arXiv](https://arxiv.org/) · [Semantic Scholar](https://www.semanticscholar.org/) |
| 引用图谱 | [Google Scholar](https://scholar.google.com/) · [Connected Papers](https://www.connectedpapers.com/) |

---

## 6. 三条最重要的规矩

1. **入库前必须核验 arXiv ID 真实存在。** 幻觉出来的文献比没有文献更有害。
2. **未核验的 venue 一律标 `venue_verified: false`。** 当前 17 篇全部为 `false`。
3. **"论文声称"与"我们判断"必须显式区分。** 用 `【原文】` / `【本组判断】` 标注。

完整规则见 [`AGENTS.md`](AGENTS.md)。

---

## 7. 与写作仓库的关系

- 阅读仓库是**证据源**：论文元数据、笔记、轴定义。
- 写作仓库是**论证层**：`group/` 放领域地图、分类论证、证据链、开放问题、PPT；`report/` 放个人综述。
- 写作仓库引用本仓库的笔记时，使用**论文 ID 或 GitHub URL**，不要用跨仓库相对路径。
- `refs/refs.bib` 只在本仓库维护；写作仓库用 `scripts/sync_refs.py` 生成本地快照。

---

*最后更新：2026-10-30*
