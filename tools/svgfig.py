"""svgfig: a small, dependency-free SVG chart library for the book's figures.

Encodes the chart-design rules the figures follow so they hold by construction.
Thin marks (bars at most 24px, 4px rounded data-end, square at the baseline).
2px lines, markers of radius at least 4 with a 2px surface ring. Hairline solid
gridlines one step off the surface. Text always in ink, never in a series colour.
Categorical hues assigned in fixed order from the validated reference palette.
One axis per chart. Every mark carries a <title> so hovering reads its value.
"""

from __future__ import annotations

import math
from xml.sax.saxutils import escape

# Palette of the online Geometric Series (erisml-lib docs/assets/css/style.css): the card
# surface, the text colours and the ColorBrewer Set2 hues the site uses on its dark ground.
SURFACE = "#0b1622"   # --bg-deep, the page background, so a figure has no visible frame
BORDER = "#2a4a56"    # --border-medium (teal at 30%) composited on the card
INK = "#e8ecf0"       # --text-primary
INK2 = "#a9bccd"      # between --text-primary and --text-secondary, for small labels
INK3 = "#8fa4b8"      # --text-secondary
GRID = "#1b2e40"      # hairline, one step off the surface
SERIES = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"]
CRITICAL = "#e78ac3"
GOOD = "#a6d854"
BOX = "#1a3248"       # --bg-hover
FONT = "Inter, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
TITLE_FONT = "'Crimson Pro', Georgia, 'Times New Roman', serif"


def fmt(v):
    if isinstance(v, float):
        if abs(v) >= 100:
            return f"{v:.0f}"
        if abs(v) >= 10:
            return f"{v:.1f}".rstrip("0").rstrip(".")
        return f"{v:.3f}".rstrip("0").rstrip(".")
    return str(v)


