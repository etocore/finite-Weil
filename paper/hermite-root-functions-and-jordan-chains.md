# Hermite root functions, Jordan chains, and canonical graded packet modes

## Status

This note identifies the explicit Hermite-dual source modes in the packet collision normal form with the root functions and Jordan chains of the classical local theory of regular analytic matrix functions.

The main conclusion requires a distinction that is important for publication:

- the individual Hermite-dual root functions depend on the chosen Smith frame and interpolation normalization;
- their orders, filtration, and associated-graded lines are intrinsic;
- because every positive packet partial multiplicity is simple, each nonzero associated-graded root space is one-dimensional;
- the Hermite construction therefore gives a distinguished representative of every canonical graded line.

The note also explains the missing exponent \(m\) directly from the target jet basis and identifies the exterior-power singular constants with Euclidean norms of wedges of right and left root modes.

No claim is made that root functions, Jordan chains, or their relation to local Smith forms are new. The packet-specific result is the explicit realization of those objects by Vandermonde-dual and Hermite coefficient-extraction modes, with the computed order list

\[
0^{\times(2N-2m+2)},
1,2,\ldots,m-1,m+1,\ldots,2m-1.
\]

---

## 1. Analytic packet Smith form

Fix all non-scale parameters \(p\) in a nondegenerate ordered common-scale collision chart. The established analytic normal form is

\[
J(h)=A(h)D(h)B(h),
\]

where \(A,B,A^{-1},B^{-1}\) are holomorphic near \(h=0\), and

\[
D(h)=\operatorname{diag}
\bigl(h^{\alpha_1},\ldots,h^{\alpha_{2N}}\bigr),
\qquad
0\le \alpha_1\le\cdots\le\alpha_{2N}.
\]

For an \(m\)-node packet cluster,

\[
(\alpha_i)_{i=1}^{2N}
=
\left(
\underbrace{0,\ldots,0}_{2N-2m+2},
1,2,\ldots,m-1,
m+1,\ldots,2m-1
\right).
\]

Write

\[
r_i(h):=B(h)^{-1}e_i
\]

for the right Smith-frame germs and

\[
\lambda_i(h)^{\mathsf T}
:=
e_i^{\mathsf T}A(h)^{-1}
\]

for the algebraic left Smith-frame row germs.

These satisfy the exact diagonal pairing

\[
\boxed{
\lambda_i(h)^{\mathsf T}J(h)r_j(h)
=
\delta_{ij}h^{\alpha_j}.
}
\]

Indeed,

\[
\lambda_i^{\mathsf T}Jr_j
=
e_i^{\mathsf T}A^{-1}ADB B^{-1}e_j
=
e_i^{\mathsf T}De_j.
\]

This identity is the basic bridge between the packet interpolation modes and the classical root-function theory.

---

## 2. Exact root orders

A holomorphic vector germ \(r(h)\) is a right root function of exact order \(q\ge1\) at \(h=0\) if

\[
J(h)r(h)=h^q a(h),
\qquad
a(0)\ne0,
\]

and \(r(0)\ne0\). Since \(J\) is a regular square germ, there is no rational nullspace that must be quotiented out.

### Theorem 2.1 - Smith-frame roots

For every index \(i\) with \(\alpha_i>0\), the germ

\[
r_i(h)=B(h)^{-1}e_i
\]

is a root function of exact order \(\alpha_i\). More precisely,

\[
\boxed{
J(h)r_i(h)
=
h^{\alpha_i}a_i(h),
\qquad
a_i(h):=A(h)e_i,
}
\]

and

\[
a_i(0)=A(0)e_i\ne0.
\]

For \(\alpha_i=0\), the same formula gives a regular nonvanishing source mode rather than a root function.

### Proof

The factorization gives

\[
Jr_i
=
ADB B^{-1}e_i
=
AD e_i
=
h^{\alpha_i}Ae_i.
\]

Since \(A(0)\) is invertible, \(A(0)e_i\ne0\). Also \(B(0)^{-1}e_i\ne0\). Therefore the vanishing order is exactly \(\alpha_i\). \(\square\)

### Corollary 2.2 - polynomial representatives

