"""生成中期汇报 deck（6 页 + 2 backup，5 分钟 / 280 s）。

可读性版（2026-11-02）：正文 12–14 pt、标题 30 pt、大数字 32–34 pt；
屏幕上只留判断与数字，论据与出处放讲稿备注与 backup 页。

用法：
    python make_deck.py

输出：deck-rsi-midterm.pptx（16:9，中文字体 Microsoft YaHei，含讲稿备注）
数据源：../p2/taxonomy-ae.png、../p2/classification.md、../p1/stats.md、p4/plan.md
改动顺序：先改 deck-outline.md 与 narrative.md → 再改本脚本 → 重跑。
"""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt
from pptx.oxml.ns import qn
from lxml import etree

HERE = Path(__file__).resolve().parent
IMG = HERE.parent / "p2" / "taxonomy-ae.png"
OUT = HERE / "deck-rsi-midterm.pptx"

FONT = "Microsoft YaHei"
NAVY = RGBColor(0x12, 0x25, 0x3A)
ACCENT = RGBColor(0xC2, 0x6A, 0x0B)
INK = RGBColor(0x1F, 0x29, 0x37)
MUTED = RGBColor(0x6B, 0x72, 0x80)
LIGHT = RGBColor(0xF3, 0xF4, 0xF6)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BORDER = RGBColor(0xD8, 0xDD, 0xE4)
GREEN = RGBColor(0x0F, 0x76, 0x6E)
RED = RGBColor(0x9B, 0x22, 0x26)

W, H = 13.333, 7.5


# ---------------------------------------------------------------- primitives
def style_run(run, size, bold=False, color=INK, italic=False):
    f = run.font
    f.name = FONT
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    f.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    for tag in ("a:ea", "a:cs"):
        for old in rPr.findall(qn(tag)):
            rPr.remove(old)
        el = etree.SubElement(rPr, qn(tag))
        el.set("typeface", FONT)


def rect(slide, x, y, w, h, fill, line=None, line_w=1.0, shape=1):
    from pptx.enum.shapes import MSO_SHAPE

    kind = MSO_SHAPE.RECTANGLE if shape == 1 else MSO_SHAPE.ROUNDED_RECTANGLE
    shp = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        shp.fill.background()
    else:
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(line_w)
    shp.shadow.inherit = False
    if shape == 2:
        try:
            shp.adjustments[0] = 0.06
        except Exception:
            pass
    return shp


def textbox(slide, x, y, w, h):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.04)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    return tf


def para(tf, text, size=14, bold=False, color=INK, before=0, after=4,
         first=False, align=PP_ALIGN.LEFT, spacing=1.12):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(before)
    p.space_after = Pt(after)
    p.line_spacing = spacing
    run = p.add_run()
    run.text = text
    style_run(run, size, bold, color)
    return p


def header(slide, kicker, title, page, total=8):
    rect(slide, 0, 0, W, 0.10, NAVY)
    rect(slide, 0, 0.10, 1.6, 0.035, ACCENT)
    tf = textbox(slide, 0.55, 0.22, 10.0, 0.32)
    para(tf, kicker, 11, True, ACCENT, first=True, after=0)
    tf = textbox(slide, 0.55, 0.50, 12.3, 0.68)
    para(tf, title, 30, True, NAVY, first=True, after=0, spacing=1.0)
    tf = textbox(slide, 0.55, 7.06, 8.0, 0.3)
    para(tf, "P3（szh）· RSI 中期汇报 · 2026-11-02", 10, False, MUTED, first=True, after=0)
    tf = textbox(slide, 11.7, 7.06, 1.1, 0.3)
    para(tf, f"{page} / {total}", 10, False, MUTED, first=True, after=0, align=PP_ALIGN.RIGHT)


def add_table(slide, x, y, data, col_widths, row_h=0.45, header=True,
              body_size=12, header_size=12, zebra=True, align_center_cols=()):
    rows, cols = len(data), len(data[0])
    width = sum(col_widths)
    shape = slide.shapes.add_table(rows, cols, Inches(x), Inches(y),
                                   Inches(width), Inches(row_h * rows))
    tbl = shape.table
    tbl.first_row = False
    tbl.horz_banding = False
    for i, cw in enumerate(col_widths):
        tbl.columns[i].width = Inches(cw)
    for r in range(rows):
        tbl.rows[r].height = Inches(row_h)
        for c in range(cols):
            cell = tbl.cell(r, c)
            cell.margin_left = cell.margin_right = Inches(0.08)
            cell.margin_top = cell.margin_bottom = Inches(0.02)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            if header and r == 0:
                cell.fill.fore_color.rgb = NAVY
            elif zebra and r % 2 == 0:
                cell.fill.fore_color.rgb = LIGHT
            else:
                cell.fill.fore_color.rgb = WHITE
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if c in align_center_cols else PP_ALIGN.LEFT
            p.space_before = Pt(0)
            p.space_after = Pt(0)
            p.line_spacing = 1.0
            run = p.add_run()
            run.text = str(data[r][c])
            is_head = header and r == 0
            style_run(run, header_size if is_head else body_size,
                      bold=is_head or (c == 0 and rows > 1),
                      color=WHITE if is_head else INK)
    return tbl


