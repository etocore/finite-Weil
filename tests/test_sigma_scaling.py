"""Tests for the small-bandwidth scaling experiment."""

import numpy as np

from experiments.sigma_scaling import certified_cutoff, packet_family, run_case
from finite_weil import prime_truncation_eigenvalue_bound


def test_packet_family_is_symmetric_with_requested_spacing() -> None:
    packets = packet_family(1.5, 0.2, 1.5)

    assert np.allclose(packets.centers, -packets.centers[::-1])
    assert np.max(np.diff(packets.centers)) <= 1.5 * 0.2 + 1e-12


def test_certified_cutoff_meets_the_requested_tolerance() -> None:
    packets = packet_family(1.0, 0.3, 1.5)
    cutoff, bound = certified_cutoff(packets, 1e-6)

    assert bound <= 1e-6
    assert prime_truncation_eigenvalue_bound(packets, cutoff) == bound


def test_run_case_spectrum_is_positive_within_truncation_budget() -> None:
    row = run_case(
        sigma=0.25,
        extent=1.0,
        spacing_ratio=1.5,
        truncation_tolerance=1e-8,
        relative_tolerance=1e-12,
        envelope_floor=1e-15,
    )

    assert row.lambda_min >= -(row.truncation_bound + 1e-10)
    assert row.lambda_max >= row.lambda_min
    assert row.truncation_bound <= 1e-8
    if row.zeros_used:
        assert row.zero_side_max_error < 1e-10
        assert row.zero_side_lambda_min >= 0.0
