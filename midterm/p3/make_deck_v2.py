# -*- coding: utf-8 -*-
"""Rebuilt midterm deck: 7 content slides + 3 backup (5 min / 280 s).

Structure:
  P1 claim  P2 scope & sample  P3 taxonomy map  P4 evidence 1 (A axis)
  P5 evidence 2 (E axis)  P6 evidence 3 + 3 checks  P7 plan
  B1 Q&A  B2 five-axis table  B3 search/venue/numbers

Run: python make_deck_v2.py
Out: RSI-Harness-中期汇报-2026-11-02.pptx
"""
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent
IMG = HERE / "taxonomy-ae-clean.png"
OUT = HERE / "RSI-Harness-中期汇报-2026-11-02.pptx"

FONT = "Microsoft YaHei"
NAVY = RGBColor(0x12, 0x25, 0x3A)
NAVY2 = RGBColor(0x2C, 0x45, 0x60)
ACCENT = RGBColor(0xC2, 0x6A, 0x0B)
INK = RGBColor(0x1F, 0x29, 0x37)
MUTED = RGBColor(0x6B, 0x72, 0x80)
LINE = RGBColor(0xD8, 0xDD, 0xE4)
LIGHT = RGBColor(0xF4, 0xF5, 0xF7)
PALE = RGBColor(0xE9, 0xED, 0xF2)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PALE_BLUE = RGBColor(0x9A, 0xB0, 0xC6)
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


def rect(s, x, y, w, h, fill, line=None, line_w=0.75, rounded=True, radius=0.06):
    kind = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    shp = s.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
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
    if rounded:
        try:
            shp.adjustments[0] = radius
        except Exception:
            pass
    return shp


def textbox(s, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    box = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.0)
    tf.margin_top = tf.margin_bottom = Inches(0.0)
    tf.vertical_anchor = anchor
    return tf


def para(tf, text, size=14, bold=False, color=INK, before=0, after=0,
         first=False, align=PP_ALIGN.LEFT, spacing=1.12, italic=False):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(before)
    p.space_after = Pt(after)
    p.line_spacing = spacing
    run = p.add_run()
    run.text = text
    style_run(run, size, bold, color, italic)
    return p


def rich(tf, parts, size=14, first=False, align=PP_ALIGN.LEFT, spacing=1.12, after=0):
    """parts: list of (text, dict(size=..., bold=..., color=...))."""
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(0)
    p.space_after = Pt(after)
    p.line_spacing = spacing
    for text, opts in parts:
        run = p.add_run()
        run.text = text
        style_run(run, opts.get("size", size), opts.get("bold", False),
                  opts.get("color", INK), opts.get("italic", False))
    return p


def header(s, kicker, title, page):
    tf = textbox(s, 0.55, 0.30, 9.0, 0.28)
    para(tf, kicker, 10.5, True, ACCENT, first=True, after=0)
    tf = textbox(s, 0.55, 0.58, 12.25, 0.80)
    para(tf, title, 30, True, NAVY, first=True, after=0, spacing=1.0)
    # footer
    tf = textbox(s, 0.55, 7.12, 7.0, 0.24)
    para(tf, "RSI 中期汇报 · 2026-11-02", 9, False, MUTED, first=True, after=0)
    tf = textbox(s, 11.35, 7.12, 1.45, 0.24)
    para(tf, page, 9, False, MUTED, first=True, after=0, align=PP_ALIGN.RIGHT)


def add_table(s, x, y, data, col_widths, row_heights, header_row=True,
              body_size=12, header_size=11, zebra=True, bold_first=True,
              align_center_cols=()):
    rows, cols = len(data), len(data[0])
    width = sum(col_widths)
    height = sum(row_heights)
    shape = s.shapes.add_table(rows, cols, Inches(x), Inches(y), Inches(width), Inches(height))
    tbl = shape.table
    tbl.first_row = False
    tbl.horz_banding = False
    for i, cw in enumerate(col_widths):
        tbl.columns[i].width = Inches(cw)
    for r in range(rows):
        tbl.rows[r].height = Inches(row_heights[r])
        for c in range(cols):
            cell = tbl.cell(r, c)
            cell.margin_left = cell.margin_right = Inches(0.10)
            cell.margin_top = cell.margin_bottom = Inches(0.04)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            if header_row and r == 0:
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
            p.line_spacing = 1.05
            run = p.add_run()
            run.text = str(data[r][c])
            is_head = header_row and r == 0
            style_run(run, header_size if is_head else body_size,
                      bold=is_head or (bold_first and c == 0),
                      color=WHITE if is_head else INK)
    return tbl


