# Local Smith form of the packet realization Jacobian

## Status

This note places the established common-scale packet factorization in the classical local theory of regular analytic matrix functions.

The main point is conceptual:

\[
J(h,p)=A(h,p)D_m(h)B(h,p)
\]

is not merely an adapted conditioning factorization. For every fixed nondegenerate auxiliary parameter \(p\), it is a local analytic Smith form of the one-parameter matrix function \(h\mapsto J(h,p)\).

The packet calculation therefore determines the local partial multiplicities explicitly.

No new existence theorem for Smith forms is claimed here. The new packet-specific information is the computed exponent multiset, its missing middle exponent, and the metric refinement developed elsewhere in the repository.

---

## 1. Setting

Consider the square finite moment realization

\[
\mathcal R_N(X,u)
=
\left(
\sum_{j=1}^N u_jx_j^k
\right)_{k=0}^{2N-1}
\]

and its Jacobian

\[
J=D\mathcal R_N.
\]

For an ordered cluster of size \(m\ge2\), write

\[
x_j=x+h\xi_j,
\qquad
1\le j\le m,
\]

where the normalized offsets are pairwise distinct. Let \(p\) denote all auxiliary variables other than the collision scale \(h\):

\[
p=(x,\xi,u,y,v).
\]

Assume:

1. the normalized offsets \(\xi_i\) are pairwise distinct;
2. the exterior nodes are separated from the cluster center and from one another;
3. all limiting coefficients are nonzero.

The varying-shape normal-form theorem proves that on a product neighborhood of \((0,p_0)\),

\[
\boxed{
J(h,p)=A(h,p)D_m(h)B(h,p),
}
\]

where \(A,B,A^{-1},B^{-1}\) are jointly holomorphic and

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

For the local Smith discussion, fix \(p\) in this neighborhood and regard \(J(h,p)\) as a one-variable holomorphic matrix function of \(h\).

---

## 2. Local analytic equivalence

Let \(\mathcal O_0\) denote the local ring of germs of holomorphic functions in \(h\) at \(h=0\).

Two square matrix germs \(M_1,M_2\in\operatorname{Mat}_n(\mathcal O_0)\) are locally analytically equivalent if

\[
M_1(h)=E(h)M_2(h)F(h),
\]

where

\[
E,F\in GL_n(\mathcal O_0).
\]

The ring \(\mathcal O_0\) is a discrete valuation ring with valuation

\[
\nu(f)=\operatorname{ord}_{h=0}f.
\]

A local Smith form is a diagonal representative

\[
\operatorname{diag}
\left(
 h^{\alpha_1},\ldots,h^{\alpha_n}
\right),
\qquad
0\le\alpha_1\le\cdots\le\alpha_n,
\]

under local analytic equivalence. The integers \(\alpha_i\) are the local partial multiplicities.

---

## 3. Packet local Smith theorem

### Theorem 3.1 - local Smith partial multiplicities

Fix a nondegenerate auxiliary parameter \(p\) in the varying-shape normal-form neighborhood. Then the germ \(h\mapsto J(h,p)\) is regular and has local Smith form

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

Equivalently, its local partial multiplicities are

\[
\boxed{
\underbrace{0,\ldots,0}_{2N-2m+2},
1,2,\ldots,m-1,
m+1,\ldots,2m-1.
}
\]

### Proof

The established varying-shape factorization gives

\[
J(h,p)=A(h,p)D_m(h)B(h,p).
\]

For fixed \(p\), the matrices \(A(h,p)\) and \(B(h,p)\) are holomorphic in \(h\), and

\[
\det A(0,p)\ne0,
\qquad
\det B(0,p)\ne0.
\]

Hence their germs belong to

\[
GL_{2N}(\mathcal O_0).
\]

Thus \(J\) is locally analytically equivalent to \(D_m\).

The exponents in \(D_m\) are nonnegative and nondecreasing. Therefore \(D_m\) is already in local Smith form. The displayed exponents are consequently the local partial multiplicities of \(J\). \(\square\)

---

## 4. The missing exponent is an analytic invariant

### Corollary 4.1

The absence of exponent \(m\) from the packet list

\[
1,2,\ldots,m-1,m+1,\ldots,2m-1
\]

is invariant under arbitrary holomorphic changes of source and target frame that remain invertible at the collision face.

### Proof

Local partial multiplicities are invariants of local analytic equivalence. Multiplication on the left or right by a matrix in

\[
GL_{2N}(\mathcal O_0)
\]

cannot change the Smith exponents. Since \(m\) is absent from the computed local Smith form, it remains absent after every such frame change. \(\square\)

### Remark 4.2

This is stronger than saying that one particular construction of \(A,D,B\) happens to omit \(m\). The gap belongs to the analytic equivalence class of the packet Jacobian germ.

---

## 5. Determinant order

### Corollary 5.1

The collision order of the determinant is

\[
\boxed{
\operatorname{ord}_{h=0}\det J(h,p)
=
2m(m-1).
}
\]

### Proof

The valuation of the determinant equals the sum of the local partial multiplicities. The zero exponents do not contribute, so

