# General cluster normal form for finite exponential packet realizations

## Status

This note proves the full cluster version of the collision theorem for the finite exponential moment map

\[
\mathcal R_N(X,u)
=
(a_0,\ldots,a_{2N-1}),
\qquad
 a_k=\sum_{j=1}^N u_jx_j^k.
\]

Suppose \(m\ge2\) nodes approach one point at a common scale,

\[
x_j(h)=x+h\xi_j,
\qquad 1\le j\le m,
\]

where the offsets \(\xi_1,\ldots,\xi_m\) are fixed and pairwise distinct. All remaining nodes stay separated from \(x\), and all coefficients have nonzero limits.

The Jacobian admits a bounded-equivalence normal form whose cluster exponents are

\[
\boxed{
0,0,1,2,\ldots,m-1,m+1,m+2,\ldots,2m-1.
}
\]

Equivalently, among the \(2m\) cluster directions, exactly \(2m-2\) collapse, with orders

\[
\boxed{
1,2,\ldots,m-1,m+1,m+2,\ldots,2m-1.
}
\]

The exponent \(m\) is absent. Consequently,

\[
\boxed{
\kappa_{\mathrm{abs}}(J(h))\asymp |h|^{-(2m-1)}.
}
\]

The proof uses two dual interpolation systems:

1. ordinary Vandermonde duality for derivative-column combinations;
2. Hermite coefficient extraction for value-column combinations.

The underlying Vandermonde, confluent Vandermonde, Hermite interpolation, and clustered-Prony ingredients are classical. The packet-specific contribution here is the explicit bounded-equivalence construction and its geometric interpretation. No novelty claim is made until the exponent hierarchy is compared line by line with the existing structured-matrix and Prony literature.

---

## 1. Setup

Let

\[
M(z)
=
(1,z,z^2,\ldots,z^{2N-1})^{\mathsf T}\in\mathbb C^{2N}.
\]

Fix an integer

\[
2\le m\le N.
\]

Let the first \(m\) nodes form a cluster

\[
x_j(h)=x+h\xi_j,
\qquad 1\le j\le m,
\]

where

\[
\xi_i\ne\xi_j
\qquad(i\ne j).
\]

Let the remaining nodes

\[
x_{m+1},\ldots,x_N
\]

be fixed and pairwise distinct, with

\[
x_j\ne x
\qquad(j>m).
\]

Assume

\[
u_j(h)\longrightarrow u_j(0)\ne0
\]

for every \(j\).

After a fixed column permutation, write the Jacobian in grouped value-then-motion coordinates. Define the unweighted confluent matrix

\[
C(h)
=
\bigl[
M(x_1(h)),\ldots,M(x_N(h)),
M'(x_1(h)),\ldots,M'(x_N(h))
\bigr]
\]

and the diagonal coefficient matrix

\[
U(h)
=
\operatorname{diag}
\bigl(
1,\ldots,1,
 u_1(h),\ldots,u_N(h)
\bigr).
\]

Then

\[
J(h)=C(h)U(h).
\]

Because every limiting coefficient is nonzero, \(U(h)\) and \(U(h)^{-1}\) are uniformly bounded for sufficiently small \(h\). Thus the singular exponents are determined by \(C(h)\).

---

## 2. Vandermonde-dual derivative modes

Let

\[
V_\xi
=
(\xi_j^q)_{
0\le q\le m-1,
1\le j\le m}.
\]

Since the offsets are distinct, \(V_\xi\) is invertible.

For each

\[
0\le q\le m-1,
\]

let

\[
b^{(q)}=(b_1^{(q)},\ldots,b_m^{(q)})^{\mathsf T}
\]

be the unique vector satisfying

\[
\sum_{j=1}^m b_j^{(q)}\xi_j^s
=
\delta_{qs},
\qquad
0\le s\le m-1.
\]

Define the derivative mode

\[
D_q(h)
:=
\sum_{j=1}^m b_j^{(q)}M'(x+h\xi_j).
\]

Taylor expansion gives