def notes(s, text):
    s.notes_slide.notes_text_frame.text = text.strip()


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def small_label(s, x, y, text, size=10.5, color=MUTED, bold=True, w=5.0):
    tf = textbox(s, x, y, w, 0.26)
    para(tf, text, size, bold, color, first=True, after=0)


def stat(s, x, y, number, label, note="", number_size=46, number_color=NAVY):
    tf = textbox(s, x, y, 4.0, 0.78)
    para(tf, number, number_size, True, number_color, first=True, after=0, spacing=0.95)
    tf = textbox(s, x, y + 0.80, 4.0, 0.30)
    para(tf, label, 11.5, False, INK, first=True, after=0)
    if note:
        tf = textbox(s, x, y + 1.10, 4.0, 0.28)
        para(tf, note, 9.5, False, MUTED, first=True, after=0)


# ---------------------------------------------------------------- build
prs = Presentation()
prs.slide_width = Inches(W)
prs.slide_height = Inches(H)

# ================================================================ P1 cover
s = blank(prs)
rect(s, 0, 0, W, H, NAVY, rounded=False)

tf = textbox(s, 0.90, 0.95, 10.0, 0.30)
para(tf, "RECURSIVE SELF-IMPROVEMENT IN HARNESS  ·  中期汇报", 11, True,
     PALE_BLUE, first=True, after=0)

tf = textbox(s, 0.90, 1.45, 11.6, 1.75)
para(tf, "Harness 自进化：", 42, True, WHITE, first=True, after=2, spacing=1.05)
para(tf, "19 篇文献读出的共识与空白", 42, True, WHITE, after=0, spacing=1.05)

tf = textbox(s, 0.90, 3.12, 11.6, 0.32)
para(tf, "9 篇核心样本 · 19 篇入库 · 7 篇待精读", 12.5, False, RGBColor(0xC9, 0xD6, 0xE3),
     first=True, after=0)

rect(s, 0.90, 3.60, 11.55, 2.20, WHITE, rounded=True, radius=0.05)
tf = textbox(s, 1.15, 3.76, 11.05, 0.26)
para(tf, "核心结论", 10.5, True, ACCENT, first=True, after=0)
tf = textbox(s, 1.15, 4.06, 11.05, 1.60)
para(tf, "9 篇里 6 篇在改代码；去掉 2 篇不算 harness 的，还有 4 篇。", 15.0, True, NAVY,
     first=True, after=5, spacing=1.28)
para(tf, "只有 3 篇说清递归到哪层，5 篇作者没界定。", 15.0, True, NAVY,
     after=5, spacing=1.28)
para(tf, "形式化保证只有 SEVerA，自偏好只有 RHO；高递归 + 高保证，9 篇里一篇都没有。",
     15.0, True, NAVY, after=0, spacing=1.28)

tf = textbox(s, 0.90, 6.55, 11.5, 0.28)
para(tf, "汇报日 2026-11-02｜数据截至 2026-10-31", 10.5, False, PALE_BLUE,
     first=True, after=0)

notes(s, """
20 秒。先给结论，不介绍背景。
「先给结论。19 篇文献，我们挑出 9 篇做了分类。9 篇里 6 篇改的是代码，去掉两篇不算 harness 的还有 4 篇。但只有 3 篇说清楚自己递归到哪一层，剩下 5 篇作者没界定。保证这块，形式化只有 SEVerA，自偏好只有 RHO。高递归、高保证同时做到的一篇都没有。」

【论据】
- 19 篇入库、全部 skim、0 篇精读；9 篇 = 7 篇精读候选 + SICA、MGM。
- 6/9 是主 A 值：STOP、DGM、AlphaEvolve、SEVerA、SICA、MGM。扣掉 AlphaEvolve、SEVerA 后为 4/9。
- E 轴能落位 3 篇：STOP=iterative、DGM=full-rsi（仅代码层）、RHO=one-shot。
""")

# ================================================================ P2 scope
s = blank(prs)
header(s, "01 · 范围", "19 篇入库，9 篇进图", "2 / 7")

small_label(s, 0.55, 1.45, "只做最外层")

rect(s, 0.55, 1.80, 3.10, 1.00, LIGHT)
tf = textbox(s, 0.72, 1.92, 2.80, 0.34)
para(tf, "模型层", 14, True, NAVY, first=True, after=0)
tf = textbox(s, 0.72, 2.28, 2.80, 0.28)
para(tf, "改参数、改训练", 10.5, False, MUTED, first=True, after=0)