\[
\operatorname{ord}_{h=0}\det J
=
\sum_{q=1}^{m-1}q
+
\sum_{q=m+1}^{2m-1}q.
\]

Now

\[
\sum_{q=1}^{m-1}q
=
\frac{m(m-1)}2,
\]

and

\[
\sum_{q=m+1}^{2m-1}q
=
\frac{(m-1)(3m)}2.
\]

Therefore

\[
\operatorname{ord}_{h=0}\det J
=
\frac{m(m-1)}2
+
\frac{3m(m-1)}2
=
2m(m-1).
\]

This agrees with the exact Vandermonde determinant computation. \(\square\)

---

## 6. Pole order of the inverse

### Proposition 6.1

The meromorphic inverse \(J(h,p)^{-1}\) has pole order

\[
\boxed{
\operatorname{poleord}_{h=0}J^{-1}
=
2m-1.
}
\]

### Proof

For \(h\ne0\),

\[
J^{-1}
=
B^{-1}D_m^{-1}A^{-1}.
\]

The factors \(A^{-1}\) and \(B^{-1}\) are holomorphic at \(h=0\). The largest pole in \(D_m^{-1}\) is

\[
h^{-(2m-1)}.
\]

Hence the pole order is at most \(2m-1\).

Because \(2m-1\) is a local partial multiplicity, no holomorphic invertible left or right factor can remove that pole from the local analytic equivalence class. Therefore the pole order is exactly \(2m-1\). \(\square\)

### Corollary 6.2

The absolute local condition number obeys

\[
\|J(h,p)^{-1}\|
\asymp
|h|^{-(2m-1)}
\]

uniformly on compact shape subcharts.

This recovers the deepest singular exponent from the largest local partial multiplicity.

---

## 7. Determinantal ideals

For \(1\le k\le2N\), let \(I_k(J)\) be the ideal in \(\mathcal O_0\) generated by all \(k\times k\) minors of \(J\).

Because \(\mathcal O_0\) is a discrete valuation ring, each nonzero ideal has the form

\[
I_k(J)=(h^{\beta_k}).
\]

### Proposition 7.1

If

\[
0\le\alpha_1\le\cdots\le\alpha_{2N}
\]

are the packet partial multiplicities, then

\[
\boxed{
\beta_k
=
\alpha_1+\cdots+\alpha_k.
}
\]

### Proof

The determinantal ideals are invariant under multiplication by holomorphic invertible matrices. Thus

\[
I_k(J)=I_k(D_m).
\]

For a diagonal matrix with ordered powers \(h^{\alpha_i}\), the minimum valuation among its nonzero \(k\times k\) minors is obtained by selecting the first \(k\) diagonal entries. Therefore

\[
I_k(D_m)
=
\left(
 h^{\alpha_1+\cdots+\alpha_k}
\right).
\]

This proves the claim. \(\square\)

### Consequence 7.2

The complete exponent list can be recovered intrinsically from the valuations of determinantal ideals:

\[
\alpha_k
=
\beta_k-\beta_{k-1},
\qquad
\beta_0:=0.
\]

Thus the packet exponent hierarchy does not depend on the chosen Hermite or finite-difference construction used to reveal it.

---

## 8. Singular-value exponents

Local Smith theory classifies analytic equivalence. Singular values also depend on the chosen Hermitian structures. Nevertheless, bounded invertible analytic factors preserve their powers of \(h\).

### Theorem 8.1

Let

\[
0\le\alpha_1\le\cdots\le\alpha_{2N}
\]

be the local partial multiplicities in increasing order. Number the singular values in nonincreasing order:

\[
\sigma_1(J)\ge\cdots\ge\sigma_{2N}(J).
\]

Then, after reversing the exponent order,

\[
\boxed{
\sigma_{2N-k+1}(J(h,p))
\asymp
|h|^{\alpha_k},
\qquad
1\le k\le2N.
}
\]

The comparison is uniform on compact shape subcharts.

### Proof

Since \(A,B,A^{-1},B^{-1}\) are uniformly bounded on compact subcharts, there exist constants \(c,C>0\) such that

\[
c\,\sigma_j(D_m(h))
\le
\sigma_j(J(h,p))
\le
C\,\sigma_j(D_m(h))
\]

for all \(j\) and sufficiently small \(h\).

The singular values of \(D_m(h)\) are the absolute values of its diagonal entries, reordered nonincreasingly. Hence their powers are precisely the reversed partial multiplicities. \(\square\)

### Remark 8.2

The theorem determines only the exponent of each singular value. The exact leading constants require the finer exterior-power and projection analysis already developed in the repository.

That refinement is not supplied by Smith form alone.

---

## 9. Root functions and the packet filtration

A vector germ \(v(h)\in\mathcal O_0^{2N}\) is a root function of order at least \(q\) if

\[
J(h,p)v(h)
=
O(h^q).
\]

Define

\[
\mathscr F^q_p
=
\left\{
 v(0):
 v(h)\text{ is holomorphic and }
 J(h,p)v(h)=O(h^q)
\right\}.
\]

### Proposition 9.1

In the packet Smith frame,