class Canvas:
    def __init__(self, w=720, h=400, title=""):
        self.w, self.h = w, h
        self.parts = []
        self.title = title

    def add(self, s):
        self.parts.append(s)

    # ---- primitives
    def rect(self, x, y, w, h, fill, r_top=4, title=None, opacity=1.0):
        """Bar with rounded data-end at the top and a square baseline."""
        w = max(w, 0.5)
        h = max(h, 0.5)
        r = min(r_top, w / 2, h)
        d = (f"M{x:.2f},{y + h:.2f} L{x:.2f},{y + r:.2f} Q{x:.2f},{y:.2f} {x + r:.2f},{y:.2f} "
             f"L{x + w - r:.2f},{y:.2f} Q{x + w:.2f},{y:.2f} {x + w:.2f},{y + r:.2f} L{x + w:.2f},{y + h:.2f} Z")
        t = f"<title>{escape(title)}</title>" if title else ""
        self.add(f'<path d="{d}" fill="{fill}" fill-opacity="{opacity}">{t}</path>')

    def hrect(self, x, y, w, h, fill, title=None, opacity=1.0):
        """Horizontal bar with rounded data-end at the right, square at the left baseline."""
        w = max(w, 0.5)
        r = min(4, h / 2, w)
        d = (f"M{x:.2f},{y:.2f} L{x + w - r:.2f},{y:.2f} Q{x + w:.2f},{y:.2f} {x + w:.2f},{y + r:.2f} "
             f"L{x + w:.2f},{y + h - r:.2f} Q{x + w:.2f},{y + h:.2f} {x + w - r:.2f},{y + h:.2f} L{x:.2f},{y + h:.2f} Z")
        t = f"<title>{escape(title)}</title>" if title else ""
        self.add(f'<path d="{d}" fill="{fill}" fill-opacity="{opacity}">{t}</path>')

    def line(self, x1, y1, x2, y2, stroke=INK, width=2, dash=None, opacity=1.0):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" '
                 f'stroke-width="{width}" stroke-linecap="round"{da} stroke-opacity="{opacity}"/>')

    def polyline(self, pts, stroke, width=2, title=None):
        d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        t = f"<title>{escape(title)}</title>" if title else ""
        self.add(f'<polyline points="{d}" fill="none" stroke="{stroke}" stroke-width="{width}" '
                 f'stroke-linejoin="round" stroke-linecap="round">{t}</polyline>')

    def dot(self, x, y, fill, r=4.5, title=None):
        t = f"<title>{escape(title)}</title>" if title else ""
        self.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r + 2:.2f}" fill="{SURFACE}"/>')
        self.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}">{t}</circle>')

    def text(self, x, y, s, size=12, anchor="start", color=INK, weight="normal", italic=False, rotate=None):
        st = f'font-family="{FONT}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}"'
        if italic:
            st += ' font-style="italic"'
        tr = f' transform="rotate({rotate} {x:.2f} {y:.2f})"' if rotate is not None else ""
        self.add(f'<text x="{x:.2f}" y="{y:.2f}" {st}{tr}>{escape(str(s))}</text>')

    def ellipse(self, cx, cy, rx, ry, angle=0, stroke=INK, fill="none", width=2, opacity=1.0, title=None):
        t = f"<title>{escape(title)}</title>" if title else ""
        self.add(f'<ellipse cx="{cx:.2f}" cy="{cy:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" transform="rotate({angle} {cx:.2f} {cy:.2f})" '
                 f'fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{width}">{t}</ellipse>')

    def arrow(self, x1, y1, x2, y2, stroke=INK2, width=1.5):
        self.line(x1, y1, x2, y2, stroke, width)
        ang = math.atan2(y2 - y1, x2 - x1)
        for s in (+1, -1):
            a = ang + s * 2.6
            self.line(x2, y2, x2 + 8 * math.cos(a), y2 + 8 * math.sin(a), stroke, width)

    def box(self, x, y, w, h, label, sub=None, fill=BOX, stroke=BORDER):
        self.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
        if sub:
            self.text(x + w / 2, y + h / 2 - 3, label, 12, "middle", INK, "600")
            self.text(x + w / 2, y + h / 2 + 13, sub, 10.5, "middle", INK2)
        else:
            self.text(x + w / 2, y + h / 2 + 4, label, 12, "middle", INK, "600")

    # ---- output
    def save(self, path, caption=None):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" '
                f'role="img" aria-label="{escape(self.title or caption or "figure")}">'
                f'<rect width="100%" height="100%" fill="{SURFACE}"/>')
        body = "".join(self.parts)
        if self.title:
            body = f'<text x="18" y="27" font-family="{TITLE_FONT}" font-size="17" font-weight="600" fill="{INK}">{escape(self.title)}</text>' + body
        with open(path, "w", encoding="utf-8") as f:
            f.write(head + body + "</svg>")


# ---------------------------------------------------------------- axes


class Axes:
    """A single-axis plotting area with hairline gridlines."""

    def __init__(self, c: Canvas, x0, y0, w, h, xlim, ylim, xticks=(), yticks=(), xlabel="", ylabel="", xlog=False, ylog=False):
        self.c, self.x0, self.y0, self.w, self.h = c, x0, y0, w, h
        self.xlim, self.ylim, self.xlog, self.ylog = xlim, ylim, xlog, ylog
        for v in yticks:
            y = self.Y(v)
            c.line(x0, y, x0 + w, y, GRID, 1)
            c.text(x0 - 8, y + 4, fmt(v), 11, "end", INK2)
        for v in xticks:
            x = self.X(v)
            c.text(x, y0 + h + 16, fmt(v), 11, "middle", INK2)
        c.line(x0, y0 + h, x0 + w, y0 + h, GRID, 1)
        if xlabel:
            c.text(x0 + w / 2, y0 + h + 34, xlabel, 11.5, "middle", INK2)
        if ylabel:
            c.text(x0 - 44, y0 + h / 2, ylabel, 11.5, "middle", INK2, rotate=-90)

    def X(self, v):
        a, b = self.xlim
        if self.xlog:
            return self.x0 + self.w * (math.log10(v) - math.log10(a)) / (math.log10(b) - math.log10(a))
        return self.x0 + self.w * (v - a) / (b - a)

    def Y(self, v):
        a, b = self.ylim
        if self.ylog:
            return self.y0 + self.h * (1 - (math.log10(v) - math.log10(a)) / (math.log10(b) - math.log10(a)))
        return self.y0 + self.h * (1 - (v - a) / (b - a))


