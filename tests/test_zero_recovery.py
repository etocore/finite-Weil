"""Tests for the matrix-pencil zero-recovery experiment."""

import numpy as np
import pytest

from experiments.zero_recovery import (
    ZETA_ZEROS,
    envelope_amplitude_ratios,
    matrix_pencil_frequencies,
    prime_side_kernel_samples,
    run_case,
)


def test_matrix_pencil_recovers_synthetic_damped_cosines() -> None:
    sigma = 0.1
    step = 0.06
    count = 160
    frequencies = np.asarray(ZETA_ZEROS[:5])
    amplitudes = 4.0 * np.pi * sigma**2 * np.exp(-((sigma * frequencies) ** 2))
    deltas = step * np.arange(count)
    samples = (np.cos(np.outer(deltas, frequencies)) * amplitudes).sum(axis=1)

    recovered, order = matrix_pencil_frequencies(
        samples,
        step,
        model_order=5,
    )

    assert order == 5
    assert recovered.size == 5
    assert np.allclose(recovered, frequencies, atol=1e-7)

    ratios = envelope_amplitude_ratios(recovered, samples, step, sigma)
    assert np.allclose(ratios, 1.0, atol=1e-6)


def test_prime_side_kernel_matches_zero_side_expansion() -> None:
    """Prime-side samples reproduce the damped-cosine model they encode."""

    sigma = 0.15
    step = 0.25
    count = 24
    cutoff = 60000

    samples = prime_side_kernel_samples(sigma, step, count, cutoff)

    deltas = step * np.arange(count)
    model = np.zeros_like(deltas)
    for gamma in ZETA_ZEROS:
        model += (
            4.0
            * np.pi
            * sigma**2
            * np.exp(-((sigma * gamma) ** 2))
            * np.cos(gamma * deltas)
        )
    assert np.max(np.abs(samples - model)) < 1e-8


def test_run_case_recovers_the_first_zeta_zero_from_primes() -> None:
    row = run_case(0.2, envelope_floor=1e-8, delta_max=8.0)

    assert row.recovered, "expected at least one filtered frequency"
    closest = min(row.recovered, key=lambda f: abs(f - ZETA_ZEROS[0]))
    assert closest == pytest.approx(ZETA_ZEROS[0], abs=1e-3)


def test_matrix_pencil_input_validation() -> None:
    with pytest.raises(ValueError, match="one-dimensional"):
        matrix_pencil_frequencies(np.zeros(4), 0.1)
    with pytest.raises(ValueError, match="positive"):
        matrix_pencil_frequencies(np.zeros(16), -0.1)
    with pytest.raises(ValueError, match="at least 4"):
        prime_side_kernel_samples(0.2, 0.1, 2, 100)
