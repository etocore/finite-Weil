from experiments.collision_source_lattice import (
    exact_chart_smith_data,
    predicted_chart_exponents,
    predicted_chart_valuation,
    predicted_chart_valuations,
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
        assert result.valuations == predicted_chart_valuations(cluster_size)
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


def test_chart_valuation_formula() -> None:
    for cluster_size in range(2, 9):
        assert predicted_chart_valuations(cluster_size)[:2] == (0, 0)
        for minor_size in range(3, 2 * cluster_size + 1):
            assert predicted_chart_valuation(cluster_size, minor_size) == (
                minor_size * (minor_size - 1) // 2 - 2
            )


def test_chart_exponents_have_only_grade_two_missing() -> None:
    for cluster_size in range(3, 9):
        assert predicted_chart_exponents(cluster_size) == (
            0,
            0,
            1,
            *range(3, 2 * cluster_size),
        )
