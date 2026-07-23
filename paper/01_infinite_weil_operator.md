# The Infinite Weil Form and Its Formal Operator

## 1. Scope

This chapter defines the infinite object approximated by the finite matrices in `finite_weil`.

The primary object is a sesquilinear form on a dense test-function space. Operator language is used only where justified. In particular, this chapter does not assume that the full Weil form is bounded or that it already determines a self-adjoint operator on all of \(L^2(\mathbb R)\).

## 2. Ambient Hilbert space and core

Let

\[
\mathcal H=L^2(\mathbb R)
\]

with inner product

\[
\langle f,g\rangle
=
\int_{\mathbb R} f(x)\overline{g(x)}\,dx.
\]

Take the Schwartz space

\[
\mathcal D=\mathcal S(\mathbb R)
\]

as the initial common core.

Under the fixed Fourier convention,

\[
\langle f,g\rangle
=
\frac{1}{2\pi}
\int_{\mathbb R}
\widehat f(t)\overline{\widehat g(t)}\,dt.
\]

## 3. Completed primitive quadratic data

Let \(\chi\) be a primitive quadratic Dirichlet character with conductor \(q\) and parity

\[
a=\frac{1-\chi(-1)}2.
\]

The completed \(L\)-function is

\[
\Lambda(s,\chi)
=
\left(\frac q\pi\right)^{(s+a)/2}
\Gamma\!\left(\frac{s+a}{2}\right)L(s,\chi).
\]

The logarithmic derivative decomposes into conductor, gamma, and arithmetic pieces. The Weil form is organized according to this decomposition.

## 4. Conductor form

### Proposition 4.1

Define

\[
Q_{\mathrm{cond},\chi}(f,g)
=
\log\!\left(\frac q\pi\right)
\langle f,g\rangle.
\]

Then \(Q_{\mathrm{cond},\chi}\) is a bounded Hermitian form on \(L^2(\mathbb R)\), represented by

\[
W_{\mathrm{cond},\chi}
=
\log\!\left(\frac q\pi\right)I.
\]

### Proof

The coefficient is real, so

\[
Q_{\mathrm{cond},\chi}(g,f)
=
\overline{Q_{\mathrm{cond},\chi}(f,g)}.
\]

Boundedness follows immediately from Cauchy-Schwarz. The representing operator is the stated scalar multiple of the identity.

## 5. Gamma form

Let \(\omega_a:\mathbb R\to\mathbb R\) denote the real gamma weight obtained from the symmetric explicit formula. Its exact normalization is deliberately left as a theorem target until the contour calculation is completed.

Define formally

\[
Q_{\Gamma,\chi}(f,g)
=
\frac{1}{2\pi}
\int_{\mathbb R}
\omega_a(t)
\widehat f(t)
\overline{\widehat g(t)}\,dt.
\]

The expected weight is logarithmic at infinity because

\[
\psi(z)=\log z+O(|z|^{-1})
\]

in sectors avoiding the negative real axis. Consequently,

\[
\omega_a(t)=\log(|t|/2)+O(|t|^{-1})
\]

up to the normalization fixed by the contour derivation.

### Proposition 5.1

Assume \(\omega_a\) is real-valued, locally bounded, and satisfies

\[
|\omega_a(t)|\le C(1+\log(1+|t|)).
\]

Then \(Q_{\Gamma,\chi}\) is well-defined and Hermitian on \(\mathcal S(\mathbb R)\).

### Proof

For Schwartz functions, the product

\[
\widehat f(t)\overline{\widehat g(t)}
\]

decays faster than every power of \(|t|\). Multiplication by a logarithmically growing weight remains integrable. Since \(\omega_a\) is real,

\[
Q_{\Gamma,\chi}(g,f)
=
\overline{Q_{\Gamma,\chi}(f,g)}.
\]

### Formal Fourier multiplier

Let \(\mathcal F\) denote the Fourier transform. On a suitable domain, the gamma contribution is formally

\[
W_{\Gamma,\chi}
=
\mathcal F^{-1}M_{\omega_a}\mathcal F,
\]

where \(M_{\omega_a}\) is multiplication by \(\omega_a\).

A natural maximal multiplier domain is