rect(s, 0.55, 2.92, 3.10, 1.00, LIGHT)
tf = textbox(s, 0.72, 3.04, 2.80, 0.34)
para(tf, "数据层", 14, True, NAVY, first=True, after=0)
tf = textbox(s, 0.72, 3.40, 2.80, 0.28)
para(tf, "改数据、改经验", 10.5, False, MUTED, first=True, after=0)

rect(s, 0.55, 4.04, 3.10, 1.42, NAVY)
tf = textbox(s, 0.72, 4.16, 2.80, 0.38)
para(tf, "Harness", 17, True, WHITE, first=True, after=0)
tf = textbox(s, 0.72, 4.56, 2.80, 0.50)
para(tf, "改架构、工具、控制流、上下文", 10.5, False, RGBColor(0xD5, 0xDF, 0xE9),
     first=True, after=0, spacing=1.15)
tf = textbox(s, 0.72, 5.04, 2.80, 0.28)
para(tf, "← 我们只做这层", 10.5, True, RGBColor(0xE8, 0xB4, 0x7A), first=True, after=0)

small_label(s, 3.95, 1.45, "样本")

rect(s, 3.95, 1.80, 4.35, 0.98, NAVY)
tf = textbox(s, 4.12, 1.90, 2.0, 0.48)
para(tf, "19 入库", 19, True, WHITE, first=True, after=0)
tf = textbox(s, 5.70, 2.03, 2.45, 0.28)
para(tf, "全部 skim", 9.5, False, RGBColor(0xD5, 0xDF, 0xE9), first=True, after=0,
     align=PP_ALIGN.RIGHT)

rect(s, 3.95, 2.98, 3.55, 0.98, NAVY2)
tf = textbox(s, 4.12, 3.08, 1.8, 0.48)
para(tf, "9 进图", 19, True, WHITE, first=True, after=0)
tf = textbox(s, 4.95, 3.21, 2.40, 0.28)
para(tf, "7 精读候选 + 2 补充", 9.0, False, RGBColor(0xD5, 0xDF, 0xE9),
     first=True, after=0, align=PP_ALIGN.RIGHT)

rect(s, 3.95, 4.16, 2.85, 0.98, ACCENT)
tf = textbox(s, 4.12, 4.26, 1.8, 0.48)
para(tf, "7 待精读", 19, True, WHITE, first=True, after=0)
tf = textbox(s, 5.05, 4.39, 1.60, 0.28)
para(tf, "2/2/2/1", 9.0, False, RGBColor(0xFA, 0xE6, 0xCF), first=True, after=0,
     align=PP_ALIGN.RIGHT)

small_label(s, 8.80, 1.45, "时效与可信度")
stat(s, 8.80, 1.85, "12/19", "是 2026 年的", "63% 的池子来自最近一年", 46, NAVY)
stat(s, 8.80, 3.35, "0/12", "有可核验的录用记录", "2026 年的 12 篇里", 46, ACCENT)
tf = textbox(s, 8.80, 4.85, 3.90, 0.55)
para(tf, "4/19 有录用：STOP、ADAS、DGM、Gao 综述。", 9.5, False, MUTED,
     first=True, after=0, spacing=1.12)

rect(s, 0.55, 5.72, 12.20, 0.66, LIGHT)
tf = textbox(s, 0.78, 5.82, 11.80, 0.50)
para(tf, "9 = 7 篇精读候选 + 2 篇补充（SICA、MGM）；n=9 有选择偏差，不外推。", 10.5,
     False, INK, first=True, after=0)

notes(s, """
35 秒。先划边界，再交样本。
「我们只做最外层。模型层改参数，数据层改数据，我们改的是把模型和数据组织起来的那个程序，也就是 harness。池子 19 篇，全部做了 skim；其中 9 篇进了图，7 篇是接下来的精读名单。19 篇里 12 篇是 2026 年的，但 2026 年这 12 篇，一篇都还没有可核验的录用记录。所以这个方向在加速，但说它已经站住，还早。」

【论据】
- 19 篇构成：seed 4、harness-core 7、industry 1、survey 7；综述占 37%，不进 evidence。
- 4 篇已核验：STOP=COLM 2024、ADAS=ICLR 2025、DGM=ICLR 2026、Gao 综述=TMLR 2026。
- 9 篇 = 7 篇精读名单 + SICA、MGM；n=9 有选择偏差，不能外推整个领域。
- 149→50→2 的检索漏斗在 B3，不在正文。
""")

# ================================================================ P3 map
s = blank(prs)
header(s, "02 · 分类", "一张图：横轴改什么，纵轴递归到哪层", "3 / 7")

