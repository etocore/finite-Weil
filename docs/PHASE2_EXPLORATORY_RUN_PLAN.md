# Phase 2 exploratory run plan

## Status

This document defines the next executable research step. It does **not** claim that a high-band run has already been performed, and it does not authorize any result to be described as certified until every gate in `docs/FALSIFICATION_PROTOCOL.md` is satisfied.

## Objective

Use the existing finite-Weil machinery to run a preregistered exploratory ladder at modulation frequencies above the project's adopted verification horizon, while preserving the separation:

> Geometry is the probe space; arithmetic is the state.

The first deliverable is a reproducible floating-point exploration with complete manifests and search accounting. The second deliverable, after the interval gates are complete, is a certified rerun of the same manifests.

## Hard stop before execution

No numerical result may be labeled certified unless all of the following are present and passing:

1. complex-Hermitian interval generalized-eigenvalue verification;
2. interval modulated Archimedean assembly;
3. geometry-aware rigorous prime-tail bound;
4. exact nonzero-modulation pole orientation tests;
5. immutable manifest validation;
6. computed-only conclusion generation;
7. Phase 1 calibration regression suite;
8. separately authored reproduction implementation.

Until then, outputs are `exploratory_float` only.

## Frozen first batch

The first exploratory batch uses four geometry classes:

1. `baseline_calibrated` - the validated Phase 1 geometry;
2. `eta_o_optimized` - optimized before exact-form evaluation under a frozen Gram-floor constraint;
3. `pole_balanced` - selected using `Phi_u(+1/2)`, `Phi_u(-1/2)`, and conditioning only;
4. `nonoptimized_control` - a fixed control geometry.

The exact node vectors and widths must be copied from existing validated repository artifacts before the run. No substitute geometry may be introduced after observing target-band values.

## Frequency ladder

The lower endpoint must be supplied as external metadata in the manifest. The first ladder is multiplicative rather than hand-picked:

```text
omega_k = omega_start * 2^(k/4),  k = 0,...,16
```

This spans four octaves with four points per octave. It is intentionally coarse.

Refinement is triggered only by thresholds already stored in the manifest. Each trigger produces the same fixed local stencil:

```text
omega * {1 - 2^-10, 1 - 2^-12, 1, 1 + 2^-12, 1 + 2^-10}
```

No additional frequency may be inserted during the run.

## Arithmetic precision

For each frequency, decimal precision is chosen before evaluation by

```text
dps = max(80, ceil(log10(omega)) + 60)
```

and the precision-doubling rerun uses `2*dps`.

This rule is intentionally conservative and independent of the observed eigenvalue.

## Prime cutoff rule

The exploratory cutoff must be generated from the actual section geometry. Let

```text
Delta_max = max_ij |x_i - x_j|.
```

The first floating-point pass uses

```text
log_cutoff = Delta_max + 11*sigma
```

or a stronger existing repository rule if already proved. The certified pass must replace this heuristic with the rigorous prime-tail routine required by the protocol.

The cutoff and resulting tail estimate are recorded for every section.

## Recorded observables

Every evaluation records:

- smallest generalized eigenvalue;
- Gram floor and condition number;
- odd susceptibility `eta_o`;
- even-sector pole response `r_e`;
- `Phi_u(+1/2)` and `Phi_u(-1/2)` for the minimizing state;
- residual norm;
- Hermitian defect;
- prime cutoff and estimated/certified tail;
- Archimedean quadrature settings and error estimate/enclosure;
- pole orientation test status;
- precision and implementation identifier;
- search index and total search count.

## Classification

The report generator may emit only one of:

- `calibration_failure`;
- `inadmissible_geometry`;
- `exploratory_float_positive`;
- `exploratory_float_warning`;
- `certified_survival_window`;
- `candidate_requires_independent_reproduction`;
- `certified_negative_reproduced`.

No free-form conclusion string is allowed.

## Trigger rules

The initial manifest must freeze numerical values for:

- floating warning threshold;
- verified proximity threshold;
- `eta_o` warning threshold;
- local descent threshold;
- minimum Gram floor;
- maximum allowed Hermitian defect;
- maximum tail-to-margin ratio.

A warning is not evidence of negativity. It authorizes only the fixed refinement stencil and precision-doubling schedule.

## Audit order for any negative-looking value

1. rerun the same manifest at doubled precision;
2. verify matrix orientation and Fourier conventions;
3. verify Gram whitening and generalized-eigenvalue residual;
4. increase prime cutoff under the same geometry;
5. tighten Archimedean quadrature;
6. compare with the independent implementation;
7. run interval certification;
8. only then interpret the sign.

## Required outputs

Each batch writes:

```text
artifacts/phase2/<run_id>/manifest.json
artifacts/phase2/<run_id>/sections.jsonl
artifacts/phase2/<run_id>/summary.json
artifacts/phase2/<run_id>/search_ledger.csv
artifacts/phase2/<run_id>/README.md
```

The summary must be generated entirely from machine fields.

## Immediate implementation queue

1. locate and freeze the validated Phase 1 modulated assembly entry point;
2. add immutable manifest parsing and hashing;
3. add a single-section high-precision runner;
4. add the frozen multiplicative ladder and refinement stencil;
5. add computed-only classification;
6. add regression tests for orientation, Hermitian symmetry, precision stability, and search accounting;
7. run the batch as `exploratory_float`;
8. do not promote any output until the certification gates are complete.