Expand

\[
r_i(h)=\sum_{s\ge0}r_{i,s}h^s.
\]

If \(\alpha_i>0\), then the Taylor polynomial

\[
p_i(h)
:=
\sum_{s=0}^{\alpha_i}r_{i,s}h^s
\]

is a root polynomial of exact order \(\alpha_i\).

### Proof

Because

\[
r_i(h)-p_i(h)=O(h^{\alpha_i+1}),
\]

and \(J(h)\) is holomorphic,

\[
J(h)p_i(h)
=
J(h)r_i(h)+O(h^{\alpha_i+1})
=
h^{\alpha_i}a_i(0)+O(h^{\alpha_i+1}).
\]

The leading coefficient is nonzero. \(\square\)

The degree-\(\alpha_i\) truncation is used here to guarantee that the exact order is preserved. A shorter truncation still satisfies the chain equations below, but its order can depend on the omitted coefficient.

---

## 3. A maximal set of packet root functions

Let

\[
I_+:=\{i:\alpha_i>0\}.
\]

For the packet cluster,

\[
|I_+|=2m-2.
\]

### Theorem 3.1 - maximal root system

The family

\[
\{r_i(h):i\in I_+\}
\]

is a maximal set of right root functions for the analytic germ \(J(h)\) at \(h=0\). Its orders are exactly the nonzero local Smith partial multiplicities

\[
1,2,\ldots,m-1,m+1,\ldots,2m-1.
\]

### Proof

For every \(i\in I_+\), Theorem 2.1 gives

\[
J(0)r_i(0)=0.
\]

The vectors \(r_i(0)=B(0)^{-1}e_i\) are linearly independent because \(B(0)^{-1}\) is invertible. Their number is

\[
2m-2
=
\operatorname{corank}J(0),
\]

so they form a basis of \(\ker J(0)\). Thus the set is complete.

In the diagonal model \(D(h)\), the standard coordinate roots \(e_i\), \(i\in I_+\), form the maximal root system and have orders \(\alpha_i\). Multiplication by the holomorphic invertible source factor \(B(h)^{-1}\) carries this system to the displayed packet roots without changing the orders or completeness. Hence the resulting set is maximal. \(\square\)

### Remark 3.2

The theorem does not make the individual germs \(r_i\) canonical. A different local Smith factorization can produce different representatives. What is canonical is developed in Section 6: the filtration and the associated-graded root lines.

---

## 4. Packet Jordan chains

Write the Taylor expansions

\[
J(h)=\sum_{a\ge0}J_a h^a,
\qquad
r_i(h)=\sum_{b\ge0}r_{i,b}h^b,
\]

where

\[
J_a=\frac1{a!}J^{(a)}(0).
\]

If \(\alpha_i>0\), the identity

\[
J(h)r_i(h)=h^{\alpha_i}a_i(h)
\]

implies that every coefficient below order \(\alpha_i\) vanishes.

### Theorem 4.1 - explicit Jordan-chain equations

For every \(i\in I_+\) and every

\[
0\le s<\alpha_i,
\]

we have

\[
\boxed{
\sum_{a=0}^{s}J_a r_{i,s-a}=0.
}
\]

Therefore

\[
\boxed{
(r_{i,0},r_{i,1},\ldots,r_{i,\alpha_i-1})
}
\]

is a Jordan chain of length \(\alpha_i\) for the analytic matrix function \(J\) at \(h=0\).

### Proof

The coefficient of \(h^s\) in \(J(h)r_i(h)\) is

\[
\sum_{a=0}^{s}J_a r_{i,s-a}.
\]

It vanishes for \(s<\alpha_i\). \(\square\)

### Theorem 4.2 - maximality of each Smith chain

The Jordan chain in Theorem 4.1 cannot be extended to length \(\alpha_i+1\) while keeping its first \(\alpha_i\) vectors fixed.

### Proof

Suppose there were a vector \(z\) such that

\[
\widetilde r(h)
=
\sum_{b=0}^{\alpha_i-1}r_{i,b}h^b+zh^{\alpha_i}
\]

satisfied

\[
J(h)\widetilde r(h)=O(h^{\alpha_i+1}).
\]

