import numpy as np
import pytest

from finite_weil.collisions import (
    collision_translation_relation,
    corrected_collision_matrix,
)


@pytest.mark.parametrize(
    ("nodes", "weights"),
    [
        ([-1.0, 0.0, 1.0], [1.0, 2.0, 3.0]),
        ([-2.0, -0.5, 0.75, 3.0], [1.0, -2.0, 4.0, 0.5]),
        ([0.0, 1.0, 3.0, 7.0, 9.0], [2.0, 1.0, -1.0, 3.0, 5.0]),
    ],
)
def test_translation_relation_is_dual_to_common_translation(
    nodes: list[float],
    weights: list[float],
) -> None:
    matrix = corrected_collision_matrix(nodes, weights)
    relation = collision_translation_relation(nodes, weights)

    assert np.allclose(matrix.T @ relation, np.ones(len(nodes)))


def test_translation_relation_annihilates_centered_variations() -> None:
    nodes = np.asarray([-1.5, -0.25, 0.75, 2.0])
    weights = np.asarray([1.0, 2.0, -0.5, 3.0])
    matrix = corrected_collision_matrix(nodes, weights)
    relation = collision_translation_relation(nodes, weights)
    centered_variation = np.asarray([1.0, -2.0, 0.5, 0.5])

    assert np.isclose(np.sum(centered_variation), 0.0)
    assert np.isclose(relation @ matrix @ centered_variation, 0.0)


def test_translation_relation_recovers_translation_amplitude() -> None:
    nodes = np.asarray([-1.0, 0.5, 2.0])
    weights = np.asarray([1.0, -3.0, 2.0])
    matrix = corrected_collision_matrix(nodes, weights)
    relation = collision_translation_relation(nodes, weights)
    variation = np.asarray([2.0, -1.0, 4.0])

    assert np.isclose(relation @ matrix @ variation, np.sum(variation))
