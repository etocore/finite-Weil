"""Finite pole matrix for the completed Riemann zeta function.

The completed function ``Lambda(s) = pi^(-s/2) Gamma(s/2) zeta(s)`` has simple
poles at ``s = 0`` and ``s = 1``.  Under the project's Fourier convention their
contribution to the Weil sesquilinear form is

    Q_pole(f, g) = conj(L_{-1/2}(f)) L_{1/2}(g) + conj(L_{1/2}(f)) L_{-1/2}(g),

where ``L_a(f) = integral_R f(x) exp(a x) dx`` is the bilateral Laplace
evaluation.  For the Gaussian packet family the evaluations are available in
closed form, and the packet-coordinate pole matrix is the rank-at-most-two
real symmetric matrix

    P_ij = 4 pi sigma^2 exp(sigma^2 / 4) cosh((c_i - c_j) / 2).

The derivation is recorded in ``paper/12_pole_term.md``.  The pole block
applies only to the principal character ``D = 1``; primitive non-principal
Dirichlet L-functions are entire and receive no pole contribution.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from .packets import GaussianPacketFamily

FloatArray = NDArray[np.float64]
FloatMatrix = NDArray[np.float64]


def pole_vectors(packets: GaussianPacketFamily) -> tuple[FloatArray, FloatArray]:
    """Return the closed-form Laplace vectors ``(p_minus, p_plus)``.

    The components are ``(p_-)_j = L_{-1/2}(g_j)`` and ``(p_+)_j = L_{1/2}(g_j)``
    with

        L_{+-1/2}(g_j) = sigma sqrt(2 pi) exp(sigma^2 / 8) exp(+-c_j / 2).
    """

    centers = np.asarray(packets.centers, dtype=float)
    sigma = float(packets.sigma)
    prefactor = sigma * np.sqrt(2.0 * np.pi) * np.exp(sigma**2 / 8.0)
    p_minus = np.asarray(prefactor * np.exp(-centers / 2.0), dtype=float)
    p_plus = np.asarray(prefactor * np.exp(centers / 2.0), dtype=float)
    return p_minus, p_plus


def pole_matrix(packets: GaussianPacketFamily) -> FloatMatrix:
    """Return the rank-at-most-two pole matrix ``p_- p_+^T + p_+ p_-^T``."""

    p_minus, p_plus = pole_vectors(packets)
    return np.asarray(
        np.outer(p_minus, p_plus) + np.outer(p_plus, p_minus),
        dtype=float,
    )