Set

\[
w(h)=B(h)\widetilde r(h).
\]

Because \(\widetilde r(0)=r_i(0)=B(0)^{-1}e_i\),

\[
w(0)=e_i.
\]

Since \(A\) is invertible, the assumed estimate is equivalent to

\[
D(h)w(h)=O(h^{\alpha_i+1}).
\]

But the \(i\)-th component is

\[
h^{\alpha_i}w_i(h),
\qquad
w_i(0)=1,
\]

which has exact order \(\alpha_i\), a contradiction. \(\square\)

Thus the explicit Hermite root germs generate maximal Jordan chains, not merely chains satisfying a finite collection of cancellation identities.

---

## 5. Identification with the explicit Hermite-dual modes

In the varying-shape construction, the packet Jacobian is written in grouped coordinates as

\[
J=C U,
\]

where \(U\) is the invertible diagonal coefficient matrix. The explicit column transformation \(P(h,\xi)\) satisfies

\[
C(h,p)P(h,\xi)=A(h,p)D_m(h),
\]

and the right regular factor is

\[
B=P^{-1}U.
\]

Consequently,

\[
\boxed{
B^{-1}=U^{-1}P.
}
\]

Therefore the right root functions are exactly the coefficient-corrected columns of the explicit interpolation transform \(P\).

The cluster columns of \(P\) were chosen to produce

\[
V_0,
D_0,D_1,\ldots,D_{m-1},
V_{m+1},\ldots,V_{2m-1}.
\]

Here:

- \(D_q\) is the Vandermonde-dual derivative combination;
- \(V_r\) is the Hermite coefficient-extraction combination.

Let \(p_{D_q}\) and \(p_{V_r}\) denote the corresponding columns of \(P\).

### Theorem 5.1 - explicit packet root modes

The collapsing right root functions are

\[
\boxed{
r_{D,q}(h)=U(h)^{-1}p_{D_q}(h),
\qquad
1\le q\le m-1,
}
\]

with exact orders

\[
\operatorname{ord}_J r_{D,q}=q,
\]

and

\[
\boxed{
r_{V,r}(h)=U(h)^{-1}p_{V_r}(h),
\qquad
m+1\le r\le2m-1,
}
\]

with exact orders

\[
\operatorname{ord}_J r_{V,r}=r.
\]

The modes associated with \(V_0\), \(D_0\), and the exterior packet columns have order zero and remain regular at the collision face.

### Proof

The columns of \(U^{-1}P=B^{-1}\) are the Smith-frame germs \(r_i=B^{-1}e_i\). Their diagonal entries in \(D_m\) are respectively

\[
1,
1,h,h^2,\ldots,h^{m-1},
h^{m+1},\ldots,h^{2m-1},
\]

with additional unit entries for the exterior modes. The result follows from Theorem 2.1. \(\square\)

### Corollary 5.2 - leading target jets

The explicit roots satisfy

\[
\boxed{
\lim_{h\to0}h^{-q}J(h)r_{D,q}(h)
=
\frac1{q!}M^{(q+1)}(x),
\qquad
1\le q\le m-1,
}
\]

and

\[
\boxed{
\lim_{h\to0}h^{-r}J(h)r_{V,r}(h)
=
\frac1{r!}M^{(r)}(x),
\qquad
m+1\le r\le2m-1.
}
\]

Thus the right root functions are not abstract Smith vectors. They are explicit source cancellations whose first surviving images are individual target jets.

---

## 6. Canonical filtration and associated-graded lines

For \(q\ge1\), define the root filtration

\[
\mathscr F^q
=
\left\{
v(0):
 v(h)\text{ is holomorphic and }J(h)v(h)=O(h^q)
\right\}.
\]

The local Smith form gives

\[
\mathscr F^q
=
B(0)^{-1}
\operatorname{span}
\{e_i:\alpha_i\ge q\}.
\]

Define the associated-graded root space

\[
\operatorname{gr}^q\mathscr F
:=
\mathscr F^q/\mathscr F^{q+1}.
\]

### Theorem 6.1 - intrinsic graded dimensions

For every \(q\ge1\),

