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