def legend(c: Canvas, x, y, items, size=11.5):
    """items: list of (label, colour). Drawn in one row."""
    for label, col in items:
        c.add(f'<rect x="{x:.2f}" y="{y - 9:.2f}" width="12" height="12" rx="3" fill="{col}"/>')
        c.text(x + 18, y + 1, label, size, "start", INK2)
        x += 18 + 7.2 * len(label) + 22


# ---------------------------------------------------------------- chart forms


def bar_chart(path, title, cats, vals, ylabel="", ylim=None, yticks=None, refline=None, reflabel=None,
              colors=None, w=720, h=400, direct=True, caption=None, note=None, reflabel_anchor="end", catsize=11):
    c = Canvas(w, h, title)
    ylim = ylim or (0, max(vals) * 1.15)
    yticks = yticks or []
    ax = Axes(c, 70, 44, w - 100, h - 110, (0, len(cats)), ylim, (), yticks, "", ylabel)
    slot = ax.w / len(cats)
    bw = min(24, slot * 0.6)
    for i, (cat, v) in enumerate(zip(cats, vals)):
        col = (colors[i] if colors else SERIES[0])
        x = ax.x0 + slot * (i + 0.5) - bw / 2
        y = ax.Y(max(v, ylim[0]))
        base = ax.Y(max(0, ylim[0]))
        top, bottom = min(y, base), max(y, base)
        c.rect(x, top, bw, bottom - top, col, title=f"{cat} {fmt(v)}")
        if direct:
            c.text(x + bw / 2, top - 6, fmt(v), 11, "middle", INK)
        c.text(ax.x0 + slot * (i + 0.5), ax.y0 + ax.h + 16, cat, catsize, "middle", INK2)
    if refline is not None:
        y = ax.Y(refline)
        c.line(ax.x0, y, ax.x0 + ax.w, y, INK3, 1.5, dash="4 4")
        if reflabel:
            rx = ax.x0 + ax.w if reflabel_anchor == "end" else ax.x0 + 4
            c.text(rx, y - 5, reflabel, 10.5, reflabel_anchor, INK2, italic=True)
    if note:
        c.text(16, h - 10, note, 10.5, "start", INK3, italic=True)
    c.save(path, caption)


def grouped_bars(path, title, cats, series, ylabel="", ylim=(0, 1), yticks=None, w=720, h=400,
                 refline=None, reflabel=None, direct=True, note=None):
    """series: list of (name, values)."""
    c = Canvas(w, h, title)
    yticks = yticks or []
    ax = Axes(c, 70, 52, w - 100, h - 126, (0, len(cats)), ylim, (), yticks, "", ylabel)
    slot = ax.w / len(cats)
    n = len(series)
    bw = min(24, slot * 0.7 / n - 2)
    for i, cat in enumerate(cats):
        cx = ax.x0 + slot * (i + 0.5)
        total = n * bw + (n - 1) * 2
        for j, (name, vals) in enumerate(series):
            v = vals[i]
            if v is None:
                continue
            x = cx - total / 2 + j * (bw + 2)
            y = ax.Y(v)
            c.rect(x, y, bw, ax.Y(ylim[0]) - y, SERIES[j], title=f"{cat}, {name} {fmt(v)}")
            if direct:
                c.text(x + bw / 2, y - 5, fmt(v), 10, "middle", INK)
        c.text(cx, ax.y0 + ax.h + 16, cat, 11, "middle", INK2)
    if refline is not None:
        y = ax.Y(refline)
        c.line(ax.x0, y, ax.x0 + ax.w, y, INK3, 1.5, dash="4 4")
        if reflabel:
            c.text(ax.x0 + ax.w, y - 5, reflabel, 10.5, "end", INK2, italic=True)
    legend(c, 70, 40, [(nm, SERIES[j]) for j, (nm, _) in enumerate(series)])
    if note:
        c.text(16, h - 10, note, 10.5, "start", INK3, italic=True)
    c.save(path)


