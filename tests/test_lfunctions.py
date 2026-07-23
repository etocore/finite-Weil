from math import log

import pytest

from finite_weil.explicit_formula import von_mangoldt
from finite_weil.lfunctions import (
    PrimitiveQuadraticCharacter,
    is_fundamental_discriminant,
    kronecker_symbol,
    prime_power_base,
)


def test_fundamental_discriminants() -> None:
    for value in (-8, -7, -4, -3, 1, 5, 8, 12, 13):
        assert is_fundamental_discriminant(value)
    for value in (0, 4, 9, 16, 20):
        assert not is_fundamental_discriminant(value)


def test_character_modulo_three() -> None:
    chi = PrimitiveQuadraticCharacter(-3)
    assert chi.conductor == 3
    assert chi.parity == 1
    assert [chi(n) for n in range(1, 7)] == [1, -1, 0, 1, -1, 0]


def test_character_modulo_five() -> None:
    chi = PrimitiveQuadraticCharacter(5)
    assert chi.parity == 0
    assert [chi(n) for n in range(1, 6)] == [1, -1, -1, 1, 0]


def test_kronecker_even_denominator() -> None:
    assert kronecker_symbol(5, 2) == -1
    assert kronecker_symbol(7, 2) == 1
    assert kronecker_symbol(2, 2) == 0


def test_reject_nonfundamental_discriminant() -> None:
    with pytest.raises(ValueError):
        PrimitiveQuadraticCharacter(9)


def test_prime_power_detection_and_mangoldt() -> None:
    assert prime_power_base(2) == (2, 1)
    assert prime_power_base(8) == (2, 3)
    assert prime_power_base(9) == (3, 2)
    assert prime_power_base(12) is None
    assert von_mangoldt(8) == pytest.approx(log(2))
    assert von_mangoldt(12) == 0.0
