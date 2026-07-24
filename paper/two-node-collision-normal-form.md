# Two-node collision normal form for finite exponential packet realizations

## Status

This note proves the first anisotropic boundary theorem for the finite exponential moment map

\[
\mathcal R_N(X,u)
=
(a_0,\ldots,a_{2N-1}),
\qquad
a_k=\sum_{j=1}^N u_jx_j^k.
\]

When two nodes collide while all remaining nodes stay separated and all coefficients remain nonzero, exactly two singular values of the Jacobian collapse. Their orders are

\[
|h|
\qquad\text{and}\qquad
|h|^3.
\]

Consequently, the absolute packet condition number diverges like

\[
|h|^{-3}.
\]

The proof uses a collision-adapted divided-difference basis and generalized Hermite interpolation. The underlying confluent Vandermonde facts are classical. The normal-form formulation is adapted to the packet-geometry program.

---

## 1. Setup

For

\[
m(z)
=
(1,z,z^2,\ldots,z^{2N-1})^{\mathsf T},
\]

write

\[
m^{(r)}(z)
=
\frac{d^r}{dz^r}m(z).
\]

Fix pairwise distinct complex numbers

\[
x,x_3,\ldots,x_N,
\]

and define a two-node collision by

\[
x_1=x,
\qquad
x_2=x+h,
\qquad
h\to0.
\]

The remaining nodes are fixed. Let

\[
u_j(h)\to u_j(0)\neq0
\]

for every \(j\). Constant coefficients are included as a special case.

Use interleaved parameter coordinates

\[
(u_1,x_1,u_2,x_2,\ldots,u_N,x_N).
\]

The Jacobian is

\[
J(h)
=
\bigl[
 m(x_1),u_1(h)m'(x_1),
 \ldots,
 m(x_N),u_N(h)m'(x_N)
\bigr].
\]

A simultaneous permutation of columns changes neither the singular values nor the condition number, so the same conclusions hold in grouped coordinates.

---

## 2. The unweighted confluent matrix

Separate the coefficient scaling by defining

\[
C(h)
=
\bigl[
 m(x),m'(x),m(x+h),m'(x+h),
 m(x_3),m'(x_3),\ldots,m(x_N),m'(x_N)
\bigr]
\]

and

\[
U(h)
=
\operatorname{diag}
\bigl(
1,u_1(h),1,u_2(h),\ldots,1,u_N(h)
\bigr).
\]

Then

\[
J(h)=C(h)U(h).
\]

Because every limiting coefficient is nonzero, both \(U(h)\) and \(U(h)^{-1}\) are uniformly bounded for sufficiently small \(h\).

---

## 3. Collision-adapted column operations

Focus first on the four columns belonging to the colliding nodes. Define

\[
r_2(h)
:=
m'(x+h)-m'(x)
\]

and

\[
r_3(h)
:=
m(x+h)-m(x)
-\frac h2\bigl(m'(x)+m'(x+h)\bigr).
\]

These are obtained from the original four columns by the right multiplication

\[
P_4(h)
=
\begin{pmatrix}
1&0&0&-1\\
0&1&-1&-h/2\\
0&0&0&1\\
0&0&1&-h/2
\end{pmatrix}.
\]

Indeed,