def line_chart(path, title, xs, series, xlabel="", ylabel="", xlim=None, ylim=None, xticks=None, yticks=None,
               xlog=False, w=720, h=400, markers=True, endlabels=True, note=None, refline=None, reflabel=None,
               dashed=(), ylog=False, reflabel_anchor="end"):
    c = Canvas(w, h, title)
    xlim = xlim or (min(xs), max(xs))
    allv = [v for _, ys in series for v in ys if v is not None]
    ylim = ylim or (0, max(allv) * 1.1)
    ax = Axes(c, 70, 52, w - 160, h - 126, xlim, ylim, xticks or [], yticks or [], xlabel, ylabel, xlog, ylog)
    for j, (name, ys) in enumerate(series):
        col = SERIES[j]
        pts = [(ax.X(x), ax.Y(y)) for x, y in zip(xs, ys) if y is not None]
        if name in dashed:
            for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
                c.line(x1, y1, x2, y2, col, 2, dash="5 5")
        else:
            c.polyline(pts, col, 2, title=name)
        if markers:
            for (px, py), x, y in zip(pts, [x for x, y in zip(xs, ys) if y is not None], [y for y in ys if y is not None]):
                c.dot(px, py, col, 4.5, title=f"{name}, {fmt(x)} {fmt(y)}")
        if endlabels and pts:
            c.text(pts[-1][0] + 10, pts[-1][1] + 4, name, 11, "start", INK2)
    if refline is not None:
        y = ax.Y(refline)
        c.line(ax.x0, y, ax.x0 + ax.w, y, INK3, 1.5, dash="4 4")
        if reflabel:
            rx = ax.x0 + ax.w if reflabel_anchor == "end" else ax.x0 + 4
            c.text(rx, y - 5, reflabel, 10.5, reflabel_anchor, INK2, italic=True)
    if len(series) >= 2:
        legend(c, 70, 40, [(nm, SERIES[j]) for j, (nm, _) in enumerate(series)])
    if note:
        c.text(16, h - 10, note, 10.5, "start", INK3, italic=True)
    c.save(path)


def dumbbell(path, title, cats, a, b, aname, bname, xlim=(0, 1), xticks=None, w=720, h=None, note=None, refline=None, reflabel=None):
    """Horizontal dumbbell, one row per category, two values joined by a line."""
    h = h or (70 + 34 * len(cats) + 50)
    c = Canvas(w, h, title)
    ax = Axes(c, 170, 52, w - 210, 34 * len(cats), xlim, (0, len(cats)), xticks or [], [], "", "")
    for i, cat in enumerate(cats):
        y = ax.y0 + 34 * (i + 0.5)
        c.text(ax.x0 - 10, y + 4, cat, 11.5, "end", INK2)
        c.line(ax.x0, y, ax.x0 + ax.w, y, GRID, 1)
        if a[i] is None or b[i] is None:
            continue
        xa, xb = ax.X(a[i]), ax.X(b[i])
        c.line(xa, y, xb, y, INK3, 2)
        c.dot(xa, y, SERIES[0], 5, title=f"{cat}, {aname} {fmt(a[i])}")
        c.dot(xb, y, SERIES[1], 5, title=f"{cat}, {bname} {fmt(b[i])}")
        lo, hi = (xa, xb) if xa < xb else (xb, xa)
        c.text(lo - 9, y + 4, fmt(min(a[i], b[i])), 10.5, "end", INK)
        c.text(hi + 9, y + 4, fmt(max(a[i], b[i])), 10.5, "start", INK)
    if refline is not None:
        x = ax.X(refline)
        c.line(x, ax.y0, x, ax.y0 + ax.h, INK3, 1.5, dash="4 4")
        if reflabel:
            c.text(x + 4, ax.y0 - 6, reflabel, 10.5, "start", INK2, italic=True)
    legend(c, 170, 40, [(aname, SERIES[0]), (bname, SERIES[1])])
    if note:
        c.text(16, h - 10, note, 10.5, "start", INK3, italic=True)
    c.save(path)


