# Finite Weil

Finite Weil is a research codebase for finite-dimensional restrictions of Weil explicit-formula forms attached to completed L-functions.

The project distinguishes five kinds of statements:

1. proved mathematical statements;
2. exact finite identities implemented in code;
3. interval-certified computational statements;
4. reproducible floating-point observations;
5. open conjectures and research questions.

This repository does **not** claim a proof of RH or GRH. Its current scope is finite-dimensional spectral mathematics, explicit-formula assembly, perturbation bounds, inverse recovery experiments, and the development of rigorous computational methods.

## Current mathematical baseline

For primitive non-principal quadratic characters, the implemented finite matrix is assembled from conductor, gamma-factor, and truncated prime-power contributions. For the principal character `D = 1`, the completed zeta function is meromorphic, so the mathematically correct default assembly also includes the rank-two pole matrix derived in `paper/12_pole_term.md`.

The default `WeilOperator` behavior is therefore:

- include the pole block automatically for `D = 1`;
- omit it for non-principal primitive quadratic characters;
- require an explicit `include_pole=False` only for labeled historical reproductions of the earlier pole-free zeta computations.

The large negative `D = 1` spectra reported in the early cutoff studies were produced by that historical pole-free assembly. They are retained only as reproducible diagnostics of the omitted pole term and must not be interpreted as spectra of the completed-zeta Weil form. The corrected assembly is compared with independently reconstructed zero-side matrices in papers 13 and 15 and in the committed experiment artifacts.

## Current research program

The active program includes:

- auditing the explicit-formula normalization and all downstream claims;
- proving and numerically evaluating fixed-packet prime-tail bounds;
- recovering low-lying zero frequencies from finite prime data;
- tracking complex pencil modes as a structural diagnostic for off-unit-circle behavior;
- studying the small-bandwidth and Toeplitz regimes without claiming an infinite-dimensional limit theorem;
- replacing floating-point truncation budgets with directed-rounding enclosures where full certification is required.

The canonical claim ledger is `docs/RESEARCH_MAP.md`. The repository-wide correction rules and audit progress are recorded in `docs/REPOSITORY_AUDIT.md`.

## Run experiments locally

Create a Python 3.11 or newer environment, then install the package with its experiment dependencies:

```bash
python -m pip install -e ".[experiments]"
```

The repository contains several independent experiment drivers. Their outputs are floating-point observations unless the relevant paper and artifact explicitly state that every numerical step has been rigorously enclosed. In particular, evaluating a proved analytic tail-bound formula in ordinary floating point is not itself an interval certificate.

The original convergence sweep remains available through:

```bash
python -m experiments.run
```

For `D = 1`, interpret historical sweep outputs according to the script's explicit pole setting and the correction notices in the associated papers. Current zeta experiments should use the automatic pole-inclusive default.

## Repository layout

- `finite_weil/` - mathematical implementation
- `tests/` - tests for definitions, identities, regressions, and failure paths
- `experiments/` - reproducible numerical studies
- `paper/` - theorem statements, derivations, observations, and open problems
- `paper/data/` - committed numerical artifacts quoted by the papers
- `certificates/` - machine-readable rigorous certificates, when available
- `docs/` - claim ledger, assumptions, audit notes, and research maps

## Development rule

Every theorem-facing implementation should have:

- an explicit mathematical statement;
- documented hypotheses and normalization conventions;
- a corresponding test or independent verification path;
- a clear distinction between exact identities, proved inequalities, floating-point evaluations, and rigorous numerical enclosures;
- explicit historical labeling when reproducing a superseded computation.

No downstream document should cite a historical pole-free `D = 1` result as evidence about the completed-zeta Weil form.