tf = textbox(s, 0.55, 1.22, 12.2, 0.30)
rich(tf, [
    ("A 改什么", {"bold": True, "color": NAVY}),
    ("　｜　B 靠什么信号　｜　C 怎么搜　｜　D 有什么保证　｜　", {"color": MUTED}),
    ("E 递归到哪层", {"bold": True, "color": NAVY}),
], size=11, first=True)
tf = textbox(s, 0.55, 1.50, 12.2, 0.26)
para(tf, "这张图只画 A 和 E；B、C、D 在 B2 的表里。", 9.5, False, MUTED, first=True, after=0)

s.shapes.add_picture(str(IMG), Inches(0.45), Inches(1.82), width=Inches(8.30))

small_label(s, 9.05, 1.82, "读图三步")
steps = [
    ("1", "先看哪一列", "它改的是什么"),
    ("2", "再看哪一行", "作者自己说的递归深度"),
    ("3", "最后看灰带", "5 篇作者没说清，我们不替他们填"),
]
y = 2.22
for num, t, d in steps:
    tf = textbox(s, 9.05, y, 0.40, 0.40)
    para(tf, num, 18, True, ACCENT, first=True, after=0)
    tf = textbox(s, 9.48, y - 0.02, 3.30, 0.32)
    para(tf, t, 13, True, NAVY, first=True, after=0)
    tf = textbox(s, 9.48, y + 0.32, 3.30, 0.55)
    para(tf, d, 10.5, False, MUTED, first=True, after=0, spacing=1.12)
    y += 1.18

rect(s, 9.05, 5.85, 3.75, 0.74, LIGHT)
tf = textbox(s, 9.20, 5.94, 3.45, 0.58)
para(tf, "灰带 ≠ one-shot ≠ 低递归。它只表示：作者没说。", 9.5, False, INK,
     first=True, after=0, spacing=1.12)

tf = textbox(s, 0.55, 6.62, 8.10, 0.28)
para(tf, "点 = 一篇论文；橙 = 工业界 / 产学合作，蓝 = 学术界；菱形 = 补充样本。", 9.0,
     False, MUTED, first=True, after=0)

notes(s, """
60 秒。这一页只讲怎么读，不报结论数字。
「怎么看这 9 篇？我们用了五个轴，今天只画两个：横轴是改什么，纵轴是递归到哪一层。一个点一篇论文。最下面这条灰带，是 5 篇作者自己没说清楚递归到哪一层。我们没有替他们填，先放在灰带里。读的时候三步：先看哪一列，再看哪一行，最后看是不是在灰带里。」

【论据】
- 5 篇灰带：ADAS、AlphaEvolve、SEVerA、Harness≠Benefit、MGM；SICA 是 full-rsi 候选，单独标菱形。
- A 轴计数（主值）：code 6、control-flow 1（ADAS）、tool 1（RHO）、memory 1（Harness≠Benefit）。
- D 轴：empirical 7、formal-safety 1、none 1；B 轴：external 6、failure-trajectory 2、self-preference 1。
- 若问「为什么 AlphaEvolve 不算」：它的 prompt 模板、LLM ensemble、program database、evaluator 都是固定外壳。
- 若问「RHSI 呢」：作者自称 recursive / co-evolution，但明说只做了循环前半段，所以不填 co-evolution。
""")

# ================================================================ P4 evidence 1
s = blank(prs)
header(s, "03 · 证据 1", "6 篇改代码，4 篇改的是 harness 自己", "4 / 7")

tf = textbox(s, 0.55, 1.60, 2.55, 1.25)
para(tf, "6/9", 76, True, NAVY, first=True, after=0, spacing=0.95)
tf = textbox(s, 0.55, 2.82, 2.55, 0.30)
para(tf, "主值是 code", 13, True, MUTED, first=True, after=0)

tf = textbox(s, 3.10, 1.85, 0.85, 0.65)
para(tf, "→", 40, True, ACCENT, first=True, after=0, align=PP_ALIGN.CENTER)

tf = textbox(s, 3.95, 1.60, 2.55, 1.25)
para(tf, "4/9", 76, True, ACCENT, first=True, after=0, spacing=0.95)
tf = textbox(s, 3.95, 2.82, 2.55, 0.30)
para(tf, "扣掉 2 篇后", 13, True, MUTED, first=True, after=0)

small_label(s, 6.65, 1.55, "这 2 篇不算进来", 10.5, ACCENT)

tf = textbox(s, 6.65, 1.92, 6.10, 0.34)
para(tf, "AlphaEvolve 2025", 15, True, NAVY, first=True, after=0)
tf = textbox(s, 6.65, 2.28, 6.10, 0.30)
para(tf, "改的是任务算法，不是 harness。", 12, False, INK, first=True, after=0)