\[
[m(x),m'(x),m(x+h),m'(x+h)]P_4(h)
=
[m(x),m'(x),r_2(h),r_3(h)].
\]

The determinant is

\[
\det P_4(h)=-1,
\]

and

\[
P_4(h)^{-1}
=
\begin{pmatrix}
1&0&1&0\\
0&1&h&1\\
0&0&h/2&1\\
0&0&1&0
\end{pmatrix}.
\]

Therefore \(P_4(h)\) and \(P_4(h)^{-1}\) remain uniformly bounded as \(h\to0\).

Extend \(P_4(h)\) by the identity on all remaining columns and call the resulting \(2N\times2N\) matrix \(P(h)\).

---

## 4. Divided-difference limits

For \(h\neq0\), define

\[
q_2(h)
:=
\frac{m'(x+h)-m'(x)}{h}
\]

and

\[
q_3(h)
:=
\frac{
 m(x+h)-m(x)
 -\frac h2(m'(x)+m'(x+h))
}{h^3}.
\]

Taylor expansion at \(x\) gives

\[
q_2(h)
=
m''(x)+O(h)
\]

and

\[
q_3(h)
=
-\frac1{12}m'''(x)+O(h).
\]

Because \(m\) is polynomial, these divided differences extend holomorphically through \(h=0\). Set

\[
q_2(0)=m''(x),
\qquad
q_3(0)=-\frac1{12}m'''(x).
\]

Now define

\[
A(h)
=
\bigl[
 m(x),m'(x),q_2(h),q_3(h),
 m(x_3),m'(x_3),\ldots,m(x_N),m'(x_N)
\bigr]
\]

and

\[
D(h)
=
\operatorname{diag}
\bigl(
1,1,h,h^3,1,1,\ldots,1,1
\bigr).
\]

Then the exact factorization is

\[
\boxed{
C(h)P(h)=A(h)D(h).
}
\]

Equivalently,

\[
\boxed{
J(h)=A(h)D(h)B(h),
\qquad
B(h):=P(h)^{-1}U(h).
}
\]

The matrices \(B(h)\) and \(B(h)^{-1}\) are uniformly bounded near \(h=0\).

---

## 5. Invertibility of the limiting regular factor

### Lemma 5.1

The matrix

\[
A(0)
=
\bigl[
 m(x),m'(x),m''(x),-\tfrac1{12}m'''(x),
 m(x_3),m'(x_3),\ldots,m(x_N),m'(x_N)
\bigr]
\]

is invertible.

### Proof

The nonzero scalar \(-1/12\) does not affect invertibility, so it is enough to consider the matrix with first four columns

\[
m(x),m'(x),m''(x),m'''(x).
\]

Its transpose is the generalized Hermite data map on polynomials of degree at most \(2N-1\):

\[
p
\longmapsto
\bigl(
 p(x),p'(x),p''(x),p'''(x),
 p(x_3),p'(x_3),\ldots,p(x_N),p'(x_N)
\bigr).
\]

The total number of prescribed data is

\[
4+2(N-2)=2N.
\]

Generalized Hermite interpolation at the distinct nodes

\[
x,x_3,\ldots,x_N
\]

states that arbitrary such data are realized by a unique polynomial of degree at most \(2N-1\). Hence the data map, and therefore \(A(0)\), is invertible. \(\square\)

Since \(A(h)\to A(0)\), continuity of inversion gives constants \(M_A,m_A>0\) and \(\varepsilon>0\) such that

\[
\|A(h)\|\le M_A,
\qquad
\sigma_{\min}(A(h))\ge m_A
\]

whenever \(|h|<\varepsilon\).

The same is true for \(B(h)\): there are constants \(M_B,m_B>0\) such that

\[
\|B(h)\|\le M_B,
\qquad
\sigma_{\min}(B(h))\ge m_B.
\]

Thus the entire singular behavior has been isolated in the diagonal matrix \(D(h)\).

---

## 6. Singular-value comparison

We use the standard inequalities

\[
\sigma_k(LMR)
\le
\|L\|\,\|R\|\,\sigma_k(M)
\]

and, for invertible square \(L,R\),

\[
\sigma_k(LMR)
\ge
\sigma_{\min}(L)\,
\sigma_{\min}(R)\,
\sigma_k(M).
\]

Apply them to

\[
J(h)=A(h)D(h)B(h).
\]

For \(0<|h|<\min\{1,\varepsilon\}\), the singular values of \(D(h)\), in nonincreasing order, are

\[
\underbrace{1,\ldots,1}_{2N-2\text{ times}},
|h|,
|h|^3.
\]

Therefore every singular value of \(J(h)\) is comparable to the corresponding singular value of \(D(h)\), with constants independent of \(h\).

---

## 7. Main theorem

### Theorem 7.1 - two-node collision normal form

Under the setup above, there exist constants

\[
0<c<C<\infty
\]

and \(\varepsilon>0\) such that, for every \(0<|h|<\varepsilon\), the singular values

\[
\sigma_1(J(h))\ge\cdots\ge\sigma_{2N}(J(h))
\]

satisfy

\[
c
\le
\sigma_k(J(h))
\le
C,
\qquad
1\le k\le2N-2,
\]

\[
\boxed{
 c|h|
 \le
 \sigma_{2N-1}(J(h))
 \le
 C|h|
}
\]

and

\[
\boxed{
 c|h|^3
 \le
 \sigma_{2N}(J(h))
 \le
 C|h|^3.
}
\]

Equivalently,

\[
\sigma_{2N-1}(J(h))\asymp|h|,
\qquad
\sigma_{2N}(J(h))\asymp|h|^3.
\]

### Proof

The exact factorization

\[
J(h)=A(h)D(h)B(h)
\]

was proved above. Both regular factors and their inverses are uniformly bounded near \(h=0\), while the ordered singular values of \(D(h)\) are exactly

\[
1,\ldots,1,|h|,|h|^3.
\]

The two-sided singular-value inequalities give the stated estimates. \(\square\)

---

## 8. Condition-number blow-up

### Corollary 8.1

The absolute packet condition number satisfies

\[
\boxed{
\kappa_{\mathrm{abs}}(X(h),u(h))
=
\|J(h)^{-1}\|
\asymp
|h|^{-3}.
}
\]

### Proof

By definition,

\[
\|J(h)^{-1}\|
=
\frac1{\sigma_{2N}(J(h))}.
\]

Apply Theorem 7.1. \(\square\)

Because the largest singular value remains bounded above and below, the usual matrix condition number also obeys

\[
\operatorname{cond}J(h)\asymp|h|^{-3}.
\]

---

## 9. Pullback-metric degeneration

Let

\[
G(h)=J(h)^*J(h).
\]

Its eigenvalues are the squared singular values of \(J(h)\). Hence the two collapsing metric eigenvalues satisfy

\[
\boxed{
\lambda_{2N-1}(G(h))\asymp|h|^2,
\qquad
\lambda_{2N}(G(h))\asymp|h|^6,
}
\]

while the remaining \(2N-2\) eigenvalues stay bounded above and below.

Thus an ordinary two-node collision is anisotropic. One tangent scale collapses quadratically in the metric and the other collapses at sixth order.

---

## 10. Compatibility with the determinant theorem

The exact Jacobian determinant formula gives

\[
|\det J(h)|
=
\left(\prod_j|u_j(h)|\right)
\prod_{i<j}|x_j(h)-x_i(h)|^4.
\]

Only the factor associated with the colliding pair tends to zero, so

\[
|\det J(h)|\asymp|h|^4.
\]

The normal form resolves this total fourth-order volume collapse into the two directional scales

\[
|h|\cdot|h|^3=|h|^4.
\]

The determinant theorem determines the product. The collision normal form determines the individual orders.

---

## 11. Adapted weak directions

The column operations identify two natural nearly invisible parameter combinations.

After removing the fixed coefficient scalings, the first weak output direction is

\[
m'(x+h)-m'(x)
=
hm''(x)+O(h^2).
\]

In the original Jacobian coordinates, this is generated by the tangent combination

\[
\delta x_1=-\frac1{u_1},
\qquad
\delta x_2=\frac1{u_2},
\qquad
\delta u_1=\delta u_2=0.
\]

The second weak output direction is

\[
m(x+h)-m(x)
-\frac h2\bigl(m'(x)+m'(x+h)\bigr)
=
-\frac{h^3}{12}m'''(x)+O(h^4).
\]

It is generated by

\[
\delta u_1=-1,
\qquad
\delta u_2=1,
\qquad
\delta x_1=-\frac{h}{2u_1},
\qquad
\delta x_2=-\frac{h}{2u_2}.
\]

These adapted directions are not asserted to be exact singular vectors. They are uniformly well-conditioned coordinates that expose the two asymptotic scales.

---

## 12. What is proved and what remains open

### Proved here

- An exact factorization
  \[
  J(h)=A(h)D(h)B(h)
  \]
  with \(A(h)\), \(B(h)\), and their inverses uniformly bounded.
- The diagonal collision scales
  \[
  1,\ldots,1,h,h^3.
  \]
- The singular-value laws
  \[
  \sigma_{2N-1}\asymp|h|,
  \qquad
  \sigma_{2N}\asymp|h|^3.
  \]
- The condition-number law
  \[
  \kappa_{\mathrm{abs}}\asymp|h|^{-3}.
  \]
- The pullback-metric collapse orders
  \[
  |h|^2
  \quad\text{and}\quad
  |h|^6.
  \]

### Still open

- Exact leading constants for the two collapsing singular values.
- A canonical unitary normal form rather than a bounded-equivalence normal form.
- The corresponding hierarchy for clusters of three or more colliding nodes.
- Metric extension in confluent packet coordinates.
- Sharp global lower bounds in terms of minimum separation, coefficient size, and node radius.

The next theorem target is the exact leading coefficient of the cubic singular scale. A successful orthogonal reduction would identify the component of \(m'''(x)\) surviving after projection away from the limiting rank-\((2N-2)\) image and the first weak direction.