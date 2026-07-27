"""Assembly and spectral analysis of truncated finite Weil operators.

For an entire completed primitive quadratic L-function, the coordinate matrix is
assembled as

    A = A_conductor + A_gamma + A_prime(cutoff).

For the completed zeta function (the principal character ``D = 1``), the
meromorphic completion also contributes the rank-two pole block

    A = A_conductor + A_gamma + A_prime(cutoff) + A_pole.

``WeilOperator`` includes that pole block automatically for ``D = 1`` unless a
historical pole-free computation is explicitly requested. Gaussian packets are
not orthonormal, so spectral quantities are computed from the generalized
problem ``A v = lambda B v`` with packet Gram matrix ``B``.
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
from .poles import pole_matrix

FloatArray = NDArray[np.float64]
FloatMatrix = NDArray[np.float64]


@dataclass(frozen=True, slots=True)
class WeilOperator:
    """Truncated finite Weil operator for a primitive quadratic character.

    ``include_pole`` controls the completed-zeta pole matrix derived in
    ``paper/12_pole_term.md``. The default ``None`` resolves automatically:
    the pole block is included exactly for the principal character ``D = 1``,
    whose completed function is meromorphic, and omitted for non-principal
    primitive quadratic L-functions, whose completions are entire. Pass
    ``False`` only to reproduce explicitly labeled historical pole-free
    assemblies. Passing ``True`` for a non-principal character is rejected.
    """

    packets: GaussianPacketFamily
    data: CompletedDirichletData
    prime_cutoff: int
    prime_weight: PrimeWeight = sharp_prime_weight
    prime_support_multiplier: float = 1.0
    include_pole: bool | None = None

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
        if self.include_pole is not None and not isinstance(self.include_pole, bool):
            raise TypeError("include_pole must be a boolean or None")
        if self.include_pole is True and self.data.conductor != 1:
            raise ValueError(
                "the pole matrix applies only to the principal character D = 1"
            )

    @property
    def pole_included(self) -> bool:
        """Return whether the assembled matrix contains the pole block."""

        if self.include_pole is None:
            return self.data.conductor == 1
        return self.include_pole

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

    def pole_matrix(self) -> FloatMatrix:
        """Return the pole contribution, or a zero matrix when not included."""

        if not self.pole_included:
            dimension = self.packets.dimension
            return np.zeros((dimension, dimension), dtype=float)
        return pole_matrix(self.packets)

    def archimedean_matrix(
        self,
        *,
        epsabs: float = 1e-11,
        epsrel: float = 1e-11,
    ) -> FloatMatrix:
        """Return conductor plus gamma contributions.

        The completed-zeta pole block is not part of this method; it is added by
        :meth:`matrix` when ``pole_included`` is true.
        """

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
        if self.pole_included:
            matrix += self.pole_matrix()
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
