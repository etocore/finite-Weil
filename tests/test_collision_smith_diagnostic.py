from fractions import Fraction

import numpy as np

from experiments.collision_smith_diagnostic import (
    determinantal_valuations,
    exact_centered_frame,
    exact_determinantal_valuations,
    exact_simplified_upper_exponents,
    exact_weighted_upper_constant_matrix,
    simplified_upper_exponents,
    smith_exponents_from_valuations,
    weighted_upper_constant_matrix,
)


def test_smith_exponents_recover_successive_differences() -> None:
    assert smith_exponents_from_valuations((3, 7, 12)) == (3, 4, 5)


def test_exact_minor_valuations_do_not_use_a_tolerance() -> None:
    matrix = (
        (Fraction(1), Fraction(2)),
        (Fraction(3), Fraction(5)),
        (Fraction(7), Fraction(11)),
    )

    valuations = exact_determinantal_valuations(matrix, (3, 4, 5))

    assert valuations == (3, 7)
    assert smith_exponents_from_valuations(valuations) == (3, 4)


def test_determinantal_valuations_for_generic_weighted_rows() -> None:
    matrix = np.asarray(
        [
            [1.0, 2.0],
            [3.0, 5.0],
            [7.0, 11.0],
        ],
        dtype=np.complex128,
    )

    valuations = determinantal_valuations(matrix, [3, 4, 5])

    assert valuations == (3, 7)


def test_exact_centered_frame_has_integer_columns() -> None:
    frame = exact_centered_frame(3)

    assert frame == (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(-1), Fraction(-1)),
    )


def test_reduced_upper_block_exact_and_float_agree_for_m3() -> None:
    exact = exact_simplified_upper_exponents(
        (Fraction(-1), Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(2), Fraction(3)),
    )
    floating = simplified_upper_exponents([-1.0, 0.0, 1.0], [1.0, 2.0, 3.0])

    assert exact == (3, 4)
    assert floating == exact


def test_reduced_upper_block_exact_for_m4() -> None:
    exponents = exact_simplified_upper_exponents(
        (Fraction(-2), Fraction(-1, 2), Fraction(3, 4), Fraction(7, 4)),
        (Fraction(1), Fraction(2), Fraction(-1), Fraction(3)),
    )

    assert exponents == (4, 5, 6)


def test_exact_centered_constant_matrix_has_expected_shape() -> None:
    matrix = exact_weighted_upper_constant_matrix(
        (Fraction(-1), Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(2), Fraction(3)),
    )

    assert len(matrix) == 3
    assert len(matrix[0]) == 2


def test_floating_centered_constant_matrix_has_expected_rank() -> None:
    matrix = weighted_upper_constant_matrix(
        [-1.0, 0.0, 1.0],
        [1.0, 2.0, 3.0],
    )

    assert matrix.shape == (3, 2)
    assert np.linalg.matrix_rank(matrix) == 2
