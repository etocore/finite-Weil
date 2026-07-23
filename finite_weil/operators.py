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


def generalized_eigenvalues(operator: ArrayLike, gram: ArrayLike) -> FloatArray:
    """Return the ordered generalized eigenvalues of ``A v = lambda B v``."""

    a = _as_symmetric_matrix(operator, name="operator")
    b = _as_symmetric_matrix(gram, name="gram")
    if a.shape != b.shape:
        raise ValueError("operator and gram must have the same shape")
    return np.asarray(eigh(a, b, eigvals_only=True, check_finite=True), dtype=float)


def gram_operator_norm(operator: ArrayLike, gram: ArrayLike) -> float:
    """Return the intrinsic operator norm induced by a positive Gram matrix.

    For a Gram-self-adjoint matrix ``H``, this equals the largest absolute
    generalized eigenvalue of ``H v = lambda B v``.
    """

    eigenvalues = generalized_eigenvalues(operator, gram)
    return float(np.max(np.abs(eigenvalues)))