tf = textbox(s, 6.65, 2.78, 6.10, 0.34)
para(tf, "SEVerA 2026", 15, True, NAVY, first=True, after=0)
tf = textbox(s, 6.65, 3.14, 6.10, 0.30)
para(tf, "Learn 阶段改的是模型权重。", 12, False, INK, first=True, after=0)

tf = textbox(s, 6.65, 3.48, 6.10, 0.30)
rich(tf, [
    ("算进来的 4 篇：", {"bold": True, "color": MUTED}),
    ("STOP、DGM、SICA、MGM", {"color": INK}),
], size=11, first=True)

rect(s, 0.55, 4.55, 12.20, 1.15, LIGHT)
tf = textbox(s, 0.80, 4.74, 11.75, 0.80)
para(tf, "code 还是最大的一类；但改代码，不等于递归到哪一层。", 18, True, NAVY,
     first=True, after=0, spacing=1.10)

tf = textbox(s, 0.55, 6.08, 12.20, 0.45)
para(tf, "ADAS 的 A 值有 control-flow / code 两种读法；如果记成 code，会变成 7/9，精读时要定。",
     9.5, False, MUTED, first=True, after=0, spacing=1.10)

notes(s, """
40 秒。标题已经说了两个数字，讲的时候把「为什么扣」说清楚。
「第一件事，改什么。9 篇里 6 篇的主值是代码，这是最集中的一列。但这里面有 2 篇要单独说：AlphaEvolve 改的是任务算法，不是它自己；SEVerA 的 Learn 阶段改的是模型权重。把这两篇拿掉，还有 4 篇，代码仍然是最大的一类。所以『大家在改代码』这个判断成立；但改代码，不等于递归到哪一层。」

【论据】
- 6 篇主 A 值 = code：STOP、DGM、AlphaEvolve、SEVerA、SICA、MGM。
- 扣掉 AlphaEvolve（任务算法、pipeline 固定）与 SEVerA（Learn 用 GRPO 改权重）后为 4 篇。
- ADAS 的 A 值有 control-flow / code 两读；若记 code，主值会变成 7/9，说明 A 轴粒度要等精读复核。
""")

# ================================================================ P5 evidence 2
s = blank(prs)
header(s, "04 · 证据 2", "只有 3 篇说清了递归到哪层", "5 / 7")

# col 1
tf = textbox(s, 0.55, 1.55, 1.0, 0.80)
para(tf, "3", 44, True, NAVY, first=True, after=0, spacing=0.95)
small_label(s, 1.45, 1.62, "说清", 11, MUTED, True, 2.0)
items1 = [
    ("STOP", "iterative"),
    ("DGM", "full-rsi（只在代码层）"),
    ("RHO", "one-shot"),
]
y = 2.55
for name, val in items1:
    tf = textbox(s, 0.55, y, 3.60, 0.30)
    para(tf, name, 14, True, NAVY, first=True, after=0)
    tf = textbox(s, 0.55, y + 0.30, 3.60, 0.30)
    para(tf, val, 11, False, INK, first=True, after=0)
    y += 0.82

# col 2
tf = textbox(s, 4.55, 1.55, 1.0, 0.80)
para(tf, "1", 44, True, NAVY, first=True, after=0, spacing=0.95)
small_label(s, 5.45, 1.62, "候选", 11, MUTED, True, 2.0)
tf = textbox(s, 4.55, 2.55, 3.30, 0.30)
para(tf, "SICA", 14, True, NAVY, first=True, after=0)
tf = textbox(s, 4.55, 2.85, 3.30, 0.60)
para(tf, "自称 fully self-improving，等精读再定。", 11, False, INK,
     first=True, after=0, spacing=1.12)

# col 3
tf = textbox(s, 8.15, 1.55, 1.0, 0.80)
para(tf, "5", 44, True, MUTED, first=True, after=0, spacing=0.95)
small_label(s, 9.05, 1.62, "没说", 11, MUTED, True, 2.0)
names = ["ADAS", "AlphaEvolve", "SEVerA", "Harness≠Benefit", "MGM"]
y = 2.55
for name in names:
    tf = textbox(s, 8.15, y, 4.55, 0.30)
    para(tf, name, 12.5, False, INK, first=True, after=0)
    y += 0.40

rect(s, 0.55, 5.55, 12.20, 0.92, NAVY)
tf = textbox(s, 0.80, 5.66, 11.75, 0.72)
rich(tf, [
    ("co-evolution：0 篇确认", {"size": 24, "bold": True, "color": WHITE}),
    ("     0 是「没人确认」，不是「没人做」", {"size": 11, "color": RGBColor(0xE8, 0xB4, 0x7A)}),
], size=24, first=True, spacing=1.0)

