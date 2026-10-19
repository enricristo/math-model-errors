# 05 · Principal values of complex powers

**Area:** complex analysis · **Verification:** [`p05_complex_powers.py`](../src/mme/p05_complex_powers.py), SymPy and `cmath`

## Problem

Using the principal branch of the logarithm, $\operatorname{Log} z = \ln|z| + i\operatorname{Arg} z$ with $\operatorname{Arg} z \in (-\pi, \pi]$, compute $i^i$ and $(i-1)^i$. Is $\operatorname{Log}(z_1z_2) = \operatorname{Log} z_1 + \operatorname{Log} z_2$?

## A tempting wrong answer

"$i^i = e^{-\pi/2}$. For $i - 1$, $\arg = \arctan(1/(-1)) = -\pi/4$, so $(i-1)^i = e^{\pi/4}\,e^{i\ln\sqrt2}$. And the logarithm turns products into sums."

## Why it is wrong

$\arctan(y/x)$ gives the argument only in the right half plane. The point $-1 + i$ is in the second quadrant, with $\operatorname{Arg} = 3\pi/4$. As for additivity, $\operatorname{Arg} z_1 + \operatorname{Arg} z_2$ can leave $(-\pi, \pi]$, and then the principal value of the product differs by $2\pi i$.

## Correct solution

$$i^i = e^{i\operatorname{Log} i} = e^{i\cdot i\pi/2} = e^{-\pi/2} \approx 0.2079,$$

$$(i-1)^i = e^{i\left(\ln\sqrt2 + i\frac{3\pi}{4}\right)} = e^{-3\pi/4}\left(\cos\ln\sqrt2 + i\sin\ln\sqrt2\right).$$

For $z_1 = z_2 = -1$: $\operatorname{Log}(1) = 0$, while $\operatorname{Log}(-1) + \operatorname{Log}(-1) = 2\pi i$.

## Verification

SymPy returns $e^{-\pi/2}$ exactly for $i^i$; numerical principal powers in `cmath` match both closed forms; the gap in the logarithm is $-2\pi i$.