\[
\boxed{
\dim\operatorname{gr}^q\mathscr F
=
\#\{i:\alpha_i=q\}.
}
\]

For the packet cluster,

\[
\boxed{
\dim\operatorname{gr}^q\mathscr F
=
\begin{cases}
1,
& q\in\{1,\ldots,m-1,m+1,\ldots,2m-1\},\\
0,
& q=m,
\end{cases}
}
\]

and the graded spaces vanish outside the positive partial-multiplicity list.

### Proof

The quotient removes precisely those Smith coordinates with exponent at least \(q+1\), leaving one basis class for each coordinate with exponent exactly \(q\). \(\square\)

### Corollary 6.2 - precise canonicality statement

If \(\alpha_i=q>0\), then

\[
[r_i(0)]
\in
\operatorname{gr}^q\mathscr F
\]

spans the corresponding one-dimensional graded root space.

Any other maximal root system produces the same line. Its representative can differ from \(r_i(0)\) by:

- a nonzero scalar;
- a vector in \(\mathscr F^{q+1}\);
- frame-dependent higher Taylor terms.

Therefore the Hermite-dual root mode is a distinguished lift of a canonical graded line, not an absolutely canonical vector germ.

### Corollary 6.3 - invariant meaning of the missing exponent

Because

\[
\operatorname{gr}^m\mathscr F=0,
\]

we have

\[
\boxed{
\mathscr F^m=\mathscr F^{m+1}.
}
\]

Thus order \(m\) introduces no new independent root direction. This is the intrinsic filtration statement behind the missing Smith exponent.

This does not forbid writing a nonmaximal root function whose image happens to vanish to exact order \(m\). It says that no new associated-graded root line and no partial multiplicity occur at order \(m\).

---

## 7. Why the exponent \(m\) is missing

The explicit interpolation construction provides a direct jet-level mechanism for the invariant gap.

The Vandermonde-dual derivative modes satisfy

\[
h^{-q}D_q(h)
\longrightarrow
\frac1{q!}M^{(q+1)}(x).
\]

At the top derivative-dual order \(q=m-1\),

\[
\boxed{
h^{-(m-1)}D_{m-1}(h)
\longrightarrow
\frac1{(m-1)!}M^{(m)}(x).
}
\]

A hypothetical Hermite coefficient-extraction mode \(V_m\) would satisfy

\[
\boxed{
h^{-m}V_m(h)
\longrightarrow
\frac1{m!}M^{(m)}(x).
}
\]

The two limiting columns are proportional. They cannot both occur as independent columns of the invertible regular boundary factor \(A(0)\).

The actual packet basis selects

\[
V_0
\rightsquigarrow
M^{(0)}(x),
\]

\[
D_0,\ldots,D_{m-1}
\rightsquigarrow
M^{(1)}(x),\ldots,M^{(m)}(x),
\]

and

\[
V_{m+1},\ldots,V_{2m-1}
\rightsquigarrow
M^{(m+1)}(x),\ldots,M^{(2m-1)}(x).
\]

Hence the limiting cluster block contains exactly one representative of every target jet

\[
M^{(0)}(x),M^{(1)}(x),\ldots,M^{(2m-1)}(x).
\]

### Proposition 7.1 - jet-duplication mechanism

The omission of the \(V_m\) mode is exactly what prevents duplication of the target jet \(M^{(m)}(x)\) at the boundary. The explicit Hermite-dual construction therefore realizes the invariant Smith gap through the proportionality

\[
\frac1{(m-1)!}M^{(m)}(x)
\parallel
\frac1{m!}M^{(m)}(x).
\]

### Proof

The displayed jet limits show that \(D_{m-1}\) and the hypothetical \(V_m\) have the same leading target line after their respective normalizations. If both were used, the limiting regular cluster block would contain two proportional columns and would be singular. The chosen list replaces \(V_m\) by \(D_{m-1}\) and retains all higher coefficient-extraction modes, producing the complete independent jet basis through order \(2m-1\). \(\square\)

Combined with the uniqueness of local Smith partial multiplicities, this gives both:

1. a constructive explanation of the gap in the Hermite frame;
2. an invariant proof that no holomorphic invertible frame change can restore a partial multiplicity at \(m\).

