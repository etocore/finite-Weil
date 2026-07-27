"""Tests for the completed-zeta pole matrix.

The test list follows the implementation contract in ``paper/12_pole_term.md``:
closed-form Laplace evaluations, symmetry, rank structure, eigenvalue
identities, swap invariance, conditional assembly, and independent zero-side
validation.
"""

from math import exp, pi

import numpy as np
import pytest
from scipy.integrate import quad

from finite_weil import (
    CompletedDirichletData,
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    WeilOperator,
    generalized_eigenvalues,
    pole_matrix,
    pole_vectors,
)

# Imaginary parts of the first nontrivial zeros of the Riemann zeta function.
# With sigma = 0.15 packets, the omitted tail beyond the seventh zero is
# bounded by exp(-(0.15 * 43.3)**2) < 5e-19 per zero and is negligible at the
# tolerance used below.
ZETA_ZEROS = (
    14.134725141734695,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739190,
    37.586178158825671,
    40.918719012147495,
)


def test_pole_vectors_match_numerical_laplace_evaluations() -> None:
    packets = GaussianPacketFamily([-0.8, 0.3, 1.1], sigma=0.45)
    p_minus, p_plus = pole_vectors(packets)

    for j, center in enumerate(packets.centers):
        for a, vector in ((-0.5, p_minus), (0.5, p_plus)):

            def integrand(x: float, center: float = center, a: float = a) -> float:
                # A single combined exponent keeps the integrand integrable and
                # avoids overflow: it is bounded above and underflows to zero.
                exponent = -((x - center) ** 2) / (2.0 * packets.sigma**2) + a * x
                return exp(exponent)

            expected, _ = quad(integrand, -np.inf, np.inf, epsabs=1e-12)
            assert vector[j] == pytest.approx(expected, rel=1e-10)


def test_pole_matrix_is_symmetric_with_cosh_entries() -> None:
    packets = GaussianPacketFamily([-1.0, 0.0, 0.7], sigma=0.35)
    matrix = pole_matrix(packets)

    assert np.allclose(matrix, matrix.T)

    delta = packets.centers[:, None] - packets.centers[None, :]
    expected = (
        4.0
        * pi
        * packets.sigma**2
        * exp(packets.sigma**2 / 4.0)
        * np.cosh(delta / 2.0)
    )
    assert np.allclose(matrix, expected)


def test_pole_matrix_rank_structure() -> None:
    several = GaussianPacketFamily([-0.9, 0.2, 0.5, 1.3], sigma=0.4)
    assert np.linalg.matrix_rank(pole_matrix(several), tol=1e-10) == 2

    single = GaussianPacketFamily([0.7], sigma=0.4)
    assert np.linalg.matrix_rank(pole_matrix(single), tol=1e-10) == 1


def test_pole_matrix_nonzero_eigenvalues_match_outer_product_identity() -> None:
    packets = GaussianPacketFamily([-1.2, -0.1, 0.4, 0.9], sigma=0.3)
    p_minus, p_plus = pole_vectors(packets)

    inner = float(p_plus @ p_minus)
    norms = float(np.linalg.norm(p_plus) * np.linalg.norm(p_minus))
    eigenvalues = np.linalg.eigvalsh(pole_matrix(packets))

    assert eigenvalues[0] == pytest.approx(inner - norms, rel=1e-12)
    assert eigenvalues[-1] == pytest.approx(inner + norms, rel=1e-12)
    assert np.allclose(eigenvalues[1:-1], 0.0, atol=1e-10)
    assert eigenvalues[0] < 0.0 < eigenvalues[-1]


def test_pole_matrix_is_invariant_under_vector_swap() -> None:
    packets = GaussianPacketFamily([-0.6, 0.8], sigma=0.5)
    p_minus, p_plus = pole_vectors(packets)

    direct = np.outer(p_minus, p_plus) + np.outer(p_plus, p_minus)
    swapped = np.outer(p_plus, p_minus) + np.outer(p_minus, p_plus)

    assert np.allclose(direct, swapped)
    assert np.allclose(pole_matrix(packets), direct)


