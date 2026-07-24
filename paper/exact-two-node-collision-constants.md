# Exact singular-value constants for a two-node packet collision

## Status

This note sharpens the two-node collision normal form for the finite exponential moment map

\[
\mathcal R_N(X,u)
=
(a_0,\ldots,a_{2N-1}),
\qquad
 a_k=\sum_{j=1}^N u_jx_j^k.
\]

The preceding normal-form theorem proves only

\[
\sigma_{2N-1}(J(h))\asymp |h|,
\qquad
\sigma_{2N}(J(h))\asymp |h|^3.
\]

Here the asymptotic constants are identified exactly in the standard Euclidean parameter and moment metrics.

The result has two parts:

1. the linear constant is the norm of a first-order effective map from the right kernel of the collision Jacobian to its left cokernel;
2. the cubic constant follows from the exact determinant formula and can be rewritten as an orthogonal projection of the third jet.

The perturbation argument is classical. The projection formulas are specialized to the packet Jacobian.

---

## 1. Collision setup

Let

\[
m(z)=(1,z,z^2,\ldots,z^{2N-1})^{\mathsf T}\in\mathbb C^{2N}.
\]

Fix pairwise distinct nodes

\[
x,x_3,\ldots,x_N
\]

and nonzero coefficients

\[
\alpha,\beta,u_3,\ldots,u_N\in\mathbb C.
\]

Set

\[
x_1=x,
\qquad
x_2=x+h,
\]

and keep the coefficients fixed as \(h\to0\). In interleaved coordinates

\[
(u_1,x_1,u_2,x_2,\ldots,u_N,x_N),
\]

the Jacobian is

\[
J(h)
=
\bigl[
 m(x),\alpha m'(x),m(x+h),\beta m'(x+h),
 m(x_3),u_3m'(x_3),\ldots,m(x_N),u_Nm'(x_N)
\bigr].
\]

Write

\[
n:=2N.
\]

At \(h=0\), the rank is \(n-2\).

Define the unweighted limiting range matrix

\[
M_0
=
\bigl[
 m(x),m'(x),m(x_3),m'(x_3),\ldots,m(x_N),m'(x_N)
\bigr],
\]

whose \(n-2\) columns are linearly independent by generalized Hermite interpolation.

Let

\[
\mathcal R_0:=\operatorname{ran}M_0,
\qquad
\mathcal L_0:=\mathcal R_0^\perp,
\]

and let

\[
P_0:\mathbb C^n\to\mathcal L_0
\]

be the orthogonal projection.

Set

\[
a:=P_0m''(x),
\qquad
b:=P_0m'''(x).
\]

Generalized Hermite interpolation with multiplicity four at \(x\) and multiplicity two at the remaining nodes implies

\[
a\neq0
\]

and

\[
b\notin\operatorname{span}\{a\}.
\]

Define

\[
b_\perp
:=
P_{\mathcal L_0\cap a^\perp}m'''(x)
=
P_{a^\perp}b.
\]

Thus

\[
b_\perp\neq0.
\]

---

## 2. A first-order singular-value reduction lemma

### Lemma 2.1

Let \(A(h)\) be a differentiable family of square matrices such that

\[
\operatorname{rank}A(0)=n-r.
\]

Let

\[
K=\ker A(0),
\qquad
L=\ker A(0)^*.
\]

Let \(P_L\) denote orthogonal projection onto \(L\). Then the nonzero singular values of

\[
T:=P_LA'(0)|_K:K\to L
\]

are exactly the nonzero limits of singular values of \(A(h)\) divided by \(|h|\).

More precisely, if \(T\) has rank \(q\), then \(q\) singular values satisfy

\[
\frac{\sigma_{n-r+1}(A(h))}{|h|},\ldots,
\frac{\sigma_{n-r+q}(A(h))}{|h|}
\longrightarrow
\sigma_1(T),\ldots,\sigma_q(T),
\]

