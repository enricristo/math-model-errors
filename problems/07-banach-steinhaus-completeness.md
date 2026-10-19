# 07 · Banach-Steinhaus needs completeness

**Area:** functional analysis · **Verification:** [`p07_banach_steinhaus.py`](../src/mme/p07_banach_steinhaus.py)

## Problem

Let $c_{00}$ be the space of real sequences with finitely many nonzero terms, with the sup norm, and let $T_n x = n\,x_n$. Is the family $\{T_n\}$ pointwise bounded? Is $\sup_n \|T_n\|$ finite?

## A tempting wrong answer

"For each $x$, $\sup_n |T_n x| < \infty$, so by the uniform boundedness principle $\sup_n \|T_n\| < \infty$."

## Why it is wrong

The uniform boundedness principle needs the domain to be a Banach space; its proof uses the Baire category theorem, which needs completeness. $c_{00}$ is not complete: $(1, \frac12, \frac13, \dots, \frac1N, 0, \dots)$ is Cauchy and its limit is not finitely supported.

## Correct solution

Pointwise bounded: yes, for fixed $x$ only finitely many $x_n$ are nonzero, so $\sup_n |n x_n|$ is a maximum over finitely many numbers. Uniformly bounded: no, $\|T_n\| = n$, attained at the unit vector $e_n$. The family shows that completeness cannot be dropped from Banach-Steinhaus.

## Verification

For $x = (1, -\frac12, \frac14, 0, \dots)$, $\sup_n |T_n x| = 1$; the operator norms at $e_n$ are $1, 10, 1000$ for $n = 1, 10, 1000$.
