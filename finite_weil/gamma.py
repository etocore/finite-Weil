"""Archimedean gamma-factor contribution to the finite Weil form.

For parity ``a`` in ``{0, 1}``, the symmetric explicit formula contributes the
real Fourier multiplier

    w_a(t) = Re psi((a + 1/2 + i t) / 2),

where ``psi`` is the digamma function.  For the Gaussian packet family used by
this project, the matrix entries reduce to a one-dimensional even quadrature.
"""

from __future__ import annotations

from math import cos, exp

import numpy as np
from numpy.typing import NDArray
from scipy.integrate import quad
from scipy.special import digamma

from .completed import CompletedDirichletData
from .packets import GaussianPacketFamily

FloatMatrix = NDArray[np.float64]


def gamma_weight(t: float, parity: int) -> float:
    """Return the symmetric gamma multiplier at frequency ``t``.

    The multiplier is

        Re psi((parity + 1/2 + i t) / 2).
    """

    if parity not in (0, 1):
        raise ValueError("parity must be 0 or 1")
    if not np.isfinite(t):
        raise ValueError("t must be finite")

    argument = (parity + 0.5 + 1j * float(t)) / 2.0
    return float(np.real(digamma(argument)))


def gamma_kernel(
    delta: float,
    sigma: float,
    parity: int,
    *,
    epsabs: float = 1e-11,
    epsrel: float = 1e-11,
) -> float:
    """Return the Gaussian-packet gamma kernel at center difference ``delta``.

    With the Fourier convention fixed by the project,

        K(delta) = 2 sigma^2 integral_0^infinity
            w_a(t) exp(-(sigma t)^2) cos(delta t) dt.
    """

    if not np.isfinite(delta):
        raise ValueError("delta must be finite")
    if sigma <= 0 or not np.isfinite(sigma):
        raise ValueError("sigma must be a finite positive number")
    if parity not in (0, 1):
        raise ValueError("parity must be 0 or 1")
    if epsabs <= 0 or not np.isfinite(epsabs):
        raise ValueError("epsabs must be a finite positive number")
    if epsrel <= 0 or not np.isfinite(epsrel):
        raise ValueError("epsrel must be a finite positive number")

    sigma_squared = sigma**2

    def integrand(t: float) -> float:
        return (
            2.0
            * sigma_squared
            * gamma_weight(t, parity)
            * exp(-(sigma * t) ** 2)
            * cos(delta * t)
        )

    value, _ = quad(
        integrand,
        0.0,
        np.inf,
        epsabs=epsabs,
        epsrel=epsrel,
        limit=200,
    )
    return float(value)


def gamma_matrix(
    packets: GaussianPacketFamily,
    data: CompletedDirichletData,
    *,
    epsabs: float = 1e-11,
    epsrel: float = 1e-11,
) -> FloatMatrix:
    """Return the real symmetric gamma-factor matrix for ``packets``."""

    dimension = packets.dimension
    matrix = np.empty((dimension, dimension), dtype=float)

    for i, left_center in enumerate(packets.centers):
        for j in range(i, dimension):
            delta = float(packets.centers[j] - left_center)
            value = gamma_kernel(
                delta,
                packets.sigma,
                data.parity,
                epsabs=epsabs,
                epsrel=epsrel,
            )
            matrix[i, j] = value
            matrix[j, i] = value

    return matrix
