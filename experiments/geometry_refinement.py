"""Study packet-geometry refinement and reconstruct minimizing functions.

The experiment varies packet extent and spacing while choosing a prime cutoff from
the translation geometry. For every finite model it records the smallest whitened
eigenpair, residual norm, retained Gram rank, and the fraction of reconstructed
L2 mass near the packet-space boundary.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from math import ceil, exp
from pathlib import Path

import numpy as np
from scipy.integrate import trapezoid

from experiments.convergence import parse_floats
from finite_weil import (
    CompletedDirichletData,
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    WeilOperator,
)


@dataclass(frozen=True, slots=True)
class GeometryRow:
    discriminant: int
    extent: float
    spacing: float
    sigma: float
    dimension: int
    prime_cutoff: int
    lambda_min: float
    residual_norm: float
    gram_condition: float
    retained_rank: int
    boundary_mass: float
    peak_location: float


def packet_centers_from_spacing(extent: float, spacing: float) -> np.ndarray:
    """Return a symmetric grid whose realized spacing does not exceed the target."""

    if extent <= 0 or not np.isfinite(extent):
        raise ValueError("extent must be a finite positive number")
    if spacing <= 0 or not np.isfinite(spacing):
        raise ValueError("spacing must be a finite positive number")
    half_steps = max(1, int(ceil(extent / spacing)))
    return np.linspace(-extent, extent, 2 * half_steps + 1, dtype=float)


def geometry_prime_cutoff(
    extent: float,
    sigma: float,
    *,
    tail_sigmas: float = 4.0,
    minimum: int = 1000,
) -> int:
    """Choose ``N`` so ``log(N)`` exceeds packet separation plus a Gaussian tail."""

    if tail_sigmas <= 0 or not np.isfinite(tail_sigmas):
        raise ValueError("tail_sigmas must be a finite positive number")
    log_cutoff = 2.0 * extent + tail_sigmas * sigma
    return max(minimum, int(ceil(exp(log_cutoff))))


def boundary_mass_fraction(
    packets: GaussianPacketFamily,
    coefficients: np.ndarray,
    extent: float,
    *,
    boundary_fraction: float = 0.8,
    grid_points: int = 4001,
) -> tuple[float, float]:
    """Return reconstructed boundary mass and absolute-peak location."""

    if not 0 < boundary_fraction < 1:
        raise ValueError("boundary_fraction must lie between zero and one")
    padding = 5.0 * packets.sigma
    grid = np.linspace(-extent - padding, extent + padding, grid_points)
    values = packets.linear_combination(coefficients, grid)
    density = values**2
    total = float(trapezoid(density, grid))
    boundary = np.abs(grid) >= boundary_fraction * extent
    boundary_mass = float(trapezoid(density * boundary, grid) / total)
    peak_location = float(grid[int(np.argmax(np.abs(values)))])
    return boundary_mass, peak_location


def run_case(
    discriminant: int,
    extent: float,
    spacing: float,
    sigma_ratio: float,
    relative_tolerance: float,
    tail_sigmas: float,
) -> GeometryRow:
    """Run one geometry-aware minimizer reconstruction."""

    centers = packet_centers_from_spacing(extent, spacing)
    realized_spacing = float(centers[1] - centers[0])
    sigma = sigma_ratio * realized_spacing
    packets = GaussianPacketFamily(centers, sigma)
    cutoff = geometry_prime_cutoff(extent, sigma, tail_sigmas=tail_sigmas)
    character = PrimitiveQuadraticCharacter(discriminant)
    operator = WeilOperator(
        packets=packets,
        data=CompletedDirichletData(character),
        prime_cutoff=cutoff,
    )

    gram = operator.gram_matrix()
    pair = operator.smallest_generalized_eigenpair(
        relative_tolerance=relative_tolerance,
    )
    boundary_mass, peak_location = boundary_mass_fraction(
        packets,
        pair.coefficients,
        extent,
    )

    return GeometryRow(
        discriminant=discriminant,
        extent=extent,
        spacing=realized_spacing,
        sigma=sigma,
        dimension=packets.dimension,
        prime_cutoff=cutoff,
        lambda_min=pair.eigenvalue,
        residual_norm=pair.residual_norm,
        gram_condition=float(np.linalg.cond(gram)),
        retained_rank=pair.retained_rank,
        boundary_mass=boundary_mass,
        peak_location=peak_location,
    )


def write_rows(path: Path, rows: list[GeometryRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(GeometryRow.__annotations__))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discriminant", type=int, default=1)
    parser.add_argument("--extents", default="2,3,4")
    parser.add_argument("--spacings", default="1,0.75,0.5")
    parser.add_argument("--sigma-ratio", type=float, default=0.75)
    parser.add_argument("--relative-tolerance", type=float, default=1e-12)
    parser.add_argument("--tail-sigmas", type=float, default=4.0)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/geometry-refinement.csv"),
    )
    args = parser.parse_args()

    rows: list[GeometryRow] = []
    for extent in parse_floats(args.extents):
        for spacing in parse_floats(args.spacings):
            row = run_case(
                discriminant=args.discriminant,
                extent=extent,
                spacing=spacing,
                sigma_ratio=args.sigma_ratio,
                relative_tolerance=args.relative_tolerance,
                tail_sigmas=args.tail_sigmas,
            )
            rows.append(row)
            print(
                f"L={row.extent:g} h={row.spacing:.5g} m={row.dimension:>2} "
                f"N={row.prime_cutoff:>7} lambda={row.lambda_min:.10g} "
                f"boundary={row.boundary_mass:.5g} residual={row.residual_norm:.3g}"
            )

    write_rows(args.output, rows)
    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
