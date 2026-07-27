"""Zero-side validation of the assembled matrices for quadratic characters.

For a real primitive character the root number is one, so the completed
function ``Lambda(1/2 + i t, chi)`` is real on the critical line and its
zeros there are sign changes.  ``L(s, chi)`` is evaluated exactly through the
Hurwitz-zeta representation

    L(s, chi) = q^{-s} sum_{a=1}^{q} chi(a) zeta(s, a/q),

so the reference zeros are computed independently of every matrix in this
repository.  The experiment then compares the assembled
conductor + gamma + prime (+ pole for D = 1) matrix entrywise against

    Z_ij = sum_{gamma > 0} 4 pi sigma^2 e^{-(sigma gamma)^2}
           cos(gamma (c_i - c_j)).

Requires ``mpmath`` (installed with the ``experiments`` extra).
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from math import pi
from pathlib import Path

import numpy as np

from finite_weil import (
    CompletedDirichletData,
    GaussianPacketFamily,
    PrimitiveQuadraticCharacter,
    WeilOperator,
    generalized_eigenvalues,
)


@dataclass(frozen=True, slots=True)
class ZeroSideRow:
    discriminant: int
    sigma: float
    dimension: int
    prime_cutoff: int
    zeros_used: int
    first_zero: float
    max_entry_error: float
    max_zero_side_entry: float
    lambda_min: float


def completed_lambda(t: float, character: PrimitiveQuadraticCharacter) -> float:
    """Return the real value of ``Lambda(1/2 + i t, chi)``."""

    import mpmath as mp

    q = character.conductor
    parity = character.parity
    s = mp.mpf("0.5") + 1j * mp.mpf(t)
    l_value = mp.power(q, -s) * mp.fsum(
        character(a) * mp.zeta(s, mp.mpf(a) / q)
        for a in range(1, q + 1)
        if character(a) != 0
    )
    prefactor = mp.power(mp.mpf(q) / mp.pi, (s + parity) / 2)
    return float((prefactor * mp.gamma((s + parity) / 2) * l_value).real)


def critical_zeros(
    character: PrimitiveQuadraticCharacter,
    t_max: float,
    *,
    scan_step: float = 0.02,
) -> list[float]:
    """Return ordinates of critical-line zeros found by sign scanning."""

    import mpmath as mp

    mp.mp.dps = 20
    grid = np.arange(scan_step, t_max + scan_step, scan_step)
    values = [completed_lambda(float(t), character) for t in grid]
    zeros: list[float] = []
    for i in range(len(grid) - 1):
        if values[i] == 0.0:
            zeros.append(float(grid[i]))
        elif values[i] * values[i + 1] < 0:
            root = mp.findroot(
                lambda t: completed_lambda(float(t), character),
                mp.mpf(float(grid[i] + grid[i + 1]) / 2),
                solver="secant",
            )
            zeros.append(float(root))
    return zeros


def run_case(
    discriminant: int,
    sigma: float,
    extent: float,
    dimension: int,
    cutoff: int,
    envelope_floor: float,
) -> ZeroSideRow:
    character = PrimitiveQuadraticCharacter(discriminant)
    centers = np.linspace(-extent, extent, dimension)
    packets = GaussianPacketFamily(centers, sigma)
    operator = WeilOperator(
        packets=packets,
        data=CompletedDirichletData(character),
        prime_cutoff=cutoff,
    )

    t_max = float(np.sqrt(-np.log(envelope_floor)) / sigma)
    gammas = critical_zeros(character, t_max)

    delta = centers[:, None] - centers[None, :]
    zero_side = np.zeros_like(delta)
    for gamma in gammas:
        zero_side += (
            4.0
            * pi
            * sigma**2
            * np.exp(-((sigma * gamma) ** 2))
            * np.cos(gamma * delta)
        )

    assembled = operator.matrix()
    spectrum = generalized_eigenvalues(
        assembled,
        packets.gram_matrix(),
        relative_tolerance=1e-12,
    )

    return ZeroSideRow(
        discriminant=discriminant,
        sigma=sigma,
        dimension=dimension,
        prime_cutoff=cutoff,
        zeros_used=len(gammas),
        first_zero=gammas[0] if gammas else float("nan"),
        max_entry_error=float(np.max(np.abs(assembled - zero_side))),
        max_zero_side_entry=float(np.max(np.abs(zero_side))),
        lambda_min=float(spectrum[0]),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discriminants", default="1,5,-3,8,13")
    parser.add_argument("--sigma", type=float, default=0.15)
    parser.add_argument("--extent", type=float, default=1.5)
    parser.add_argument("--dimension", type=int, default=7)
    parser.add_argument("--cutoff", type=int, default=2000)
    parser.add_argument("--envelope-floor", type=float, default=1e-14)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/dirichlet-zero-side.csv"),
    )
    args = parser.parse_args()

    rows: list[ZeroSideRow] = []
    for item in args.discriminants.split(","):
        discriminant = int(item.strip())
        row = run_case(
            discriminant=discriminant,
            sigma=args.sigma,
            extent=args.extent,
            dimension=args.dimension,
            cutoff=args.cutoff,
            envelope_floor=args.envelope_floor,
        )
        rows.append(row)
        print(
            f"D={row.discriminant:>3} zeros={row.zeros_used:>3} "
            f"first={row.first_zero:8.4f} max|A-Z|={row.max_entry_error:.3e} "
            f"max|Z|={row.max_zero_side_entry:.3e} lam_min={row.lambda_min:.3e}"
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(ZeroSideRow.__annotations__))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))
    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
