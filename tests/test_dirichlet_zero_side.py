"""Zero-side regression for a non-principal quadratic character.

Skipped when ``mpmath`` is unavailable (it ships with the ``experiments``
extra, not the core package).  The reference zeros are computed at run time
from the Hurwitz-zeta representation of ``L(s, chi_5)``, independently of
every matrix implementation in the package.
"""

import numpy as np
import pytest

pytest.importorskip("mpmath")

from experiments.dirichlet_zero_side import critical_zeros, run_case
from finite_weil import PrimitiveQuadraticCharacter


def test_chi5_zeros_match_known_low_ordinates() -> None:
    zeros = critical_zeros(PrimitiveQuadraticCharacter(5), 12.0)

    # Low zeros of L(s, chi_5); reference values reproduced by this module's
    # own independent computation and stable to the displayed digits.
    assert len(zeros) >= 3
    assert zeros[0] == pytest.approx(6.6485, abs=2e-4)
    assert zeros[1] == pytest.approx(9.8314, abs=2e-4)
    assert zeros[2] == pytest.approx(11.9588, abs=2e-4)


def test_chi5_assembled_matrix_matches_zero_side() -> None:
    row = run_case(
        discriminant=5,
        sigma=0.2,
        extent=1.2,
        dimension=5,
        cutoff=2000,
        envelope_floor=1e-13,
    )

    assert row.zeros_used >= 5
    assert row.max_zero_side_entry > 1e-3
    assert row.max_entry_error < 1e-12
    assert row.lambda_min > 0.0
    assert np.isfinite(row.first_zero)
