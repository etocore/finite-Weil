from math import log, sqrt

import numpy as np
import pytest

from finite_weil.explicit_formula import (
    assemble_prime_operator,
    prime_operator_terms,
    quadratic_prime_power_coefficient,
    universal_prime_operator,
)
from finite_weil.lfunctions import PrimitiveQuadraticCharacter
from finite_weil.packets import GaussianPacketFamily


def test_universal_prime_operator_is_symmetric() -> None:
    packets = GaussianPacketFamily([-0.4, 0.0, 0.7], sigma=0.3)
    matrix = universal_prime_operator(packets, 5)
    assert np.allclose(matrix, matrix.T)


def test_quadratic_coefficient_sign_and_ramification() -> None:
    chi = PrimitiveQuadraticCharacter(-3)
    assert quadratic_prime_power_coefficient(2, chi) == pytest.approx(
        -log(2) / sqrt(2)
    )
    assert quadratic_prime_power_coefficient(3, chi) == 0.0
    assert quadratic_prime_power_coefficient(4, chi) == pytest.approx(
        log(2) / 2
    )
    assert quadratic_prime_power_coefficient(6, chi) == 0.0


def test_assembly_equals_manual_finite_sum() -> None:
    packets = GaussianPacketFamily([-0.25, 0.4], sigma=0.2)
    chi = PrimitiveQuadraticCharacter(5)
    cutoff = 8

    assembled = assemble_prime_operator(packets, chi, cutoff)
    manual = np.zeros_like(assembled)
    for n in range(2, cutoff + 1):
        manual += quadratic_prime_power_coefficient(n, chi) * universal_prime_operator(
            packets, n
        )

    assert np.allclose(assembled, manual)


def test_terms_include_only_nonzero_prime_powers() -> None:
    packets = GaussianPacketFamily([0.0], sigma=0.5)
    chi = PrimitiveQuadraticCharacter(-4)
    terms = prime_operator_terms(packets, chi, 10)
    assert [term.n for term in terms] == [3, 5, 7, 9]
