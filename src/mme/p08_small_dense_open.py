"""Problem 08: a dense open subset of [0, 1] with small measure.

Enumerate the rationals q_1, q_2, ... of [0, 1] and let U be the union of the open
intervals of length eps / 2^k centered at q_k. U is open and dense (it contains every
rational) and its measure is at most eps. Its complement is closed, has empty
interior (nowhere dense) and measure at least 1 - eps. The tempting answer says a
dense open set must have full measure, mixing up topological and measure-theoretic
size.
"""

from __future__ import annotations

from fractions import Fraction


def rationals(count: int) -> list[Fraction]:
    """The first `count` distinct rationals of [0, 1], by increasing denominator."""
    seen: list[Fraction] = []
    q = 1
    while len(seen) < count:
        for p in range(0, q + 1):
            r = Fraction(p, q)
            if r not in seen:
                seen.append(r)
                if len(seen) == count:
                    break
        q += 1
    return seen


def covering(eps: float, count: int) -> list[tuple[float, float]]:
    """The first `count` intervals of the construction, clipped to [0, 1]."""
    out = []
    for k, q in enumerate(rationals(count), start=1):
        half = eps / 2 ** (k + 1)
        out.append((max(0.0, float(q) - half), min(1.0, float(q) + half)))
    return out


def union_length(intervals: list[tuple[float, float]]) -> float:
    total, end = 0.0, -1.0
    for a, b in sorted(intervals):
        if b <= end:
            continue
        total += b - max(a, end)
        end = b
    return total
