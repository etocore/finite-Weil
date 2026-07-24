import numpy as np

from finite_weil import (
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    assemble_prime_operator,
    exponential_prime_weight,
    generalized_eigenvalues,
    gram_whitened_matrix,
    sharp_prime_weight,
)


def test_sharp_weight_reproduces_original_cutoff() -> None:
    packets = GaussianPacketFamily([-1.0, 0.0, 1.0], 0.5)
    character = PrimitiveQuadraticCharacter(5)

    direct = assemble_prime_operator(packets, character, 25)
    explicit = assemble_prime_operator(
        packets,
        character,
        25,
        weight=sharp_prime_weight,
        support_multiplier=4.0,
    )

    assert np.allclose(direct, explicit)


def test_exponential_weight_is_symmetric_and_finite() -> None:
    packets = GaussianPacketFamily([-1.0, 0.0, 1.0], 0.5)
    character = PrimitiveQuadraticCharacter(5)

    matrix = assemble_prime_operator(
        packets,
        character,
        25,
        weight=exponential_prime_weight,
        support_multiplier=6.0,
    )

    assert np.all(np.isfinite(matrix))
    assert np.allclose(matrix, matrix.T)


def test_gram_whitening_matches_direct_solver_when_well_conditioned() -> None:
    gram = np.diag([2.0, 4.0])
    operator = np.diag([6.0, -8.0])

    direct = generalized_eigenvalues(operator, gram)
    whitened = generalized_eigenvalues(
        operator,
        gram,
        relative_tolerance=1e-14,
    )

    assert np.allclose(direct, whitened)


def test_gram_whitening_discards_numerically_null_mode() -> None:
    gram = np.diag([1.0, 1e-18])
    operator = np.diag([2.0, 7.0])

    whitened = gram_whitened_matrix(
        operator,
        gram,
        relative_tolerance=1e-12,
    )
    values = generalized_eigenvalues(
        operator,
        gram,
        relative_tolerance=1e-12,
    )

    assert whitened.shape == (1, 1)
    assert np.allclose(values, [2.0])
