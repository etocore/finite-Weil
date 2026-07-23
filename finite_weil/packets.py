"""Gaussian packet spaces used by the finite Weil model.

The normalization in this module is explicit and intentionally isolated. Future
imports from historical scripts must be reconciled against these definitions.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray


FloatMatrix = NDArray[np.float64]


@dataclass(frozen=True, slots=True)
class GaussianPacketFamily:
    """Translated unit-amplitude Gaussian packets.

    The packet centered at ``t_j`` is

        g_j(x) = exp(-(x - t_j)^2 / (2 sigma^2)).

    The Gram matrix is computed in the ordinary real ``L^2(R)`` inner product.
    """

    centers: NDArray[np.float64]
    sigma: float

    def __init__(self, centers: ArrayLike, sigma: float) -> None:
        centers_array = np.asarray(centers, dtype=float)
        if centers_array.ndim != 1:
            raise ValueError("centers must be one-dimensional")
        if centers_array.size == 0:
            raise ValueError("at least one center is required")
        if not np.all(np.isfinite(centers_array)):
            raise ValueError("centers must be finite")
        if sigma <= 0 or not np.isfinite(sigma):
            raise ValueError("sigma must be a finite positive number")
        if np.unique(centers_array).size != centers_array.size:
            raise ValueError("centers must be pairwise distinct")

        object.__setattr__(self, "centers", centers_array)
        object.__setattr__(self, "sigma", float(sigma))

    @property
    def dimension(self) -> int:
        return int(self.centers.size)

    def gram_matrix(self) -> FloatMatrix:
        """Return the exact analytic Gram matrix for the packet family."""

        delta = self.centers[:, None] - self.centers[None, :]
        prefactor = np.sqrt(np.pi) * self.sigma
        return prefactor * np.exp(-(delta**2) / (4.0 * self.sigma**2))

    def translated_correlation(self, shift: float) -> FloatMatrix:
        """Return ``<g_i, g_j(. - shift)>`` as an analytic matrix."""

        if not np.isfinite(shift):
            raise ValueError("shift must be finite")
        delta = self.centers[:, None] - self.centers[None, :] - shift
        prefactor = np.sqrt(np.pi) * self.sigma
        return prefactor * np.exp(-(delta**2) / (4.0 * self.sigma**2))

    def symmetric_translation_operator(self, shift: float) -> FloatMatrix:
        """Return the symmetric two-sided translation correlation matrix.

        This is ``-(C(shift) + C(-shift))``, matching the universal prime-power
        operator convention used in the current finite Weil reconstruction.
        """

        return -(
            self.translated_correlation(shift)
            + self.translated_correlation(-shift)
        )
