import numpy as np

from experiments.geometry_refinement import (
    boundary_mass_fraction,
    geometry_prime_cutoff,
    packet_centers_from_spacing,
)
from finite_weil import GaussianPacketFamily


def test_packet_centers_from_spacing_are_symmetric() -> None:
    centers = packet_centers_from_spacing(2.0, 0.75)

    assert np.isclose(centers[0], -2.0)
    assert np.isclose(centers[-1], 2.0)
    assert np.allclose(centers, -centers[::-1])
    assert np.max(np.diff(centers)) <= 0.75


def test_geometry_prime_cutoff_covers_translation_scale() -> None:
    cutoff = geometry_prime_cutoff(3.0, 0.5, tail_sigmas=4.0)

    assert np.log(cutoff) >= 2.0 * 3.0 + 4.0 * 0.5


def test_boundary_mass_identifies_centered_packet() -> None:
    packets = GaussianPacketFamily([-1.0, 0.0, 1.0], sigma=0.4)
    coefficients = np.asarray([0.0, 1.0, 0.0])

    mass, peak = boundary_mass_fraction(packets, coefficients, extent=1.0)

    assert mass < 0.1
    assert abs(peak) < 0.01