\[
M'(x+h\xi_j)
=
\sum_{s\ge0}
\frac{h^s\xi_j^s}{s!}
M^{(s+1)}(x).
\]

Therefore

\[
D_q(h)
=
\frac{h^q}{q!}M^{(q+1)}(x)
+O(h^{q+1}).
\]

Hence

\[
\widehat D_q(h)
:=
h^{-q}D_q(h)
\]

extends holomorphically through \(h=0\), with

\[
\widehat D_q(0)
=
\frac1{q!}M^{(q+1)}(x).
\]

The derivative modes supply the exponents

\[
0,1,2,\ldots,m-1
\]

and the limiting jets

\[
M'(x),M''(x),\ldots,M^{(m)}(x).
\]

---

## 3. Hermite coefficient-extraction modes

Let

\[
\mathcal P_{2m-1}
=
\{p\in\mathbb C[t]:\deg p\le2m-1\}.
\]

The Hermite data map

\[
\mathcal H_\xi:
\mathcal P_{2m-1}
\longrightarrow
\mathbb C^{2m},
\]

\[
p
\longmapsto
\bigl(
 p(\xi_1),\ldots,p(\xi_m),
 p'(\xi_1),\ldots,p'(\xi_m)
\bigr)
\]

is an isomorphism.

Define the degree set

\[
R_m
:=
\{0\}\cup\{m+1,m+2,\ldots,2m-1\}.
\]

It contains exactly \(m\) integers.

For each \(r\in R_m\), let

\[
a^{(r)}=(a_1^{(r)},\ldots,a_m^{(r)})^{\mathsf T},
\qquad
c^{(r)}=(c_1^{(r)},\ldots,c_m^{(r)})^{\mathsf T}
\]

be the unique Hermite weights representing the coefficient extractor

\[
[t^r]p.
\]

Thus, for every \(p\in\mathcal P_{2m-1}\),

\[
[t^r]p
=
\sum_{j=1}^m a_j^{(r)}p(\xi_j)
+
\sum_{j=1}^m c_j^{(r)}p'(\xi_j).
\]

Equivalently,

\[
\sum_{j=1}^m a_j^{(r)}\xi_j^s
+
s\sum_{j=1}^m c_j^{(r)}\xi_j^{s-1}
=
\delta_{rs},
\qquad
0\le s\le2m-1.
\]

Define the value-corrected mode

\[
V_r(h)
:=
\sum_{j=1}^m a_j^{(r)}M(x+h\xi_j)
+
h\sum_{j=1}^m c_j^{(r)}M'(x+h\xi_j).
\]

Taylor expansion gives

\[
V_r(h)
=
\sum_{s\ge0}
\frac{h^s}{s!}
\left(
\sum_j a_j^{(r)}\xi_j^s
+s\sum_j c_j^{(r)}\xi_j^{s-1}
\right)
M^{(s)}(x).
\]

The coefficient-extraction identities imply

\[
V_r(h)
=
\frac{h^r}{r!}M^{(r)}(x)
+O(h^{2m})
\]

when \(r\le2m-1\). In particular,

\[
\widehat V_r(h)
:=
h^{-r}V_r(h)
\]

extends holomorphically through \(h=0\), and

\[
\widehat V_r(0)
=
\frac1{r!}M^{(r)}(x).
\]

These modes supply the exponents

\[
0,m+1,m+2,\ldots,2m-1
\]

and the limiting jets

\[
M(x),M^{(m+1)}(x),\ldots,M^{(2m-1)}(x).
\]

Together with the derivative modes, every jet

\[
M^{(0)}(x),M^{(1)}(x),\ldots,M^{(2m-1)}(x)
\]

appears exactly once.

---

## 4. Invertibility of the column transformation

The transformed cluster columns are obtained from the original \(2m\) cluster columns by a matrix \(P_m(h)\).

At \(h=0\), after fixed row and column permutations, \(P_m(0)\) is block diagonal:

\[
P_m(0)
\sim
\begin{pmatrix}
A_m&0\\
0&B_m
\end{pmatrix},
\]

where

