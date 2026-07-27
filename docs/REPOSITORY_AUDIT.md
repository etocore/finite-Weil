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

## Progress

The detailed file-by-file ledger will be expanded during the audit. A checked file is not considered complete until its mathematics, code references, temporal language, and downstream citations have all been reviewed.
