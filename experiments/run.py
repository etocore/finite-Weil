"""Run a complete local convergence experiment and generate plots.

Usage:

    python -m experiments.run

The default profile is intentionally modest. Pass ``--profile full`` for the
larger sweep used by the GitHub Actions workflow.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from .convergence import parse_floats, parse_ints, run_case, write_rows
from .plot_convergence import plot_convergence

PROFILES = {
    "quick": {
        "discriminants": "1,-3,5,8,13",
        "dimensions": "4,8,16",
        "sigmas": "0.5,1.0",
        "cutoffs": "50,100,250",
    },
    "full": {
        "discriminants": "1,-3,5,8,13",
        "dimensions": "4,8,16,32",
        "sigmas": "0.25,0.5,1.0",
        "cutoffs": "50,100,250,500,1000",
    },
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=tuple(PROFILES), default="quick")
    parser.add_argument("--center-extent", type=float, default=6.0)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts"))
    args = parser.parse_args()

    config = PROFILES[args.profile]
    discriminants = parse_ints(config["discriminants"])
    dimensions = parse_ints(config["dimensions"])
    sigmas = parse_floats(config["sigmas"])
    cutoffs = parse_ints(config["cutoffs"])

    rows = []
    total = len(discriminants) * len(dimensions) * len(sigmas) * len(cutoffs)
    completed = 0
    for discriminant in discriminants:
        for dimension in dimensions:
            for sigma in sigmas:
                for cutoff in cutoffs:
                    row = run_case(
                        discriminant=discriminant,
                        dimension=dimension,
                        sigma=sigma,
                        cutoff=cutoff,
                        center_extent=args.center_extent,
                    )
                    rows.append(row)
                    completed += 1
                    print(
                        f"[{completed:>3}/{total}] D={discriminant:>3} "
                        f"n={dimension:>2} sigma={sigma:g} cutoff={cutoff:>4} "
                        f"lambda_min={row.lambda_min:.8g} "
                        f"cond(B)={row.gram_condition:.4g}"
                    )

    csv_path = args.output_dir / "convergence.csv"
    write_rows(csv_path, rows)

    for discriminant in discriminants:
        for sigma in sigmas:
            output = args.output_dir / (
                f"convergence-D{discriminant}-sigma{sigma:g}.png"
            )
            plot_convergence(csv_path, discriminant, sigma, output)

    print(f"wrote {len(rows)} rows to {csv_path}")
    print(f"wrote {len(discriminants) * len(sigmas)} plots to {args.output_dir}")


if __name__ == "__main__":
    main()
