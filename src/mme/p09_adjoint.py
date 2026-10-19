"""Problem 09: the matrix of the adjoint under a non-standard inner product.

On R^2 with <x, y>_G = x^T G y, G symmetric positive definite, the adjoint of A
satisfies <A x, y>_G = <x, A* y>_G, which gives A* = G^{-1} A^T G. It equals A^T only
when G commutes appropriately with A (for example G = I, an orthonormal basis). The
tempting answer is A^T.
"""

from __future__ import annotations

import sympy as sp

G = sp.Matrix([[2, 1], [1, 1]])
A = sp.Matrix([[1, 2], [0, 1]])


def adjoint(A: sp.Matrix, G: sp.Matrix) -> sp.Matrix:
    return G.inv() * A.T * G


def is_adjoint(A: sp.Matrix, B: sp.Matrix, G: sp.Matrix) -> bool:
    """<A x, y>_G == <x, B y>_G for all x, y, i.e. A^T G == G B."""
    return sp.simplify(A.T * G - G * B) == sp.zeros(*A.shape)
