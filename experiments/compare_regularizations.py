"""Compare sharp and smoothly weighted prime truncations.

This experiment evaluates the smallest Gram-whitened eigenvalue for three prime
weights:

- sharp cutoff;
- exponential damping ``exp(-n / cutoff)``;
- log-Gaussian damping ``exp(-(log(n) / log(cutoff))**2)``.

The output is a CSV file containing one row per parameter tuple. Smooth weights
are numerical regularizations only and are not interpreted as proved tail
corrections.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from pathlib import Path
from time import perf_counter

import numpy as np

from experiments.convergence import packet_centers, parse_floats, parse_ints
from finite_weil import (
    CompletedDirichletData,
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    WeilOperator,
    exponential_prime_weight,
    gaussian_log_prime_weight,
    generalized_eigenvalues,
    sharp_prime_weight,
)


@dataclass(frozen=True, slots=True)
class RegularizationRow:
    discriminant: int
    dimension: int
    sigma: float
    cutoff: int
    weight: str
    lambda_min: float
    lambda_max: float
    operator_norm: float
    gram_condition: float
    retained_rank: int
    runtime_seconds: float


WEIGHTS = {
    "sharp": (sharp_prime_weight, 1.0),
    "exponential": (exponential_prime_weight, 8.0),
    "gaussian_log": (gaussian_log_prime_weight, 8.0),
}


def retained_gram_rank(gram: np.ndarray, relative_tolerance: float) -> int:
    """Return the number of Gram modes retained by whitening."""

    eigenvalues = np.linalg.eigvalsh(gram)
    maximum = float(eigenvalues[-1])
    return int(np.count_nonzero(eigenvalues > relative_tolerance * maximum))


def run_case(
    discriminant: int,
    dimension: int,
    sigma: float,
    cutoff: int,
    center_extent: float,
    weight_name: str,
    relative_tolerance: float,
) -> RegularizationRow:
    """Run one weighted, Gram-whitened spectral experiment."""

    if weight_name not in WEIGHTS:
        raise ValueError(f"unknown weight: {weight_name}")

    weight, support_multiplier = WEIGHTS[weight_name]
    character = PrimitiveQuadraticCharacter(discriminant)
    packets = GaussianPacketFamily(packet_centers(dimension, center_extent), sigma)
    data = CompletedDirichletData(character)
    operator = WeilOperator(
        packets=packets,
        data=data,
        prime_cutoff=cutoff,
        prime_weight=weight,
        prime_support_multiplier=support_multiplier,
    )

    start = perf_counter()
    gram = operator.gram_matrix()
    matrix = operator.matrix()
    eigenvalues = generalized_eigenvalues(
        matrix,
        gram,
        relative_tolerance=relative_tolerance,
    )
    elapsed = perf_counter() - start

    return RegularizationRow(
        discriminant=discriminant,
        dimension=dimension,
        sigma=sigma,
        cutoff=cutoff,
        weight=weight_name,
        lambda_min=float(eigenvalues[0]),
        lambda_max=float(eigenvalues[-1]),
        operator_norm=float(np.max(np.abs(eigenvalues))),
        gram_condition=float(np.linalg.cond(gram)),
        retained_rank=retained_gram_rank(gram, relative_tolerance),
        runtime_seconds=float(elapsed),
    )


def write_rows(path: Path, rows: list[RegularizationRow]) -> None:
    """Write comparison rows as CSV."""

    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(RegularizationRow.__annotations__)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discriminants", default="1,-3,5,8,13")
    parser.add_argument("--dimensions", default="4,8,16,32")
    parser.add_argument("--sigmas", default="0.25,0.5,1.0")
    parser.add_argument("--cutoffs", default="50,100,250,500,1000")
    parser.add_argument("--weights", default="sharp,exponential,gaussian_log")
    parser.add_argument("--center-extent", type=float, default=6.0)
    parser.add_argument("--relative-tolerance", type=float, default=1e-12)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/regularized-comparison.csv"),
    )
    args = parser.parse_args()

    selected_weights = tuple(
        item.strip() for item in args.weights.split(",") if item.strip()
    )
    rows: list[RegularizationRow] = []
    for discriminant in parse_ints(args.discriminants):
        for dimension in parse_ints(args.dimensions):
            for sigma in parse_floats(args.sigmas):
                for cutoff in parse_ints(args.cutoffs):
                    for weight_name in selected_weights:
                        row = run_case(
                            discriminant=discriminant,
                            dimension=dimension,
                            sigma=sigma,
                            cutoff=cutoff,
                            center_extent=args.center_extent,
                            weight_name=weight_name,
                            relative_tolerance=args.relative_tolerance,
                        )
                        rows.append(row)
                        print(
                            f"D={discriminant:>3} n={dimension:>2} sigma={sigma:g} "
                            f"cutoff={cutoff:>4} weight={weight_name:<12} "
                            f"lambda_min={row.lambda_min:.8g} rank={row.retained_rank}"
                        )

    write_rows(args.output, rows)
    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
