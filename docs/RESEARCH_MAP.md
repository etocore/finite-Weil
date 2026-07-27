# Research map

This document is the project's claim ledger. A statement moves upward only when its proof or certificate is committed and reviewed.

| Claim | Current status | Required evidence | Next action |
|---|---|---|---|
| Gaussian packet Gram formula | Proved analytically | Written derivation and unit tests | Add proof to paper |
| Distinct translated Gaussian packets are linearly independent | Previously proved in project notes, not yet imported | Referee-ready proof | Reconstruct in paper |
| Symmetry of the implemented universal matrix `T_n` | Implemented and tested from explicit Gaussian correlations | Written proposition matching code notation | Add proof to paper |
| Finite identity `A_prime(N;D) = sum beta_D(n) T_n` | Exact by implemented definition; arithmetic tests added | Independent hand-derived matrix example | Add a worked example and theorem statement |
| Identification of `A_prime` with the classical explicit-formula prime term | Observed at machine precision (`paper/13_pole_cancellation.md`) | Entrywise agreement of the full assembly with independently computed zero-side matrices | Upgrade the floating-point comparison to an interval certificate |
| Completed-zeta pole matrix `P` | Implemented and tested from the derivation in `paper/12_pole_term.md` | Closed-form Laplace checks, rank/eigenvalue identities, zero-side regression test | Extend to other meromorphic completions |
| Deep-cutoff negativity for `D = 1` is the missing pole block | Observed (`paper/13_pole_cancellation.md`) | With-pole spectrum collapses to `~1e-5` at cutoff `1e7` | Certified budget now available via `paper/14_certified_prime_tail.md` |
| Entrywise prime-tail bound and eigenvalue-shift budget on fixed packet spaces | Proved (`paper/14_certified_prime_tail.md`); evaluated in floating point | Closed-form theorem, quadrature and refinement-domination tests | Directed-rounding enclosure of `lambda_min(B)` for full certification |
| Low-lying zeros are identifiable from finite prime data | Observed (`paper/15_zero_recovery.md`) | Matrix-pencil recovery of the first 14 zeta zeros with envelope-consistent amplitudes | Extend to quadratic characters and study noise limits |
| Small-bandwidth positivity within certified truncation budget | Observed (`paper/16_small_sigma_regime.md`) | Sigma sweep with certified cutoffs and zero-side comparison | Szego-type limit of the whitened Toeplitz spectra |
| Primitive quadratic character arithmetic | Implemented and tested for representative discriminants | Broader reference-value tests | Add exhaustive small-conductor checks |
| Complete finite Weil operator decomposition | Historical, not reconstructed | Conductor term, gamma term, exact definitions, proof, regression tests | Resolve normalization issue #2 |
| Generalized eigenvalue perturbation bound | Standard finite-dimensional result; project specialization not yet imported | Precise hypotheses and proof | Add theorem module and paper section |
| Dirichlet pair interval perturbation certificate | Historical computational result, not reproduced here | Source code, machine-readable certificate, independent rerun | Import and audit old bundle |
| Approximate law `lambda_min = log(q) - D` | Numerical observation | Broader conductor sweep and uncertainty analysis | Implement experiment driver only after full operator audit |
| Bandwidth robustness of `D(sigma, q)` | Unknown | Joint sigma-conductor phase diagram | Primary experiment after normalization freeze |
| Infinite-dimensional limit or RH/GRH implication | Open and unclaimed | New theorem, not numerical extrapolation | Do not imply from finite data |

## Status vocabulary

- **Proved**: a complete mathematical proof is present in the repository.
- **Certified**: a finite computational statement has a reproducible, machine-checkable enclosure.
- **Observed**: a floating-point experiment has been reproduced but is not a theorem.
- **Historical**: reported by an earlier project artifact but not yet reconstructed here.
- **Open**: no proof or certificate currently exists.