tf = textbox(s, 0.55, 6.62, 12.20, 0.32)
para(tf, "RHSI 自称 co-evolution，但作者说只做完了循环的前半段，所以没算。", 9.5,
     False, MUTED, first=True, after=0)

notes(s, """
40 秒。把「3 + 1 + 5」说清，重点在「0 是没人确认」。
「第二件事，递归到哪一层。只有 3 篇能对上号：STOP 是 iterative，DGM 是 full-rsi 但只在代码层，RHO 是 one-shot。SICA 自称 fully self-improving，我们先记候选。剩下 5 篇，作者没界定，我们不替他们填。所以 co-evolution 现在只能写 0 篇确认，不能写『领域里没有』。RHSI 说自己 co-evolution，但只做完了前半段，我们没算。」

【论据】
- 作者原话：STOP「this is not full recursive self-improvement.」；DGM「iteratively modifies its own code…」；RHO「We evaluated a single retrospective optimization round…」。
- 5 篇未界定：ADAS、AlphaEvolve、SEVerA、Harness≠Benefit、MGM。
- RHSI = arxiv-2607.15524；作者自述只完成递归循环前半段。
""")

# ================================================================ P6 evidence 3
s = blank(prs)
header(s, "05 · 证据 3 与争议", "能更新，不等于有收益", "6 / 7")

rows = [
    ["问题", "现在看到什么", "什么能推翻我们"],
    ["收益", "9 篇里，把选择偏差、验证集过拟合、基准污染拆开报的，我们没找到。",
     "7 篇里若有 hold-out、有尝试次数、增益能复现。"],
    ["验证器", "形式化只有 SEVerA，而且它不管 token / 时间；自偏好只有 RHO，作者自己说最偏好的 0.78 不是最高的 0.85。",
     "两者在无标注部署下都成立。"],
    ["成本", "DGM $22k / 2 周；SICA 15 轮约 $7k；AlphaEvolve 约 100 compute-hours / 次；RHO 103 / 41 / 320 agent calls。四种单位，没法直接比。",
     "同一单位报完整成本，增益还在。"],
]
add_table(s, 0.55, 1.55, rows, [1.70, 6.20, 4.30], [0.45, 1.30, 1.42, 1.42],
          body_size=12.5, header_size=11, align_center_cols=())

rect(s, 0.55, 6.15, 12.20, 0.62, LIGHT)
tf = textbox(s, 0.80, 6.25, 11.75, 0.42)
para(tf, "这三条，就是 7 篇精读的检查表。", 16, True, NAVY, first=True, after=0)

notes(s, """
55 秒。三条按「收益、验证器、成本」讲，每条一句事实 + 一句什么能推翻。
「第三件事，凭什么信。我们看三个地方。第一，收益：9 篇里，把选择偏差、验证集过拟合、基准污染拆开报的，我们没找到。第二，验证器：形式化只有 SEVerA，它自己说不管 token 和时间；自偏好只有 RHO，作者自己报告最偏好的 0.78 不是最高的 0.85。第三，成本：DGM 报美元，SICA 报轮次，AlphaEvolve 报 compute-hours，RHO 报 agent calls，四种单位，没法直接比。这三条，就是 7 篇精读要查的清单。」

【论据】
- 收益：Harness≠Benefit（arxiv-2605.30621）主张把「更新」与「收益」解耦；增益可能来自选择偏差、验证集过拟合、基准污染。
- 验证器：RHO 的机制保证「不劣于基线」，不是验证独立；作者自报最偏好 0.78、测试最高 0.85。SEVerA 的 Theorem 5.4 只覆盖功能规格，作者自陈 resource-unaware。
- 成本：DGM 约 $22,000 / 2 周（baseline 各约 $10,000）；SICA 15 轮约 $7,000；AlphaEvolve 约 100 compute-hours / 次；RHO 103 vs 41（1 轮）/ 320（10 轮）agent calls。
""")

# ================================================================ P7 plan
s = blank(prs)
header(s, "06 · 计划", "接下来两周：7 篇精读，回答 3 个问题", "7 / 7")

small_label(s, 0.55, 1.45, "7 篇，2/2/2/1")
plan = [
    ["人", "论文"],
    ["P1", "STOP、ADAS"],
    ["P2", "DGM、AlphaEvolve"],
    ["P3", "RHO、SEVerA"],
    ["P4", "Harness≠Benefit"],
]
add_table(s, 0.55, 1.78, plan, [0.72, 3.05], [0.42, 0.44, 0.44, 0.44, 0.44],
          body_size=11.5, header_size=10.5, align_center_cols=(0,))

