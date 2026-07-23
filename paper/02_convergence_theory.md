# Convergence Theory for Finite Weil Restrictions

## 1. Purpose

Finite matrices are useful only when their relation to the infinite form is stated precisely. This chapter separates three different limits that must not be conflated:

1. enlargement of the packet space;
2. removal of the prime cutoff;
3. improvement of numerical quadrature.

Each requires its own error analysis.

## 2. Finite-dimensional spaces

Let \(\mathcal H=L^2(\mathbb R)\) and let \(\mathcal D\subset\mathcal H\) be a dense form core, initially \(\mathcal S(\mathbb R)\).

Let

\[
V_1\subset V_2\subset\cdots\subset\mathcal D
\]

be finite-dimensional spaces, and let \(P_N\) denote the orthogonal projection onto \(V_N\).

The density requirement is

\[
\overline{\bigcup_{N\ge1}V_N}^{\,\mathcal H}=\mathcal H
\]

or, for form approximation, density in the form norm associated with the closed form under study.

A family of translated Gaussian packets is not automatically nested or complete merely because the number of centers increases. Completeness and conditioning must be checked for each sampling scheme.

## 3. Form restrictions

Let \(Q\) be a Hermitian form on \(\mathcal D\). Its restriction to \(V_N\) is

\[
Q_N=Q|_{V_N\times V_N}.
\]

Given a basis \(\{\varphi_j^{(N)}\}_{j=1}^N\), define

\[
A_N=(Q(\varphi_j^{(N)},\varphi_i^{(N)}))_{i,j}
\]

and

\[
B_N=(\langle\varphi_j^{(N)},\varphi_i^{(N)}\rangle)_{i,j}.
\]

The matrix \(A_N\) depends on the chosen basis. The generalized eigenvalues of \((A_N,B_N)\) depend only on the restricted form and Hilbert structure, provided \(B_N\) is positive definite.

## 4. Three notions of convergence

### 4.1 Pointwise form convergence

A sequence \(Q_m\) converges pointwise on a core if

\[
Q_m(f,g)\to Q(f,g)
\]

for every fixed \(f,g\in\mathcal D\).

This is the minimum expected from removing a prime cutoff. By itself, it does not imply spectral convergence.

### 4.2 Form-norm approximation

Suppose \(Q\) is closed and lower semibounded. For a sufficiently large constant \(c\), define

\[
\|f\|_Q^2=Q(f,f)+c\|f\|^2.
\]

A Galerkin sequence is form-dense when

\[
\inf_{v\in V_N}\|f-v\|_Q\to0
\]

for every \(f\) in the form domain.

This is the natural condition for variational convergence of low-lying spectral values.

### 4.3 Strong resolvent convergence

For self-adjoint operators \(W_N\) and \(W\), strong resolvent convergence means

\[
(W_N-z)^{-1}f\to(W-z)^{-1}f
\]

for every \(f\in\mathcal H\) and every nonreal \(z\).

This controls spectral projections away from unstable boundary points, but it still does not guarantee naive convergence of every eigenvalue when essential spectrum is present.

## 5. Galerkin approximation

Assume for this section that \(Q\) is densely defined, closed, and lower semibounded, with representing self-adjoint operator \(W\).

Define the finite Rayleigh minimum

\[
\lambda_N
=
\inf_{0\ne v\in V_N}
\frac{Q(v,v)}{\|v\|^2}.
\]

If the spaces are nested, then

\[
\lambda_{N+1}\le\lambda_N.
\]

Thus the finite minimum is monotone nonincreasing as the trial space grows.

### Proposition 5.1

If \(\bigcup_N V_N\) is form-dense, then

\[
\lambda_N\downarrow
\inf_{0\ne f\in\mathcal D(Q)}
\frac{Q(f,f)}{\|f\|^2}
=
\inf\sigma(W).
\]

### Status

This is a standard variational conclusion under the stated closedness, semiboundedness, nesting, and form-density hypotheses. The repository has not yet proved those hypotheses for the full Weil form.

## 6. Positivity and finite restrictions

If \(Q\) is nonnegative on its full domain, then every finite restriction is nonnegative.

The converse requires density and continuity in an appropriate topology.

### Proposition 6.1

Assume \(Q\) is closed and lower semibounded, \(\bigcup_N V_N\) is form-dense, and

\[
Q(v,v)\ge0
\]

for every \(v\in\bigcup_N V_N\). Then

\[
Q(f,f)\ge0
\]

for every \(f\) in the form domain.

### Proof sketch

