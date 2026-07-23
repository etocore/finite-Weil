from math import log, pi

import pytest

from finite_weil.completed import CompletedDirichletData
from finite_weil.lfunctions import PrimitiveQuadraticCharacter


def test_even_character_completed_data() -> None:
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(5))

    assert data.conductor == 5
    assert data.parity == 0
    assert data.gamma_shift == 0.0
    assert data.log_conductor_scale == pytest.approx(log(5 / pi))
    assert data.prefactor_log_derivative() == pytest.approx(0.5 * log(5 / pi))


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
