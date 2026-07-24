"""Assembly and spectral analysis of truncated finite Weil operators.

The coordinate matrix is assembled from the three contributions currently fixed
by the project:

    A = A_conductor + A_gamma + A_prime(cutoff).

Gaussian packets are not orthonormal, so spectral quantities are computed from
the generalized problem ``A v = lambda B v`` with packet Gram matrix ``B``.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from .completed import CompletedDirichletData, conductor_matrix
from .explicit_formula import PrimeWeight, assemble_prime_operator, sharp_prime_weight
from .gamma import gamma_matrix
from .operators import (
    GeneralizedEigenpair,
    generalized_eigenvalues,
    gram_operator_norm,
    smallest_generalized_eigenpair,
)
from .packets import GaussianPacketFamily

FloatArray = NDArray[np.float64]
FloatMatrix = NDArray[np.float64]


@dataclass(frozen=True, slots=True)
class WeilOperator:
    """Truncated finite Weil operator for a primitive quadratic character."""

    packets: GaussianPacketFamily
    data: CompletedDirichletData
    prime_cutoff: int
    prime_weight: PrimeWeight = sharp_prime_weight
    prime_support_multiplier: float = 1.0

    def __post_init__(self) -> None:
        if isinstance(self.prime_cutoff, bool) or not isinstance(self.prime_cutoff, int):
            raise TypeError("prime_cutoff must be an integer")
        if self.prime_cutoff < 2:
            raise ValueError("prime_cutoff must be at least 2")
        if (
            self.prime_support_multiplier <= 0
            or not np.isfinite(self.prime_support_multiplier)
        ):
            raise ValueError(
                "prime_support_multiplier must be a finite positive number"
            )

    def gram_matrix(self) -> FloatMatrix:
        """Return the packet Gram matrix ``B``."""

        return self.packets.gram_matrix()

    def conductor_matrix(self) -> FloatMatrix:
        """Return the exact conductor contribution."""

        return conductor_matrix(self.packets, self.data)

    def gamma_matrix(
        self,
        *,
        epsabs: float = 1e-11,
        epsrel: float = 1e-11,
    ) -> FloatMatrix:
        """Return the Archimedean gamma-factor contribution."""

        return gamma_matrix(
            self.packets,
            self.data,
            epsabs=epsabs,
            epsrel=epsrel,
        )

    def prime_matrix(self) -> FloatMatrix:
        """Return the weighted prime-power contribution."""

        return assemble_prime_operator(
            self.packets,
            self.data.character,
            self.prime_cutoff,
            weight=self.prime_weight,
            support_multiplier=self.prime_support_multiplier,
        )

    def archimedean_matrix(
        self,
        *,
        epsabs: float = 1e-11,
        epsrel: float = 1e-11,
    ) -> FloatMatrix:
        """Return conductor plus gamma contributions."""

        return self.conductor_matrix() + self.gamma_matrix(
            epsabs=epsabs,
            epsrel=epsrel,
        )

    def matrix(
        self,
        *,
        epsabs: float = 1e-11,
        epsrel: float = 1e-11,
    ) -> FloatMatrix:
        """Return the complete truncated coordinate matrix."""

        matrix = self.archimedean_matrix(epsabs=epsabs, epsrel=epsrel)
        matrix += self.prime_matrix()
        return np.asarray(matrix, dtype=float)

    def generalized_eigenvalues(
        self,
        *,
        epsabs: float = 1e-11,
        epsrel: float = 1e-11,
        relative_tolerance: float | None = None,
    ) -> FloatArray:
        """Return ordered intrinsic eigenvalues from ``A v = lambda B v``."""

        return generalized_eigenvalues(
            self.matrix(epsabs=epsabs, epsrel=epsrel),
            self.gram_matrix(),
            relative_tolerance=relative_tolerance,
        )

    def smallest_generalized_eigenpair(
        self,
        *,
        epsabs: float = 1e-11,
        epsrel: float = 1e-11,
        relative_tolerance: float | None = None,
    ) -> GeneralizedEigenpair:
        """Return the minimizing eigenvalue and reconstructed packet coefficients."""

        return smallest_generalized_eigenpair(
            self.matrix(epsabs=epsabs, epsrel=epsrel),
            self.gram_matrix(),
            relative_tolerance=relative_tolerance,
        )

    def smallest_generalized_eigenvalue(
        self,
        *,
        epsabs: float = 1e-11,
        epsrel: float = 1e-11,
        relative_tolerance: float | None = None,
    ) -> float:
        """Return the smallest generalized eigenvalue."""

        return self.smallest_generalized_eigenpair(
            epsabs=epsabs,
            epsrel=epsrel,
            relative_tolerance=relative_tolerance,
        ).eigenvalue

    def operator_norm(
        self,
        *,
        epsabs: float = 1e-11,
        epsrel: float = 1e-11,
        relative_tolerance: float | None = None,
    ) -> float:
        """Return the Gram-induced norm of the truncated operator."""

        return gram_operator_norm(
            self.matrix(epsabs=epsabs, epsrel=epsrel),
            self.gram_matrix(),
            relative_tolerance=relative_tolerance,
        )
