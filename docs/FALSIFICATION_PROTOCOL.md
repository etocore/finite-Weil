# Protocol: attempting to falsify RH with certified finite Weil sections

## Status

This document is a preregistered research protocol. It defines a one-way falsification experiment for the Riemann hypothesis using certified finite sections of Weil's quadratic form. It does not define a proving strategy for RH.

A reported violation is not a mathematical result until every certificate condition below is met and an independent implementation reproduces it.

## 1. Objective and logical asymmetry

Weil's criterion states that RH is equivalent to nonnegativity of the exact Weil quadratic form on every admissible test function. Consequently, a single admissible test function with a rigorously verified negative exact value would disprove RH.

Finite sampling cannot prove RH. Certified positive sections are recorded only as survival windows for the tested packet family.

The experiment therefore has a permanent asymmetry:

- one exact certified negative can falsify RH;
- any number of certified positive samples cannot prove RH.

## 2. Candidate section

A Phase 2 section is completely determined by a machine-readable manifest containing:

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
- search index and total number of sections examined.

No parameter may be silently altered after a candidate is observed. Any refinement is a new run with a new manifest.

## 3. Certification requirements

A candidate negative must bound the exact form, not a finite floating-point truncation.

### 3.1 Truncated generalized eigenvalue

The assembled Hermitian matrix and Gram matrix must be enclosed by interval matrices. The smallest generalized eigenvalue must be bounded using a residual-based verification method, with all complex arithmetic enclosed.

The certificate must report:

- an upper bound for the candidate eigenvalue;
- a lower bound for the Gram floor;
- the residual enclosure;
- the verified spectral separation used by the method;
- the precision and directed-rounding backend.

### 3.2 Prime tail

The omitted prime-power contribution must be bounded entrywise and in operator norm using the actual section geometry. The cutoff must scale with the maximum packet difference, not with a reference geometry.

For Gaussian packets, the tail estimate must use the decay

\[
\exp\!\left(-\frac{(\log n-\Delta)^2}{4\sigma^2}\right)
\]

and a stated explicit prime-counting majorant. The implementation must record the exact inequality and constants used. A numerical tail estimate without a derivation is not a certificate.

### 3.3 Archimedean remainder

All numerical quadrature in the archimedean term must be interval-enclosed. The certificate must distinguish:

- truncation of an infinite integral;
- discretization or quadrature error;
- special-function evaluation error.

### 3.4 Pole term

The pole contribution must be assembled from its exact closed form. It must not be estimated numerically when an exact packet formula is available. Orientation and transpose conventions must be tested at nonzero modulation, because errors can be invisible at `omega = 0`.

### 3.5 Exact negativity margin

Let `lambda_upper` be the verified upper bound for the truncated generalized eigenvalue and let

\[
E_{\mathrm{tail}},\quad E_{\infty},\quad E_{\mathrm{other}}
\]

be rigorous operator-norm bounds for all omitted or uncertain contributions after conversion through the verified Gram floor. A candidate is certified negative only if

\[
\lambda_{\mathrm{upper}}
+
E_{\mathrm{tail}}
+
E_{\infty}
+
E_{\mathrm{other}}
<0.
\]

The reported margin is the negative of the left side.

## 4. Calibration gate

No high-band run may begin until the current implementation passes all of the following:

1. reproduces the validated `omega = 0` reference assembly within its existing tolerance;
2. reproduces known moderate-height spectral features from arithmetic data alone;
3. resolves a known close pair when the width is sharpened sufficiently;
4. shows the expected loss of resolution under a deliberately broadened width;
5. passes orientation tests that fail after either matrix factor is transposed;
6. passes a Gram-conditioning stress test;
7. verifies that all conclusion labels are generated from computed interval signs rather than hardcoded text.

These are calibration tests, not evidence for RH.

## 5. Phase 2 target band

The first exploratory target band begins strictly beyond the zero-verification horizon used by the project. The exact lower endpoint must be recorded in the manifest together with the source and date supporting that horizon.

No hardcoded claim about the current verified-zero horizon belongs in theorem-facing code. The value is external metadata and must be updated only through a documented protocol revision.

The initial design uses modulation frequencies on a coarse ladder, followed by local refinement only when a preregistered discriminator triggers.

## 6. Parameter design guided by the transform

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

## 7. Search accounting

Every run must report:

- all frequencies attempted;
- all geometries attempted;
- all widths attempted;
- all optimizer seeds;
- all rejected sections and rejection reasons;
- the total number of exact-form evaluations;
- the total number of interval certifications.

Any reported candidate must include this search count. Local refinement around a trigger is part of the search count.

## 8. Trigger and refinement rules

A coarse-grid point triggers refinement only when one of the following preregistered conditions holds:

- the floating-point minimum eigenvalue crosses a fixed warning threshold;
- the verified upper bound enters a fixed proximity band around zero;
- `eta_o` crosses its fixed criticality warning threshold;
- two adjacent points display a sign-consistent local descent exceeding a fixed slope threshold.

The numerical thresholds belong in the Phase 2 manifest and may not be changed during the run.

A trigger authorizes a fixed refinement stencil and a fixed precision-doubling schedule. It does not authorize arbitrary parameter changes.

## 9. Negative-result precommitments

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

## 10. Null results

Every fully certified positive batch is recorded as a survival window for the tested family. The report must state explicitly that it is not evidence sufficient to prove RH and that unsampled test functions remain unrestricted.

The quantitative outputs remain scientifically useful:

- certified minimum-eigenvalue ladder;
- odd susceptibility ladder;
- even pole-channel ladder;
- transform-profile data;
- conditioning and resolution laws;
- empirical frequency-density law with rigorous numerical error bars where certification is complete.

## 11. Required implementation work

Phase 2 cannot be called certified until the repository contains:

- a complex-Hermitian interval generalized-eigenvalue verifier;
- interval enclosures for modulated archimedean assembly;
- a geometry-aware rigorous prime-tail bound;
- exact pole-term assembly with nonzero-modulation orientation tests;
- immutable run manifests;
- an independent implementation interface;
- machine-generated reports whose conclusions derive only from certificate fields.

## 12. Stop conditions

A batch stops immediately if:

- calibration fails;
- the Gram floor falls below the preregistered admissibility threshold;
- any interval enclosure returns nonfinite bounds;
- the tail bound exceeds the allowed fraction of the warning margin;
- implementation outputs disagree beyond their certified overlap;
- the search ledger becomes incomplete.

Stopped batches are retained and reported. They are not silently rerun under modified rules.

## 13. Interpretation

The finite geometry is a probe architecture. The arithmetic assembly is the tested state. Generation and transform nondegeneracy ensure that the probe family itself is not collapsing, but they do not imply positivity of the arithmetic form.

The experiment asks only whether a certified finite section can produce an exact negative Weil value. Its expected outcome is no violation. Its realistic products are the instrument, its audit trail, and the certified susceptibility and spectral ladders.