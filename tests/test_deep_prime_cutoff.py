import numpy as np

from finite_weil import (
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    assemble_prime_operator,
    prime_operator_terms,
    prime_power_values,
)


def test_prime_power_values_are_exact_and_sorted() -> None:
    assert prime_power_values(20) == (
        (2, 2),
        (3, 3),
        (4, 2),
        (5, 5),
        (7, 7),
        (8, 2),
        (9, 3),
        (11, 11),
        (13, 13),
        (16, 2),
        (17, 17),
        (19, 19),
    )


def test_vectorized_prime_assembly_matches_term_sum() -> None:
    packets = GaussianPacketFamily([-1.0, 0.25, 1.5], sigma=0.6)
    character = PrimitiveQuadraticCharacter(5)

    vectorized = assemble_prime_operator(packets, character, cutoff=100)
    direct = np.zeros_like(vectorized)
    for term in prime_operator_terms(packets, character, cutoff=100):
        direct += term.coefficient * term.weight * term.matrix

    assert np.allclose(vectorized, direct, rtol=1e-13, atol=1e-13)
    assert np.allclose(vectorized, vectorized.T, rtol=0.0, atol=1e-14)


def test_prime_power_values_validate_cutoff_type() -> None:
    try:
        prime_power_values(True)
    except TypeError:
        pass
    else:
        raise AssertionError("boolean cutoff should be rejected")
