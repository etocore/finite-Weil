"""Compute exact h-adic determinantal data for the raw moment Jacobian.

For nodes ``x_j = h * xi_j`` and weights ``u_j``, consider moments

    M_r = sum_j u_j x_j**r,     0 <= r < 2m.

The Jacobian with respect to weights and node positions has columns

    dM_r/du_j = x_j**r,
    dM_r/dx_j = r * u_j * x_j**(r - 1).

Every entry is a rational coefficient times one power of ``h``. For any fixed
minor, every determinant term has the same h-order, so its valuation is

    sum(selected rows) - number(selected position columns)

provided the corresponding coefficient determinant is nonzero. This makes the
full determinantal-ideal computation exact and avoids polynomial expansion.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations

Rational = Fraction
RationalMatrix = tuple[tuple[Rational, ...], ...]


@dataclass(frozen=True, slots=True)
class MinorWitness:
    """One nonzero minor attaining a determinantal valuation."""

    size: int
    valuation: int
    rows: tuple[int, ...]
    columns: tuple[int, ...]
    leading_coefficient: Rational


@dataclass(frozen=True, slots=True)
class RawMomentSmithResult:
    """Exact determinantal valuations, Smith exponents, and witnesses."""

    cluster_size: int
    valuations: tuple[int, ...]
    exponents: tuple[int, ...]
    witnesses: tuple[MinorWitness, ...]


def _as_rationals(values: Iterable[object], *, name: str) -> tuple[Rational, ...]:
    result = tuple(Fraction(value) for value in values)
    if len(result) < 2:
        raise ValueError(f"{name} must contain at least two entries")
    return result


def exact_determinant(matrix: Sequence[Sequence[Rational]]) -> Rational:
    """Return a determinant over Q by fraction-preserving elimination."""

    rows = [list(map(Fraction, row)) for row in matrix]
    size = len(rows)
    if any(len(row) != size for row in rows):
        raise ValueError("matrix must be square")
    determinant = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if rows[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            determinant = -determinant
        pivot_value = rows[column][column]
        determinant *= pivot_value
        for row in range(column + 1, size):
            factor = rows[row][column] / pivot_value
            for entry in range(column + 1, size):
                rows[row][entry] -= factor * rows[column][entry]
    return determinant


def raw_moment_coefficient_matrix(
    nodes: Iterable[object],
    weights: Iterable[object],
) -> RationalMatrix:
    """Return the h-free coefficient matrix of the 2m by 2m Jacobian."""

    xi = _as_rationals(nodes, name="nodes")
    u = _as_rationals(weights, name="weights")
    if len(xi) != len(u):
        raise ValueError("nodes and weights must have the same length")
    if len(set(xi)) != len(xi):
        raise ValueError("nodes must be pairwise distinct")

    size = 2 * len(xi)
    rows: list[tuple[Rational, ...]] = []
    for degree in range(size):
        weight_entries = tuple(node**degree for node in xi)
        position_entries = tuple(
            Fraction(0)
            if degree == 0
            else degree * weight * node ** (degree - 1)
            for node, weight in zip(xi, u, strict=True)
        )
        rows.append(weight_entries + position_entries)
    return tuple(rows)


def minor_valuation(
    rows: Sequence[int],
    columns: Sequence[int],
    cluster_size: int,
) -> int:
    """Return the common h-order of all terms in the selected minor."""

    position_columns = sum(column >= cluster_size for column in columns)
    return sum(rows) - position_columns


def exact_determinantal_data(
    nodes: Iterable[object],
    weights: Iterable[object],
) -> RawMomentSmithResult:
    """Compute all exact determinantal valuations and one witness per size."""

    matrix = raw_moment_coefficient_matrix(nodes, weights)
    size = len(matrix)
    cluster_size = size // 2
    valuations: list[int] = []
    witnesses: list[MinorWitness] = []

    for minor_size in range(1, size + 1):
        best: MinorWitness | None = None
        for selected_rows in combinations(range(size), minor_size):
            for selected_columns in combinations(range(size), minor_size):
                valuation = minor_valuation(
                    selected_rows, selected_columns, cluster_size
                )
                if best is not None and valuation >= best.valuation:
                    continue
                coefficient = exact_determinant(
                    [
                        [matrix[row][column] for column in selected_columns]
                        for row in selected_rows
                    ]
                )
                if coefficient != 0:
                    best = MinorWitness(
                        minor_size,
                        valuation,
                        selected_rows,
                        selected_columns,
                        coefficient,
                    )
        if best is None:
            raise ValueError(f"no nonzero minor of size {minor_size}")
        valuations.append(best.valuation)
        witnesses.append(best)

    previous = 0
    exponents: list[int] = []
    for valuation in valuations:
        exponents.append(valuation - previous)
        previous = valuation
    return RawMomentSmithResult(
        cluster_size,
        tuple(valuations),
        tuple(exponents),
        tuple(witnesses),
    )


def predicted_exponents(cluster_size: int) -> tuple[int, ...]:
    """Return the missing-grade pattern suggested by exact computations."""

    if cluster_size < 2:
        raise ValueError("cluster_size must be at least two")
    return (
        0,
        0,
        *range(1, cluster_size),
        *range(cluster_size + 1, 2 * cluster_size),
    )


def _parse_rationals(text: str) -> tuple[Rational, ...]:
    return tuple(Fraction(item.strip()) for item in text.split(",") if item.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes", default="-1,0,1")
    parser.add_argument("--weights", default="1,2,3")
    args = parser.parse_args()

    result = exact_determinantal_data(
        _parse_rationals(args.nodes),
        _parse_rationals(args.weights),
    )
    print("m:", result.cluster_size)
    print("valuations:", result.valuations)
    print("Smith exponents:", result.exponents)
    print("predicted:", predicted_exponents(result.cluster_size))
    for witness in result.witnesses:
        print(
            f"k={witness.size}: nu={witness.valuation}, "
            f"rows={witness.rows}, columns={witness.columns}, "
            f"coefficient={witness.leading_coefficient}"
        )


if __name__ == "__main__":
    main()
