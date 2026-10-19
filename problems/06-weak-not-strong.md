# 06 · Weak but not strong convergence of $\sin(2\pi n x)$

**Area:** functional analysis · **Verification:** [`p06_weak_convergence.py`](../src/mme/p06_weak_convergence.py), quadrature in SciPy · **Figure:** [`06_weak.png`](../figures/06_weak.png)

## Problem

Let $s_n(x) = \sin(2\pi n x)$ on $[0, 1]$. Does $s_n \to 0$ in $L^2(0,1)$? Weakly? Pointwise?

## A tempting wrong answer

"Yes, $s_n \to 0$ in $L^2$: the oscillations get faster and cancel, so the functions average out to zero."

## Why it is wrong

Averaging out is a statement about integrals against a fixed function, which is weak convergence. The $L^2$ norm measures the size of $s_n$ itself, and fast oscillation does not make it smaller.

## Correct solution

* Strong: no, $\|s_n\|_2^2 = \int_0^1 \sin^2(2\pi n x)\,dx = \tfrac12$ for every $n$.
* Weak: yes, $\int_0^1 s_n g \to 0$ for every $g \in L^2$ (Riemann-Lebesgue lemma, or Bessel's inequality for the orthogonal family $\sqrt2\,s_n$). For $g(x) = x$ the integral is exactly $-1/(2\pi n)$.
* Pointwise: no, $s_n(1/4)$ runs through $1, 0, -1, 0, \dots$

## Verification

Quadrature gives $\|s_n\|_2 = 1/\sqrt2$ for $n = 1, 5, 50$, and $\left|\int_0^1 s_n(x)\,x\,dx\right| = 1/(2\pi n)$ decreasing to $0$.

![Weak convergence](../figures/06_weak.png)
