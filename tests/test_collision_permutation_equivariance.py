from experiments.collision_permutation_equivariance import (
    filtration_dimensions,
    permute_pairs,
    permuted_column_order,
    raw_moment_coefficient_matrix,
    reorder_columns,
)


def test_raw_jacobian_is_equivariant_under_pair_permutations() -> None:
    nodes = (0, 1, 3, 5)
    weights = (2, 7, 11, 13)
    permutation = (2, 0, 3, 1)

    original = raw_moment_coefficient_matrix(nodes, weights)
    permuted_nodes, permuted_weights = permute_pairs(nodes, weights, permutation)
    permuted = raw_moment_coefficient_matrix(permuted_nodes, permuted_weights)

    assert permuted == reorder_columns(original, permuted_column_order(permutation))


def test_affine_gauge_filtration_dimensions_have_no_grade_two_jump() -> None:
    exponents = (0, 0, 1, 3, 4, 5)
    assert filtration_dimensions(exponents) == (6, 4, 3, 3, 2, 1)


def test_physical_filtration_dimensions_record_missing_grade_m() -> None:
    exponents = (0, 0, 1, 2, 4, 5)
    assert filtration_dimensions(exponents) == (6, 4, 3, 2, 2, 1)
