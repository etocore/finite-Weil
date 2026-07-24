import numpy as np

from finite_weil import (
    GaussianPacketFamily,
    smallest_generalized_eigenpair,
)


def test_smallest_generalized_eigenpair_matches_diagonal_case() -> None:
    gram = np.diag([2.0, 4.0])
    operator = np.diag([6.0, -8.0])

    pair = smallest_generalized_eigenpair(operator, gram)

    assert np.isclose(pair.eigenvalue, -2.0)
    assert np.isclose(pair.coefficients @ gram @ pair.coefficients, 1.0)
    assert pair.residual_norm < 1e-13
    assert pair.retained_rank == 2


def test_whitened_eigenpair_discards_numerically_null_mode() -> None:
    gram = np.diag([1.0, 1e-16])
    operator = np.diag([2.0, -100.0])

    pair = smallest_generalized_eigenpair(
        operator,
        gram,
        relative_tolerance=1e-12,
    )

    assert np.isclose(pair.eigenvalue, 2.0)
    # Eigenvectors are defined only up to an overall sign.
    assert np.allclose(np.abs(pair.coefficients), [1.0, 0.0])
    assert pair.retained_rank == 1
    assert pair.residual_norm < 1e-13


def test_packet_linear_combination_reconstructs_samples() -> None:
    packets = GaussianPacketFamily([-1.0, 1.0], sigma=0.5)
    points = np.asarray([-1.0, 0.0, 1.0])
    coefficients = np.asarray([2.0, -0.5])

    values = packets.linear_combination(coefficients, points)
    expected = packets.evaluate(points) @ coefficients

    assert np.allclose(values, expected)
