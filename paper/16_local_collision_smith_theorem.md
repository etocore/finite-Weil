# Local Smith spectrum on the nondegenerate collision face

## 1. Scope and claim boundary

This note proves the local Smith exponent list for the Jacobian of a common-scale ordered weighted collision after the cluster center has been separated.

The proof uses only:

1. the Vandermonde isomorphism for lower moments;
2. the corrected upper-moment determinant;
3. the translation covector \(\lambda=C^{-\mathsf T}\mathbf 1\);
4. triangularity of the derivative-jet frame.

The result is local on the ordered nondegenerate face

\[
\mathcal B_m^\circ
=
\{\Delta(\xi)\ne0\}
\cap
\left\{\prod_j u_j\ne0\right\}.
\]

It does not yet prove that the corresponding root spaces glue globally as holomorphic bundles, descend to unordered clusters, or extend across nested collisions.

## 2. Collision expansion

Let a cluster be written as

\[
x_j=c+h\xi_j,
\]

where \(c\) is the center, \(h\) is the common collision scale, and \(\xi\) is a normalized ordered shape.

For an analytic target family \(M(x)\), the cluster contribution has Taylor expansion

\[
\mathcal R(h)
=
\sum_{r\ge0}
\frac{h^r}{r!}
U_rM^{(r)}(c),
\qquad
U_r=\sum_{j=1}^m u_j\xi_j^r.
\]

The tangent source variables are:

- \(m\) independent weight variations;
- \(m-1\) centered node variations after the common translation direction has been removed.

Thus the reduced collision Jacobian has source dimension

\[
2m-1.
\]

We study it over the local power-series ring in \(h\).

## 3. Lower root germs

Let

\[
V(\xi)_{rj}=\xi_j^r,
\qquad
0\le r\le m-1.
\]

Because \(\Delta(\xi)\ne0\), the Vandermonde matrix is invertible.

For each \(0\le r\le m-1\), choose a weight variation \(a^{(r)}\) satisfying

\[
V(\xi)a^{(r)}=e_r,
\]

where \(e_r\) is the \(r\)-th standard basis vector. Equivalently,

\[
\delta U_k(a^{(r)})=\delta_{kr},
\qquad
0\le k\le m-1.
\]

The corresponding Jacobian column has expansion

\[
J(h)a^{(r)}
=
\frac{h^r}{r!}M^{(r)}(c)
+O(h^m).
\]

Hence the lower root germs have exact orders

\[
0,1,\ldots,m-1.
\]

Their leading target vectors are

\[
M(c),M'(c),\ldots,M^{(m-1)}(c).
\]

## 4. Corrected centered position map

For a node variation \(\delta\xi\), uniquely correct the weights so that

\[
\delta U_0=\cdots=\delta U_{m-1}=0.
\]

The corrected upper moments are

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
C_{sj}
=
 u_jq_\xi'(\xi_j)H_s(\xi_j).
\]

On \(\mathcal B_m^\circ\),

\[
\det C
=
\pm
\left(\prod_j u_j\right)
\Delta(\xi)^3
\ne0.
\]

Let

\[
E_0
=
\{\delta\xi:\mathbf 1^{\mathsf T}\delta\xi=0\}
\]

be the centered node hyperplane. The reduced position block is

\[
C|_{E_0}:E_0\to\mathbb C^m.
\]

Its image has codimension one.

## 5. Translation-adapted target frame

Define

\[
\lambda=C^{-\mathsf T}\mathbf 1.
\]

Then

\[
\lambda^{\mathsf T}C
=
\mathbf 1^{\mathsf T},
\]

so

\[
\lambda^{\mathsf T}C\delta\xi=0
\]

for every \(\delta\xi\in E_0\).

Choose an invertible target change

\[
T\in GL_m(\mathbb C)
\]

whose first row is \(\lambda^{\mathsf T}\). Then

\[
TC|_{E_0}
=
\begin{pmatrix}
0\\
\widetilde C
\end{pmatrix},
\]

where

\[
\widetilde C:E_0\to\mathbb C^{m-1}
\]

is an isomorphism.

The quotient-polynomial basis \(H_0,\ldots,H_{m-1}\) is triangular relative to the monomial basis. Therefore this target change can be incorporated into an invertible triangular change of the upper derivative jets.

After the vanished translation-dual coordinate is removed, the surviving upper target grades are

