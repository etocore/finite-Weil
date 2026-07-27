# The missing collision grade as the removed translation direction

## 1. Scope and claim boundary

This note identifies the exact one-dimensional target relation that appears after the common translation direction is removed from an ordered weighted collision chart.

It proves that the relation is not generally the raw equation

\[
\delta U_m=0.
\]

Instead, it is the unique triangular target covector dual to common node translation.

The result supplies the local missing-grade mechanism. It does **not** yet prove the complete Smith spectrum, construct the root filtration as a holomorphic bundle, treat nested collisions, or descend from ordered to unordered clusters.

## 2. Corrected higher-moment map

Let

\[
q_\xi(t)=\prod_{j=1}^m(t-\xi_j)
\]

for pairwise distinct ordered nodes \(\xi_1,\ldots,\xi_m\), and let all weights \(u_j\) be nonzero.

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
0\le s\le m-1,
\]

where \(H_s\) is the quotient polynomial in

\[
t^{m+s}=q_\xi(t)H_s(t)+R_s(t),
\qquad
\deg R_s<m.
\]

Write

\[
C=C^{\mathrm{full}}(\xi,u),
\qquad
C_{sj}=u_jq_\xi'(\xi_j)H_s(\xi_j).
\]

The determinant theorem gives

\[
\det C
=
\pm
\left(\prod_j u_j\right)
\Delta(\xi)^3,
\]

so \(C\) is invertible on the nondegenerate ordered collision face.

## 3. Translation and centered variations

A common infinitesimal translation is the node variation

\[
\delta\xi=a\mathbf 1,
\qquad
\mathbf 1=(1,\ldots,1)^{\mathsf T}.
\]

After the center coordinate has been separated, the remaining node variations lie in the centered hyperplane

\[
E_0
=
\left\{
\delta\xi\in\mathbb C^m:
\mathbf 1^{\mathsf T}\delta\xi=0
\right\}.
\]

The scale direction together with the normalized shape tangent space spans \(E_0\). Thus the reduced upper map is the restriction

\[
C|_{E_0}:E_0\longrightarrow\mathbb C^m.
\]

Since \(C\) is invertible and \(E_0\) has codimension one, the image \(C(E_0)\) also has codimension one.

## 4. Exact target relation

Define

\[
\boxed{
\lambda=C^{-\mathsf T}\mathbf 1.
}
\]

Equivalently, \(\lambda\) is the unique solution of

\[
\boxed{
C^{\mathsf T}\lambda=\mathbf 1.
}
\]

Then for every node variation \(\delta\xi\),

\[
\lambda^{\mathsf T}C\delta\xi
=
\mathbf 1^{\mathsf T}\delta\xi.
\]

Therefore:

### Theorem 4.1 - Translation relation

For every centered node variation \(\delta\xi\in E_0\),

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

Moreover, this relation spans the full left kernel of the reduced map \(C|_{E_0}\).

#### Proof

The identity follows immediately from

\[
\lambda^{\mathsf T}C
=
\mathbf 1^{\mathsf T}.
\]

If \(\delta\xi\in E_0\), then

\[
\mathbf 1^{\mathsf T}\delta\xi=0,
\]

so

\[
\lambda^{\mathsf T}C\delta\xi=0.
\]

Because \(C\) is invertible, \(C(E_0)\) has dimension \(m-1\). Its annihilator is therefore one-dimensional, and the nonzero covector \(\lambda\) spans it. \(\square\)

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
\frac{1}{u_jq_\xi'(\xi_j)}
\qquad
(1\le j\le m).
\]

Thus the polynomial

\[
P_\lambda(t)
=
\sum_{s=0}^{m-1}\lambda_sH_s(t)
\]

is the unique polynomial of degree less than \(m\) interpolating the barycentric-weight data

\[
P_\lambda(\xi_j)
=
\frac{1}{u_jq_\xi'(\xi_j)}.
\]

This explains two features seen in the exploratory computation:

1. the relation depends on the individual weights, not only on symmetric functions of the node shape;
2. it is naturally expressed in the quotient basis \(H_0,\ldots,H_{m-1}\), rather than as the literal vanishing of the first raw upper moment.

## 6. Missing grade after a triangular target change

The quotient polynomials satisfy

\[
H_s(t)=t^s+\text{lower-degree terms}.
\]

Therefore the passage from raw derivative jets

\[
M^{(m)},M^{(m+1)},\ldots,M^{(2m-1)}
\]

to the \(H_s\)-adapted target frame is triangular with nonzero diagonal.

The covector \(\lambda\) identifies one target line as dual to the removed translation direction. Choose any invertible target change whose first row is \(\lambda^{\mathsf T}\). In the transformed target coordinates, the first upper coordinate vanishes identically on centered variations, while the remaining \(m-1\) upper coordinates are independent.

Hence the normalized upper block has grades

\[
m+1,m+2,\ldots,2m-1,
\]

with no independent grade-\(m\) line.

This is the precise local meaning of

\[
\boxed{\operatorname{gr}_m=0.}
\]

The missing grade is the target image of the translation direction removed when the cluster center is separated.

## 7. Consequence for the local exponent list

The lower weight block supplies independent grades

\[
0,1,\ldots,m-1
\]

through the Vandermonde isomorphism

\[
\delta u
\longmapsto
(\delta U_0,\ldots,\delta U_{m-1}).
\]

The centered position block has dimension \(m-1\). After the target relation above is used to remove its first triangular coordinate, the surviving upper grades are

\[
m+1,\ldots,2m-1.
\]

Thus the algebra predicts the local exponent list

\[
\boxed{
E_m
=
\{0,1,\ldots,m-1,m+1,\ldots,2m-1\}.
}
\]

A complete Smith-spectrum theorem still requires construction of root germs with these exact orders and proof that the relevant leading target vectors remain independent throughout the nondegenerate face. This note identifies the algebraic reason for the gap but does not replace that root-germ argument.

## 8. Implementation correspondence

The exact covector is implemented by

```text
finite_weil.collisions.collision_translation_relation
```

which solves

```text
C.T @ lambda = ones(m).
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

## 9. Claim ledger

| Statement | Status |
|---|---|
| Full corrected matrix is invertible on the nondegenerate ordered face | Proved in the preceding note |
| Scale plus normalized shape spans the centered node hyperplane | Elementary linear algebra |
| \(\lambda=C^{-\mathsf T}\mathbf 1\) annihilates the reduced upper image | Proved |
| The missing target relation is dual to removed translation | Proved |
| The relation has a barycentric interpolation description | Proved |
| A triangular target frame removes the raw grade-\(m\) coordinate | Proved locally |
| Complete local Smith spectrum | Next theorem target |
| Holomorphic root filtration on the full face | Open |
| Extension to nested collisions | Open |
| Descent to unordered clusters | Open |
