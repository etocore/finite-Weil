import numpy as np

from experiments.relative_collision_schur import (
    analyze_relative_slopes,
    project_mod_exterior,
)


def test_projection_removes_exterior_target_span() -> None:
    exterior = np.asarray(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [0.0, 0.0],
        ],
        dtype=np.complex128,
    )
    cluster = np.asarray(
        [
            [2.0, 0.0],
            [3.0, 0.0],
            [5.0, 7.0],
        ],
        dtype=np.complex128,
    )

    relative = project_mod_exterior(cluster, exterior)

    np.testing.assert_allclose(exterior.conjugate().T @ relative, 0.0, atol=1e-12)
    np.testing.assert_allclose(relative[2, :], [5.0, 7.0], atol=1e-12)


def test_zero_exterior_columns_leave_cluster_unchanged() -> None:
    cluster = np.eye(3, dtype=np.complex128)
    exterior = np.empty((3, 0), dtype=np.complex128)

    np.testing.assert_allclose(project_mod_exterior(cluster, exterior), cluster)


def test_relative_slope_fitter_detects_absorbed_leading_direction() -> None:
    def builder(h: float, exterior_count: int, exterior_scale: float):
        del exterior_scale
        cluster = np.asarray(
            [
                [1.0, 0.0],
                [0.0, h],
                [0.0, h**2],
            ],
            dtype=np.complex128,
        )
        if exterior_count == 0:
            exterior = np.empty((3, 0), dtype=np.complex128)
        else:
            exterior = np.asarray([[0.0], [1.0], [0.0]], dtype=np.complex128)
        return cluster, exterior

    scales = 10.0 ** (-np.arange(1, 6, dtype=np.float64))
    isolated = analyze_relative_slopes(
        builder,
        scales,
        exterior_count=0,
        exterior_scale=1.0,
    )
    relative = analyze_relative_slopes(
        builder,
        scales,
        exterior_count=1,
        exterior_scale=1.0,
    )

    np.testing.assert_allclose(np.sort(isolated.isolated_slopes), [0.0, 1.0], atol=1e-10)
    np.testing.assert_allclose(np.sort(relative.relative_slopes), [0.0, 2.0], atol=1e-10)