\[
m+1,m+2,\ldots,2m-1.
\]

## 6. Upper root germs

Choose a basis

\[
b^{(1)},\ldots,b^{(m-1)}
\]

of \(E_0\) such that

\[
\widetilde Cb^{(s)}=e_s,
\qquad
1\le s\le m-1.
\]

For each \(b^{(s)}\), include the unique lower-moment weight correction.

In the translation-adapted upper target frame, the resulting Jacobian column has leading term

\[
J(h)b^{(s)}
=
\frac{h^{m+s}}{(m+s)!}
\widetilde M_{m+s}(c)
+O(h^{m+s+1}),
\]

for \(1\le s\le m-1\), where the vectors \(\widetilde M_{m+s}(c)\) are the transformed upper derivative jets.

Therefore the upper root germs have exact orders

\[
m+1,m+2,\ldots,2m-1.
\]

Their leading target vectors are independent because \(\widetilde C\) is invertible and the upper target change is invertible.

## 7. Analytic factorization

Collect the lower and upper source root germs into a source matrix \(R(h)\). Its value at \(h=0\) is invertible because:

- the lower weight roots form a basis of the weight tangent space;
- the corrected upper roots project to a basis of \(E_0\).

Collect the corresponding leading target vectors into a target matrix \(L(h)\). Its value at \(h=0\) is invertible because:

- the lower derivative jets are independent in the chosen jet truncation;
- the translation-adapted upper leading vectors are independent;
- lower and upper grades occupy distinct target levels.

Hence the reduced collision Jacobian admits a local factorization

\[
\boxed{
J_{\mathrm{red}}(h)
=
L(h)
\operatorname{diag}
\left(
1,h,\ldots,h^{m-1},
 h^{m+1},\ldots,h^{2m-1}
\right)
R(h),
}
\]

where \(L(h)\) and \(R(h)\) are analytic and invertible at \(h=0\).

This is a Smith factorization over the local analytic ring.

## 8. Local Smith theorem

### Theorem 8.1 - Universal common-scale collision spectrum

On the ordered nondegenerate collision face \(\mathcal B_m^\circ\), after separating the common center coordinate, the reduced collision Jacobian has Smith exponents

\[
\boxed{
E_m
=
\{0,1,\ldots,m-1,m+1,\ldots,2m-1\}.
}
\]

Each exponent occurs with multiplicity one.

The missing exponent \(m\) is the target coordinate dual to the removed common translation direction.

#### Proof

The lower Vandermonde root germs provide the exponents

\[
0,1,\ldots,m-1.
\]

The corrected centered position map has rank \(m-1\). The translation covector removes its unique degree-\(m\) target relation, and the remaining triangular upper jets provide the exponents

\[
m+1,\ldots,2m-1.
\]

The analytic source and target changes constructed above are invertible at \(h=0\), giving the stated Smith factorization. \(\square\)

## 9. Determinant order check

The sum of the exponents is

\[
\sum_{r=0}^{m-1}r
+
\sum_{r=m+1}^{2m-1}r
=
\frac{m(m-1)}2
+
\frac{(m-1)(3m)}2
=
2m(m-1).
\]

Thus every square reduced Jacobian minor representing the full source and target frames has determinant order

\[
\boxed{2m(m-1)}.
\]

This is a consistency check for symbolic and numerical implementations.

## 10. What remains

The local theorem does not yet provide the global root filtration. The next tasks are:

1. show that the lower and upper root lines vary holomorphically across \(\mathcal B_m^\circ\);
2. determine their permutation behavior under relabeling of nodes;
3. descend the filtration to the unordered collision quotient;
4. describe degeneration near vanishing weights and nested collision trees.

## 11. Claim ledger

| Statement | Status |
|---|---|
| Lower root orders \(0,\ldots,m-1\) | Proved by Vandermonde inversion |
| Corrected position block is invertible before centering | Proved by the Vandermonde-cubic determinant |
| Centered upper block has one target relation | Proved |
| Missing relation is dual to common translation | Proved |
| Upper root orders \(m+1,\ldots,2m-1\) | Proved locally by triangular target reduction |
| Local Smith spectrum \(E_m\) | Proved on the ordered nondegenerate face |
| Holomorphic global root filtration | Open |
| Descent to unordered clusters | Open |
| Nested collision spectrum | Open |
