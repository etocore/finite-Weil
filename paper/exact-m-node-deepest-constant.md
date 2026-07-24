# Exact deepest singular-value constant for a common-scale packet cluster

## Status

This note sharpens the general common-scale cluster normal form for the finite exponential moment map

\[
\mathcal R_N(X,u)
=
(a_0,\ldots,a_{2N-1}),
\qquad
 a_k=\sum_{j=1}^N u_jx_j^k.
\]

For an \(m\)-node cluster

\[
x_j(h)=x+h\xi_j,
\qquad
1\le j\le m,
\]

with fixed pairwise distinct offsets \(\xi_j\), the preceding normal-form theorem proves

\[
\sigma_{2N}(J(h))\asymp h^{2m-1}
\]

for \(h\to0^+\). The purpose of this note is to compute the exact Euclidean leading constant.

The main result is

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_{2N}(J(h))}{h^{2m-1}}
=
\frac1{\Gamma(\xi)\,\|\operatorname{coeff}P\|_2},
}
\]

where

\[
P(z)
=
(z-x)^{2m-1}
\left(\frac{E(z)}{E(x)}\right)^2,
\qquad
E(z)=\prod_{\ell=m+1}^N(z-y_\ell),
\]

and the cluster-shape factor is

\[
\boxed{
\Gamma(\xi)
=
\left(
\sum_{j=1}^m
\left|
\frac{q_\xi''(\xi_j)}{q_\xi'(\xi_j)^3}
\right|^2
\right)^{1/2},
\qquad
q_\xi(t)=\prod_{j=1}^m(t-\xi_j).
}
\]

The proof comes from a rank-one leading term of the inverse Jacobian. It also shows that the deepest cluster constant is independent of all nonzero packet coefficients.

The Hermite interpolation formulas used below are classical. The rank-one inverse formulation is adapted to the packet Jacobian.

---

## 1. Setup

Let

\[
M(z)
=
(1,z,z^2,\ldots,z^{2N-1})^{\mathsf T}.
\]

Fix

\[
2\le m\le N.
\]

Let the cluster nodes be

\[
x_j(h)=x+h\xi_j,
\qquad
1\le j\le m,
\]

where

\[
\xi_i\ne\xi_j
\qquad(i\ne j).
\]

Let the remaining nodes be fixed:

\[
x_\ell(h)=y_\ell,
\qquad
m+1\le\ell\le N,
\]

with

\[
y_\ell\ne x
\]

and all nodes \(y_\ell\) pairwise distinct.

Assume

\[
u_j(h)\to u_j(0)\ne0.
\]

Use interleaved parameter coordinates

\[
(u_1,x_1,u_2,x_2,\ldots,u_N,x_N).
\]

Then

\[
J(h)
=
\bigl[
M(x_1(h)),u_1(h)M'(x_1(h)),\ldots,
M(x_N(h)),u_N(h)M'(x_N(h))
\bigr].
\]

All norms are the standard Euclidean norms on parameter space and moment space.

Define the exterior node polynomial

\[
E(z)
:=
\prod_{\ell=m+1}^N(z-y_\ell).
\]

When \(m=N\), interpret \(E\equiv1\).

Because no exterior node equals \(x\),

\[
E(x)\ne0.
\]

---

## 2. The inverse Jacobian and fundamental Hermite polynomials

For each node, define the Lagrange polynomial

\[
\ell_j^{(h)}(z)
:=
\prod_{i\ne j}
\frac{z-x_i(h)}{x_j(h)-x_i(h)}.
\]

The standard fundamental Hermite polynomials are

\[
H_j^{(h)}(z)
:=
\left[
1-2\bigl(\ell_j^{(h)}\bigr)'(x_j(h))
(z-x_j(h))
\right]
\bigl(\ell_j^{(h)}(z)\bigr)^2
\]

and

\[
K_j^{(h)}(z)
:=
(z-x_j(h))
\bigl(\ell_j^{(h)}(z)\bigr)^2.
\]

They satisfy

\[
H_j^{(h)}(x_i(h))=\delta_{ij},
\qquad
\bigl(H_j^{(h)}\bigr)'(x_i(h))=0,
\]

and

\[
K_j^{(h)}(x_i(h))=0,
\qquad
\bigl(K_j^{(h)}\bigr)'(x_i(h))=\delta_{ij}.
\]

For a polynomial

\[
p(z)=\sum_{k=0}^{2N-1}c_kz^k,
\]

write

\[
\operatorname{coeff}p
:=(c_0,\ldots,c_{2N-1})^{\mathsf T}.
\]

Then

\[
(\operatorname{coeff}p)^{\mathsf T}M(t)=p(t)
\]

and

\[
(\operatorname{coeff}p)^{\mathsf T}M'(t)=p'(t).
\]

It follows directly from the interpolation identities that the rows of \(J(h)^{-1}\) are:

- in the row corresponding to \(u_j\),
  \[
  (\operatorname{coeff}H_j^{(h)})^{\mathsf T};
  \]
- in the row corresponding to \(x_j\),
  \[
  \frac1{u_j(h)}
  (\operatorname{coeff}K_j^{(h)})^{\mathsf T}.
  \]

Thus the leading singular behavior of \(J(h)^{-1}\) can be read from the asymptotics of the fundamental Hermite polynomials.

---

## 3. Cluster Lagrange asymptotics

Define the cluster polynomial

\[
q_\xi(t)
:=
\prod_{j=1}^m(t-\xi_j).
\]

For each cluster index, set

\[
d_j
:=
q_\xi'(\xi_j)
=
\prod_{\substack{1\le i\le m\\i\ne j}}
(\xi_j-\xi_i)
\]

and

\[
s_j
:=
\sum_{\substack{1\le i\le m\\i\ne j}}
\frac1{\xi_j-\xi_i}.
\]

The elementary identity

\[
q_\xi''(\xi_j)=2q_\xi'(\xi_j)s_j
\]

gives

\[
s_j
=
\frac{q_\xi''(\xi_j)}{2q_\xi'(\xi_j)}.
\]

Define

\[
L(z)
:=
\frac{(z-x)^{m-1}E(z)}{E(x)}.
\]

### Lemma 3.1

For every cluster index \(1\le j\le m\), coefficient-wise in the polynomial space,

\[
\boxed{
h^{m-1}\ell_j^{(h)}(z)
\longrightarrow
\frac1{d_j}L(z)
}
\]

and

\[
\boxed{
h\bigl(\ell_j^{(h)}\bigr)'(x_j(h))
\longrightarrow
s_j.
}
\]

### Proof

The cluster part of the denominator of \(\ell_j^{(h)}\) is

\[
\prod_{\substack{1\le i\le m\\i\ne j}}
\bigl(x+h\xi_j-(x+h\xi_i)\bigr)
=
h^{m-1}d_j.
\]

The exterior part tends to

\[
E(x).
\]

The numerator tends coefficient-wise to

\[
(z-x)^{m-1}E(z).
\]

This proves the first limit.

For the derivative at its own node,

\[
\bigl(\ell_j^{(h)}\bigr)'(x_j(h))
=
\sum_{i\ne j}
\frac1{x_j(h)-x_i(h)}.
\]

Multiplying by \(h\), the cluster terms converge to \(s_j\), while every exterior term tends to zero. \(\square\)

---

## 4. The dominant inverse mode

Define the geometric polynomial

\[
\boxed{
P(z)
:=
(z-x)L(z)^2
=
(z-x)^{2m-1}
\left(\frac{E(z)}{E(x)}\right)^2.
}
\]

For each cluster index define

\[
\gamma_j
:=
-\frac{q_\xi''(\xi_j)}{q_\xi'(\xi_j)^3}.
\]

Equivalently,

\[
\gamma_j
=
-\frac{2s_j}{d_j^2}.
\]

### Lemma 4.1

For \(1\le j\le m\),

\[
\boxed{
h^{2m-1}H_j^{(h)}(z)
\longrightarrow
\gamma_jP(z)
}
\]

coefficient-wise, while

\[
\boxed{
h^{2m-1}K_j^{(h)}(z)
\longrightarrow0.
}
\]

For every exterior index \(j>m\), both

\[
h^{2m-1}H_j^{(h)}
\quad\text{and}\quad
h^{2m-1}K_j^{(h)}
\]

converge to zero.

### Proof

For a cluster index,

\[
H_j^{(h)}
=
\bigl(\ell_j^{(h)}\bigr)^2
-
2\bigl(\ell_j^{(h)}\bigr)'(x_j(h))
(z-x_j(h))
\bigl(\ell_j^{(h)}\bigr)^2.
\]

The first term satisfies

\[
h^{2m-1}
\bigl(\ell_j^{(h)}\bigr)^2
=
h
\left(h^{m-1}\ell_j^{(h)}\right)^2
\longrightarrow0.
\]

For the second term, Lemma 3.1 gives

\[
-2
\left[h\bigl(\ell_j^{(h)}\bigr)'(x_j(h))\right]
(z-x_j(h))
\left[h^{m-1}\ell_j^{(h)}(z)\right]^2
\longrightarrow
-
\frac{2s_j}{d_j^2}
(z-x)L(z)^2.
\]

This is exactly

\[
\gamma_jP(z).
\]

Similarly,

\[
h^{2m-1}K_j^{(h)}
=
h
(z-x_j(h))
\left[h^{m-1}\ell_j^{(h)}\right]^2
\longrightarrow0.
\]

For an exterior index, every node separation in the denominator remains bounded away from zero. Hence the corresponding Lagrange and Hermite polynomials remain coefficient-wise bounded, so multiplication by \(h^{2m-1}\) forces convergence to zero. \(\square\)

---

## 5. Rank-one inverse limit

Let

\[
p:=\operatorname{coeff}P\in\mathbb C^{2N}.
\]

Let

\[
r_\xi\in\mathbb C^{2N}
\]

be the parameter-space vector whose entry in the \(u_j\) coordinate is \(\gamma_j\) for \(1\le j\le m\), and whose remaining entries are zero.

Define

\[
\Gamma(\xi)
:=
\|r_\xi\|_2
=
\left(
\sum_{j=1}^m
\left|
\frac{q_\xi''(\xi_j)}{q_\xi'(\xi_j)^3}
\right|^2
\right)^{1/2}.
\]

### Lemma 5.1

\[
\Gamma(\xi)>0.
\]

### Proof

If \(q_\xi''(\xi_j)=0\) for every \(j\), then the polynomial \(q_\xi''\), of degree \(m-2\), would vanish at the \(m\) distinct points \(\xi_1,\ldots,\xi_m\). Hence \(q_\xi''\equiv0\), which is impossible for a monic polynomial of degree \(m\ge2\). \(\square\)

### Theorem 5.2 - rank-one leading inverse

In operator norm,

\[
\boxed{
h^{2m-1}J(h)^{-1}
\longrightarrow
r_\xi p^{\mathsf T}.
}
\]

The limiting matrix has rank one and

\[
\boxed{
\|r_\xi p^{\mathsf T}\|
=
\Gamma(\xi)\,\|p\|_2.
}
\]

### Proof

The row description of \(J(h)^{-1}\) from Section 2 and the polynomial limits from Lemma 4.1 show coefficient-wise convergence of every row.

The cluster value rows converge to

\[
\gamma_jp^{\mathsf T},
\]

and every cluster motion row and every exterior row converges to zero after multiplication by \(h^{2m-1}\). This is precisely the matrix limit

\[
r_\xi p^{\mathsf T}.
\]

Finite-dimensional coefficient-wise convergence is equivalent to convergence in every matrix norm.

A rank-one matrix \(ab^{\mathsf T}\) has operator norm \(\|a\|_2\|b\|_2\). Therefore

\[
\|r_\xi p^{\mathsf T}\|
=
\Gamma(\xi)\|p\|_2.
\]

\(\square\)

---

## 6. Exact deepest singular-value constant

### Theorem 6.1

Under the common-scale cluster assumptions,

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_{2N}(J(h))}{h^{2m-1}}
=
\frac1{\Gamma(\xi)\,\|\operatorname{coeff}P\|_2}.
}
\]

Equivalently,

\[
\boxed{
\lim_{h\to0^+}
h^{2m-1}\kappa_{\mathrm{abs}}(J(h))
=
\Gamma(\xi)\,\|\operatorname{coeff}P\|_2.
}
\]

### Proof

For \(h>0\),

\[
\sigma_{2N}(J(h))
=
\frac1{\|J(h)^{-1}\|}.
\]

Theorem 5.2 gives

\[
h^{2m-1}\|J(h)^{-1}\|
\longrightarrow
\Gamma(\xi)\|p\|_2.
\]

Taking reciprocals proves the singular-value limit. The condition-number formula is the same identity written for \(\kappa_{\mathrm{abs}}=\|J^{-1}\|\). \(\square\)

### Consequence 6.2 - coefficient independence

The deepest constant is independent of

\[
u_1,\ldots,u_N,
\]

provided their limits are nonzero.

This happens because the dominant inverse rows are the value-recovery Hermite rows \(H_j^{(h)}\), which do not contain coefficient scalings. The node-motion rows contain \(1/u_j\), but they grow only through order \(h^{-(2m-2)}\) and therefore disappear from the leading rank-one limit.

---

## 7. Orthogonal jet-projection form

Define the codimension-one regular subspace

\[
\mathcal W_{m-1}
:=
\operatorname{span}
\Bigl(
M(x),M'(x),\ldots,M^{(2m-2)}(x),
M(y_{m+1}),M'(y_{m+1}),\ldots,
M(y_N),M'(y_N)
\Bigr).
\]

The number of displayed vectors is

\[
2m-1+2(N-m)=2N-1.
\]

Generalized Hermite interpolation shows that they are linearly independent.

Let

\[
Q_{m-1}
\]

be orthogonal projection onto

\[
\mathcal W_{m-1}^{\perp}.
\]

The polynomial \(P\) has

- a zero of order \(2m-1\) at \(x\);
- a double zero at each exterior node \(y_\ell\).

Therefore \(\overline p\) spans \(\mathcal W_{m-1}^{\perp}\). Moreover,

\[
P^{(2m-1)}(x)=(2m-1)!.
\]

It follows that

\[
\boxed{
\left\|Q_{m-1}M^{(2m-1)}(x)\right\|_2
=
\frac{(2m-1)!}{\|p\|_2}.
}
\]

Substituting into Theorem 6.1 gives the geometric form.

### Corollary 7.1 - deepest constant as a projected jet

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_{2N}(J(h))}{h^{2m-1}}
=
\frac{
\left\|Q_{m-1}M^{(2m-1)}(x)\right\|_2
}
{(2m-1)!\,\Gamma(\xi)}.
}
\]

