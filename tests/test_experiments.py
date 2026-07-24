from pathlib import Path

import numpy as np

from experiments.convergence import packet_centers, run_case, write_rows


def test_packet_centers_are_symmetric() -> None:
    centers = packet_centers(5, 2.0)

    assert np.allclose(centers, [-2.0, -1.0, 0.0, 1.0, 2.0])


def test_run_case_returns_finite_measurements() -> None:
    row = run_case(
        discriminant=5,
        dimension=3,
        sigma=0.75,
        cutoff=10,
        center_extent=2.0,
    )

    assert row.discriminant == 5
    assert row.dimension == 3
    assert np.isfinite(row.lambda_min)
    assert np.isfinite(row.lambda_max)
    assert np.isfinite(row.operator_norm)
    assert row.gram_condition >= 1.0
    assert row.runtime_seconds >= 0.0


def test_write_rows_creates_csv(tmp_path: Path) -> None:
    row = run_case(
        discriminant=-3,
        dimension=2,
        sigma=1.0,
        cutoff=5,
        center_extent=1.0,
    )
    output = tmp_path / "results.csv"

    write_rows(output, [row])

    text = output.read_text(encoding="utf-8")
    assert "lambda_min" in text
    assert "-3" in text
