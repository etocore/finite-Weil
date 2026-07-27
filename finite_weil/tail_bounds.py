"""Analytic prime-tail bounds for fixed Gaussian packet spaces.

For a Gaussian packet family with centers ``c_i`` and width ``sigma``, the
prime matrix entry at center difference ``delta = c_i - c_j`` is

    A_prime(N)_ij
        = - sum_{2 <= n <= N} beta_chi(n) sqrt(pi) sigma
          [ G(delta - log n) + G(delta + log n) ],

with ``G(x) = exp(-x^2 / 4 sigma^2)`` and ``|beta_chi(n)| <= log(n)/sqrt(n)``.

Because prime powers are integers and the summand is eventually decreasing,
the omitted tail is bounded by an integral that evaluates in closed form.
Substituting ``u = log x`` and completing the square,

    integral_N^inf (log x / sqrt x) exp(-(log x - delta)^2 / 4 sigma^2) dx
        = e^{delta/2 + sigma^2/4}
          [ mu sigma sqrt(pi) erfc((L - mu) / 2 sigma)
            + 2 sigma^2 e^{-(L - mu)^2 / 4 sigma^2} ],

with ``L = log N`` and ``mu = delta + sigma^2``.  The derivation and the
resulting truncation theorem are recorded in
``paper/14_certified_prime_tail.md``.

The bounds proved there are exact inequalities.  The functions below evaluate
those closed forms in floating point; they are not interval enclosures.
"""

from __future__ import annotations

from math import log

import numpy as np
from numpy.typing import NDArray
from scipy.special import erfc

from .packets import GaussianPacketFamily

FloatMatrix = NDArray[np.float64]


def _validate_cutoff(cutoff: int, largest_delta: float) -> float:
    if isinstance(cutoff, bool) or not isinstance(cutoff, int):
        raise TypeError("cutoff must be an integer")
    if cutoff < 2:
        raise ValueError("cutoff must be at least 2")
    log_cutoff = log(cutoff)
    if log_cutoff < max(2.0, largest_delta):
        raise ValueError(
            "certified bound requires log(cutoff) >= max(2, max |c_i - c_j|)"
        )
    return log_cutoff


def _one_sided_log_tail(
    delta: NDArray[np.float64] | float,
    sigma: float,
    log_cutoff: float,
) -> NDArray[np.float64]:
    """Return ``integral_L^inf u e^{u/2} exp(-(u - delta)^2 / 4 sigma^2) du``.

    The formula is exact; the integrand is positive, so the value is positive.
    """

    delta_array = np.asarray(delta, dtype=float)
    mu = delta_array + sigma**2
    gaussian = np.exp(-((log_cutoff - mu) ** 2) / (4.0 * sigma**2))
    complementary = erfc((log_cutoff - mu) / (2.0 * sigma))
    prefactor = np.exp(delta_array / 2.0 + sigma**2 / 4.0)
    return np.asarray(
        prefactor
        * (
            mu * sigma * np.sqrt(np.pi) * complementary
            + 2.0 * sigma**2 * gaussian
        ),
        dtype=float,
    )


def prime_tail_entry_bound(delta: float, sigma: float, cutoff: int) -> float:
    """Return the certified entrywise prime-tail bound at center difference ``delta``.

    The returned value bounds
    ``|A_prime(infinity) - A_prime(cutoff)|`` for the entry with center
    difference ``delta``, uniformly over primitive quadratic characters.
    """

    if not np.isfinite(delta):
        raise ValueError("delta must be finite")
    if sigma <= 0 or not np.isfinite(sigma):
        raise ValueError("sigma must be a finite positive number")
    magnitude = abs(float(delta))
    log_cutoff = _validate_cutoff(cutoff, magnitude)

    return float(
        np.sqrt(np.pi)
        * sigma
        * (
            _one_sided_log_tail(magnitude, sigma, log_cutoff)
            + _one_sided_log_tail(-magnitude, sigma, log_cutoff)
        )
    )


def prime_tail_bound_matrix(
    packets: GaussianPacketFamily,
    cutoff: int,
) -> FloatMatrix:
    """Return the symmetric matrix of certified entrywise tail bounds."""

    delta = packets.centers[:, None] - packets.centers[None, :]
    magnitude = np.abs(delta)
    log_cutoff = _validate_cutoff(cutoff, float(np.max(magnitude)))
    sigma = packets.sigma

    bound = np.sqrt(np.pi) * sigma * (
        _one_sided_log_tail(magnitude, sigma, log_cutoff)
        + _one_sided_log_tail(-magnitude, sigma, log_cutoff)
    )
    return np.asarray(bound, dtype=float)


def prime_tail_spectral_bound(
    packets: GaussianPacketFamily,
    cutoff: int,
) -> float:
    """Return a certified bound for ``||A_prime(inf) - A_prime(cutoff)||_2``.

    For a symmetric entrywise bound matrix ``E``, the spectral norm of any
    matrix dominated entrywise by ``E`` is at most the largest row sum of
    ``E``.
    """

    bound_matrix = prime_tail_bound_matrix(packets, cutoff)
    return float(np.max(np.sum(bound_matrix, axis=1)))


def prime_truncation_eigenvalue_bound(
    packets: GaussianPacketFamily,
    cutoff: int,
) -> float:
    """Return a bound for the generalized-eigenvalue shift from prime truncation.

    Every generalized eigenvalue of the pencil ``(A, B)`` moves by at most
    ``||T||_2 / lambda_min(B)`` under a symmetric perturbation ``T`` of ``A``.
    The Gram matrix eigenvalue is computed in floating point, so this value is
    a proved formula evaluated numerically, not an interval certificate.
    """

    spectral = prime_tail_spectral_bound(packets, cutoff)
    gram_minimum = float(np.linalg.eigvalsh(packets.gram_matrix())[0])
    if gram_minimum <= 0.0:
        raise ValueError("gram matrix must be numerically positive definite")
    return spectral / gram_minimum