def card(slide, x, y, w, h, tag, title, lines, tag_color=ACCENT,
         body=12, title_size=15, body_top=0.86):
    rect(slide, x, y, w, h, WHITE, BORDER, 0.75, shape=2)
    rect(slide, x, y, 0.075, h, tag_color)
    tf = textbox(slide, x + 0.18, y + 0.10, w - 0.30, 0.30)
    para(tf, tag, 11, True, tag_color, first=True, after=0)
    tf = textbox(slide, x + 0.18, y + 0.40, w - 0.30, 0.42)
    para(tf, title, title_size, True, NAVY, first=True, after=0, spacing=1.0)
    tf = textbox(slide, x + 0.18, y + body_top, w - 0.30, h - body_top - 0.06)
    for i, (text, opts) in enumerate(lines):
        para(tf, text, opts.get("size", body), opts.get("bold", False),
             opts.get("color", INK), first=(i == 0), after=opts.get("after", 4),
             before=opts.get("before", 0), spacing=opts.get("spacing", 1.12))


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text.strip()


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


# ---------------------------------------------------------------- build
prs = Presentation()
prs.slide_width = Inches(W)
prs.slide_height = Inches(H)

# ============ P1 · 封面 + 核心结论 ============
s = blank(prs)
rect(s, 0, 0, W, H, NAVY)
rect(s, 0.9, 0.95, 0.9, 0.05, ACCENT)
tf = textbox(s, 0.9, 1.10, 8.4, 0.32)
para(tf, "RECURSIVE SELF-IMPROVEMENT IN HARNESS  ·  中期汇报", 12, True,
     RGBColor(0x9A, 0xB0, 0xC6), first=True, after=0)

tf = textbox(s, 0.9, 1.55, 11.6, 1.7)
para(tf, "共识在「改什么」，", 42, True, WHITE, first=True, after=2, spacing=1.05)
para(tf, "分歧在「递归到哪层」", 42, True, WHITE, after=0, spacing=1.05)

rect(s, 0.9, 3.60, 11.5, 1.88, WHITE, None, shape=2)
tf = textbox(s, 1.15, 3.73, 11.05, 1.65)
para(tf, "核心结论", 11, True, ACCENT, first=True, after=8)
para(tf, "harness 自进化的共识在「改什么」（9 篇里 6 篇改的是代码），分歧在「递归到哪层」和「凭什么相信改进」——高递归与高保证的格点至今是空白，不是已被占领。",
     20, True, NAVY, after=0, spacing=1.24)

tf = textbox(s, 0.9, 5.95, 11.4, 0.4)
para(tf, "中期汇报（5 分钟）｜P3（szh）｜汇报日 2026-11-02｜数据截至 2026-10-31，n = 19", 12,
     False, RGBColor(0x9A, 0xB0, 0xC6), first=True, after=0)

tf = textbox(s, 0.9, 6.55, 11.6, 0.35)
para(tf, "材料：P1 统计与核验 · P2 分类与 A×E 图 · P3 叙事与整合 · P4 精读计划与风险", 11,
     False, RGBColor(0x7E, 0x95, 0xAC), first=True, after=0)

notes(s, """
25 秒。先给结论，不要介绍背景。
「先给结论。我们把 19 篇文献、9 篇核心样本放在同一张图上，读出来的是：大家已经同意改什么了——9 篇里 6 篇改的是代码；但递归到哪一层、凭什么相信这个改进，没有共识。真正高递归、高保证的格点，现在还是空的。」
然后直接翻页，不要停在封面上解释标题。

【论据（不投屏，被追问时用）】
- 19 篇入库、全部 skim、0 篇精读；9 篇 = P4 的 7 篇精读名单 + SICA、MGM。
- 「6 篇改代码」的口径是主 A 值：STOP、DGM、AlphaEvolve、SEVerA、SICA、MGM。
- 高递归格点：full-rsi 只有 DGM（且仅代码层）；co-evolution 为 0。
""")

