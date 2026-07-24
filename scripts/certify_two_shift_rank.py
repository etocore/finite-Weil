#!/usr/bin/env python3
"""Rigorous interval certificate for two-shift generation.

For fixed N, s, and t, this script builds the even and odd parity-sector
commutator maps and certifies maximal rank by enclosing a square maximal minor
with interval arithmetic. A sector is certified when the determinant interval
of the selected (m^2-1) x (m^2-1) minor excludes zero.

The implementation uses mpmath interval arithmetic. Numerical QR pivoting is
used only to *select* a candidate minor. The final determinant test is carried
out entirely with intervals, so the proof does not depend on floating-point
rank decisions.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from itertools import combinations
from pathlib import Path
from typing import Iterable

import mpmath as mp
import numpy as np

from two_shift_rank_certificate import (
    commutator_map,
    paired_gaussian_translation,
    parity_bases,
    restrict,
)


@dataclass(frozen=True)
class MinorCertificate:
    sector: str
    dimension: int
    target_rank: int
    row_indices: list[int]
    column_indices: list[int]
    determinant_lower: str
    determinant_upper: str
    excludes_zero: bool


@dataclass(frozen=True)
class PairCertificate:
    n: int
    s: str
    t: str
    spacing: str
    sigma: str
    precision_bits: int
    plus: MinorCertificate
    minus: MinorCertificate
    certified: bool


def _iv(x: float | str | mp.mpf) -> mp.iv.mpf:
    return mp.iv.mpf(str(x))


def paired_gaussian_translation_iv(
    n: int,
    shift: str,
    *,
    spacing: str,
    sigma: str,
) -> list[list[mp.iv.mpf]]:
    if n < 1:
        raise ValueError("n must be positive")

    sh = _iv(shift)
    h = _iv(spacing)
    sig = _iv(sigma)
    if float(spacing) <= 0 or float(sigma) <= 0:
        raise ValueError("spacing and sigma must be positive")

    four_sig2 = 4 * sig * sig
    two_sig2 = 2 * sig * sig
    out: list[list[mp.iv.mpf]] = []
    for i in range(n):
        row: list[mp.iv.mpf] = []
        for j in range(n):
            k = abs(i - j)
            kh = _iv(k) * h
            scale = 2 * mp.iv.exp(-(sh * sh + kh * kh) / four_sig2)
            row.append(scale * mp.iv.cosh(kh * sh / two_sig2))
        out.append(row)
    return out


def parity_bases_iv(n: int) -> tuple[list[list[mp.iv.mpf]], list[list[mp.iv.mpf]]]:
    q_plus, q_minus = parity_bases(n)
    return (
        [[_iv(value) for value in row] for row in q_plus.tolist()],
        [[_iv(value) for value in row] for row in q_minus.tolist()],
    )


def matmul_iv(
    a: list[list[mp.iv.mpf]], b: list[list[mp.iv.mpf]]
) -> list[list[mp.iv.mpf]]:
    if not a or not b:
        return []
    rows, inner, cols = len(a), len(a[0]), len(b[0])
    if len(b) != inner:
        raise ValueError("matrix shape mismatch")
    return [
        [sum((a[i][k] * b[k][j] for k in range(inner)), _iv(0)) for j in range(cols)]
        for i in range(rows)
    ]


def transpose_iv(a: list[list[mp.iv.mpf]]) -> list[list[mp.iv.mpf]]:
    return [list(row) for row in zip(*a)] if a else []


def restrict_iv(
    matrix: list[list[mp.iv.mpf]], basis: list[list[mp.iv.mpf]]
) -> list[list[mp.iv.mpf]]:
    return matmul_iv(matmul_iv(transpose_iv(basis), matrix), basis)


def commutator_map_iv(
    a: list[list[mp.iv.mpf]], b: list[list[mp.iv.mpf]]
) -> list[list[mp.iv.mpf]]:
    if len(a) != len(b):
        raise ValueError("sector dimensions differ")
    m = len(a)
    size = m * m
    out = [[_iv(0) for _ in range(size)] for _ in range(2 * size)]

    # Column-vectorization convention. Basis column q corresponds to E_{ij}
    # with q = i + j*m.
    for j in range(m):
        for i in range(m):
            q = i + j * m
            for col in range(m):
                for row in range(m):
                    p = row + col * m
                    value_a = _iv(0)
                    value_b = _iv(0)
                    if row == i:
                        value_a += a[j][col]
                        value_b += b[j][col]
                    if col == j:
                        value_a -= a[row][i]
                        value_b -= b[row][i]
                    out[p][q] = value_a
                    out[size + p][q] = value_b
    return out


def select_minor(linear_map: np.ndarray, target_rank: int) -> tuple[list[int], list[int]]:
    if target_rank == 0:
        return [], []

    # Greedy column selection by residual norm.
    selected_cols: list[int] = []
    q_basis = np.zeros((linear_map.shape[0], 0))
    remaining = list(range(linear_map.shape[1]))
    for _ in range(target_rank):
        best_col = None
        best_norm = -1.0
        best_residual = None
        for col in remaining:
            vec = linear_map[:, col]
            residual = vec - q_basis @ (q_basis.T @ vec) if q_basis.shape[1] else vec
            norm = float(np.linalg.norm(residual))
            if norm > best_norm:
                best_col = col
                best_norm = norm
                best_residual = residual
        if best_col is None or best_residual is None or best_norm <= 0:
            raise RuntimeError("failed to select independent columns")
        selected_cols.append(best_col)
        remaining.remove(best_col)
        unit = best_residual / best_norm
        q_basis = np.column_stack((q_basis, unit))

    sub = linear_map[:, selected_cols]
    selected_rows: list[int] = []
    q_rows = np.zeros((sub.shape[1], 0))
    remaining_rows = list(range(sub.shape[0]))
    for _ in range(target_rank):
        best_row = None
        best_norm = -1.0
        best_residual = None
        for row in remaining_rows:
            vec = sub[row, :]
            residual = vec - q_rows @ (q_rows.T @ vec) if q_rows.shape[1] else vec
            norm = float(np.linalg.norm(residual))
            if norm > best_norm:
                best_row = row
                best_norm = norm
                best_residual = residual
        if best_row is None or best_residual is None or best_norm <= 0:
            raise RuntimeError("failed to select independent rows")
        selected_rows.append(best_row)
        remaining_rows.remove(best_row)
        unit = best_residual / best_norm
        q_rows = np.column_stack((q_rows, unit))

    return selected_rows, selected_cols


def determinant_iv(matrix: list[list[mp.iv.mpf]]) -> mp.iv.mpf:
    n = len(matrix)
    if n == 0:
        return _iv(1)
    a = [row[:] for row in matrix]
    det = _iv(1)

    for col in range(n):
        pivot = None
        for row in range(col, n):
            interval = a[row][col]
            if not (interval.a <= 0 <= interval.b):
                pivot = row
                break
        if pivot is None:
            # Fall back to the narrowest interval with largest midpoint.
            candidates = range(col, n)
            pivot = max(candidates, key=lambda r: abs(float(mp.mid(a[r][col]))))
            if a[pivot][col].a <= 0 <= a[pivot][col].b:
                return mp.iv.mpf([-mp.inf, mp.inf])
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det

        pivot_value = a[col][col]
        det *= pivot_value
        for row in range(col + 1, n):
            factor = a[row][col] / pivot_value
            for k in range(col + 1, n):
                a[row][k] -= factor * a[col][k]
            a[row][col] = _iv(0)
    return det


def interval_bounds(value: mp.iv.mpf) -> tuple[str, str, bool]:
    lower = str(value.a)
    upper = str(value.b)
    excludes_zero = not (value.a <= 0 <= value.b)
    return lower, upper, excludes_zero


def certify_sector(
    sector: str,
    numeric_map: np.ndarray,
    interval_map: list[list[mp.iv.mpf]],
    dimension: int,
) -> MinorCertificate:
    target = dimension * dimension - 1
    if target == 0:
        return MinorCertificate(sector, dimension, 0, [], [], "1", "1", True)

    rows, cols = select_minor(numeric_map, target)
    minor = [[interval_map[i][j] for j in cols] for i in rows]
    det_interval = determinant_iv(minor)
    lower, upper, excludes_zero = interval_bounds(det_interval)
    return MinorCertificate(
        sector=sector,
        dimension=dimension,
        target_rank=target,
        row_indices=rows,
        column_indices=cols,
        determinant_lower=lower,
        determinant_upper=upper,
        excludes_zero=excludes_zero,
    )


def build_maps(
    n: int,
    s: str,
    t: str,
    *,
    spacing: str,
    sigma: str,
) -> tuple[tuple[np.ndarray, list[list[mp.iv.mpf]], int], tuple[np.ndarray, list[list[mp.iv.mpf]], int]]:
    sf, tf = float(s), float(t)
    hf, sigf = float(spacing), float(sigma)
    ts = paired_gaussian_translation(n, sf, spacing=hf, sigma=sigf)
    tt = paired_gaussian_translation(n, tf, spacing=hf, sigma=sigf)
    q_plus, q_minus = parity_bases(n)

    plus_numeric = commutator_map(restrict(ts, q_plus), restrict(tt, q_plus))
    minus_numeric = commutator_map(restrict(ts, q_minus), restrict(tt, q_minus)) if q_minus.shape[1] else np.zeros((0, 0))

    ts_iv = paired_gaussian_translation_iv(n, s, spacing=spacing, sigma=sigma)
    tt_iv = paired_gaussian_translation_iv(n, t, spacing=spacing, sigma=sigma)
    qp_iv, qm_iv = parity_bases_iv(n)
    plus_iv = commutator_map_iv(restrict_iv(ts_iv, qp_iv), restrict_iv(tt_iv, qp_iv))
    minus_iv = commutator_map_iv(restrict_iv(ts_iv, qm_iv), restrict_iv(tt_iv, qm_iv)) if qm_iv and len(qm_iv[0]) else []

    return (
        (plus_numeric, plus_iv, q_plus.shape[1]),
        (minus_numeric, minus_iv, q_minus.shape[1]),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--s", required=True)
    parser.add_argument("--t", required=True)
    parser.add_argument("--spacing", default="1")
    parser.add_argument("--sigma", default="1")
    parser.add_argument("--precision-bits", type=int, default=256)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if abs(float(args.s)) == abs(float(args.t)):
        raise SystemExit("s and t must satisfy s^2 != t^2")

    mp.iv.dps = max(30, int(args.precision_bits / 3.3219280948873626))
    plus_data, minus_data = build_maps(
        args.n,
        args.s,
        args.t,
        spacing=args.spacing,
        sigma=args.sigma,
    )
    plus = certify_sector("even", *plus_data)
    minus = certify_sector("odd", *minus_data)
    cert = PairCertificate(
        n=args.n,
        s=args.s,
        t=args.t,
        spacing=args.spacing,
        sigma=args.sigma,
        precision_bits=args.precision_bits,
        plus=plus,
        minus=minus,
        certified=plus.excludes_zero and minus.excludes_zero,
    )

    payload = json.dumps(asdict(cert), indent=2, sort_keys=True)
    print(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    if not cert.certified:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
