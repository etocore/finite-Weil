"""Compute exact determinantal valuations for a collision-block diagnostic.

The raw confluent moment Jacobian should be analyzed directly whenever available.
This module retains the older reduced upper block as a comparison model, but its
rational-input CLI now performs all polynomial algebra and minor tests exactly.
Floating-point determinants are not used to decide whether a minor vanishes.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
from typing import TypeAlias

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.linalg import null_space

from finite_weil.collisions import corrected_collision_matrix

ComplexArray = NDArray[np.complex128]
ComplexMatrix = NDArray[np.complex128]
RationalMatrix: TypeAlias = tuple[tuple[Fraction, ...], ...]


def _as_complex_vector(value: ArrayLike, *, name: str) -> ComplexArray:
    vector = np.asarray(value, dtype=np.complex128)
    if vector.ndim != 1 or vector.size < 2:
        raise ValueError(f"{name} must be one-dimensional with length at least two")
    if not np.all(np.isfinite(vector.real)) or not np.all(np.isfinite(vector.imag)):
        raise ValueError(f"{name} must be finite")
    return vector


def centered_frame(nodes: ArrayLike) -> ComplexMatrix:
    """Return an orthonormal floating basis of ``sum(delta_xi_j) = 0``."""

    xi = _as_complex_vector(nodes, name="nodes")
    constraint = np.ones((1, xi.size), dtype=np.complex128)
    return np.asarray(null_space(constraint), dtype=np.complex128)


def exact_centered_frame(size: int) -> RationalMatrix:
    """Return the integer frame ``e_j - e_last`` for centered variations."""

    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 2:
        raise ValueError("size must be at least two")
    return tuple(
        tuple(
            Fraction(1 if row == column else -1 if row == size - 1 else 0)
            for column in range(size - 1)
        )
        for row in range(size)
    )


def weighted_upper_constant_matrix(
    nodes: ArrayLike,
    weights: ArrayLike,
) -> ComplexMatrix:
    """Return the floating comparison matrix ``C @ B``."""

    xi = _as_complex_vector(nodes, name="nodes")
    u = _as_complex_vector(weights, name="weights")
    if xi.size != u.size:
        raise ValueError("nodes and weights must have the same length")
    return corrected_collision_matrix(xi, u) @ centered_frame(xi)


def _poly_multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def _node_polynomial(nodes: tuple[Fraction, ...]) -> list[Fraction]:
    coefficients = [Fraction(1)]
    for node in nodes:
        coefficients = _poly_multiply(coefficients, [Fraction(1), -node])
    return coefficients


def _monomial_quotient(
    node_polynomial: list[Fraction],
    dividend_degree: int,
) -> list[Fraction]:
    """Divide ``t**dividend_degree`` by a monic polynomial, descending order."""

    divisor_degree = len(node_polynomial) - 1
    if dividend_degree < divisor_degree:
        return [Fraction(0)]
    remainder = [Fraction(1)] + [Fraction(0)] * dividend_degree
    quotient = [Fraction(0)] * (dividend_degree - divisor_degree + 1)
    for index in range(len(quotient)):
        coefficient = remainder[index]
        quotient[index] = coefficient
        if coefficient:
            for offset, divisor_coefficient in enumerate(node_polynomial):
                remainder[index + offset] -= coefficient * divisor_coefficient
    return quotient


def _polyval(coefficients: list[Fraction], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in coefficients:
        result = result * value + coefficient
    return result


def exact_corrected_collision_matrix(
    nodes: tuple[Fraction, ...],
    weights: tuple[Fraction, ...],
) -> RationalMatrix:
    """Return the corrected collision matrix exactly over ``Q``."""

    if len(nodes) != len(weights):
        raise ValueError("nodes and weights must have the same length")
    if len(nodes) < 2 or len(set(nodes)) != len(nodes):
        raise ValueError("nodes must be pairwise distinct and have length at least two")
    size = len(nodes)
    polynomial = _node_polynomial(nodes)
    derivatives = tuple(
        np.prod([nodes[j] - nodes[k] for k in range(size) if k != j], dtype=object)
        for j in range(size)
    )
    rows: list[tuple[Fraction, ...]] = []
    for offset in range(size):
        quotient = _monomial_quotient(polynomial, size + offset)
        rows.append(
            tuple(
                weights[j]
                * Fraction(derivatives[j])
                * _polyval(quotient, nodes[j])
                for j in range(size)
            )
        )
    return tuple(rows)


def _matrix_multiply(left: RationalMatrix, right: RationalMatrix) -> RationalMatrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not align")
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def exact_weighted_upper_constant_matrix(
    nodes: tuple[Fraction, ...],
    weights: tuple[Fraction, ...],
) -> RationalMatrix:
    """Return ``C @ B`` exactly using the integer centered frame."""

    return _matrix_multiply(
        exact_corrected_collision_matrix(nodes, weights),
        exact_centered_frame(len(nodes)),
    )


def _exact_determinant(matrix: RationalMatrix) -> Fraction:
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a nonempty square matrix")
    work = [list(row) for row in matrix]
    sign = 1
    determinant = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        determinant *= pivot_value
        for row in range(column + 1, size):
            factor = work[row][column] / pivot_value
            for local_column in range(column + 1, size):
                work[row][local_column] -= factor * work[column][local_column]
    return sign * determinant


def exact_determinantal_valuations(
    constant_matrix: RationalMatrix,
    row_grades: tuple[int, ...],
) -> tuple[int, ...]:
    """Return minimum row-grade sums among exactly nonzero minors."""

    row_count = len(constant_matrix)
    if row_count == 0:
        raise ValueError("constant_matrix must be nonempty")
    column_count = len(constant_matrix[0])
    if any(len(row) != column_count for row in constant_matrix):
        raise ValueError("constant_matrix rows must have equal length")
    if len(row_grades) != row_count:
        raise ValueError("row_grades must match the matrix row count")

    valuations: list[int] = []
    for size in range(1, min(row_count, column_count) + 1):
        best: int | None = None
        for rows in combinations(range(row_count), size):
            row_weight = sum(row_grades[row] for row in rows)
            for columns in combinations(range(column_count), size):
                minor = tuple(
                    tuple(constant_matrix[row][column] for column in columns)
                    for row in rows
                )
                if _exact_determinant(minor) == 0:
                    continue
                if best is None or row_weight < best:
                    best = row_weight
        if best is None:
            raise ValueError(f"no nonzero minor of size {size}")
        valuations.append(best)
    return tuple(valuations)


def determinantal_valuations(
    constant_matrix: ArrayLike,
    row_grades: ArrayLike,
    *,
    tolerance: float = 1e-10,
) -> tuple[int, ...]:
    """Compatibility floating-point valuation diagnostic.

    Exact polynomial work should use :func:`exact_determinantal_valuations`.
    """

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
    """Return floating diagnostic exponents of the reduced upper block."""

    xi = _as_complex_vector(nodes, name="nodes")
    matrix = weighted_upper_constant_matrix(xi, weights)
    grades = np.arange(xi.size, 2 * xi.size, dtype=int)
    return smith_exponents_from_valuations(determinantal_valuations(matrix, grades))


def exact_simplified_upper_exponents(
    nodes: tuple[Fraction, ...],
    weights: tuple[Fraction, ...],
) -> tuple[int, ...]:
    """Return exact exponents of the reduced comparison block."""

    matrix = exact_weighted_upper_constant_matrix(nodes, weights)
    grades = tuple(range(len(nodes), 2 * len(nodes)))
    return smith_exponents_from_valuations(
        exact_determinantal_valuations(matrix, grades)
    )


def _parse_rationals(value: str) -> tuple[Fraction, ...]:
    return tuple(Fraction(item.strip()) for item in value.split(","))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes", default="-1,0,1")
    parser.add_argument("--weights", default="1,2,3")
    args = parser.parse_args()

    nodes = _parse_rationals(args.nodes)
    weights = _parse_rationals(args.weights)
    matrix = exact_weighted_upper_constant_matrix(nodes, weights)
    grades = tuple(range(len(nodes), 2 * len(nodes)))
    valuations = exact_determinantal_valuations(matrix, grades)
    exponents = smith_exponents_from_valuations(valuations)
    print("exact reduced-block valuations:", valuations)
    print("exact reduced-block exponents:", exponents)
    print("warning: this reduced block is not the raw moment Jacobian germ")


if __name__ == "__main__":
    main()
