"""Exact permutation-equivariance diagnostics for raw collision Jacobians.

The raw moment map is symmetric under simultaneous permutation of node-weight pairs.
This module verifies the corresponding covariance of its Jacobian and records the
boundary-filtration dimensions implied by a Smith exponent list.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from fractions import Fraction

Rational = Fraction
RationalMatrix = tuple[tuple[Rational, ...], ...]


def raw_moment_coefficient_matrix(
    nodes: Iterable[object],
    weights: Iterable[object],
) -> RationalMatrix:
    """Return the coefficient matrix of the physical raw moment Jacobian.

    Rows are indexed by degrees 0 through 2m-1. Columns are ordered as all weight
    columns followed by all physical-position columns. Explicit powers of the
    collision scale are omitted because permutation covariance concerns only the
    coefficient matrix.
    """

    xi = tuple(Fraction(value) for value in nodes)
    u = tuple(Fraction(value) for value in weights)
    if len(xi) != len(u):
        raise ValueError("nodes and weights must have the same length")
    if not xi:
        raise ValueError("at least one node is required")

    size = len(xi)
    rows: list[tuple[Rational, ...]] = []
    for degree in range(2 * size):
        weight_columns = tuple(node**degree for node in xi)
        position_columns = tuple(
            Fraction(0)
            if degree == 0
            else degree * weight * node ** (degree - 1)
            for node, weight in zip(xi, u, strict=True)
        )
        rows.append(weight_columns + position_columns)
    return tuple(rows)


def permute_pairs(
    nodes: Sequence[object],
    weights: Sequence[object],
    permutation: Sequence[int],
) -> tuple[tuple[Rational, ...], tuple[Rational, ...]]:
    """Simultaneously permute node-weight pairs."""

    size = len(nodes)
    if len(weights) != size or sorted(permutation) != list(range(size)):
        raise ValueError("permutation must contain every pair index exactly once")
    xi = tuple(Fraction(nodes[index]) for index in permutation)
    u = tuple(Fraction(weights[index]) for index in permutation)
    return xi, u


def permuted_column_order(permutation: Sequence[int]) -> tuple[int, ...]:
    """Return the induced column order on weight and position columns."""

    size = len(permutation)
    if sorted(permutation) != list(range(size)):
        raise ValueError("invalid permutation")
    return tuple(permutation) + tuple(size + index for index in permutation)


def reorder_columns(matrix: RationalMatrix, order: Sequence[int]) -> RationalMatrix:
    """Return a matrix with columns selected in the supplied order."""

    return tuple(tuple(row[index] for index in order) for row in matrix)


def filtration_dimensions(exponents: Iterable[int]) -> tuple[int, ...]:
    """Return dim Lambda_r/hLambda_r for every nontrivial filtration level.

    For Smith exponents e_i, the boundary divisibility filtration has dimension
    #{i : e_i >= r} at level r.
    """

    values = tuple(int(value) for value in exponents)
    if any(value < 0 for value in values):
        raise ValueError("Smith exponents must be nonnegative")
    if not values:
        return ()
    return tuple(sum(value >= level for value in values) for level in range(max(values) + 1))
