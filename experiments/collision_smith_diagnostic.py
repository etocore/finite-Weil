"""Diagnose h-adic exponents of the simplified corrected collision block.

The model studied here is

    diag(h**m, ..., h**(2*m - 1)) @ C @ B,

where ``C`` is the corrected upper-moment matrix and the columns of ``B`` span
centered node variations. Determinantal valuations are computed from nonzero
minors of the constant matrix ``C @ B``.

This is a diagnostic for the simplified model, not the full collision Jacobian.
"""

from __future__ import annotations

import argparse
from itertools import combinations

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.linalg import null_space

from finite_weil.collisions import corrected_collision_matrix

ComplexArray = NDArray[np.complex128]
ComplexMatrix = NDArray[np.complex128]


def _as_complex_vector(value: ArrayLike, *, name: str) -> ComplexArray:
    vector = np.asarray(value, dtype=np.complex128)
    if vector.ndim != 1 or vector.size < 2:
        raise ValueError(f"{name} must be one-dimensional with length at least two")
    if not np.all(np.isfinite(vector.real)) or not np.all(np.isfinite(vector.imag)):
        raise ValueError(f"{name} must be finite")
    return vector


def centered_frame(nodes: ArrayLike) -> ComplexMatrix:
    """Return an orthonormal basis of ``sum(delta_xi_j) = 0``."""

    xi = _as_complex_vector(nodes, name="nodes")
    constraint = np.ones((1, xi.size), dtype=np.complex128)
    return np.asarray(null_space(constraint), dtype=np.complex128)


def weighted_upper_constant_matrix(
    nodes: ArrayLike,
    weights: ArrayLike,
) -> ComplexMatrix:
    """Return the constant matrix ``C @ B`` for centered node variations."""

    xi = _as_complex_vector(nodes, name="nodes")
    u = _as_complex_vector(weights, name="weights")
    if xi.size != u.size:
        raise ValueError("nodes and weights must have the same length")
    return corrected_collision_matrix(xi, u) @ centered_frame(xi)


def determinantal_valuations(
    constant_matrix: ArrayLike,
    row_grades: ArrayLike,
    *,
    tolerance: float = 1e-10,
) -> tuple[int, ...]:
    """Return minimum h-valuations of nonzero minors of each positive size."""

    matrix = np.asarray(constant_matrix, dtype=np.complex128)
    grades = np.asarray(row_grades, dtype=int)
    if matrix.ndim != 2:
        raise ValueError("constant_matrix must be two-dimensional")
    if grades.ndim != 1 or grades.size != matrix.shape[0]:
        raise ValueError("row_grades must match the matrix row count")
    if tolerance <= 0 or not np.isfinite(tolerance):
        raise ValueError("tolerance must be a finite positive number")

    valuations: list[int] = []
    for size in range(1, min(matrix.shape) + 1):
        best: int | None = None
        for rows in combinations(range(matrix.shape[0]), size):
            row_weight = int(np.sum(grades[list(rows)]))
            for columns in combinations(range(matrix.shape[1]), size):
                minor = matrix[np.ix_(rows, columns)]
                if abs(np.linalg.det(minor)) <= tolerance:
                    continue
                if best is None or row_weight < best:
                    best = row_weight
        if best is None:
            raise ValueError(f"no nonzero minor of size {size}")
        valuations.append(best)
    return tuple(valuations)


def smith_exponents_from_valuations(
    valuations: tuple[int, ...],
) -> tuple[int, ...]:
    """Recover invariant-factor exponents from determinantal-divisor orders."""

    previous = 0
    exponents: list[int] = []
    for value in valuations:
        if value < previous:
            raise ValueError("determinantal valuations must be nondecreasing")
        exponents.append(value - previous)
        previous = value
    return tuple(exponents)


def simplified_upper_exponents(
    nodes: ArrayLike,
    weights: ArrayLike,
) -> tuple[int, ...]:
    """Return h-adic exponents of the simplified centered upper block."""

    xi = _as_complex_vector(nodes, name="nodes")
    matrix = weighted_upper_constant_matrix(xi, weights)
    grades = np.arange(xi.size, 2 * xi.size, dtype=int)
    valuations = determinantal_valuations(matrix, grades)
    return smith_exponents_from_valuations(valuations)


def _parse_numbers(value: str) -> ComplexArray:
    return np.asarray(
        [complex(item.strip()) for item in value.split(",")],
        dtype=np.complex128,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes", default="-1,0,1")
    parser.add_argument("--weights", default="1,2,3")
    args = parser.parse_args()

    nodes = _parse_numbers(args.nodes)
    weights = _parse_numbers(args.weights)
    exponents = simplified_upper_exponents(nodes, weights)
    print("simplified upper exponents:", exponents)
    print("combined with lower block:", tuple(range(nodes.size)) + exponents)


if __name__ == "__main__":
    main()