\[
A_m
=
\bigl(a^{(r)}\bigr)_{r\in R_m}
\]

and

\[
B_m
=
\bigl(b^{(q)}\bigr)_{0\le q\le m-1}.
\]

The matrix \(B_m\) is invertible because it is the dual Vandermonde matrix.

The nontrivial point is the value-weight block \(A_m\).

### Lemma 4.1 - value-weight determinant

Let

\[
\Delta(\xi)
:=
\prod_{1\le i<j\le m}(\xi_j-\xi_i).
\]

Then

\[
\boxed{
\det A_m
=
\pm\frac{m!}{\Delta(\xi)^3}.
}
\]

In particular, \(A_m\) is invertible.

### Proof

Let \(H_\xi\) be the \(2m\times2m\) matrix of the Hermite data map in the monomial basis

\[
1,t,\ldots,t^{2m-1}.
\]

The rows indexed by value data are

\[
(1,\xi_j,\ldots,\xi_j^{2m-1}),
\]

and the derivative rows are

\[
(0,1,2\xi_j,\ldots,(2m-1)\xi_j^{2m-2}).
\]

The rows of \(H_\xi^{-1}\) are the Hermite representations of the coefficient extractors. The block \(A_m\) is the minor of \(H_\xi^{-1}\) with

- coefficient rows indexed by
  \[
  R_m=\{0,m+1,\ldots,2m-1\},
  \]
- data columns indexed by the \(m\) value evaluations.

Jacobi's complementary-minor identity gives

\[
\det A_m
=
\pm
\frac{
\det H_\xi[
\text{derivative rows},
\{1,2,\ldots,m\}
]
}{\det H_\xi}.
\]

The complementary numerator is

\[
\det(r\xi_j^{r-1})_{
1\le j,r\le m}
=
m!\,\Delta(\xi).
\]

The confluent Vandermonde determinant is

\[
\det H_\xi
=
\pm\Delta(\xi)^4.
\]

Therefore

\[
\det A_m
=
\pm\frac{m!}{\Delta(\xi)^3}.
\]

This is nonzero because the offsets are distinct. \(\square\)

It follows that

\[
\det P_m(0)\ne0.
\]

Since \(P_m(h)\) depends polynomially on \(h\), both \(P_m(h)\) and \(P_m(h)^{-1}\) remain uniformly bounded for sufficiently small \(h\).

Extend \(P_m(h)\) by the identity on all noncluster columns and denote the full matrix by \(P(h)\).

---

## 5. The regular factor

Order the transformed cluster columns as

\[
V_0,
D_0,D_1,\ldots,D_{m-1},
V_{m+1},\ldots,V_{2m-1}.
\]

Let \(A(h)\) be the matrix formed by the normalized transformed columns

\[
\widehat V_0,
\widehat D_0,
\widehat D_1,\ldots,
\widehat D_{m-1},
\widehat V_{m+1},\ldots,
\widehat V_{2m-1}
\]

followed by the unmodified value and derivative columns at the noncluster nodes.

At \(h=0\), the cluster part of \(A(0)\) is, up to nonzero factorial scalings,

\[
M(x),M'(x),M''(x),\ldots,M^{(2m-1)}(x).
\]

The remaining columns are

\[
M(x_j),M'(x_j),
\qquad j>m.
\]

Thus \(A(0)^{\mathsf T}\) is the generalized Hermite data map with

- multiplicity \(2m\) at \(x\);
- multiplicity \(2\) at every remaining node.

The total number of data is

\[
2m+2(N-m)=2N.
\]

Generalized Hermite interpolation gives:

### Lemma 5.1

\[
A(0)
\]

is invertible.

Consequently, \(A(h)\), \(A(h)^{-1}\), and their operator norms remain uniformly bounded near \(h=0\).

---

## 6. Exact bounded-equivalence normal form

Define the diagonal scale matrix \(D_m(h)\) by assigning exponent

\[
0
\]

to \(V_0\), exponent

\[
q
\]

to \(D_q\), and exponent

\[
r
\]

to \(V_r\). All noncluster columns receive exponent zero.

