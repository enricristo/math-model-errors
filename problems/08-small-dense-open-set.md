# 08 · A dense open subset of $[0,1]$ with small measure

**Area:** measure theory · **Verification:** [`p08_small_dense_open.py`](../src/mme/p08_small_dense_open.py) · **Figure:** [`08_dense_open.png`](../figures/08_dense_open.png)

## Problem

Given $\varepsilon > 0$, is there an open dense subset of $[0, 1]$ with Lebesgue measure at most $\varepsilon$? What can be said about its complement?

## A tempting wrong answer

"No. A dense open set is large: its closure is all of $[0, 1]$, so its measure must be $1$."

## Why it is wrong

Density and measure measure different things. The closure of a set can be the whole interval while the set itself is a thin union of intervals; Lebesgue measure does not pass to closures.

## Correct solution

Enumerate the rationals $q_1, q_2, \dots$ of $[0,1]$ and let $U = \bigcup_k (q_k - \varepsilon/2^{k+1},\ q_k + \varepsilon/2^{k+1})$. Then $U$ is open, dense (it contains every rational) and

$$\lambda(U) \le \sum_{k \ge 1} \frac{\varepsilon}{2^k} = \varepsilon.$$

The complement $K = [0,1]\setminus U$ is closed with empty interior (nowhere dense), yet $\lambda(K) \ge 1 - \varepsilon$: topologically small, metrically large.

## Verification

With $\varepsilon = 0.1$ and the first 400 rationals, the union of the intervals has length below $0.1$ and every one of those rationals is covered.

![Dense open set](../figures/08_dense_open.png)
