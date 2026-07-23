"""Plot smallest generalized eigenvalues from a convergence CSV file."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--discriminant", type=int, default=1)
    parser.add_argument("--sigma", type=float, default=0.5)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/convergence.png"),
    )
    args = parser.parse_args()

    grouped: dict[int, list[tuple[int, float]]] = defaultdict(list)
    for row in read_rows(args.csv_path):
        if int(row["discriminant"]) != args.discriminant:
            continue
        if float(row["sigma"]) != args.sigma:
            continue
        grouped[int(row["dimension"])].append(
            (int(row["cutoff"]), float(row["lambda_min"]))
        )

    if not grouped:
        raise ValueError("no rows matched the requested discriminant and sigma")

    for dimension, values in sorted(grouped.items()):
        values.sort()
        cutoffs = [value[0] for value in values]
        minima = [value[1] for value in values]
        plt.plot(cutoffs, minima, marker="o", label=f"dimension={dimension}")

    plt.xlabel("prime cutoff")
    plt.ylabel("smallest generalized eigenvalue")
    plt.title(f"Finite Weil refinement: D={args.discriminant}, sigma={args.sigma:g}")
    plt.legend()
    plt.grid(True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(args.output, dpi=180, bbox_inches="tight")
    print(f"wrote plot to {args.output}")


if __name__ == "__main__":
    main()
