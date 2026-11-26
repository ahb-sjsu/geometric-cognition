"""Figures for Geometric Cognition, Chapters 1 to 17 (2026-11-26).

Every figure is drawn from a formula, a definition or numbers printed in its chapter. Chapters
1, 2, 3, 5, 6, 8, 9, 12, 13 and 15 already hold a diagram captioned "Figure N.1 (diagram)", so
the figures here continue from N.2 in those chapters.

Not drawn, on purpose: any benchmark score on the "Unresolved" list of
CORRECTIONS-2026-11-26.md (E2 recovery and displacement, A4, M3 and M4 of Flash 3, Flash 2.5 and
Claude, the L2 sycophancy rates, E1 scores, the composites, the 38 percent recovery ceiling),
and the A1 flip rates of Section 10.2, whose ordering Chapters 1 and 16 contradict.
The Anthropic model is labelled "Claude" only, because its version name is unresolved.
"""

import math
import random

from figkit import CRITICAL, GRID, INK, INK2, INK3, SERIES, Axes, Canvas, legend, reg


# ------------------------------------------------------------------ helpers
def _metric(l1, l2, theta):
    """Symmetric 2x2 metric with eigenvalues l1, l2 and the l1 axis at angle theta (radians)."""
    cs, sn = math.cos(theta), math.sin(theta)
    return (l1 * cs * cs + l2 * sn * sn, (l1 - l2) * sn * cs, l1 * sn * sn + l2 * cs * cs)


def _eig(g):
    a, b, d = g
    m, r = (a + d) / 2, math.hypot((a - d) / 2, b)
    return m + r, m - r, 0.5 * math.atan2(2 * b, a - d)


def _ellipse(c, cx, cy, g, s, col, title=None):
    """Draw the metric g = (g11, g12, g22) as an ellipse with semi-axes s * sqrt(eigenvalue)."""
    l1, l2, ang = _eig(g)
    c.line(cx - 46, cy, cx + 46, cy, GRID, 1)
    c.line(cx, cy - 46, cx, cy + 46, GRID, 1)
    c.ellipse(cx, cy, s * math.sqrt(l1), s * math.sqrt(max(l2, 1e-9)), -math.degrees(ang), col, col, 2, 0.14, title)


def _lbar(c, x_right, y, w, h, fill, title):
    """Horizontal bar that grows to the left from x_right, rounded at its left (data) end."""
    r = min(4, h / 2, w)
    x = x_right - w
    d = (f"M{x_right:.2f},{y:.2f} L{x + r:.2f},{y:.2f} Q{x:.2f},{y:.2f} {x:.2f},{y + r:.2f} "
         f"L{x:.2f},{y + h - r:.2f} Q{x:.2f},{y + h:.2f} {x + r:.2f},{y + h:.2f} L{x_right:.2f},{y + h:.2f} Z")
    c.add(f'<path d="{d}" fill="{fill}"><title>{title}</title></path>')


def _band(c, x, y, w, h, fill, opacity=0.10):
    c.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{fill}" fill-opacity="{opacity}"/>')


def _vec(c, x1, y1, x2, y2, col, width=2.5):
    c.arrow(x1, y1, x2, y2, col, width)


