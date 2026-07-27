"""Construct uniform witness minors for the raw moment Smith pattern.

For the raw 2m by 2m moment Jacobian, every k-minor has h-order

    sum(selected row degrees) - number(selected position columns)

when its h-free coefficient determinant is nonzero. This module records the
uniform row and column choices that attain the conjectured lower bound.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from fractions import Fraction

from experiments.raw_moment_smith import (
    Rational,
    exact_determinant,
    minor_valuation,
    raw_moment_coefficient_matrix,
)


@dataclass(frozen=True, slots=True)
class UniformWitness:
    """Exact coefficient and valuation of the canonical k-minor."""

    size: int
    valuation: int
    rows: tuple[int, ...]
    columns: tuple[int, ...]
    leading_coefficient: Rational


def predicted_valuation(cluster_size: int, minor_size: int) -> int:
    """Return the proposed valuation of the k-th determinantal divisor."""

    if cluster_size < 2:
        raise ValueError("cluster_size must be at least two")
    if not 1 <= minor_size <= 2 * cluster_size:
        raise ValueError("minor_size must lie between 1 and 2m")
    if minor_size <= cluster_size + 1:
        return (minor_size - 1) * (minor_size - 2) // 2
    return minor_size * (minor_size - 1) // 2 - cluster_size


def predicted_valuations(cluster_size: int) -> tuple[int, ...]:
    """Return all proposed determinantal-divisor valuations."""

    return tuple(
        predicted_valuation(cluster_size, size)
        for size in range(1, 2 * cluster_size + 1)
    )


def canonical_witness_indices(
    cluster_size: int,
    minor_size: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return the uniform row and column sets for a candidate witness minor.

    Columns 0,...,m-1 are weight columns and columns m,...,2m-1 are
    position columns. The witness always uses the first k rows.

    For k <= m+1 it uses one weight column and k-1 position columns. For
    k > m+1 it uses all m position columns and k-m weight columns.
    """

    predicted_valuation(cluster_size, minor_size)
    rows = tuple(range(minor_size))
    if minor_size <= cluster_size + 1:
        columns = (0, *range(cluster_size, cluster_size + minor_size - 1))
    else:
        weight_count = minor_size - cluster_size
        columns = (*range(weight_count), *range(cluster_size, 2 * cluster_size))
    return rows, tuple(columns)


def canonical_witness(
    nodes: Iterable[object],
    weights: Iterable[object],
    minor_size: int,
) -> UniformWitness:
    """Evaluate the canonical witness minor over exact rational arithmetic."""

    node_values = tuple(Fraction(value) for value in nodes)
    weight_values = tuple(Fraction(value) for value in weights)
    matrix = raw_moment_coefficient_matrix(node_values, weight_values)
    cluster_size = len(node_values)
    rows, columns = canonical_witness_indices(cluster_size, minor_size)
    coefficient = exact_determinant(
        [[matrix[row][column] for column in columns] for row in rows]
    )
    return UniformWitness(
        minor_size,
        minor_valuation(rows, columns, cluster_size),
        rows,
        columns,
        coefficient,
    )


def elementary_lower_bound(cluster_size: int, minor_size: int) -> int:
    """Return the universal grade lower bound for a nonzero k-minor.

    The smallest possible sum of k distinct row degrees is 0+...+(k-1).
    At most m position columns exist. When the minimal row set contains row
    zero, a nonzero minor must also contain a weight column because every
    position entry in row zero vanishes. Thus at most k-1 position columns
    can contribute in the range k <= m+1.
    """

    predicted_valuation(cluster_size, minor_size)
    row_sum = minor_size * (minor_size - 1) // 2
    position_count = min(cluster_size, minor_size - 1)
    return row_sum - position_count


def verify_canonical_witnesses(
    nodes: Iterable[object],
    weights: Iterable[object],
) -> tuple[UniformWitness, ...]:
    """Return all canonical witnesses, rejecting a nongeneric specialization."""

    node_values = tuple(nodes)
    weight_values = tuple(weights)
    witnesses = tuple(
        canonical_witness(node_values, weight_values, size)
        for size in range(1, 2 * len(node_values) + 1)
    )
    zero_sizes = [witness.size for witness in witnesses if witness.leading_coefficient == 0]
    if zero_sizes:
        raise ValueError(
            "canonical witness vanished for minor sizes "
            + ", ".join(map(str, zero_sizes))
        )
    return witnesses