# ============ P2 · 边界与规模 ============
s = blank(prs)
header(s, "01 · 边界与规模", "只改最外层的程序结构——池子够宽，厚度不够", 2)

tf = textbox(s, 0.55, 1.14, 5.6, 0.3)
para(tf, "RSI 三层次：本组只做 Harness", 11.5, True, MUTED, first=True, after=0)
add_table(s, 0.55, 1.46, [
    ["层次", "改什么", "本组"],
    ["Model", "参数、训练过程", "否"],
    ["Data", "数据、经验、生产管线", "否"],
    ["Harness", "架构、工具、脚手架、控制流", "是"],
], [1.1, 3.5, 0.95], row_h=0.48, body_size=12, header_size=12, align_center_cols=(2,))

rect(s, 0.55, 3.60, 5.55, 1.55, LIGHT, None, shape=2)
rect(s, 0.55, 3.60, 0.07, 1.55, ACCENT)
tf = textbox(s, 0.78, 3.70, 5.2, 1.38)
para(tf, "本方向的核心问题", 11, True, ACCENT, first=True, after=4)
para(tf, "系统能否修改「产生行为」，", 15.5, True, NAVY, after=0, spacing=1.12)
para(tf, "乃至产生「下一次改进」的程序结构？", 15.5, True, NAVY, after=5, spacing=1.12)
para(tf, "不改参数、不改数据，改的是把它们组织起来的那个程序。", 11.5, False, MUTED, after=0)

blocks = [
    ("① 规模", "19", "篇入库，全部完成 skim", "7 篇精读候选，0 篇已精读"),
    ("② 时效与可信度", "12/19", "出自 2026（63%）；4/19 有录用", "2026 年 12 篇中 0 篇——加速 ≠ 已被检验"),
    ("③ 漏斗", "149→2", "检索命中 → 新增入库", "标题层筛查约 50 条；宽度够、厚度不够"),
]
y = 1.14
for tag, big, mid, small in blocks:
    rect(s, 6.35, y, 6.42, 1.34, WHITE, BORDER, 0.75, shape=2)
    tf = textbox(s, 6.52, y + 0.10, 2.4, 0.30)
    para(tf, tag, 11, True, ACCENT, first=True, after=0)
    tf = textbox(s, 6.52, y + 0.42, 2.35, 0.62)
    para(tf, big, 32, True, NAVY, first=True, after=0, spacing=1.0)
    tf = textbox(s, 9.05, y + 0.36, 3.55, 0.92)
    para(tf, mid, 12.5, True, INK, first=True, after=4, spacing=1.10)
    para(tf, small, 11, False, ACCENT if tag.startswith("②") else MUTED, after=0, spacing=1.10)
    y += 1.40

rect(s, 0.55, 5.55, 12.22, 0.92, LIGHT, None, shape=2)
tf = textbox(s, 0.78, 5.63, 11.85, 0.78)
para(tf, "149 检索命中 → 约 50 标题筛查 → 2 新增 → 19 池 → 19 skim → 7 精读候选 → 0 已精读",
     12.5, True, NAVY, first=True, after=3)
para(tf, "149 是查询命中数，不是阅读数；第 ② 层用「≈」是因为只看了标题与日期。", 10.5, False,
     MUTED, after=0)

notes(s, """
35 秒。快讲，不要念表。
「我们只改最外层的程序结构，不碰参数、不碰数据。池子 19 篇，63% 是 2026 年的——看起来这个方向在加速。但同一个数字的另一面是：2026 年这 12 篇，一篇都还没有可核验的录用记录。所以加速是真的，'已经站住'还不能说。漏斗上，149 条检索最后只新增 2 篇入库，说明池子的宽度够了，厚度不够。」

【论据（不投屏）】
- 4 篇已核验：STOP=COLM 2024 Spotlight、ADAS=ICLR 2025、DGM=ICLR 2026、Gao 综述=TMLR 2026，全是 2023–2025 的工作。
- 19 篇构成：seed 4、harness-core 7、industry 1、survey 7；综述占 37%，不能进 evidence。
- 11 篇 industry:true 中 3 篇是综述（Code as Harness、Safety survey、DCRI），可作工业界实证的只有 8 篇。
- 漏斗：149 命中（6 条 arXiv 查询 + 1 条网络检索）→ 约 50 标题筛查 → 2 新增入库。
""")

# ============ P3 · A×E 图 ============
s = blank(prs)
header(s, "02 · 分类体系", "A×E 体系图：改什么 × 递归到哪层", 3)

