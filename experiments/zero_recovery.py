"""Recover low-lying zeta zeros from the prime-side Weil kernel.

Paper 13 validated the identity

    K(delta) = sum_{gamma > 0} 4 pi sigma^2 e^{-sigma^2 gamma^2} cos(gamma delta)

for the translation-invariant kernel of the assembled completed-zeta model
(conductor + gamma + pole + prime sum).  The right-hand side is a finite sum
of damped cosines up to the envelope floor, so the frequencies ``gamma`` are
recoverable from uniform samples of the *prime-side* kernel by the matrix
pencil (ESPRIT) method, with no zero data used.

This experiment quantifies how many zeros are identifiable as a function of
the packet bandwidth ``sigma``.  It is a numerical study of the inverse
problem posed in ``paper/03_spectral_program.md`` section 13.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from math import log, pi, sqrt
from pathlib import Path

import numpy as np

from finite_weil.explicit_formula import prime_power_values
from finite_weil.gamma import gamma_kernel
from finite_weil.tail_bounds import prime_tail_entry_bound

# Reference values for reporting only; the recovery itself never uses them.
ZETA_ZEROS = (
    14.134725141734695,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739190,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167159,
    49.773832477672302,
)


@dataclass(frozen=True, slots=True)
class RecoveryRow:
    sigma: float
    step: float
    samples: int
    prime_cutoff: int
    model_order: int
    recovered: tuple[float, ...]
    amplitude_ratios: tuple[float, ...]


def prime_side_kernel_samples(
    sigma: float,
    step: float,
    count: int,
    prime_cutoff: int,
) -> np.ndarray:
    """Return ``K(m * step)`` for the assembled completed-zeta kernel.

    The kernel is built from the conductor, gamma, pole, and truncated prime
    contributions only.  No information about zeta zeros enters.
    """

    if sigma <= 0 or not np.isfinite(sigma):
        raise ValueError("sigma must be a finite positive number")
    if step <= 0 or not np.isfinite(step):
        raise ValueError("step must be a finite positive number")
    if count < 4:
        raise ValueError("count must be at least 4")

    deltas = step * np.arange(count)
    kernel = -log(pi) * sqrt(pi) * sigma * np.exp(
        -(deltas**2) / (4.0 * sigma**2)
    )
    kernel += 4.0 * pi * sigma**2 * np.exp(sigma**2 / 4.0) * np.cosh(deltas / 2.0)
    kernel += np.array([gamma_kernel(float(d), sigma, 0) for d in deltas])

    prefactor = sqrt(pi) * sigma
    for n, p in prime_power_values(prime_cutoff):
        beta = log(p) / sqrt(n)
        log_n = log(n)
        kernel -= beta * prefactor * (
            np.exp(-((deltas - log_n) ** 2) / (4.0 * sigma**2))
            + np.exp(-((deltas + log_n) ** 2) / (4.0 * sigma**2))
        )
    return kernel


def matrix_pencil_frequencies(
    samples: np.ndarray,
    step: float,
    *,
    model_order: int | None = None,
    singular_value_tolerance: float = 1e-8,
) -> tuple[np.ndarray, int]:
    """Return recovered positive frequencies and the model order used.

    The samples are assumed to follow ``y_m = sum_j a_j cos(omega_j step m)``
    up to a small error.  The estimator is the standard matrix-pencil method:
    SVD-truncate the Hankel matrix of the samples, then read the frequencies
    from the eigenvalues of the shifted pencil in the signal subspace.
    """

    y = np.asarray(samples, dtype=float)
    if y.ndim != 1 or y.size < 8:
        raise ValueError("samples must be a one-dimensional array of length >= 8")
    if step <= 0 or not np.isfinite(step):
        raise ValueError("step must be a finite positive number")

    columns = y.size // 2
    rows = y.size - columns
    row_index = np.arange(rows)[:, None]
    column_index = np.arange(columns)[None, :]
    hankel_zero = y[row_index + column_index]
    hankel_one = y[row_index + column_index + 1]

    left, singular, right_h = np.linalg.svd(hankel_zero, full_matrices=False)
    if model_order is None:
        significant = int(
            np.count_nonzero(singular > singular_value_tolerance * singular[0])
        )
        model_order = max(1, significant // 2)
    rank = 2 * model_order
    rank = min(rank, singular.size)

    reduced = (
        left[:, :rank].T @ hankel_one @ right_h[:rank].T
    ) / singular[:rank][None, :]
    eigenvalues = np.linalg.eigvals(reduced)
    frequencies = np.angle(eigenvalues) / step
    positive = np.sort(frequencies[frequencies > 0.0])
    return positive, model_order


def envelope_amplitude_ratios(
    frequencies: np.ndarray,
    samples: np.ndarray,
    step: float,
    sigma: float,
) -> np.ndarray:
    """Return fitted amplitudes divided by the predicted zero-side envelope.

    A genuine simple zero at ``gamma`` must appear with amplitude
    ``4 pi sigma^2 exp(-(sigma gamma)^2)``, so its ratio is close to one,
    while spurious pencil frequencies fit truncation error and produce
    ratios far from one.
    """

    deltas = step * np.arange(samples.size)
    design = np.cos(np.outer(deltas, frequencies))
    fitted, *_ = np.linalg.lstsq(design, samples, rcond=None)
    predicted = 4.0 * pi * sigma**2 * np.exp(-((sigma * frequencies) ** 2))
    return np.asarray(fitted / predicted, dtype=float)


def run_case(
    sigma: float,
    envelope_floor: float,
    delta_max: float,
    *,
    ratio_window: tuple[float, float] = (0.5, 2.0),
) -> RecoveryRow:
    """Choose sampling from ``sigma`` and run one recovery."""

    gamma_ceiling = sqrt(max(1.0, -np.log(envelope_floor))) / sigma
    step = 0.9 * pi / gamma_ceiling
    count = int(np.ceil(delta_max / step))

    # Deepen the prime cutoff until the certified entrywise tail bound at the
    # farthest sample is below the smallest amplitude the sweep tries to see.
    amplitude_floor = envelope_floor * 4.0 * pi * sigma**2
    cutoff = max(2, int(np.ceil(np.exp(max(2.0, delta_max)))))
    while prime_tail_entry_bound(delta_max, sigma, cutoff) > amplitude_floor:
        cutoff *= 2

    samples = prime_side_kernel_samples(sigma, step, count, cutoff)
    frequencies, order = matrix_pencil_frequencies(samples, step)
    ratios = envelope_amplitude_ratios(frequencies, samples, step, sigma)
    keep = (ratios > ratio_window[0]) & (ratios < ratio_window[1])
    return RecoveryRow(
        sigma=sigma,
        step=step,
        samples=count,
        prime_cutoff=cutoff,
        model_order=order,
        recovered=tuple(float(f) for f in frequencies[keep]),
        amplitude_ratios=tuple(float(r) for r in ratios[keep]),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sigmas", default="0.2,0.15,0.1,0.07")
    parser.add_argument("--envelope-floor", type=float, default=1e-9)
    parser.add_argument("--delta-max", type=float, default=10.0)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/zero-recovery.csv"),
    )
    args = parser.parse_args()

    rows: list[RecoveryRow] = []
    for item in args.sigmas.split(","):
        sigma = float(item.strip())
        row = run_case(sigma, args.envelope_floor, args.delta_max)
        rows.append(row)
        recovered = ", ".join(
            f"{f:.4f} (x{r:.2f})"
            for f, r in zip(row.recovered, row.amplitude_ratios)
        )
        print(
            f"sigma={row.sigma:g} order={row.model_order} cutoff={row.prime_cutoff} "
            f"recovered=[{recovered}]"
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "sigma",
                "step",
                "samples",
                "prime_cutoff",
                "model_order",
                "recovered",
                "amplitude_ratios",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row.sigma,
                    row.step,
                    row.samples,
                    row.prime_cutoff,
                    row.model_order,
                    ";".join(f"{f:.10f}" for f in row.recovered),
                    ";".join(f"{r:.6f}" for r in row.amplitude_ratios),
                ]
            )
    print(f"wrote {len(rows)} rows to {args.output}")
    print("reference zeta zeros:", ", ".join(f"{g:.4f}" for g in ZETA_ZEROS))


if __name__ == "__main__":
    main()
