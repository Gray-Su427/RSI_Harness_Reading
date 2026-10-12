# report/ — LaTeX 综述报告

> ⚠️ **寒假综述报告需个人独立撰写。** 本目录是全组共享的**骨架**，不是成稿。

英文报告，`article` 类 + `natbib` + `IEEEtran.bst`，`pdflatex` 编译（无需 XeLaTeX）。

---

## 编译

```bash
cd report
make            # 需要 latexmk
```

或 Windows 下双击 `build.bat`。

`build.bat` 会自动检测：有 `latexmk` 就用它，没有则回退到
`pdflatex → bibtex → pdflatex ×2` 的经典四遍流程。

### 前置条件

- **TeX Live**（推荐，https://www.tug.org/texlive/）或 MiKTeX
- `refs/refs.bib` 必须存在。当前已提供引导版本（17 篇，从 `verified.csv` 构造）

> 按 `AGENTS.md` §7.4，`refs.bib` 最终应由 Zotero 导出。
> 当前文件头部有醒目注释，核验完 venue 后请同步更新。

---

## 文件

```
report/
├── main.tex                  主文件
├── preamble.tex              宏包与自定义命令
├── sections/
│   ├── 00-abstract.tex       摘要（150-250 词）
│   ├── 01-introduction.tex   引言
│   ├── 02-background.tex     RSI 定义与术语固定
│   ├── 03-taxonomy.tex       五轴分类体系
│   ├── 04-evidence.tex       >=3 条证据
│   ├── 05-open-questions.tex 2-3 个开放问题
│   └── 06-conclusion.tex     核心结论
├── tables/
│   └── comparison.tex        方法比较表
├── Makefile
└── build.bat
```

---

## ⚠️ 两个已知风险

### 1. 中文路径

本仓库位于 `学术文献阅读` 下（**待改名**为 `NJU_Grade2_RSI_LitReview`）。

TeX 工具链在 Windows 上对非 ASCII 路径的历史兼容问题可能导致
`Package inputenc Error` 或文件找不到。

**若编译失败**，把整个 `report/` 目录复制到纯 ASCII 路径再编译：

```bash
mkdir -p /c/temp/rsr
cp -r report/* /c/temp/rsr/
cd /c/temp/rsr && make
```

文件名已全部使用 ASCII，不含中文，复制后即可正常编译。

### 2. 跨目录 bibliography

`main.tex` 使用：

```latex
\bibliographystyle{IEEEtran}
\bibliography{../refs/refs}
```

从 `report/` 运行时，`../refs/refs.bib` 应能正确解析（main.bbl 会生成在 `report/`）。

**若 BibTeX 报 "I couldn't open database file"**，改用环境变量方案：

```bash
export BIBINPUTS="../refs:"
bibtex main
```

或在 `main.tex` 中改为先复制一份 `refs.bib` 到 `report/` 下（**不推荐**，
会破坏单一数据源）。

---

## 自定义命令

`preamble.tex` 中定义，写作时可直接用：

| 命令 | 效果 |
|---|---|
| `\paperID{arxiv-2505.22954}` | 灰色等宽显示论文 ID |
| `\unverified` | 红色 `[UNVERIFIED]` 标记 |
| `\todo{...}` | 红色斜体占位符，**提交前须全部清除** |
| `\na` | 灰色破折号（表格空单元格） |

### 提交前清理

```bash
grep -rn '\\todo{' sections/ *.tex
```

必须**零命中**。`\todo` 是骨架期的标记，不是正文。

---

## 写作顺序

**不要**从 `01-introduction.tex` 开始写。正确顺序：

```
03-taxonomy  →  04-evidence  →  05-open-questions  →  01-introduction  →  00-abstract
```

理由与 `synthesis/README.md` 相同：结论是被推导出来的，不是被预设的。
先定分类轴容易让文献被强行归类；先写引言容易把引言写成目录。

最后由 `06-conclusion.tex` 的核心结论反推 `00-abstract.tex`。

### 核心结论的三处一致性

课程硬指标要求 **1 句核心结论**。它必须出现在**四个地方且完全一致**：

- [ ] `report/sections/06-conclusion.tex`（正文，权威版本）
- [ ] `report/sections/00-abstract.tex`
- [ ] `../README.md` 第 2 节
- [ ] `../slides/outline.md` 的 P1 与 P13

---

## 内容来源

本目录的**所有内容**必须来自以下三处，不得凭空生成：

| 来源 | 对应内容 |
|---|---|
| `../synthesis/taxonomy.md` | `03-taxonomy.tex` |
| `../synthesis/evidence.md` | `04-evidence.tex` + `tables/comparison.tex` |
| `../synthesis/open-questions.md` | `05-open-questions.tex` |
| `../notes/deep/*.md` | 各节的事实与引用 |
| `../refs/refs.bib` | 全部引用 |

> **幻觉防护**：本综述的每一条引用都必须能追溯到 `refs/refs.bib`，
> 而 `refs/refs.bib` 的每一条都能追溯到 `refs/verified.csv` 的 arXiv ID 核验记录。
> 链条断裂即为幻觉。

---

## 相关文件

- 质量门禁：[`../AGENTS.md`](../AGENTS.md) §6
- 分类体系：[`../synthesis/taxonomy.md`](../synthesis/taxonomy.md)
- 争议清单：[`../synthesis/open-questions.md`](../synthesis/open-questions.md)
- 汇报 PPT：[`../slides/outline.md`](../slides/outline.md)