s.shapes.add_picture(str(IMG), Inches(0.35), Inches(1.05), width=Inches(8.70))
tf = textbox(s, 0.35, 5.88, 8.70, 0.55)
para(tf, "图 1 · A×E 体系图（n = 9）。橙 = 工业界 / 产学合作，蓝 = 学术界；灰带 = 作者未自我界定。",
     11, False, MUTED, first=True, after=0, spacing=1.1)

readings = [
    ("密集 · code 列", "6 / 9", "同一列从 full-rsi 一直延伸到灰带", ACCENT),
    ("空白 · 三个格点", "0 / 0 / 0", "co-evolution、evaluator、context 主值全为 0", RED),
    ("灰带 · 作者未界定", "5 篇", "ADAS、AlphaEvolve、SEVerA、Harness≠Benefit、MGM", GREEN),
]
y = 1.05
for tag, big, desc, color in readings:
    rect(s, 9.25, y, 3.73, 1.30, WHITE, BORDER, 0.75, shape=2)
    rect(s, 9.25, y, 0.07, 1.30, color)
    tf = textbox(s, 9.40, y + 0.09, 2.3, 0.30)
    para(tf, tag, 11, True, color, first=True, after=0)
    tf = textbox(s, 9.40, y + 0.40, 1.7, 0.55)
    para(tf, big, 22, True, NAVY, first=True, after=0, spacing=1.0)
    tf = textbox(s, 9.40, y + 0.92, 3.45, 0.36)
    para(tf, desc, 11, False, INK, first=True, after=0, spacing=1.08)
    y += 1.42

rect(s, 9.25, 5.32, 3.73, 1.10, RGBColor(0xEC, 0xF6, 0xF5), None, shape=2)
tf = textbox(s, 9.40, 5.40, 3.45, 0.95)
para(tf, "能落位的只有 3 篇", 11, True, GREEN, first=True, after=3)
para(tf, "STOP = iterative｜DGM = full-rsi（仅代码层）｜RHO = one-shot", 10.5, False, INK,
     after=0, spacing=1.10)

notes(s, """
65 秒。这一页是主体，按「密集 → 空白 → 灰带」三步讲。
「这张图横轴是改什么，纵轴是递归到哪一层。先看密集区：9 篇里 6 篇改代码，这是共识。但注意同一列——从最上面的 full-rsi 一直到最下面的灰带都有点，说明'改代码'和'递归到哪层'是两件事。
再看空白：共进化那一行是空的，评测器、上下文这两列也是空的；形式化保证只有一个点，SEVerA；自偏好也只有一个点，RHO。空白本身就是我们的中期结论之一。
最后看底部灰带：5 篇作者自己没有界定递归深度。我们没有替作者填，因为按项目纪律，E 轴只认作者原话。所以现在能落位的只有 3 篇：STOP 迭代、DGM 完整 RSI 但只在代码层、RHO 单轮。」

【论据（不投屏）】
- 5 篇灰带：ADAS、AlphaEvolve、SEVerA、Harness≠Benefit、MGM；SICA 是 full-rsi 候选，单独标虚线。
- A 轴计数（主值）：code 6、control-flow 1（ADAS）、tool 1（RHO）、memory 1（Harness≠Benefit）。
- D 轴：empirical 7、formal-safety 1、none 1；B 轴：external 6、failure-trajectory 2、self-preference 1。
- 边界三篇：AlphaEvolve 改任务算法；SEVerA 的 Learn 用 GRPO 改权重；Harness≠Benefit 是测量研究。
- 若问「为什么 AlphaEvolve 不算」：它的 prompt 模板、LLM ensemble、program database、evaluator 都是固定外壳。
- 若问「RHSI 呢」：作者自称 recursive / co-evolution，但明说只做了循环前半段，所以不填 co-evolution。
""")

# ============ P4 · 三条发现 ============
s = blank(prs)
header(s, "03 · 三条发现", "密集区在哪、空白在哪、哪些不能硬归类", 4)

