# 09 · The matrix of the adjoint with a non-standard inner product

**Area:** linear algebra · **Verification:** [`p09_adjoint.py`](../src/mme/p09_adjoint.py), SymPy

## Problem

On $\mathbb{R}^2$ use the inner product $\langle x, y\rangle_G = x^\top G y$ with $G = \begin{pmatrix} 2 & 1 \\ 1 & 1\end{pmatrix}$. Find the matrix, in the standard basis, of the adjoint of $A = \begin{pmatrix} 1 & 2 \\ 0 & 1\end{pmatrix}$.

## A tempting wrong answer

"The adjoint of a real matrix is its transpose: $A^* = A^\top = \begin{pmatrix} 1 & 0 \\ 2 & 1\end{pmatrix}$."

## Why it is wrong

$A^* = A^\top$ holds when the matrix is written in an orthonormal basis for the inner product in use. The standard basis is not orthonormal for $\langle\cdot,\cdot\rangle_G$.

## Correct solution

$\langle Ax, y\rangle_G = x^\top A^\top G y$ must equal $\langle x, A^*y\rangle_G = x^\top G A^* y$ for all $x, y$, so $GA^* = A^\top G$ and

$$A^* = G^{-1}A^\top G = \begin{pmatrix} -3 & -2 \\ 8 & 5\end{pmatrix}.$$

## Verification

SymPy checks $A^\top G = G A^*$ for the matrix above and that $A^\top$ fails the same identity.
