# Finite Weil

Finite Weil is a research codebase for finite-dimensional compressions of Weil explicit-formula operators attached to completed L-functions.

The project is organized around four distinct kinds of claims:

1. proved mathematical statements;
2. interval-certified computational theorems;
3. reproducible numerical observations;
4. open conjectures and research questions.

This repository does **not** claim a proof of RH or GRH. Its present scope is finite-dimensional spectral mathematics, perturbation theory, explicit-formula computations, and computer-assisted verification.

## Immediate research program

The first milestone is a clean reconstruction of the Gaussian packet model and the finite prime-operator decomposition. The first large experiment will measure

\[
D(\sigma,q)=\lambda_{\min}(\sigma,q)-\log q
\]

across packet bandwidths and primitive quadratic characters.

## Run the convergence experiment locally

Create a Python 3.11 or newer environment, then install the package with its experiment dependencies:

```bash
python -m pip install -e ".[experiments]"
```

Run the default local sweep and generate the CSV plus all plots with one command:

```bash
python -m experiments.run
```

The default `quick` profile evaluates 90 parameter combinations. The full 300-case sweep is:

```bash
python -m experiments.run --profile full
```

Results are written to `artifacts/convergence.csv` and one PNG for each discriminant/sigma slice. These are floating-point numerical observations, not certified results and not evidence for RH or GRH.

## Repository layout

- `finite_weil/` - mathematical implementation
- `tests/` - tests corresponding to definitions and proved identities
- `experiments/` - reproducible numerical studies
- `paper/` - theorem statements and proofs
- `certificates/` - machine-readable interval certificates
- `docs/` - research map, assumptions, and implementation notes

## Development rule

Every theorem-facing implementation should have:

- an explicit mathematical statement;
- a corresponding test;
- documented hypotheses;
- a clear distinction between floating-point evidence and certified computation.

## Status

The repository is being rebuilt from first principles. Historical scripts will be imported only after their normalization and assumptions are audited.
