# Research map

This document is the project's current claim ledger. Historical interpretations superseded by later work are recorded in `docs/CORRECTION_LEDGER.md` and must not be cited as current claims.

A statement moves upward only when its proof, reproducible artifact, or certificate is committed and reviewed.

| Claim | Current status | Evidence in repository | Next action |
|---|---|---|---|
| Gaussian packet Gram formula | Proved analytically | Written derivation and unit tests | Consolidate into a referee-facing foundation chapter |
| Distinct translated Gaussian packets are linearly independent | Proved in project work, not yet consolidated | Existing project notes and downstream use | Import a complete proof into the paper sequence |
| Symmetry of the implemented universal matrix `T_n` | Implemented and tested | Explicit Gaussian correlation formula and tests | Add a theorem statement matching code notation |
| Finite identity `A_prime(N;D) = sum beta_D(n) T_n` | Exact by definition | Implementation and arithmetic tests | Add an independent worked matrix example |
| Identification of the arithmetic assembly with the classical explicit formula on tested packet spaces | Observed at machine precision | `paper/13_pole_cancellation.md`, `experiments/dirichlet_zero_side.py`, and `paper/data/dirichlet-zero-side.csv` | Replace floating-point comparisons with interval enclosures |
| Completed-zeta pole matrix `P` | Proved and implemented | `paper/12_pole_term.md`, `finite_weil/poles.py`, and regression tests | Extend the data model to other meromorphic completed functions |
| Historical deep-cutoff negativity for `D = 1` is caused by omission of `P` | Numerically resolved | `paper/13_pole_cancellation.md`, corrected default API, and committed pole-cancellation artifact | Add an interval-enclosed cancellation example |
| Entrywise prime-tail inequality on each fixed Gaussian packet space | Proved | `paper/14_certified_prime_tail.md` and `finite_weil/tail_bounds.py` | Evaluate the full bound chain with directed rounding |
| Generalized-eigenvalue perturbation budget from the prime tail | Proved formula, floating-point evaluated | Paper 14, implementation, quadrature and refinement-domination tests | Interval-enclose Gram entries, `erfc`, row sums, `lambda_min(B)`, and the final quotient |
| Low zeta ordinates are recoverable from finite arithmetic-side samples | Reproducible observation | `paper/15_zero_recovery.md`, tests, and `paper/data/zero-recovery.csv` | Quantify stability, mode separation, and sensitivity to off-circle components |
| Complex pencil modes can represent off-unit-circle behavior | Demonstrated on synthetic data | Off-circle control test and decay-rate output | Derive a forward model and detection bounds for hypothetical off-critical contributions |
| Small-bandwidth spectra track visible zero mass | Reproducible observation | `paper/16_small_sigma_regime.md` and `paper/data/sigma-scaling.csv` | Prove an appropriate Toeplitz or Szegő-type limit theorem |
| Toeplitz negative-symbol-dip formulation of RH failure | Conjectural bridge only | Missing-step list in papers 16 and the correction ledger | Prove sampled-kernel, Hermitian-symbol, smoothing, finite-section, and aliasing steps |
| Primitive quadratic character arithmetic | Implemented and tested for representative discriminants | Unit tests and five-character zero-side artifact | Add broader small-conductor reference checks |
| Finite variational interpretation of `(A,B)` | Proved | `paper/11_variational_foundation.md` | Update application notation everywhere to include the pole term when meromorphic |
| Infinite-dimensional Weil operator represented by the packet limit | Open and unclaimed | Finite variational theory explicitly stops short of this | Establish a dense domain, convergence, semiboundedness, and closability before operator language |
| Dirichlet pair interval perturbation certificate | Historical and not yet reconstructed | Earlier project artifact only | Import source, certificate, and independent rerun before citing |
| Approximate law `lambda_min = log(q) - D` | Historical numerical observation, not part of the current validated program | No current theorem or corrected broad sweep | Reassess only after corrected operator and error budgets are used throughout |
| Bandwidth robustness of `D(sigma,q)` | Open and currently deprioritized | None | Reframe in terms of visible zero mass and corrected completed-function assembly |
| RH or GRH implication from finite numerics | Open and unclaimed | None | Do not imply from finite agreement, positivity, or recovered critical-line ordinates |

## Status vocabulary

- **Proved**: a complete mathematical proof is present in the repository.
- **Certified**: a finite computational statement has a reproducible machine-checkable enclosure using rigorous arithmetic.
- **Observed**: a floating-point experiment has been reproduced and its parameters or artifact are committed.
- **Historical**: an earlier result retained for provenance or reproduction but not accepted as a current claim.
- **Conjectural**: a precise proposed bridge whose missing proof obligations are listed.
- **Open**: no proof or sufficient computational evidence currently exists.

## Repository-wide claim rules

1. Every `D = 1` completed-zeta assembly includes the pole block unless a script explicitly declares itself historical.
2. Historical pole-free negative spectra may not be called Weil-negative directions or counterexample candidates.
3. A proved formula evaluated in ordinary floating point is not a certified numerical enclosure.
4. Positivity of a zero-side matrix built from critical-line ordinates is structural and is not an independent test of RH.
5. Complex pencil decay rates provide a representation and diagnostic, not a validated off-critical-zero detector.
6. Collision and flat-limit packet geometry may be cited independently, but not as evidence for a disproved negative-direction interpretation.
