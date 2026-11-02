# -*- coding: utf-8 -*-
"""Clean A×E figure for the rebuilt midterm deck.

Differences from p2/make_taxonomy_ae.py:
- no figure title, no right-hand notes panel, no long per-point notes
- larger labels (designed to be placed 8.8 in wide on a 13.33 in slide)
- same data/positions as the p2 figure

Run: python make_taxonomy_clean.py
Out: taxonomy-ae-clean.png (300 dpi)
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "Noto Sans SC", "SimHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False

INDUSTRY = "#C26A0B"
ACADEMIA = "#3F6FA8"
INK = "#1F2937"
MUTED = "#6B7280"
GRID = "#D8DDE4"
BAND = "#F3F4F6"
STRIP = "#ECEEF1"

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

# Same positions as p2/make_taxonomy_ae.py; only the label offsets changed
# because labels are now one line.
PAPERS = [
    dict(key="STOP", label="STOP 2023", a=2.00, e="iterative", industry=True,
         marker="o", dx=-10, dy=10, ha="right", va="bottom"),
    dict(key="ADAS", label="ADAS 2024", a=1.00, e="pending", industry=False,
         marker="o", dx=0, dy=-17, ha="center", va="top", fs=9.4),
    dict(key="DGM", label="DGM 2025", a=2.00, e="full-rsi", industry=True,
         marker="o", dx=-10, dy=10, ha="right", va="bottom"),
    dict(key="AlphaEvolve", label="AlphaEvolve 2025", a=1.76, e="pending", industry=True,
         marker="o", dx=-8, dy=14, ha="right", va="bottom", fs=9.4),
    dict(key="RHO", label="RHO 2026", a=3.00, e="one-shot", industry=True,
         marker="o", dx=11, dy=0, ha="left", va="center"),
    dict(key="SEVerA", label="SEVerA 2026", a=2.00, e="pending", industry=True,
         marker="o", dx=0, dy=-17, ha="center", va="top", fs=9.4),
    dict(key="HarnessBenefit", label="Harness≠Benefit 2026", a=4.00, e="pending",
         industry=True, marker="o", dx=0, dy=14, ha="center", va="bottom", fs=9.4),
    dict(key="SICA", label="SICA 2025（候选）", a=2.30, e="full-rsi", industry=True,
         marker="D", dx=11, dy=0, ha="left", va="center"),
    dict(key="MGM", label="MGM 2026", a=2.24, e="pending", industry=False,
         marker="D", dx=11, dy=14, ha="left", va="bottom", fs=9.4),
]


def y_of(p):
    return STRIP_Y if p["e"] == "pending" else E_LEVELS[p["e"]]


def main():
    fig = plt.figure(figsize=(8.8, 4.9), facecolor="white")
    ax = fig.add_axes([0.195, 0.16, 0.785, 0.80])

    ax.set_xlim(-0.6, 6.6)
    ax.set_ylim(-1.78, 4.10)
    ax.set_axisbelow(True)

    for i in range(7):
        ax.axvspan(i - 0.5, i + 0.5, color=BAND if i % 2 == 0 else "white", zorder=0)
        if i:
            ax.axvline(i - 0.5, color=GRID, lw=0.6, zorder=1)
    for y in E_LEVELS.values():
        ax.axhline(y, color=GRID, lw=0.8, ls=":", zorder=1)

    ax.axhspan(-1.16, -0.15, color=STRIP, zorder=0)
    ax.axhline(-0.15, color="#8C8C8C", lw=1.0, ls=(0, (4, 3)), zorder=2)

    for p in PAPERS:
        x, y = p["a"], y_of(p)
        color = INDUSTRY if p["industry"] else ACADEMIA
        size = 150 if p["marker"] == "o" else 120
        ax.scatter([x], [y], s=size, marker=p["marker"], facecolor=color,
                   edgecolor=INK, linewidth=1.1, zorder=6)
        ax.annotate(p["label"], xy=(x, y), xytext=(p["dx"], p["dy"]),
                    textcoords="offset points", ha=p["ha"], va=p["va"],
                    fontsize=p.get("fs", 10.2), color=INK, zorder=8,
                    bbox=dict(facecolor="white", edgecolor="none", alpha=0.82, pad=0.6))

    ax.set_xticks(range(7))
    ax.set_xticklabels([f"{name}\n({count})" for name, count in A_LABELS],
                       fontsize=10.2, linespacing=1.25, color=INK)
    ax.set_yticks([E_LEVELS["one-shot"], E_LEVELS["iterative"],
                   E_LEVELS["full-rsi"], E_LEVELS["co-evolution"], STRIP_Y])
    ax.set_yticklabels([
        "one-shot（1）",
        "iterative（1）",
        "full-rsi（1+1 候选）",
        "co-evolution（0）",
        "待精读（5）\nE 未界定",
    ], fontsize=10.2, linespacing=1.25, color=INK)
    ax.tick_params(axis="both", length=0, pad=7)

    ax.set_xlabel("A 改进对象（主值；括号内为 9 篇中的计数）", fontsize=10.5, labelpad=9, color=INK)
    ax.text(-0.55, 3.98, "E 递归深度 ↑", fontsize=10.5, fontweight="bold",
            ha="left", va="top", color=INK)

    # Compact legend in the empty top-right area.
    lx, ly = 4.42, 3.62
    ax.scatter([lx], [ly], s=70, marker="o", facecolor=INDUSTRY, edgecolor=INK,
               linewidth=1.0, zorder=9)
    ax.text(lx + 0.14, ly, "工业界 / 产学合作", fontsize=8.8, va="center", color=INK)
    ax.scatter([lx], [ly - 0.30], s=70, marker="o", facecolor=ACADEMIA, edgecolor=INK,
               linewidth=1.0, zorder=9)
    ax.text(lx + 0.14, ly - 0.30, "学术界", fontsize=8.8, va="center", color=INK)
    ax.scatter([lx], [ly - 0.60], s=60, marker="D", facecolor="white", edgecolor=INK,
               linewidth=1.0, zorder=9)
    ax.text(lx + 0.14, ly - 0.60, "补充样本", fontsize=8.8, va="center", color=INK)

    out = Path(__file__).resolve().parent
    fig.savefig(out / "taxonomy-ae-clean.png", dpi=300, facecolor="white",
                bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    print(f"wrote {out / 'taxonomy-ae-clean.png'}")


if __name__ == "__main__":
    main()
