"""Problem 02: a point on the Fučík spectrum.

The Fučík spectrum of -u'' on (0, pi) with Dirichlet conditions is the set of
(alpha, beta) for which

    -u'' = alpha u^+ - beta u^-,  u(0) = u(pi) = 0

has a nontrivial solution. Solutions with exactly one interior zero are a positive
hump of length pi / sqrt(alpha) next to a negative hump of length pi / sqrt(beta),
so they exist exactly on the curve 1 / sqrt(alpha) + 1 / sqrt(beta) = 1.

For alpha = 9/4 this gives beta = 9. The tempting answers treat the problem as an
eigenvalue problem (beta = alpha, or beta = 4, the second eigenvalue).
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def beta_on_first_curve(alpha: float) -> float:
    """beta with 1/sqrt(alpha) + 1/sqrt(beta) = 1, for alpha > 1."""
    return 1 / (1 - 1 / np.sqrt(alpha)) ** 2


def endpoint_and_zeros(alpha: float, beta: float) -> tuple[float, int]:
    """Value u(pi) and number of interior zeros, shooting from u(0) = 0, u'(0) = 1."""

    def rhs(t, y):
        u, v = y
        return [v, -(alpha * max(u, 0.0) - beta * max(-u, 0.0))]

    def crossing(t, y):
        return y[0]

    sol = solve_ivp(rhs, [0, np.pi], [0.0, 1.0], events=crossing, method="DOP853", rtol=1e-11, atol=1e-13)
    interior = [t for t in sol.t_events[0] if 1e-6 < t < np.pi - 1e-6]
    return sol.y[0, -1], len(interior)


def beta_shooting(alpha: float, lo: float, hi: float) -> float:
    """beta in [lo, hi] for which the solution starting positive vanishes at pi."""
    return brentq(lambda b: endpoint_and_zeros(alpha, b)[0], lo, hi, xtol=1e-12)
