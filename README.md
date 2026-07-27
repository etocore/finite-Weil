# Finite Weil

Finite Weil is a research codebase for finite-dimensional compressions of Weil explicit-formula forms attached to completed L-functions.

The project distinguishes four kinds of statements:

1. proved mathematical statements;
2. interval-certified computational statements;
3. reproducible floating-point observations;
4. open conjectures and research questions.

This repository does **not** claim a proof of RH or GRH. Its present scope is finite-dimensional spectral mathematics, explicit-formula computation, perturbation theory, Gaussian packet geometry, and computer-assisted validation.

## Current validated picture

For a primitive quadratic character, the implemented finite matrix is assembled from the conductor, gamma, and prime contributions. For the principal character `D = 1`, the completed zeta function also contributes the rank-at-most-two pole block

\[
P_{ij}=4\pi\sigma^2e^{\sigma^2/4}\cosh\!\left(\frac{c_i-c_j}{2}\right).
\]

`WeilOperator` includes this block automatically for `D = 1`. Historical scripts that reproduce the old pole-free chapter 8/9 tables opt out explicitly.

The earlier large negative deep-cutoff eigenvalues for `D = 1` were not negative Weil certificates. They were the spectral signature of omitting this analytically required pole block. The corrected arithmetic-side matrices agree with independently assembled zero-side matrices to floating-point precision for the tested characters.

The repository also contains:

- an explicit analytic bound for the omitted prime tail on each fixed Gaussian packet space;
- complex-mode matrix-pencil recovery of low zeta ordinates from the arithmetic side;
- small-bandwidth scaling experiments with floating-point evaluations of the analytic truncation budget;
- collision and flat-limit results for degenerating Gaussian packet families.

## Claim boundaries

- The prime-tail inequality is proved analytically, but its numerical evaluation currently uses ordinary floating point rather than directed rounding.
- Zero-side agreement and zero recovery are reproducible numerical observations, not interval certificates.
- Complex pencil modes can represent off-unit-circle behavior, but the repository does not claim a quantified detector for off-critical zeros.
- Finite positivity or negativity does not by itself establish an infinite-dimensional statement.

## Install and test

Create a Python 3.11 or newer environment, then install the package with experiment dependencies:

```bash
python -m pip install -e ".[experiments]"
```

Run the test suite:

```bash
python -m pytest
```

Run the current principal experiments:

```bash
python -m experiments.pole_cancellation
python -m experiments.dirichlet_zero_side
python -m experiments.zero_recovery
python -m experiments.sigma_scaling
```

Historical convergence and deep-cutoff scripts remain available for reproduction, but their `D = 1` outputs are intentionally pole-free and must not be interpreted as the completed-zeta Weil form.

## Repository layout

- `finite_weil/` - mathematical implementation
- `tests/` - tests corresponding to definitions and proved identities
- `experiments/` - reproducible numerical studies
- `paper/` - theorem statements, proofs, historical chapters, and numerical reports
- `paper/data/` - committed run records for quoted numerical tables
- `certificates/` - machine-readable interval certificates, where available
- `docs/` - research map, correction ledger, assumptions, and implementation notes

## Development rule

Every theorem-facing implementation should have:

- an explicit mathematical statement;
- a corresponding test;
- documented hypotheses;
- a clear distinction between proof, floating-point evidence, and interval certification;
- an explicit supersession note when later work invalidates an earlier interpretation.

The repository preserves historical artifacts for reproducibility, but current claims are governed by `docs/RESEARCH_MAP.md` and `docs/CORRECTION_LEDGER.md`.