def test_pole_block_is_gated_to_the_principal_character() -> None:
    packets = GaussianPacketFamily([-0.5, 0.5], sigma=0.4)
    zeta_data = CompletedDirichletData(PrimitiveQuadraticCharacter(1))
    dirichlet_data = CompletedDirichletData(PrimitiveQuadraticCharacter(5))

    with_pole = WeilOperator(packets, zeta_data, prime_cutoff=5, include_pole=True)
    without = WeilOperator(packets, zeta_data, prime_cutoff=5, include_pole=False)

    assert np.allclose(
        with_pole.matrix(),
        without.matrix() + pole_matrix(packets),
    )
    assert np.allclose(without.pole_matrix(), 0.0)

    with pytest.raises(ValueError, match="principal character"):
        WeilOperator(packets, dirichlet_data, prime_cutoff=5, include_pole=True)


def test_default_pole_resolution_follows_the_conductor() -> None:
    """The default assembles the mathematically correct completed function."""

    packets = GaussianPacketFamily([-0.5, 0.5], sigma=0.4)
    zeta = WeilOperator(
        packets,
        CompletedDirichletData(PrimitiveQuadraticCharacter(1)),
        prime_cutoff=5,
    )
    dirichlet = WeilOperator(
        packets,
        CompletedDirichletData(PrimitiveQuadraticCharacter(5)),
        prime_cutoff=5,
    )

    assert zeta.pole_included
    assert not dirichlet.pole_included
    assert np.allclose(zeta.pole_matrix(), pole_matrix(packets))
    assert np.allclose(dirichlet.pole_matrix(), 0.0)


def test_zeta_operator_with_pole_matches_zero_side_matrix() -> None:
    """Independent zero-side validation of the full D = 1 assembly.

    The explicit formula predicts that, once the prime sum is resolved to the
    packet geometry, the assembled matrix equals

        Z_ij = sum_gamma 4 pi sigma^2 exp(-(sigma gamma)^2) cos(gamma (c_i - c_j))

    summed over the imaginary parts of the nontrivial zeta zeros.  This ties
    the conductor, gamma, prime, and pole normalizations to the actual zeros.
    """

    sigma = 0.15
    centers = np.linspace(-1.5, 1.5, 7)
    packets = GaussianPacketFamily(centers, sigma)
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(1))
    operator = WeilOperator(
        packets,
        data,
        prime_cutoff=2000,
        include_pole=True,
    )

    assembled = operator.matrix()

    delta = centers[:, None] - centers[None, :]
    zero_side = np.zeros_like(delta)
    for gamma in ZETA_ZEROS:
        zero_side += (
            4.0
            * pi
            * sigma**2
            * exp(-((sigma * gamma) ** 2))
            * np.cos(gamma * delta)
        )

    assert np.max(np.abs(assembled - zero_side)) < 5e-13

    spectrum = generalized_eigenvalues(
        assembled,
        packets.gram_matrix(),
        relative_tolerance=1e-12,
    )
    assert np.all(spectrum > 0.0)


def test_deep_cutoff_negativity_is_cancelled_by_the_pole_matrix() -> None:
    """The pole matrix removes the large negative deep-cutoff eigenvalue.

    For sigma = 0.5 packets on [-2, 2] every zero-side term is bounded by
    exp(-(0.5 * 14.13)**2) ~ 2e-22, so the exact assembled form is numerically
    zero.  Without the pole block the smallest eigenvalue is far below zero.
    """

    packets = GaussianPacketFamily(np.linspace(-2.0, 2.0, 5), sigma=0.5)
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(1))
    cutoff = 2000  # log(2000) = 7.6 > 2 * extent + 4 * sigma = 6.0

    without = WeilOperator(packets, data, prime_cutoff=cutoff, include_pole=False)
    with_pole = WeilOperator(packets, data, prime_cutoff=cutoff, include_pole=True)
    gram = packets.gram_matrix()

    lambda_without = generalized_eigenvalues(
        without.matrix(), gram, relative_tolerance=1e-12
    )[0]
    spectrum_with = generalized_eigenvalues(
        with_pole.matrix(), gram, relative_tolerance=1e-12
    )

    assert lambda_without < -1.0
    assert np.max(np.abs(spectrum_with)) < 1e-4
