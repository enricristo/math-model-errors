"""Problem 06: sin(2 pi n x) on [0, 1].

The functions s_n(x) = sin(2 pi n x) converge weakly to 0 in L^2(0, 1): for every
g in L^2, int_0^1 s_n g -> 0 (Riemann-Lebesgue). They do not converge strongly,
since ||s_n||_2 = 1 / sqrt(2) for every n, and they do not converge pointwise either
(s_n(1/4) runs through 1, 0, -1, 0, ...). The tempting answer says s_n -> 0 in L^2
"because the oscillations cancel".
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad


def l2_norm(n: int) -> float:
    return np.sqrt(quad(lambda x: np.sin(2 * np.pi * n * x) ** 2, 0, 1, limit=400)[0])


def pairing(n: int, g) -> float:
    """int_0^1 sin(2 pi n x) g(x) dx."""
    return quad(lambda x: np.sin(2 * np.pi * n * x) * g(x), 0, 1, limit=400)[0]
