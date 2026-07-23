"""Completed primitive Dirichlet L-function normalization data.

For a primitive character ``chi`` of conductor ``q`` and parity ``a`` in
``{0, 1}``, the project uses

    Lambda(s, chi)
        = (q / pi)^((s + a) / 2)
          Gamma((s + a) / 2)
          L(s, chi).

Under the explicit-formula convention fixed in the project, the two symmetric
contour contributions combine the one-sided logarithmic derivative
``(1 / 2) log(q / pi)`` into the scalar Weil-form contribution
``log(q / pi) <f, g>``. Its packet-coordinate matrix is therefore
``log(q / pi) B``, where ``B`` is the packet Gram matrix.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, pi

from numpy.typing import NDArray
import numpy as np

from .gram import scalar_form_matrix
from .lfunctions import PrimitiveQuadraticCharacter
from .packets import GaussianPacketFamily

FloatMatrix = NDArray[np.float64]


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
        """Return the one-sided logarithmic derivative of the power prefactor.

        For ``(q / pi)^((s + a) / 2)``, differentiation with respect to ``s``
        gives ``(1 / 2) log(q / pi)``.
        """

        return 0.5 * self.log_conductor_scale

    def conductor_form_coefficient(self) -> float:
        """Return the scalar coefficient in the symmetric Weil form.

        The explicit formula contains both sides of the functional equation.
        Their equal constant contributions add, so the coefficient is twice the
        one-sided prefactor logarithmic derivative.
        """

        return 2.0 * self.prefactor_log_derivative()


def conductor_matrix(
    packets: GaussianPacketFamily,
    data: CompletedDirichletData,
) -> FloatMatrix:
    """Return the exact conductor contribution ``log(q / pi) B``."""

    return scalar_form_matrix(packets, data.conductor_form_coefficient())
