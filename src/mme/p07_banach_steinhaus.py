"""Problem 07: Banach-Steinhaus needs completeness.

On c_00, the finitely supported real sequences with the sup norm, the functionals
T_n(x) = n x_n are pointwise bounded: for a fixed x only finitely many x_n are
nonzero, so sup_n |T_n x| is a maximum over finitely many terms. Yet ||T_n|| = n,
so the family is not uniformly bounded. Banach-Steinhaus does not apply because c_00
is not complete. The tempting answer applies the theorem anyway and concludes that
the norms are bounded.
"""

from __future__ import annotations

import numpy as np


def T(n: int, x: np.ndarray) -> float:
    """T_n x = n * x_n, with x indexed from 1 and zero past its length."""
    return n * x[n - 1] if n <= len(x) else 0.0


def sup_over_n(x: np.ndarray, n_max: int = 10_000) -> float:
    return max(abs(T(n, x)) for n in range(1, n_max + 1))


def operator_norm(n: int) -> float:
    """||T_n|| is attained at the unit vector e_n."""
    e = np.zeros(n)
    e[-1] = 1.0
    return abs(T(n, e))
