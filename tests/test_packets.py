import numpy as np

from finite_weil import GaussianPacketFamily


def test_gram_matrix_is_symmetric_positive_definite() -> None:
    family = GaussianPacketFamily([-1.0, 0.0, 1.0], sigma=0.3)
    gram = family.gram_matrix()

    assert np.allclose(gram, gram.T)
    assert np.min(np.linalg.eigvalsh(gram)) > 0.0


def test_zero_shift_correlation_equals_gram() -> None:
    family = GaussianPacketFamily([-0.5, 0.5], sigma=0.2)

    assert np.allclose(
        family.translated_correlation(0.0),
        family.gram_matrix(),
    )


def test_two_sided_translation_operator_is_symmetric() -> None:
    family = GaussianPacketFamily([-1.0, 0.0, 1.0], sigma=0.4)
    operator = family.symmetric_translation_operator(np.log(2.0))

    assert np.allclose(operator, operator.T)


def test_duplicate_centers_are_rejected() -> None:
    try:
        GaussianPacketFamily([0.0, 0.0], sigma=0.2)
    except ValueError as error:
        assert "distinct" in str(error)
    else:
        raise AssertionError("duplicate centers should be rejected")
