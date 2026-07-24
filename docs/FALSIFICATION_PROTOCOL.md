# Protocol: certified finite Weil sections and exploratory RH falsification

## Status

This document is a preregistered research protocol for interval-certified finite-dimensional approximations of Weil's quadratic form, together with an explicitly one-way exploratory falsification program for the Riemann hypothesis.

The framework contribution is primary. The high-band sweep is exploratory and does not define a proving strategy for RH.

A reported violation is not a mathematical result until every certificate condition below is met and an independent implementation reproduces it.

## 1. Objective and logical asymmetry

Weil's criterion states that RH is equivalent to nonnegativity of the exact Weil quadratic form on every admissible test function. Consequently, a single admissible test function with a rigorously verified negative exact value would disprove RH.

Finite sampling cannot prove RH. Certified positive sections are recorded only as survival windows for the tested packet family.

The experiment therefore has a permanent asymmetry:

- one exact certified negative can falsify RH;
- any number of certified positive samples cannot prove RH.

A certified positive finite section establishes only that the implementation agrees with the exact criterion on that section within the stated enclosure. Inside a region already covered by independent zero computations, it adds essentially no new evidence for RH beyond those computations.

## 2. Framework claim and organizing principle

The central framework claim is numerical-analytic rather than conjectural:

> Geometry is the probe space; arithmetic is the state.

The packet geometry determines the finite test space and its conditioning. The explicit-formula assembly - prime powers, Archimedean contribution, pole term, and Gram normalization - determines the arithmetic quadratic form evaluated on that space.

The framework paper studies:

- exact finite-section formulas;
- interval-certified matrix assembly;
- rigorous truncation and quadrature bounds;
- generalized-eigenvalue verification;
- reproducible machine-readable certificates;
- calibration of the instrument response.

The high-band RH sweep is an application of this framework and is secondary to it.

## 3. Candidate section

A section is completely determined by a machine-readable manifest containing:

- packet nodes;
- Gaussian width `sigma`;
- modulation frequency `omega`;
- prime cutoff;
- working precision;
- quadrature parameters;
- Gram matrix convention;
- Fourier and reflection conventions;
- code commit SHA;
- implementation identifier;
- search index and total number of sections examined;
- the external zero-verification horizon metadata used to classify the band.

No parameter may be silently altered after a candidate is observed. Any refinement is a new run with a new manifest.

## 4. Certification requirements

A candidate negative must bound the exact form, not a finite floating-point truncation.

### 4.1 Truncated generalized eigenvalue

The assembled Hermitian matrix and Gram matrix must be enclosed by interval matrices. The smallest generalized eigenvalue must be bounded using a residual-based verification method, with all complex arithmetic enclosed.

The certificate must report:

- an upper bound for the candidate eigenvalue;
- a lower bound for the Gram floor;
- the residual enclosure;
- the verified spectral separation used by the method;
- the precision and directed-rounding backend.

### 4.2 Prime tail

The omitted prime-power contribution must be bounded entrywise and in operator norm using the actual section geometry. The cutoff must scale with the maximum packet difference, not with a reference geometry.

For Gaussian packets, the tail estimate must use the decay

\[
\exp\!\left(-\frac{(\log n-\Delta)^2}{4\sigma^2}\right)
\]

and a stated explicit prime-counting majorant. The implementation must record the exact inequality and constants used. A numerical tail estimate without a derivation is not a certificate.

### 4.3 Archimedean remainder

All numerical quadrature in the Archimedean term must be interval-enclosed. The certificate must distinguish:

- truncation of an infinite integral;
- discretization or quadrature error;
- special-function evaluation error.

### 4.4 Pole term

The pole contribution must be assembled from its exact closed form. It must not be estimated numerically when an exact packet formula is available. Orientation and transpose conventions must be tested at nonzero modulation, because errors can be invisible at `omega = 0`.

### 4.5 Exact negativity margin

Let `lambda_upper` be the verified upper bound for the truncated generalized eigenvalue and let

\[
E_{\mathrm{tail}},\quad E_{\infty},\quad E_{\mathrm{other}}
\]

be rigorous operator-norm bounds for all omitted or uncertain contributions after conversion through the verified Gram floor. A candidate is certified negative only if

\[
\lambda_{\mathrm{upper}}
+E_{\mathrm{tail}}
+E_{\infty}
+E_{\mathrm{other}}
<0.
\]

