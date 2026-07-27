"""Small-bandwidth scaling study of the assembled completed-zeta operator.

Wide packets (sigma = 0.5 and above) see essentially no zero-side mass, so
positivity of the assembled operator is a statement about near-perfect
cancellation.  As sigma decreases, the packets resolve the low-lying zeros
and the generalized spectrum approaches the spectral content of the zero
measure inside the packet bandwidth.  In the small-sigma limit with spacing
proportional to sigma, the Gram matrix approaches a well-conditioned Toeplitz
matrix and Weil positivity on the packet family becomes classical
Bochner-Herglotz positive-definiteness of the sampled kernel.

For each sigma the prime cutoff is chosen with the proved tail bound of
``finite_weil.tail_bounds`` (evaluated in floating point) so that the
reported eigenvalues carry an explicit truncation-error budget.  When
``mpmath`` is installed, the assembled matrix is also compared entrywise
against the zero-side matrix built from actual zeta zeros.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from math import ceil, pi
from pathlib import Path

import numpy as np

from finite_weil import (
    CompletedDirichletData,
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    WeilOperator,
    generalized_eigenvalues,
    prime_truncation_eigenvalue_bound,
)


@dataclass(frozen=True, slots=True)
class SigmaScalingRow:
    sigma: float
    extent: float
    dimension: int
    prime_cutoff: int
    truncation_bound: float
    gram_condition: float
    retained_rank: int
    lambda_min: float
    lambda_max: float
    zeros_used: int
    zero_side_max_error: float
    zero_side_lambda_min: float


def packet_family(extent: float, sigma: float, spacing_ratio: float) -> GaussianPacketFamily:
    spacing = spacing_ratio * sigma
    half_steps = max(1, ceil(extent / spacing))
    centers = np.linspace(-extent, extent, 2 * half_steps + 1)
    return GaussianPacketFamily(centers, sigma)


def tail_resolved_cutoff(
    packets: GaussianPacketFamily,
    tolerance: float,
    *,
    maximum: int = 4_000_000,
) -> tuple[int, float]:
    """Return the smallest doubling cutoff whose eigenvalue-shift bound passes.

    Raises instead of silently returning an unresolved cutoff, so sweep rows
    can never carry a truncation budget larger than requested.
    """

    extent = float(np.max(np.abs(packets.centers)))
    cutoff = max(16, int(np.exp(max(2.0, 2.0 * extent))) + 1)
    while True:
        bound = prime_truncation_eigenvalue_bound(packets, cutoff)
        if bound <= tolerance:
            return cutoff, bound
        if cutoff >= maximum:
            raise RuntimeError(
                f"failed to reach truncation tolerance {tolerance:g} by cutoff "
                f"{maximum}; final bound was {bound:g}"
            )
        cutoff = min(2 * cutoff, maximum)


def zeta_zeros_for_envelope(sigma: float, floor: float) -> list[float]:
    """Return zeta-zero ordinates until the Gaussian envelope drops below ``floor``."""

    try:
        import mpmath
    except ImportError:
        return []

    mpmath.mp.dps = 20
    zeros: list[float] = []
    index = 1
    while True:
        gamma = float(mpmath.im(mpmath.zetazero(index)))
        if np.exp(-((sigma * gamma) ** 2)) < floor:
            return zeros
        zeros.append(gamma)
        index += 1


def run_case(
    sigma: float,
    extent: float,
    spacing_ratio: float,
    truncation_tolerance: float,
    relative_tolerance: float,
    envelope_floor: float,
) -> SigmaScalingRow:
    packets = packet_family(extent, sigma, spacing_ratio)
    cutoff, bound = tail_resolved_cutoff(packets, truncation_tolerance)
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(1))
    operator = WeilOperator(
        packets=packets,
        data=data,
        prime_cutoff=cutoff,
        include_pole=True,
    )

    gram = packets.gram_matrix()
    matrix = operator.matrix()
    spectrum = generalized_eigenvalues(
        matrix,
        gram,
        relative_tolerance=relative_tolerance,
    )
    gram_values = np.linalg.eigvalsh(gram)
    retained = int(
        np.count_nonzero(gram_values > relative_tolerance * gram_values[-1])
    )

    zeros = zeta_zeros_for_envelope(sigma, envelope_floor)
    if zeros:
        delta = packets.centers[:, None] - packets.centers[None, :]
        zero_side = np.zeros_like(delta)
        for gamma in zeros:
            zero_side += (
                4.0
                * pi
                * sigma**2
                * np.exp(-((sigma * gamma) ** 2))
                * np.cos(gamma * delta)
            )
        zero_error = float(np.max(np.abs(matrix - zero_side)))
        zero_lambda_min = float(
            generalized_eigenvalues(
                zero_side,
                gram,
                relative_tolerance=relative_tolerance,
            )[0]
        )
    else:
        zero_error = float("nan")
        zero_lambda_min = float("nan")

    return SigmaScalingRow(
        sigma=sigma,
        extent=extent,
        dimension=packets.dimension,
        prime_cutoff=cutoff,
        truncation_bound=bound,
        gram_condition=float(np.linalg.cond(gram)),
        retained_rank=retained,
        lambda_min=float(spectrum[0]),
        lambda_max=float(spectrum[-1]),
        zeros_used=len(zeros),
        zero_side_max_error=zero_error,
        zero_side_lambda_min=zero_lambda_min,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sigmas", default="0.5,0.35,0.25,0.18,0.12")
    parser.add_argument("--extent", type=float, default=1.5)
    parser.add_argument("--spacing-ratio", type=float, default=1.5)
    parser.add_argument("--truncation-tolerance", type=float, default=1e-8)
    parser.add_argument("--relative-tolerance", type=float, default=1e-12)
    parser.add_argument("--envelope-floor", type=float, default=1e-15)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/sigma-scaling.csv"),
    )
    args = parser.parse_args()

    rows: list[SigmaScalingRow] = []
    for item in args.sigmas.split(","):
        sigma = float(item.strip())
        row = run_case(
            sigma=sigma,
            extent=args.extent,
            spacing_ratio=args.spacing_ratio,
            truncation_tolerance=args.truncation_tolerance,
            relative_tolerance=args.relative_tolerance,
            envelope_floor=args.envelope_floor,
        )
        rows.append(row)
        print(
            f"sigma={row.sigma:g} m={row.dimension:>2} N={row.prime_cutoff:>8} "
            f"bound={row.truncation_bound:.2e} lam_min={row.lambda_min:.6e} "
            f"lam_max={row.lambda_max:.6e} zeros={row.zeros_used} "
            f"zero_err={row.zero_side_max_error:.2e}"
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(SigmaScalingRow.__annotations__),
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))
    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
