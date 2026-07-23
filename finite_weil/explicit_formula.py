"""Prime-power terms in the finite Weil explicit-formula model.

The conventions in this module are definitions for the current reconstruction:

    T_n = -(C(log n) + C(-log n)),
    beta_chi(n) = Lambda(n) chi(n) / sqrt(n),
    A_prime(N) = sum_{2 <= n <= N} beta_chi(n) T_n.

The optional smooth weights are numerical regularizations of the truncated prime
sum. They do not change the arithmetic coefficients or the universal translation
matrices and should not be interpreted as a proved tail treatment.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from math import exp, log, sqrt

import numpy as np
from numpy.typing import NDArray

from .lfunctions import PrimitiveQuadraticCharacter, prime_power_base
from .packets import GaussianPacketFamily

FloatMatrix = NDArray[np.float64]
PrimeWeight = Callable[[int, int], float]


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


def sharp_prime_weight(n: int, cutoff: int) -> float:
    """Return the sharp cutoff weight ``1_{n <= cutoff}``."""

    if cutoff < 2:
        raise ValueError("cutoff must be at least 2")
    return 1.0 if 2 <= n <= cutoff else 0.0


def exponential_prime_weight(n: int, cutoff: int) -> float:
    """Return the smooth weight ``exp(-n / cutoff)`` for ``n >= 2``."""

    if cutoff < 2:
        raise ValueError("cutoff must be at least 2")
    if n < 2:
        return 0.0
    return exp(-float(n) / float(cutoff))


def gaussian_log_prime_weight(n: int, cutoff: int) -> float:
    """Return ``exp(-(log(n) / log(cutoff))**2)`` for ``n >= 2``."""

    if cutoff < 2:
        raise ValueError("cutoff must be at least 2")
    if n < 2:
        return 0.0
    scale = log(cutoff)
    return exp(-((log(n) / scale) ** 2))


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
    weight: float
    matrix: FloatMatrix


def prime_operator_terms(
    packets: GaussianPacketFamily,
    character: PrimitiveQuadraticCharacter,
    cutoff: int,
    *,
    weight: PrimeWeight = sharp_prime_weight,
    support_multiplier: float = 1.0,
) -> tuple[PrimeOperatorTerm, ...]:
    """Return weighted nonzero prime-power terms for the chosen regularization.

    ``support_multiplier`` controls the finite evaluation range. For the sharp
    cutoff the default value ``1`` reproduces the original sum. Smooth weights
    can be evaluated farther out, for example with ``support_multiplier=8``.
    """

    if cutoff < 2:
        return ()
    if support_multiplier <= 0 or not np.isfinite(support_multiplier):
        raise ValueError("support_multiplier must be a finite positive number")

    maximum = max(2, int(np.ceil(cutoff * support_multiplier)))
    terms: list[PrimeOperatorTerm] = []
    for n in range(2, maximum + 1):
        coefficient = quadratic_prime_power_coefficient(n, character)
        if coefficient == 0.0:
            continue
        term_weight = float(weight(n, cutoff))
        if not np.isfinite(term_weight):
            raise ValueError("prime weight must return finite values")
        if term_weight == 0.0:
            continue
        terms.append(
            PrimeOperatorTerm(
                n=n,
                coefficient=coefficient,
                weight=term_weight,
                matrix=universal_prime_operator(packets, n),
            )
        )
    return tuple(terms)


def assemble_prime_operator(
    packets: GaussianPacketFamily,
    character: PrimitiveQuadraticCharacter,
    cutoff: int,
    *,
    weight: PrimeWeight = sharp_prime_weight,
    support_multiplier: float = 1.0,
) -> FloatMatrix:
    """Assemble a weighted truncated prime matrix."""

    matrix = np.zeros((packets.dimension, packets.dimension), dtype=float)
    for term in prime_operator_terms(
        packets,
        character,
        cutoff,
        weight=weight,
        support_multiplier=support_multiplier,
    ):
        matrix += term.coefficient * term.weight * term.matrix
    return matrix