The reported margin is the negative of the left side.

## 5. Phase 1 - calibration of the instrument response

Phase 1 is a calibration program, not a falsification test and not evidence for RH.

Its purpose is to establish that the implementation reproduces known arithmetic spectral features and to measure the instrument response model used to interpret later scans.

No high-band run may begin until the current implementation passes all of the following:

1. reproduces the validated `omega = 0` reference assembly within its existing tolerance;
2. reproduces known moderate-height spectral features from arithmetic data alone;
3. resolves a known close pair when the width is sharpened sufficiently;
4. shows the expected loss of resolution under a deliberately broadened width;
5. passes orientation tests that fail after either matrix factor is transposed;
6. passes a Gram-conditioning stress test;
7. verifies that all conclusion labels are generated from computed interval signs rather than hardcoded text.

The legitimate Phase 1 outputs are:

- frequency response and resolution width;
- centroid behavior for unresolved pairs;
- splitting behavior as resolution improves;
- conditioning sensitivity;
- numerical agreement with known spectral data;
- a bug and convention ledger.

These results calibrate the spectrometer. They do not validate its behavior in regions without ground truth.

## 6. Literature and novelty discipline

High regions of the critical line are not unexplored territory. The project must not claim novelty from merely evaluating large `omega`.

Before publication, the framework paper must include a literature review covering at least:

- systematic verification of RH to large finite heights;
- large-scale zero computations and isolated high-window studies;
- prior numerical work on Weil's criterion and explicit-formula quadratic forms;
- interval or computer-assisted certification methods for related spectral problems.

The only plausible novelty claim is the observable and its certification architecture:

> interval-certified finite-dimensional Weil-section positivity or negativity with complete truncation, pole, Archimedean, conditioning, and reproduction accounting.

That claim remains provisional until the literature review is complete.

## 7. Phase 2 target band and role

Phase 2 is an exploratory appendix to the framework program, not the headline contribution.

The first exploratory target band begins strictly beyond the zero-verification horizon adopted by the project. The exact lower endpoint must be recorded in the manifest together with the source and date supporting that horizon.

No hardcoded claim about the current verified-zero horizon belongs in theorem-facing code. The value is external metadata and must be updated only through a documented protocol revision.

The initial design uses modulation frequencies on a coarse ladder, followed by local refinement only when a preregistered discriminator triggers.

A certified-positive window in territory already covered by independent zero computations is primarily a calibration or cross-check result. A certified-positive window outside that territory is still only a survival window for the sampled packet family.

## 8. Parameter design guided by the transform

The packet transform is

\[
\Phi_u(z)=\sum_i u(i)e^{zx_i}.
\]

The high-band design is not an unconstrained parameter search. It is guided by quantities already defined by the finite-section theory:

- odd-sector susceptibility `eta_o`;
- even-sector pole-channel response `r_e`;
- values and derivatives of `Phi_u` at the pole channels `z = +/-1/2`;
- Gram conditioning;
- packet resolution inferred from `sigma`;
- nondegeneracy of the translated family.

The first batch must include:

- a baseline geometry inherited from the calibrated section;
- an `eta_o`-optimized geometry subject to a preregistered Gram-floor constraint;
- a pole-channel-balanced geometry controlling both `Phi_u(1/2)` and `Phi_u(-1/2)`;
- a deliberately nonoptimized control geometry.

The optimizer may use only quantities available before evaluation of the final exact Weil form at the target frequency. This prevents direct fishing on the outcome variable.

Selection language must remain operational. The protocol does not say that the mathematics "points" to a region after seeing the result. It says that preregistered susceptibility, pole-channel, conditioning, and resolution criteria rank candidate sections before exact-form evaluation.

## 9. Search accounting

Every run must report:

- all frequencies attempted;
- all geometries attempted;
- all widths attempted;
- all optimizer seeds;
- all rejected sections and rejection reasons;
- the total number of exact-form evaluations;
- the total number of interval certifications.

Any reported candidate must include this search count. Local refinement around a trigger is part of the search count.

## 10. Trigger and refinement rules

A coarse-grid point triggers refinement only when one of the following preregistered conditions holds:

