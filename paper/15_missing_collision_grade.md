# The translation relation in corrected collision moments

## 1. Scope and corrected claim boundary

This note identifies the exact codimension-one relation obtained after common node translation is removed from the corrected upper-moment map.

It proves the coefficient-level identity

\[
\lambda^{\mathsf T}C\delta\xi=0
\]

for centered node variations, where

\[
\lambda=C^{-\mathsf T}\mathbf 1.
\]

This relation is exact. However, it lives before the upper rows are weighted by the collision powers

\[
h^m,h^{m+1},\ldots,h^{2m-1}.
\]

Therefore it does **not** by itself prove that grade \(m\) is absent from the local Smith spectrum. The earlier triangular-target interpretation was too strong and is corrected here.

## 2. Corrected higher-moment map

Let

\[
q_\xi(t)=\prod_{j=1}^m(t-\xi_j)
\]

for pairwise distinct ordered nodes, with nonzero weights \(u_j\).

After the unique weight correction satisfying

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
C=C^{\mathrm{full}}(\xi,u),
\qquad
C_{sj}=u_jq_\xi'(\xi_j)H_s(\xi_j).
\]

The determinant formula gives

\[
\det C
=
\pm
\left(\prod_j u_j\right)
\Delta(\xi)^3,
\]

so \(C\) is invertible on the nondegenerate ordered face.

## 3. Translation and centered variations

A common infinitesimal translation is

\[
\delta\xi=a\mathbf 1,
\qquad
\mathbf 1=(1,\ldots,1)^{\mathsf T}.
\]

After the center coordinate has been separated, the remaining node variations lie in

\[
E_0
=
\left\{
\delta\xi\in\mathbb C^m:
\mathbf 1^{\mathsf T}\delta\xi=0
\right\}.
\]

Because \(C\) is invertible and \(E_0\) has codimension one, the image \(C(E_0)\) also has codimension one.

## 4. Exact translation covector

Define

\[
\boxed{
\lambda=C^{-\mathsf T}\mathbf 1.
}
\]

Equivalently,

\[
\boxed{
C^{\mathsf T}\lambda=\mathbf 1.
}
\]

Then for every node variation,

\[
\lambda^{\mathsf T}C\delta\xi
=
\mathbf 1^{\mathsf T}\delta\xi.
\]

Therefore:

### Theorem 4.1 - Translation relation

For every centered variation \(\delta\xi\in E_0\),

\[
\boxed{
\lambda^{\mathsf T}
\begin{pmatrix}
\delta U_m\\
\delta U_{m+1}\\
\vdots\\
\delta U_{2m-1}
\end{pmatrix}
=0.
}
\]

Moreover, this relation spans the full left kernel of \(C|_{E_0}\).

#### Proof

Since

\[
\lambda^{\mathsf T}C
=
\mathbf 1^{\mathsf T},
\]

we obtain

\[
\lambda^{\mathsf T}C\delta\xi
=
\mathbf 1^{\mathsf T}\delta\xi
=0
\]

for every \(\delta\xi\in E_0\). The image \(C(E_0)\) has dimension \(m-1\), so its annihilator is one-dimensional. \(\square\)

## 5. Interpolation description

Factor

\[
C
=
A_H
\operatorname{diag}
\left(u_jq_\xi'(\xi_j)\right),
\]

where

\[
(A_H)_{sj}=H_s(\xi_j).
\]

The equation

\[
C^{\mathsf T}\lambda=\mathbf 1
\]

is equivalent to

\[
\sum_{s=0}^{m-1}\lambda_sH_s(\xi_j)
=
\frac{1}{u_jq_\xi'(\xi_j)}.
\]

Thus

\[
P_\lambda(t)
=
\sum_{s=0}^{m-1}\lambda_sH_s(t)
\]

is the unique polynomial of degree less than \(m\) satisfying

\[
P_\lambda(\xi_j)
=
\frac{1}{u_jq_\xi'(\xi_j)}.
\]

This gives a barycentric interpolation formula for the translation covector.

## 6. Why this does not yet remove grade m

The actual upper collision contribution is weighted by

\[
D_m(h)
=
\operatorname{diag}
\left(h^m,h^{m+1},\ldots,h^{2m-1}\right).
\]

The \(h\)-weighted upper block is

\[
D_m(h)C|_{E_0}.
\]

Although

\[
\lambda^{\mathsf T}C|_{E_0}=0,
\]

one does not generally have

\[
\lambda^{\mathsf T}D_m(h)C|_{E_0}=0.
\]

To convert the unweighted relation into a relation among the weighted rows would require coefficients involving negative powers of \(h\). Such operations are not allowed over the local analytic ring used in Smith theory.

Therefore the translation relation proves a coefficient-level codimension-one statement, but not an \(h\)-adic missing-grade theorem.

## 7. Implementation correspondence

The exact covector is implemented by

```text
finite_weil.collisions.collision_translation_relation
```

which solves

```text
C.T @ lambda = ones(m)
```

Regression tests verify

\[
C^{\mathsf T}\lambda=\mathbf 1
\]

and

\[
\lambda^{\mathsf T}C\delta\xi=0
\]

for centered variations.

## 8. Revised theorem target

The missing exponent \(m\) requires an additional \(h\)-compatible mechanism. The next calculation must use the exact Jacobian from the singular-value experiments and determine whether:

1. the degree-\(m\) coefficient vanishes after the true source normalization;
2. an analytic source correction raises its order;
3. a center-scale Schur complement cancels it;
4. the observed exponent list belongs to a different reduced matrix.

## 9. Claim ledger

| Statement | Status |
|---|---|
| Full corrected matrix is invertible on the nondegenerate ordered face | Proved |
| \(\lambda=C^{-\mathsf T}\mathbf 1\) annihilates the unweighted centered image | Proved |
| Translation relation has a barycentric interpolation description | Proved |
| Translation relation alone removes grade \(m\) | False |
| Constant triangular target change proves \(\operatorname{gr}_m=0\) | False in general |
| Complete local Smith spectrum | Open |
| Exact h-compatible missing-grade mechanism | Immediate theorem target |
| Holomorphic global root filtration | Open |
| Extension to nested collisions | Open |
| Descent to unordered clusters | Open |
