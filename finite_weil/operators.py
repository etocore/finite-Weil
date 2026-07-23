"""Coordinate-aware linear algebra for finite Weil operators."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.linalg import eigh

FloatArray = NDArray[np.float64]


def _as_symmetric_matrix(value: ArrayLike, *, name: str) -> FloatArray:
    matrix = np.asarray(value, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"{name} must be square")
    if not np.all(np.isfinite(matrix)):
        raise ValueError(f"{name} must contain only finite entries")
    if not np.allclose(matrix, matrix.T, rtol=1e-12, atol=1e-12):
        raise ValueError(f"{name} must be symmetric")
    return matrix


def gram_whitened_matrix(
    operator: ArrayLike,
    gram: ArrayLike,
    *,
    relative_tolerance: float = 1e-12,
) -> FloatArray:
    """Return the operator in a numerically orthonormalized packet basis.

    Gram eigenmodes below ``relative_tolerance * lambda_max(B)`` are discarded.
    The retained matrix is congruent to the original quadratic form on the stable
    packet subspace and avoids failures caused by nearly dependent packets.
    """

    a = _as_symmetric_matrix(operator, name="operator")
    b = _as_symmetric_matrix(gram, name="gram")
    if a.shape != b.shape:
        raise ValueError("operator and gram must have the same shape")
    if relative_tolerance <= 0 or not np.isfinite(relative_tolerance):
        raise ValueError("relative_tolerance must be a finite positive number")

    values, vectors = eigh(b, check_finite=True)
    maximum = float(values[-1])
    if maximum <= 0:
        raise ValueError("gram must be positive definite on a nonzero subspace")
    retained = values > relative_tolerance * maximum
    if not np.any(retained):
        raise ValueError("no stable Gram modes remain at the requested tolerance")

    basis = vectors[:, retained] / np.sqrt(values[retained])[None, :]
    whitened = basis.T @ a @ basis
    return np.asarray(0.5 * (whitened + whitened.T), dtype=float)


def generalized_eigenvalues(
    operator: ArrayLike,
    gram: ArrayLike,
    *,
    relative_tolerance: float | None = None,
) -> FloatArray:
    """Return ordered eigenvalues of ``A v = lambda B v``.

    With ``relative_tolerance=None`` this uses SciPy's direct definite generalized
    solver. Supplying a tolerance first whitens the Gram matrix and truncates
    numerically null packet modes.
    """

    a = _as_symmetric_matrix(operator, name="operator")
    b = _as_symmetric_matrix(gram, name="gram")
    if a.shape != b.shape:
        raise ValueError("operator and gram must have the same shape")
    if relative_tolerance is None:
        return np.asarray(eigh(a, b, eigvals_only=True, check_finite=True), dtype=float)
    whitened = gram_whitened_matrix(
        a,
        b,
        relative_tolerance=relative_tolerance,
    )
    return np.asarray(eigh(whitened, eigvals_only=True, check_finite=True), dtype=float)


def gram_operator_norm(
    operator: ArrayLike,
    gram: ArrayLike,
    *,
    relative_tolerance: float | None = None,
) -> float:
    """Return the largest absolute intrinsic eigenvalue."""

    eigenvalues = generalized_eigenvalues(
        operator,
        gram,
        relative_tolerance=relative_tolerance,
    )
    return float(np.max(np.abs(eigenvalues)))