After ordering the diagonal entries nondecreasingly,

\[
D_m(h)
=
\operatorname{diag}
\Bigl(
\underbrace{1,\ldots,1}_{2N-2m+2},
 h,h^2,\ldots,h^{m-1},
 h^{m+1},\ldots,h^{2m-1}
\Bigr).
\]

The construction gives the exact identity

\[
C(h)P(h)=A(h)D_m(h).
\]

Therefore

\[
\boxed{
J(h)=A(h)D_m(h)B(h),
\qquad
B(h):=P(h)^{-1}U(h).
}
\]

Both \(A(h)\), \(B(h)\), and their inverses are uniformly bounded near \(h=0\).

---

## 7. Main theorem

### Theorem 7.1 - \(m\)-node cluster normal form

Under the setup above, the Jacobian admits a bounded-equivalence factorization

\[
J(h)=A(h)D_m(h)B(h)
\]

with uniformly invertible regular factors and diagonal exponent list

\[
\boxed{
\underbrace{0,\ldots,0}_{2N-2m+2},
1,2,\ldots,m-1,
 m+1,m+2,\ldots,2m-1.
}
\]

Let

\[
\sigma_1(J(h))\ge\cdots\ge\sigma_{2N}(J(h)).
\]

Then the first

\[
2N-2m+2
\]

singular values remain bounded above and below by positive constants, while the remaining singular values satisfy

\[
\boxed{
\sigma_{2N-2m+2+r}(J(h))
\asymp
|h|^r,
\qquad
1\le r\le m-1,
}
\]

and

\[
\boxed{
\sigma_{2N-m+1+s}(J(h))
\asymp
|h|^{m+s},
\qquad
1\le s\le m-1.
}
\]

Equivalently, the collapsing singular-value exponents are

\[
\boxed{
1,2,\ldots,m-1,m+1,m+2,\ldots,2m-1.
}
\]

### Proof

The exact factorization was established above. For invertible matrices \(L,R\), singular values obey

\[
\sigma_{\min}(L)\sigma_{\min}(R)\sigma_k(M)
\le
\sigma_k(LMR)
\le
\|L\|\|R\|\sigma_k(M).
\]

Apply these inequalities to

\[
J(h)=A(h)D_m(h)B(h).
\]

The regular factors and their inverses are uniformly bounded, while the singular values of the diagonal matrix are exactly the absolute values of its diagonal entries. \(\square\)

---

## 8. Condition number and metric degeneration

### Corollary 8.1 - condition-number exponent

The smallest singular value satisfies

\[
\boxed{
\sigma_{2N}(J(h))\asymp |h|^{2m-1}.
}
\]

Therefore

\[
\boxed{
\kappa_{\mathrm{abs}}(J(h))
=
\|J(h)^{-1}\|
\asymp
|h|^{-(2m-1)}.
}
\]

Because the largest singular value remains bounded above and below,

\[
\operatorname{cond}J(h)
\asymp
|h|^{-(2m-1)}.
\]

Let

\[
G(h)=J(h)^*J(h).
\]

The collapsing pullback-metric eigenvalue exponents are twice the Jacobian exponents:

\[
\boxed{
2,4,\ldots,2m-2,
2m+2,2m+4,\ldots,4m-2.
}
\]

---

## 9. Determinant compatibility

The exact Jacobian determinant contains the cluster factor

\[
\prod_{1\le i<j\le m}
|x_j(h)-x_i(h)|^4.
\]

Since

\[
x_j(h)-x_i(h)
=
h(\xi_j-\xi_i),
\]

this contributes

\[
|h|^{4\binom m2}
=
|h|^{2m(m-1)}.
\]

The sum of the collapsing singular exponents is

\[
\sum_{r=1}^{m-1}r
+
\sum_{r=m+1}^{2m-1}r
=
2m(m-1).
\]

Thus the normal form resolves the determinant order exactly:

\[
\boxed{
\prod_{\text{collapsing directions}}
|h|^{e_r}
=
|h|^{2m(m-1)}.
}
\]

