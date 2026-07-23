# Spectral Research Program for Finite Weil Theory

## 1. Purpose and status

This chapter is a research agenda. It contains conjectures, computational questions, and proposed experiments. Unless explicitly labeled otherwise, nothing here is claimed as a theorem.

The governing principle is to extract mathematically meaningful information from finite restrictions of the Weil form without overstating what finite numerics can prove about the Riemann hypothesis or generalized Riemann hypotheses.

## 2. Primary computational object

For a primitive quadratic character \(\chi\), a packet family \(V_N\), and a prime cutoff \(X\), define a finite Hermitian matrix

\[
A_{N,X}
=
A_{\mathrm{cond},N}
+
A_{\Gamma,N}
+
A_{\mathrm{prime},N,X}.
\]

Let \(B_N\) be the packet Gram matrix. The basis-independent finite spectrum is the generalized spectrum of

\[
A_{N,X}v=\lambda B_Nv.
\]

The first diagnostic quantity is

\[
\lambda_{\min}(N,X)
=
\min_{v\ne0}
\frac{v^*A_{N,X}v}{v^*B_Nv}.
\]

This quantity should always be reported together with conditioning and truncation diagnostics.

## 3. Baseline experiment matrix

Initial experiments should vary four independent parameters:

1. character discriminant \(D\);
2. packet dimension \(N\);
3. packet width and center geometry;
4. prime cutoff \(X\).

Suggested baseline characters include

\[
D\in\{1,-3,5,8,12,13,17,24,29\}.
\]

The inclusion of \(D=1\) provides the trivial primitive quadratic character and a bridge to the zeta setting, subject to the precise completed-function convention used by the package.

## 4. Experiment A: cutoff stabilization

### Question

For fixed \(N\) and packet geometry, does

\[
\lambda_{\min}(N,X)
\]

stabilize as \(X\to\infty\)?

### Measurements

Record:

- successive differences in \(\lambda_{\min}\);
- operator-norm differences between consecutive matrices;
- prime-tail estimates where available;
- runtime and number of prime powers included.

### Interpretation

Stable digits without a rigorous tail bound are a numerical observation, not a certificate. Failure to stabilize may indicate an insufficient cutoff, an incorrect normalization, or a genuinely sensitive trial direction.

## 5. Experiment B: space enrichment

### Question

For a nested or explicitly controlled sequence \(V_N\), how does

\[
\lambda_{\min}(N,X)
\]

change with \(N\)?

For nested spaces and an exact fixed form, the variational minimum should be nonincreasing. Any violation is a diagnostic for one of the following:

- spaces are not nested;
- cutoffs or quadratures changed with \(N\);
- matrix assembly is inconsistent;
- numerical conditioning is corrupting the generalized eigenproblem.

### Required plots

Plot separately:

- \(\lambda_{\min}\) versus \(N\);
- \(\kappa(B_N)\) versus \(N\);
- residual norm of the minimizing generalized eigenpair;
- sensitivity under orthonormalization.

## 6. Experiment C: basis comparison

Gaussian packets are a computational starting point, not a privileged basis.

Candidate alternatives include:

- Hermite functions;
- multiscale Gaussian frames;
- compactly supported wavelets;
- prolate spheroidal wave functions;
- adaptive dictionaries learned from approximate minimizing directions.

### Comparison criteria

A basis should be judged by:

- approximation error per degree of freedom;
- Gram conditioning;
- sparsity or structure of each operator component;
- quadrature cost;
- stability of generalized spectra;
- availability of rigorous tail estimates.

### Conjecture 6.1

There exists a basis in which the Archimedean contribution is substantially more diagonal than in translated Gaussian packets while the prime contribution remains computationally tractable.

## 7. Experiment D: Archimedean-arithmetic competition

Decompose the Rayleigh quotient of a candidate direction \(v\) into

\[
\mathcal R(v)
=
\mathcal R_{\mathrm{cond}}(v)
+
\mathcal R_{\Gamma}(v)
+
\mathcal R_{\mathrm{prime}}(v).
\]

For the minimizing finite direction, report each component separately.

This answers a more informative question than positivity alone:

> Which scales and frequencies make the arithmetic term most capable of overcoming the Archimedean contribution?

The minimizing vector should also be reconstructed as a physical-space and Fourier-space test function.

## 8. Experiment E: parity and conductor scaling

The gamma weight depends on parity, while the conductor term contributes

\[
\log(q/\pi)B_N.
\]

Study normalized operators such as

\[
A_{N,X}-\log(q/\pi)B_N
\]

across characters of the same parity and differing conductor.

### Question

