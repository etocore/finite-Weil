from experiments.collision_source_lattice import (
    exact_chart_smith_data,
    predicted_chart_exponents,
    source_change_determinant,
)


def test_source_change_has_unit_coefficient_after_h_factor() -> None:
    assert source_change_determinant((0, 1)) == 1
    assert source_change_determinant((0, 1, 3)) == 1
    assert source_change_determinant((0, 1, 3, 5)) == 1


def test_anchored_chart_exact_small_cases() -> None:
    data = {
        2: ((0, 1), (1, 2)),
        3: ((0, 1, 3), (1, 2, 5)),
        4: ((0, 1, 2, 4), (1, 2, 5, 7)),
    }
    expected_valuations = {
        2: (0, 0, 1, 4),
        3: (0, 0, 1, 4, 8, 13),
        4: (0, 0, 1, 4, 8, 13, 19, 26),
    }

    for cluster_size, (nodes, weights) in data.items():
        result = exact_chart_smith_data(nodes, weights)
        assert result.valuations == expected_valuations[cluster_size]
        assert result.exponents == predicted_chart_exponents(cluster_size)


def test_chart_pattern_is_stable_across_generic_specializations() -> None:
    cases = (
        ((0, 1, 2), (2, 3, 5)),
        ((0, 1, 4), (1, 4, 7)),
        ((0, 1, 2, 5), (1, 3, 4, 9)),
    )
    for nodes, weights in cases:
        result = exact_chart_smith_data(nodes, weights)
        assert result.exponents == predicted_chart_exponents(len(nodes))
