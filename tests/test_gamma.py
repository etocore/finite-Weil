from math import exp, log

import numpy as np
import pytest
from scipy.integrate import quad
from scipy.special import digamma

from finite_weil.completed import CompletedDirichletData
from finite_weil.gamma import gamma_kernel, gamma_matrix, gamma_weight
from finite_weil.lfunctions import PrimitiveQuadraticCharacter
from finite_weil.packets import GaussianPacketFamily


def test_gamma_weight_matches_direct_digamma_evaluation() -> None:
    for parity in (0, 1):
        for t in (-7.5, -0.25, 0.0, 0.25, 7.5):
            argument = (parity + 0.5 + 1j * t) / 2.0
            assert gamma_weight(t, parity) == pytest.approx(float(digamma(argument).real))


def test_gamma_weight_is_even_and_parity_dependent() -> None:
    for parity in (0, 1):
        assert gamma_weight(3.25, parity) == pytest.approx(gamma_weight(-3.25, parity))

    assert gamma_weight(0.0, 0) != pytest.approx(gamma_weight(0.0, 1))


def test_gamma_weight_has_expected_large_frequency_asymptotic() -> None:
    for parity in (0, 1):
        t = 1.0e4
        assert gamma_weight(t, parity) == pytest.approx(log(t / 2.0), abs=1.0e-8)


def test_gamma_kernel_matches_independent_full_line_quadrature() -> None:
    delta = 0.8
    sigma = 0.45
    parity = 1

    def integrand(t: float) -> float:
        argument = (parity + 0.5 + 1j * t) / 2.0
        return (
            sigma**2
            * float(digamma(argument).real)
            * exp(-(sigma * t) ** 2)
            * np.cos(delta * t)
        )

    expected, _ = quad(integrand, -np.inf, np.inf, epsabs=1e-11, epsrel=1e-11)
    assert gamma_kernel(delta, sigma, parity) == pytest.approx(expected, abs=1e-10)


def test_gamma_matrix_is_symmetric_and_translation_invariant() -> None:
    centers = np.asarray([-0.7, 0.1, 1.2])
    shifted_centers = centers + 17.3
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(5))

    matrix = gamma_matrix(GaussianPacketFamily(centers, sigma=0.4), data)
    shifted = gamma_matrix(GaussianPacketFamily(shifted_centers, sigma=0.4), data)

    assert np.allclose(matrix, matrix.T)
    assert np.allclose(matrix, shifted)


def test_gamma_matrix_depends_on_character_parity() -> None:
    packets = GaussianPacketFamily([-0.2, 0.5], sigma=0.35)
    even = gamma_matrix(
        packets,
        CompletedDirichletData(PrimitiveQuadraticCharacter(5)),
    )
    odd = gamma_matrix(
        packets,
        CompletedDirichletData(PrimitiveQuadraticCharacter(-3)),
    )

    assert not np.allclose(even, odd)


def test_gamma_input_validation() -> None:
    with pytest.raises(ValueError, match="parity"):
        gamma_weight(0.0, 2)
    with pytest.raises(ValueError, match="finite"):
        gamma_weight(np.inf, 0)
    with pytest.raises(ValueError, match="positive"):
        gamma_kernel(0.0, 0.0, 0)
