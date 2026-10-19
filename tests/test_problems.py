"""Every claim made in problems/*.md, checked numerically or symbolically."""

import cmath
import math

import numpy as np
import pytest
import sympy as sp

from mme import (
    p01_plaplacian as p01,
    p02_fucik as p02,
    p03_ambrosetti_rabinowitz as p03,
    p04_newton_square_root as p04,
    p05_complex_powers as p05,
    p06_weak_convergence as p06,
    p07_banach_steinhaus as p07,
    p08_small_dense_open as p08,
    p09_adjoint as p09,
)


# 01 ──────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("p", [1.5, 2.0, 3.0, 4.0])
def test_p01_shooting_matches_closed_form(p):
    assert p01.lambda1_shooting(p) == pytest.approx(p01.lambda1_formula(p), rel=1e-8)


def test_p01_numbers_quoted():
    assert p01.lambda1_formula(3) == pytest.approx(28.28876198, abs=1e-7)
    assert p01.lambda1_wrong(3) == pytest.approx(14.14438099, abs=1e-7)
    assert p01.lambda1_formula(2) == pytest.approx(math.pi**2)


@pytest.mark.parametrize("p", [1.5, 3.0, 4.0])
def test_p01_wrong_answer_is_off_by_p_minus_one(p):
    assert p01.lambda1_formula(p) / p01.lambda1_wrong(p) == pytest.approx(p - 1)


# 02 ──────────────────────────────────────────────────────────────────────────
def test_p02_closed_form_value():
    assert p02.beta_on_first_curve(9 / 4) == pytest.approx(9.0)


def test_p02_shooting_finds_beta_nine_with_one_zero():
    beta = p02.beta_shooting(9 / 4, 5.0, 20.0)
    assert beta == pytest.approx(9.0, abs=1e-8)
    assert p02.endpoint_and_zeros(9 / 4, beta)[1] == 1


@pytest.mark.parametrize("beta", [9 / 4, 4.0])
def test_p02_tempting_answers_are_not_in_the_spectrum(beta):
    assert abs(p02.endpoint_and_zeros(9 / 4, beta)[0]) > 1e-2


# 03 ──────────────────────────────────────────────────────────────────────────
def test_p03_superquadratic_but_not_ambrosetti_rabinowitz():
    assert p03.superquadratic_limit() == sp.oo
    assert p03.ar_ratio_limit() == 2


# 04 ──────────────────────────────────────────────────────────────────────────
def test_p04_half_planes():
    assert p04.limit_label(0.3 + 2j) == "+1"
    assert p04.limit_label(-0.3 + 2j) == "-1"


def test_p04_imaginary_axis():
    assert p04.orbit(1j, 5)[-1] == 0
    z = p04.orbit(0.7j, 200)
    assert all(abs(w.real) < 1e-12 for w in z)
    assert p04.limit_label(0.7j) == "none"


def test_p04_conjugation_squares():
    z = 0.4 - 1.3j
    assert p04.cayley(p04.step(z)) == pytest.approx(p04.cayley(z) ** 2)


# 05 ──────────────────────────────────────────────────────────────────────────
def test_p05_i_to_the_i():
    assert p05.i_to_i_exact() == sp.exp(-sp.pi / 2)
    assert p05.principal_power(1j, 1j) == pytest.approx(math.exp(-math.pi / 2))


def test_p05_i_minus_one_to_the_i():
    expected = math.exp(-3 * math.pi / 4) * cmath.exp(1j * math.log(math.sqrt(2)))
    assert p05.principal_power(-1 + 1j, 1j) == pytest.approx(expected)
    assert complex(sp.N(p05.i_minus_one_to_i_exact())) == pytest.approx(expected)
    assert cmath.phase(-1 + 1j) == pytest.approx(3 * math.pi / 4)
    assert p05.wrong_argument(-1 + 1j) == pytest.approx(-math.pi / 4)


def test_p05_log_not_additive():
    assert p05.log_additivity_gap(-1, -1) == pytest.approx(-2j * math.pi)


# 06 ──────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("n", [1, 5, 50])
def test_p06_norm_constant(n):
    assert p06.l2_norm(n) == pytest.approx(1 / math.sqrt(2), rel=1e-8)


def test_p06_pairings_go_to_zero():
    g = lambda x: x  # noqa: E731
    vals = [abs(p06.pairing(n, g)) for n in (1, 10, 100)]
    assert vals[0] > vals[1] > vals[2]
    assert vals[2] == pytest.approx(1 / (2 * math.pi * 100), rel=1e-6)


# 07 ──────────────────────────────────────────────────────────────────────────
def test_p07_pointwise_bounded_not_uniformly():
    x = np.array([1.0, -0.5, 0.25])
    assert p07.sup_over_n(x) == pytest.approx(1.0)
    assert [p07.operator_norm(n) for n in (1, 10, 1000)] == [1, 10, 1000]


# 08 ──────────────────────────────────────────────────────────────────────────
def test_p08_measure_small_and_contains_rationals():
    eps = 0.1
    intervals = p08.covering(eps, 400)
    assert p08.union_length(intervals) <= eps
    for q, (a, b) in zip(p08.rationals(400), intervals):
        assert a <= float(q) <= b


# 09 ──────────────────────────────────────────────────────────────────────────
def test_p09_adjoint_is_not_the_transpose():
    star = p09.adjoint(p09.A, p09.G)
    assert p09.is_adjoint(p09.A, star, p09.G)
    assert not p09.is_adjoint(p09.A, p09.A.T, p09.G)
    assert star == sp.Matrix([[-3, -2], [8, 5]])
