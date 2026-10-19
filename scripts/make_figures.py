"""Regenerate every figure in ``figures/``.

Usage, from the repository root::

    python scripts/make_figures.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mme import p01_plaplacian as p01  # noqa: E402
from mme import p04_newton_square_root as p04  # noqa: E402
from mme import p06_weak_convergence as p06  # noqa: E402
from mme import p08_small_dense_open as p08  # noqa: E402
from mme import viz  # noqa: E402
from mme.viz import AMBER, AMBER_WASH, CONTEXT, INK, INK_2, INK_3, NAVY, NAVY_LIGHT, NAVY_WASH, PAPER  # noqa: E402

FIGURES = ROOT / "figures"


# ── 00 · overview ───────────────────────────────────────────────────────────
def fig_overview():
    problems = sorted((ROOT / "problems").glob("*.md"))
    areas = {re.search(r"\*\*Area:\*\* ([^·]+)", p.read_text(encoding="utf-8")).group(1).strip() for p in problems}
    tests = (ROOT / "tests" / "test_problems.py").read_text(encoding="utf-8")
    n_tests = len(re.findall(r"^def test_", tests, flags=re.M))
    return viz.overview(
        [
            (str(len(problems)), "original problems", "each with a wrong and a right answer"),
            (str(len(areas)), "areas", "from analysis to linear algebra"),
            (str(n_tests), "test functions", "every claim recomputed in Python"),
            ("0", "confidential items", "nothing from evaluation platforms"),
        ]
    )


# ── 01 · p-Laplacian ────────────────────────────────────────────────────────
def fig_plaplacian():
    ps = np.linspace(1.25, 5, 300)
    fig, ax = plt.subplots(figsize=(9.6, 5.0))
    ax.plot(ps, [p01.lambda1_wrong(p) for p in ps], color=CONTEXT, lw=1.8, ls=(0, (5, 3)))
    ax.plot(ps, [p01.lambda1_formula(p) for p in ps], color=AMBER, lw=2.4)
    qs = [1.5, 2.0, 3.0, 4.0]
    ax.scatter(qs, [p01.lambda1_shooting(q) for q in qs], s=40, color=PAPER, edgecolors=NAVY, linewidths=1.6, zorder=4)
    ax.set_yscale("log")
    ax.text(4.95, p01.lambda1_formula(4.95) * 1.12, r"correct: $(p-1)\,\pi_p^{\,p}$", color=AMBER, ha="right",
            fontsize=10, fontweight="semibold")  # fmt: skip
    ax.text(4.95, p01.lambda1_wrong(4.95) / 1.25, r"tempting: $\pi_p^{\,p}$", color=INK_3, ha="right", fontsize=9.5)
    ax.text(3.0, p01.lambda1_formula(3) * 1.18, "28.29", color=INK, ha="center", fontsize=9)
    ax.text(3.0, p01.lambda1_wrong(3) / 1.32, "14.14", color=INK_3, ha="center", fontsize=9)
    ax.text(1.3, 120, "circles: shooting method,\nno formula used", color=INK_2, fontsize=8.5, va="top")
    ax.set_xlabel("p")
    ax.set_ylabel("first eigenvalue λ₁ (log scale)")
    ax.grid(which="minor", visible=False)
    viz.headline(fig, "Dropping the factor p − 1 misses λ₁ by exactly that factor",
                 "First eigenvalue of the p-Laplacian on (0, 1). The two answers agree only at p = 2")  # fmt: skip
    return fig


# ── 02 · Fučík spectrum ─────────────────────────────────────────────────────
def fig_fucik():
    fig, ax = plt.subplots(figsize=(7.6, 6.6))
    a = np.linspace(1.0001, 14, 800)

    def curve(m, n):
        """Solutions with m positive and n negative humps: m/sqrt(alpha) + n/sqrt(beta) = 1."""
        rest = 1 - m / np.sqrt(a)
        b = np.where(rest > 0, (n / np.where(rest > 0, rest, 1)) ** 2, np.nan)
        return b

    ax.axvline(1, color=CONTEXT, lw=1.2)
    ax.axhline(1, color=CONTEXT, lw=1.2)
    for m, n in [(1, 2), (2, 1)]:
        ax.plot(a, curve(m, n), color=NAVY_LIGHT, lw=1.4)
    ax.plot(a, curve(1, 1), color=NAVY, lw=2.2)
    ax.plot([0, 14], [0, 14], color=CONTEXT, lw=0.9, ls=(0, (3, 3)))
    for k in (1, 2, 3):
        ax.scatter([k * k], [k * k], s=28, color=PAPER, edgecolors=INK_3, linewidths=1.2, zorder=3)
    ax.text(9.2, 8.3, "eigenvalues (k², k²)", color=INK_3, fontsize=8.5)
    ax.scatter([9 / 4], [9], s=80, color=AMBER, zorder=5)
    ax.text(2.6, 9.4, "(9/4, 9): one interior zero", color=AMBER, fontsize=10, fontweight="semibold")
    for b, lab in [(4, "β = 4"), (9 / 4, "β = 9/4")]:
        ax.scatter([9 / 4], [b], s=44, marker="x", color=INK, linewidths=1.4, zorder=5)
        ax.text(2.0, b, lab, color=INK_2, fontsize=8.5, va="center", ha="right")
    ax.text(13.8, 0.45, "× tempting answers, not in the spectrum · grey lines α = 1, β = 1 are trivial",
            color=INK_2, fontsize=8.5, ha="right")  # fmt: skip
    ax.text(7.0, 3.3, "1/√α + 1/√β = 1", color=NAVY, fontsize=10, fontweight="semibold")
    ax.text(10.5, 4.6, "two zeros", color=NAVY_LIGHT, fontsize=8.5)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 14)
    ax.set_aspect("equal")
    ax.set_xlabel("α")
    ax.set_ylabel("β")
    viz.headline(fig, "The answer is β = 9, off the diagonal of eigenvalues",
                 "Fučík spectrum of −u″ on (0, π). Solutions with one interior zero live on the dark curve")  # fmt: skip
    return fig


# ── 04 · Newton basins ──────────────────────────────────────────────────────
def fig_newton():
    n = 500
    xs = np.linspace(-2.5, 2.5, n)
    X, Y = np.meshgrid(xs, xs)
    Z = X + 1j * Y
    with np.errstate(all="ignore"):
        W = (Z - 1) / (Z + 1)
        basin = np.where(np.abs(W) < 1, 1.0, 0.0)
    fig, ax = plt.subplots(figsize=(7.4, 6.6))
    from matplotlib.colors import ListedColormap

    ax.imshow(basin, extent=[-2.5, 2.5, -2.5, 2.5], origin="lower", cmap=ListedColormap([AMBER_WASH, NAVY_WASH]),
              interpolation="nearest")  # fmt: skip
    ax.axvline(0, color=AMBER, lw=2.4)
    for z0, col in [(0.35 + 1.6j, NAVY), (-0.5 - 1.4j, INK_2)]:
        orb = p04.orbit(z0, 8)
        ax.plot([z.real for z in orb], [z.imag for z in orb], color=col, lw=1.0, marker="o", ms=3.5)
    orb = p04.orbit(0.7j, 12)
    ys = [z.imag for z in orb if abs(z.imag) < 2.5]
    ax.scatter([0] * len(ys), ys, s=22, color=AMBER, edgecolors=PAPER, linewidths=0.8, zorder=5)
    ax.scatter([1, -1], [0, 0], s=60, color=INK, zorder=6)
    ax.text(1.08, -0.22, "+1", color=INK, fontsize=10, fontweight="semibold")
    ax.text(-1.32, -0.22, "−1", color=INK, fontsize=10, fontweight="semibold")
    ax.text(1.25, 2.1, "converges to +1", color=NAVY, fontsize=9.5)
    ax.text(-2.35, 2.1, "converges to −1", color=INK_2, fontsize=9.5)
    ax.text(0.1, -2.3, "imaginary axis: never converges", color=AMBER, fontsize=10, fontweight="semibold")
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect("equal")
    ax.grid(False)
    ax.set_xlabel("Re z₀")
    ax.set_ylabel("Im z₀")
    viz.headline(fig, "Newton's method for z² = 1 fails on a whole line",
                 r"Where $z \mapsto (z + 1/z)/2$ goes, by starting point. Orbits on the axis stay on it forever")  # fmt: skip
    return fig


# ── 06 · weak convergence ───────────────────────────────────────────────────
def fig_weak():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(12, 4.6))
    x = np.linspace(0, 1, 2000)
    ax.plot(x, np.sin(2 * np.pi * 12 * x), color=NAVY_LIGHT, lw=1.0)
    ax.plot(x, np.sin(2 * np.pi * x), color=NAVY, lw=2.0)
    ax.text(0.27, 1.12, "n = 1", color=NAVY, fontsize=9.5, ha="center")
    ax.text(0.62, -1.28, "n = 12", color=INK_2, fontsize=9.5, ha="center")
    ax.set_ylim(-1.45, 1.4)
    ax.set_xlabel("x")
    ax.set_title("sin(2πnx): faster, not smaller", pad=10)

    ns = np.arange(1, 41)
    norms = [p06.l2_norm(int(n)) for n in ns]
    pair = [abs(p06.pairing(int(n), lambda t: t)) for n in ns]
    bx.plot(ns, norms, color=NAVY, lw=2.0)
    bx.scatter(ns, pair, s=16, color=AMBER, zorder=3)
    bx.text(40, 0.735, "L² norm = 1/√2 for every n", color=NAVY, fontsize=9.5, ha="right")
    bx.text(6, 0.14, "pairing with g(x) = x\nequals 1/(2πn) → 0", color=AMBER, fontsize=9.5, fontweight="semibold")
    bx.set_ylim(0, 0.85)
    bx.set_xlabel("n")
    bx.set_title("Size against pairings", pad=10)
    viz.headline(fig, "Oscillation kills every pairing, not the norm",
                 "sin(2πnx) converges to 0 weakly in L²(0, 1), but its norm never moves", extra_top=8)  # fmt: skip
    fig.subplots_adjust(wspace=0.2)
    return fig


# ── 08 · dense open set ─────────────────────────────────────────────────────
def fig_dense_open():
    eps = 0.3
    fig, ax = plt.subplots(figsize=(12, 3.0))
    intervals = p08.covering(eps, 120)
    ax.add_patch(plt.Rectangle((0, -0.2), 1, 0.4, color=NAVY_WASH, lw=0))
    for a, b in intervals:
        ax.add_patch(plt.Rectangle((a, -0.2), b - a, 0.4, color=AMBER, lw=0))
    length = p08.union_length(intervals)
    ax.text(0.0, 0.5, f"first 120 intervals: total length {length:.3f} ≤ ε = {eps}", color=AMBER, fontsize=10,
            fontweight="semibold")  # fmt: skip
    ax.text(1.0, -0.42, "what is left after all intervals: measure ≥ 1 − ε, yet no interior", color=INK_2, fontsize=9, ha="right")
    ax.set_xlim(-0.01, 1.01)
    ax.set_ylim(-0.55, 0.7)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(False)
    viz.headline(fig, "Dense and open, yet almost empty",
                 r"An interval of length $\varepsilon/2^{k+1}$ around the k-th rational. Every rational is covered")  # fmt: skip
    return fig


def main() -> None:
    for name, build in [
        ("00_overview.png", fig_overview),
        ("01_p_laplacian.png", fig_plaplacian),
        ("02_fucik.png", fig_fucik),
        ("04_newton.png", fig_newton),
        ("06_weak.png", fig_weak),
        ("08_dense_open.png", fig_dense_open),
    ]:
        print("wrote", viz.save(build(), FIGURES / name).relative_to(ROOT))


if __name__ == "__main__":
    main()
