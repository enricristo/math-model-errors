"""Problem 04: z -> (z + 1/z) / 2 in the complex plane.

This is Newton's method for z^2 = 1. With w = (z - 1) / (z + 1) the map becomes
w -> w^2, so the iteration converges to 1 when |w| < 1 (Re z > 0), to -1 when
|w| > 1 (Re z < 0), and never converges when |w| = 1, which is exactly the imaginary
axis. There the iterates stay on the axis and, for some starting points, hit 0,
where the map is undefined. The tempting answer is "converges to 1 or -1 for every
z_0 != 0".
"""

from __future__ import annotations

import numpy as np


def step(z: complex) -> complex:
    return (z + 1 / z) / 2


def orbit(z0: complex, n: int) -> list[complex]:
    """The first n iterates, stopping early if the orbit hits 0."""
    out = [complex(z0)]
    for _ in range(n):
        if out[-1] == 0:
            break
        out.append(step(out[-1]))
    return out


def cayley(z: complex) -> complex:
    """w = (z - 1) / (z + 1), which conjugates the map to w -> w^2."""
    return (z - 1) / (z + 1)


def limit_label(z0: complex, n: int = 60, tol: float = 1e-10) -> str:
    """'+1', '-1' or 'none' after n steps."""
    z = orbit(z0, n)[-1]
    if not np.isfinite(z) or z == 0:
        return "none"
    if abs(z - 1) < tol:
        return "+1"
    if abs(z + 1) < tol:
        return "-1"
    return "none"
