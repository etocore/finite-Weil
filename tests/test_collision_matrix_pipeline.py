import numpy as np

from experiments.collision_matrix_pipeline import (
    analyze_stage,
    collision_centers,
    fully_whitened_matrix,
    numerical_jacobian,
)


def test_collision_centers_center_cluster_and_preserve_exterior() -> None:
    centers = collision_centers(0.25, [-1.0, 0.0, 2.0], [5.0])

    assert np.isclose(np.mean(centers[:3]), 0.0)
    assert np.isclose(centers[-1], 5.0)


def test_numerical_jacobian_matches_linear_map() -> None:
    matrix = np.asarray([[2.0, -1.0], [3.0, 4.0]])

    jacobian = numerical_jacobian(lambda point: matrix @ point, np.asarray([1.0, 2.0]))

    np.testing.assert_allclose(jacobian, matrix, atol=1e-9)


def test_stage_analysis_recovers_known_exponents() -> None:
    scales = 10.0 ** (-np.arange(1, 6, dtype=float))

    def builder(h: float):
        parameters = np.asarray([0.0, 0.0])

        def target(point: np.ndarray) -> np.ndarray:
            return np.asarray([point[0], h**2 * point[1]])

        return target, parameters

    result = analyze_stage("toy", builder, scales)

    np.testing.assert_allclose(np.sort(result.slopes), [0.0, 2.0], atol=1e-8)


def test_fully_whitened_matrix_matches_diagonal_case() -> None:
    operator = np.diag([6.0, -8.0])
    gram = np.diag([2.0, 4.0])

    whitened = fully_whitened_matrix(operator, gram)

    np.testing.assert_allclose(whitened, np.diag([3.0, -2.0]))
