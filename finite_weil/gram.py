"""Gram-form utilities for finite packet spaces.

This module isolates basis geometry from arithmetic and explicit-formula data.
Every scalar multiplication form on the packet span is represented by a scalar
multiple of the packet Gram matrix.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from .packets import GaussianPacketFamily

FloatMatrix = NDArray[np.float64]


def gram_matrix(packets: GaussianPacketFamily) -> FloatMatrix:
    """Return the packet Gram matrix."""

    return packets.gram_matrix()


def scalar_form_matrix(
    packets: GaussianPacketFamily,
    scalar: float,
) -> FloatMatrix:
    """Return the matrix of ``(f, g) -> scalar * <f, g>`` on the packet span."""

    if not np.isfinite(scalar):
        raise ValueError("scalar must be finite")
    return float(scalar) * packets.gram_matrix()
