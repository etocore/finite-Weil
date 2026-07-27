"""Compare isolated and exterior-relative collision singular-value slopes.

This experiment is intentionally model-agnostic at the block-elimination level. Callers
supply cluster and exterior Jacobian columns for each collision scale ``h``. The module
projects cluster columns to the orthogonal complement of the exterior target image and
fits power-law slopes of the resulting singular values.

The numerical projection is a diagnostic for the relative Smith conjecture. It is not a
proof and should be replaced by exact determinantal-divisor calculations once the exact
original Jacobian is reconstructed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np
from numpy.typing import NDArray

RealArray = NDArray[np.float64]
ComplexMatrix = NDArray[np.complex128]
JacobianBuilder = Callable[[float, int, float], tuple[ComplexMatrix, ComplexMatrix]]


@dataclass(frozen=True, slots=True)
class RelativeSlopeResult:
    """Fitted isolated and relative singular-value exponents."""

    exterior_count: int
    exterior_scale: float
    collision_scales: RealArray
    isolated_slopes: RealArray
    relative_slopes: RealArray
    isolated_residuals: RealArray
    relative_residuals: RealArray


def project_mod_exterior(
    cluster_columns: ComplexMatrix,
    exterior_columns: ComplexMatrix,
    *,
    rank_tolerance: float | None = None,
) -> ComplexMatrix:
    """Project cluster columns orthogonally modulo the exterior target image."""

    cluster = np.asarray(cluster_columns, dtype=np.complex128)
    exterior = np.asarray(exterior_columns, dtype=np.complex128)
    if cluster.ndim != 2 or exterior.ndim != 2:
        raise ValueError("cluster and exterior columns must be matrices")
    if cluster.shape[0] != exterior.shape[0]:
        raise ValueError("cluster and exterior matrices must share a target dimension")
    if exterior.shape[1] == 0:
        return cluster.copy()

    u, singular_values, _ = np.linalg.svd(exterior, full_matrices=False)
    if rank_tolerance is None:
        rank_tolerance = (
            max(exterior.shape)
            * np.finfo(np.float64).eps
            * float(singular_values[0])
        )
    rank = int(np.count_nonzero(singular_values > rank_tolerance))
    if rank == 0:
        return cluster.copy()

    exterior_basis = u[:, :rank]
    return cluster - exterior_basis @ (exterior_basis.conjugate().T @ cluster)


def _fit_slopes(scales: RealArray, singular_values: RealArray) -> tuple[RealArray, RealArray]:
    log_h = np.log(scales)
    slopes = np.empty(singular_values.shape[1], dtype=np.float64)
    residuals = np.empty_like(slopes)
    design = np.column_stack([log_h, np.ones(log_h.size)])

    for index in range(singular_values.shape[1]):
        values = singular_values[:, index]
        if np.any(values <= 0.0) or not np.all(np.isfinite(values)):
            raise ValueError("singular values must remain positive and finite")
        coefficients, _, _, _ = np.linalg.lstsq(design, np.log(values), rcond=None)
        fitted = design @ coefficients
        slopes[index] = coefficients[0]
        residuals[index] = float(np.linalg.norm(np.log(values) - fitted))

    return slopes, residuals


def analyze_relative_slopes(
    builder: JacobianBuilder,
    collision_scales: Iterable[float],
    *,
    exterior_count: int,
    exterior_scale: float,
) -> RelativeSlopeResult:
    """Fit isolated and exterior-relative slopes for one experiment configuration."""

    scales = np.asarray(tuple(collision_scales), dtype=np.float64)
    if scales.ndim != 1 or scales.size < 3:
        raise ValueError("collision_scales must contain at least three values")
    if np.any(scales <= 0.0) or not np.all(np.isfinite(scales)):
        raise ValueError("collision_scales must be positive and finite")
    if isinstance(exterior_count, bool) or not isinstance(exterior_count, int):
        raise TypeError("exterior_count must be an integer")
    if exterior_count < 0:
        raise ValueError("exterior_count must be nonnegative")
    if not np.isfinite(exterior_scale) or exterior_scale <= 0.0:
        raise ValueError("exterior_scale must be positive and finite")

    isolated_samples: list[RealArray] = []
    relative_samples: list[RealArray] = []

    for h in scales:
        cluster, exterior = builder(float(h), exterior_count, float(exterior_scale))
        cluster = np.asarray(cluster, dtype=np.complex128)
        exterior = np.asarray(exterior, dtype=np.complex128)
        isolated_samples.append(np.linalg.svd(cluster, compute_uv=False))
        relative = project_mod_exterior(cluster, exterior)
        relative_samples.append(np.linalg.svd(relative, compute_uv=False))

    isolated_values = np.asarray(isolated_samples, dtype=np.float64)
    relative_values = np.asarray(relative_samples, dtype=np.float64)
    isolated_slopes, isolated_residuals = _fit_slopes(scales, isolated_values)
    relative_slopes, relative_residuals = _fit_slopes(scales, relative_values)

    return RelativeSlopeResult(
        exterior_count=exterior_count,
        exterior_scale=exterior_scale,
        collision_scales=scales,
        isolated_slopes=isolated_slopes,
        relative_slopes=relative_slopes,
        isolated_residuals=isolated_residuals,
        relative_residuals=relative_residuals,
    )
