# Repository consistency audit

This file records the repository-wide audit initiated after the completed-zeta pole correction and the subsequent review fixes.

The audit treats every mathematical statement, implementation comment, experiment, artifact, and cross-reference as requiring one of the following explicit statuses:

- **Proved**: a complete proof is present in the repository.
- **Exact implementation**: the code matches a stated finite definition or identity.
- **Observed**: supported by a committed floating-point experiment, but not proved.
- **Historically reproduced**: retained to reproduce an earlier computation whose mathematical interpretation has been superseded.
- **Open**: conjectural or not yet established.

The principal correction governing this audit is that the completed zeta function requires the rank-two pole block. Any `D = 1` result computed with `include_pole=False` is historical pole-free data and must not be cited as the spectrum of the completed-zeta Weil form.

## Audit rules

1. Every current `D = 1` assembly must include the pole block automatically or explicitly.
2. Historical pole-free scripts must set `include_pole=False` explicitly and label their output as historical.
3. No floating-point result may be called certified unless every numerical step is enclosed with directed rounding or an equivalent rigorous method.
4. Every claimed experiment must have a committed script and either a regression test or a committed result artifact with its evidentiary status stated.
5. Downstream papers must not use superseded negative spectra as evidence about Weil positivity.
6. Off-critical zeros must be modeled through complex exponential modes, not merely anomalous cosine amplitudes.
7. Toeplitz and symbol-limit statements remain conjectural until the required sampling, smoothing, finite-section, and aliasing arguments are proved.

## File ledger

| File | Audit status | Principal findings | Action |
|---|---|---|---|
| `README.md` | First pass complete | Original future-work description and pole-free baseline were stale | Rewritten to state the corrected operator and current claim boundary |
| `finite_weil/weil_operator.py` | First pass complete | Module docstring still described a three-term operator | Corrected to distinguish principal four-term and non-principal three-term assemblies |
| `paper/09_prime_cutoff_geometry.md` | Deep audit complete | Negative table was unlabeled pole-free data; "exact" overstated floating-point spectra; early drift and limiting negativity were conflated; dimension dependence was called unresolved after the pole explanation; tail-bound work was still described as future | Rewritten line by line, historical data quarantined, corrected comparison added, surviving geometric claim narrowed, Paper 14 linked, dependency map added |

## Paper 9 findings in detail

The following propositions survived review:

- Gaussian packet-pair entries are localized near logarithmic prime scales matching the center separation.
- A cutoff with `log(N) < 2E` ends before some packet-pair Gaussian envelope centers when centers lie in `[-E,E]`.
- Cutoff refinement and packet-space refinement are distinct operations.
- Shallow common cutoffs can compare differently resolved packet spaces.

The following statements were superseded or narrowed:

- The large negative eigenvalues do not belong to the corrected completed-zeta operator.
- Stabilization over the final sampled cutoff interval is not a proof of convergence.
- The phrase "exact deep-cutoff experiment" was inaccurate for floating-point eigenspectra.
- Insufficient arithmetic depth explains early cutoff drift, but not the limiting negative spectrum.
- The dimension dependence is explained primarily by the Gram representation of the omitted rank-two pole block.
- The heuristic `log(N) >> 2E` is not a quantitative error rule.
- Derivation of a prime-tail estimate is completed in Paper 14 and is no longer future work.

## Progress rule

A checked file is not considered complete until its mathematics, code references, temporal language, artifacts, and downstream citations have all been reviewed. Paper 9 is complete at the source-file level; its downstream uses will be rechecked during the audits of Papers 10 through 16.
