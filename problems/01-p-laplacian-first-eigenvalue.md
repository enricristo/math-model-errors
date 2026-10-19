# 01 · The first eigenvalue of the one dimensional p-Laplacian

**Area:** nonlinear ODE, p-Laplacian · **Verification:** [`p01_plaplacian.py`](../src/mme/p01_plaplacian.py), shooting method in SciPy · **Figure:** [`01_p_laplacian.png`](../figures/01_p_laplacian.png)

## Problem

Let $p > 1$. Find the smallest $\lambda > 0$ for which

$$-\left(|u'|^{p-2}u'\right)' = \lambda\,|u|^{p-2}u \quad \text{on } (0, 1), \qquad u(0) = u(1) = 0,$$

has a nontrivial solution. Give the value for $p = 3$.

## A tempting wrong answer

"The eigenfunction is a generalized sine $\sin_p(\pi_p x)$, so $\lambda_1 = \pi_p^{\,p}$. For $p = 3$, $\lambda_1 \approx 14.144$."

## Why it is wrong

The answer borrows the shape of the case $p = 2$, where $\lambda_1 = \pi^2$, and silently drops a factor. With $\pi_p = 2\int_0^1 (1-s^p)^{-1/p}ds$, the generalized sine solves $\left(|u'|^{p-2}u'\right)' + (p-1)|u|^{p-2}u = 0$, not the equation with coefficient $1$. Different authors put the factor $(p-1)^{1/p}$ inside or outside $\pi_p$, and mixing the two conventions is exactly where the error comes from. For $p = 2$ the factor is $1$, which hides the mistake.

## Correct solution

Rescaling $u(x) = \sin_p(\pi_p x)$ shows that

$$\lambda_1 = (p-1)\,\pi_p^{\,p}, \qquad \pi_p = \frac{2\pi}{p\,\sin(\pi/p)}.$$

For $p = 3$: $\pi_3 = 4\pi/(3\sqrt3) \approx 2.4184$ and $\lambda_1 = 2\pi_3^{\,3} \approx 28.2888$, twice the tempting value. The closed form of $\pi_p$ is formally proved in Lean in [lean-repo](https://github.com/enricristo/lean-repo/blob/main/notes/pi-p.md).

## Verification

The check never uses the closed form for $\lambda_1$. It integrates the equation from $u(0) = 0$, $u'(0) = 1$ and adjusts $\lambda$ by root finding until the first zero of $u$ is at $x = 1$. For $p = 1.5, 2, 3, 4$ the result agrees with $(p-1)\pi_p^{\,p}$ to $10^{-8}$ relative error, and the ratio to the tempting answer is exactly $p - 1$.

![First eigenvalue](../figures/01_p_laplacian.png)