small_label(s, 4.85, 1.45, "3 个问题", 10.5, MUTED, True, 5.0)
qs = [
    "co-evolution 是没做出来，还是做不出来？",
    "自偏好能不能和独立评测共存？",
    "形式化保证能不能覆盖 token 和时间预算？",
]
y = 1.82
for i, q in enumerate(qs):
    tf = textbox(s, 4.85, y + 0.04, 0.45, 0.30)
    para(tf, f"0{i + 1}", 10, True, ACCENT, first=True, after=0)
    tf = textbox(s, 5.30, y, 7.40, 0.34)
    para(tf, q, 14, True, NAVY, first=True, after=0)
    y += 0.70

small_label(s, 4.85, 4.25, "两周排期", 10.5, MUTED, True, 5.0)
rect(s, 4.95, 4.98, 7.55, 0.02, LINE, rounded=False)
phases = [
    (4.95, "D1–D7", "七篇草稿"),
    (6.85, "D8–D9", "补附录和成本"),
    (8.75, "D10–D11", "交叉核对"),
    (10.65, "D12–D14", "定稿"),
]
for x, d, t in phases:
    shp = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x), Inches(4.91), Inches(0.15), Inches(0.15))
    shp.fill.solid()
    shp.fill.fore_color.rgb = ACCENT if d == "D12–D14" else NAVY
    shp.line.fill.background()
    shp.shadow.inherit = False
    tf = textbox(s, x - 0.02, 4.52, 1.75, 0.28)
    para(tf, d, 10.5, True, NAVY, first=True, after=0)
    tf = textbox(s, x - 0.02, 5.12, 1.75, 0.28)
    para(tf, t, 9.5, False, INK, first=True, after=0)

tf = textbox(s, 0.55, 6.52, 9.60, 0.30)
para(tf, "风险：R1 venue、R4 种子综述已关闭；R2 成本、R3 复现仍开放。", 9.5,
     False, MUTED, first=True, after=0)
tf = textbox(s, 10.30, 6.48, 2.45, 0.32)
para(tf, "谢谢 · 讨论", 11.5, True, NAVY, first=True, after=0, align=PP_ALIGN.RIGHT)

notes(s, """
30 秒。收尾要快。
「接下来两周，7 篇，二二二一。第一周出 7 篇 Schema 草稿；第二周补附录和成本，交叉核对，最后定稿。要回答三个问题：co-evolution 是没做出来，还是根本做不出来；自偏好能不能和独立评测共存；形式化保证能不能覆盖 token 和时间预算。风险这块，venue 和两篇种子综述已经关了，成本和复现还开着。谢谢。」

【论据】
- 分工：P1 STOP / ADAS；P2 DGM / AlphaEvolve；P3 RHO / SEVerA；P4 Harness≠Benefit。
- R1 关闭：4/19 有可追溯录用来源；R4 关闭：两篇指定综述已入库（19 篇、19 张 skim）。
- R2 仍开放：STOP 只有渐近预算；AlphaEvolve 缺整轮总成本；DGM/RHO/SEVerA 粒度不同。R3 仍开放：多数依赖闭源模型或历史 API。
""")

# ================================================================ B1 Q&A
s = blank(prs)
header(s, "BACKUP · B1", "8 条 Q&A 速查", "B1")

qa = [
    ["问题", "回答要点", "人"],
    ["① 七篇怎么选？", "覆盖经典 / 自修改 / 工业 / 自偏好 / 形式化 + 一篇测量研究；同行评审项已由 STOP / ADAS / DGM 满足。", "P1"],
    ["② 读到哪一步？", "19 篇 skim、0 篇精读；中期交的是地图、判断与计划，七篇是精读名单。", "P1"],
    ["③ 多轮为何不算 full RSI？", "只看改进后的系统参与什么：搜产物 vs 改下一轮的程序；作者未界定就记待核实。", "P2"],
    ["④ AlphaEvolve 为何选？", "工业级的「强外部 evaluator + 进化搜索」对照；pipeline 固定，不改 harness。", "P2"],
    ["⑤ 自偏好会自说自话？", "有风险：最偏好 0.78 ≠ 最高 0.85；它保证不劣于基线，不是验证独立。", "P3"],
    ["⑥ SEVerA 是否已安全？", "只覆盖给定规格下的功能正确；作者自陈不含 token / 时间；Learn 还改权重。", "P3"],
    ["⑦ 能更新 ≠ 有收益？", "生成端与使用端是两种能力；增益不随基础能力单调增长，弱模型可能不加载更新。", "P4"],
    ["⑧ 两周交什么？", "7 篇完整 Schema + 方法比较 + 3 条证据 + 2–3 争议；缺成本不作效率结论。", "P4"],
]
add_table(s, 0.50, 1.42, qa, [3.00, 8.20, 0.95], [0.42] + [0.58] * 8,
          body_size=9.8, header_size=10, align_center_cols=(2,))
