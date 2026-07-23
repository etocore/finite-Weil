"""Arithmetic data for finite Weil experiments.

The first supported family is the primitive real Dirichlet character

    chi_D(n) = (D / n),

where ``D`` is a fundamental discriminant and ``(D / n)`` is the Kronecker
symbol.  No analytic continuation or zero data is encoded here: this module
contains arithmetic coefficients only.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt


def _is_squarefree(n: int) -> bool:
    n = abs(n)
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1 if p == 2 else 2
    return True


def is_fundamental_discriminant(discriminant: int) -> bool:
    """Return whether ``discriminant`` is a nonzero fundamental discriminant."""

    d = int(discriminant)
    if d == 0:
        return False
    if d % 4 == 1:
        return _is_squarefree(d)
    if d % 4 == 0:
        m = d // 4
        return m % 4 in (2, 3) and _is_squarefree(m)
    return False


def jacobi_symbol(a: int, n: int) -> int:
    """Return the Jacobi symbol ``(a / n)`` for positive odd ``n``."""

    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def kronecker_symbol(a: int, n: int) -> int:
    """Return the Kronecker symbol ``(a / n)``.

    This implementation supports all integer numerators and denominators and is
    sufficient for primitive quadratic characters ``chi_D(n)``.
    """

    a = int(a)
    n = int(n)
    if n == 0:
        return 1 if abs(a) == 1 else 0
    if n == 1:
        return 1
    if n == -1:
        return -1 if a < 0 else 1

    sign = 1
    if n < 0:
        n = -n
        if a < 0:
            sign = -1

    twos = 0
    while n % 2 == 0:
        n //= 2
        twos += 1

    if twos:
        if a % 2 == 0:
            return 0
        two_symbol = 1 if a % 8 in (1, 7) else -1
        if twos % 2:
            sign *= two_symbol

    if n == 1:
        return sign
    return sign * jacobi_symbol(a, n)


@dataclass(frozen=True, slots=True)
class PrimitiveQuadraticCharacter:
    """Primitive quadratic Dirichlet character attached to a fundamental ``D``."""

    discriminant: int

    def __post_init__(self) -> None:
        if not is_fundamental_discriminant(self.discriminant):
            raise ValueError("discriminant must be a nonzero fundamental discriminant")

    @property
    def conductor(self) -> int:
        return abs(self.discriminant)

    @property
    def parity(self) -> int:
        """Return ``0`` for even and ``1`` for odd character parity."""

        return 0 if self.discriminant > 0 else 1

    def __call__(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n == 0:
            return 0
        return kronecker_symbol(self.discriminant, n)

    def is_coprime_to_conductor(self, n: int) -> bool:
        return gcd(int(n), self.conductor) == 1


def prime_power_base(n: int) -> tuple[int, int] | None:
    """Return ``(p, k)`` when ``n = p**k`` with prime ``p``; otherwise ``None``."""

    n = int(n)
    if n < 2:
        return None
    for p in range(2, isqrt(n) + 1):
        if n % p:
            continue
        value = n
        exponent = 0
        while value % p == 0:
            value //= p
            exponent += 1
        if value == 1 and _is_prime(p):
            return p, exponent
        return None
    return (n, 1) if _is_prime(n) else None


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True