---

## 8. Left-right root duality and the inverse pole

The exact diagonal pairing also identifies the Laurent coefficients of \(J^{-1}\).

Let \(i_{\max}\) be the unique index with

\[
\alpha_{i_{\max}}=2m-1.
\]

Define the metric left vector

\[
\ell_{i}(0)
:=
A(0)^{-*}e_i.
\]

It represents the algebraic row \(\lambda_i(0)^{\mathsf T}\) under the standard Hermitian inner product.

### Theorem 8.1 - deepest inverse residue from root modes

As \(h\to0\) along the positive real scale,

\[
\boxed{
h^{2m-1}J(h)^{-1}
\longrightarrow
r_{i_{\max}}(0)\,\ell_{i_{\max}}(0)^*.
}
\]

Consequently,

\[
\boxed{
\lim_{h\to0^+}
h^{2m-1}\|J(h)^{-1}\|
=
\|r_{i_{\max}}(0)\|\,\|\ell_{i_{\max}}(0)\|.
}
\]

Equivalently, the deepest singular value satisfies

\[
\boxed{
\sigma_{\min}(J(h))
\sim
\frac{h^{2m-1}}
{\|r_{i_{\max}}(0)\|\,\|\ell_{i_{\max}}(0)\|}.
}
\]

### Proof

From

\[
J^{-1}=B^{-1}D^{-1}A^{-1},
\]

multiplication by \(h^{2m-1}\) kills every diagonal inverse term except the unique deepest coordinate. Thus

\[
h^{2m-1}J^{-1}
\longrightarrow
B(0)^{-1}e_{i_{\max}}e_{i_{\max}}^{\mathsf T}A(0)^{-1}.
\]

The left row is represented by \(A(0)^{-*}e_{i_{\max}}\), giving the rank-one operator displayed above. Its norm is the product of the two vector norms. \(\square\)

This identifies the previously computed deepest packet vectors with the terminal right and left members of the maximal root system.

---

## 9. Exterior powers as wedges of canonical graded roots

Order the positive exponents increasingly and select the \(k\) deepest indices

\[
I_k=\{i_1,\ldots,i_k\}.
\]

Let

\[
S_k=\sum_{i\in I_k}\alpha_i.
\]

Define the right root wedge

\[
R_{I_k}
:=
r_{i_1}(0)\wedge\cdots\wedge r_{i_k}(0),
\]

and the metric left root wedge

\[
L_{I_k}
:=
\ell_{i_1}(0)\wedge\cdots\wedge\ell_{i_k}(0).
\]

### Theorem 9.1 - root-wedge form of the exterior limit

\[
\boxed{
h^{S_k}\bigwedge^k J(h)^{-1}
\longrightarrow
R_{I_k}L_{I_k}^*.
}
\]

Therefore

\[
\boxed{
\lim_{h\to0^+}
h^{S_k}
\left\|\bigwedge^kJ(h)^{-1}\right\|
=
\|R_{I_k}\|\,\|L_{I_k}\|.
}
\]

### Proof

Take exterior powers in

\[
J^{-1}=B^{-1}D^{-1}A^{-1}.
\]

After multiplication by \(h^{S_k}\), the unique deepest \(k\)-coordinate of \(igwedge^kD^{-1}\) survives. Applying the exterior powers of \(B(0)^{-1}\) and \(A(0)^{-1}\) produces precisely the right and left root wedges. \(\square\)

### Corollary 9.2

The exact cumulative and individual singular-value constants proved elsewhere in the repository are Euclidean volume invariants of the maximal right and left root systems.

In particular, after ordering the roots from deepest to shallowest and orthogonally removing the deeper root directions, the constant at each exponent is

\[
\boxed{
c_k
=
\frac1{\|\widehat r_k\|\,\|\widehat\ell_k\|}.
}
\]

Thus the exterior-power constant hierarchy is the metric refinement of the classical maximal-root-function hierarchy.

---

## 10. Behavior under a different Smith frame

Suppose

\[
J=\widehat A D\widehat B
\]

is another local Smith factorization with the same ordered diagonal \(D\). Let

