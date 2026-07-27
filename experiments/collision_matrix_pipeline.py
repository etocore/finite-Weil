"""Locate the first matrix pipeline stage that changes collision exponents.

The experiment treats packet centers as source variables and compares numerical
Jacobian singular-value slopes for several target maps:

- sampled Gaussian synthesis;
- the packet Gram matrix;
- the assembled Weil matrix;
- the paired matrix target ``(A, B)``;
- the fully retained Gram-whitened matrix;
- generalized eigenvalues.

Slope fitting is diagnostic. Exact Smith or determinantal-divisor calculations
remain necessary before promoting an observed pattern to a theorem.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Iterable
from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import eigh

from finite_weil import (
    CompletedDirichletData,
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    WeilOperator,
)

FloatArray = NDArray[np.float64]
StageMap = Callable[[FloatArray], FloatArray]


@dataclass(frozen=True, slots=True)
class StageSlopeResult:
    """Singular-value slopes for one target map."""

    stage: str
    collision_scales: FloatArray
    slopes: FloatArray
    residuals: FloatArray


def collision_centers(
    h: float,
    cluster_shape: Iterable[float],
    exterior_centers: Iterable[float] = (),
) -> FloatArray:
    """Return a centered shrinking cluster followed by separated centers."""

    shape = np.asarray(tuple(cluster_shape), dtype=float)
    exterior = np.asarray(tuple(exterior_centers), dtype=float)
    if shape.ndim != 1 or shape.size < 2:
        raise ValueError("cluster_shape must contain at least two entries")
    if not np.all(np.isfinite(shape)) or not np.all(np.isfinite(exterior)):
        raise ValueError("centers must be finite")
    if not np.isfinite(h) or h <= 0.0:
        raise ValueError("h must be positive and finite")
    centered_shape = shape - float(np.mean(shape))
    return np.concatenate((h * centered_shape, exterior))


def numerical_jacobian(
    target: StageMap,
    parameters: FloatArray,
    *,
    relative_step: float = 1e-6,
) -> FloatArray:
    """Return a central-difference Jacobian of a flattened real target."""

    point = np.asarray(parameters, dtype=float)
    if point.ndim != 1 or not np.all(np.isfinite(point)):
        raise ValueError("parameters must be a finite vector")
    if not np.isfinite(relative_step) or relative_step <= 0.0:
        raise ValueError("relative_step must be positive and finite")

    baseline = np.asarray(target(point), dtype=float).ravel()
    jacobian = np.empty((baseline.size, point.size), dtype=float)
    for index, value in enumerate(point):
        step = relative_step * max(1.0, abs(float(value)))
        forward = point.copy()
        backward = point.copy()
        forward[index] += step
        backward[index] -= step
        jacobian[:, index] = (
            np.asarray(target(forward), dtype=float).ravel()
            - np.asarray(target(backward), dtype=float).ravel()
        ) / (2.0 * step)
    return jacobian


def _fit_slopes(scales: FloatArray, samples: FloatArray) -> tuple[FloatArray, FloatArray]:
    log_h = np.log(scales)
    design = np.column_stack((log_h, np.ones(log_h.size)))
    slopes = np.empty(samples.shape[1], dtype=float)
    residuals = np.empty(samples.shape[1], dtype=float)
    for index in range(samples.shape[1]):
        values = samples[:, index]
        if np.any(values <= 0.0) or not np.all(np.isfinite(values)):
            raise ValueError("singular values must remain positive and finite")
        coefficients, _, _, _ = np.linalg.lstsq(design, np.log(values), rcond=None)
        fitted = design @ coefficients
        slopes[index] = float(coefficients[0])
        residuals[index] = float(np.linalg.norm(np.log(values) - fitted))
    return slopes, residuals


def analyze_stage(
    stage: str,
    target_builder: Callable[[float], tuple[StageMap, FloatArray]],
    collision_scales: Iterable[float],
) -> StageSlopeResult:
    """Fit Jacobian singular-value slopes for one stage."""

    scales = np.asarray(tuple(collision_scales), dtype=float)
    if scales.ndim != 1 or scales.size < 3:
        raise ValueError("collision_scales must contain at least three values")
    samples: list[FloatArray] = []
    for h in scales:
        target, parameters = target_builder(float(h))
        singular_values = np.linalg.svd(
            numerical_jacobian(target, parameters), compute_uv=False
        )
        samples.append(np.sort(singular_values)[::-1])
    values = np.asarray(samples, dtype=float)
    slopes, residuals = _fit_slopes(scales, values)
    return StageSlopeResult(stage, scales, slopes, residuals)


def fully_whitened_matrix(operator: FloatArray, gram: FloatArray) -> FloatArray:
    """Return ``B^(-1/2) A B^(-1/2)`` without Gram-mode truncation."""

    values, vectors = eigh(gram, check_finite=True)
    if np.any(values <= 0.0):
        raise ValueError("gram must be positive definite")
    basis = vectors / np.sqrt(values)[None, :]
    matrix = basis.T @ operator @ basis
    return np.asarray(0.5 * (matrix + matrix.T), dtype=float)


def make_weil_stage_maps(
    *,
    sigma: float,
    discriminant: int,
    prime_cutoff: int,
    sample_grid: FloatArray,
) -> dict[str, StageMap]:
    """Construct actual repository target maps as functions of packet centers."""

    character = PrimitiveQuadraticCharacter(discriminant)
    data = CompletedDirichletData(character)

    def packets(centers: FloatArray) -> GaussianPacketFamily:
        return GaussianPacketFamily(centers, sigma=sigma)

    def matrices(centers: FloatArray) -> tuple[FloatArray, FloatArray]:
        family = packets(centers)
        operator = WeilOperator(family, data, prime_cutoff=prime_cutoff)
        return operator.matrix(), operator.gram_matrix()

    def synthesis(centers: FloatArray) -> FloatArray:
        return packets(centers).evaluate(sample_grid).ravel()

    def gram(centers: FloatArray) -> FloatArray:
        return packets(centers).gram_matrix().ravel()

    def weil(centers: FloatArray) -> FloatArray:
        operator, _ = matrices(centers)
        return operator.ravel()

    def paired(centers: FloatArray) -> FloatArray:
        operator, gram_matrix = matrices(centers)
        return np.concatenate((operator.ravel(), gram_matrix.ravel()))

    def whitened(centers: FloatArray) -> FloatArray:
        operator, gram_matrix = matrices(centers)
        return fully_whitened_matrix(operator, gram_matrix).ravel()

    def spectrum(centers: FloatArray) -> FloatArray:
        operator, gram_matrix = matrices(centers)
        return np.asarray(eigh(operator, gram_matrix, eigvals_only=True), dtype=float)

    return {
        "synthesis": synthesis,
        "gram": gram,
        "weil": weil,
        "paired": paired,
        "whitened": whitened,
        "generalized_eigenvalues": spectrum,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cluster-shape", default="-1,0,1")
    parser.add_argument("--exterior-centers", default="4")
    parser.add_argument("--sigma", type=float, default=0.75)
    parser.add_argument("--discriminant", type=int, default=1)
    parser.add_argument("--prime-cutoff", type=int, default=50)
    args = parser.parse_args()

    shape = tuple(float(value) for value in args.cluster_shape.split(",") if value)
    exterior = tuple(
        float(value) for value in args.exterior_centers.split(",") if value
    )
    scales = 10.0 ** (-np.arange(1, 5, dtype=float))
    grid = np.linspace(-6.0, 6.0, 401)
    maps = make_weil_stage_maps(
        sigma=args.sigma,
        discriminant=args.discriminant,
        prime_cutoff=args.prime_cutoff,
        sample_grid=grid,
    )

    for name, target in maps.items():
        def builder(h: float, target: StageMap = target) -> tuple[StageMap, FloatArray]:
            return target, collision_centers(h, shape, exterior)

        result = analyze_stage(name, builder, scales)
        ordered = ", ".join(f"{value:.4f}" for value in np.sort(result.slopes))
        print(f"{name:>24}: {ordered}")


if __name__ == "__main__":
    main()