def stacked_bars(path, title, cats, parts, ylabel="", w=720, h=420, note=None):
    """parts: list of (name, values summing to about 1 per category). Segments separated by a 2px surface gap."""
    c = Canvas(w, h, title)
    ax = Axes(c, 70, 52, w - 100, h - 140, (0, len(cats)), (0, 1), (), [0, 0.25, 0.5, 0.75, 1.0], "", ylabel)
    slot = ax.w / len(cats)
    bw = min(24, slot * 0.5)
    for i, cat in enumerate(cats):
        x = ax.x0 + slot * (i + 0.5) - bw / 2
        acc = 0.0
        for j, (name, vals) in enumerate(parts):
            v = vals[i]
            y1, y0 = ax.Y(acc), ax.Y(acc + v)
            hgt = max(y1 - y0 - 2, 0.5)
            c.add(f'<rect x="{x:.2f}" y="{y0 + 1:.2f}" width="{bw:.2f}" height="{hgt:.2f}" fill="{SERIES[j]}"><title>{escape(f"{cat}, {name} {fmt(v)}")}</title></rect>')
            if v >= 0.12:
                c.text(x + bw + 6, (y0 + y1) / 2 + 4, fmt(v), 10, "start", INK2)
            acc += v
        c.text(ax.x0 + slot * (i + 0.5), ax.y0 + ax.h + 16, cat, 11, "middle", INK2)
    legend(c, 70, 40, [(nm, SERIES[j]) for j, (nm, _) in enumerate(parts)], 10.5)
    if note:
        c.text(16, h - 10, note, 10.5, "start", INK3, italic=True)
    c.save(path)


def dot_rows(path, title, cats, points, xlim, xticks, xlabel="", w=720, h=None, note=None, refs=()):
    """points: list of lists, one list of x-values per category (e.g. seeds). refs: (x, label) vertical lines."""
    h = h or (70 + 34 * len(cats) + 50)
    c = Canvas(w, h, title)
    ax = Axes(c, 170, 52, w - 210, 34 * len(cats), xlim, (0, len(cats)), xticks, [], xlabel, "")
    for i, cat in enumerate(cats):
        y = ax.y0 + 34 * (i + 0.5)
        c.text(ax.x0 - 10, y + 4, cat, 11.5, "end", INK2)
        c.line(ax.x0, y, ax.x0 + ax.w, y, GRID, 1)
        for v in points[i]:
            c.dot(ax.X(v), y, SERIES[0], 5, title=f"{cat} {fmt(v)}")
        c.text(ax.X(max(points[i])) + 10, y + 4, ", ".join(fmt(v) for v in points[i]), 10.5, "start", INK)
    for x, lab in refs:
        c.line(ax.X(x), ax.y0, ax.X(x), ax.y0 + ax.h, INK3, 1.5, dash="4 4")
        c.text(ax.X(x) + 4, ax.y0 - 6, lab, 10.5, "start", INK2, italic=True)
    if note:
        c.text(16, h - 10, note, 10.5, "start", INK3, italic=True)
    c.save(path)
