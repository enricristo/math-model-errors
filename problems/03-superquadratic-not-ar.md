# 03 · Superquadratic does not imply Ambrosetti-Rabinowitz

**Area:** variational methods · **Verification:** [`p03_ambrosetti_rabinowitz.py`](../src/mme/p03_ambrosetti_rabinowitz.py), limits in SymPy

## Problem

Let $f(t) = t\ln(1+|t|)$ and $F(t) = \int_0^t f(s)\,ds$. Is $f$ superquadratic at infinity, $F(t)/t^2 \to \infty$? Does it satisfy the Ambrosetti-Rabinowitz condition: there are $\theta > 2$ and $R > 0$ with $0 < \theta F(t) \le t f(t)$ for $|t| \ge R$?

## A tempting wrong answer

"Yes to both: $f$ grows faster than any linear function, so it is superlinear, and superlinear nonlinearities satisfy Ambrosetti-Rabinowitz."

## Why it is wrong

Ambrosetti-Rabinowitz asks for a fixed margin: $tf(t)$ must beat $F(t)$ by a factor $\theta > 2$. Growth like $t^2\ln t$ is faster than $t^2$, so the nonlinearity is superquadratic, but it is too slow to leave that margin. The condition holds for powers $|t|^{q-2}t$ with $q > 2$, which is where the intuition comes from.

## Correct solution

For $t > 0$,

$$F(t) = \frac{t^2-1}{2}\ln(1+t) - \frac{t^2}{4} + \frac{t}{2},$$

so $F(t)/t^2 \to \infty$ (superquadratic), while

$$\frac{t f(t)}{F(t)} = \frac{t^2\ln(1+t)}{\tfrac{t^2}{2}\ln(1+t) + O(t^2)} \longrightarrow 2.$$

No $\theta > 2$ works, and the condition fails. Superquadratic problems of this kind need other compactness arguments, such as Cerami sequences or monotonicity of $f(t)/t$.

## Verification

SymPy computes the primitive in closed form and both limits: $F(t)/t^2 \to \infty$ and $tf(t)/F(t) \to 2$.
