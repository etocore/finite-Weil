# 12. The Infinite Weil Quadratic-Form Program

## Status and claim boundary

This document isolates the infinite-dimensional sesquilinear forms that motivate the finite Gaussian-packet matrices developed elsewhere in this repository. It fixes notation, proves the properties presently justified by the reconstructed normalization, and separates those results from the unresolved prime-series problem.

The following are **not** claimed here:

- convergence of the untruncated prime contribution on all of Schwartz space;
- closability or semiboundedness of the complete form;
- existence of an associated self-adjoint operator;
- convergence of finite spectra to an infinite spectrum;
- any consequence for RH or GRH.

The finite packet models remain exact Rayleigh-Ritz problems for their explicitly assembled truncated forms. Establishing an infinite operator requires additional analysis.

## 1. Ambient Hilbert space and Fourier convention

Let

\[
\mathcal H=L^2(\mathbb R),
\qquad
\langle f,g\rangle
=
\int_{\mathbb R}f(x)\overline{g(x)}\,dx,
\]

with the inner product linear in the first argument. The initial test domain is the Schwartz space

\[
\mathcal D_0=\mathcal S(\mathbb R),
\]

which is dense in \(\mathcal H\).

The Fourier transform convention is

\[
\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx,
\qquad
f(x)=\frac1{2\pi}\int_{\mathbb R}\widehat f(t)e^{itx}\,dt.
\]

Thus Parseval's identity takes the form

\[
\langle f,g\rangle
=
\frac1{2\pi}
\int_{\mathbb R}
\widehat f(t)\overline{\widehat g(t)}\,dt.
\]

## 2. Arithmetic data

Let \(\chi\) be a primitive quadratic Dirichlet character of conductor \(q\), and put

\[
a=\frac{1-\chi(-1)}2\in\{0,1\}.
\]

The completed \(L\)-function convention fixed in this repository is

\[
\Lambda(s,\chi)
=
\left(\frac q\pi\right)^{(s+a)/2}
\Gamma\!\left(\frac{s+a}{2}\right)
L(s,\chi).
\]

Define the archimedean multiplier

\[
\omega_a(t)
=
\operatorname{Re}\psi\!\left(\frac{a+\tfrac12+it}{2}\right),
\]

