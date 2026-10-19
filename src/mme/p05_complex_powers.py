"""Problem 05: principal values of complex powers.

With the principal logarithm Log z = ln|z| + i Arg z, Arg in (-pi, pi]:

* i^i = exp(i Log i) = e^{-pi/2}, a real number;
* (i - 1)^i = exp(i Log(-1 + i)) = e^{-3 pi / 4} (cos(ln sqrt 2) + i sin(ln sqrt 2)),
  because -1 + i lies in the second quadrant, Arg = 3 pi / 4;
* Log(z1 z2) need not equal Log z1 + Log z2: for z1 = z2 = -1 the left side is 0
  and the right side is 2 pi i.

The tempting errors use arctan(y / x) for the argument (which gives -pi/4 for
-1 + i) or treat Log as additive.
"""

from __future__ import annotations

import cmath

import sympy as sp


def principal_power(z: complex, w: complex) -> complex:
    return cmath.exp(w * cmath.log(z))


def i_to_i_exact() -> sp.Expr:
    return sp.simplify(sp.exp(sp.I * sp.log(sp.I)))


def i_minus_one_to_i_exact() -> sp.Expr:
    return sp.exp(sp.I * sp.log(sp.I - 1))


def wrong_argument(z: complex) -> float:
    """The arctan(y/x) shortcut, wrong outside the right half plane."""
    import math

    return math.atan(z.imag / z.real)


def log_additivity_gap(z1: complex, z2: complex) -> complex:
    """Log(z1 z2) - (Log z1 + Log z2); always a multiple of 2 pi i."""
    return cmath.log(z1 * z2) - (cmath.log(z1) + cmath.log(z2))