Thus the exact deepest scale separates into two factors:

1. a cluster-shape factor \(\Gamma(\xi)^{-1}\);
2. a geometric jet-survival factor measuring how much of \(M^{(2m-1)}(x)\) remains after removing all lower confluent jets and all exterior packet directions.

---

## 8. Recovery of the two-node formula

Take

\[
m=2,
\qquad
\xi_1=0,
\qquad
\xi_2=1.
\]

Then

\[
q_\xi(t)=t(t-1),
\qquad
q_\xi''(t)=2,
\]

and

\[
\gamma_1=2,
\qquad
\gamma_2=-2.
\]

Hence

\[
\Gamma(\xi)=2\sqrt2.
\]

The projection formula becomes

\[
\lim_{h\to0^+}
\frac{\sigma_{2N}(J(h))}{h^3}
=
\frac{
\left\|Q_1M'''(x)\right\|_2
}
{3!\,2\sqrt2}
=
\frac{
\left\|Q_1M'''(x)\right\|_2
}
{12\sqrt2}.
\]

This is exactly the previously proved two-node cubic constant.

---

## 9. Symmetric three-node example

Take

\[
m=N=3,
\qquad
x=0,
\qquad
(\xi_1,\xi_2,\xi_3)=(-1,0,1).
\]

Then