cols = [
    ("发现 1 · 密集区", "共识在改进对象，不在递归深度",
     [("6 / 9 主 A 值 = code", {"bold": True, "size": 14}),
      ("STOP、DGM、AlphaEvolve、SEVerA、SICA、MGM", {"size": 11.5, "color": MUTED}),
      ("E 轴可落位仅 3 篇，5 篇待精读", {"size": 12}),
      ("→ A 轴不能替代 E 轴", {"size": 11.5, "color": MUTED})],
     "反例：AlphaEvolve 的 code 是任务算法，算进密集区会高估样本量。",
     ACCENT),
    ("发现 2 · 空白", "高递归与高保证的格点是空的",
     [("co-evolution 0｜evaluator 0｜context 0", {"bold": True, "size": 12.5}),
      ("formal-safety 仅 SEVerA", {"size": 12}),
      ("self-preference 仅 RHO", {"size": 12}),
      ("→ 空白是方向，不是天花板", {"size": 11.5, "color": MUTED})],
     "反例：RHSI 自称 co-evolution，但只做完循环前半段。",
     RED),
    ("发现 3 · 反例", "三篇边界工作只能标注",
     [("AlphaEvolve —— 任务算法", {"bold": True, "size": 12.5}),
      ("SEVerA —— Learn 改权重", {"bold": True, "size": 12.5}),
      ("Harness≠Benefit —— 测量研究", {"bold": True, "size": 12.5}),
      ("→ 删掉会失去三类对照", {"size": 11.5, "color": MUTED})],
     "宁可标边界，也不替作者下「都算 harness RSI」的结论。",
     GREEN),
]
x = 0.55
for tag, title, lines, reverse, color in cols:
    card(s, x, 1.15, 3.95, 3.75, tag, title, lines, tag_color=color)
    rect(s, x + 0.18, 4.02, 3.60, 0.76, LIGHT, None, shape=2)
    tf = textbox(s, x + 0.28, 4.08, 3.40, 0.66)
    para(tf, reverse, 10.5, False, MUTED, first=True, after=0, spacing=1.06)
    x += 4.14

rect(s, 0.55, 5.14, 12.22, 0.98, NAVY, None, shape=2)
tf = textbox(s, 0.80, 5.22, 11.75, 0.84)
para(tf, "三条发现指向同一个结论", 11, True, RGBColor(0xE5, 0xB5, 0x7A), first=True, after=3)
para(tf, "密集区是「改什么」的共识；空白是「递归深度 + 保证强度」的未占领区——后者才是选题空间。",
     16, True, WHITE, after=0, spacing=1.12)

tf = textbox(s, 0.55, 6.30, 12.2, 0.35)
para(tf, "口径：n = 9 有选择偏差（7 篇精读 + 2 篇补充），不外推整个领域。", 10.5, False, MUTED,
     first=True, after=0)

notes(s, """
65 秒。每条一句判断 + 一篇支撑 + 一篇反例。
「三条发现。第一，密集区：6 篇改代码，但能落位的递归深度只有 3 篇——共识在改进对象，不在递归深度。
第二，空白：共进化、评测器、上下文三个格点为零，形式化保证只有一篇。注意 RHSI 自称共进化，但作者自己说只做完了循环的前半段，所以不能填进去——这是'声称'和'完成'的差别。
第三，反例：有三篇是边界。AlphaEvolve 改的是任务算法，SEVerA 的 Learn 阶段改模型权重，Harness≠Benefit 是测量研究。我们没有为了凑数把它们硬归成 harness RSI，而是保留并标注——这本身也是结论。」

【论据（不投屏）】
- 组合格点：9 篇里没有一篇同时做到「高递归 + 高保证」——full-rsi 只有 DGM（代码层），formal-safety 只有 SEVerA，两者不是同一篇。
- AlphaEvolve：prompt 模板、LLM ensemble、program database、evaluator 全固定，只优化任务算法。
- SEVerA：Search 合成程序（code），Learn 用 GRPO 微调权重，所以只作跨界对照。
- Harness≠Benefit：A/B 记录的是被测协议（skills / prompts / memories），不是本文提出的方法；D=none，是测量研究。
- ADAS 的 A 主值有 control-flow / code 两种读法；若改记 code，密集区会变成 7/9，说明 A 轴粒度需要精读后复核。
""")

# ============ P5 · 三个争议 ============
s = blank(prs)
header(s, "04 · 三个争议", "结论可信吗、机制自洽吗、比较公平吗", 5)

qs = [
    ("Q1", "能更新 ≠ 有收益", "arxiv-2605.30621",
     "先拆三种污染：选择偏差、验证集过拟合、基准污染；查是否有 hold-out 与尝试次数 N。",
     "增益可独立复现 → 领域叙事成立，价值回到分类与设计空间。"),
    ("Q2", "验证器独立于被优化对象吗", "RHO 2606.05922 · SEVerA 2603.25111",
     "RHO 只保证「不劣于基线」：最偏好 0.78 ≠ 测试最高 0.85；SEVerA 不含 token / 时间预算。",
     "自偏好与形式化在无标注部署下成立 → 是实用性突破，不是循环论证。"),
    ("Q3", "成本扣除了吗", "DGM 2505.22954 · RHO 2606.05922",
     "DGM 约 $22k / 2 周；RHO 是唯一同口径 agent calls（103 vs 41 vs 320）；多数只做部分报告。",
     "若同口径报告成本且仍有增益 → 本条作废。"),
]
x = 0.55
for tag, title, src, stance, wrong in qs:
    card(s, x, 1.15, 3.95, 3.65, tag, title,
         [("出处：" + src, {"size": 10.5, "color": MUTED, "after": 12}),
          ("我们的立场", {"size": 11, "bold": True, "color": ACCENT, "after": 4}),
          (stance, {"size": 12, "after": 14}),
          ("如果我错了", {"size": 11, "bold": True, "color": ACCENT, "after": 4}),
          (wrong, {"size": 11.5})],
         tag_color=ACCENT, body=12)
    x += 4.14

