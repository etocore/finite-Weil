"""Prime-power terms in the finite Weil explicit-formula model.

The conventions in this module are definitions for the current reconstruction:

    T_n = -(C(log n) + C(-log n)),
    beta_chi(n) = Lambda(n) chi(n) / sqrt(n),
    A_prime(N) = sum_{2 <= n <= N} beta_chi(n) T_n.

With these choices the minus sign in the classical two-sided prime term is
contained in ``T_n``.  The archimedean and conductor matrices are deliberately
not included until their Fourier normalization has been independently audited.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt

import numpy as np
from numpy.typing import NDArray

from .lfunctions import PrimitiveQuadraticCharacter, prime_power_base
from .packets import GaussianPacketFamily

FloatMatrix = NDArray[np.float64]


def von_mangoldt(n: int) -> float:
    """Return the von Mangoldt function ``Lambda(n)``."""

    decomposition = prime_power_base(n)
    if decomposition is None:
        return 0.0
    prime, _ = decomposition
    return log(prime)


def quadratic_prime_power_coefficient(
    n: int, character: PrimitiveQuadraticCharacter
) -> float:
    """Return ``Lambda(n) chi(n) / sqrt(n)``."""

    if n < 2:
        return 0.0
    mangoldt = von_mangoldt(n)
    if mangoldt == 0.0:
        return 0.0
    return mangoldt * character(n) / sqrt(n)


def universal_prime_operator(
    packets: GaussianPacketFamily, n: int
) -> FloatMatrix:
    """Return the universal symmetric matrix ``T_n`` for integer ``n >= 2``."""

    if n < 2:
        raise ValueError("n must be at least 2")
    return packets.symmetric_translation_operator(log(n))


@dataclass(frozen=True, slots=True)
class PrimeOperatorTerm:
    n: int
    coefficient: float
    matrix: FloatMatrix


def prime_operator_terms(
    packets: GaussianPacketFamily,
    character: PrimitiveQuadraticCharacter,
    cutoff: int,
) -> tuple[PrimeOperatorTerm, ...]:
    """Return all nonzero prime-power terms through ``cutoff``."""

    if cutoff < 2:
        return ()
    terms: list[PrimeOperatorTerm] = []
    for n in range(2, cutoff + 1):
        coefficient = quadratic_prime_power_coefficient(n, character)
        if coefficient == 0.0:
            continue
        terms.append(
            PrimeOperatorTerm(
                n=n,
                coefficient=coefficient,
                matrix=universal_prime_operator(packets, n),
            )
        )
    return tuple(terms)


def assemble_prime_operator(
    packets: GaussianPacketFamily,
    character: PrimitiveQuadraticCharacter,
    cutoff: int,
) -> FloatMatrix:
    """Assemble the truncated prime matrix through ``n <= cutoff``."""

    matrix = np.zeros((packets.dimension, packets.dimension), dtype=float)
    for term in prime_operator_terms(packets, character, cutoff):
        matrix += term.coefficient * term.matrix
    return matrix
