# Affine-gauge invariance of the collision Smith spectrum

## 1. Purpose

The anchored collision chart fixes

\[
\xi_0=0,
\qquad
\xi_1=1,
\]

and has generic Smith exponents

\[
0,0,1,3,4,\ldots,2m-1.
\]

This note proves that the same spectrum is obtained in every regular analytic
collision chart that removes translation and dilation by a local affine gauge.
In particular, it applies to weighted-center and weighted-variance normalization
on the open set where total weight and weighted variance are nonzero.

## 2. Collision blowup coordinates

Write the physical nodes as

\[
x_j=c+h\xi_j.
\]

The affine group acts on shape coordinates by

\[
\xi_j\longmapsto \frac{\xi_j-\beta}{\alpha},
\qquad
\alpha\ne0.
\]

The corresponding collision variables transform as

\[
c'=c+h\beta,
\qquad
h'=h\alpha,
\qquad
\xi_j'=\frac{\xi_j-\beta}{\alpha}.
\]

The physical nodes are unchanged:

\[
c'+h'\xi_j'=c+h\xi_j.
\]

A regular affine gauge is a local analytic slice transverse to this affine
action. Two regular gauges determine analytic functions

\[
\alpha=\alpha(u,\eta),
\qquad
\beta=\beta(u,\eta),
\]

with \(\alpha\ne0\), where \(\eta\) denotes local shape coordinates on one
slice.

## 3. The chart transition is unimodular

Let

\[
(u,c,h,\eta)
\longmapsto
(u,c',h',\eta')
\]

be the transition between two regular affine gauges. Its Jacobian has the form

\[
\begin{pmatrix}
I&0&0&0\\
*&1&\beta&h*\\
*&0&\alpha&h*\\
*&0&0&D_\eta\eta'
\end{pmatrix}
\]

up to a permutation of source coordinates. At the boundary \(h=0\), this
becomes block triangular. Its determinant is

\[
\alpha\det(D_\eta\eta').
\]

Regularity of both slices implies

\[
\alpha\ne0,
\qquad
\det(D_\eta\eta')\ne0.
\]

Hence the determinant is a unit in the local analytic ring. The transition is
therefore analytic unimodular.

Consequently, right multiplication of the collision Jacobian by the chart
transition does not change its determinantal ideals or Smith exponents.

## 4. Gauge-invariance theorem

### Theorem 4.1

Let two ordered common-scale collision charts be obtained by regular analytic
affine gauge fixing of translation and dilation. Assume their overlap lies in
the open set where the affine normalization is defined. Then their raw moment
Jacobians are right-equivalent over the local analytic ring. In particular,
they have identical h-adic determinantal valuations and identical Smith
exponents.

### Corollary 4.2

Every regular affine collision gauge has the same generic spectrum as the
anchored chart:

\[
\boxed{
0,0,1,3,4,\ldots,2m-1.
}
\]

For \(m\ge3\), grade \(2\) is absent.

The grade-2 gap is therefore not an artifact of choosing two node anchors. It is
an invariant of the affine-gauge collision lattice on the regular collision
blowup.

## 5. Weighted-center and weighted-variance gauge

Define

\[
U_0=\sum_j u_j,
\qquad
\mu=\frac{\sum_j u_jx_j}{U_0}.
\]

Assume

\[
U_0\ne0.
\]

Set the collision center to

\[
c=\mu.
\]

For a fixed nonzero normalization constant \(V_*\), define the scale locally by

\[
h^2
=
\frac{1}{V_*U_0}
\sum_j u_j(x_j-c)^2.
\]

Choose one local analytic branch of the square root away from zero weighted
variance. Then the normalized shape satisfies

\[
\sum_j u_j\xi_j=0,
\qquad
\sum_j u_j\xi_j^2=V_*U_0.
\]

The infinitesimal shape constraints are

\[
\sum_j u_j\,\delta\xi_j=0,
\qquad
\sum_j u_j\xi_j\,\delta\xi_j=0.
\]

Their gradients are independent exactly when the weighted center and variance
normalization are regular. On that open set they define an \((m-2)\)-dimensional
local affine slice.

Therefore the weighted-center/variance chart is analytically unimodularly
related to the anchored chart and has the same Smith spectrum.

## 6. Exact tangent diagnostic

At a fixed weighted-centered shape, choose any basis

\[
s_1,\ldots,s_{m-2}
\]

of the tangent space

\[
\left\{
\delta\xi:
\sum_j u_j\delta\xi_j=0,
\quad
\sum_j u_j\xi_j\delta\xi_j=0
\right\}.
\]

The physical node tangent vectors are

\[
\mathbf 1,
\qquad
\xi,
\qquad
h s_1,\ldots,h s_{m-2}.
\]

The coefficient of the source-change determinant is

\[
\det[\mathbf1,\xi,s_1,\ldots,s_{m-2}].
\]

For centered shapes, the two constraint covectors pair with \(\mathbf1,\xi\)
as

\[
\begin{pmatrix}
U_0&0\\
0&\sum_j u_j\xi_j^2
\end{pmatrix}.
\]

Thus the determinant is nonzero whenever

\[
U_0\ne0
\]

and the weighted variance is nonzero. The source-change valuation remains

\[
m-2.
\]

Exact rational computations in

```text
experiments/affine_gauge_smith.py
```

verify the resulting spectrum for centered three- and four-node examples,
including nonuniform weights.

## 7. What is invariant and what is not

The physical-coordinate lattice and the affine-gauge collision lattice are not
unimodularly equivalent: the physical-to-collision source determinant contains

\[
h^{m-2}.
\]

That singular change moves the missing grade from \(m\) to \(2\).

By contrast, two regular affine gauges are coordinate charts on the same
collision blowup. Their transition has unit determinant and therefore preserves
the grade-2 spectrum.

The correct distinction is

\[
\boxed{
\text{physical lattice: missing grade }m,
\qquad
\text{regular affine-gauge lattice: missing grade }2.
}
\]

## 8. Remaining limitation

This theorem concerns the raw moment map on the ordered common-scale collision
blowup. It does not yet prove:

- descent to unordered clusters;
- compatibility across nested or multiscale collision faces;
- equivalence with Gaussian synthesis for every \(m\);
- preservation through the Gram or Weil quadratic-form construction.

The next geometric task is to globalize the grade-2 filtration over the regular
ordered common-scale boundary face and then analyze its descent under node
permutations.
