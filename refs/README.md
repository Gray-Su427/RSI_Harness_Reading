# refs/ — 文献元数据

本目录是项目内**唯一的文献数据源**。笔记、证据、LaTeX 报告中的每一条引用都必须能追溯到这里。

## 文件

| 文件 | 作用 | 维护方式 |
|---|---|---|
| `verified.csv` | **已核验**论文的元数据（当前 17 篇） | 手工维护 |
| `pool.csv` | 泛读候选池，**尚未**核验/筛选的全集 | 泛读阶段持续追加 |
| `refs.bib` | BibTeX 库，供 LaTeX 报告引用 | **由 Zotero 导出**，勿手写 |

> `refs.bib` 当前尚未生成。按 `AGENTS.md` §7.4，用 Zotero 管理并导出到本目录。
> LaTeX 报告通过 `\bibliography{../refs/refs}` 引用本文件，不复制副本。

---

## `verified.csv` 字段说明

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | 文本 | **主键**，与笔记文件名一致。`arxiv-<YYMM>.<NNNNN>` 或 `venue-<年份>-<slug>` |
| `title` | 文本 | 原文标题，**不要翻译** |
| `authors` | 文本 | 前 3 位作者 + `et al.` |
| `year` | 整数 | 发表/发布年份 |
| `venue` | 文本 | 会议全称，或 `arXiv preprint` |
| `venue_verified` | `true`/`false` | **仅当**经 DBLP / OpenReview / 会议官网确认后填 `true` |
| `industry` | `true`/`false` | 是否工业界（或产学合作） |
| `org` | 文本 | 机构。非空便于按机构聚类分析 |
| `role` | 枚举 | `seed` 课程种子 / `harness-core` 直接命中 / `industry` 工业界 / `survey` 综述 |
| `axis_a_object` | 列表 | 改进对象。`;` 分隔多值 |
| `axis_b_signal` | 列表 | 改进信号。`;` 分隔 |
| `axis_c_search` | 列表 | 搜索算子。`;` 分隔 |
| `axis_d_guarantee` | 枚举 | `none` / `empirical` / `formal` / `formal-safety` |
| `axis_e_recursiveness` | 枚举 | `one-shot` / `iterative` / `full-rsi` / `co-evolution` |
| `source_url` | URL | 实际检索到的页面 URL（核验凭证） |
| `read_status` | 枚举 | `pool` / `skim` / `deep` |
| `note` | 文本 | 自由备注，`;` 内为同一备注内的分隔符 |

### ⚠️ 关于 `venue_verified`

**当前 17 篇全部为 `false`。**

只核验了 arXiv ID 真实存在，**未核验任何录用状态**。其中 4 篇课程种子的 venue 直接来自课程 PPT，属于二手信息：

- `arxiv-2310.02304` STOP — PPT 称 COLM 2024
- `arxiv-2408.08435` ADAS — PPT 称 ICLR 2025
- `arxiv-2505.22954` DGM — PPT 称 ICLR 2026
- `arxiv-2504.15228` SICA — PPT 未标 venue

**优先核验 DGM**：它同时占"工业界"与"2025–2026 新工作"两项硬指标，venue 填错影响最大。

核验方法见 `AGENTS.md` §7.1。**不要根据作者或机构的过往发表记录推断会议。**

### ⚠️ 关于 `axis_*` 字段

这五轴是**待验证假设**，见 `AGENTS.md` §5 与 `synthesis/taxonomy.md`。

CSV 中的取值只填了摘要可支撑的部分；**未精读的论文保持为空**，不要提前填满。
空值不是遗漏，是"尚未判断"的诚实标记。

---

## `pool.csv` 字段说明

泛读候选池，结构同上但允许更松。追加时**至少**填：

`id` · `title` · `year` · `source_url` · `read_status=pool`

其余字段可在升为 skim / deep 时补齐。升入 `verified.csv` 前必须完成 arXiv ID 核验。

---

## 多值字段约定

用 **分号 `;`** 分隔，例：

```
control-flow;code
```

CSV 字段内的**逗号**必须用双引号包裹（标准 CSV 转义）：

```
"Zhang, Hu, Lu, Lange, Clune"
```

---

## Excel 打开乱码？

文件为 **UTF-8 无 BOM**。用 VS Code / Excel 均可，Excel 请在导入时显式选择"UTF-8"。
若确需 BOM，Python 侧请用 `encoding="utf-8-sig"` 读取（`scripts/fetch_pdfs.py` 已兼容）。

---

## 相关文件

- 字段规则全文：[`../AGENTS.md`](../AGENTS.md) §7
- 分类体系：[`../synthesis/taxonomy.md`](../synthesis/taxonomy.md)
- PDF 下载脚本：[`../scripts/fetch_pdfs.py`](../scripts/fetch_pdfs.py)
