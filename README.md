# Review of Recursive Self-Improvement: Harness

RSI 专题课程 · 小组综述项目 · 方向：**Harness 自进化**

> 本仓库是全组**共享的调研素材与方法论**。寒假提交的综述报告为**个人独立撰写**，
> 本目录提供的是证据、分类骨架与工具链，不是报告成稿。

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

## 2. 一句话核心结论

<!-- TODO: 第三阶段填写。Gate 3 要求：必须是被 taxonomy / evidence / open-questions 三份文件同时支撑的一句话。 -->

**待定**

> 填写指引：不要写成"综述介绍了什么"，要写成"我们从文献中读出了什么判断"。
> 反例（不合格）："本文综述了 Harness 自进化的各种方法。"
> 正例（合格）："在 X 条件下，Harness 自进化的收益可由 Y 解释，但该结论在 Z 条件下失效。"

---

## 3. 进度看板

| 阶段 | 交付物 | 状态 | 说明 |
|---|---|---|---|
| 第一次课 | 领域地图 + 选题边界 | ⬜ 未开始 | 见 `notes/skim/` |
| 第二次课 | 精读笔记 ≥5 篇 + 分类体系 | ⬜ 未开始 | 见 `notes/deep/` |
| 第三次课 | 证据链 + 争议 + PPT | ⬜ 未开始 | 见 `synthesis/` |
| 汇报 | 10 min 报告 + 5 min 提问 | ⬜ 未开始 | 见 `slides/outline.md` |
| 寒假 | 综述报告（个人独立） | ⬜ 未开始 | 见 `report/` 骨架 |

### 硬指标自检

来自课程 PPT 第 12 页，缺一不可：

- [ ] 完整 Schema 精读笔记 ≥ **5** 篇
- [ ] 其中 ≥ **1** 篇经典 / 高质量同行评审
- [ ] 其中 ≥ **1** 篇 **2025–2026** 新工作
- [ ] 其中 ≥ **1** 篇工业界（或产学合作）
- [ ] ≥ **3** 条主要证据，每条附 **≥2** 篇参考文献
- [ ] **2–3** 个争议结论或开放问题
- [ ] **1** 个分类体系
- [ ] **1** 句核心结论

详细自检清单见 [`AGENTS.md`](AGENTS.md) 第 6 节质量门禁。

---

## 4. 目录导航

```
.
├── AGENTS.md          🔴 工作契约：规则、Schema、质量门禁、AI 红线
├── README.md          ← 你在这里
├── .gitignore
│
├── refs/              文献元数据
│   ├── verified.csv   已核验论文（17 篇）
│   └── pool.csv       泛读候选池
│
├── notes/             笔记
│   ├── TEMPLATE.md    笔记 Schema 模板
│   ├── skim/          泛读卡片
│   └── deep/          精读笔记
│
├── synthesis/         综合产出
│   ├── taxonomy.md    分类体系（五轴，待验证）
│   ├── evidence.md    证据链
│   └── open-questions.md
│
├── slides/            PPT 大纲
│
├── scripts/           工具
│   └── fetch_pdfs.py  按 CSV 批量下载论文 PDF
│
└── report/            LaTeX 综述报告骨架（英文）
```

---

## 5. 快速上手

```bash
# 1. 下载已核验论文的 PDF（先 dry-run 看解析结果）
python scripts/fetch_pdfs.py --dry-run
python scripts/fetch_pdfs.py

# 2. 泛读：按 notes/README.md 的 5 步路径读，在 notes/skim/ 建卡片

# 3. 精读：复制 notes/TEMPLATE.md 到 notes/deep/<id>.md

# 4. 编译综述报告
cd report && make          # 或 Windows 下双击 build.bat
```

### 检索渠道

| 用途 | 渠道 |
|---|---|
| venue / 录用状态核验 | [DBLP](https://dblp.org/) · [OpenReview](https://openreview.net/) |
| 文献检索 | [arXiv](https://arxiv.org/) · [Semantic Scholar](https://www.semanticscholar.org/) |
| 引用图谱 | [Google Scholar](https://scholar.google.com/) · [Connected Papers](https://www.connectedpapers.com/) |

---

## 6. 三条最重要的规矩

1. **入库前必须核验 arXiv ID 真实存在。** 幻觉出来的文献比没有文献更有害。
2. **未核验的 venue 一律标 `venue_verified: false`。** 当前 `refs/verified.csv` 中 17 篇**全部**为 `false`。
3. **"论文声称"与"我们判断"必须显式区分。** 用 `【原文】` / `【本组判断】` 标注。

完整规则见 [`AGENTS.md`](AGENTS.md) 第 7 节与第 10 节。

---

*最后更新：2026-10-12*
