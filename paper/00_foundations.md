# Foundations of the Finite Weil Program

## 1. Purpose

This document fixes the mathematical objects that the `finite_weil` package is intended to approximate.

The central object is not initially a matrix. It is a sesquilinear form built from the explicit formula for a completed primitive quadratic Dirichlet \(L\)-function. Finite matrices arise only after restricting that form to a finite-dimensional packet space.

The repository follows four rules:

1. definitions precede implementations;
2. normalization constants are derived rather than guessed;
3. proved statements are separated from conjectures;
4. numerical evidence is never presented as a theorem.

## 2. Fourier convention

Throughout,

\[
\widehat f(u)=\int_{\mathbb R} f(x)e^{-iux}\,dx,
\]

with inverse transform

\[
f(x)=\frac{1}{2\pi}\int_{\mathbb R}\widehat f(u)e^{iux}\,du.
\]

Parseval's identity is therefore

\[
\langle f,g\rangle_{L^2(\mathbb R)}
=
\frac{1}{2\pi}
\int_{\mathbb R}
\widehat f(u)\overline{\widehat g(u)}\,du.
\]

Translations are defined by

\[
(\tau_a f)(x)=f(x-a),
\]

so that

\[
\widehat{\tau_a f}(u)=e^{-iua}\widehat f(u).
\]

These conventions agree with `docs/FOURIER_CONVENTION.md` and are binding for every operator formula in the repository.

## 3. Completed Dirichlet data

Let \(\chi\) be a primitive quadratic Dirichlet character of conductor \(q\). Define its parity

\[
a=\frac{1-\chi(-1)}{2}\in\{0,1\}.
\]

The completed \(L\)-function is

\[
\Lambda(s,\chi)
=
\left(\frac q\pi\right)^{(s+a)/2}
\Gamma\!\left(\frac{s+a}{2}\right)
L(s,\chi).
\]

Its logarithmic derivative splits as

\[
\frac{\Lambda'}{\Lambda}(s)
=
\frac12\log\!\left(\frac q\pi\right)
+
\frac12\psi\!\left(\frac{s+a}{2}\right)
+
\frac{L'}{L}(s),
\]

where \(\psi=\Gamma'/\Gamma\).

The implementation of this normalization is `finite_weil.completed.CompletedDirichletData`.

## 4. Test-function space

The natural initial domain is the Schwartz space

\[
\mathcal S(\mathbb R).
\]

This choice ensures:

- rapid decay in physical and Fourier space;
- convergence of the Archimedean integrals;
- well-defined evaluation against the prime-power distribution;
- stability under translation and Fourier transform.

At this stage, no claim is made that the final closed operator acts on all of \(L^2(\mathbb R)\). Questions of closure, self-adjointness, and maximal domain belong to the infinite-operator program.

## 5. Weil sesquilinear form

For admissible test functions \(f,g\), define formally

\[
Q_\chi(f,g)
=
Q_{\mathrm{cond},\chi}(f,g)
+
Q_{\Gamma,\chi}(f,g)
+
Q_{\mathrm{prime},\chi}(f,g).
\]

The decomposition mirrors the logarithmic derivative above.

### 5.1 Conductor contribution

The symmetric explicit formula doubles the prefactor derivative \(\tfrac12\log(q/\pi)\). Hence

\[
Q_{\mathrm{cond},\chi}(f,g)
=
\log\!\left(\frac q\pi\right)
\langle f,g\rangle.
\]

Therefore the conductor operator is formally

\[
W_{\mathrm{cond},\chi}
=
\log\!\left(\frac q\pi\right)I.
\]

This is implemented by `finite_weil.completed.conductor_matrix` after projection to a packet space.

### 5.2 Gamma contribution

The exact coefficient and contour normalization for the gamma contribution must be derived from the same symmetric explicit formula used for the conductor term. The intended Fourier-side form is of the shape

\[
Q_{\Gamma,\chi}(f,g)
=
\frac{1}{2\pi}
\int_{\mathbb R}
\omega_a(t)
\widehat f(t)
\overline{\widehat g(t)}\,dt,
\]

where \(\omega_a\) is a real parity-dependent digamma weight.

The repository must not choose between

\[
\omega_a(t)
=
\operatorname{Re}\psi\!\left(\frac{a+\tfrac12+it}{2}\right)
\]

and a possible half-scaled variant until the contour derivation is written explicitly.

### 5.3 Prime contribution

For a primitive quadratic character, the arithmetic coefficients are

\[
\Lambda(n)\chi(n).
\]

The prime contribution is a distributional translation operator supported at logarithms of prime powers. Its precise sesquilinear form depends on the chosen explicit-formula test-function convention and must remain consistent with `finite_weil.explicit_formula`.

The prime side is expected to be unbounded before suitable domain restrictions or regularization. No claim of boundedness is made here.

## 6. Finite packet spaces

Let

\[
V_N=\operatorname{span}\{\varphi_1,\dots,\varphi_N\}
\subset\mathcal S(\mathbb R),
\]

where the current implementation uses translated Gaussian packets.

The Gram matrix is

\[
B_{ij}=\langle\varphi_i,\varphi_j\rangle.
\]

For any sesquilinear form \(Q\), define its finite matrix by

\[
A_{ij}=Q(\varphi_j,\varphi_i),
\]

subject to the repository's fixed index convention.

When the basis is nonorthonormal, spectral questions belong to the generalized eigenvalue problem

\[
A v=\lambda B v,
\]

not automatically to the ordinary eigenvalue problem for \(A\).

This distinction is essential. Positivity of the restricted form is equivalent to

\[
v^*Av\ge 0
\]

for all coefficient vectors \(v\), while basis-independent spectral values are obtained relative to \(B\).

## 7. Operator language

The notation

\[
Q_\chi(f,g)=\langle f,W_\chi g\rangle
\]

is initially formal.

To turn it into an operator theorem, one must establish:

- a dense domain;
- Hermitian symmetry of the form;
- semiboundedness or another criterion for closability;
- existence of a representing self-adjoint operator, when applicable.

Until those results are proved, the repository should distinguish carefully between:

- the infinite sesquilinear form \(Q_\chi\);
- formal operator notation \(W_\chi\);
- finite restricted matrices \(A_N\).

## 8. Status labels

Mathematical statements in this repository should use one of the following labels:

- **Definition**: fixes notation or an object;
- **Proposition**: proved within the repository;
- **Derived formula**: follows from stated conventions and a documented calculation;
- **Numerical observation**: supported only by computation;
- **Conjecture**: unproved research claim;
- **Open problem**: a question without an asserted answer.

## 9. Immediate theorem targets

The next rigorous targets are:

1. derive the exact gamma weight from the symmetric contour formula;
2. prove Hermitian symmetry of the Archimedean form on \(\mathcal S(\mathbb R)\);
3. characterize the Gaussian-packet gamma kernel;
4. define the finite generalized eigenproblem relative to the Gram matrix;
5. state a convergence theorem with explicit hypotheses rather than assuming spectral convergence.

These targets provide the foundation for `paper/01_infinite_weil_operator.md`, `paper/02_convergence_theory.md`, and `paper/03_spectral_program.md`.