while the remaining \(r-q\) vanishing singular values are \(o(|h|)\).

### Proof

Choose unitary changes of domain and codomain so that

\[
A(0)
=
\begin{pmatrix}
\Sigma&0\\
0&0
\end{pmatrix},
\]

where \(\Sigma\in\mathbb C^{(n-r)\times(n-r)}\) is invertible and the lower-right block acts from \(K\) to \(L\).

Then

\[
A(h)
=
\begin{pmatrix}
\Sigma+O(h)&O(h)\\
O(h)&hT+o(h)
\end{pmatrix}.
\]

Block Gaussian elimination by left and right factors of the form \(I+O(h)\) removes the off-diagonal blocks and gives

\[
(I+O(h))A(h)(I+O(h))
=
\begin{pmatrix}
\Sigma+O(h)&0\\
0&hT+o(h)
\end{pmatrix}.
\]

The eliminating factors and their inverses converge to the identity, so they do not alter first-order singular-value constants. The large singular values converge to those of \(\Sigma\), while the \(r\) small singular values are those of \(hT+o(h)\) to first order. This proves the claim. \(\square\)

---

## 3. The right kernel and the linear constant

At the collision,

\[
J(0)
=
\bigl[
 m,\alpha m',m,\beta m',\ldots
\bigr].
\]

Two orthonormal vectors spanning \(\ker J(0)\) are

\[
k_0
=
\frac1{\sqrt2}(1,0,-1,0,0,\ldots,0)^{\mathsf T}
\]

and

\[
k_1
=
\frac1{s}
(0,\alpha^{-1},0,-\beta^{-1},0,\ldots,0)^{\mathsf T},
\]

where

\[
s
:=
\sqrt{|\alpha|^{-2}+|\beta|^{-2}}.
\]

Differentiate \(J(h)\) at zero. Since only the second node moves,

\[
P_0J'(0)k_0=0,
\]

because \(J'(0)k_0\) is a scalar multiple of \(m'(x)\in\mathcal R_0\).

On the second kernel vector,

\[
J(h)k_1
=
\frac{m'(x)-m'(x+h)}{s},
\]

so

\[
P_0J'(0)k_1
=
-\frac{a}{s}.
\]

Therefore the first effective map

\[
T=P_0J'(0)|_{\ker J(0)}
\]

has rank one and its unique nonzero singular value is

\[
\frac{\|a\|}{s}.
\]

### Theorem 3.1 - exact linear collision constant

The next-to-smallest singular value satisfies

\[
\boxed{
\lim_{h\to0}
\frac{\sigma_{n-1}(J(h))}{|h|}
=
\frac{\|P_0m''(x)\|}
{\sqrt{|\alpha|^{-2}+|\beta|^{-2}}}
}
\]

or equivalently

\[
\boxed{
\lim_{h\to0}
\frac{\sigma_{n-1}(J(h))}{|h|}
=
\frac{|\alpha\beta|}{\sqrt{|\alpha|^2+|\beta|^2}}
\|P_0m''(x)\|.
}
\]

### Proof

Apply Lemma 2.1 to \(J(h)\). The first effective map has rank one and the nonzero singular value computed above. \(\square\)

---

## 4. Product of the nonzero limiting singular values

Let

\[
\Pi_0
:=
\prod_{k=1}^{n-2}\sigma_k(J(0)).
\]

Factor

\[
J(0)=M_0S_0,
\]

where \(S_0\) records the duplicated collision columns and the coefficient scalings.

Because the rows of \(S_0\) have disjoint supports,

\[
S_0S_0^*
=
\operatorname{diag}
\bigl(
2,
|\alpha|^2+|\beta|^2,
1,|u_3|^2,
\ldots,
1,|u_N|^2
\bigr).
\]

For a full-column-rank matrix \(M\) and a full-row-rank matrix \(S\), the product of the nonzero singular values of \(MS\) is

\[
\sqrt{\det(M^*M)\det(SS^*)}.
\]