rect(s, 0.55, 5.05, 12.22, 1.00, LIGHT, None, shape=2)
tf = textbox(s, 0.80, 5.14, 11.75, 0.84)
para(tf, "这三问就是 7 篇精读的检查表", 13, True, NAVY, first=True, after=3)
para(tf, "答不上来就明说「这正是开放问题」——回答不了自己提出的争议，比不提出更糟。", 11.5,
     False, INK, after=0)

notes(s, """
55 秒。三张卡各 15–20 秒，不要展开论证过程。
「三个争议，按'结论可信吗、机制自洽吗、比较公平吗'递进。
Q1：能更新不等于有收益，要把选择偏差、验证集过拟合、基准污染拆开。
Q2：验证器是不是独立的？RHO 用自偏好，作者自己承认最偏好的方案不是测试最高的——0.78 对 0.85；SEVerA 有形式化保证，但只保功能正确，不保预算。
Q3：成本。DGM 报了两万两千美元两周，RHO 给了唯一一组同口径 agent calls，其余多数没报——所以我们不做效率结论。」
时间紧时砍 Q3 的「如果我错了」，直接进下一页。

【论据（不投屏）】
- Q1 出处细节：该文主张 harness 更新与 harness 收益应当解耦；增益可能来自选择偏差（多试几次）、验证集过拟合、基准污染。
- Q2 原文：「What the mechanism reliably guarantees is safety rather than perfect ranking.」；反例原文：最偏好 0.78，测试最高 0.85。
- Q2 的 SEVerA：Theorem 5.4 只覆盖功能性规格；作者自陈 resource-unaware，不含 LLM calls / token / wall-clock。
- Q3 数字：DGM 约 $22,000 / 2 周（两个 baseline 各约 $10,000）；RHO 103 vs Meta-Harness 41（1 轮）/ 320（10 轮）agent calls。
- 若问「那 RHO 到底可不可信」：它保证不劣于基线，不是保证最优；单轮、非累积，作者把多轮列为 future work。
""")

# ============ P6 · 计划与开放问题 ============
s = blank(prs)
header(s, "05 · 计划", "7 篇、两周、四条风险——中期交的是判断，不是精读", 6)

tf = textbox(s, 0.55, 1.12, 3.7, 0.28)
para(tf, "精读名单（2 / 2 / 2 / 1）", 11, True, MUTED, first=True, after=0)
add_table(s, 0.55, 1.42, [
    ["人", "论文"],
    ["P1", "STOP、ADAS"],
    ["P2", "DGM、AlphaEvolve"],
    ["P3", "RHO、SEVerA"],
    ["P4", "Harness≠Benefit"],
], [0.70, 3.00], row_h=0.46, body_size=12, header_size=12, align_center_cols=(0,))

tf = textbox(s, 0.55, 3.80, 3.7, 0.28)
para(tf, "两周排期（D1–D14 = 11/03–11/16）", 11, True, MUTED, first=True, after=0)
for i, (d, t) in enumerate([("D1–D7", "七篇 Schema 草稿"), ("D8–D9", "补附录与成本"),
                            ("D10–D11", "交叉核对证据"), ("D12–D14", "证据与争议定稿")]):
    yy = 4.12 + i * 0.55
    rect(s, 0.55, yy, 1.05, 0.40, NAVY if i % 2 == 0 else RGBColor(0x2C, 0x45, 0x60), None, shape=2)
    tf = textbox(s, 0.55, yy + 0.08, 1.05, 0.28)
    para(tf, d, 10.5, True, WHITE, first=True, after=0, align=PP_ALIGN.CENTER)
    tf = textbox(s, 1.72, yy + 0.06, 2.05, 0.30)
    para(tf, t, 11.5, False, INK, first=True, after=0)

