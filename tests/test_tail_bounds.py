"""Tests for the certified prime-tail bounds."""

from math import exp, log, sqrt

import numpy as np
import pytest
from scipy.integrate import quad

from finite_weil import (
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    assemble_prime_operator,
)
from finite_weil.tail_bounds import (
    _one_sided_log_tail,
    prime_tail_bound_matrix,
    prime_tail_entry_bound,
    prime_tail_spectral_bound,
    prime_truncation_eigenvalue_bound,
)


def test_one_sided_closed_form_matches_quadrature() -> None:
    sigma = 0.45
    log_cutoff = 5.5
    for delta in (-3.0, -0.5, 0.0, 1.2, 3.0):

        def integrand(u: float, delta: float = delta) -> float:
            return u * exp(u / 2.0 - ((u - delta) ** 2) / (4.0 * sigma**2))

        expected, _ = quad(integrand, log_cutoff, np.inf, epsabs=1e-13)
        value = float(_one_sided_log_tail(delta, sigma, log_cutoff))
        assert value == pytest.approx(expected, rel=1e-10)


def test_entry_bound_dominates_integer_log_weight_tail() -> None:
    """The bound dominates the full integer sum it was derived from."""

    sigma = 0.5
    delta = 1.5
    cutoff = 60
    direct = 0.0
    for n in range(cutoff + 1, 300000):
        u = log(n)
        direct += (
            u
            / sqrt(n)
            * sqrt(np.pi)
            * sigma
            * (
                exp(-((delta - u) ** 2) / (4.0 * sigma**2))
                + exp(-((delta + u) ** 2) / (4.0 * sigma**2))
            )
        )
    assert prime_tail_entry_bound(delta, sigma, cutoff) >= direct


def test_bound_dominates_actual_prime_refinement() -> None:
    """Deep refinements stay entrywise below the certified tail bound."""

    packets = GaussianPacketFamily(np.linspace(-1.5, 1.5, 5), sigma=0.5)
    character = PrimitiveQuadraticCharacter(1)
    shallow_cutoff = 500

    shallow = assemble_prime_operator(packets, character, shallow_cutoff)
    deep = assemble_prime_operator(packets, character, 200000)
    bound = prime_tail_bound_matrix(packets, shallow_cutoff)

    assert np.all(np.abs(deep - shallow) <= bound)


def test_bound_decreases_with_cutoff() -> None:
    packets = GaussianPacketFamily(np.linspace(-1.0, 1.0, 4), sigma=0.4)

    values = [
        prime_tail_spectral_bound(packets, cutoff)
        for cutoff in (100, 1000, 10000, 100000)
    ]
    assert all(later < earlier for earlier, later in zip(values, values[1:]))
    assert values[-1] < 1e-12


def test_eigenvalue_bound_dominates_observed_shift() -> None:
    packets = GaussianPacketFamily(np.linspace(-1.0, 1.0, 4), sigma=0.4)
    character = PrimitiveQuadraticCharacter(5)
    gram = packets.gram_matrix()
    shallow_cutoff = 200

    from finite_weil import generalized_eigenvalues

    shallow = generalized_eigenvalues(
        assemble_prime_operator(packets, character, shallow_cutoff), gram
    )
    deep = generalized_eigenvalues(
        assemble_prime_operator(packets, character, 100000), gram
    )
    bound = prime_truncation_eigenvalue_bound(packets, shallow_cutoff)

    assert np.max(np.abs(deep - shallow)) <= bound


def test_small_cutoff_is_rejected() -> None:
    packets = GaussianPacketFamily(np.linspace(-3.0, 3.0, 4), sigma=0.4)

    with pytest.raises(ValueError, match="log\\(cutoff\\)"):
        prime_tail_bound_matrix(packets, 100)
    with pytest.raises(ValueError, match="at least 2"):
        prime_tail_entry_bound(0.0, 0.4, 1)
    with pytest.raises(TypeError, match="integer"):
        prime_tail_entry_bound(0.0, 0.4, 2.5)  # type: ignore[arg-type]