After removing the scalar conductor shift, do spectra for different primitive quadratic characters exhibit common statistical or geometric features?

Any observed universality must be distinguished from artifacts of shared packet geometry or cutoff selection.

## 9. Experiment F: minimizing directions

A negative or near-zero generalized eigenvalue is only the beginning. The associated coefficient vector should be converted into the actual test function

\[
f_N=\sum_j v_j\varphi_j.
\]

Analyze:

- localization in physical space;
- localization in Fourier space;
- sign and oscillation pattern;
- sensitivity to packet width;
- contribution of each prime power;
- persistence under basis enrichment.

A robust direction should survive moderate perturbations in all numerical choices.

## 10. Search for finite negative certificates

Weil's criterion suggests a black-swan search: one valid admissible test function with negative Weil form would disprove the relevant hypothesis.

The finite program can search for candidate directions, but a candidate becomes a certificate only after all of the following are proved:

1. the reconstructed test function belongs to the admissible class;
2. the infinite prime contribution is rigorously enclosed;
3. the gamma integral is rigorously enclosed;
4. basis and quadrature errors are bounded;
5. the final upper bound for the full Weil form is strictly negative.

Until then, a negative finite eigenvalue is a lead, not a disproof.

## 11. Certified positivity program

The opposite direction is also useful. For a fixed finite space, one can seek a rigorous lower bound

\[
A_{N,X}\succeq \eta B_N
\]

for some explicit \(\eta\).

A certificate may combine:

- interval matrix entries;
- Cholesky or LDL factorization with directed rounding;
- perturbation bounds;
- generalized Gershgorin estimates;
- verified eigenvalue enclosures.

Such a result proves positivity only on the stated finite space and for the rigorously controlled infinite form.

## 12. Trace and determinant observables

Once the generalized operator is well-conditioned, investigate finite observables such as

\[
\operatorname{tr}(B_N^{-1}A_N),
\]

regularized determinants, and heat traces

\[
\operatorname{tr}\exp(-tB_N^{-1}A_N).
\]

### Open problem 12.1

Determine whether appropriately renormalized finite trace observables recover known zero-counting or explicit-formula quantities in a stable limit.

Naive determinants are basis-sensitive and numerically unstable; every proposed observable must be formulated invariantly with respect to the Gram metric.

## 13. Inverse problem

The forward map is schematically

\[
\chi\longmapsto Q_\chi\longmapsto\{(A_N,B_N)\}_N.
\]

The inverse problem asks what arithmetic data can be recovered from a family of finite restricted forms.

Potential targets include:

- conductor;
- parity;
- low prime coefficients;
- character values on prime powers;
- equivalence or distinguishability of characters from finite spectral data.

### Conjecture 13.1

For sufficiently rich packet families and sufficiently many cutoff levels, the arithmetic prime-power coefficients are identifiable from the matrix family up to the natural symmetries of the explicit formula.

This is not currently proved.

## 14. Reproducibility standard

Every published experiment should record:

- commit SHA;
- Python and dependency versions;
- character discriminant and completed normalization;
- packet centers and widths;
- basis dimension;
- prime cutoff convention;
- quadrature tolerances;
- Gram condition number;
- matrix Hermitian defect;
- generalized eigenpair residuals;
- random seeds, if any;
- raw output sufficient to reproduce figures.

## 15. Stop conditions

An experiment should be treated as numerically unreliable when any of the following occurs:

- the Gram matrix loses positive definiteness numerically;
- the generalized eigenpair residual is comparable to the claimed effect;
- the result changes materially under harmless basis rescaling;
- cutoff changes exceed the observed spectral gap;
- quadrature warnings are ignored;
- ordinary eigenvalues are substituted for generalized eigenvalues;
- a matrix is symmetrized after assembly without investigating the source of asymmetry.

## 16. Near-term implementation sequence

The recommended next code milestones are:

1. complete the contour derivation of the gamma normalization;
2. implement `gamma_weight`, `gamma_kernel`, and `gamma_matrix`;
3. add generalized Hermitian eigenvalue utilities using the Gram matrix;
4. assemble a cutoff `WeilOperator` object;
5. add reproducible convergence experiments;
6. introduce rigorous quadrature and interval enclosures only after floating-point validation.

## 17. Long-term objective

The long-term objective is not merely to produce large matrices. It is to create a transparent bridge between:

- the explicit formula;
- finite-dimensional variational problems;
- rigorous numerical certificates;
- operator-theoretic questions about Weil positivity.

Success should be measured by the quality of definitions, error bounds, and falsifiable experiments, not by proximity rhetoric surrounding an unsolved problem.
