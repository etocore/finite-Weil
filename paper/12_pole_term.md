# The finite pole matrix for the completed Riemann zeta function

## 1. Scope and claim status

This chapter derives the finite-dimensional contribution of the poles of

\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

to the Weil form restricted to a Gaussian packet family.

The analytic derivation is unconditional. Numerical values quoted in external experiments are not used to determine the formula or its sign and are not asserted here unless reproduced inside this repository.

## 2. Explicit-formula pole functional

Under the additive Fourier convention

\[
\widehat f(z)=\int_{\mathbb R} f(x)e^{-izx}\,dx,
\]

the pole part of the completed-zeta Weil functional is

\[
W_{0,2}(F)=\widehat F(i/2)+\widehat F(-i/2).
\]

In the standard decomposition of the zeta Weil functional, this block enters with a positive sign relative to the archimedean and prime blocks. Thus the sign of the pole term is fixed analytically by the explicit formula, not fitted from spectral data.

For the polarized form, let

\[
f^*(x)=\overline{f(-x)}.
\]

Since

\[
\widehat{f^**g}(z)
=
\overline{\widehat f(\overline z)}\,\widehat g(z),
\]

the pole contribution is

\[
Q_{\mathrm{pole}}(f,g)
=
\overline{\widehat f(-i/2)}\,\widehat g(i/2)
+
\overline{\widehat f(i/2)}\,\widehat g(-i/2).
\]

Equivalently, define the bilateral Laplace evaluations

\[
L_a(f)=\int_{\mathbb R} f(x)e^{ax}\,dx.
\]

Then

\[
\widehat f(i/2)=L_{1/2}(f),
\qquad
\widehat f(-i/2)=L_{-1/2}(f),
\]

and therefore

\[
\boxed{
Q_{\mathrm{pole}}(f,g)
=
\overline{L_{-1/2}(f)}L_{1/2}(g)
+
\overline{L_{1/2}(f)}L_{-1/2}(g)
}.
\]

For the quadratic form,

\[
Q_{\mathrm{pole}}(f,f)
=
2\operatorname{Re}
\left(
L_{1/2}(f)\overline{L_{-1/2}(f)}
\right).
\]

For real-valued functions this reduces to

\[
Q_{\mathrm{pole}}(f,f)
=
2L_{1/2}(f)L_{-1/2}(f).
\]

## 3. Cross-correlation derivation

The same factorization can be obtained directly from the packet cross-correlation

\[
F_{f,g}(u)
=
\int_{\mathbb R}f(x+u)\overline{g(x)}\,dx.
\]

Its Mellin-side test function is

\[
H_{f,g}(s)
=
\int_{\mathbb R}F_{f,g}(u)e^{(s-1/2)u}\,du.
\]

Changing variables gives

\[
H_{f,g}(s)
=
L_{s-1/2}(f)
\overline{L_{1/2-\overline s}(g)}.
\]

Hence

\[
H_{f,g}(1)
=
L_{1/2}(f)\overline{L_{-1/2}(g)},
\]

and

\[
H_{f,g}(0)
=
L_{-1/2}(f)\overline{L_{1/2}(g)}.
\]

The two completed-zeta poles therefore produce exactly the Hermitian rank-at-most-two form above.

## 4. Gaussian packet evaluation

Let

\[
g_j(x)
=
\exp\left(-\frac{(x-c_j)^2}{2\sigma^2}\right).
\]

For real \(a\), completing the square gives

\[
\int_{\mathbb R}g_j(x)e^{ax}\,dx
=
\sigma\sqrt{2\pi}
\exp\left(ac_j+\frac{\sigma^2a^2}{2}\right).
\]

At \(a=\pm 1/2\),

\[
L_{1/2}(g_j)
=
\sigma\sqrt{2\pi}\,e^{\sigma^2/8}e^{c_j/2},
\]

\[
L_{-1/2}(g_j)
=
\sigma\sqrt{2\pi}\,e^{\sigma^2/8}e^{-c_j/2}.
\]

