# A certified prime-tail bound on fixed packet spaces

## 1. Scope and claim status

This chapter proves an explicit truncation theorem for the prime matrix on a
fixed Gaussian packet space.  The inequalities are unconditional finite
statements.  Their numerical evaluation in `finite_weil.tail_bounds` is
floating point, not interval arithmetic; the chapter states precisely which
side of that line each claim sits on.

The theorem resolves, **for fixed finite packet spaces**, the first, second,
and fourth open obligations of `paper/07_prime_operator.md`: a uniform tail
bound, entrywise convergence of the untruncated prime matrix, and control of
the resulting generalized spectra.  It says nothing about convergence on a
dense function class or about any infinite-dimensional operator.

## 2. Setting

Fix a packet family with distinct centers \(c_1,\dots,c_m\) and width
\(\sigma>0\), and write \(\delta_{ij}=c_i-c_j\).  For a primitive quadratic
character \(\chi\) and cutoff \(N\), the implemented prime matrix is

\[
A_{\mathrm{prime}}(N)_{ij}
=
-\sum_{2\le n\le N}
\beta_\chi(n)\,\sqrt\pi\,\sigma
\left[
G(\delta_{ij}-\log n)+G(\delta_{ij}+\log n)
\right],
\]

with \(G(x)=e^{-x^2/4\sigma^2}\) and
\(|\beta_\chi(n)|\le\Lambda(n)/\sqrt n\le(\log n)/\sqrt n\).

## 3. The closed-form tail integral

### Lemma 3.1

For every real \(\delta\), \(\sigma>0\), and \(L\in\mathbb R\), with
\(\mu=\delta+\sigma^2\),

\[
\int_L^\infty u\,e^{u/2}e^{-(u-\delta)^2/4\sigma^2}\,du
=
e^{\delta/2+\sigma^2/4}
\left[
\mu\sigma\sqrt\pi\,\operatorname{erfc}\!\left(\frac{L-\mu}{2\sigma}\right)
+2\sigma^2e^{-(L-\mu)^2/4\sigma^2}
\right].
\]

#### Proof

Completing the square,

\[
\frac u2-\frac{(u-\delta)^2}{4\sigma^2}
=
\frac\delta2+\frac{\sigma^2}4-\frac{(u-\mu)^2}{4\sigma^2}.
\]

Split \(u=(u-\mu)+\mu\).  The first piece integrates to
\(2\sigma^2e^{-(L-\mu)^2/4\sigma^2}\), the second to
\(\mu\sigma\sqrt\pi\operatorname{erfc}((L-\mu)/2\sigma)\). \(\square\)

Write \(I_\sigma(\delta;L)\) for the right-hand side.  Since the integrand is
positive on \([L,\infty)\) for \(L>0\), the value is positive.

## 4. Truncation theorem

### Theorem 4.1

Let \(N\ge2\) satisfy \(L=\log N\ge\max(2,\max_{ij}|\delta_{ij}|)\).  Then:

1. **(Entrywise absolute convergence.)**  For every entry, the untruncated
   series defining \(A_{\mathrm{prime}}(\infty)_{ij}\) converges absolutely.

2. **(Entrywise tail bound.)**

\[
\bigl|A_{\mathrm{prime}}(\infty)_{ij}-A_{\mathrm{prime}}(N)_{ij}\bigr|
\le
E_{ij}(N)
:=
\sqrt\pi\,\sigma
\Bigl[
I_\sigma\bigl(|\delta_{ij}|;L\bigr)
+
I_\sigma\bigl(-|\delta_{ij}|;L\bigr)
\Bigr],
\]

uniformly over all primitive quadratic characters.

3. **(Spectral bound.)**  With \(T=A_{\mathrm{prime}}(\infty)-A_{\mathrm{prime}}(N)\),

\[
\|T\|_2
\le
\max_i\sum_j E_{ij}(N).
\]

4. **(Generalized-eigenvalue shift.)**  For any symmetric \(A\) containing
   \(A_{\mathrm{prime}}(N)\) as a summand and Gram matrix \(B\succ0\), every
   generalized eigenvalue of \((A+T,B)\) differs from the corresponding
   eigenvalue of \((A,B)\) by at most
   \(\max_i\sum_jE_{ij}(N)\,/\,\lambda_{\min}(B)\).