tf = textbox(s, 4.45, 1.12, 4.0, 0.28)
para(tf, "四条风险与当前状态", 11, True, MUTED, first=True, after=0)
risks = [
    ("R1 venue", "已关闭", "4 篇已核验（COLM / ICLR×2 / TMLR）", GREEN),
    ("R4 种子综述", "已关闭", "已入库，池 19 篇、skim 19 篇", GREEN),
    ("R2 成本", "仍开放", "DGM / RHO 可查，其余多为部分报告", ACCENT),
    ("R3 复现", "仍开放", "链接可访问 ≠ 可运行 ≠ 已复现", ACCENT),
]
yy = 1.42
for name, status, note, color in risks:
    rect(s, 4.45, yy, 4.30, 1.08, WHITE, BORDER, 0.75, shape=2)
    rect(s, 4.45, yy, 0.06, 1.08, color)
    tf = textbox(s, 4.62, yy + 0.11, 2.45, 0.32)
    para(tf, name, 12, True, NAVY, first=True, after=0)
    tf = textbox(s, 7.15, yy + 0.11, 1.45, 0.30)
    para(tf, status, 11, True, color, first=True, after=0, align=PP_ALIGN.RIGHT)
    tf = textbox(s, 4.62, yy + 0.50, 3.95, 0.50)
    para(tf, note, 10.5, False, MUTED, first=True, after=0, spacing=1.05)
    yy += 1.16

tf = textbox(s, 8.95, 1.12, 3.9, 0.28)
para(tf, "三个开放问题", 11, True, MUTED, first=True, after=0)
for i, q in enumerate(["co-evolution 是没做出来，还是做不出来？",
                       "自偏好能否与独立评测共存？",
                       "形式化保证能否覆盖资源预算？"]):
    yy = 1.42 + i * 1.10
    rect(s, 8.95, yy, 3.85, 0.96, LIGHT, None, shape=2)
    tf = textbox(s, 9.12, yy + 0.10, 3.55, 0.78)
    para(tf, f"0{i + 1}", 10, True, ACCENT, first=True, after=3)
    para(tf, q, 12.5, True, NAVY, after=0, spacing=1.10)

rect(s, 8.95, 4.78, 3.85, 1.45, NAVY, None, shape=2)
tf = textbox(s, 9.15, 4.88, 3.50, 1.28)
para(tf, "中期交付", 10, True, RGBColor(0x9A, 0xB0, 0xC6), first=True, after=5)
para(tf, "19 篇 skim｜4 篇核验｜9 篇分类｜6 页 deck", 11.5, True, WHITE,
     after=5, spacing=1.15)
para(tf, "0 篇精读——这是状态，不是欠账。", 11, False, RGBColor(0xE5, 0xB5, 0x7A), after=0)

tf = textbox(s, 0.55, 6.45, 12.2, 0.35)
para(tf, "谢谢 · 提问环节有 8 条 Q&A 与 9 篇分类总表两张 backup", 12, True, NAVY, first=True, after=0)

notes(s, """
35 秒。收尾要快、要稳。
「最后是计划。7 篇，二二二一分工，汇报后 11 月 3 日到 16 日两周：第一周出草稿，第二周补附录和成本、交叉核对。风险四条，venue 和两篇种子综述已经被 CP1 关掉了，剩下成本和复现。开放问题三个：共进化是没做出来还是做不出来；自偏好能不能和独立评测共存；形式化保证能不能覆盖预算。谢谢。」

【论据（不投屏）】
- 7 篇分工：P1 STOP / ADAS（经典、控制流）；P2 DGM / AlphaEvolve（工业界、full-rsi）；P3 RHO / SEVerA（self-preference、formal-safety）；P4 Harness≠Benefit（测量效度）。
- R1 关闭依据：4/19 有可追溯录用来源（COLM 2024、ICLR 2025、ICLR 2026、TMLR 2026）。
- R4 关闭依据：两篇指定综述已入库（arxiv-2507.21046、venue-2026-dcri-survey），19 篇、19 张 skim。
- R2 仍开放：STOP 只有渐近预算；AlphaEvolve 缺整轮总成本；DGM / RHO / SEVerA 有不同粒度。
- R3 仍开放：多数依赖闭源模型或历史 API；未安装、未运行、未复现。
- 8 条 Q&A 中 2 条（Q5/Q6）已定稿，其余 6 条待本人确认——未确认的不说「我们」。
""")

# ============ B1 · backup 8 Q&A ============
s = blank(prs)
header(s, "BACKUP 1", "8 条 Q&A 速查（每条约 20 秒）", 7)

