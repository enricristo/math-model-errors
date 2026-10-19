"""Problem 03: superquadratic does not imply Ambrosetti-Rabinowitz.

f(t) = t ln(1 + |t|) has F(t) / t^2 -> infinity (it is superquadratic), but the
Ambrosetti-Rabinowitz condition

    exists theta > 2, R > 0 with 0 < theta F(t) <= t f(t) for |t| >= R

fails, because t f(t) / F(t) -> 2. The tempting answer says the condition holds
because f grows faster than linearly.
"""

from __future__ import annotations

import sympy as sp

t, s = sp.symbols("t s", positive=True)


def f(x):
    """The nonlinearity, for x > 0."""
    return x * sp.log(1 + x)


def primitive() -> sp.Expr:
    """F(t) = int_0^t f(s) ds, for t > 0, in closed form."""
    return sp.simplify(sp.integrate(f(s), (s, 0, t)))


def ar_ratio_limit() -> sp.Expr:
    """lim_{t -> infinity} t f(t) / F(t)."""
    return sp.limit(t * f(t) / primitive(), t, sp.oo)


def superquadratic_limit() -> sp.Expr:
    """lim_{t -> infinity} F(t) / t^2."""
    return sp.limit(primitive() / t**2, t, sp.oo)
