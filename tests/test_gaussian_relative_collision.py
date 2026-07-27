import numpy as np
import pytest

from experiments.gaussian_relative_collision import (
    analyze_gaussian_relative_collision,
    centered_frame,
    gaussian_collision_blocks,
    project_mod_exterior,
)


def test_centered_frame_has_zero_coordinate_sum() -> None:
    frame = centered_frame(4)

    assert frame.shape == (4, 3)
    assert np.allclose(np.ones(4) @ frame, 0.0, atol=1e-14)
    assert np.allclose(frame.T @ frame, np.eye(3), atol=1e-14)


def test_exterior_projection_annihilates_exterior_overlap() -> None:
    cluster, exterior = gaussian_collision_blocks(3, 0.1, 2, 3.5)
    projected = project_mod_exterior(cluster, exterior)

    assert np.linalg.norm(exterior.T @ projected) < 1e-10


@pytest.mark.parametrize("cluster_size", [2, 3, 4])
@pytest.mark.parametrize("exterior_count", [0, 1, 2, 3])
def test_gaussian_relative_slopes_remain_consecutive(
    cluster_size: int,
    exterior_count: int,
) -> None:
    scales = np.logspace(-1.5, -0.5, 8)
    result = analyze_gaussian_relative_collision(
        cluster_size,
        scales,
        exterior_count=exterior_count,
        exterior_distance=4.0,
    )
    expected = np.arange(2 * cluster_size - 1, dtype=float)

    assert np.allclose(result.isolated_slopes, expected, atol=0.08)
    assert np.allclose(result.relative_slopes, expected, atol=0.08)


def test_relative_slopes_are_stable_under_exterior_distance() -> None:
    scales = np.logspace(-1.5, -0.5, 8)
    near = analyze_gaussian_relative_collision(
        4,
        scales,
        exterior_count=2,
        exterior_distance=3.0,
    )
    far = analyze_gaussian_relative_collision(
        4,
        scales,
        exterior_count=2,
        exterior_distance=5.0,
    )

    assert np.allclose(near.relative_slopes, far.relative_slopes, atol=0.08)
