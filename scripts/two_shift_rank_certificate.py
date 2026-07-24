#!/usr/bin/env python3
"""Search for numerical witness pairs for two-shift generation.

This script constructs the paired Gaussian translation matrices T_s on an
N-point equally spaced symmetric grid, restricts them to reflection parity
sectors, and computes the rank of

    X -> ([X, T_s^+], [X, T_t^+])

and its odd-sector analogue.

A pair is a numerical witness when both sector ranks equal n_sector**2 - 1.
That is evidence for a rigorous certificate, not by itself a proof. The output
also reports the smallest nonzero singular value so promising pairs can be
passed to interval or exact-arithmetic certification.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import product
from math import exp

import numpy as np


@dataclass(frozen=True)
class SectorResult:
    dimension: int
    rank: int
    target_rank: int
    smallest_nonzero_singular_value: float
    nullity: int


def paired_gaussian_translation(
    n: int,
    shift: float,
    *,
    spacing: float = 1.0,
    sigma: float = 1.0,
) -> np.ndarray:
    """Return the symmetric Toeplitz paired-translation matrix T_shift.

    The irrelevant positive common normalization is retained. Entries depend
    only on k = |i-j| and are

        2 exp(-(shift^2 + (k h)^2)/(4 sigma^2))
          cosh(k h shift/(2 sigma^2)).

    Multiplying an entire generator by a nonzero scalar does not change its
    commutant, so this convention is sufficient for the rank problem.
    """
    if n < 1:
        raise ValueError("n must be positive")
    if spacing <= 0 or sigma <= 0:
        raise ValueError("spacing and sigma must be positive")

    idx = np.arange(n)
    k = np.abs(idx[:, None] - idx[None, :]).astype(float)
    kh = k * spacing
    scale = 2.0 * np.exp(-(shift * shift + kh * kh) / (4.0 * sigma * sigma))
    return scale * np.cosh(kh * shift / (2.0 * sigma * sigma))


def parity_bases(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Return orthonormal column bases for the +1 and -1 eigenspaces of J."""
    even: list[np.ndarray] = []
    odd: list[np.ndarray] = []
    used: set[int] = set()

    for i in range(n):
        if i in used:
            continue
        j = n - 1 - i
        used.add(i)
        used.add(j)
        if i == j:
            v = np.zeros(n)
            v[i] = 1.0
            even.append(v)
            continue
        e = np.zeros(n)
        o = np.zeros(n)
        e[i] = e[j] = 1.0 / np.sqrt(2.0)
        o[i] = 1.0 / np.sqrt(2.0)
        o[j] = -1.0 / np.sqrt(2.0)
        even.append(e)
        odd.append(o)

    q_plus = np.column_stack(even)
    q_minus = np.column_stack(odd) if odd else np.zeros((n, 0))
    return q_plus, q_minus


def restrict(matrix: np.ndarray, basis: np.ndarray) -> np.ndarray:
    return basis.T @ matrix @ basis


def commutator_map(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Matrix of X -> (XA-AX, XB-BX) under column vectorization."""
    if a.shape != b.shape or a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError("a and b must be square matrices of the same size")
    m = a.shape[0]
    identity = np.eye(m)
    # vec(XA-AX) = (A^T kron I - I kron A) vec(X)
    la = np.kron(a.T, identity) - np.kron(identity, a)
    lb = np.kron(b.T, identity) - np.kron(identity, b)
    return np.vstack((la, lb))


def rank_result(linear_map: np.ndarray, dimension: int, rtol: float) -> SectorResult:
    if dimension == 0:
        return SectorResult(0, 0, 0, float("inf"), 0)
    singular_values = np.linalg.svd(linear_map, compute_uv=False)
    scale = singular_values[0] if singular_values.size else 0.0
    threshold = rtol * max(linear_map.shape) * scale
    rank = int(np.count_nonzero(singular_values > threshold))
    nonzero = singular_values[singular_values > threshold]
    smallest = float(nonzero[-1]) if nonzero.size else 0.0
    target = dimension * dimension - 1
    return SectorResult(
        dimension=dimension,
        rank=rank,
        target_rank=target,
        smallest_nonzero_singular_value=smallest,
        nullity=dimension * dimension - rank,
    )


def evaluate_pair(
    n: int,
    s: float,
    t: float,
    *,
    spacing: float,
    sigma: float,
    rtol: float,
) -> tuple[SectorResult, SectorResult]:
    ts = paired_gaussian_translation(n, s, spacing=spacing, sigma=sigma)
    tt = paired_gaussian_translation(n, t, spacing=spacing, sigma=sigma)
    q_plus, q_minus = parity_bases(n)

    plus_map = commutator_map(restrict(ts, q_plus), restrict(tt, q_plus))
    plus = rank_result(plus_map, q_plus.shape[1], rtol)

    if q_minus.shape[1]:
        minus_map = commutator_map(restrict(ts, q_minus), restrict(tt, q_minus))
        minus = rank_result(minus_map, q_minus.shape[1], rtol)
    else:
        minus = SectorResult(0, 0, 0, float("inf"), 0)
    return plus, minus


def is_witness(results: tuple[SectorResult, SectorResult]) -> bool:
    return all(result.rank == result.target_rank for result in results)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--s-min", type=float, default=0.25)
    parser.add_argument("--s-max", type=float, default=3.0)
    parser.add_argument("--steps", type=int, default=24)
    parser.add_argument("--spacing", type=float, default=1.0)
    parser.add_argument("--sigma", type=float, default=1.0)
    parser.add_argument("--rtol", type=float, default=1e-12)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    shifts = np.linspace(args.s_min, args.s_max, args.steps)
    candidates: list[tuple[float, float, float, SectorResult, SectorResult]] = []

    for s, t in product(shifts, repeat=2):
        # T_{-s}=T_s, so equal absolute shifts are the same generator.
        if np.isclose(s * s, t * t, rtol=0.0, atol=1e-14):
            continue
        plus, minus = evaluate_pair(
            args.n,
            float(s),
            float(t),
            spacing=args.spacing,
            sigma=args.sigma,
            rtol=args.rtol,
        )
        if is_witness((plus, minus)):
            margin = min(
                plus.smallest_nonzero_singular_value,
                minus.smallest_nonzero_singular_value,
            )
            candidates.append((margin, float(s), float(t), plus, minus))

    candidates.sort(key=lambda item: item[0], reverse=True)
    if not candidates:
        raise SystemExit("No numerical witness found on this grid.")

    print(f"Found {len(candidates)} numerical witness pairs for N={args.n}.")
    print("Best candidates by smallest nonzero singular-value margin:")
    for margin, s, t, plus, minus in candidates[: args.top]:
        print(
            f"s={s:.16g}, t={t:.16g}, margin={margin:.6e}, "
            f"rank+={plus.rank}/{plus.target_rank}, "
            f"rank-={minus.rank}/{minus.target_rank}, "
            f"nullity+= {plus.nullity}, nullity-= {minus.nullity}"
        )


if __name__ == "__main__":
    main()
