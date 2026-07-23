import numpy as np

from finite_weil import generalized_eigenvalues, gram_operator_norm


def test_generalized_eigenvalues_match_diagonal_case() -> None:
    gram = np.diag([2.0, 4.0])
    operator = np.diag([6.0, -8.0])

    values = generalized_eigenvalues(operator, gram)

    assert np.allclose(values, [-2.0, 3.0])


def test_gram_operator_norm_is_largest_absolute_generalized_eigenvalue() -> None:
    gram = np.diag([2.0, 4.0])
    operator = np.diag([6.0, -8.0])

    assert np.isclose(gram_operator_norm(operator, gram), 3.0)
