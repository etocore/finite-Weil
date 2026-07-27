from experiments.affine_gauge_smith import (
    exact_gauge_smith_data,
    gauge_tangent_determinant,
    predicted_affine_gauge_exponents,
    weighted_centered_shape_basis,
)


def test_weighted_centered_shape_basis_satisfies_constraints() -> None:
    nodes = (-1, 0, 1)
    weights = (1, 2, 1)
    basis = weighted_centered_shape_basis(nodes, weights)

    assert len(basis) == 1
    for vector in basis:
        assert sum(weight * entry for weight, entry in zip(weights, vector, strict=True)) == 0
        assert (
            sum(
                weight * node * entry
                for weight, node, entry in zip(weights, nodes, vector, strict=True)
            )
            == 0
        )


def test_weighted_center_variance_gauges_are_regular() -> None:
    cases = (
        ((-1, 0, 1), (1, 2, 1)),
        ((-3, -1, 1, 3), (1, 1, 1, 1)),
    )
    for nodes, weights in cases:
        basis = weighted_centered_shape_basis(nodes, weights)
        assert gauge_tangent_determinant(nodes, basis) != 0


def test_weighted_center_variance_spectrum_matches_anchored_chart() -> None:
    cases = (
        ((-1, 0, 1), (1, 2, 1)),
        ((-3, -1, 1, 3), (1, 1, 1, 1)),
    )
    for nodes, weights in cases:
        basis = weighted_centered_shape_basis(nodes, weights)
        result = exact_gauge_smith_data(nodes, weights, basis)
        assert result.exponents == predicted_affine_gauge_exponents(len(nodes))


def test_nonuniform_centered_weights_preserve_the_pattern() -> None:
    nodes = (-2, -1, 1, 2)
    weights = (1, 2, 2, 1)
    basis = weighted_centered_shape_basis(nodes, weights)
    result = exact_gauge_smith_data(nodes, weights, basis)
    assert result.exponents == predicted_affine_gauge_exponents(4)