\[
q_\xi(t)=t^3-t,
\qquad
q_\xi'(t)=3t^2-1,
\qquad
q_\xi''(t)=6t.
\]

The shape coefficients are

\[
\gamma_1=\frac34,
\qquad
\gamma_2=0,
\qquad
\gamma_3=-\frac34,
\]

so

\[
\Gamma(\xi)
=
\frac3{2\sqrt2}.
\]

Because \(E\equiv1\) and \(x=0\),

\[
P(z)=z^5
\]

and

\[
\|\operatorname{coeff}P\|_2=1.
\]

Therefore

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_6(J(h))}{h^5}
=
\frac{2\sqrt2}{3}.
}
\]

This gives an exact constant for the deepest member of the three-node hierarchy

\[
1,2,4,5.
\]

---

## 10. What is proved and what remains open

### Proved here

- The inverse Jacobian has a rank-one leading term at order \(h^{-(2m-1)}\).
- The exact deepest singular-value constant is
  \[
  \frac1{\Gamma(\xi)\|\operatorname{coeff}P\|_2}.
  \]
- The exact inverse-condition constant is
  \[
  \Gamma(\xi)\|\operatorname{coeff}P\|_2.
  \]
- The deepest constant is independent of all nonzero packet coefficients.
- The constant separates into a cluster-shape factor and a projected highest-jet factor.
- The two-node constant is recovered exactly.
- For the symmetric three-node cluster at the origin, the constant is \(2\sqrt2/3\).

### Still open

- Exact constants for every intermediate collapsing singular value.
- A canonical unitary cluster normal form producing all constants simultaneously.
- Several clusters collapsing at the same scale.
- Nonuniform collision paths with different powers of \(h\).
- Sharp global lower bounds that combine separation, cluster shape, coefficient size, and node radius.
- Metric completion and curvature near higher confluent strata.

The next structural target is a successive effective-map or inverse-filtration theorem that produces the complete list of cluster constants, not only the deepest one.