# ------------------------------------------------------------------ chapter 1
def fig_01_2():
    a, b, v = (0.95, 0.35), (0.40, 0.90), 0.65
    assert abs(sum(a) / 2 - v) < 1e-12 and abs(sum(b) / 2 - v) < 1e-12
    p = reg("chapters/ch01_iq_trap.md", "1.2",
            "The fibers of a scalar contraction for a profile of two scores, drawn for the uniform-weight contraction "
            "of Definition 1.2, the mean of the two scores. The axes are the scores on the two tasks, and each line "
            "is the set of all profiles with one value of the mean. The profiles A = (0.95, 0.35) and B = (0.40, "
            "0.90) are illustrative values on the line of mean 0.65. The score 0.65 is the same for both and for "
            "every other point of that line, which is the content of Theorem 1.1.",
            "## 1.5 The Empirical Demonstration")
    c = Canvas(720, 400, "One score, a whole line of different profiles")
    ax = Axes(c, 80, 50, 290, 290, (0, 1), (0, 1), [0, 0.25, 0.5, 0.75, 1], [0, 0.25, 0.5, 0.75, 1],
              "score on task 1", "score on task 2")
    c.line(ax.x0, ax.y0, ax.x0, ax.y0 + ax.h, GRID, 1)
    c.line(ax.x0 + ax.w, ax.y0, ax.x0 + ax.w, ax.y0 + ax.h, GRID, 1)
    for m in (0.2, 0.35, 0.5, 0.65, 0.8):
        lo, hi = max(0.0, 2 * m - 1), min(1.0, 2 * m)
        hot = abs(m - v) < 1e-9
        c.line(ax.X(lo), ax.Y(2 * m - lo), ax.X(hi), ax.Y(2 * m - hi), SERIES[0] if hot else INK3, 2.5 if hot else 1.2,
               opacity=1.0 if hot else 0.7)
    c.dot(ax.X(a[0]), ax.Y(a[1]), SERIES[1], 5.5, title="A = (0.95, 0.35), mean 0.65")
    c.dot(ax.X(b[0]), ax.Y(b[1]), SERIES[2], 5.5, title="B = (0.40, 0.90), mean 0.65")
    c.text(ax.X(a[0]) - 12, ax.Y(a[1]) + 18, "A", 12.5, "end", INK, "600")
    c.text(ax.X(b[0]) - 12, ax.Y(b[1]) + 18, "B", 12.5, "end", INK, "600")
    x0 = 420
    c.text(x0, 84, "contraction: φ(C) = (C1 + C2) / 2", 12, "start", INK, "600")
    c.text(x0, 106, "each line: all profiles with one value of φ", 11.5, "start", INK2)
    c.text(x0, 124, "lines drawn at φ = 0.2, 0.35, 0.5, 0.65, 0.8", 11.5, "start", INK2)
    c.text(x0, 166, "A = (0.95, 0.35)   φ = 0.65", 11.5, "start", INK2)
    c.text(x0, 184, "B = (0.40, 0.90)   φ = 0.65", 11.5, "start", INK2)
    c.text(x0, 226, "From 0.65 alone, no function returns", 11.5, "start", INK2)
    c.text(x0, 244, "A rather than B, or any other point", 11.5, "start", INK2)
    c.text(x0, 262, "of the highlighted line.", 11.5, "start", INK2)
    legend(c, x0, 304, [("fiber φ = 0.65", SERIES[0]), ("A", SERIES[1]), ("B", SERIES[2])])
    c.text(16, 390, "A and B are illustrative values, not benchmark scores", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_01_3():
    tasks = ["diagnosis", "drug interactions", "treatment planning", "patient communication", "medical coding"]
    models = [("Model A", [0.95, 0.60, 0.80, 0.70, 0.85]), ("Model B", [0.70, 0.85, 0.75, 0.80, 0.80]),
              ("Model C", [0.80, 0.75, 0.78, 0.77, 0.80])]
    for _, s in models:
        assert abs(sum(s) / 5 - 0.78) < 1e-9
    p = reg("chapters/ch01_iq_trap.md", "1.3",
            "The hypothetical hospital evaluation of Section 1.14: three models scored on five task types, with the "
            "score on each task on the vertical axis. The dashed line is the composite, the mean of the five scores, "
            "which is 0.78 for all three. The composite ranks the models as tied while the profiles differ: Model A "
            "peaks on diagnosis, Model B on drug interactions, and Model C is flat.",
            "## 1.15 Looking Forward: From Trap to Manifold")
    c = Canvas(720, 400, "Three profiles, one composite of 0.78 (hypothetical example)")
    ax = Axes(c, 70, 58, 610, 260, (0, 5), (0.5, 1.0), [], [0.5, 0.6, 0.7, 0.8, 0.9, 1.0], "", "score on the task")
    for i, t in enumerate(tasks):
        c.text(ax.X(i + 0.5), ax.y0 + ax.h + 18, t, 11, "middle", INK2)
    y = ax.Y(0.78)
    c.line(ax.x0, y, ax.x0 + ax.w, y, INK3, 1.5, dash="5 4")
    c.line(ax.x0 + ax.w - 196, 42, ax.x0 + ax.w - 170, 42, INK3, 1.5, dash="5 4")
    c.text(ax.x0 + ax.w, 46, "composite 0.78, all three models", 11.5, "end", INK2)
    for j, (name, s) in enumerate(models):
        pts = [(ax.X(i + 0.5), ax.Y(v)) for i, v in enumerate(s)]
        c.polyline(pts, SERIES[j], 2, title=name)
        for (px, py), t, v in zip(pts, tasks, s):
            c.dot(px, py, SERIES[j], 4.5, title=f"{name}, {t}: {v:.2f}")
    c.text(ax.X(0.5) + 10, ax.Y(0.95) + 4, "0.95", 10.5, "start", INK)
    c.text(ax.X(1.5) + 10, ax.Y(0.60) + 4, "0.60", 10.5, "start", INK)
    c.text(ax.X(1.5) + 10, ax.Y(0.85) + 4, "0.85", 10.5, "start", INK)
    c.text(ax.X(0.5) + 10, ax.Y(0.70) + 4, "0.70", 10.5, "start", INK)
    legend(c, 70, 46, [(n, SERIES[j]) for j, (n, _) in enumerate(models)])
    c.text(16, 390, "hypothetical scores from the worked example of Section 1.14, not benchmark data", 10.5, "start",
           INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 2
def fig_02_2():
    L, k0 = 5.0, 0.048
    amp = lambda k: math.exp(math.sqrt(k) * L)  # noqa: E731
    assert abs(amp(k0) - 3.0) < 0.02 and abs(math.log(3) / 5 - 0.22) < 0.005
    p = reg("chapters/ch02_kahneman.md", "2.2",
            "The amplification factor exp(sqrt(|κ|) L) that the worked example of Section 2.12 posits, drawn for a "
            "trajectory of length L = 5. The horizontal axis is the magnitude of the sectional curvature and the "
            "vertical axis the ratio of the displacement in the judgment to the perturbation of the input. The marked "
            "point is the worked example, where an amplification of 3.0 gives |κ| of about 0.048. The perturbation of "
            "0.1 and the displacement of 0.3 behind that factor are the example's modelling assumptions, not "
            "measurements.",
            "## 2.13 The Failure of Scalar Measurement, Revisited")
    c = Canvas(720, 400, "Negative curvature amplifies a small perturbation exponentially")
    ax = Axes(c, 80, 52, 540, 270, (0, 0.12), (0, 6), [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12], [0, 1, 2, 3, 4, 5, 6],
              "magnitude of sectional curvature |κ|", "amplification δJ / ε")
    y1 = ax.Y(1)
    c.line(ax.x0, y1, ax.x0 + ax.w, y1, INK3, 1.2, dash="4 4")
    c.text(ax.x0 + ax.w - 4, y1 + 15, "flat: no amplification", 10.5, "end", INK2, italic=True)
    pts = [(ax.X(k), ax.Y(amp(k))) for k in [i * 0.12 / 240 for i in range(241)]]
    c.polyline(pts, SERIES[0], 2.5, title="exp(sqrt(|κ|) L), L = 5")
    px, py = ax.X(k0), ax.Y(amp(k0))
    c.line(px, py, px, ax.y0 + ax.h, INK3, 1.2, dash="3 4")
    c.line(ax.x0, py, px, py, INK3, 1.2, dash="3 4")
    c.dot(px, py, CRITICAL, 5.5, title="worked example: |κ| ≈ 0.048, amplification 3.0")
    c.text(px + 12, py + 22, "worked example of Section 2.12", 11.5, "start", INK, "600")
    c.text(px + 12, py + 39, "amplification 3.0  →  |κ| ≈ 0.048", 11, "start", INK2)
    c.text(ax.x0 + 14, ax.y0 + 16, "δJ / ε = exp(sqrt(|κ|) · L),  L = 5", 11.5, "start", INK2, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 3
def fig_03_2():
    p = reg("chapters/ch03_cognitive_manifold.md", "3.1",
            "The three curvature regimes of Section 3.10, as a schematic: in each panel five neighbouring reasoning "
            "trajectories start parallel and run from left to right. With zero curvature their separation stays "
            "constant, with positive curvature they converge, and with negative curvature they diverge. The "
            "separations are drawn in proportion to 1, cos(sqrt(κ) t) and cosh(sqrt(|κ|) t), the last of which grows "
            "like the exponential the section gives. All panels use sqrt(|κ|) T = 1.2 at the right edge, an "
            "illustrative value.",
            "## 3.11 Worked Example: Mapping a Cognitive Trajectory")
    c = Canvas(720, 400, "Curvature sets whether nearby trajectories hold, meet or part")
    w, T = 190, 1.2
    panels = [("κ = 0", "flat: separation constant", lambda t: 1.0, SERIES[2]),
              ("κ > 0", "trajectories converge", lambda t: math.cos(t), SERIES[0]),
              ("κ < 0", "trajectories diverge", lambda t: math.cosh(t), SERIES[1])]
    for i, (head, sub, J, col) in enumerate(panels):
        x0, cy = 36 + i * 226, 205
        c.add(f'<rect x="{x0 - 10:.1f}" y="62" width="{w + 20}" height="286" rx="6" fill="none" stroke="{GRID}" stroke-width="1"/>')
        c.text(x0 + w / 2, 86, head, 13, "middle", INK, "600")
        c.text(x0 + w / 2, 104, sub, 11.5, "middle", INK2)
        for k in (-2, -1, 0, 1, 2):
            pts = [(x0 + w * s / 60, cy + 6 + k * 21 * J(T * s / 60)) for s in range(61)]
            c.polyline(pts, col, 2)
            c.dot(pts[0][0], pts[0][1], col, 3)
        c.arrow(x0 + 40, 332, x0 + w - 40, 332, INK3, 1.2)
        c.text(x0 + w / 2, 326, "t", 11, "middle", INK3, italic=True)
    c.text(16, 390, "schematic: separations follow 1, cos(sqrt(κ) t) and cosh(sqrt(|κ|) t), with sqrt(|κ|) T = 1.2",
           10.5, "start", INK3, italic=True)
    c.save(p)


def fig_03_3():
    phases = [("Phase 1", "gradient following", 0, 40, 0.02, "κ ≈ 0.02"),
              ("Phase 2", "System 1 to 2 transition", 40, 100, 0.35, "peak κ ≈ 0.35"),
              ("Phase 3", "convergence", 100, 180, 0.08, "κ falls to ≈ 0.08")]
    assert phases[1][4] == max(ph[4] for ph in phases)
    p = reg("chapters/ch03_cognitive_manifold.md", "3.2",
            "The curvature of the trajectory in the worked example of Section 3.11, which is hypothetical: the fMRI "
            "session of Maya Chen's running example and its numbers are illustrative, not data. The horizontal axis "
            "is time in the three-minute session and the vertical axis the trajectory curvature. Each block spans one "
            "of the three phases the example names and stands at the value the example gives for it: about 0.02 in "
            "Phase 1, a peak of about 0.35 in Phase 2, and about 0.08 in Phase 3.",
            "## 3.12 The Manifold for Different Cognitive Tasks")
    c = Canvas(720, 400, "Hypothetical session: curvature peaks in the transition phase")
    ax = Axes(c, 80, 60, 580, 250, (0, 180), (0, 0.42), [0, 40, 100, 180], [0, 0.1, 0.2, 0.3, 0.4],
              "time in the session (seconds)", "trajectory curvature κ")
    for j, (name, role, t0, t1, k, lab) in enumerate(phases):
        xa, xb = ax.X(t0), ax.X(t1)
        col = CRITICAL if j == 1 else SERIES[0]
        _band(c, xa + 2, ax.Y(k), xb - xa - 4, ax.Y(0) - ax.Y(k), col, 0.30)
        c.line(xa + 2, ax.Y(k), xb - 2, ax.Y(k), col, 2.5)
        c.text((xa + xb) / 2, ax.Y(k) - 26, name, 12, "middle", INK, "600")
        c.text((xa + xb) / 2, ax.Y(k) - 10, lab, 11, "middle", INK2)
        c.text((xa + xb) / 2, ax.y0 + ax.h - 8 if j == 1 else ax.Y(k) - 44, role, 10.5, "middle", INK2, italic=True)
        if j:
            c.line(xa, ax.y0, xa, ax.y0 + ax.h, INK3, 1, dash="3 4")
    c.text(16, 390, "illustrative, hypothetical data from the running example; one stated value per phase, no time course",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 4
def fig_04_1():
    cases = [(1.0, 1.0), (1.5, 0.5), (1.9, 0.1)]
    for al, be in cases:
        assert abs(al + be - 2) < 1e-12  # the resource constraint |S| α + (n - |S|) β = n with n = 2, |S| = 1
    p = reg("chapters/ch04_attention_metric.md", "4.1",
            "The selective attention operator of Definition 4.2 in two dimensions, with one attended dimension "
            "(horizontal, scaled by α) and one unattended dimension (vertical, scaled by β), on an identity baseline. "
            "Each ellipse has semi-axes proportional to the square roots of the two metric components, so a long axis "
            "marks high resolution. The resource constraint α + β = 2 holds in all three panels, and the values are "
            "illustrative. As β falls toward 0 the ellipse collapses onto the attended dimension, the reduction of "
            "effective dimensionality that the section describes.",
            "## 4.4 Divided Attention Widens the Metric")
    c = Canvas(720, 400, "Selective attention narrows the metric under a fixed budget")
    heads = ["baseline", "selective", "strongly selective"]
    for i, (al, be) in enumerate(cases):
        cx, cy = 130 + i * 230, 205
        c.line(cx - 100, cy, cx + 100, cy, GRID, 1)
        c.line(cx, cy - 100, cx, cy + 100, GRID, 1)
        c.ellipse(cx, cy, 68 * math.sqrt(al), 68 * math.sqrt(be), 0, SERIES[i], SERIES[i], 2, 0.14,
                  title=f"α = {al}, β = {be}")
        c.text(cx, 74, heads[i], 12.5, "middle", INK, "600")
        c.text(cx, 92, f"α = {al:.1f},  β = {be:.1f}", 11.5, "middle", INK2)
    c.text(360, 332, "α + β = 2 in every panel: amplifying one dimension suppresses the other", 11.5, "middle", INK2)
    c.text(360, 352, "horizontal axis: attended dimension; vertical axis: unattended dimension", 11, "middle", INK3,
           italic=True)
    c.text(16, 390, "semi-axes proportional to sqrt(α) and sqrt(β); identity baseline; illustrative values", 10.5,
           "start", INK3, italic=True)
    c.save(p)


def fig_04_2():
    snr = lambda wg, k: 1 + wg / k  # noqa: E731
    assert snr(12, 1) == 13 and snr(12, 2) == 7 and snr(4, 4) == 2
    p = reg("chapters/ch04_attention_metric.md", "4.2",
            "The per-target signal-to-noise ratio under equal division of a fixed attention budget W over k targets, "
            "from Proposition 4.2 of Technical Appendix 4B: 1 + W / (k g), where g is the metric component along the "
            "noise dimension. The horizontal axis is the number of targets and the vertical axis the ratio on each "
            "target. The two curves are drawn for W / g = 4 and 12, illustrative values, and at k = 1 the ratio is "
            "that of selective attention. The dashed line at 1 is the level at which the metric treats signal and "
            "noise equally.",
            "## 4.5 The A4 Divided Attention Split: The Metric Made Visible")
    c = Canvas(720, 400, "Dividing a fixed budget lowers the resolution on each target")
    ks = [1, 2, 3, 4, 5, 6]
    ax = Axes(c, 80, 58, 520, 260, (0.5, 6.5), (0, 14), ks, [0, 2, 4, 6, 8, 10, 12, 14],
              "number of attention targets k", "signal-to-noise ratio per target")
    y1 = ax.Y(1)
    c.line(ax.x0, y1, ax.x0 + ax.w, y1, INK3, 1.5, dash="4 4")
    c.text(ax.x0 + 6, y1 + 15, "ratio 1: no discrimination", 10.5, "start", INK2, italic=True)
    for j, wg in enumerate((12, 4)):
        pts = [(ax.X(k), ax.Y(snr(wg, k))) for k in ks]
        c.polyline(pts, SERIES[j], 2)
        for (px, py), k in zip(pts, ks):
            c.dot(px, py, SERIES[j], 4.5, title=f"W/g_n = {wg}, k = {k}: {snr(wg, k):.2f}")
        c.text(pts[-1][0] + 12, pts[-1][1] + 4, f"W / g_n = {wg}", 11, "start", INK2)
    c.text(ax.X(1) + 12, ax.Y(13) + 4, "selective: 1 + W / g_n = 13", 11, "start", INK)
    c.text(ax.X(2) + 12, ax.Y(7) - 2, "two targets: 7", 11, "start", INK)
    c.text(ax.x0 + ax.w - 4, ax.y0 + 14, "ratio per target = 1 + W / (k · g_n)", 11.5, "end", INK2, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 5
def fig_05_2():
    c_per, beta = 2.0, 1.0
    neffs = [10.2, 14.4, 16.0]
    acc = lambda n, k: 1 / (1 + math.exp(-beta * (n - c_per * k)))  # noqa: E731
    half = [n / c_per for n in neffs]
    assert [round(h, 1) for h in half] == [5.1, 7.2, 8.0]   # k* of about 5, about 7 and at least 8 in Appendix 5B
    assert all(abs(acc(n, h) - 0.5) < 1e-12 for n, h in zip(neffs, half))
    p = reg("chapters/ch05_working_memory.md", "5.2",
            "The sigmoid model of Section 5.12 and Technical Appendix 5B, as the chapter defines it: accuracy = 1 / "
            "(1 + exp(-β (n - 2k))), where n is the effective tangent space dimension and k the number of parties, on "
            "the horizontal axis. The three curves use the dimensions that Appendix 5B estimates for three model "
            "generations, 10.2, 14.4 and the lower bound 16, with a sharpness β = 1, an illustrative value. Each "
            "curve passes through one half at k = n / 2, marked by a dot. The curves are the posited model, not "
            "measured accuracies; the benchmark tested k = 2, 4, 6 and 8.",
            "## 5.13 Working Memory in Human Cognition")
    c = Canvas(720, 400, "A larger tangent space moves the capacity transition to more parties")
    ax = Axes(c, 80, 62, 580, 256, (0, 10), (0, 1.05), [0, 2, 4, 6, 8, 10], [0, 0.25, 0.5, 0.75, 1.0],
              "number of parties k", "modelled accuracy")
    for k in (2, 4, 6, 8):
        c.line(ax.X(k), ax.y0, ax.X(k), ax.y0 + ax.h, GRID, 1)
    names = ["n_eff = 10.2", "n_eff = 14.4", "n_eff = 16 (lower bound)"]
    for j, n in enumerate(neffs):
        pts = [(ax.X(k), ax.Y(acc(n, k))) for k in [i / 20 for i in range(201)]]
        c.polyline(pts, SERIES[j], 2.5, title=names[j])
    for j, h in enumerate(half):
        c.dot(ax.X(h), ax.Y(0.5), SERIES[j], 5, title=f"accuracy 0.5 at k = {h:.1f}")
    c.text(ax.X(5.1) - 10, ax.Y(0.5) + 18, "k = 5.1", 10.5, "end", INK)
    c.text(ax.X(7.2) - 10, ax.Y(0.5) + 18, "7.2", 10.5, "end", INK)
    c.text(ax.X(8.0) + 10, ax.Y(0.5) - 8, "8", 10.5, "start", INK)
    c.text(ax.X(2) + 4, ax.y0 + ax.h - 6, "tested: k = 2, 4, 6, 8", 10.5, "start", INK3, italic=True)
    legend(c, 80, 48, [(nm, SERIES[j]) for j, nm in enumerate(names)])
    c.text(16, 390, "posited model, drawn for c = 2 and an illustrative sharpness β = 1; not measured accuracies", 10.5,
           "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 6
def fig_06_2():
    l1, l2 = 4.0, 1.0
    for th in (0, 30, 60, 90):
        e1, e2, _ = _eig(_metric(l1, l2, math.radians(th)))
        assert abs(e1 - l1) < 1e-9 and abs(e2 - l2) < 1e-9   # a rotation keeps the eigenvalues
    g90 = _metric(l1, l2, math.pi / 2)
    assert abs(g90[0] - l2) < 1e-9 and abs(g90[2] - l1) < 1e-9
    p = reg("chapters/ch06_executive_functions.md", "6.1",
            "Framework switching as the metric rotation of Definition 6.1, in two cognitive dimensions. Each ellipse "
            "is the attention metric at one rotation angle, with semi-axes proportional to the square roots of its "
            "eigenvalues, so the long axis points along the most heavily weighted direction. The rotation keeps the "
            "eigenvalues and turns the axes: at 90 degrees the weights of the two dimensions have exchanged. The "
            "eigenvalues 4 and 1, the angles and the naming of the two dimensions are illustrative choices.",
            "## 6.3 Inhibitory Control as Gradient Suppression")
    c = Canvas(720, 400, "A framework switch rotates the metric and keeps its shape")
    for i, th in enumerate((0, 30, 60, 90)):
        cx, cy = 105 + i * 170, 200
        g = _metric(l1, l2, math.radians(th))
        c.line(cx - 72, cy, cx + 72, cy, GRID, 1)
        c.line(cx, cy - 72, cx, cy + 72, GRID, 1)
        l, m, ang = _eig(g)
        c.ellipse(cx, cy, 30 * math.sqrt(l), 30 * math.sqrt(m), -math.degrees(ang), SERIES[i], SERIES[i], 2, 0.14,
                  title=f"θ = {th}°")
        c.text(cx, 96, f"θ = {th}°", 12.5, "middle", INK, "600")
        if i < 3:
            c.arrow(cx + 80, cy, cx + 92, cy, INK3, 1.2)
    c.text(105, 76, "utilitarian metric", 11.5, "middle", INK2)
    c.text(615, 76, "deontological metric", 11.5, "middle", INK2)
    c.text(105, 296, "weight on aggregate welfare", 10.5, "middle", INK3, italic=True)
    c.text(615, 296, "weight on duties and rights", 10.5, "middle", INK3, italic=True)
    c.text(360, 338, "horizontal: aggregate-welfare dimension; vertical: duties-and-rights dimension", 11, "middle", INK2)
    c.text(16, 390, "schematic: eigenvalues 4 and 1 at every angle; semi-axes proportional to their square roots", 10.5,
           "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 7
def fig_07_1():
    rows = [("Gemini 2.0 Flash", -12.3, 8.7, 3.1), ("Gemini 2.5 Flash", -10.5, 6.2, 2.8),
            ("Gemini 3 Flash", -11.8, 7.4, 1.4), ("Gemini 2.5 Pro", -14.1, 9.8, 4.2), ("Claude", -9.1, -1.5, 2.1)]
    ratios = [abs(e) / abs(d) for _, e, d, _ in rows]
    assert all(1.35 < r < 1.75 for r in ratios[:4]) and abs(ratios[4] - 6.1) < 0.05
    assert min(abs(r[1]) for r in rows) == 9.1 and max(abs(r[1]) for r in rows) == 14.1
    assert all(r[2] > 0 for r in rows[:4]) and rows[4][2] < 0
    p = reg("chapters/ch07_social_cognition.md", "7.1",
            "Framing drift by model, as the table of Section 7.4 reports it: the change in the total harm score, on a "
            "70-point scale, from the neutral text to the rewritten text. For each model the upper bar is the drift "
            "under euphemistic rewriting, the lower bar the drift under dramatic rewriting, and the grey bracket the "
            "control drift from re-judging the same neutral text, drawn on both sides of zero. Euphemistic rewriting "
            "lowers the score for all five models; dramatic rewriting raises it for the four Gemini models and lowers "
            "it by 1.5 for Claude, less than Claude's control drift of 2.1. The asymmetry ratio of Definition 7.3 is "
            "6.1 for Claude and 1.4 to 1.7 for the Gemini models.",
            "## 7.6 The Selectivity Pattern: Which Symmetries Hold")
    c = Canvas(720, 440, "Euphemistic framing lowers every harm score; dramatic raises four")
    ax = Axes(c, 170, 64, 500, 300, (-16, 12), (0, 5), [-16, -12, -8, -4, 0, 4, 8, 12], [],
              "drift in total harm score from neutral (points on a 70-point scale)", "")
    for v in (-16, -12, -8, -4, 4, 8, 12):
        c.line(ax.X(v), ax.y0, ax.X(v), ax.y0 + ax.h, GRID, 1)
    x0 = ax.X(0)
    for i, (name, e, d, ctl) in enumerate(rows):
        y = ax.y0 + 60 * i + 30
        c.text(ax.x0 - 12, y + 4, name, 11.5, "end", INK2)
        _lbar(c, x0, y - 17, x0 - ax.X(e), 12, SERIES[0], f"{name}, euphemistic drift {e}")
        c.text(ax.X(e) - 7, y - 7, f"−{abs(e):.1f}", 10.5, "end", INK)
        if d > 0:
            c.hrect(x0, y - 1, ax.X(d) - x0, 12, SERIES[1], title=f"{name}, dramatic drift +{d}")
            c.text(ax.X(d) + 7, y + 9, f"+{d:.1f}", 10.5, "start", INK)
        else:
            _lbar(c, x0, y - 1, x0 - ax.X(d), 12, SERIES[1], f"{name}, dramatic drift {d}")
            c.text(x0 + 7, y + 9, f"−{abs(d):.1f}", 10.5, "start", INK)
        yb = y + 20
        c.line(ax.X(-ctl), yb, ax.X(ctl), yb, INK3, 1.5)
        c.line(ax.X(-ctl), yb - 3, ax.X(-ctl), yb + 3, INK3, 1.5)
        c.line(ax.X(ctl), yb - 3, ax.X(ctl), yb + 3, INK3, 1.5)
        c.text(ax.X(ctl) + 7, yb + 4, f"control ±{ctl:.1f}", 10, "start", INK3)
    c.line(x0, ax.y0, x0, ax.y0 + ax.h, INK3, 1.5)
    legend(c, 170, 50, [("euphemistic rewriting", SERIES[0]), ("dramatic rewriting", SERIES[1])])
    c.text(16, 430, "values from the table of Section 7.4; asymmetry ratio |euphemistic| / |dramatic|: Claude 6.1, Gemini 1.4 to 1.7",
           10.5, "start", INK3, italic=True)
    c.save(p)


def fig_07_2():
    dims = ["physical", "emotional", "financial", "autonomy", "trust", "social", "identity"]
    j0, je, jd = [0, 7, 8, 6, 8, 5, 2], [0, 4, 5, 3, 5, 3, 1], [1, 9, 9, 8, 9, 7, 3]
    assert (sum(j0), sum(je), sum(jd)) == (36, 21, 46)
    assert sum(abs(a - b) for a, b in zip(je, j0)) == 15 and sum(abs(a - b) for a, b in zip(jd, j0)) == 10
    assert round(sum(je) / sum(j0), 2) == 0.58 and round(sum(jd) / sum(j0), 2) == 1.28
    p = reg("chapters/ch07_social_cognition.md", "7.2",
            "The three judgment vectors of the worked example of Section 7.11, an illustrative example built on the "
            "scenario of Maya Chen's running example. The horizontal axis lists the seven harm dimensions and the "
            "vertical axis is the harm score on each, from 0 to 10. The euphemistic version lies at or below the "
            "neutral version on every dimension and the dramatic version above it, so the profile keeps its shape "
            "while its size changes. The totals are 36, 21 and 46, which gives the scaling factors of about 0.58 and "
            "1.28 that the example reads as a conformal change.",
            "## 7.12 Implications for Moral AI")
    c = Canvas(720, 400, "Illustrative: framing rescales the judgment and keeps its shape")
    ax = Axes(c, 70, 62, 600, 256, (0, 7), (0, 10), [], [0, 2, 4, 6, 8, 10], "", "harm score (0 to 10)")
    for i, d in enumerate(dims):
        c.text(ax.X(i + 0.5), ax.y0 + ax.h + 18, d, 11, "middle", INK2)
    series = [("dramatic, total 46", jd, SERIES[1]), ("neutral, total 36", j0, SERIES[2]),
              ("euphemistic, total 21", je, SERIES[0])]
    for name, vals, col in series:
        pts = [(ax.X(i + 0.5), ax.Y(v)) for i, v in enumerate(vals)]
        c.polyline(pts, col, 2, title=name)
        for (px, py), d, v in zip(pts, dims, vals):
            c.dot(px, py, col, 4.5, title=f"{name.split(',')[0]}, {d}: {v}")
    legend(c, 70, 48, [(n, col) for n, _, col in series])
    c.text(16, 390, "illustrative worked example (Section 7.11): 21 / 36 ≈ 0.58 and 46 / 36 ≈ 1.28", 10.5, "start",
           INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 8
def fig_08_2():
    levels = [("irrelevant", 0.3, 0.4), ("moderate", 4.1, 4.4), ("extreme", 8.2, 6.7)]
    assert abs(levels[2][1] / levels[1][1] - 2.0) < 1e-9 and levels[0][1] < levels[1][1] < levels[2][1]
    p = reg("chapters/ch08_learning.md", "8.1",
            "Graded belief revision on L4, as Section 8.5 reports it for the three Gemini models. The horizontal axis "
            "is the intensity of the corrective evidence and the vertical axis the size of the mean revision, the "
            "downward shift in severity in points. Irrelevant evidence moves the judgment by 0.3 points, moderate "
            "evidence by 4.1 and extreme evidence by 8.2, with the z values against the control arm printed above the "
            "bars. The ordering is the one Definition 8.2 requires of a graded revision function.",
            "## 8.6 The Discrimination Failure: A Geometric Analysis")
    c = Canvas(720, 400, "Revision grows with the strength of the evidence")
    ax = Axes(c, 80, 58, 330, 262, (0, 3), (0, 10), [], [0, 2, 4, 6, 8, 10], "intensity of corrective evidence",
              "mean revision (severity points, downward)")
    for i, (name, v, z) in enumerate(levels):
        x = ax.X(i + 0.5) - 12
        c.rect(x, ax.Y(v), 24, ax.Y(0) - ax.Y(v), SERIES[0], title=f"{name} evidence: revision −{v} points, z = {z}")
        c.text(x + 12, ax.Y(v) - 20, f"−{v:.1f}", 11.5, "middle", INK, "600")
        c.text(x + 12, ax.Y(v) - 6, f"z = {z:.1f}", 10.5, "middle", INK2)
        c.text(x + 12, ax.y0 + ax.h + 16, name, 11, "middle", INK2)
    x0 = 450
    c.text(x0, 96, "Definition 8.2, graded revision", 12, "start", INK, "600")
    c.text(x0, 118, "e1 > e2  implies  r(e1) > r(e2)", 11.5, "start", INK2)
    c.text(x0, 136, "ideal form: r(e) = α e + β, with β ≈ 0", 11.5, "start", INK2)
    c.text(x0, 178, "L4, three Gemini models", 12, "start", INK, "600")
    c.text(x0, 200, "extreme > moderate > irrelevant", 11.5, "start", INK2)
    c.text(x0, 218, "irrelevant evidence: not significant", 11.5, "start", INK2)
    c.text(x0, 236, "(z = 0.4, p = 0.69)", 11.5, "start", INK2)
    c.text(16, 390, "values from the table of Section 8.5; the evidence levels are categories, not a measured scale", 10.5,
           "start", INK3, italic=True)
    c.save(p)


def fig_08_3():
    lam = 0.5
    phi = math.acos(lam)
    assert abs(math.degrees(phi) - 60) < 1e-9
    p = reg("chapters/ch08_learning.md", "8.2",
            "The correction filter of Definition 8.3 as a projection, a schematic. The horizontal line is the "
            "subspace V of valid correction directions, the thin arrow is the evidence vector E that a correction "
            "produces, and the thick arrow is the filtered evidence, the projection of E onto V. A valid correction "
            "lies in V and passes in full, and with a perfect filter an invalid correction is orthogonal to V and "
            "nothing passes. With a leaky filter a fraction λ of the invalid evidence passes, the leakage of "
            "Proposition 8.2, drawn here for the illustrative value λ = 0.5.",
            "## 8.7 The Sycophancy-Stability Correlation")
    c = Canvas(720, 400, "The correction filter is a projection; sycophancy is its leakage")
    L = 130
    panels = [("valid correction", "E lies in V: all of it passes", 0.0, SERIES[0]),
              ("invalid correction, perfect filter", "E is orthogonal to V: nothing passes", math.pi / 2, SERIES[2]),
              ("invalid correction, leaky filter", "a fraction λ = 0.5 passes", phi, SERIES[1])]
    for i, (head, sub, ang, col) in enumerate(panels):
        x0, y0 = 40 + i * 232, 290
        c.text(x0 + 88, 76, head, 12, "middle", INK, "600")
        c.text(x0 + 88, 94, sub, 11, "middle", INK2)
        c.line(x0 - 8, y0, x0 + 184, y0, INK3, 1.5)
        c.text(x0 + 184, y0 + 18, "V: valid directions", 10.5, "end", INK3, italic=True)
        ex, ey = x0 + 20 + L * math.cos(ang), y0 - L * math.sin(ang)
        px = x0 + 20 + L * math.cos(ang)
        if ang > 1e-6:
            c.line(ex, ey, px, y0, INK3, 1.2, dash="3 4")
            _vec(c, x0 + 20, y0, ex, ey, INK2, 1.5)
            c.text(ex + 10, ey + 4, "E", 12.5, "start", INK, "600")
        else:
            _vec(c, x0 + 20, y0 - 22, ex, ey - 22, INK2, 1.5)
            c.text(x0 + 20 + L / 2, y0 - 32, "E", 12.5, "middle", INK, "600")
        if math.cos(ang) > 1e-6:
            _vec(c, x0 + 20, y0, px, y0, col, 3.5)
            c.text(x0 + 20 + (px - x0 - 20) / 2, y0 - 9 if ang < 1e-6 else y0 + 36,
                   "filtered = E" if ang < 1e-6 else "filtered = λ |E|", 11, "middle", INK)
        else:
            c.dot(x0 + 20, y0, col, 5)
            c.text(x0 + 34, y0 + 36, "filtered = 0", 11, "start", INK)
    c.text(16, 390, "schematic: filtered evidence = projection of E onto V; λ = 0.5 is illustrative, not a measured leakage",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 9
def fig_09_2():
    pro, f20 = (0.500, 0.000), (0.042, 0.827)
    for tau in (0.25, 0.5):
        assert not any(m3 > tau and m4 > tau for m3, m4 in (pro, f20))   # Quadrant I holds neither point
    assert pro[0] > 0.25 and pro[1] <= 0.25 and f20[0] <= 0.25 and f20[1] > 0.25   # II and IV at tau = 0.25
    p = reg("chapters/ch09_metacognition.md", "9.2",
            "The metacognitive configuration space of Definition 9.5 at its true scale: self-monitoring accuracy M3 "
            "on the horizontal axis and the effort scaling index M4 on the vertical axis. The solid lines are the "
            "threshold 0.25 of Technical Appendix 9B, the dashed lines the threshold 0.5, and the shaded region is "
            "Quadrant I at the threshold 0.25. Only Gemini 2.5 Pro at (0.500, 0.000) and Gemini 2.0 Flash at (0.042, "
            "0.827) are drawn, the two models whose values the chapters agree on; neither lies in Quadrant I at "
            "either threshold. Section 9.7 also places Gemini 3 Flash and Gemini 2.5 Flash in Quadrant IV, and with "
            "four models a sampling artifact cannot be excluded.",
            "## 9.9 Metacognition as a Two-Dimensional Manifold")
    c = Canvas(720, 400, "The two settled points of the M3 and M4 plane lie outside Quadrant I")
    ax = Axes(c, 80, 50, 290, 290, (0, 1), (0, 1), [0, 0.25, 0.5, 0.75, 1], [0, 0.25, 0.5, 0.75, 1],
              "M3, self-monitoring accuracy", "M4, effort scaling index")
    c.line(ax.x0, ax.y0, ax.x0, ax.y0 + ax.h, GRID, 1)
    c.line(ax.x0 + ax.w, ax.y0, ax.x0 + ax.w, ax.y0 + ax.h, GRID, 1)
    _band(c, ax.X(0.25), ax.Y(1), ax.X(1) - ax.X(0.25), ax.Y(0.25) - ax.Y(1), CRITICAL, 0.13)
    c.line(ax.X(0.25), ax.y0, ax.X(0.25), ax.y0 + ax.h, INK3, 1.5)
    c.line(ax.x0, ax.Y(0.25), ax.x0 + ax.w, ax.Y(0.25), INK3, 1.5)
    c.line(ax.X(0.5), ax.y0, ax.X(0.5), ax.y0 + ax.h, INK3, 1.2, dash="4 4")
    c.line(ax.x0, ax.Y(0.5), ax.x0 + ax.w, ax.Y(0.5), INK3, 1.2, dash="4 4")
    c.text(ax.X(0.76), ax.Y(0.84), "Quadrant I", 12, "middle", INK, "600")
    c.text(ax.X(0.76), ax.Y(0.84) + 16, "no model", 11, "middle", INK2)
    c.text(ax.X(0.76), ax.Y(0.12) + 2, "II", 12, "middle", INK2, "600")
    c.text(ax.X(0.125), ax.Y(0.12) + 2, "III", 12, "middle", INK2, "600")
    c.text(ax.X(0.125), ax.Y(0.62), "IV", 12, "middle", INK2, "600")
    c.dot(ax.X(pro[0]), ax.Y(pro[1]), SERIES[0], 5.5, title="Gemini 2.5 Pro: M3 0.500, M4 0.000")
    c.dot(ax.X(f20[0]), ax.Y(f20[1]), SERIES[1], 5.5, title="Gemini 2.0 Flash: M3 0.042, M4 0.827")
    c.text(ax.X(pro[0]) + 10, ax.Y(pro[1]) - 10, "Pro", 11.5, "start", INK, "600")
    c.text(ax.X(f20[0]) + 11, ax.Y(f20[1]) + 4, "Flash 2.0", 11.5, "start", INK, "600")
    x0 = 420
    c.text(x0, 84, "Gemini 2.5 Pro   (0.500, 0.000)", 11.5, "start", INK2)
    c.text(x0, 102, "knows which items are hard, does not", 11, "start", INK3)
    c.text(x0, 118, "scale effort: Quadrant II at τ = 0.25", 11, "start", INK3)
    c.text(x0, 150, "Gemini 2.0 Flash   (0.042, 0.827)", 11.5, "start", INK2)
    c.text(x0, 168, "scales effort, does not know which", 11, "start", INK3)
    c.text(x0, 184, "items are hard: Quadrant IV", 11, "start", INK3)
    c.line(x0, 214, x0 + 26, 214, INK3, 1.5)
    c.text(x0 + 34, 218, "threshold τ = 0.25 (Appendix 9B)", 11, "start", INK2)
    c.line(x0, 234, x0 + 26, 234, INK3, 1.2, dash="4 4")
    c.text(x0 + 34, 238, "threshold τ = 0.5", 11, "start", INK2)
    c.text(x0, 276, "Gemini 3 Flash and Gemini 2.5 Flash:", 11, "start", INK3)
    c.text(x0, 292, "placed in IV by Section 9.7; their values", 11, "start", INK3)
    c.text(x0, 308, "differ between chapters, so not drawn", 11, "start", INK3)
    legend(c, x0, 340, [("Pro", SERIES[0]), ("Flash 2.0", SERIES[1]), ("Quadrant I", CRITICAL)])
    c.text(16, 390, "values from the table of Section 9.7, the same in Section 16.7; four models, exploratory", 10.5,
           "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 10
def fig_10_1():
    rank = lambda r: (1 + r) ** 2 / (1 + r * r)  # noqa: E731
    assert abs(rank(3.0) - 1.6) < 1e-12 and abs((0.75 + 0.25) ** 2 / (0.75 ** 2 + 0.25 ** 2) - 1.6) < 1e-12
    assert rank(1.0) == 2.0
    p = reg("chapters/ch10_attention.md", "10.1",
            "The effective rank of Definition 10.3 for a metric with two eigenvalues, as a function of their ratio. "
            "The horizontal axis is the ratio of the attention weight on the primary stream to the weight on the "
            "secondary stream, on a logarithmic scale, and the vertical axis is the participation ratio of the two "
            "eigenvalues. An isotropic metric, ratio 1, has effective rank 2, and the rank falls toward 1 as the "
            "weight concentrates on one stream. The marked point is the worked example of Section 10.11, a "
            "hypothetical model: a ratio of 3.0, with 75 percent of the budget on the primary stream, gives an "
            "effective rank of 1.6.",
            "## 10.12 The Attention Filter as Geometric Object")
    c = Canvas(720, 400, "Effective rank falls from 2 toward 1 as attention concentrates")
    ax = Axes(c, 80, 52, 540, 268, (1, 30), (0.9, 2.1), [1, 2, 3, 5, 10, 20, 30], [1.0, 1.2, 1.4, 1.6, 1.8, 2.0],
              "ratio of attention weights a1 / a2 (logarithmic scale)", "effective rank", xlog=True)
    y1 = ax.Y(1.0)
    c.line(ax.x0, y1, ax.x0 + ax.w, y1, INK3, 1.5, dash="4 4")
    c.text(ax.x0 + ax.w - 4, y1 + 15, "rank-1 limit: one stream only", 10.5, "end", INK2, italic=True)
    rs = [10 ** (i * math.log10(30) / 200) for i in range(201)]
    c.polyline([(ax.X(r), ax.Y(rank(r))) for r in rs], SERIES[0], 2.5, title="(a1 + a2)² / (a1² + a2²)")
    c.dot(ax.X(1), ax.Y(2), SERIES[2], 5, title="isotropic: ratio 1, effective rank 2")
    c.text(ax.X(1) + 12, ax.Y(2) - 8, "isotropic: rank 2", 11, "start", INK)
    px, py = ax.X(3.0), ax.Y(1.6)
    c.line(px, py, px, ax.y0 + ax.h, INK3, 1.2, dash="3 4")
    c.line(ax.x0, py, px, py, INK3, 1.2, dash="3 4")
    c.dot(px, py, CRITICAL, 5.5, title="worked example: ratio 3.0, effective rank 1.6")
    c.text(px + 12, py - 28, "worked example of Section 10.11", 11.5, "start", INK, "600")
    c.text(px + 12, py - 12, "a1 / a2 = 3.0  →  rank 1.6", 11, "start", INK2)
    c.text(ax.x0 + ax.w - 4, ax.y0 + 14, "rank = (a1 + a2)² / (a1² + a2²)", 11.5, "end", INK2, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 11
def fig_11_1():
    g1, g2 = (4.0, 0.0, 1.0), (1.0, 0.0, 4.0)
    mid = tuple(0.5 * a + 0.5 * b for a, b in zip(g1, g2))
    assert mid == (2.5, 0.0, 2.5)                       # the blend is isotropic halfway
    r45 = _metric(4.0, 1.0, math.pi / 4)
    e1, e2, _ = _eig(r45)
    assert abs(e1 - 4) < 1e-9 and abs(e2 - 1) < 1e-9     # the rotation is not
    assert all(abs(a - b) < 1e-9 for a, b in zip(_metric(4.0, 1.0, math.pi / 2), g2))
    p = reg("chapters/ch11_executive_control.md", "11.1",
            "A framework switch between two attention metrics, drawn under the two definitions the volume gives. The "
            "lower row is the metric-regime transition of Definition 11.2, the weighted average (1 - α) g1 + α g2, "
            "whose intermediate metrics are blends that weight both dimensions equally at the halfway point. The "
            "upper row is the rotation of Definition 6.1 between the same two metrics, which keeps the shape and "
            "turns the axes, so the two definitions agree at the ends and differ in between. Each ellipse has semi- "
            "axes proportional to the square roots of the eigenvalues, and the metrics diag(4, 1) and diag(1, 4) are "
            "illustrative.",
            "## 11.3 Inhibitory Control as Maintaining Governance Margin Near the Safety Boundary")
    c = Canvas(720, 440, "Two definitions of a framework switch: rotate, or blend")
    xs = [170 + i * 122 for i in range(5)]
    c.text(16, 120, "Definition 6.1", 12, "start", INK, "600")
    c.text(16, 138, "rotation", 11.5, "start", INK2)
    c.text(16, 290, "Definition 11.2", 12, "start", INK, "600")
    c.text(16, 308, "weighted average", 11.5, "start", INK2)
    for i, x in enumerate(xs):
        th, al = 22.5 * i, 0.25 * i
        _ellipse(c, x, 128, _metric(4.0, 1.0, math.radians(th)), 22, SERIES[0], f"rotation, θ = {th}°")
        c.text(x, 196, f"θ = {th:g}°", 11, "middle", INK2)
        g = tuple((1 - al) * a + al * b for a, b in zip(g1, g2))
        _ellipse(c, x, 298, g, 22, SERIES[1], f"blend, α = {al}")
        c.text(x, 366, f"α = {al:g}", 11, "middle", INK2)
    c.text(xs[0], 66, "framework 1: g1", 11.5, "middle", INK2)
    c.text(xs[4], 66, "framework 2: g2", 11.5, "middle", INK2)
    c.text(xs[2], 66, "halfway", 11.5, "middle", INK2)
    c.text(xs[2], 388, "equal weight on both dimensions", 10.5, "middle", INK3, italic=True)
    c.text(xs[2], 218, "same shape, turned 45°", 10.5, "middle", INK3, italic=True)
    c.text(16, 430, "schematic: g1 = diag(4, 1), g2 = diag(1, 4), illustrative; semi-axes proportional to sqrt(eigenvalue)",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 12
def fig_12_2():
    phi = lambda b, x: 1 / (1 + math.exp(-b * x))  # noqa: E731
    b0 = 3.0
    slope = b0 / 4                                      # slope of phi at the threshold
    assert abs((phi(b0, 1e-6) - phi(b0, -1e-6)) / 2e-6 - slope) < 1e-6
    width = 1 / slope                                   # the tangent runs from 0 to 1 over 4 / beta
    assert abs(width - 4 / b0) < 1e-12
    p = reg("chapters/ch12_dual_process.md", "12.2",
            "The order parameter of Technical Appendix 12A, φ = 1 / (1 + exp(-β x)), where x is the scalar curvature "
            "measured from the threshold, on the horizontal axis in curvature units. The vertical axis is φ, the "
            "weight on geodesic computation against gradient following, and the dashed step is the sharp threshold of "
            "Definition 12.3, the limit of large β. The two curves are drawn for β = 3 and β = 5, the range the "
            "appendix attaches to the sigmoid of Maya Chen's hypothetical experiment, so they are illustrative. The "
            "bracket marks the transition width of about 4 / β for β = 3.",
            "## Technical Appendix 12B: Override Fraction --- Analytical Bounds")
    c = Canvas(720, 400, "The regime transition as a soft step in curvature (illustrative β)")
    ax = Axes(c, 80, 62, 540, 256, (-2, 2), (0, 1.05), [-2, -1, 0, 1, 2], [0, 0.25, 0.5, 0.75, 1.0],
              "scalar curvature relative to the threshold, R − R* (curvature units)", "order parameter φ")
    xz = ax.X(0)
    for (xa, ya, xb, yb) in ((ax.X(-2), ax.Y(0), xz, ax.Y(0)), (xz, ax.Y(0), xz, ax.Y(1)), (xz, ax.Y(1), ax.X(2), ax.Y(1))):
        c.line(xa, ya, xb, yb, INK3, 1.5, dash="5 4")
    xs = [-2 + i * 4 / 240 for i in range(241)]
    for j, b in enumerate((3.0, 5.0)):
        c.polyline([(ax.X(x), ax.Y(phi(b, x))) for x in xs], SERIES[j], 2.5, title=f"β = {b:g}")
    yb = ax.Y(0.5)
    xa, xb2 = ax.X(-width / 2), ax.X(width / 2)
    c.line(xa, ax.Y(0.12), xb2, ax.Y(0.12), INK2, 1.5)
    c.line(xa, ax.Y(0.12) - 4, xa, ax.Y(0.12) + 4, INK2, 1.5)
    c.line(xb2, ax.Y(0.12) - 4, xb2, ax.Y(0.12) + 4, INK2, 1.5)
    c.text(xb2 + 10, ax.Y(0.12) + 4, "width ≈ 4 / β = 1.33 for β = 3", 11, "start", INK)
    c.dot(xz, yb, INK, 3.5, title="φ = 0.5 at the threshold")
    c.text(ax.X(-1.95), ax.Y(0.9), "System 1:", 11.5, "start", INK, "600")
    c.text(ax.X(-1.95), ax.Y(0.9) + 16, "gradient following", 11, "start", INK2)
    c.text(ax.X(1.95), ax.Y(0.78), "System 2:", 11.5, "end", INK, "600")
    c.text(ax.X(1.95), ax.Y(0.78) + 16, "geodesic computation", 11, "end", INK2)
    legend(c, 80, 48, [("β = 3", SERIES[0]), ("β = 5", SERIES[1]), ("β → ∞: sharp threshold (Definition 12.3)", INK3)])
    c.text(16, 390, "β = 3 to 5 comes from the hypothetical experiment of the running example: illustrative, not fitted to data",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 13
def fig_13_2():
    ages = [2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]
    dims = [3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 17]
    assert all(b > a for a, b in zip(dims, dims[1:])) and len(ages) == len(dims)
    metric = [(2.5, 0 / 3), (3, 0 / 3), (4, 0 / 4), (5, 1 / 4), (6, 2 / 5), (7, 4 / 5), (8, 5 / 5)]
    paths = [(4, 3 / 6), (5, 4 / 6), (6, 5 / 6), (7, 6 / 6)]
    ops = [(7, 1 / 3), (8, 2 / 3), (9, 2 / 3), (10, 2.5 / 3), (11, 3 / 3)]
    assert metric[5][1] - metric[4][1] == max(b[1] - a[1] for a, b in zip(metric, metric[1:]))   # sharpest step: 6 to 7
    p = reg("chapters/ch13_development.md", "13.2",
            "The illustrative longitudinal data of Section 13.8, constructed for the hypothetical case of Maya Chen's "
            "running example to show the pattern the model predicts; they are not measurements. The upper panel is "
            "the estimated dimensionality of the cognitive manifold against age in years, with the range 18 to 20 at "
            "age 12 drawn as a bar. The lower panel is the fraction of tasks passed on metric consistency, path "
            "connectivity and operation closure, each drawn only at the ages where the table gives a count. The "
            "dashed lines mark the two transitions the section names, metric stabilization between ages 6 and 7 and "
            "operation closure between ages 10 and 11.",
            "## 13.9 The Development of the Curvature Threshold")
    c = Canvas(720, 520, "Illustrative data: dimension grows steadily, two measures jump")
    a1 = Axes(c, 80, 64, 580, 160, (1.5, 12.5), (0, 22), [], [0, 5, 10, 15, 20], "", "estimated dimensionality")
    a2 = Axes(c, 80, 272, 580, 160, (1.5, 12.5), (0, 1.1), list(range(2, 13)), [0, 0.5, 1.0], "age (years)",
              "fraction of tasks passed")
    for t, lab in ((6.5, "metric stabilization"), (10.5, "operation closure")):
        for a in (a1, a2):
            c.line(a.X(t), a.y0, a.X(t), a.y0 + a.h, INK3, 1.2, dash="4 4")
        c.text(a1.X(t) - 6, a1.y0 + 12, lab, 10.5, "end", INK2, italic=True)
    pts = [(a1.X(a), a1.Y(d)) for a, d in zip(ages, dims)]
    c.polyline(pts, SERIES[0], 2, title="estimated dimensionality")
    for (px, py), a, d in zip(pts, ages, dims):
        c.dot(px, py, SERIES[0], 4, title=f"age {a:g}: {d} dimensions")
    c.line(pts[-1][0], pts[-1][1], a1.X(12), a1.Y(19), SERIES[0], 2, dash="3 4")
    c.line(a1.X(12), a1.Y(18), a1.X(12), a1.Y(20), SERIES[0], 4)
    c.text(a1.X(12) + 9, a1.Y(19) + 4, "18 to 20", 10.5, "start", INK)
    c.text(a1.X(2) + 8, a1.Y(3) + 14, "3", 10.5, "start", INK)
    c.text(a1.X(11) - 9, a1.Y(17) - 4, "17", 10.5, "end", INK)
    series = [("metric consistency", metric, SERIES[1]), ("path connectivity", paths, SERIES[2]),
              ("operation closure", ops, SERIES[3])]
    for name, data, col in series:
        pp = [(a2.X(a), a2.Y(v)) for a, v in data]
        c.polyline(pp, col, 2, title=name)
        for (px, py), (a, v) in zip(pp, data):
            c.dot(px, py, col, 4, title=f"{name}, age {a:g}: {v:.2f}")
    legend(c, 80, 256, [(n, col) for n, _, col in series], 11)
    c.text(16, 510, "ILLUSTRATIVE: constructed data of the running example (Section 13.8), not measurements of a child",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 14
def fig_14_1():
    a_anx, a_over, flat = 3.0, 0.5, 6.0
    assert a_anx > 1 > a_over > 0
    p = reg("chapters/ch14_pathology.md", "14.1",
            "The heuristic field defects of Sections 14.3 and 14.4, as the chapter defines them, drawn as the "
            "estimated cost-to-go h on the vertical axis against the true cost-to-go d on the horizontal axis. The "
            "inflation factor of Definition 14.5 is the ratio h / d, the slope of a line through the origin: 1 for a "
            "healthy estimate, far above 1 for the inflated field posited for anxiety, and below 1 for the deflated "
            "field of the overconfidence in Chapter 9. The collapsed field posited for depression is flat, so its "
            "gradient is near zero and the ratio is undefined. The ratios 3 and 0.5 and the flat level are "
            "illustrative.",
            "## 14.5 Autism as Metric Rigidity")
    c = Canvas(720, 400, "Four heuristic fields: accurate, inflated, deflated, collapsed")
    ax = Axes(c, 80, 52, 440, 268, (0, 10), (0, 12), [0, 2, 4, 6, 8, 10], [0, 2, 4, 6, 8, 10, 12],
              "true cost-to-go d(x, goal)", "estimated cost-to-go h(x)")
    c.line(ax.X(0), ax.Y(0), ax.X(10), ax.Y(10), SERIES[0], 2.5)
    c.line(ax.X(0), ax.Y(0), ax.X(4), ax.Y(12), SERIES[1], 2.5)
    c.line(ax.X(0), ax.Y(0), ax.X(10), ax.Y(5), SERIES[2], 2.5)
    c.line(ax.X(0), ax.Y(flat), ax.X(10), ax.Y(flat), SERIES[3], 2.5, dash="7 5")
    x0 = ax.x0 + ax.w + 14
    c.text(ax.X(4) + 10, ax.Y(12) + 12, "inflated, h / d = 3", 11.5, "start", INK, "600")
    c.text(ax.X(4) + 10, ax.Y(12) + 28, "anxiety (posited)", 11, "start", INK2)
    c.text(x0, ax.Y(10) + 2, "healthy, h / d = 1", 11.5, "start", INK, "600")
    c.text(x0, ax.Y(10) + 18, "accurate estimate", 11, "start", INK2)
    c.text(x0, ax.Y(flat) - 2, "collapsed, flat", 11.5, "start", INK, "600")
    c.text(x0, ax.Y(flat) + 14, "depression (posited):", 11, "start", INK2)
    c.text(x0, ax.Y(flat) + 29, "gradient ≈ 0", 11, "start", INK2)
    c.text(x0, ax.Y(5) + 34, "deflated, h / d = 0.5", 11.5, "start", INK, "600")
    c.text(x0, ax.Y(5) + 50, "overconfidence (Ch. 9)", 11, "start", INK2)
    c.text(16, 390, "schematic of Definitions 14.2, 14.4 and 14.5; the ratios 3 and 0.5 and the flat level are illustrative",
           10.5, "start", INK3, italic=True)
    c.save(p)


def fig_14_2():
    rng = random.Random(11)
    n = 240
    stable = [1.0 if i < n // 2 else 2.0 for i in range(n)]
    rigid = [1.0] * n
    unstable, v = [], 1.0
    for i in range(n):
        target = 1.0 if i < n // 2 else 2.0
        v += rng.gauss(0, 0.11) + 0.03 * (target - v)   # endogenous noise plus a weak pull to the task's setting
        v = min(max(v, 0.05), 2.95)
        unstable.append(v)
    msi = lambda s: sum(abs(b - a) for a, b in zip(s, s[1:])) / (len(s) - 1)  # noqa: E731
    assert msi(unstable) > msi(stable) > msi(rigid) == 0.0   # the ordering of Technical Appendix 14A
    p = reg("chapters/ch14_pathology.md", "14.2",
            "Three attention metrics over time, a schematic of the definitions of Sections 14.2 and 14.5: each panel "
            "shows one metric component against time, with a change of context at the dashed line. The stable metric "
            "changes only when the context changes, and the rigid metric of Definition 14.6, the posited account of "
            "autism, does not change even then. The unstable metric of Definition 14.1, the posited account of ADHD, "
            "also moves by an endogenous noise term while the context is constant; its trace is a simulated random "
            "walk, not data. The mean change between successive samples orders the three as Technical Appendix 14A "
            "predicts: unstable above stable above rigid.",
            "## 14.6 The Four Pathologies as a Geometric Taxonomy")
    c = Canvas(720, 440, "Stable, unstable and rigid metrics around one change of context")
    rows = [("stable", "changes only with the context", stable, SERIES[0]),
            ("unstable (Definition 14.1)", "∂g/∂t = ξ(t): endogenous noise", unstable, SERIES[1]),
            ("rigid (Definition 14.6)", "∂g/∂c ≈ 0: no adaptation", rigid, SERIES[2])]
    for r, (name, sub, data, col) in enumerate(rows):
        ax = Axes(c, 250, 62 + r * 112, 420, 84, (0, n - 1), (0, 3), [], [], "", "")
        c.line(ax.x0, ax.y0, ax.x0, ax.y0 + ax.h, GRID, 1)
        xm = ax.X(n / 2 - 0.5)
        c.line(xm, ax.y0 - 4, xm, ax.y0 + ax.h, INK3, 1.2, dash="4 4")
        c.polyline([(ax.X(i), ax.Y(v)) for i, v in enumerate(data)], col, 2, title=name)
        c.text(16, ax.y0 + 36, name, 12, "start", INK, "600")
        c.text(16, ax.y0 + 54, sub, 11, "start", INK2)
        if r == 0:
            c.text(xm - 8, ax.y0 + 8, "context A", 10.5, "end", INK3, italic=True)
            c.text(xm + 8, ax.y0 + 8, "context B", 10.5, "start", INK3, italic=True)
        if r == 2:
            c.text(ax.x0 + ax.w / 2, ax.y0 + ax.h + 20, "time", 11.5, "middle", INK2)
    c.text(238, 118, "metric component", 10.5, "middle", INK3, rotate=-90)
    c.text(16, 430, "schematic: the unstable trace is a simulated random walk, not measured data", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 15
def fig_15_2():
    blocks = [(0, 4, "Input encoding", "projection onto the cognitive manifold"),
              (5, 8, "Feature extraction", "gradient-following phase (System 1)"),
              (9, 13, "Intermediate processing", "curvature detection phase"),
              (14, 18, "Conflict resolution", "geodesic computation phase (System 2)"),
              (19, 25, "Integration", "trajectory convergence"),
              (26, 32, "Output formation", "projection from manifold to output space")]
    assert blocks[0][0] == 0 and blocks[-1][1] == 32
    assert all(b[0] == a[1] + 1 for a, b in zip(blocks, blocks[1:]))   # the six blocks tile layers 0 to 32
    p = reg("chapters/ch15_llm_cognition.md", "15.2",
            "The layer-by-layer mapping of Section 15.4, which the chapter calls illustrative and specific to the "
            "model and task of Maya Chen's running example. The horizontal axis is the layer index, 0 to 32, and each "
            "bar spans one block of layers, labelled with the processing function and the geometric reading the table "
            "gives. The marked block, layers 14 to 18, is where the running example places its illustrative curvature "
            "spike. Different models and tasks may have different layer assignments.",
            "## 15.5 In-Context Learning as Local Metric Adaptation")
    c = Canvas(720, 400, "Illustrative mapping: layer blocks as phases of one trajectory")
    x0, w, top, rh = 40, 310, 64, 44
    X = lambda l: x0 + w * l / 33  # noqa: E731
    for l in (0, 5, 9, 14, 19, 26, 33):
        c.line(X(l), top - 6, X(l), top + 6 * rh, GRID, 1)
    for l in (0, 5, 9, 14, 19, 26):
        c.text(X(l) + 2, top + 6 * rh + 16, str(l), 10.5, "start", INK2)
    c.text(X(33), top + 6 * rh + 16, "32", 10.5, "end", INK2)
    c.text(x0 + w / 2, top + 6 * rh + 34, "layer index", 11.5, "middle", INK2)
    for i, (a, b, fn, geo) in enumerate(blocks):
        y = top + i * rh
        hot = (a, b) == (14, 18)
        col = CRITICAL if hot else SERIES[0] if i in (0, 5) else SERIES[2]
        c.add(f'<rect x="{X(a) + 1:.2f}" y="{y + 9:.2f}" width="{X(b + 1) - X(a) - 2:.2f}" height="22" rx="4" '
              f'fill="{col}"><title>layers {a} to {b}: {fn}, {geo}</title></rect>')
        c.text(374, y + 17, f"Layers {a} to {b}: {fn}", 11.5, "start", INK, "600")
        c.text(374, y + 33, geo + ("; curvature spike (illustrative)" if hot else ""), 10.5, "start", INK2)
    legend(c, 40, 48, [("projection in or out", SERIES[0]), ("on the manifold", SERIES[2]), ("curvature spike", CRITICAL)])
    c.text(16, 390, "illustrative: the layer assignment belongs to the hypothetical model of the running example", 10.5,
           "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 17
def fig_17_1():
    b = 0.4
    reach = lambda th: 1 / (1 - b * math.cos(th))  # noqa: E731   F(v) = |v| - b v1 = 1
    fwd, back = reach(0.0), reach(math.pi)
    assert abs(fwd - 1 / 0.6) < 1e-12 and abs(back - 1 / 1.4) < 1e-12 and fwd > 1 > back
    p = reg("chapters/ch17_open_questions.md", "17.1",
            "The open question of Section 17.2 as a schematic: each curve is the set of displacements that cost one "
            "unit of effort from the state at the centre. Under a Riemannian metric a displacement costs the same as "
            "its reverse, so the curve is symmetric about the centre, drawn here as a circle. Under a Finsler norm "
            "the cost depends on the direction, so one unit of effort carries the state farther one way than the "
            "other; the right panel uses one illustrative norm, F(v) = |v| - 0.4 v1, since the chapter does not "
            "specify a form. The direction labels follow the sycophancy asymmetry the section posits, and no "
            "directional distance has been measured.",
            "## 17.3 Can We Measure the Heuristic Field from Neural Activations?")
    c = Canvas(720, 400, "Riemannian or Finsler: does a step cost what its reverse costs?")
    s = 78
    for i, (cx, head, sub) in enumerate(((180, "Riemannian metric", "F(v) = F(−v)"),
                                         (520, "Finsler norm", "F(v) ≠ F(−v) in general"))):
        cy = 212
        c.text(cx, 76, head, 12.5, "middle", INK, "600")
        c.text(cx, 94, sub, 11.5, "middle", INK2)
        c.line(cx - 150, cy, cx + 150, cy, GRID, 1)
        c.line(cx, cy - 100, cx, cy + 100, GRID, 1)
        f = (lambda th: 1.0) if i == 0 else reach
        pts = [(cx + s * f(t) * math.cos(t), cy - s * f(t) * math.sin(t)) for t in [k * math.pi / 90 for k in range(181)]]
        c.polyline(pts, SERIES[i], 2.5, title="unit-cost curve")
        rf, rb = s * f(0.0), s * f(math.pi)
        _vec(c, cx, cy, cx + rf - 2, cy, INK, 2)
        _vec(c, cx, cy, cx - rb + 2, cy, INK2, 2)
        c.dot(cx, cy, INK, 3.5)
        c.text(cx + rf / 2, cy - 10, f"{f(0.0):.2f}", 11, "middle", INK)
        c.text(cx - rb / 2 - 2, cy - 10, f"{f(math.pi):.2f}", 11, "middle", INK)
        c.text(cx + 148, cy + 124, "toward agreement →", 10.5, "end", INK3, italic=True)
        c.text(cx - 148, cy + 124, "← toward disagreement", 10.5, "start", INK3, italic=True)
    c.text(180, 366, "one unit of effort reaches equally far both ways", 11, "middle", INK2)
    c.text(520, 366, "one unit reaches 1.67 one way, 0.71 the other", 11, "middle", INK2)
    c.text(16, 390, "schematic: the Finsler panel uses F(v) = |v| − 0.4 v1, an illustrative norm; nothing here is measured",
           10.5, "start", INK3, italic=True)
    c.save(p)
