from fractions import Fraction

from experiments.raw_moment_smith import (
    exact_determinant,
    exact_determinantal_data,
    minor_valuation,
    predicted_exponents,
    raw_moment_coefficient_matrix,
)


def test_exact_determinant_over_rationals() -> None:
    matrix = [
        [Fraction(1, 2), Fraction(1, 3)],
        [Fraction(2, 5), Fraction(3, 7)],
    ]
    assert exact_determinant(matrix) == Fraction(17, 210)


def test_raw_moment_coefficient_matrix_for_two_nodes() -> None:
    matrix = raw_moment_coefficient_matrix([-1, 1], [2, 3])
    assert matrix[0] == (1, 1, 0, 0)
    assert matrix[1] == (-1, 1, 2, 3)
    assert matrix[2] == (1, 1, -4, 6)


def test_minor_valuation_counts_position_columns() -> None:
    assert minor_valuation((0, 2, 4), (0, 3, 5), 3) == 4


def test_exact_m2_smith_data() -> None:
    result = exact_determinantal_data([-1, 1], [2, 3])
    assert result.valuations == (0, 0, 1, 4)
    assert result.exponents == (0, 0, 1, 3)
    assert result.exponents == predicted_exponents(2)


def test_exact_m3_smith_data_matches_observed_gap() -> None:
    result = exact_determinantal_data([-1, 0, 1], [1, 2, 3])
    assert result.valuations == (0, 0, 1, 3, 7, 12)
    assert result.exponents == (0, 0, 1, 2, 4, 5)
    assert result.exponents == predicted_exponents(3)
    assert all(witness.leading_coefficient != 0 for witness in result.witnesses)


def test_exact_m4_smith_data_matches_missing_grade_pattern() -> None:
    result = exact_determinantal_data([-2, -1, 1, 3], [1, 2, 3, 5])
    assert result.valuations == (0, 0, 1, 3, 6, 11, 17, 24)
    assert result.exponents == (0, 0, 1, 2, 3, 5, 6, 7)
    assert result.exponents == predicted_exponents(4)