Hence

\[
\boxed{
\Pi_0
=
\sqrt{\det(M_0^*M_0)}
\sqrt{2(|\alpha|^2+|\beta|^2)}
\prod_{j=3}^N|u_j|.
}
\]

---

## 5. Determinant coefficient at the collision

The exact interleaved-coordinate determinant formula gives

\[
|\det J(h)|
=
\left(\prod_{j=1}^N|u_j|\right)
\prod_{1\le i<j\le N}|x_j-x_i|^4.
\]

Therefore

\[
|\det J(h)|
=
\Gamma |h|^4(1+o(1)),
\]

where

\[
\Gamma
=
|\alpha\beta|
\left(\prod_{j=3}^N|u_j|\right)
\left(\prod_{j=3}^N|x_j-x|^8\right)
\left(\prod_{3\le i<j\le N}|x_j-x_i|^4\right).
\]

Write

\[
V_*
:=
\left(\prod_{j=3}^N|x_j-x|^8\right)
\left(\prod_{3\le i<j\le N}|x_j-x_i|^4\right).
\]

Thus

\[
\Gamma
=
|\alpha\beta|
\left(\prod_{j=3}^N|u_j|\right)V_*.
\]

---

## 6. Exact cubic constant from the determinant product

Since

\[
|\det J(h)|
=
\prod_{k=1}^n\sigma_k(J(h)),
\]

and the first \(n-2\) singular values converge to the nonzero singular values of \(J(0)\),

\[
\lim_{h\to0}
\frac{\sigma_n(J(h))}{|h|^3}
=
\frac{\Gamma}{\Pi_0c_1},
\]

where

\[
c_1
=
\frac{|\alpha\beta|}{\sqrt{|\alpha|^2+|\beta|^2}}
\|a\|.
\]

Substituting the formulas for \(\Gamma\), \(\Pi_0\), and \(c_1\) yields

\[
\boxed{
\lim_{h\to0}
\frac{\sigma_n(J(h))}{|h|^3}
=
\frac{V_*}
{\sqrt2\,\sqrt{\det(M_0^*M_0)}\,\|a\|}.
}
\]

All coefficient factors cancel.

This formula is already exact, but it has a cleaner geometric form.

---

## 7. Projection form of the cubic constant

Consider the square generalized confluent matrix

\[
H_0
=
\bigl[
M_0,m''(x),m'''(x)
\bigr].
\]

The multiplicity pattern is four at \(x\) and two at every other node. The unnormalized confluent Vandermonde formula gives

\[
|\det H_0|
=
(0!1!2!3!)V_*
=
12V_*.
\]

On the other hand, orthogonal volume decomposition gives

\[
|\det H_0|
=
\sqrt{\det(M_0^*M_0)}
\|a\|
\|b_\perp\|.
\]

Therefore

\[
12V_*
=
\sqrt{\det(M_0^*M_0)}
\|a\|
\|b_\perp\|.
\]

Substituting into the previous formula proves the main result.

### Theorem 7.1 - exact cubic collision constant

The smallest singular value satisfies

\[
\boxed{
\lim_{h\to0}
\frac{\sigma_n(J(h))}{|h|^3}
=
\frac1{12\sqrt2}
\left\|
P_{\mathcal L_0\cap(P_0m''(x))^\perp}
m'''(x)
\right\|.
}
\]

Equivalently, with

