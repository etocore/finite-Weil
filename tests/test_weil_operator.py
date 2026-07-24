import numpy as np
import pytest

from finite_weil.completed import CompletedDirichletData, conductor_matrix
from finite_weil.explicit_formula import assemble_prime_operator
from finite_weil.gamma import gamma_matrix
from finite_weil.lfunctions import PrimitiveQuadraticCharacter
from finite_weil.operators import generalized_eigenvalues, gram_operator_norm
from finite_weil.packets import GaussianPacketFamily
from finite_weil.weil_operator import WeilOperator


def make_operator() -> WeilOperator:
    packets = GaussianPacketFamily([-0.45, 0.25], sigma=0.55)
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(5))
    return WeilOperator(packets, data, prime_cutoff=7)


def test_component_methods_match_standalone_implementations() -> None:
    operator = make_operator()

    assert np.allclose(
        operator.conductor_matrix(),
        conductor_matrix(operator.packets, operator.data),
    )
    assert np.allclose(
        operator.gamma_matrix(),
        gamma_matrix(operator.packets, operator.data),
    )
    assert np.allclose(
        operator.prime_matrix(),
        assemble_prime_operator(
            operator.packets,
            operator.data.character,
            operator.prime_cutoff,
        ),
    )


def test_complete_matrix_is_sum_of_three_contributions() -> None:
    operator = make_operator()

    expected = (
        operator.conductor_matrix()
        + operator.gamma_matrix()
        + operator.prime_matrix()
    )

    assert np.allclose(operator.matrix(), expected)
    assert np.allclose(operator.matrix(), operator.matrix().T)


def test_generalized_spectral_methods_use_packet_gram_matrix() -> None:
    operator = make_operator()
    matrix = operator.matrix()
    gram = operator.gram_matrix()
    expected = generalized_eigenvalues(matrix, gram)

    assert np.allclose(operator.generalized_eigenvalues(), expected)
    assert operator.smallest_generalized_eigenvalue() == pytest.approx(expected[0])
    assert operator.operator_norm() == pytest.approx(gram_operator_norm(matrix, gram))


@pytest.mark.parametrize("cutoff", [0, 1, -5])
def test_prime_cutoff_must_be_at_least_two(cutoff: int) -> None:
    packets = GaussianPacketFamily([0.0], sigma=0.5)
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(1))

    with pytest.raises(ValueError, match="at least 2"):
        WeilOperator(packets, data, cutoff)


@pytest.mark.parametrize("cutoff", [2.5, "7", True])
def test_prime_cutoff_must_be_an_integer(cutoff: object) -> None:
    packets = GaussianPacketFamily([0.0], sigma=0.5)
    data = CompletedDirichletData(PrimitiveQuadraticCharacter(1))

    with pytest.raises(TypeError, match="integer"):
        WeilOperator(packets, data, cutoff)  # type: ignore[arg-type]
