# Minimizer reconstruction and geometry diagnostics

## Finite generalized eigenproblem

Let \(A\) be a real symmetric coordinate matrix and \(B\) the Gaussian-packet Gram matrix. On a numerically stable packet subspace, the smallest generalized eigenvalue is

\[
\lambda_{\min}
=
\min_{c\ne 0}
\frac{c^{\mathsf T}Ac}{c^{\mathsf T}Bc}.
\]

The minimizing coordinate vector is normalized by

\[
c^{\mathsf T}Bc=1.
\]

It reconstructs the ordinary function

\[
f_c(x)=\sum_j c_j g_j(x).
\]

Because \(B_{ij}=\langle g_i,g_j\rangle_{L^2(\mathbb R)}\), the normalization implies

\[
\|f_c\|_{L^2(\mathbb R)}=1.
\]

## Gram whitening

If

\[
B=U\operatorname{diag}(\beta_1,\ldots,\beta_m)U^{\mathsf T},
\]

retain only modes satisfying

\[
\beta_j>\tau\,\beta_{\max}.
\]

Writing

\[
S=U_{\rm ret}\operatorname{diag}(\beta_j^{-1/2}),
\]

the stable generalized problem becomes the ordinary symmetric problem

\[
(S^{\mathsf T}AS)y=\lambda y,
\qquad
c=Sy.
\]

This construction guarantees \(c^{\mathsf T}Bc=1\) when \(y\) has Euclidean norm one.

## Residual

For a reconstructed pair \((\lambda,c)\), define the coordinate residual

\[
r=Ac-\lambda Bc.
\]

The implementation records 

\[
\|r\|_2.
\]

When Gram modes are discarded, the eigenproblem is solved only after projection onto the retained stable subspace. The full-coordinate residual can therefore detect coupling from the retained minimizer into discarded directions. It should not automatically be expected to vanish at machine precision in an ill-conditioned model.

## Boundary localization

For packet centers in \([-L,L]\), define a boundary region by

\[
|x|\ge \eta L,
\qquad 0<\eta<1.
\]

For the normalized reconstructed minimizer, record

\[
M_{\partial}
=
\int_{|x|\ge \eta L}|f_c(x)|^2\,dx.
\]

A persistent value near one under refinement would indicate that the minimizing mode is escaping toward the truncation boundary. A value that decreases or remains small while the minimizer stabilizes would be evidence against a simple boundary artifact.

## Geometry-aware arithmetic cutoff

For packet extent \(L\), pairwise center differences reach \(2L\). The translated Gaussian prime kernel is concentrated near

\[
\log n\approx |t_i-t_j|.
\]

The first geometry experiment therefore chooses the sharp prime cutoff by

\[
\log N\ge 2L+k\sigma,
\]

with a configurable tail parameter \(k\). This is a numerical coverage rule, not yet a rigorous truncation-error theorem.

## Current claim boundary

The implemented reconstruction proves only finite-dimensional linear-algebra identities. The geometry experiment supplies reproducible numerical observations about the compressed operator. It does not establish convergence to an infinite-dimensional Weil operator.
