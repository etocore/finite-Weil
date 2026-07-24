# The Archimedean gamma contribution

## Status

This note fixes the gamma-factor normalization used by the finite Weil model for primitive quadratic Dirichlet L-functions. It is a derivation document, not a claim that the full infinite operator has already been constructed as a self-adjoint operator.

## Completed-function normalization

For a primitive character `chi` of conductor `q` and parity

\[
a=\frac{1-\chi(-1)}2\in\{0,1\},
\]

the project uses

\[
\Lambda(s,\chi)=\left(\frac q\pi\right)^{(s+a)/2}
\Gamma\!\left(\frac{s+a}{2}\right)L(s,\chi).
\]

Hence

\[
\frac{\Lambda'}{\Lambda}(s,\chi)
=
\frac12\log\!\left(\frac q\pi\right)
+
\frac12\psi\!\left(\frac{s+a}{2}\right)
+
\frac{L'}{L}(s,\chi),
\]

where `psi = Gamma'/Gamma` is the digamma function.

## Symmetric contour normalization

The Weil form pairs the logarithmic derivative on the critical line with its functional-equation partner. For real quadratic characters, the two gamma terms are complex conjugates. At

\[
s=\frac12+it,
\]

the one-sided term is

\[
\frac12\psi\!\left(\frac{a+\tfrac12+it}{2}\right).
\]

Adding the reflected contribution gives

\[
\frac12\psi(z)+\frac12\overline{\psi(z)}
=
\operatorname{Re}\psi(z),
\qquad
z=\frac{a+\tfrac12+it}{2}.
\]

Therefore the frequency multiplier in the symmetric Weil form is

\[
w_a(t)
=
\operatorname{Re}\psi\!\left(\frac{a+\tfrac12+it}{2}\right).
\]

This is the gamma analogue of the conductor calculation: each contour contributes a factor `1/2`, and the symmetric pair combines them into a single real multiplier. There is no additional factor of `1/2` in `w_a`.

## Fourier convention

The repository fixes

\[
\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx,
\qquad
f(x)=\frac1{2\pi}\int_{\mathbb R}\widehat f(t)e^{itx}\,dt.
\]

Accordingly, the gamma sesquilinear form is

\[
Q_\Gamma(f,g)
=
\frac1{2\pi}\int_{\mathbb R}
 w_a(t)\widehat f(t)\overline{\widehat g(t)}\,dt.
\]

The multiplier is real and even, so this form is Hermitian on any test-function class for which the integral converges.

## Gaussian packet specialization

For

\[
g_j(x)=\exp\!\left(-\frac{(x-c_j)^2}{2\sigma^2}\right),
\]

our Fourier convention gives

\[
\widehat g_j(t)
=
\sqrt{2\pi}\,\sigma
e^{-\sigma^2t^2/2}e^{-itc_j}.
\]

Thus

\[
\widehat g_i(t)\overline{\widehat g_j(t)}
=
2\pi\sigma^2e^{-\sigma^2t^2}e^{it(c_j-c_i)}.
\]

Substitution into the form yields

\[
(A_\Gamma)_{ij}
=
\sigma^2\int_{-\infty}^{\infty}
 w_a(t)e^{-\sigma^2t^2}e^{it(c_j-c_i)}\,dt.
\]

Since `w_a` is real and even, the imaginary part vanishes:

\[
(A_\Gamma)_{ij}
=
2\sigma^2\int_0^\infty
 w_a(t)e^{-\sigma^2t^2}
 \cos\!\bigl(t(c_j-c_i)\bigr)\,dt.
\]

Define

\[
K_{a,\sigma}(\delta)
=
2\sigma^2\int_0^\infty
 w_a(t)e^{-\sigma^2t^2}\cos(\delta t)\,dt.
\]

Then

\[
(A_\Gamma)_{ij}=K_{a,\sigma}(c_j-c_i).
\]

Consequences:

1. `A_Gamma` is real symmetric.
2. It is invariant under a common translation of all packet centers.
3. For equally spaced centers, it is Toeplitz.
4. The Gaussian factor makes the integral absolutely convergent despite the logarithmic growth of the digamma multiplier.

## Asymptotic check

The standard digamma expansion

\[
\psi(z)=\log z-\frac1{2z}+O(|z|^{-2})
\]

implies

\[
w_a(t)=\log\!\left(\frac{|t|}{2}\right)+O(|t|^{-2})
\qquad (|t|\to\infty).
\]

This asymptotic is used as a regression test for the implementation.

## Implementation correspondence

The derivation is realized by:

```text
finite_weil.gamma.gamma_weight
finite_weil.gamma.gamma_kernel
finite_weil.gamma.gamma_matrix
```

The code evaluates the exact SciPy digamma function and performs adaptive quadrature on the even half-line representation above.
