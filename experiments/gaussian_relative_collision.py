"""Test collision singular-value slopes in the concrete Gaussian feature map.

The cluster feature map is

    (u_j, x_j) -> sum_j u_j g(.-x_j),

sampled on a dense real grid.  Exterior packets contribute their weight and center
columns, and the cluster columns are projected modulo that exterior image before
singular-value slopes are fitted.

This is a numerical diagnostic.  It tests whether separated Gaussian packets
alone create the observed missing collision grade.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import null_space

RealArray = NDArray[np.float64]
RealMatrix = NDArray[np.float64]


@dataclass(frozen=True, slots=True)
class GaussianRelativeResult:
    """Fitted isolated and exterior-relative singular-value slopes."""

    cluster_size: int
    exterior_count: int
    exterior_distance: float
    collision_scales: RealArray
    isolated_slopes: RealArray
    relative_slopes: RealArray


def gaussian(grid: RealArray, center: float, sigma: float) -> RealArray:
    """Evaluate a translated unit-amplitude Gaussian."""

    return np.exp(-((grid - center) ** 2) / (2.0 * sigma**2))


def gaussian_center_derivative(
    grid: RealArray,
    center: float,
    sigma: float,
) -> RealArray:
    """Differentiate the translated Gaussian with respect to its center."""

    return (grid - center) * gaussian(grid, center, sigma) / sigma**2


def centered_frame(size: int) -> RealMatrix:
    """Return an orthonormal frame for vectors whose coordinates sum to zero."""

    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 2:
        raise ValueError("size must be at least two")
    return np.asarray(null_space(np.ones((1, size))), dtype=float)


def gaussian_collision_blocks(
    cluster_size: int,
    collision_scale: float,
    exterior_count: int,
    exterior_distance: float,
    *,
    sigma: float = 1.0,
    grid_extent: float = 12.0,
    grid_points: int = 2001,
) -> tuple[RealMatrix, RealMatrix]:
    """Return cluster and exterior Jacobian columns in sampled function space."""

    if cluster_size < 2:
        raise ValueError("cluster_size must be at least two")
    if collision_scale <= 0.0:
        raise ValueError("collision_scale must be positive")
    if exterior_count < 0:
        raise ValueError("exterior_count must be nonnegative")
    if exterior_distance <= 0.0:
        raise ValueError("exterior_distance must be positive")
    if sigma <= 0.0:
        raise ValueError("sigma must be positive")

    grid = np.linspace(-grid_extent, grid_extent, grid_points, dtype=float)
    nodes = np.linspace(
        -(cluster_size - 1) / 2.0,
        (cluster_size - 1) / 2.0,
        cluster_size,
        dtype=float,
    )
    weights = np.arange(1, cluster_size + 1, dtype=float)

    weight_columns = np.column_stack(
        [gaussian(grid, collision_scale * node, sigma) for node in nodes]
    )
    position_columns = np.column_stack(
        [
            collision_scale
            * weights[index]
            * gaussian_center_derivative(grid, collision_scale * node, sigma)
            for index, node in enumerate(nodes)
        ]
    ) @ centered_frame(cluster_size)
    cluster = np.column_stack([weight_columns, position_columns])

    exterior_columns: list[RealArray] = []
    for index in range(exterior_count):
        center = exterior_distance * (index + 1)
        exterior_columns.extend(
            [
                gaussian(grid, center, sigma),
                gaussian_center_derivative(grid, center, sigma),
            ]
        )
    exterior = (
        np.column_stack(exterior_columns)
        if exterior_columns
        else np.empty((grid.size, 0), dtype=float)
    )
    return np.asarray(cluster, dtype=float), np.asarray(exterior, dtype=float)


def project_mod_exterior(cluster: RealMatrix, exterior: RealMatrix) -> RealMatrix:
    """Project cluster columns orthogonally off the exterior column space."""

    if exterior.shape[1] == 0:
        return cluster.copy()
    basis, _ = np.linalg.qr(exterior, mode="reduced")
    return np.asarray(cluster - basis @ (basis.T @ cluster), dtype=float)


def _fit_slopes(scales: RealArray, samples: RealMatrix) -> RealArray:
    design = np.column_stack([np.log(scales), np.ones(scales.size)])
    slopes = np.empty(samples.shape[1], dtype=float)
    for index in range(samples.shape[1]):
        coefficients, _, _, _ = np.linalg.lstsq(
            design,
            np.log(samples[:, index]),
            rcond=None,
        )
        slopes[index] = coefficients[0]
    return np.sort(slopes)


def analyze_gaussian_relative_collision(
    cluster_size: int,
    collision_scales: RealArray,
    *,
    exterior_count: int,
    exterior_distance: float,
    sigma: float = 1.0,
) -> GaussianRelativeResult:
    """Fit isolated and relative slopes for the concrete Gaussian feature map."""

    scales = np.asarray(collision_scales, dtype=float)
    if scales.ndim != 1 or scales.size < 3:
        raise ValueError("collision_scales must contain at least three values")
    if np.any(scales <= 0.0):
        raise ValueError("collision_scales must be positive")

    isolated: list[RealArray] = []
    relative: list[RealArray] = []
    for scale in scales:
        cluster, exterior = gaussian_collision_blocks(
            cluster_size,
            float(scale),
            exterior_count,
            exterior_distance,
            sigma=sigma,
        )
        isolated.append(np.linalg.svd(cluster, compute_uv=False)[::-1])
        projected = project_mod_exterior(cluster, exterior)
        relative.append(np.linalg.svd(projected, compute_uv=False)[::-1])

    isolated_samples = np.asarray(isolated, dtype=float)
    relative_samples = np.asarray(relative, dtype=float)
    return GaussianRelativeResult(
        cluster_size=cluster_size,
        exterior_count=exterior_count,
        exterior_distance=exterior_distance,
        collision_scales=scales,
        isolated_slopes=_fit_slopes(scales, isolated_samples),
        relative_slopes=_fit_slopes(scales, relative_samples),
    )
