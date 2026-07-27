"""Measure the effect of the completed-zeta pole matrix at deep prime cutoffs.

For the principal character the deep-cutoff experiments in
``paper/09_prime_cutoff_geometry.md`` reported smallest whitened eigenvalues
near -900 without the pole block.  The explicit formula predicts that adding
the rank-two pole matrix of ``paper/12_pole_term.md`` cancels this negativity
to within the prime-tail truncation error, because the exact assembled form
equals the zero-side sum, which is numerically zero for the packet widths
used here.

This script recomputes the Gram-whitened extreme eigenvalues with and without
the pole matrix for each cutoff and writes one CSV row per case.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from pathlib import Path
from time import perf_counter

import numpy as np

from experiments.convergence import packet_centers, parse_ints
from finite_weil import (
    CompletedDirichletData,
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    WeilOperator,
    generalized_eigenvalues,
)


@dataclass(frozen=True, slots=True)
class PoleCancellationRow:
    dimension: int
    sigma: float
    cutoff: int
    center_extent: float
    lambda_min_without_pole: float
    lambda_min_with_pole: float
    lambda_max_with_pole: float
    retained_rank: int
    runtime_seconds: float


def run_case(
    dimension: int,
    sigma: float,
    cutoff: int,
    center_extent: float,
    relative_tolerance: float,
) -> PoleCancellationRow:
    packets = GaussianPacketFamily(packet_centers(dimension, center_extent), sigma)
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(1))
    gram = packets.gram_matrix()

    start = perf_counter()
    without = WeilOperator(packets=packets, data=data, prime_cutoff=cutoff)
    base_matrix = without.matrix()
    values_without = generalized_eigenvalues(
        base_matrix,
        gram,
        relative_tolerance=relative_tolerance,
    )
    with_pole = WeilOperator(
        packets=packets,
        data=data,
        prime_cutoff=cutoff,
        include_pole=True,
    )
    values_with = generalized_eigenvalues(
        base_matrix + with_pole.pole_matrix(),
        gram,
        relative_tolerance=relative_tolerance,
    )
    elapsed = perf_counter() - start

    retained = np.linalg.eigvalsh(gram)
    rank = int(np.count_nonzero(retained > relative_tolerance * retained[-1]))

    return PoleCancellationRow(
        dimension=dimension,
        sigma=sigma,
        cutoff=cutoff,
        center_extent=center_extent,
        lambda_min_without_pole=float(values_without[0]),
        lambda_min_with_pole=float(values_with[0]),
        lambda_max_with_pole=float(values_with[-1]),
        retained_rank=rank,
        runtime_seconds=float(elapsed),
    )


def write_rows(path: Path, rows: list[PoleCancellationRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(PoleCancellationRow.__annotations__),
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dimensions", default="8,16")
    parser.add_argument("--sigma", type=float, default=0.5)
    parser.add_argument("--cutoffs", default="100000,1000000,10000000")
    parser.add_argument("--center-extent", type=float, default=6.0)
    parser.add_argument("--relative-tolerance", type=float, default=1e-12)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/pole-cancellation.csv"),
    )
    args = parser.parse_args()

    rows: list[PoleCancellationRow] = []
    for dimension in parse_ints(args.dimensions):
        for cutoff in parse_ints(args.cutoffs):
            row = run_case(
                dimension=dimension,
                sigma=args.sigma,
                cutoff=cutoff,
                center_extent=args.center_extent,
                relative_tolerance=args.relative_tolerance,
            )
            rows.append(row)
            print(
                f"n={row.dimension:>2} cutoff={row.cutoff:>9} "
                f"lambda_min(no pole)={row.lambda_min_without_pole:>14.6f} "
                f"lambda_min(pole)={row.lambda_min_with_pole:>12.6f} "
                f"lambda_max(pole)={row.lambda_max_with_pole:>12.6f}"
            )

    write_rows(args.output, rows)
    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
