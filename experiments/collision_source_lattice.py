"""Compare physical node coordinates with an anchored collision chart.

Fix an affine normalization

    xi_0 = 0,  xi_1 = 1,

and write

    x_j = c + h * xi_j.

The collision-chart variables are

    (u_0,...,u_{m-1}, c, h, xi_2,...,xi_{m-1}).

This module computes the exact source-change determinant and the exact h-adic
minors of the raw moment map in that chart.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations

from experiments.raw_moment_smith import Rational, exact_determinant

RationalMatrix = tuple[tuple[Rational, ...], ...]


@dataclass(frozen=True, slots=True)
class ChartSmithResult:
    """Exact determinantal valuations and Smith exponents in the chart."""

    cluster_size: int
    valuations: tuple[int, ...]
    exponents: tuple[int, ...]


def _as_rationals(values: Iterable[object], *, name: str) -> tuple[Rational, ...]:
    result = tuple(Fraction(value) for value in values)
    if len(result) < 2:
        raise ValueError(f"{name} must contain at least two entries")
    return result


def source_change_coefficient_matrix(nodes: Iterable[object]) -> RationalMatrix:
    """Return the h-free part of d(c,h,shape) -> d(x_0,...,x_{m-1}).

    The actual source-change matrix has columns

        1, xi, h e_2, ..., h e_{m-1}.

    This function removes the explicit h from the shape columns.
    """

    xi = _as_rationals(nodes, name="nodes")
    if xi[0] != 0 or xi[1] != 1:
        raise ValueError("anchored chart requires nodes[0] == 0 and nodes[1] == 1")
    if len(set(xi)) != len(xi):
        raise ValueError("nodes must be pairwise distinct")

    size = len(xi)
    columns = [tuple(Fraction(1) for _ in xi), xi]
    for index in range(2, size):
        columns.append(tuple(Fraction(row == index) for row in range(size)))
    return tuple(tuple(columns[column][row] for column in range(size)) for row in range(size))


def source_change_determinant(nodes: Iterable[object]) -> Rational:
    """Return the coefficient of h**(m-2) in the source-change determinant."""

    return exact_determinant(source_change_coefficient_matrix(nodes))


def chart_coefficient_matrix(
    nodes: Iterable[object],
    weights: Iterable[object],
) -> tuple[RationalMatrix, tuple[int, ...]]:
    """Return chart coefficients and column grade offsets.

    Every entry in row r and column j equals a rational coefficient times
    h**(r-offset[j]). Weight and shape columns have offset zero; center and
    scale columns have offset one.
    """

    xi = _as_rationals(nodes, name="nodes")
    u = _as_rationals(weights, name="weights")
    if len(xi) != len(u):
        raise ValueError("nodes and weights must have the same length")
    if xi[0] != 0 or xi[1] != 1:
        raise ValueError("anchored chart requires nodes[0] == 0 and nodes[1] == 1")
    if len(set(xi)) != len(xi):
        raise ValueError("nodes must be pairwise distinct")

    size = len(xi)
    rows: list[tuple[Rational, ...]] = []
    for degree in range(2 * size):
        weight_columns = tuple(node**degree for node in xi)
        center_column = sum(
            Fraction(0) if degree == 0 else degree * weight * node ** (degree - 1)
            for node, weight in zip(xi, u, strict=True)
        )
        scale_column = sum(
            Fraction(0) if degree == 0 else degree * weight * node**degree
            for node, weight in zip(xi, u, strict=True)
        )
        shape_columns = tuple(
            Fraction(0)
            if degree == 0
            else degree * u[index] * xi[index] ** (degree - 1)
            for index in range(2, size)
        )
        rows.append(weight_columns + (center_column, scale_column) + shape_columns)

    offsets = (0,) * size + (1, 1) + (0,) * (size - 2)
    return tuple(rows), offsets


def exact_chart_smith_data(
    nodes: Iterable[object],
    weights: Iterable[object],
) -> ChartSmithResult:
    """Compute exact determinantal valuations in the anchored chart."""

    matrix, offsets = chart_coefficient_matrix(nodes, weights)
    size = len(matrix)
    valuations: list[int] = []

    for minor_size in range(1, size + 1):
        best: int | None = None
        for selected_rows in combinations(range(size), minor_size):
            for selected_columns in combinations(range(size), minor_size):
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
    return ChartSmithResult(size // 2, tuple(valuations), tuple(exponents))


def predicted_chart_exponents(cluster_size: int) -> tuple[int, ...]:
    """Return the pattern suggested by exact anchored-chart computations."""

    if cluster_size < 2:
        raise ValueError("cluster_size must be at least two")
    if cluster_size == 2:
        return (0, 0, 1, 3)
    return (0, 0, 1, *range(3, 2 * cluster_size))