The missing exponent \(m\) is forced by the coexistence of

- \(m\) derivative-dual modes with exponents \(0,\ldots,m-1\), and
- \(m\) value-Hermite modes with exponents \(0,m+1,\ldots,2m-1\).

---

## 10. Three-node corollary

For \(m=3\), the cluster exponent list is

\[
\boxed{
0,0,1,2,4,5.
}
\]

Hence exactly four singular values collapse:

\[
\boxed{
|h|,
|h|^2,
|h|^4,
|h|^5.
}
\]

In the full \(2N\times2N\) Jacobian,

\[
\sigma_{2N-3}(J(h))\asymp|h|,
\]

\[
\sigma_{2N-2}(J(h))\asymp|h|^2,
\]

\[
\sigma_{2N-1}(J(h))\asymp|h|^4,
\]

and

\[
\sigma_{2N}(J(h))\asymp|h|^5.
\]

Therefore

\[
\boxed{
\kappa_{\mathrm{abs}}(J(h))\asymp|h|^{-5}.
}
\]

The determinant order is

\[
1+2+4+5=12
=
4\binom32.
\]

---

## 11. Relation to confluent coordinates

The normalized regular factor contains the full confluent jet block

\[
M(x),M'(x),\ldots,M^{(2m-1)}(x).
\]

This shows that the ordinary packet chart degenerates because it attempts to describe a multiplicity-\(2m\) confluent object using \(m\) separate value-motion pairs.

The normal form identifies the renormalizations required to pass to a nonsingular confluent chart. The singular scales are not arbitrary numerical artifacts: they are the exact powers needed to recover the successive jet coordinates.

A remaining geometric question is whether the pullback metric, after these anisotropic renormalizations, extends smoothly or only stratifiably across the confluent boundary.

---

## 12. Proven versus open

### Proven here

- A uniformly invertible column transformation for every fixed cluster shape with distinct offsets.
- An exact bounded-equivalence factorization for an arbitrary \(m\)-node cluster.
- The full singular-value exponent hierarchy
  \[
  1,\ldots,m-1,m+1,\ldots,2m-1.
  \]
- The condition-number law
  \[
  \kappa_{\mathrm{abs}}\asymp|h|^{-(2m-1)}.
  \]
- The exact agreement between the singular exponent sum and the determinant collision order.
- The three-node hierarchy
  \[
  1,2,4,5.
  \]

### Still open

- Exact leading constants for all cluster singular values.
- A canonical unitary, rather than bounded-equivalence, normal form.
- Multiple clusters collapsing at different scales.
- Nonuniform cluster paths in which pairwise distances have different powers of \(h\).
- Metric completion and curvature near higher confluent strata.
- Sharp global conditioning bounds combining cluster size, shape, separation, coefficient size, and node radius.

---

## 13. Literature boundary

Collision geometry of Prony maps, confluent Prony systems, and clustered Vandermonde matrices has a substantial existing literature. Relevant starting points include:

- D. Batenkov and Y. Yomdin, *On the Accuracy of Solving Confluent Prony Systems*, SIAM Journal on Applied Mathematics 73 (2013), 134-154.
- D. Batenkov and Y. Yomdin, *Geometry and Singularities of the Prony Mapping*, arXiv:1301.1336.
- D. Batenkov, L. Demanet, G. Goldman, and Y. Yomdin, *Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes*, SIAM Journal on Matrix Analysis and Applications 41 (2020), 199-220.
- D. Batenkov, B. Diederichs, G. Goldman, and Y. Yomdin, *The Spectral Properties of Vandermonde Matrices with Clustered Nodes*, arXiv:1909.01927.
- S. Kunis and D. Nagel, *On the Smallest Singular Value of Multivariate Vandermonde Matrices with Clustered Nodes*, arXiv:1907.07119.

The cited literature already treats collisions, confluent Prony geometry, and clustered Vandermonde spectra in substantial depth. This note should be treated as a self-contained derivation in the present packet coordinates, not as evidence that the hierarchy is new. A dedicated comparison is required before any originality statement.