\[
\boxed{
\mathscr F^q_p
=
B(0,p)^{-1}
\operatorname{span}
\{e_i:\alpha_i\ge q\}.
}
\]

In particular,

\[
\dim\mathscr F^q_p
=
\#\{i:\alpha_i\ge q\}.
\]

### Proof

Write

\[
v(h)=B(h,p)^{-1}w(h).
\]

Then

\[
J(h,p)v(h)
=
A(h,p)D_m(h)w(h).
\]

Since \(A\) is holomorphically invertible, the condition

\[
Jv=O(h^q)
\]

is equivalent to

\[
D_mw=O(h^q).
\]

At \(h=0\), a constant component \(w_i(0)\) may be nonzero only when

\[
\alpha_i\ge q.
\]

Applying \(B(0,p)^{-1}\) gives the stated formula. \(\square\)

### Corollary 9.2

The canonical exponent filtration constructed in the rescaled tangent bundle agrees with the root-function filtration of the local analytic matrix germ.

This identifies the packet filtration with a standard invariant from local analytic matrix theory.

---

## 10. Relative holomorphic variation in shape

Although the local Smith theorem is applied with \(p\) fixed, the repository proves more than a pointwise statement.

### Proposition 10.1

On every sufficiently small nondegenerate shape neighborhood, the same partial multiplicity list holds for every auxiliary parameter \(p\), and the Smith frames may be chosen jointly holomorphic in \((h,p)\).

### Proof

The varying-shape normal form supplies jointly holomorphic factors

\[
A(h,p),
\qquad
B(h,p),
\]

with a diagonal factor \(D_m(h)\) independent of \(p\). Their determinants remain nonzero throughout the neighborhood. Therefore each one-variable germ \(h\mapsto J(h,p)\) has the same local Smith diagonal, while the chosen left and right frames vary jointly holomorphically. \(\square\)

### Remark 10.2

This is a relative family of one-variable Smith forms. It should not be confused with a Smith normal form over the full multivariable local ring in \((h,p)\), which is not generally a principal ideal domain.

---

## 11. Invariance under collision-chart changes

Suppose two ordered collision charts use boundary variables \(h\) and \(\widehat h\) related on an overlap by

\[
\widehat h
=
\gamma(h,p)h,
\qquad
\gamma(0,p)\ne0.
\]

Assume the corresponding Jacobian matrices differ by holomorphic invertible source and target frame changes.

### Proposition 11.1

The local partial multiplicities are identical in the two charts.

### Proof

Because \(\gamma\) is a unit in the local ring,

\[
\widehat h^{\alpha_i}
=
\gamma(h,p)^{\alpha_i}h^{\alpha_i}.
\]

The diagonal unit factors

\[
\gamma^{\alpha_i}
\]

can be absorbed into a holomorphic invertible left or right factor. Holomorphic invertible changes of source and target frame also preserve local analytic equivalence. Therefore the Smith exponent list is unchanged. \(\square\)

### Corollary 11.2

The packet exponent multiset and the missing exponent \(m\) are intrinsic to the ordered collision face, not to the chosen reference pair used to normalize the shape.

---

## 12. Metric information beyond Smith form

The local Smith form determines:

- ranks at the boundary;
- determinant order;
- determinantal-ideal valuations;
- inverse pole order;
- singular-value exponents;
- root-function filtration dimensions.

It does not determine:

- exact singular-value constants;
- limiting left and right singular vectors in the fixed Euclidean metrics;
- the boundary matrix
  \[
  A_0^*A_0;
  \]
- the realization-volume normalization;
- metric transition matrices between collision charts.

Those depend on the chosen realization map and Hermitian structures, not only on the analytic equivalence class of \(J\).

Thus the repository's metric results are a refinement of the Smith classification rather than consequences of it.

---

## 13. Recommended terminology

Future papers should use the following distinctions.

### Analytic classification

\[
\text{local Smith partial multiplicities}
\]

for the exponent multiset.

### Conditioning classification

\[
\text{singular-value exponents and exact constants}
\]

for Euclidean asymptotics.

### Geometric resolution

\[
\text{packet-rescaled tangent bundle and extended realization metric}
\]

for the boundary geometry induced by the realization map.

A precise summary sentence is:

> The packet normal form computes the local Smith partial multiplicities of the Prony realization Jacobian; the exterior-power analysis refines those analytic invariants to exact singular constants, and the rescaled tangent construction converts the refinement into a nondegenerate boundary metric.

---

## 14. Main conclusion

The common-scale packet Jacobian has local Smith partial multiplicities

\[
\boxed{
0^{\times(2N-2m+2)},
1,2,\ldots,m-1,m+1,\ldots,2m-1.
}
\]

Therefore:

\[
\boxed{
\operatorname{ord}_{h=0}\det J
=
2m(m-1),
}
\]

\[
\boxed{
\operatorname{poleord}_{h=0}J^{-1}
=
2m-1,
}
\]

and the missing exponent \(m\) is an invariant of the local analytic equivalence class.

The abstract existence of a local Smith factorization is classical. The explicit packet partial multiplicities, exact singular constants, and realization-induced metric remain the substantive results of this program.
