# 04 · Newton's method for $z^2 = 1$ in the complex plane

**Area:** complex dynamics · **Verification:** [`p04_newton_square_root.py`](../src/mme/p04_newton_square_root.py) · **Figure:** [`04_newton.png`](../figures/04_newton.png)

## Problem

For which $z_0 \in \mathbb{C}\setminus\{0\}$ does $z_{n+1} = \frac12\left(z_n + \frac{1}{z_n}\right)$ converge, and to what?

## A tempting wrong answer

"This is Newton's method for $z^2 = 1$, which converges quadratically, so $z_n \to 1$ or $z_n \to -1$ for every $z_0 \ne 0$, depending on which root is closer."

## Why it is wrong

Global convergence of Newton's method is not guaranteed in the complex plane. Here the basins are exactly two half planes, and the boundary between them, the imaginary axis, is invariant: if $z_0 = iy$ then every $z_n$ is purely imaginary, so it can never reach $\pm1$. Some orbits on the axis even hit $0$ (for example $z_0 = i$ gives $z_1 = 0$), where the map is undefined.

## Correct solution

Put $w = \dfrac{z-1}{z+1}$. A direct computation gives $w_{n+1} = w_n^{\,2}$, so $w_n = w_0^{\,2^n}$.

* If $\operatorname{Re} z_0 > 0$ then $|w_0| < 1$, $w_n \to 0$ and $z_n \to 1$.
* If $\operatorname{Re} z_0 < 0$ then $|w_0| > 1$, $w_n \to \infty$ and $z_n \to -1$.
* If $\operatorname{Re} z_0 = 0$ then $|w_n| = 1$ for all $n$: no convergence. On this circle the map $w \mapsto w^2$ is the angle doubling map, which is chaotic.

## Verification

The code checks the conjugation identity, convergence from both half planes, and that orbits starting on the imaginary axis stay on it (real part below $10^{-12}$ after 200 steps), with $z_0 = i$ reaching $0$.

![Basins](../figures/04_newton.png)
