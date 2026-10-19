"""Problem 01: the first eigenvalue of the one dimensional p-Laplacian.

For p > 1, the first eigenvalue of

    -(|u'|^{p-2} u')' = lambda |u|^{p-2} u  on (0, 1),  u(0) = u(1) = 0,

is lambda_1 = (p - 1) pi_p^p with pi_p = 2 pi / (p sin(pi / p)). The tempting
answer pi_p^p is off by the factor p - 1 whenever p != 2.

The check below does not use the formula: it shoots from u(0) = 0, u'(0) = 1 and
adjusts lambda until the first zero of u lands at x = 1.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def pi_p(p: float) -> float:
    """pi_p in Lindqvist's normalization, 2 * int_0^1 (1 - s^p)^(-1/p) ds."""
    return 2 * np.pi / (p * np.sin(np.pi / p))


def lambda1_formula(p: float) -> float:
    """The correct closed form (p - 1) pi_p^p."""
    return (p - 1) * pi_p(p) ** p


def lambda1_wrong(p: float) -> float:
    """The common wrong answer pi_p^p, which drops the factor p - 1."""
    return pi_p(p) ** p


def first_zero(lam: float, p: float) -> float:
    """First positive zero of the solution with u(0) = 0, u'(0) = 1."""

    def rhs(t, y):
        u, v = y  # v = |u'|^{p-2} u'
        return [np.sign(v) * abs(v) ** (1 / (p - 1)), -lam * np.sign(u) * abs(u) ** (p - 1)]

    def crossing(t, y):
        return y[0] if t > 1e-6 else 1.0

    crossing.terminal, crossing.direction = True, -1
    sol = solve_ivp(rhs, [0, 3], [0.0, 1.0], events=crossing, method="DOP853", rtol=1e-10, atol=1e-12)
    return sol.t_events[0][0] if len(sol.t_events[0]) else np.inf


def lambda1_shooting(p: float) -> float:
    """lambda_1 found numerically, without using the closed form except to bracket it."""
    guess = lambda1_formula(p)
    return brentq(lambda lam: first_zero(lam, p) - 1, 0.3 * guess, 3 * guess, xtol=1e-10)