notes(s, "提问环节用。只引用，不逐条念。①② 的最新口径以 CP1 为准（19 篇 / 4 篇核验）。")

# ================================================================ B2 five-axis
s = blank(prs)
header(s, "BACKUP · B2", "9 篇核心样本 · 五轴总表", "B2")

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
add_table(s, 0.45, 1.30, rows, [1.55, 2.95, 3.05, 2.55, 1.35, 0.95],
          [0.40] + [0.43] * 9, body_size=9.2, header_size=9.8)
tf = textbox(s, 0.45, 5.95, 12.4, 0.95)
para(tf, "计数（主值）：A = code 6 / control-flow 1 / tool 1 / memory 1｜B = external 6 / failure 2 / self 1｜"
         "D = empirical 7 / formal-safety 1 / none 1｜E = one-shot 1 / iterative 1 / full-rsi 1（+1 候选）/ "
         "co-evolution 0 / 待精读 5", 9.2, False, INK, first=True, after=3, spacing=1.12)
para(tf, "来源：P2 五轴分类总表。DGM 与 AlphaEvolve 的 A–D 已回原文核对，其余 7 篇据 skim 卡待精读复核。",
     8.8, False, MUTED, after=0)
notes(s, "提问环节用。只讲三个点：code 6/9、E 轴 3+1+5、co-evolution 为 0。")

# ================================================================ B3 sources
s = blank(prs)
header(s, "BACKUP · B3", "检索、录用与数字出处", "B3")

small_label(s, 0.55, 1.35, "检索与纳入", 10.5, MUTED, True, 5.0)
funnel = [
    ["步骤", "数量"],
    ["检索命中", "149"],
    ["标题筛查", "约 50"],
    ["新增入库", "2"],
    ["池", "19"],
    ["skim", "19"],
    ["精读候选", "7"],
    ["已精读", "0"],
]
add_table(s, 0.55, 1.70, funnel, [2.60, 1.40], [0.40] + [0.42] * 7,
          body_size=10, header_size=9.8, align_center_cols=(1,))

small_label(s, 6.10, 1.35, "4 篇有可核验录用", 10.5, MUTED, True, 5.0)
venue = [
    ["论文", "录用"],
    ["STOP", "COLM 2024"],
    ["ADAS", "ICLR 2025"],
    ["DGM", "ICLR 2026"],
    ["Gao 综述", "TMLR 2026"],
]
add_table(s, 6.10, 1.70, venue, [2.30, 2.20], [0.38] + [0.38] * 4,
          body_size=10, header_size=9.8)

small_label(s, 6.10, 3.82, "关键数字", 10.5, MUTED, True, 5.0)
nums = [
    ("19", "入库；19 张 skim；0 篇精读"),
    ("12/19", "出自 2026（63%）；0/12 有录用"),
    ("9", "核心样本 = 7 篇精读候选 + SICA、MGM"),
    ("6/9 → 4/9", "主值 code；扣掉 AlphaEvolve、SEVerA"),
    ("3 + 1 + 5", "E 轴说清 / 候选 / 未界定"),
    ("0 / 0 / 0", "co-evolution / evaluator / context"),
    ("$22k / 2 周", "DGM；SICA 15 轮约 $7k"),
    ("0.78 vs 0.85", "RHO 最偏好 vs 测试最高"),
]
y = 4.16
for n, d in nums:
    tf = textbox(s, 6.10, y, 1.55, 0.26)
    para(tf, n, 10.5, True, ACCENT, first=True, after=0)
    tf = textbox(s, 7.70, y, 4.70, 0.26)
    para(tf, d, 9.5, False, INK, first=True, after=0)
    y += 0.31

tf = textbox(s, 0.55, 6.55, 12.2, 0.30)
para(tf, "来源：refs/verified.csv、p1/stats.md、p1/funnel.md、p2/classification.md、notes/skim/。",
     8.8, False, MUTED, first=True, after=0)

notes(s, "提问环节用。149 是查询命中数，不是阅读数；4 篇 venue 只写这四篇。")

prs.core_properties.title = "Harness 自进化：19 篇文献读出的共识与空白"
prs.core_properties.author = "P3（szh）"
prs.core_properties.subject = "RSI 专题中期汇报"
prs.save(OUT)
print(f"saved: {OUT} ({len(prs.slides._sldIdLst)} slides)")
