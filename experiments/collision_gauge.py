"""Explore the missing collision grade in normalized node coordinates.

This module restricts the proved corrected collision matrix to scale and normalized
shape directions, then computes its one-dimensional left kernel. The output is a
numerical observation used to identify a later symbolic missing-grade identity.
It is not itself a Smith-spectrum theorem.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.linalg import null_space

from finite_weil.collisions import corrected_collision_matrix

ComplexArray = NDArray[np.complex128]
ComplexMatrix = NDArray[np.complex128]


@dataclass(frozen=True, slots=True)
class GaugeResult:
    """Restricted collision matrix and its normalized left-kernel relation."""

    nodes: ComplexArray
    weights: ComplexArray
    source_frame: ComplexMatrix
    restricted_matrix: ComplexMatrix
    left_relation: ComplexArray
    residual_norm: float


def _as_complex_vector(value: ArrayLike, *, name: str) -> ComplexArray:
    vector = np.asarray(value, dtype=np.complex128)
    if vector.ndim != 1 or vector.size < 2:
        raise ValueError(f"{name} must be a one-dimensional vector of length at least two")
    if not np.all(np.isfinite(vector.real)) or not np.all(np.isfinite(vector.imag)):
        raise ValueError(f"{name} must be finite")
    return vector


def center_nodes(nodes: ArrayLike) -> ComplexArray:
    """Return nodes translated to arithmetic mean zero."""

    xi = _as_complex_vector(nodes, name="nodes")
    return np.asarray(xi - np.mean(xi), dtype=np.complex128)


def normalized_shape_tangent(nodes: ArrayLike) -> ComplexMatrix:
    """Return an orthonormal basis for centered, scale-orthogonal shape directions.

    For centered real nodes this is the null space of the two linear constraints
    ``sum(delta_xi) = 0`` and ``sum(conj(xi) * delta_xi) = 0``. The Hermitian
    version is used so the experiment also behaves coherently for complex nodes.
    """

    xi = center_nodes(nodes)
    constraints = np.vstack(
        [
            np.ones(xi.size, dtype=np.complex128),
            np.conjugate(xi),
        ]
    )
    basis = null_space(constraints)
    return np.asarray(basis, dtype=np.complex128)


def scale_shape_frame(nodes: ArrayLike) -> ComplexMatrix:
    """Return the source frame consisting of scale followed by shape directions."""

    xi = center_nodes(nodes)
    norm = float(np.linalg.norm(xi))
    if norm == 0.0:
        raise ValueError("centered nodes must contain a nonzero scale direction")
    scale = xi / norm
    shape = normalized_shape_tangent(xi)
    return np.asarray(np.column_stack([scale, shape]), dtype=np.complex128)


def normalized_left_relation(matrix: ArrayLike) -> ComplexArray:
    """Return a unit left-kernel vector with a deterministic phase convention."""

    value = np.asarray(matrix, dtype=np.complex128)
    if value.ndim != 2 or value.shape[0] != value.shape[1] + 1:
        raise ValueError("matrix must have exactly one more row than column")
    kernel = null_space(value.conjugate().T)
    if kernel.shape != (value.shape[0], 1):
        raise ValueError("matrix must have a one-dimensional left kernel")
    relation = np.asarray(kernel[:, 0], dtype=np.complex128)
    pivot = int(np.argmax(np.abs(relation)))
    relation *= np.exp(-1j * np.angle(relation[pivot]))
    if relation[pivot].real < 0:
        relation *= -1.0
    return relation


def analyze_gauge(nodes: ArrayLike, weights: ArrayLike) -> GaugeResult:
    """Restrict the corrected map and compute its missing target relation."""

    xi = center_nodes(nodes)
    u = _as_complex_vector(weights, name="weights")
    if xi.size != u.size:
        raise ValueError("nodes and weights must have the same length")
    frame = scale_shape_frame(xi)
    restricted = corrected_collision_matrix(xi, u) @ frame
    relation = normalized_left_relation(restricted)
    residual = relation.conjugate() @ restricted
    return GaugeResult(
        nodes=xi,
        weights=u,
        source_frame=frame,
        restricted_matrix=restricted,
        left_relation=relation,
        residual_norm=float(np.linalg.norm(residual)),
    )


def _parse_numbers(value: str) -> ComplexArray:
    return np.asarray([complex(item.strip()) for item in value.split(",")], dtype=np.complex128)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes", default="-1,0,1")
    parser.add_argument("--weights", default="1,2,3")
    args = parser.parse_args()

    result = analyze_gauge(_parse_numbers(args.nodes), _parse_numbers(args.weights))
    print("centered nodes:", result.nodes)
    print("left relation:", result.left_relation)
    print("residual norm:", f"{result.residual_norm:.3e}")


if __name__ == "__main__":
    main()
