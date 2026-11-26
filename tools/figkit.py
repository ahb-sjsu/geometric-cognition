"""Shared pieces for the book's figure modules.

A figure module is a file `tools/figs_<name>.py`. Each of its functions named `fig_*`
draws one figure:

    def fig_7_1():
        p = reg("chapters/ch07_cost.md", "7.1", "Caption sentence(s).", "## Heading the figure goes before")
        c = Canvas(720, 400, "Short title that states the point")
        ...
        c.save(p)

`reg` returns the path of the SVG to write. `tools/make_figures.py` runs every `fig_*`
function of every module and then embeds each figure in its chapter, before the named
heading, as an image line and an italic caption. Embedding is idempotent.

Rule for every figure: it is drawn from a formula or from numbers that already stand in the
chapter text, it carries no new claim, and where it repeats a number from the text the
function asserts that the number it computed agrees.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgfig import (  # noqa: E402,F401
    BORDER, BOX, CRITICAL, GOOD, GRID, INK, INK2, INK3, SERIES, SURFACE, Axes, Canvas, legend,
)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, "figures")
os.makedirs(FIG, exist_ok=True)
FIGS = []  # (chapter path relative to ROOT, label, filename, caption, heading the figure goes before)


def reg(chapter, label, caption, before):
    """Register a figure. `label` is "chapter.number" ("7.1") or "A.1" for an appendix."""
    head, num = label.split(".")
    stem = f"ch{head.zfill(2)}" if head.isdigit() else f"app{head.lower()}"
    fname = f"{stem}_fig{num}.svg"
    if any(f[2] == fname for f in FIGS):
        raise SystemExit(f"figure {label} registered twice")
    FIGS.append((chapter, label, fname, caption, before))
    return os.path.join(FIG, fname)


def h2(x):
    """Binary entropy in bits."""
    return 0.0 if x <= 0 or x >= 1 else -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def embed():
    """Insert each registered figure before its heading. Skips figures already embedded."""
    for chapter, label, fname, caption, before in FIGS:
        path = os.path.join(ROOT, chapter)
        with open(path, encoding="utf-8", newline="") as f:
            s = f.read()
        if fname in s:
            continue
        nl = "\r\n" if "\r\n" in s else "\n"
        key = nl + before + nl
        if s.count(key) != 1:
            raise SystemExit(f"{chapter}: heading not found exactly once: {before}")
        block = f"![Figure {label}](figures/{fname}){nl}{nl}*Figure {label}. {caption}*{nl}"
        s = s.replace(key, nl + block + nl + before + nl)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(s)
        print("embedded", label, "in", chapter)