\[
\widehat r_i=\widehat B^{-1}e_i.
\]

The individual vectors \(r_i(0)\) and \(\widehat r_i(0)\) need not agree. However, both determine the same intrinsic filtration

\[
\mathscr F^q
=
\{v(0):Jv=O(h^q)\}.
\]

Because the positive packet partial multiplicities are simple, for each packet exponent \(q\),

\[
\operatorname{gr}^q\mathscr F
\]

is one-dimensional. Therefore

\[
[\widehat r_q(0)]
=
c_q[r_q(0)]
\]

for some nonzero scalar \(c_q\) in the graded quotient.

This is the correct gauge statement:

> The root function is frame-dependent, while its order and associated-graded line are frame-independent.

The same statement holds across ordered collision-chart overlaps, because changing the boundary defining function by a nonvanishing unit and changing source or target frames holomorphically does not alter the local partial multiplicities or root filtration.

---

## 11. Relation to the rescaled tangent bundle

The cluster-rescaled tangent frame is

\[
T(h)=B(h)^{-1}D(h)^{-1}.
\]

Its \(i\)-th column is

\[
T_i(h)=h^{-\alpha_i}r_i(h).
\]

Thus the rescaled tangent bundle is obtained by dividing every Smith-frame root function by its exact root order.

The lifted realization differential satisfies

\[
JT=A,
\]

so

\[
J(h)T_i(h)=a_i(h)
\longrightarrow
a_i(0)\ne0.
\]

Therefore the rescaled tangent construction has the following intrinsic interpretation:

> Each canonical graded root direction is promoted to a finite boundary vector by dividing a distinguished root representative by the power prescribed by its local partial multiplicity.

The local Smith form determines the powers and the filtration. The Hermite construction supplies explicit lifts. The Euclidean realization metric supplies the boundary inner products.

---

## 12. Claim boundary

The following statements are classical in general analytic matrix theory:

- local Smith partial multiplicities;
- root functions and maximal root systems;
- equivalence between root orders and nonzero partial multiplicities;
- translation between root functions and Jordan chains;
- left-right systems and Laurent inversion.

The packet-specific results established here are:

1. the explicit root functions are the coefficient-corrected Vandermonde-dual and Hermite coefficient-extraction modes;
2. their exact orders are
   \[
   1,2,\ldots,m-1,m+1,\ldots,2m-1;
   \]
3. their first surviving images are explicit moment jets;
4. the missing exponent \(m\) is exposed by duplication of the \(M^{(m)}(x)\) target jet;
5. every positive associated-graded packet root space is one-dimensional;
6. the exterior singular constants are norms of wedges of the resulting right and left root modes;
7. the packet-rescaled tangent frame is the maximal root system divided by its exact orders.

The strongest safe summary is:

> The Hermite-dual packet modes form an explicit maximal system of root functions for the coalescing Prony Jacobian. Their orders are the packet local Smith partial multiplicities, their Taylor coefficients generate maximal Jordan chains, and their leading classes form canonical one-dimensional graded root spaces. The rescaled tangent bundle is obtained by desingularizing these root functions order by order, while the exact singular constants measure the Euclidean volumes of the corresponding right-left root wedges.

---

## References

- I. Gohberg, M. A. Kaashoek, and F. van Schagen, *On the local theory of regular analytic matrix functions*, Linear Algebra and its Applications 182 (1993), 9-25. DOI: `10.1016/0024-3795(93)90488-A`.
- M. Franchi and P. Paruolo, *Inversion of regular analytic matrix functions: Local Smith form and subspace duality*, Linear Algebra and its Applications 435 (2011), 2896-2912. DOI: `10.1016/j.laa.2011.05.005`.
- F. M. Dopico and V. Noferini, *Root polynomials and their role in the theory of matrix polynomials*, Linear Algebra and its Applications 584 (2020), 37-78. DOI: `10.1016/j.laa.2019.09.006`.
- J. Wilkening, *An algorithm for computing Jordan chains and inverting analytic matrix functions*, Linear Algebra and its Applications 427 (2007), 6-25. DOI: `10.1016/j.laa.2007.06.012`.