- the floating-point minimum eigenvalue crosses a fixed warning threshold;
- the verified upper bound enters a fixed proximity band around zero;
- `eta_o` crosses its fixed criticality warning threshold;
- two adjacent points display a sign-consistent local descent exceeding a fixed slope threshold.

The numerical thresholds belong in the Phase 2 manifest and may not be changed during the run.

A trigger authorizes a fixed refinement stencil and a fixed precision-doubling schedule. It does not authorize arbitrary parameter changes.

## 11. Negative-result precommitments

Any apparent negative is presumed to be a bug.

The audit order is:

1. implementation error;
2. orientation, Fourier-sign, or normalization error;
3. Gram whitening or conditioning failure;
4. interval-arithmetic misuse;
5. quadrature enclosure failure;
6. prime-tail or geometry-scaling gap;
7. manifest or search-accounting violation;
8. only then, the mathematical interpretation.

No candidate may be announced unless:

- a separately authored implementation reproduces it from the published manifest;
- both implementations rerun at doubled precision;
- both interval certificates verify exact negativity independently;
- the candidate survives orientation and normalization perturbation tests;
- the complete search ledger is published.

## 12. Null results

Every fully certified positive batch is recorded as a survival window for the tested family. The report must state explicitly that it cannot prove RH and that unsampled test functions remain unrestricted.

The report must also distinguish two cases:

- **inside independently checked zero territory:** primarily a calibration or framework cross-check;
- **outside independently checked zero territory:** a new certified survival window for this packet family, but not general evidence sufficient to establish RH.

The quantitative outputs remain scientifically useful:

- certified minimum-eigenvalue ladder;
- odd susceptibility ladder;
- even pole-channel ladder;
- transform-profile data;
- conditioning and resolution laws;
- empirical frequency-density law with rigorous numerical error bars where certification is complete.

## 13. Required implementation work

Phase 2 cannot be called certified until the repository contains:

- a complex-Hermitian interval generalized-eigenvalue verifier;
- interval enclosures for modulated Archimedean assembly;
- a geometry-aware rigorous prime-tail bound;
- exact pole-term assembly with nonzero-modulation orientation tests;
- immutable run manifests;
- an independent implementation interface;
- machine-generated reports whose conclusions derive only from certificate fields.

## 14. Stop conditions

A batch stops immediately if:

- calibration fails;
- the Gram floor falls below the preregistered admissibility threshold;
- any interval enclosure returns nonfinite bounds;
- the tail bound exceeds the allowed fraction of the warning margin;
- implementation outputs disagree beyond their certified overlap;
- the search ledger becomes incomplete.

Stopped batches are retained and reported. They are not silently rerun under modified rules.

## 15. Publication architecture

The repository's outputs are separated by claim type.

### Paper A - algebra generation

Primary claim type: proved mathematics.

Contents include the Gaussian packet geometry, exceptional-width analysis, shell-transform factorization, and local or fixed-shift generation theorems.

### Paper B - pole structure

Primary claim type: proved mathematics.

Contents include the exact pole matrix, packet pole channels, reflection structure, and the role of `Phi_u(+/-1/2)`.

### Paper C - certified finite-dimensional approximations of Weil's quadratic form

Primary claim type: interval-certified computational framework.

The abstract should state the organizing principle:

> Geometry is the probe space; arithmetic is the state.

Core contents:

- exact finite-section assembly;
- interval generalized-eigenvalue verification;
- prime-tail calculus;
- interval Archimedean quadrature;
- exact pole treatment;
- calibration and instrument-response measurements;
- reproducible certificate and audit architecture.

Phase 1 belongs in this paper as calibration. Phase 2 belongs only as an exploratory application or appendix unless it produces a separately reproducible mathematical event.

### Phase 2 reports

Primary claim type: reproducible numerical observation or certified survival window.

These reports must never be blended into theorem statements or described as cumulative proof evidence.

## 16. Interpretation

The finite geometry is a probe architecture. The arithmetic assembly is the tested state. Generation and transform nondegeneracy ensure that the probe family itself is not collapsing, but they do not imply positivity of the arithmetic form.

The experiment asks only whether a certified finite section can produce an exact negative Weil value. Its expected outcome is no violation.

The realistic primary product is the certified finite-section framework itself: its mathematics, interval architecture, response calibration, audit trail, and susceptibility and spectral ladders. High-band exploration is subordinate to that framework and must remain honest about what it can and cannot establish.
