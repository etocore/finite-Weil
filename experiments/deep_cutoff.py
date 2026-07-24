"""Resolve the sharp prime sum beyond the packet-translation scale.

For packets centered on ``[-extent, extent]``, pairwise center differences reach
``2 * extent``. Since the prime kernel is centered near ``log(n) = delta``, small
cutoffs can stop long before the matrix entries have passed their dominant range.
This experiment pushes the exact sharp sum to deep cutoffs and records the
Gram-whitened spectrum.
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
class DeepCutoffRow:
    discriminant: int
    dimension: int
    sigma: float
    cutoff: int
    center_extent: float
    lambda_min: float
    lambda_max: float
    operator_norm: float
    retained_rank: int
    runtime_seconds: float


def retained_rank(gram: np.ndarray, relative_tolerance: float) -> int:
    values = np.linalg.eigvalsh(gram)
    return int(np.count_nonzero(values > relative_tolerance * values[-1]))


def run_case(
    discriminant: int,
    dimension: int,
    sigma: float,
    cutoff: int,
    center_extent: float,
    relative_tolerance: float,
) -> DeepCutoffRow:
    character = PrimitiveQuadraticCharacter(discriminant)
    packets = GaussianPacketFamily(packet_centers(dimension, center_extent), sigma)
    operator = WeilOperator(
        packets=packets,
        data=CompletedDirichletData(character),
        prime_cutoff=cutoff,
    )

    start = perf_counter()
    gram = operator.gram_matrix()
    eigenvalues = generalized_eigenvalues(
        operator.matrix(),
        gram,
        relative_tolerance=relative_tolerance,
    )
    elapsed = perf_counter() - start

    return DeepCutoffRow(
        discriminant=discriminant,
        dimension=dimension,
        sigma=sigma,
        cutoff=cutoff,
        center_extent=center_extent,
        lambda_min=float(eigenvalues[0]),
        lambda_max=float(eigenvalues[-1]),
        operator_norm=float(np.max(np.abs(eigenvalues))),
        retained_rank=retained_rank(gram, relative_tolerance),
        runtime_seconds=float(elapsed),
    )


def write_rows(path: Path, rows: list[DeepCutoffRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(DeepCutoffRow.__annotations__))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discriminant", type=int, default=1)
    parser.add_argument("--dimensions", default="8,16,32")
    parser.add_argument("--sigma", type=float, default=0.5)
    parser.add_argument(
        "--cutoffs",
        default="1000,10000,100000,300000,1000000,3000000,10000000",
    )
    parser.add_argument("--center-extent", type=float, default=6.0)
    parser.add_argument("--relative-tolerance", type=float, default=1e-12)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/deep-cutoff.csv"),
    )
    args = parser.parse_args()

    rows: list[DeepCutoffRow] = []
    for dimension in parse_ints(args.dimensions):
        for cutoff in parse_ints(args.cutoffs):
            row = run_case(
                discriminant=args.discriminant,
                dimension=dimension,
                sigma=args.sigma,
                cutoff=cutoff,
                center_extent=args.center_extent,
                relative_tolerance=args.relative_tolerance,
            )
            rows.append(row)
            print(
                f"D={row.discriminant:>3} n={row.dimension:>2} "
                f"sigma={row.sigma:g} cutoff={row.cutoff:>8} "
                f"lambda_min={row.lambda_min:.10g} rank={row.retained_rank}"
            )

    write_rows(args.output, rows)
    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
