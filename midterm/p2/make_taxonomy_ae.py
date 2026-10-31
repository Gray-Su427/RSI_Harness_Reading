# -*- coding: utf-8 -*-
"""Generate the A x E taxonomy figure for the P2 midterm package.

Data source: midterm/p2/classification.md (CP2 working draft, 2026-10-31).
Run: python make_taxonomy_ae.py
Outputs: taxonomy-ae.png (300 dpi) and taxonomy-ae.svg (text as paths).
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "Noto Sans SC", "SimHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["svg.fonttype"] = "path"

INDUSTRY = "#D9773B"
ACADEMIA = "#3F6FA8"
INK = "#222222"
MUTED = "#666666"
GRID = "#D9D9D9"
BAND = "#F7F7F7"
STRIP = "#EDEDED"

A_LABELS = [
    ("prompt", "0"),
    ("control-flow", "1"),
    ("code", "6"),
    ("tool", "1"),
    ("memory", "1"),
    ("evaluator", "0"),
    ("context", "0"),
]
E_LEVELS = {"one-shot": 0.4, "iterative": 1.4, "full-rsi": 2.4, "co-evolution": 3.4}
STRIP_Y = -0.65

# a: x position; e: E level or "pending"; marker: o=7 core, D=2 supplement.
PAPERS = [
    dict(key="STOP", label="STOP 2023", a=2.00, e="iterative", industry=True,
         marker="o", dashed=False, dx=-14, dy=10, ha="right", va="bottom",
         note="作者：not full RSI"),
    dict(key="ADAS", label="ADAS 2024", a=1.00, e="pending", industry=False,
         marker="o", dashed=True, dx=0, dy=-24, ha="center", va="top",
         note="meta-agent 固定"),
    dict(key="DGM", label="DGM 2025 ★", a=2.00, e="full-rsi", industry=True,
         marker="o", dashed=False, dx=-16, dy=10, ha="right", va="bottom",
         note="唯一明确 full-rsi"),
    dict(key="AlphaEvolve", label="AlphaEvolve 2025", a=1.76, e="pending", industry=True,
         marker="o", dashed=True, dx=-10, dy=18, ha="right", va="bottom",
         note="边界：任务算法"),
    dict(key="RHO", label="RHO 2026", a=3.00, e="one-shot", industry=True,
         marker="o", dashed=False, dx=16, dy=8, ha="left", va="bottom",
         note="单轮；self-preference"),
    dict(key="SEVerA", label="SEVerA 2026", a=2.00, e="pending", industry=True,
         marker="o", dashed=True, dx=0, dy=-24, ha="center", va="top",
         note="未界定；跨界"),
    dict(key="HarnessBenefit", label="Harness≠Benefit 2026", a=4.00, e="pending", industry=True,
         marker="o", dashed=True, dx=0, dy=24, ha="center", va="bottom",
         note="测量研究"),
    dict(key="SICA", label="SICA 2025", a=2.30, e="full-rsi", industry=True,
         marker="D", dashed=True, dx=18, dy=-14, ha="left", va="top",
         note="full-rsi 候选（待裁定）"),
    dict(key="MGM", label="MGM 2026", a=2.24, e="pending", industry=False,
         marker="D", dashed=True, dx=16, dy=14, ha="left", va="bottom",
         note="标题 recursive；未界定"),
]


def y_of(paper):
    return STRIP_Y if paper["e"] == "pending" else E_LEVELS[paper["e"]]


def main():
    fig = plt.figure(figsize=(16, 9), facecolor="white")
    ax = fig.add_axes([0.080, 0.09, 0.650, 0.80])
    panel = fig.add_axes([0.745, 0.09, 0.235, 0.80])
    panel.axis("off")
    panel.set_xlim(0, 1)
    panel.set_ylim(0, 1)

    ax.set_xlim(-0.6, 6.6)
    ax.set_ylim(-1.72, 4.08)
    ax.set_axisbelow(True)

    # Category bands + grid.
    for i in range(7):
        ax.axvspan(i - 0.5, i + 0.5, color=BAND if i % 2 == 0 else "white", zorder=0)
        if i:
            ax.axvline(i - 0.5, color=GRID, lw=0.6, zorder=1)
    for y in E_LEVELS.values():
        ax.axhline(y, color=GRID, lw=0.8, ls=":", zorder=1)

    # Bottom "pending" strip.
    ax.axhspan(-1.14, -0.15, color=STRIP, zorder=0)
    ax.axhline(-0.15, color="#8C8C8C", lw=1.0, ls=(0, (4, 3)), zorder=2)

    # Points.
    for p in PAPERS:
        x, y = p["a"], y_of(p)
        color = INDUSTRY if p["industry"] else ACADEMIA
        size = 290 if p["marker"] == "o" else 240
        ax.scatter([x], [y], s=size, marker=p["marker"], facecolor=color,
                   edgecolor=INK, linewidth=1.5, zorder=6)
        if p["dashed"]:
            ax.scatter([x], [y], s=size + 110, marker=p["marker"], facecolor="none",
                       edgecolor=INK, linewidth=1.1, linestyle="--", zorder=7)
        label = f"{p['label']}\n{p['note']}"
        ax.annotate(label, xy=(x, y), xytext=(p["dx"], p["dy"]),
                    textcoords="offset points", ha=p["ha"], va=p["va"],
                    fontsize=7.8, linespacing=1.15, color=INK, zorder=8)

    # Axis ticks.
    ax.set_xticks(range(7))
    ax.set_xticklabels([f"{name}\n({count})" for name, count in A_LABELS],
                       fontsize=9, linespacing=1.2)
    ax.set_yticks([E_LEVELS["one-shot"], E_LEVELS["iterative"],
                   E_LEVELS["full-rsi"], E_LEVELS["co-evolution"], STRIP_Y])
    ax.set_yticklabels([
        "one-shot（1）",
        "iterative（1）",
        "full-rsi（1 + 1 候选）",
        "co-evolution（0）",
        "待精读（5）\nE 未界定",
    ], fontsize=9, linespacing=1.2)
    ax.tick_params(axis="both", length=0, pad=8)

    ax.set_xlabel("A 改进对象（主值；括号内为 9 篇中的计数）", fontsize=10, labelpad=12)
    ax.text(-0.55, 3.96, "E 递归深度 ↑", fontsize=10, fontweight="bold",
            ha="left", va="top", color=INK)

    # Titles.
    fig.text(0.055, 0.955, "图 1 · Harness 自进化的 A×E 体系图",
             fontsize=17, fontweight="bold", ha="left", va="top", color=INK)
    fig.text(0.055, 0.915,
             "CP2 工作稿 · 2026-10-31 · 点=论文主 A 值；E 未找到作者界定者置于底部「待精读」带，不按 one-shot 处理",
             fontsize=9.5, ha="left", va="top", color=MUTED)

    # Right panel: legend + reading notes.
    panel.text(0.0, 0.98, "图例", fontsize=12, fontweight="bold", va="top", color=INK)
    legend_rows = [
        (INDUSTRY, "o", "工业界 / 产学合作（industry=true）"),
        (ACADEMIA, "o", "学术界（industry=false）"),
        ("white", "o", "7 篇精读候选（圆）"),
        ("white", "D", "2 篇泛读补充（菱）"),
    ]
    y = 0.91
    for color, marker, text in legend_rows:
        panel.scatter([0.04], [y], s=80, marker=marker, facecolor=color,
                      edgecolor=INK, linewidth=1.2, transform=panel.transAxes, clip_on=False)
        panel.text(0.12, y, text, fontsize=8.4, va="center", color=INK)
        y -= 0.065
    panel.plot([0.02, 0.08], [y, y], color=INK, lw=1.5, transform=panel.transAxes, clip_on=False)
    panel.text(0.12, y, "实线：作者明确界定 E", fontsize=8.4, va="center", color=INK)
    y -= 0.055
    panel.plot([0.02, 0.08], [y, y], color=INK, lw=1.2, ls="--", transform=panel.transAxes, clip_on=False)
    panel.text(0.12, y, "虚线：待精读 / 边界 / 候选", fontsize=8.4, va="center", color=INK)

    panel.text(0.0, 0.56, "读图（n=9）", fontsize=11, fontweight="bold", va="top", color=INK)
    notes = [
        "A 轴：code 6/9；evaluator、context 为 0。",
        "E 轴：明确界定 3 篇（STOP、DGM、RHO）",
        "＋ 候选 1 篇（SICA）；待精读 5 篇。",
        "空白：co-evolution 0；formal-safety 仅 SEVerA。",
        "边界：AlphaEvolve 改任务算法；SEVerA 改权重；",
        "Harness≠Benefit 是测量研究。",
    ]
    y = 0.49
    for line in notes:
        panel.text(0.0, y, line, fontsize=8.0, va="top", color=INK)
        y -= 0.058

    panel.text(0.0, 0.10,
               "本组判断：改什么已有共识（code），\n递归到哪层还没有。",
               fontsize=9.2, fontweight="bold", va="bottom", color=INK, linespacing=1.4)
    panel.text(0.0, 0.02,
               "数据：refs/verified.csv + notes/skim/；\nE 轴原话见 classification.md §3。",
               fontsize=7.0, va="bottom", color=MUTED, linespacing=1.3)

    out = Path(__file__).resolve().parent
    fig.savefig(out / "taxonomy-ae.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(out / "taxonomy-ae.svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {out / 'taxonomy-ae.png'}")
    print(f"wrote {out / 'taxonomy-ae.svg'}")


if __name__ == "__main__":
    main()
