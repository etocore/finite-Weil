import numpy as np
import pytest

from finite_weil import GaussianPacketFamily, gram_matrix, scalar_form_matrix


def test_gram_wrapper_matches_packet_family() -> None:
    packets = GaussianPacketFamily([-0.5, 0.5], sigma=0.3)

    assert np.allclose(gram_matrix(packets), packets.gram_matrix())


def test_scalar_form_is_scalar_multiple_of_gram() -> None:
    packets = GaussianPacketFamily([-1.0, 0.0, 1.0], sigma=0.4)

    matrix = scalar_form_matrix(packets, 2.5)

    assert np.allclose(matrix, 2.5 * packets.gram_matrix())
    assert np.allclose(matrix, matrix.T)


def test_scalar_form_rejects_nonfinite_scalar() -> None:
    packets = GaussianPacketFamily([0.0], sigma=0.4)

    with pytest.raises(ValueError):
        scalar_form_matrix(packets, np.inf)