where \(\psi=\Gamma'/\Gamma\) is the digamma function.

For integers \(n\ge2\), define

\[
\beta_\chi(n)
=
\frac{\Lambda(n)\chi(n)}{\sqrt n},
\]

where \(\Lambda(n)\) is the von Mangoldt function.

## 3. Conductor form

### Definition 3.1

For \(f,g\in\mathcal H\), define

\[
Q_{\mathrm{cond},\chi}(f,g)
=
\log\!\left(\frac q\pi\right)\langle f,g\rangle.
\]

### Proposition 3.2

The conductor form is bounded and Hermitian on \(\mathcal H\). Its representing operator is

\[
T_{\mathrm{cond},\chi}
=
\log\!\left(\frac q\pi\right)I.
\]

#### Proof

Boundedness follows from

\[
|Q_{\mathrm{cond},\chi}(f,g)|
\le
\left|\log\!\left(\frac q\pi\right)\right|
\|f\|_2\|g\|_2.
\]

Since the scalar \(\log(q/\pi)\) is real,

\[
Q_{\mathrm{cond},\chi}(f,g)
=
\overline{Q_{\mathrm{cond},\chi}(g,f)}.
\]

The operator representation is immediate. \(\square\)

### Corollary 3.3

For every finite-dimensional subspace \(V\subset\mathcal H\) with Gram matrix \(B\), the conductor matrix is

\[
A_{\mathrm{cond},\chi}
=
\log\!\left(\frac q\pi\right)B.
\]

Consequently, adding the conductor term shifts every generalized eigenvalue by exactly \(\log(q/\pi)\).

## 4. Gamma form

### Definition 4.1

For \(f,g\in\mathcal S(\mathbb R)\), define

\[
Q_{\Gamma,a}(f,g)
=
\frac1{2\pi}
\int_{\mathbb R}
\omega_a(t)
\widehat f(t)
\overline{\widehat g(t)}\,dt.
\]

### Proposition 4.2

The integral in Definition 4.1 converges absolutely for every \(f,g\in\mathcal S(\mathbb R)\).

#### Proof

The digamma asymptotic on vertical lines gives

\[
\omega_a(t)=\log(|t|/2)+O(|t|^{-2})
\qquad (|t|\to\infty),
\]

and \(\omega_a\) is continuous on \(\mathbb R\). Hence there is a constant \(C_a>0\) such that

\[
|\omega_a(t)|
\le
C_a\bigl(1+\log(1+|t|)\bigr).
\]

Because the Fourier transform preserves Schwartz space, for every integer \(N\ge0\) there are constants \(C_{f,N},C_{g,N}\) with

\[
|\widehat f(t)|\le C_{f,N}(1+|t|)^{-N},
\qquad
|\widehat g(t)|\le C_{g,N}(1+|t|)^{-N}.
\]

Choosing \(N\ge2\), the product

\[
|\omega_a(t)\widehat f(t)\overline{\widehat g(t)}|
\]

is bounded by an integrable function. \(\square\)

### Proposition 4.3

The gamma form is Hermitian on \(\mathcal S(\mathbb R)\):

\[
Q_{\Gamma,a}(f,g)
=
\overline{Q_{\Gamma,a}(g,f)}.
\]

#### Proof

The multiplier \(\omega_a(t)\) is real-valued. Absolute convergence permits complex conjugation under the integral:

\[
\overline{Q_{\Gamma,a}(g,f)}
=
\frac1{2\pi}
\int_{\mathbb R}
\omega_a(t)
\widehat f(t)
\overline{\widehat g(t)}\,dt.
\]

This equals \(Q_{\Gamma,a}(f,g)\). \(\square\)

### Remark 4.4

The gamma form is a densely defined real Fourier-multiplier form. This document does not yet claim its closedness or identify its maximal form domain. A natural later candidate is

\[
\mathcal D_\Gamma
=
\left\{
 f\in L^2(\mathbb R):
 \int_{\mathbb R}|\omega_a(t)|\,|\widehat f(t)|^2\,dt<\infty
\right\},
\]

but a complete treatment must account for the fact that \(\omega_a\) is not asserted here to be nonnegative.

## 5. Translation correlations and finite prime forms

For \(u\in\mathbb R\), let

\[
(\tau_u g)(x)=g(x-u).
\]

Define the two-sided translation form

\[
T_u(f,g)
=
-
\bigl(
\langle f,\tau_u g\rangle
+
\langle f,\tau_{-u}g\rangle
\bigr).
\]

### Proposition 5.1

For every \(u\in\mathbb R\), \(T_u\) is a bounded Hermitian form on \(L^2(\mathbb R)\), and

\[
|T_u(f,g)|\le2\|f\|_2\|g\|_2.
\]

#### Proof

Translations are unitary on \(L^2(\mathbb R)\), so Cauchy-Schwarz gives the stated bound. Moreover \(\tau_u^*=\tau_{-u}\), hence

\[
\overline{T_u(g,f)}
=
-
\bigl(
\langle f,\tau_{-u}g\rangle
+
\langle f,\tau_u g\rangle
\bigr)
=
T_u(f,g).
\]

\(\square\)

### Definition 5.2

For a finite cutoff \(X\ge2\), define the truncated prime form

\[
Q_{\mathrm{prime},\chi}^{(X)}(f,g)
=
\sum_{2\le n\le X}
\beta_\chi(n)
T_{\log n}(f,g).
\]

The sum is finite, so this is a bounded Hermitian form on \(L^2(\mathbb R)\).

### Proposition 5.3

For each finite \(X\),

\[
\left|Q_{\mathrm{prime},\chi}^{(X)}(f,g)\right|
\le
2
\left(
\sum_{2\le n\le X}|\beta_\chi(n)|
\right)
\|f\|_2\|g\|_2.
\]

Thus the truncated prime form is represented by the bounded self-adjoint operator

\[
T_{\mathrm{prime},\chi}^{(X)}
=
-
\sum_{2\le n\le X}
\beta_\chi(n)
\left(
\tau_{\log n}+\tau_{-\log n}
\right).
\]

## 6. The untruncated prime-series problem

The formal untruncated expression is

\[
Q_{\mathrm{prime},\chi}(f,g)
\stackrel{\mathrm{formal}}{=}
\sum_{n\ge2}
\beta_\chi(n)
T_{\log n}(f,g).
\]

The elementary bound in Proposition 5.1 does not prove convergence because

\[
\sum_{n\ge2}|\beta_\chi(n)|
=
\sum_{n\ge2}
\frac{\Lambda(n)|\chi(n)|}{\sqrt n}
\]

diverges. Any rigorous definition must exploit decay or cancellation in the translated correlations.

For \(f,g\in L^2(\mathbb R)\), set

\[
C_{f,g}(u)=\langle f,\tau_u g\rangle.
\]

Then formally

\[
Q_{\mathrm{prime},\chi}(f,g)
=
-
\sum_{n\ge2}
\beta_\chi(n)
\bigl(
C_{f,g}(\log n)+C_{f,g}(-\log n)
\bigr).
\]

For Schwartz functions, \(C_{f,g}\) is itself a Schwartz function of \(u\). Nevertheless, this observation alone must be combined with a quantitative summability argument along the nonuniform sequence \(u=\log n\). Establishing such an argument is the next principal analytic task.

### Open Problem 6.1

Find a dense subspace \(\mathcal D_{\mathrm{prime}}\subset L^2(\mathbb R)\) on which the prime series converges and defines a Hermitian sesquilinear form.

The following notions must be distinguished:

1. absolute convergence for each pair \((f,g)\);
2. locally uniform convergence on bounded subsets of a test-function topology;
3. convergence after a specified smooth cutoff and removal of the cutoff;
4. convergence only as a distribution or weak form.

No equivalence among these notions is asserted.

## 7. Complete truncated forms

### Definition 7.1

For each finite cutoff \(X\), define

\[
Q_{\chi}^{(X)}(f,g)
=
Q_{\mathrm{cond},\chi}(f,g)
+
Q_{\Gamma,a}(f,g)
+
Q_{\mathrm{prime},\chi}^{(X)}(f,g),
\qquad
f,g\in\mathcal S(\mathbb R).
\]

### Theorem 7.2

For every finite \(X\), \(Q_\chi^{(X)}\) is a densely defined Hermitian form on \(L^2(\mathbb R)\).

#### Proof

The domain \(\mathcal S(\mathbb R)\) is dense in \(L^2(\mathbb R)\). The conductor and truncated prime pieces are bounded Hermitian forms on all of \(L^2\), while the gamma piece is well-defined and Hermitian on Schwartz space by Propositions 4.2 and 4.3. Their sum has the stated properties. \(\square\)

### Remark 7.3

The theorem deliberately concerns finite prime cutoff. It does not establish convergence as \(X\to\infty\), nor does it assert that the form is closed or semibounded.

## 8. Gaussian-packet Galerkin compression

Let

\[
g_j(x)=\exp\!\left(-\frac{(x-c_j)^2}{2\sigma^2}\right),
\qquad
1\le j\le N,
\]

and define

\[
V_N=\operatorname{span}\{g_1,\dots,g_N\}.
\]

Each packet belongs to \(\mathcal S(\mathbb R)\). Let

\[
B_{ij}=\langle g_j,g_i\rangle,
\qquad
A_{ij}^{(X)}=Q_\chi^{(X)}(g_j,g_i).
\]

With the repository's coordinate convention, the restricted Rayleigh quotient is

\[
\mathcal R_{N,X}(c)
=
\frac{c^*A^{(X)}c}{c^*Bc},
\qquad c\ne0.
\]

The stationary values are exactly the generalized eigenvalues of

\[
A^{(X)}c=\lambda Bc.
\]

Thus the matrices implemented in the repository are exact coordinate representations of the truncated form restricted to packet spaces. Gram whitening changes coordinates and may discard numerically unstable Gram modes; it does not create an infinite-dimensional convergence theorem.

## 9. Exact conductor removal

Write

\[
A_\chi^{(X)}
=
\log\!\left(\frac q\pi\right)B
+
A_{\Gamma,a}
+
A_{\mathrm{prime},\chi}^{(X)}.
\]

Therefore

\[
A_\chi^{(X)}-\log\!\left(\frac q\pi\right)B
=
A_{\Gamma,a}+A_{\mathrm{prime},\chi}^{(X)}.
\]

At fixed parity, packet family, and prime data, the conductor term contributes a rigid generalized-spectral shift. Subtracting \(\log q\) instead differs from subtracting the exact conductor shift by the fixed constant \(-\log\pi\).

## 10. Research program

The next stages are logically ordered as follows.

### 10.1 Prime-domain theorem

Prove convergence of the untruncated prime series on a concrete dense test domain, or define a regularized limiting form with a rigorously justified removal procedure.

### 10.2 Combined form

Once the prime term is defined, determine a common dense domain

\[
\mathcal D_\chi
\subseteq
\mathcal D_\Gamma\cap\mathcal D_{\mathrm{prime}}
\]

for

\[
Q_\chi
=
Q_{\mathrm{cond},\chi}
+
Q_{\Gamma,a}
+
Q_{\mathrm{prime},\chi}.
\]

### 10.3 Closability and semiboundedness

Determine whether \(Q_\chi\) is closable and whether it is bounded below. These are separate questions. A symmetric densely defined form need not possess either property.

### 10.4 Operator representation

If an appropriate closed semibounded form is obtained, identify the associated self-adjoint operator through the representation theorem for quadratic forms.

### 10.5 Galerkin convergence

Only after an infinite operator or closed form has been established should one prove convergence of packet-space Rayleigh-Ritz values, spectral projections, or minimizing modes.

## 11. Claim ledger

| Statement | Status |
|---|---|
| Conductor form equals \(\log(q/\pi)\langle f,g\rangle\) | Proved |
| Gamma form is absolutely convergent on Schwartz space | Proved |
| Gamma form is Hermitian on Schwartz space | Proved |
| Each finite translation form is bounded and Hermitian | Proved |
| Each truncated prime form is bounded and Hermitian | Proved |
| Each complete finite-cutoff form is densely defined and Hermitian | Proved |
| Packet matrices are exact finite-dimensional restrictions | Proved from definitions and the finite variational foundation |
| Untruncated prime form exists on Schwartz space | Open |
| Complete form is closable | Open |
| Complete form is semibounded | Open |
| A self-adjoint infinite Weil operator exists in this framework | Open |
| Finite packet spectra converge to an infinite spectrum | Open |
| Numerical finite-cutoff output proves RH or GRH | Not claimed |
