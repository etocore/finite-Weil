# Stagewise collision matrix pipeline

## Purpose

The missing collision grade has not appeared in either of the two simplest
models:

1. the corrected collision-moment block by itself;
2. Gaussian packet synthesis projected modulo separated packet and packet-
derivative directions.

The next diagnostic must therefore locate the first transformation in the actual
finite Weil matrix pipeline that changes the collision exponents.

The experiment is implemented in

```text
experiments/collision_matrix_pipeline.py
```

and covered by

```text
tests/test_collision_matrix_pipeline.py
```

## Source variables in the first pass

The current finite Weil implementation constructs packet-space matrices from the
packet centers and common width. It does not use mixture amplitudes in the Gram or
Weil matrices. The first pipeline experiment therefore differentiates with
respect to packet centers.

This is a deliberate restriction. Adding formal amplitude variables to targets
that do not depend on them would merely add zero Jacobian columns. The exact
historical source map must be recovered before a meaningful combined
weight-center Jacobian can be reconstructed.

For a cluster shape \(\xi_1,\ldots,\xi_m\), the shrinking centers are

\[
c_j(h)=h\left(\xi_j-\frac1m\sum_k\xi_k\right).
\]

Separated exterior centers are appended without scaling.

## Pipeline stages

For each collision scale \(h\), the experiment forms a numerical Jacobian for
six target maps.

### 1. Sampled packet synthesis

The first target is the flattened packet evaluation matrix

\[
\left(g_j(x_r)\right)_{r,j}
\]

on a fixed physical-space grid.

This tests the raw Gaussian dictionary geometry.

### 2. Gram matrix

The second target is

\[
B(c)_{ij}=\langle g_i,g_j\rangle.
\]

This is the first nonlinear matrix-valued stage and the primary candidate for a
collision-specific rank change.

### 3. Weil matrix

The third target is the fully assembled finite coordinate matrix

\[
A(c)=A_{\mathrm{cond}}(c)+A_\Gamma(c)+A_{\mathrm{prime}}(c).
\]

The prime cutoff is finite and recorded as part of the experiment.

### 4. Paired target

The fourth target is the direct product

\[
c\longmapsto (A(c),B(c)),
\]

implemented by concatenating the flattened matrices. This checks whether the
matrix pencil contains information absent from either matrix alone.

### 5. Fully retained whitening

When \(B(c)\) is positive definite, define

\[
W(c)=B(c)^{-1/2}A(c)B(c)^{-1/2}.
\]

No Gram modes are truncated in this stage. This distinction matters: rank
truncation is not an analytic coordinate change and can create tolerance-
dependent transitions.

### 6. Generalized eigenvalues

The final target is the ordered generalized spectrum

\[
\operatorname{spec}(A(c),B(c)).
\]

This is nonlinear and can lose differentiability at repeated eigenvalues. Any
slope change that appears only here must therefore be checked against eigenvalue
crossings before receiving a geometric interpretation.

## Numerical method

At each scale, central finite differences produce a target Jacobian. Singular
values are then fitted against powers of \(h\) by linear regression in logarithmic
coordinates.

The output is diagnostic rather than exact. In particular:

- finite differences introduce a second small scale;
- fitted slopes need not be exact integers over a finite window;
- whitening becomes ill-conditioned close to collision;
- ordered eigenvalues may not define a smooth target through crossings.

The experiment should be used to locate the first suspicious stage. Once located,
that stage should be replaced by a symbolic power-series or determinantal-divisor
calculation.

## Interpretation rule

Let the fitted exponent multisets be

\[
E_{\mathrm{synth}}, E_B, E_A, E_{(A,B)}, E_W, E_{\mathrm{spec}}.
\]

The first adjacent pair that differs identifies the transformation requiring
exact analysis.

Examples:

- if \(E_{\mathrm{synth}}=E_B\) but \(E_A\ne E_B\), the mechanism lies in the
  Weil-form assembly;
- if \(E_A=E_{(A,B)}\) but \(E_W\ne E_A\), the mechanism lies in Gram inversion
  or whitening;
- if all matrix stages agree but \(E_{\mathrm{spec}}\) changes, the gap is a
  spectral-coordinate phenomenon rather than an intrinsic matrix Smith grade.

## Claim boundary

This experiment does not yet reproduce the historical missing-grade run. It
provides the stagewise instrument needed to do so. A reproduction requires the
exact historical choices of source variables, collision path, matrix target,
normalization, whitening tolerance, exterior packets, and slope-fitting window.