Define

\[
(p_+)_j
=
\sigma\sqrt{2\pi}\,e^{\sigma^2/8}e^{c_j/2},
\qquad
(p_-)_j
=
\sigma\sqrt{2\pi}\,e^{\sigma^2/8}e^{-c_j/2}.
\]

Then the finite pole matrix is

\[
\boxed{
P=p_-p_+^*+p_+p_-^*
}.
\]

For real packet data,

\[
P=p_-p_+^T+p_+p_-^T.
\]

Its entries are

\[
\boxed{
P_{ij}
=
4\pi\sigma^2e^{\sigma^2/4}
\cosh\left(\frac{c_i-c_j}{2}\right)
}.
\]

Reversing the sign in the Fourier convention exchanges \(p_+\) and \(p_-\), leaving \(P\) unchanged.

## 5. Rank and spectral structure

Because \(P\) is a sum of two outer products,

\[
\operatorname{rank}P\le 2.
\]

It has rank exactly two when the packet space has dimension at least two and the centers are not all identical. Indeed,

\[
\frac{(p_+)_j}{(p_-)_j}=e^{c_j},
\]

so \(p_+\) and \(p_-\) are linearly dependent exactly when all centers coincide.

For real vectors \(a,b\), the two possible nonzero eigenvalues of

\[
ab^T+ba^T
\]

are

\[
a^Tb\pm \|a\|\|b\|.
\]

Therefore

\[
\lambda_\pm(P)
=
\langle p_+,p_-\rangle
\pm
\|p_+\|\|p_-\|.
\]

When the centers are not all equal, strict Cauchy-Schwarz yields

\[
\lambda_-<0<\lambda_+.
\]

Thus the pole matrix is indefinite in the Euclidean coefficient metric, despite satisfying

\[
v^TPv
=
2(v^Tp_+)(v^Tp_-)>0
\]

for every nonzero coefficient vector \(v\) with nonnegative entries.

## 6. Assembly for the principal character

For the principal quadratic datum \(D=1\), the finite completed-zeta matrix is

\[
\boxed{
A_\zeta
=
A_{\mathrm{cond}}
+
A_\Gamma
+
A_{\mathrm{prime}}
+
P
}.
\]

The conductor block remains

\[
A_{\mathrm{cond}}
=
\log(1/\pi)B
=
-\log(\pi)B.
\]

The pole block is included only for the principal character. Primitive non-principal Dirichlet \(L\)-functions are entire and receive no such term.

## 7. Implementation contract

A direct implementation may use

```python
import numpy as np


def pole_vectors(packets):
    centers = np.asarray(packets.centers, dtype=float)
    sigma = float(packets.sigma)
    prefactor = sigma * np.sqrt(2.0 * np.pi) * np.exp(sigma**2 / 8.0)
    return (
        prefactor * np.exp(-centers / 2.0),
        prefactor * np.exp(centers / 2.0),
    )


def pole_matrix(packets):
    p_minus, p_plus = pole_vectors(packets)
    return np.outer(p_minus, p_plus) + np.outer(p_plus, p_minus)
```

The implementation should be accompanied by tests for:

1. closed-form Laplace evaluations against numerical quadrature;
2. Hermitian symmetry;
3. rank at most two and the exact rank-two criterion;
4. the two nonzero eigenvalue identities;
5. invariance under swapping \(p_+\) and \(p_-\);
6. conditional assembly only for the principal character;
7. independent zero-side numerical validation before any small positive eigenvalue is treated as a regression target.

## 8. Limits

This chapter does not certify any previously reported numerical eigenvalues or interval bounds. Those require separately reproducible artifacts and independent zero-side validation.

The extension to Dedekind zeta functions and other meromorphic completed \(L\)-functions is also outside the present scope. While logarithmic derivatives record pole order rather than the numerical residue of the original function, different completions and multiplicities require their own normalization analysis.

Nothing here establishes an infinite-dimensional self-adjoint operator or proves the Riemann hypothesis.