5. **(Rate.)**  \(E_{ij}(N)\to0\) as \(N\to\infty\), Gaussian in \(\log N\).

#### Proof

For a tail term with \(n>N\), bound \(|\beta_\chi(n)|\le(\log n)/\sqrt n\) and
drop the character.  Consider the branch \(G(\delta-\log n)\) with
\(\delta=|\delta_{ij}|\) (the branch \(G(\delta+\log n)\) is the case
\(\delta=-|\delta_{ij}|\) by evenness of \(G\)).  The function

\[
f(x)=\frac{\log x}{\sqrt x}\,e^{-(\log x-\delta)^2/4\sigma^2}
\]

satisfies

\[
\frac{d}{dx}\log f(x)
=
\frac1x\left[\frac1{\log x}-\frac12-\frac{\log x-\delta}{2\sigma^2}\right]<0
\]

whenever \(\log x\ge\max(2,\delta)\), because then \(1/\log x\le1/2\) and
\(\log x\ge\delta\).  Hence \(f\) is decreasing on \([N,\infty)\), and since
prime powers are integers,

\[
\sum_{n>N}\frac{\Lambda(n)}{\sqrt n}\,e^{-(\log n-\delta)^2/4\sigma^2}
\le
\sum_{n>N}f(n)
\le
\int_N^\infty f(x)\,dx
=
\int_L^\infty u\,e^{u/2}e^{-(u-\delta)^2/4\sigma^2}\,du,
\]

using the substitution \(x=e^u\).  Lemma 3.1 evaluates the integral as
\(I_\sigma(\delta;L)\), which is finite; this proves claims 1 and 2.

Claim 3 is the standard bound
\(\|T\|_2\le\sqrt{\|T\|_1\|T\|_\infty}\) for the symmetric matrix \(T\),
whose entries are dominated by the symmetric matrix \(E\), so both norms are
at most the largest row sum of \(E\).

For claim 4, congruence by \(B^{-1/2}\) turns the pencils into ordinary
symmetric eigenproblems for \(B^{-1/2}(A)B^{-1/2}\) and
\(B^{-1/2}(A+T)B^{-1/2}\); Weyl's inequality bounds the shift by
\(\|B^{-1/2}TB^{-1/2}\|_2\le\|T\|_2/\lambda_{\min}(B)\).

Claim 5 follows since \(\operatorname{erfc}(x)\le e^{-x^2}\) for \(x\ge0\)
and \(L-\mu\to\infty\). \(\square\)

### Remark 4.2

The bound discards both the character and the restriction to prime powers, so
it is not tight; empirically it overestimates the true tail by one to two
orders of magnitude, which is acceptable because it decays Gaussian-fast in
\(\log N\).

### Remark 4.3

Claim 4 is evaluated in code with a floating-point
\(\lambda_{\min}(B)\).  A fully certified enclosure would compute
\(\lambda_{\min}(B)\) with directed rounding; this is the natural next
certification step and is deliberately not claimed here.

## 5. Implementation and tests

```text
finite_weil.tail_bounds.prime_tail_entry_bound
finite_weil.tail_bounds.prime_tail_bound_matrix
finite_weil.tail_bounds.prime_tail_spectral_bound
finite_weil.tail_bounds.prime_truncation_eigenvalue_bound
```

`tests/test_tail_bounds.py` checks the closed form against adaptive
quadrature, verifies that the bound dominates the exact integer-sum tail and
an actual deep refinement (`N = 500` versus `N = 200000`), and confirms
monotone decay in the cutoff.

## 6. Consequences

1. The deep-cutoff observations of `paper/09_prime_cutoff_geometry.md` and
   the pole-cancellation observations of `paper/13_pole_cancellation.md` now
   carry explicit truncation budgets rather than empirical stabilization
   arguments.
2. Experiments can *choose* cutoffs from a target error instead of guessing:
   `experiments/zero_recovery.py` and `experiments/sigma_scaling.py` do so.
3. The geometry rule \(\log N\gg2E\) of chapter 9 is subsumed: the bound
   makes the required margin quantitative through the
   \(\operatorname{erfc}((L-\mu)/2\sigma)\) factor.