Approximate \(f\) in form norm by \(v_N\in V_N\). Closed-form continuity gives

\[
Q(v_N,v_N)\to Q(f,f).
\]

The limit of nonnegative numbers is nonnegative.

### Warning

Checking positivity for finitely many values of \(N\) proves positivity only on those finite spaces. It cannot establish positivity on the infinite domain.

## 7. Prime-cutoff convergence

Let \(Q_{\mathrm{prime},X}\) denote the prime-power contribution truncated at a parameter \(X\). A convergence theorem must specify:

- whether the cutoff is by \(n\le X\), \(\log n\le T\), or prime power;
- whether smoothing is present;
- the test-function class;
- the topology of convergence;
- an explicit tail bound.

For a fixed pair of rapidly decaying test functions, one seeks a bound of the form

\[
|Q_{\mathrm{prime}}(f,g)-Q_{\mathrm{prime},X}(f,g)|
\le E_{\mathrm{prime}}(X;f,g),
\]

with

\[
E_{\mathrm{prime}}(X;f,g)\to0.
\]

A hard cutoff may converge slowly or interact poorly with spectral calculations. Smooth cutoffs should be considered as a separate approximation family rather than silently substituted.

## 8. Quadrature convergence

For each matrix entry, numerical quadrature produces an approximation

\[
\widetilde A_{N,ij}=A_{N,ij}+E_{N,ij}.
\]

A rigorous computation requires an interval or deterministic bound

\[
|E_{N,ij}|\le\varepsilon_{N,ij}.
\]

Entrywise error can be converted to an operator-norm estimate, for example

\[
\|E_N\|_2
\le
\sqrt{\|E_N\|_1\|E_N\|_\infty}.
\]

For a generalized eigenproblem, perturbations in both \(A_N\) and \(B_N\) matter. Poor conditioning of \(B_N\) can amplify otherwise small entrywise errors.

## 9. Conditioning of Gaussian packet spaces

Translated Gaussians become nearly linearly dependent when centers are too close relative to their width. Then

\[
\kappa(B_N)
\]

can become large.

Every spectral experiment should report at least:

- the smallest and largest eigenvalues of \(B_N\);
- the condition number of \(B_N\);
- whether Cholesky factorization succeeds stably;
- whether results persist after orthonormalization.

A numerically negative generalized eigenvalue in an ill-conditioned basis is not automatically evidence of a negative Weil direction.

## 10. Spectral pollution

Galerkin methods can generate spurious spectral values, especially in gaps of essential spectrum or for indefinite problems.

The project should not assume that every observed eigenvalue converges to a genuine spectral point of an infinite operator. Defenses include:

- variational bounds for semibounded operators;
- residual norms;
- comparison across nested spaces;
- basis changes;
- second-order spectrum methods;
- certified enclosures.

## 11. Error decomposition

For a target spectral quantity, the total discrepancy should be separated schematically as

\[
E_{\mathrm{total}}
\le
E_{\mathrm{space}}
+
E_{\mathrm{prime}}
+
E_{\mathrm{quadrature}}
+
E_{\mathrm{roundoff}}.
\]

Here:

- \(E_{\mathrm{space}}\) is finite-dimensional projection error;
- \(E_{\mathrm{prime}}\) is arithmetic truncation error;
- \(E_{\mathrm{quadrature}}\) is integration error;
- \(E_{\mathrm{roundoff}}\) is floating-point or linear-algebra error.

A numerical experiment is informative only when the dominant source is identified.

## 12. Concrete theorem program

The next convergence results should be attempted in this order:

1. prove density or characterize the closure of the chosen Gaussian packet dictionaries;
2. prove exact Hermitian symmetry of every finite cutoff matrix;
3. derive explicit gamma-quadrature tail bounds from Gaussian decay;
4. bound prime-tail contributions for fixed Gaussian packets;
5. prove convergence of each fixed matrix entry as the prime cutoff grows;
6. control the generalized spectrum under certified matrix perturbations;
7. only then investigate an infinite-dimensional spectral limit.

## 13. Non-theorems to avoid

The following statements must not appear without additional hypotheses:

- \(W_N\to W\) in operator norm;
- all eigenvalues of \(W_N\) converge;
- positivity for many finite dimensions implies RH;
- monotonicity holds for nonnested packet spaces;
- a small quadrature tolerance is a rigorous error certificate;
- ordinary eigenvalues of \(A_N\) are basis-independent when \(B_N\ne I\).

These warnings are part of the mathematical specification of the software.
