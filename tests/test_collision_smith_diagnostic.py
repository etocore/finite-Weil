import numpy as np

from experiments.collision_smith_diagnostic import (
    determinantal_valuations,
    simplified_upper_exponents,
    smith_exponents_from_valuations,
    weighted_upper_constant_matrix,
)


def test_smith_exponents_recover_successive_differences() -> None:
    assert smith_exponents_from_valuations((3, 7, 12)) == (3, 4, 5)


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
    assert smith_exponents_from_valuations(valuations) == (3, 4)


def test_simplified_upper_block_has_no_missing_first_grade_for_m3() -> None:
    exponents = simplified_upper_exponents([-1.0, 0.0, 1.0], [1.0, 2.0, 3.0])

    assert exponents == (3, 4)


def test_simplified_upper_block_has_generic_exponents_for_m4() -> None:
    exponents = simplified_upper_exponents(
        [-2.0, -0.5, 0.75, 1.75],
        [1.0, 2.0, -1.0, 3.0],
    )

    assert exponents == (4, 5, 6)


def test_centered_constant_matrix_has_expected_rank() -> None:
    matrix = weighted_upper_constant_matrix(
        [-1.0, 0.0, 1.0],
        [1.0, 2.0, 3.0],
    )

    assert matrix.shape == (3, 2)
    assert np.linalg.matrix_rank(matrix) == 2
