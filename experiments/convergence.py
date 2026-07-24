"""Run reproducible spectral-refinement experiments for finite Weil operators.

The script writes one CSV row per parameter tuple. It studies the finite model
itself and deliberately does not interpret the output as evidence for any zero
hypothesis.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from pathlib import Path
from time import perf_counter

import numpy as np
from scipy.linalg import eigh

from finite_weil import (
    CompletedDirichletData,
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    WeilOperator,
)


@dataclass(frozen=True, slots=True)
class ExperimentRow:
    discriminant: int
    dimension: int
    sigma: float
    cutoff: int
    center_extent: float
    relative_tolerance: float
    retained_rank: int
    lambda_min: float
    lambda_max: float
    operator_norm: float
    gram_condition: float
    runtime_seconds: float


def packet_centers(dimension: int, extent: float) -> np.ndarray:
    """Return evenly spaced centers on ``[-extent, extent]``."""

    if dimension < 1:
        raise ValueError("dimension must be positive")
    if extent <= 0 or not np.isfinite(extent):
        raise ValueError("extent must be a finite positive number")
    if dimension == 1:
        return np.asarray([0.0], dtype=float)
    return np.linspace(-extent, extent, dimension, dtype=float)


def stable_gram_rank(gram: np.ndarray, relative_tolerance: float) -> int:
    """Return the number of Gram eigenmodes retained by whitening."""

    values = eigh(gram, eigvals_only=True, check_finite=True)
    maximum = float(values[-1])
    if maximum <= 0:
        raise ValueError("gram must be positive definite on a nonzero subspace")
    return int(np.count_nonzero(values > relative_tolerance * maximum))


def run_case(
    discriminant: int,
    dimension: int,
    sigma: float,
    cutoff: int,
    center_extent: float,
    relative_tolerance: float = 1e-12,
) -> ExperimentRow:
    """Run one stabilized generalized-eigenvalue experiment."""

    character = PrimitiveQuadraticCharacter(discriminant)
    packets = GaussianPacketFamily(packet_centers(dimension, center_extent), sigma)
    data = CompletedDirichletData(character)
    operator = WeilOperator(packets=packets, data=data, prime_cutoff=cutoff)

    start = perf_counter()
    gram = operator.gram_matrix()
    retained_rank = stable_gram_rank(gram, relative_tolerance)
    eigenvalues = operator.generalized_eigenvalues(
        relative_tolerance=relative_tolerance
    )
    elapsed = perf_counter() - start

    return ExperimentRow(
        discriminant=discriminant,
        dimension=dimension,
        sigma=sigma,
        cutoff=cutoff,
        center_extent=center_extent,
        relative_tolerance=relative_tolerance,
        retained_rank=retained_rank,
        lambda_min=float(eigenvalues[0]),
        lambda_max=float(eigenvalues[-1]),
        operator_norm=float(np.max(np.abs(eigenvalues))),
        gram_condition=float(np.linalg.cond(gram)),
        runtime_seconds=float(elapsed),
    )


def write_rows(path: Path, rows: list[ExperimentRow]) -> None:
    """Write experiment rows as a deterministic CSV file."""

    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(asdict(rows[0]).keys()) if rows else list(ExperimentRow.__annotations__)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def parse_ints(value: str) -> tuple[int, ...]:
    return tuple(int(item.strip()) for item in value.split(",") if item.strip())


def parse_floats(value: str) -> tuple[float, ...]:
    return tuple(float(item.strip()) for item in value.split(",") if item.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discriminants", default="1,-3,5,8,13")
    parser.add_argument("--dimensions", default="4,8,16,32")
    parser.add_argument("--sigmas", default="0.25,0.5,1.0")
    parser.add_argument("--cutoffs", default="50,100,250,500,1000")
    parser.add_argument("--center-extent", type=float, default=6.0)
    parser.add_argument("--relative-tolerance", type=float, default=1e-12)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/convergence.csv"),
    )
    args = parser.parse_args()

    rows: list[ExperimentRow] = []
    for discriminant in parse_ints(args.discriminants):
        for dimension in parse_ints(args.dimensions):
            for sigma in parse_floats(args.sigmas):
                for cutoff in parse_ints(args.cutoffs):
                    row = run_case(
                        discriminant=discriminant,
                        dimension=dimension,
                        sigma=sigma,
                        cutoff=cutoff,
                        center_extent=args.center_extent,
                        relative_tolerance=args.relative_tolerance,
                    )
                    rows.append(row)
                    print(
                        f"D={discriminant:>3} n={dimension:>2} sigma={sigma:g} "
                        f"cutoff={cutoff:>4} lambda_min={row.lambda_min:.8g} "
                        f"cond(B)={row.gram_condition:.4g} rank={row.retained_rank}"
                    )

    write_rows(args.output, rows)
    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