\[
\mathcal D(W_{\Gamma,\chi})
=
\left\{
 f\in L^2(\mathbb R):
 \omega_a\widehat f\in L^2(\mathbb R)
\right\}.
\]

Once the exact real weight has been fixed, the standard multiplication-operator theorem gives a self-adjoint Fourier multiplier on this domain.

## 6. Prime-power form

The arithmetic side is supported at logarithms of prime powers. Let

\[
c_\chi(n)=\Lambda(n)\chi(n).
\]

A formal translation operator has the shape

\[
W_{\mathrm{prime},\chi}
\sim
-
\sum_{n\ge 2}
\frac{c_\chi(n)}{\sqrt n}
\bigl(\tau_{\log n}+\tau_{-\log n}\bigr),
\]

with the overall sign and normalization fixed by the explicit-formula convention implemented in the library.

For each fixed translation distance, \(\tau_a\) is unitary on \(L^2\). The difficulty is the infinite weighted sum. Absolute convergence in operator norm is not expected because

\[
\sum_{n\ge 2}
\frac{|\Lambda(n)\chi(n)|}{\sqrt n}
\]

diverges.

Therefore the prime contribution must initially be interpreted as one of the following:

- a distributional form on a test-function core;
- a cutoff operator followed by a limiting procedure;
- a regularized operator associated with an admissible explicit-formula class.

No stronger interpretation is asserted in this chapter.

## 7. Full form

Define

\[
Q_\chi
=
Q_{\mathrm{cond},\chi}
+
Q_{\Gamma,\chi}
+
Q_{\mathrm{prime},\chi}
\]

on the intersection of the domains where all three contributions are defined.

### Formal Hermitian symmetry

If the prime coefficients are real, as they are for quadratic characters, and the prime contribution uses paired translations \(\tau_a+\tau_{-a}\), then each finite cutoff is Hermitian. Thus the cutoff forms satisfy

\[
Q_{\chi,X}(g,f)
=
\overline{Q_{\chi,X}(f,g)}.
\]

Passing to an infinite limit requires a convergence theorem.

## 8. Finite restrictions

Let

\[
V_N=\operatorname{span}\{\varphi_1,\ldots,\varphi_N\}
\subset\mathcal S(\mathbb R).
\]

Define

\[
B_{ij}=\langle\varphi_j,\varphi_i\rangle
\]

and

\[
A_{ij}=Q_\chi(\varphi_j,\varphi_i).
\]

For

\[
f=\sum_j v_j\varphi_j,
\]

we obtain

\[
Q_\chi(f,f)=v^*Av,
\qquad
\|f\|^2=v^*Bv.
\]

Thus the Rayleigh quotient is

\[
\mathcal R_N(v)
=
\frac{v^*Av}{v^*Bv}.
\]

The basis-independent finite spectrum is the generalized spectrum of the matrix pencil

\[
(A,B).
\]

## 9. Gaussian packets

For translated Gaussian packets with common width \(\sigma\) and centers \(c_j\), the Fourier products have the form

\[
\widehat\varphi_i(t)
\overline{\widehat\varphi_j(t)}
=
2\pi\sigma^2
 e^{-\sigma^2t^2}
 e^{it(c_j-c_i)}.
\]

For an even real multiplier \(\omega_a\), the gamma matrix reduces to the real kernel

\[
(A_\Gamma)_{ij}
=
\sigma^2
\int_{\mathbb R}
\omega_a(t)e^{-\sigma^2t^2}
\cos\bigl(t(c_j-c_i)\bigr)\,dt.
\]

Consequences:

- the matrix is real symmetric;
- it is translation-invariant in the packet centers;
- equally spaced centers produce a Toeplitz matrix;
- only distinct center differences need independent quadrature.

## 10. Unproved operator questions

The following remain open within this repository:

1. Does the full form admit a closed semibounded realization?
2. What is the correct maximal domain of the prime contribution?
3. Is the prime contribution relatively form-bounded with respect to the Archimedean multiplier after an appropriate regularization?
4. Which convergence notion connects finite cutoff forms, infinite forms, and generalized spectra?
5. Under what hypotheses is positivity of every finite restriction sufficient to recover Weil positivity on the full admissible class?

These are research questions, not implementation details.
