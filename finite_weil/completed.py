"""Completed primitive Dirichlet L-function normalization data.

This module records the analytic normalization without yet asserting a complete
finite Weil matrix. For a primitive character ``chi`` of conductor ``q`` and
parity ``a`` in ``{0, 1}``, the project uses

    Lambda(s, chi)
        = (q / pi)^((s + a) / 2)
          Gamma((s + a) / 2)
          L(s, chi).

The finite-dimensional conductor and archimedean matrices will be added only
after the explicit-formula test-function convention is frozen.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, pi

from .lfunctions import PrimitiveQuadraticCharacter


@dataclass(frozen=True, slots=True)
class CompletedDirichletData:
    """Metadata for the completed L-function of a primitive quadratic character."""

    character: PrimitiveQuadraticCharacter

    @property
    def conductor(self) -> int:
        return self.character.conductor

    @property
    def parity(self) -> int:
        """Return ``a`` where ``chi(-1) = (-1)^a``."""

        return self.character.parity

    @property
    def gamma_shift(self) -> float:
        """Return the shift ``a / 2`` in ``Gamma(s / 2 + a / 2)``."""

        return self.parity / 2.0

    @property
    def log_conductor_scale(self) -> float:
        """Return ``log(q / pi)`` from the completed-function prefactor."""

        return log(self.conductor / pi)

    def prefactor_log_derivative(self) -> float:
        """Return the constant logarithmic derivative of the power prefactor.

        For ``(q / pi)^((s + a) / 2)``, differentiation with respect to ``s``
        gives ``(1 / 2) log(q / pi)``.
        """

        return 0.5 * self.log_conductor_scale
