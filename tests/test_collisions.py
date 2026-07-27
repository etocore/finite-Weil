import numpy as np
import pytest

from finite_weil.collisions import (
    corrected_collision_determinant,
    corrected_collision_matrix,
    node_polynomial_derivatives,
    quotient_polynomial,
    vandermonde_discriminant,
)


def test_vandermonde_discriminant_uses_ordered_nodes() -> None:
    nodes = np.asarray([-1.0, 0.0, 2.0])

    assert vandermonde_discriminant(nodes) == pytest.approx(6.0)


def test_node_polynomial_derivatives_match_direct_products() -> None:
    nodes = np.asarray([-1.0, 0.0, 2.0])

    values = node_polynomial_derivatives(nodes)

    assert np.allclose(values, [3.0, -2.0, 6.0])


def test_quotient_polynomial_has_expected_first_cases() -> None:
    nodes = np.asarray([-1.0, 0.0, 2.0])

    h0 = quotient_polynomial(nodes, 0)
    h1 = quotient_polynomial(nodes, 1)
    h2 = quotient_polynomial(nodes, 2)

    assert np.allclose(h0, [1.0])
    assert np.allclose(h1, [1.0, 1.0])
    assert np.allclose(h2, [1.0, 1.0, 3.0])


@pytest.mark.parametrize(
    ("nodes", "weights"),
    [
        ([-1.0, 1.0], [2.0, -3.0]),
        ([-1.0, 0.0, 1.0], [1.0, -2.0, 1.0]),
        ([1.0, 2.0, 3.0], [0.5, 2.0, -1.0]),
        ([-2.0, -0.5, 0.75, 3.0], [1.0, 0.25, -2.0, 4.0]),
    ],
)
def test_corrected_matrix_matches_closed_form_determinant(
    nodes: list[float],
    weights: list[float],
) -> None:
    matrix = corrected_collision_matrix(nodes, weights)
    expected = corrected_collision_determinant(nodes, weights)

    assert np.linalg.det(matrix) == pytest.approx(expected, rel=1e-11, abs=1e-11)


def test_base_moment_vanishing_does_not_destroy_corrected_map() -> None:
    nodes = np.asarray([-1.0, 0.0, 1.0])
    weights = np.asarray([1.0, -2.0, 1.0])

    moments = np.asarray(
        [
            np.sum(weights * nodes**0),
            np.sum(weights * nodes**1),
        ]
    )
    matrix = corrected_collision_matrix(nodes, weights)

    assert np.allclose(moments, 0.0)
    assert abs(np.linalg.det(matrix)) > 1e-12


def test_determinant_is_linear_in_each_individual_weight() -> None:
    nodes = np.asarray([-1.0, 0.0, 1.0])
    baseline = corrected_collision_determinant(nodes, [1.0, 2.0, 3.0])
    scaled = corrected_collision_determinant(nodes, [1.0, 2.0, 0.003])

    assert scaled / baseline == pytest.approx(0.001)


def test_repeated_nodes_are_rejected() -> None:
    with pytest.raises(ValueError, match="pairwise distinct"):
        corrected_collision_matrix([0.0, 0.0, 1.0], [1.0, 2.0, 3.0])