qa = [
    ["问题", "回答要点", "人"],
    ["① 七篇怎么选？", "覆盖经典/自修改/工业/自偏好/形式化 + 一篇测量研究；同行评审项已由 STOP/ADAS/DGM 满足。", "P1"],
    ["② 读到哪一步？", "19 篇 skim、0 篇精读；中期交的是地图、判断与计划，七篇是精读名单。", "P1"],
    ["③ 多轮为何不算 full RSI？", "只看改进后的系统参与什么：搜产物 vs 改下一轮的程序；作者未界定就记待核实。", "P2"],
    ["④ AlphaEvolve 为何选？", "工业级的「强外部 evaluator + 进化搜索」对照；pipeline 固定，不改 harness。", "P2"],
    ["⑤ 自偏好会自说自话？", "有风险：最偏好 0.78 ≠ 最高 0.85；它保证不劣于基线，不是验证独立。", "P3"],
    ["⑥ SEVerA 是否已安全？", "只覆盖给定规格下的功能正确；作者自陈不含 token / 时间；Learn 还改权重。", "P3"],
    ["⑦ 能更新≠有收益？", "生成端与使用端是两种能力；增益不随基础能力单调增长，弱模型可能不加载更新。", "P4"],
    ["⑧ 两周交什么？", "7 篇完整 Schema + 方法比较 + 3 条证据 + 2–3 争议；缺成本不作效率结论。", "P4"],
]
add_table(s, 0.45, 1.12, qa, [3.05, 8.05, 0.95], row_h=0.54, body_size=10,
          header_size=10.5, align_center_cols=(2,))
tf = textbox(s, 0.45, 6.15, 12.4, 0.35)
para(tf, "P3 已确认 ⑤⑥；①—④、⑦⑧ 待本人确认后才可用「我们」口径（见 p3/qa-signoff.md）。",
     10, False, MUTED, first=True, after=0)

notes(s, "提问环节用。只引用，不逐条念。①② 的最新口径以 CP1 为准（19 篇 / 4 篇核验）。")

# ============ B2 · backup 9 篇分类总表 ============
s = blank(prs)
header(s, "BACKUP 2", "9 篇核心样本 · 五轴分类总表", 8)

rows = [
    ["论文", "A 主值（次）", "B 信号", "C 算子", "D 保证", "E 暂定"],
    ["STOP", "code（prompt/context）", "external-verifier", "refine+evolutionary", "empirical", "iterative"],
    ["ADAS", "control-flow（code）", "external-verifier", "evolutionary", "empirical", "待精读"],
    ["DGM", "code（tool/prompt/context）", "external-verifier", "evolutionary", "empirical", "full-rsi"],
    ["AlphaEvolve", "code（任务算法）", "external-verifier", "evolutionary", "empirical", "待精读"],
    ["RHO", "tool（memory/prompt）", "self-preference", "textual-gradient", "empirical", "one-shot"],
    ["SEVerA", "code（control-flow）", "external-verifier（形式化）", "tree-search+meta-opt", "formal-safety", "待精读"],
    ["Harness≠Benefit", "memory（prompt）", "failure-trajectory", "refine（沿用）", "none（测量）", "待精读"],
    ["SICA", "code（tool/prompt）", "external-verifier", "refine", "empirical", "full-rsi 候选"],
    ["MGM", "code", "failure-trajectory", "evolutionary", "empirical", "待精读"],
]
add_table(s, 0.45, 1.12, rows, [1.55, 2.95, 3.05, 2.55, 1.35, 0.95],
          row_h=0.46, body_size=10, header_size=10.5)

tf = textbox(s, 0.45, 6.15, 12.4, 0.8)
para(tf, "计数（主值）：A = code 6 / control-flow 1 / tool 1 / memory 1｜B = external 6 / failure 2 / self 1｜D = empirical 7 / formal-safety 1 / none 1｜E = one-shot 1 / iterative 1 / full-rsi 1（+1 候选）/ co-evolution 0 / 待精读 5",
     10, False, INK, first=True, after=3, spacing=1.1)
para(tf, "来源：p2/classification.md §1。DGM 与 AlphaEvolve 的 A–D 已回原文核对，其余 7 篇据 skim 卡待精读复核。",
     9.5, False, MUTED, after=0)

notes(s, "提问环节用。只讲三个点：code 6/9、E 轴 3+1+5、co-evolution 为 0。")

prs.core_properties.title = "Harness 自进化：共识在改什么，分歧在递归到哪层"
prs.core_properties.author = "P3（szh）"
prs.core_properties.subject = "RSI 专题中期汇报（5 分钟）"
prs.save(OUT)
print(f"saved: {OUT} ({len(prs.slides._sldIdLst)} slides)")
