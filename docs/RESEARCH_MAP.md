# Research map

This document is the project's claim ledger. A statement moves upward only when its proof or certificate is committed and reviewed.

| Claim | Current status | Required evidence | Next action |
|---|---|---|---|
| Gaussian packet Gram formula | Proved analytically | Written derivation and unit tests | Add proof to paper |
| Distinct translated Gaussian packets are linearly independent | Previously proved in project notes, not yet imported | Referee-ready proof | Reconstruct in paper |
| Universal prime-power operator decomposition | Previously proved in project notes, not yet imported | Exact definitions, theorem, proof, regression tests | Rebuild normalization from source artifacts |
| Generalized eigenvalue perturbation bound | Standard finite-dimensional result; project specialization not yet imported | Precise hypotheses and proof | Add theorem module and paper section |
| Dirichlet pair interval perturbation certificate | Historical computational result, not reproduced here | Source code, machine-readable certificate, independent rerun | Import and audit old bundle |
| Approximate law lambda_min = log(q) - D | Numerical observation | Broader conductor sweep and uncertainty analysis | Implement experiment driver |
| Bandwidth robustness of D(sigma, q) | Unknown | Joint sigma-conductor phase diagram | Primary experiment |
| Infinite-dimensional limit or RH/GRH implication | Open and unclaimed | New theorem, not numerical extrapolation | Do not imply from finite data |

## Status vocabulary

- **Proved**: a complete mathematical proof is present in the repository.
- **Certified**: a finite computational statement has a reproducible, machine-checkable enclosure.
- **Observed**: a floating-point experiment has been reproduced but is not a theorem.
- **Historical**: reported by an earlier project artifact but not yet reconstructed here.
- **Open**: no proof or certificate currently exists.
