"""Exact Smith diagnostics for regular affine collision gauges.

A gauge is represented at a fixed boundary shape by node tangent vectors

    translation, dilation, shape_1, ..., shape_{m-2}.

Translation and dilation columns have h-grade offset one. Shape columns have
offset zero because physical node variations are h times shape variations.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations

from experiments.raw_moment_smith import Rational, exact_determinant

RationalVector = tuple[Rational, ...]
RationalMatrix = tuple[tuple[Rational, ...], ...]


@dataclass(frozen=True, slots=True)
class GaugeSmithResult:
    """Exact determinantal valuations and Smith exponents for one gauge."""

    cluster_size: int
    valuations: tuple[int, ...]
    exponents: tuple[int, ...]


def _fraction_vector(values: Iterable[object]) -> RationalVector:
    return tuple(Fraction(value) for value in values)


def weighted_centered_shape_basis(
    nodes: Iterable[object],
    weights: Iterable[object],
) -> tuple[RationalVector, ...]:
    """Return a rational basis tangent to fixed weighted center and variance.

    The tangent constraints are

        sum_j u_j dxi_j = 0,
        sum_j u_j xi_j dxi_j = 0.

    A deterministic reduced-row-echelon nullspace basis is returned.
    """

    xi = _fraction_vector(nodes)
    u = _fraction_vector(weights)
    if len(xi) != len(u):
        raise ValueError("nodes and weights must have the same length")
    if len(xi) < 2:
        raise ValueError("cluster size must be at least two")

    rows = [list(u), [weight * node for weight, node in zip(u, xi, strict=True)]]
    row_count = len(rows)
    column_count = len(xi)
    pivot_columns: list[int] = []
    pivot_row = 0

    for column in range(column_count):
        candidate = next(
            (row for row in range(pivot_row, row_count) if rows[row][column] != 0),
            None,
        )
        if candidate is None:
            continue
        rows[pivot_row], rows[candidate] = rows[candidate], rows[pivot_row]
        pivot = rows[pivot_row][column]
        rows[pivot_row] = [entry / pivot for entry in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor != 0:
                rows[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[row], rows[pivot_row], strict=True)
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    if len(pivot_columns) != 2:
        raise ValueError("weighted center and variance constraints are not independent")

    free_columns = [column for column in range(column_count) if column not in pivot_columns]
    basis: list[RationalVector] = []
    for free_column in free_columns:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free_column] = Fraction(1)
        for row, pivot_column in enumerate(pivot_columns):
            vector[pivot_column] = -rows[row][free_column]
        basis.append(tuple(vector))
    return tuple(basis)


def gauge_tangent_determinant(
    nodes: Iterable[object],
    shape_basis: Sequence[Sequence[object]],
) -> Rational:
    """Return det[translation, dilation, shape basis]."""

    xi = _fraction_vector(nodes)
    size = len(xi)
    shapes = tuple(_fraction_vector(vector) for vector in shape_basis)
    if len(shapes) != size - 2:
        raise ValueError("shape basis must contain m-2 vectors")
    if any(len(vector) != size for vector in shapes):
        raise ValueError("every shape vector must have length m")

    columns = [tuple(Fraction(1) for _ in xi), xi, *shapes]
    matrix = tuple(
        tuple(columns[column][row] for column in range(size)) for row in range(size)
    )
    return exact_determinant(matrix)


def gauge_coefficient_matrix(
    nodes: Iterable[object],
    weights: Iterable[object],
    shape_basis: Sequence[Sequence[object]],
) -> tuple[RationalMatrix, tuple[int, ...]]:
    """Return the moment Jacobian coefficient matrix and column offsets."""

    xi = _fraction_vector(nodes)
    u = _fraction_vector(weights)
    shapes = tuple(_fraction_vector(vector) for vector in shape_basis)
    if len(xi) != len(u):
        raise ValueError("nodes and weights must have the same length")
    size = len(xi)
    if len(shapes) != size - 2:
        raise ValueError("shape basis must contain m-2 vectors")
    if gauge_tangent_determinant(xi, shapes) == 0:
        raise ValueError("gauge tangent vectors must form a basis")

    node_vectors = [tuple(Fraction(1) for _ in xi), xi, *shapes]
    rows: list[tuple[Rational, ...]] = []
    for degree in range(2 * size):
        weight_columns = tuple(node**degree for node in xi)
        tangent_columns = tuple(
            sum(
                Fraction(0)
                if degree == 0
                else degree * weight * component * node ** (degree - 1)
                for weight, component, node in zip(u, vector, xi, strict=True)
            )
            for vector in node_vectors
        )
        rows.append(weight_columns + tangent_columns)

    offsets = (0,) * size + (1, 1) + (0,) * (size - 2)
    return tuple(rows), offsets


def exact_gauge_smith_data(
    nodes: Iterable[object],
    weights: Iterable[object],
    shape_basis: Sequence[Sequence[object]],
) -> GaugeSmithResult:
    """Compute exact determinantal valuations for a regular affine gauge."""

    matrix, offsets = gauge_coefficient_matrix(nodes, weights, shape_basis)
    matrix_size = len(matrix)
    valuations: list[int] = []

    for minor_size in range(1, matrix_size + 1):
        best: int | None = None
        for selected_rows in combinations(range(matrix_size), minor_size):
            for selected_columns in combinations(range(matrix_size), minor_size):
                valuation = sum(selected_rows) - sum(
                    offsets[column] for column in selected_columns
                )
                if best is not None and valuation >= best:
                    continue
                coefficient = exact_determinant(
                    [
                        [matrix[row][column] for column in selected_columns]
                        for row in selected_rows
                    ]
                )
                if coefficient != 0:
                    best = valuation
        if best is None:
            raise ValueError(f"no nonzero minor of size {minor_size}")
        valuations.append(best)

    previous = 0
    exponents: list[int] = []
    for valuation in valuations:
        exponents.append(valuation - previous)
        previous = valuation
    return GaugeSmithResult(matrix_size // 2, tuple(valuations), tuple(exponents))


def predicted_affine_gauge_exponents(cluster_size: int) -> tuple[int, ...]:
    """Return the generic spectrum for a regular affine collision gauge."""

    if cluster_size < 2:
        raise ValueError("cluster_size must be at least two")
    if cluster_size == 2:
        return (0, 0, 1, 3)
    return (0, 0, 1, *range(3, 2 * cluster_size))
