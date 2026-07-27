"""Algebraic utilities for ordered weighted node collisions.

The functions in this module implement the corrected higher-moment matrix proved
in ``paper/13_collision_moment_determinant.md``. They do not compute a Smith
normal form or claim the missing collision grade.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray

ComplexArray = NDArray[np.complex128]
ComplexMatrix = NDArray[np.complex128]


def _as_complex_vector(value: ArrayLike, *, name: str) -> ComplexArray:
    vector = np.asarray(value, dtype=np.complex128)
    if vector.ndim != 1:
        raise ValueError(f"{name} must be one-dimensional")
    if vector.size < 1:
        raise ValueError(f"{name} must be nonempty")
    if not np.all(np.isfinite(vector.real)) or not np.all(np.isfinite(vector.imag)):
        raise ValueError(f"{name} must be finite")
    return vector


def vandermonde_discriminant(nodes: ArrayLike) -> complex:
    """Return ``prod_{i < j} (xi_j - xi_i)`` for an ordered node vector."""

    xi = _as_complex_vector(nodes, name="nodes")
    value = 1.0 + 0.0j
    for i in range(xi.size):
        for j in range(i + 1, xi.size):
            value *= xi[j] - xi[i]
    return complex(value)


def node_polynomial_derivatives(nodes: ArrayLike) -> ComplexArray:
    """Return ``q_xi'(xi_j)`` for ``q_xi(t) = prod_j (t - xi_j)``."""

    xi = _as_complex_vector(nodes, name="nodes")
    values = np.ones(xi.size, dtype=np.complex128)
    for j in range(xi.size):
        for k in range(xi.size):
            if j != k:
                values[j] *= xi[j] - xi[k]
    return values


def quotient_polynomial(nodes: ArrayLike, degree_offset: int) -> ComplexArray:
    """Return coefficients of the quotient in ``t^(m+s) = q(t) H_s(t) + R_s``.

    Coefficients are returned in descending-power order, matching ``numpy.polyval``.
    """

    xi = _as_complex_vector(nodes, name="nodes")
    if isinstance(degree_offset, bool) or not isinstance(degree_offset, int):
        raise TypeError("degree_offset must be an integer")
    if degree_offset < 0:
        raise ValueError("degree_offset must be nonnegative")

    node_polynomial = np.poly(xi)
    dividend = np.zeros(xi.size + degree_offset + 1, dtype=np.complex128)
    dividend[0] = 1.0
    quotient, remainder = np.polydiv(dividend, node_polynomial)
    if remainder.size and np.max(np.abs(remainder)) > 1e-10:
        # The remainder is generally nonzero. This branch only rejects numerical
        # pathologies that produce nonfinite polynomial division output.
        if not np.all(np.isfinite(remainder.real)) or not np.all(
            np.isfinite(remainder.imag)
        ):
            raise FloatingPointError("polynomial division produced nonfinite values")
    return np.asarray(quotient, dtype=np.complex128)


def corrected_collision_matrix(nodes: ArrayLike, weights: ArrayLike) -> ComplexMatrix:
    """Return the full corrected map from node variations to higher moments.

    The row indexed by ``s`` and column indexed by ``j`` is

    ``u_j q_xi'(xi_j) H_s(xi_j)``, for ``0 <= s <= m - 1``.
    """

    xi = _as_complex_vector(nodes, name="nodes")
    u = _as_complex_vector(weights, name="weights")
    if xi.size != u.size:
        raise ValueError("nodes and weights must have the same length")
    if vandermonde_discriminant(xi) == 0:
        raise ValueError("nodes must be pairwise distinct")

    derivatives = node_polynomial_derivatives(xi)
    matrix = np.empty((xi.size, xi.size), dtype=np.complex128)
    for s in range(xi.size):
        quotient = quotient_polynomial(xi, s)
        matrix[s, :] = u * derivatives * np.polyval(quotient, xi)
    return matrix


def corrected_collision_determinant(nodes: ArrayLike, weights: ArrayLike) -> complex:
    """Return the closed-form determinant ``sign * prod(u_j) * Delta(xi)^3``."""

    xi = _as_complex_vector(nodes, name="nodes")
    u = _as_complex_vector(weights, name="weights")
    if xi.size != u.size:
        raise ValueError("nodes and weights must have the same length")

    sign = (-1) ** (xi.size * (xi.size - 1) // 2)
    return complex(sign * np.prod(u) * vandermonde_discriminant(xi) ** 3)
