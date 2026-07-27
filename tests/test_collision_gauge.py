import numpy as np

from experiments.collision_gauge import (
    analyze_gauge,
    center_nodes,
    normalized_shape_tangent,
    scale_shape_frame,
)


def test_center_nodes_removes_arithmetic_mean() -> None:
    nodes = center_nodes([1.0, 2.0, 4.0])

    assert np.isclose(np.sum(nodes), 0.0)


def test_shape_tangent_satisfies_center_and_scale_constraints() -> None:
    nodes = center_nodes([-2.0, -0.5, 0.75, 3.0])
    tangent = normalized_shape_tangent(nodes)

    assert tangent.shape == (4, 2)
    assert np.allclose(np.ones(4) @ tangent, 0.0, atol=1e-13)
    assert np.allclose(np.conjugate(nodes) @ tangent, 0.0, atol=1e-13)
    assert np.allclose(tangent.conjugate().T @ tangent, np.eye(2), atol=1e-13)


def test_scale_shape_frame_spans_centered_node_space() -> None:
    nodes = center_nodes([-1.5, -0.25, 0.5, 2.0])
    frame = scale_shape_frame(nodes)

    assert frame.shape == (4, 3)
    assert np.allclose(np.ones(4) @ frame, 0.0, atol=1e-13)
    assert np.linalg.matrix_rank(frame) == 3


def test_restricted_collision_map_has_one_left_relation() -> None:
    result = analyze_gauge([-1.0, 0.0, 1.0], [1.0, 2.0, 3.0])

    assert result.restricted_matrix.shape == (3, 2)
    assert result.left_relation.shape == (3,)
    assert np.linalg.matrix_rank(result.restricted_matrix) == 2
    assert result.residual_norm < 1e-12


def test_left_relation_is_stable_under_weight_rescaling() -> None:
    first = analyze_gauge([-2.0, -0.25, 0.75, 1.5], [1.0, 2.0, 3.0, 4.0])
    second = analyze_gauge([-2.0, -0.25, 0.75, 1.5], [7.0, 14.0, 21.0, 28.0])

    overlap = abs(np.vdot(first.left_relation, second.left_relation))
    assert np.isclose(overlap, 1.0, atol=1e-12)
