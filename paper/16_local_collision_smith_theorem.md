# The h-adic obstruction to the proposed local Smith factorization

## 1. Scope

This note records and corrects a failed attempt to deduce the local collision Smith spectrum directly from the translation relation

\[
\lambda^{\mathsf T}C=\mathbf 1^{\mathsf T}.
\]

The relation is exact and remains useful. However, it lives in the unweighted corrected-moment coordinates. The local Smith problem is governed by the \(h\)-weighted jet matrix, and the grading prevents the relation from being used as an ordinary analytic row operation.

Consequently, the exponent list

\[
\{0,1,\ldots,m-1,m+1,\ldots,2m-1\}
\]

is **not proved** by the translation relation alone.

## 2. Unweighted corrected position map

After correcting weights so that

\[
\delta U_0=\cdots=\delta U_{m-1}=0,
\]

the higher moments satisfy

\[
\delta U_{m+s}
=
\sum_{j=1}^m
u_jq_\xi'(\xi_j)H_s(\xi_j)\,\delta\xi_j,
\qquad
0\le s\le m-1.
\]

Write

\[
C_{sj}=u_jq_\xi'(\xi_j)H_s(\xi_j).
\]

On the nondegenerate ordered face,

\[
\det C
=
\pm
\left(\prod_j u_j\right)
\Delta(\xi)^3
\ne0.
\]

For centered variations

\[
E_0
=
\{\delta\xi:\mathbf 1^{\mathsf T}\delta\xi=0\},
\]

define

\[
\lambda=C^{-\mathsf T}\mathbf 1.
\]

Then

\[
\lambda^{\mathsf T}C\delta\xi=0
\qquad
(\delta\xi\in E_0).
\]

This is an exact codimension-one relation in the unweighted upper-moment space.

## 3. The actual h-weighted upper block

In the collision expansion, the target jets occur with different powers of the collision scale:

\[
\sum_{s=0}^{m-1}
\frac{h^{m+s}}{(m+s)!}
\delta U_{m+s}M^{(m+s)}(c).
\]

Ignoring the nonzero factorials, the upper coefficient matrix is therefore

\[
D_m(h)C|_{E_0},
\]

where

\[
D_m(h)
=
\operatorname{diag}
\left(h^m,h^{m+1},\ldots,h^{2m-1}\right).
\]

The relation

\[
\lambda^{\mathsf T}C|_{E_0}=0
\]

does not imply

\[
\lambda^{\mathsf T}D_m(h)C|_{E_0}=0.
\]

The diagonal grading matrix does not commute with the constant row covector unless the relation is supported in a single grade.

## 4. Why the previous triangular argument fails

To transfer the unweighted relation to the weighted block, one would need a row covector of the form

\[
\left(
\lambda_0,
 h^{-1}\lambda_1,
 \ldots,
 h^{-(m-1)}\lambda_{m-1}
\right),
\]

up to a common factor.

Such a transformation contains negative powers of \(h\). It is not invertible over the local analytic ring

\[
\mathbb C\{h\}
\]

and is therefore not an allowed Smith row operation.

Thus an arbitrary constant target change whose first row is \(\lambda^{\mathsf T}\) is not grade preserving. It can mix higher-order rows into the degree-\(m\) row but cannot remove the lowest \(h\)-adic term by an analytic unimodular transformation.

## 5. Small-dimensional diagnostic

The obstruction is already visible for \(m=2\).

The centered node space has dimension one. Write its nonzero generator as \(v\). The weighted upper block is the single column

\[
\begin{pmatrix}
 h^2(Cv)_0\\
 h^3(Cv)_1
\end{pmatrix}.
\]

If

\[
(Cv)_0\ne0,
\]

then the Smith exponent of this column is \(2\), because the greatest common divisor of its entries has order \(2\).

The unweighted relation between \((Cv)_0\) and \((Cv)_1\) does not change that valuation.

Therefore a missing exponent \(m\) requires an additional structural cancellation forcing the degree-\(m\) coefficient itself to vanish after the correct source normalization. It cannot follow merely from the existence of a left kernel of \(C|_{E_0}\).

## 6. Correct status of the translation relation

The identity

\[
\lambda=C^{-\mathsf T}\mathbf 1
\]

still proves:

1. the centered corrected-position image has codimension one in the unweighted upper-moment space;
2. the missing target relation is dual to common translation at the coefficient level;
3. the relation has a barycentric interpolation description;
4. the coefficients depend on both shape and weights.

It does **not** yet prove:

1. that the degree-\(m\) coefficient vanishes;
2. that an analytic target transformation removes grade \(m\);
3. that the upper Smith exponents begin at \(m+1\);
4. the complete local Smith spectrum.

## 7. Revised theorem target

The missing-grade theorem must establish an \(h\)-compatible cancellation. At least one of the following must occur in the actual collision Jacobian:

1. the degree-\(m\) corrected coefficient vanishes identically on the correctly normalized source tangent space;
2. the source chart contains an \(h\)-dependent analytic correction that raises the first upper root by one order;
3. coupling with the center or scale column produces an analytic Schur complement whose first upper coefficient cancels;
4. the experimentally observed singular-value list belongs to a different reduced matrix than \(D_m(h)C|_{E_0}\).

The next task is to reconstruct the exact Jacobian used in the numerical experiments, including all center, scale, weight, and normalization columns, and compute its \(h\)-adic minors directly.

## 8. Claim ledger

| Statement | Status |
|---|---|
| Corrected upper determinant equals \(\pm(\prod u_j)\Delta^3\) | Proved |
| Translation covector satisfies \(C^{\mathsf T}\lambda=\mathbf 1\) | Proved |
| Translation covector annihilates the unweighted centered image | Proved |
| Constant triangular target change removes grade \(m\) | False in general |
| Translation relation alone proves the missing exponent | False |
| Universal local Smith spectrum | Open |
| Exact h-compatible missing-grade mechanism | Immediate theorem target |
