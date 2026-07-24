from math import exp, log, pi

import numpy as np
import pytest
from scipy.integrate import quad

from finite_weil.completed import CompletedDirichletData, conductor_matrix
from finite_weil.lfunctions import PrimitiveQuadraticCharacter
from finite_weil.packets import GaussianPacketFamily


def test_even_character_completed_data() -> None:
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(5))

    assert data.conductor == 5
    assert data.parity == 0
    assert data.gamma_shift == 0.0
    assert data.log_conductor_scale == pytest.approx(log(5 / pi))
    assert data.prefactor_log_derivative() == pytest.approx(0.5 * log(5 / pi))
    assert data.conductor_form_coefficient() == pytest.approx(log(5 / pi))


def test_odd_character_completed_data() -> None:
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(-3))

    assert data.conductor == 3
    assert data.parity == 1
    assert data.gamma_shift == 0.5
    assert data.log_conductor_scale == pytest.approx(log(3 / pi))


def test_parity_matches_character_value_at_minus_one() -> None:
    for discriminant in (-8, -7, -4, -3, 1, 5, 8, 12, 13):
        character = PrimitiveQuadraticCharacter(discriminant)
        data = CompletedDirichletData(character)

        assert character(-1) == (-1) ** data.parity


def test_conductor_matrix_is_log_scale_times_gram() -> None:
    packets = GaussianPacketFamily([-0.4, 0.2, 0.9], sigma=0.35)
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(13))

    matrix = conductor_matrix(packets, data)

    assert np.allclose(matrix, log(13 / pi) * packets.gram_matrix())


def test_conductor_matrix_matches_independent_spectral_quadrature() -> None:
    centers = np.asarray([-0.3, 0.6])
    sigma = 0.4
    packets = GaussianPacketFamily(centers, sigma=sigma)
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(5))
    matrix = conductor_matrix(packets, data)

    coefficient = log(5 / pi)
    for i, left_center in enumerate(centers):
        for j, right_center in enumerate(centers):
            delta = right_center - left_center

            def integrand(u: float, delta: float = delta) -> float:
                spectral_product = (
                    2.0
                    * pi
                    * sigma**2
                    * exp(-(sigma * u) ** 2)
                    * np.cos(u * delta)
                )
                return coefficient * spectral_product / (2.0 * pi)

            quadrature, _ = quad(integrand, -np.inf, np.inf, epsabs=1e-11)
            assert matrix[i, j] == pytest.approx(quadrature, abs=1e-10)