\[
a=P_0m''(x),
\qquad
b=P_0m'''(x),
\]

\[
\boxed{
\lim_{h\to0}
\frac{\sigma_n(J(h))}{|h|^3}
=
\frac1{12\sqrt2}
\left\|
b-\operatorname{proj}_{\operatorname{span}\{a\}}b
\right\|.
}
\]

### Proof

The determinant-product calculation gives

\[
\lim_{h\to0}
\frac{\sigma_n(J(h))}{|h|^3}
=
\frac{V_*}
{\sqrt2\sqrt{\det(M_0^*M_0)}\|a\|}.
\]

The generalized confluent determinant and orthogonal volume decomposition give

\[
V_*
=
\frac1{12}
\sqrt{\det(M_0^*M_0)}\|a\|\|b_\perp\|.
\]

Combining the two identities proves the formula. \(\square\)

---

## 8. Exact condition-number constant

Because

\[
\kappa_{\mathrm{abs}}(J(h))
=
\frac1{\sigma_n(J(h))},
\]

Theorem 7.1 gives

\[
\boxed{
\lim_{h\to0}
|h|^3\kappa_{\mathrm{abs}}(J(h))
=
\frac{12\sqrt2}{\|b_\perp\|}.
}
\]

Thus the leading divergence of the inverse problem is determined by the component of the third jet that remains after removing

1. the limiting regular image, and
2. the first weak collision direction represented by \(P_0m''(x)\).

---

## 9. Pullback-metric constants

For

\[
G(h)=J(h)^*J(h),
\]

the eigenvalues are the squared singular values. Hence

\[
\boxed{
\lim_{h\to0}
\frac{\lambda_{n-1}(G(h))}{|h|^2}
=
\frac{\|a\|^2}
{|\alpha|^{-2}+|\beta|^{-2}}
}
\]

and

\[
\boxed{
\lim_{h\to0}
\frac{\lambda_n(G(h))}{|h|^6}
=
\frac{\|b_\perp\|^2}{288}.
}
\]

The metric collapse is therefore not only anisotropic in order; its leading coefficients are explicit projection invariants.

---

## 10. Minimal example

For \(N=2\), \(x=0\), and \(\alpha=\beta=1\),

\[
m(0)=e_1,
\qquad
m'(0)=e_2,
\qquad
m''(0)=2e_3,
\qquad
m'''(0)=6e_4.
\]

Thus

\[
a=2e_3,
\qquad
b_\perp=6e_4.
\]

The exact constants are

\[
\lim_{h\to0}
\frac{\sigma_3(J(h))}{|h|}
=
\frac{2}{\sqrt2}
=
\sqrt2,
\]

and

\[
\lim_{h\to0}
\frac{\sigma_4(J(h))}{|h|^3}
=
\frac6{12\sqrt2}
=
\frac1{2\sqrt2}.
\]

Their product is

\[
\frac12,
\]

which is consistent with the determinant coefficient after division by the two nonzero limiting singular values.

---

## 11. Interpretation

The linear scale depends on the colliding coefficients through

\[
\frac{|\alpha\beta|}{\sqrt{|\alpha|^2+|\beta|^2}}.
\]

The cubic scale does not. In the Euclidean parameter metric, coefficient dependence is transferred entirely into the first weak direction and the nonzero limiting singular values; it cancels from the deepest collision direction.

Geometrically:

- \(P_0m''(x)\) is the first new quotient direction beyond the limiting packet range;
- the orthogonal remainder of \(P_0m'''(x)\) is the second new quotient direction;
- the factors \(1\) and \(1/12\) arise from the first and third divided-difference normalizations;
- the factor \(1/\sqrt2\) comes from normalization of the two-node difference coordinate.

---

## 12. Scope and next questions

### Proved here

- The exact limit of the linear singular scale.
- The exact limit of the cubic singular scale.
- The exact leading constant for \(\kappa_{\mathrm{abs}}\sim |h|^{-3}\).
- Exact leading constants for the two collapsing pullback-metric eigenvalues.
- A projection interpretation of both constants.

### Still open

- A direct unitary block-diagonalization producing both constants without the determinant-product step.
- Extension to moving coefficient paths with the weakest possible regularity assumptions.
- The hierarchy and exact constants for clusters of three or more nodes.
- A coordinate-free formulation on the confluent compactification.
- Global estimates comparing the projection constants with minimum node separation and node radius.

The next structural target is the general \(m\)-node cluster exponent hierarchy.