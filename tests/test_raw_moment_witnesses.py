from experiments.raw_moment_witnesses import (
    canonical_witness_indices,
    elementary_lower_bound,
    predicted_valuations,
    verify_canonical_witnesses,
)


def test_predicted_valuations_match_known_cases() -> None:
    assert predicted_valuations(2) == (0, 0, 1, 4)
    assert predicted_valuations(3) == (0, 0, 1, 3, 7, 12)
    assert predicted_valuations(4) == (0, 0, 1, 3, 6, 11, 17, 24)


def test_elementary_lower_bound_equals_predicted_formula() -> None:
    for cluster_size in range(2, 8):
        expected = predicted_valuations(cluster_size)
        actual = tuple(
            elementary_lower_bound(cluster_size, size)
            for size in range(1, 2 * cluster_size + 1)
        )
        assert actual == expected


def test_canonical_indices_use_expected_column_counts() -> None:
    rows, columns = canonical_witness_indices(4, 5)
    assert rows == (0, 1, 2, 3, 4)
    assert columns == (0, 4, 5, 6, 7)

    rows, columns = canonical_witness_indices(4, 7)
    assert rows == (0, 1, 2, 3, 4, 5, 6)
    assert columns == (0, 1, 2, 4, 5, 6, 7)


def test_canonical_witnesses_are_nonzero_for_generic_rational_data() -> None:
    data = {
        2: ((-1, 1), (1, 2)),
        3: ((-1, 0, 2), (1, 2, 3)),
        4: ((-2, -1, 1, 3), (1, 2, 3, 5)),
        5: ((-3, -1, 0, 2, 4), (1, 2, 3, 5, 7)),
    }
    for cluster_size, (nodes, weights) in data.items():
        witnesses = verify_canonical_witnesses(nodes, weights)
        assert tuple(witness.valuation for witness in witnesses) == predicted_valuations(
            cluster_size
        )
        assert all(witness.leading_coefficient != 0 for witness in witnesses)
