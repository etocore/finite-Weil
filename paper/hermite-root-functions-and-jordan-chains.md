# Hermite root functions, Jordan chains, and canonical graded packet modes

## Status

This note identifies the explicit Hermite-dual source modes in the packet collision normal form with the root functions and Jordan chains of the classical local theory of regular analytic matrix functions.

The publication-level distinction is:

- individual Hermite-dual root germs depend on the chosen Smith frame and interpolation normalization;
- their orders, filtration, and associated-graded lines are intrinsic;
- every positive packet partial multiplicity is simple, so every nonzero graded root space is one-dimensional;
- the Hermite construction gives a distinguished representative of each canonical graded line.

No novelty is claimed for the general theory of root functions, Jordan chains, or local Smith forms. The packet-specific content is the explicit realization of these objects by Vandermonde-dual and Hermite coefficient-extraction modes, with order list

\[
0^{\times(2N-2m+2)},
1,2,\ldots,m-1,m+1,\ldots,2m-1.
\]

---

## 1. Analytic Smith frame

Fix the non-scale variables in a nondegenerate ordered common-scale collision chart. The established normal form is

\[
J(h)=A(h)D(h)B(h),
\]

where \(A,B,A^{-1},B^{-1}\) are holomorphic near \(h=0\), and

\[
D(h)=\operatorname{diag}
\bigl(h^{\alpha_1},\ldots,h^{\alpha_{2N}}\bigr),
\qquad
0\le\alpha_1\le\cdots\le\alpha_{2N}.
\]

For an \(m\)-node cluster,

\[
(\alpha_i)
=
\left(
\underbrace{0,\ldots,0}_{2N-2m+2},
1,2,\ldots,m-1,
m+1,\ldots,2m-1
\right).
\]

Define the right Smith-frame germs

\[
r_i(h):=B(h)^{-1}e_i
\]

and the algebraic left row germs

\[
\lambda_i(h)^{\mathsf T}
:=
e_i^{\mathsf T}A(h)^{-1}.
\]

They satisfy the exact pairing

\[
\boxed{
\lambda_i(h)^{\mathsf T}J(h)r_j(h)
=
\delta_{ij}h^{\alpha_j}.
}
\]

This follows immediately from

\[
e_i^{\mathsf T}A^{-1}(ADB)B^{-1}e_j
=
e_i^{\mathsf T}De_j.
\]

---

## 2. Exact root functions

A holomorphic vector germ \(r(h)\) is a right root function of exact order \(q\ge1\) if

\[
J(h)r(h)=h^q a(h),
\qquad
a(0)\ne0,
\qquad
r(0)\ne0.
\]

Because \(J\) is a regular square germ, there is no rational nullspace to quotient out.

### Theorem 2.1 - Smith-frame roots

For every \(i\) with \(\alpha_i>0\),

\[
\boxed{
r_i(h)=B(h)^{-1}e_i
}
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

with

\[
a_i(0)=A(0)e_i\ne0.
\]

For \(\alpha_i=0\), the same formula gives a regular source mode.

### Proof

\[
Jr_i
=
ADB B^{-1}e_i
=
AD e_i
=
h^{\alpha_i}Ae_i.
\]

The invertibility of \(A(0)\) and \(B(0)\) proves exactness and nonvanishing. \(\square\)

### Corollary 2.2 - polynomial representatives

Write

\[
r_i(h)=\sum_{s\ge0}r_{i,s}h^s.
\]

For \(\alpha_i>0\), the Taylor polynomial

\[
p_i(h)
:=
\sum_{s=0}^{\alpha_i}r_{i,s}h^s
\]

is a root polynomial of exact order \(\alpha_i\).

Indeed,

\[
r_i-p_i=O(h^{\alpha_i+1})
\]

implies

\[
Jp_i
=
h^{\alpha_i}a_i(0)+O(h^{\alpha_i+1}).
\]

The degree-\(\alpha_i\) truncation is used to preserve the exact order automatically.

---

## 3. Maximal root system

Let

\[
I_+:=\{i:\alpha_i>0\}.
\]

For the packet cluster,

\[
|I_+|=2m-2.
\]

### Theorem 3.1

The family

\[
\boxed{
\{r_i(h):i\in I_+\}
}
\]

is a maximal set of right root functions for \(J\) at \(h=0\). Its orders are

\[
\boxed{
1,2,\ldots,m-1,m+1,\ldots,2m-1.
}
\]

### Proof

For \(i\in I_+\),

\[
J(0)r_i(0)=0.
\]

The vectors \(r_i(0)=B(0)^{-1}e_i\) are linearly independent. Their number equals

\[
2m-2=\operatorname{corank}J(0),
\]

so they form a basis of \(\ker J(0)\) and the system is complete.

For the diagonal germ \(D\), the standard coordinate roots \(e_i\), \(i\in I_+\), form a maximal system with orders \(\alpha_i\). The holomorphic invertible source transformation \(B^{-1}\) carries that system to the displayed roots without changing completeness or order. \(\square\)

The individual roots are not unique. Their intrinsic content is the graded filtration developed below.

---

## 4. Jordan chains

Expand

\[
J(h)=\sum_{a\ge0}J_a h^a,
\qquad
r_i(h)=\sum_{b\ge0}r_{i,b}h^b,
\qquad
J_a=\frac1{a!}J^{(a)}(0).
\]

### Theorem 4.1 - chain equations

For every \(i\in I_+\) and every \(0\le s<\alpha_i\),

\[
\boxed{
\sum_{a=0}^{s}J_a r_{i,s-a}=0.
}
\]

Hence

\[
\boxed{
(r_{i,0},r_{i,1},\ldots,r_{i,\alpha_i-1})
}
\]

is a Jordan chain of length \(\alpha_i\) for the analytic matrix function \(J\) at \(h=0\).

### Proof

The displayed convolution is the coefficient of \(h^s\) in \(J(h)r_i(h)\), which vanishes below order \(\alpha_i\). \(\square\)

### Theorem 4.2 - nonextendability

The chain above cannot be extended to length \(\alpha_i+1\) while keeping its first \(\alpha_i\) vectors fixed.

### Proof

Suppose a vector \(z\) made

\[
\widetilde r(h)
=
\sum_{b=0}^{\alpha_i-1}r_{i,b}h^b+zh^{\alpha_i}
\]

satisfy

\[
J(h)\widetilde r(h)=O(h^{\alpha_i+1}).
\]

Set \(w(h)=B(h)\widetilde r(h)\). Since

\[
\widetilde r(0)=B(0)^{-1}e_i,
\]

we have \(w(0)=e_i\). Invertibility of \(A\) makes the assumed estimate equivalent to

\[
D(h)w(h)=O(h^{\alpha_i+1}).
\]

Its \(i\)-th component is

\[
h^{\alpha_i}w_i(h),
\qquad
w_i(0)=1,
\]

which has exact order \(\alpha_i\), a contradiction. \(\square\)

Thus the explicit packet roots generate maximal Jordan chains, not merely finite cancellation identities.

---

## 5. The Hermite-dual roots explicitly

In grouped coordinates the packet Jacobian has the form

\[
J=C U,
\]

where \(U\) is the invertible diagonal coefficient matrix. The explicit interpolation transform \(P(h,\xi)\) satisfies

\[
C(h)P(h)=A(h)D_m(h),
\]

and

\[
B=P^{-1}U.
\]

Therefore

\[
\boxed{
B^{-1}=U^{-1}P.
}
\]

The right root functions are exactly the coefficient-corrected columns of \(P\).

The cluster columns of \(P\) produce

\[
V_0,
D_0,D_1,\ldots,D_{m-1},
V_{m+1},\ldots,V_{2m-1},
\]

where \(D_q\) is the Vandermonde-dual derivative combination and \(V_r\) is the Hermite coefficient-extraction combination.

Let \(p_{D_q}\) and \(p_{V_r}\) denote the corresponding columns of \(P\).

### Theorem 5.1 - explicit packet root modes

The derivative-dual roots are

\[
\boxed{
r_{D,q}(h)=U(h)^{-1}p_{D_q}(h),
\qquad
1\le q\le m-1,
}
\]

with exact order

\[
\operatorname{ord}_J r_{D,q}=q.
\]

The Hermite coefficient-extraction roots are

\[
\boxed{
r_{V,r}(h)=U(h)^{-1}p_{V_r}(h),
\qquad
m+1\le r\le2m-1,
}
\]

with exact order

\[
\operatorname{ord}_J r_{V,r}=r.
\]

The modes \(V_0\), \(D_0\), and the exterior packet columns have order zero.

### Corollary 5.2 - first surviving target jets

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

Thus the packet root functions are explicit source cancellations whose first surviving images are individual moment jets.

---

## 6. Canonical root filtration

For \(q\ge1\), define

\[
\mathscr F^q
=
\left\{
v(0):v(h)\text{ is holomorphic and }J(h)v(h)=O(h^q)
\right\}.
\]

The Smith form gives

\[
\boxed{
\mathscr F^q
=
B(0)^{-1}
\operatorname{span}\{e_i:\alpha_i\ge q\}.
}
\]

Define

\[
\operatorname{gr}^q\mathscr F
:=
\mathscr F^q/\mathscr F^{q+1}.
\]

### Theorem 6.1 - graded dimensions

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
& q=m.
\end{cases}
}
\]

For every packet exponent \(q>0\), the class of the corresponding Hermite root

\[
[r_q(0)]\in\operatorname{gr}^q\mathscr F
\]

spans the canonical one-dimensional graded line.

Any other maximal root system gives the same line. A representative may change by a nonzero scalar, a vector in \(\mathscr F^{q+1}\), and frame-dependent higher Taylor terms.

Therefore:

> The Hermite-dual root is a distinguished lift of a canonical graded line, not an absolutely canonical germ.

### Corollary 6.2 - intrinsic missing exponent

Since

\[
\operatorname{gr}^m\mathscr F=0,
\]

we have

\[
\boxed{
\mathscr F^m=\mathscr F^{m+1}.
}
\]

Order \(m\) creates no new independent root direction and no partial multiplicity.

This does not prohibit a nonmaximal root function whose image happens to have exact order \(m\). It says there is no new associated-graded root line at that order.

---

## 7. Jet mechanism for the missing exponent

The top derivative-dual mode satisfies

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

The two limiting columns are proportional. They cannot both occur as independent columns of the invertible boundary factor \(A(0)\).

The actual basis selects

\[
V_0\rightsquigarrow M^{(0)}(x),
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

It therefore contains exactly one representative of every target jet

\[
M^{(0)}(x),M^{(1)}(x),\ldots,M^{(2m-1)}(x).
\]

### Proposition 7.1 - jet-duplication mechanism

The omission of \(V_m\) prevents duplication of the target line \(\mathbb C M^{(m)}(x)\). This is the explicit Hermite-frame mechanism behind the invariant Smith gap.

Combined with uniqueness of the local partial multiplicities, this gives both a constructive explanation of the gap and an invariant proof that an invertible holomorphic frame change cannot restore a partial multiplicity at \(m\).

---

## 8. Left-right duality and inverse residues

For the Euclidean metric, represent the algebraic left row at the boundary by

\[
\ell_i:=A(0)^{-*}e_i.
\]

Let \(i_{\max}\) be the unique index with

\[
\alpha_{i_{\max}}=2m-1.
\]

### Theorem 8.1 - deepest inverse residue

Along \(h>0\),

\[
\boxed{
h^{2m-1}J(h)^{-1}
\longrightarrow
r_{i_{\max}}(0)\ell_{i_{\max}}^*.
}
\]

Consequently,

\[
\boxed{
\lim_{h\to0^+}h^{2m-1}\|J(h)^{-1}\|
=
\|r_{i_{\max}}(0)\|\,\|\ell_{i_{\max}}\|,
}
\]

and

\[
\boxed{
\sigma_{\min}(J(h))
\sim
\frac{h^{2m-1}}
{\|r_{i_{\max}}(0)\|\,\|\ell_{i_{\max}}\|}.
}
\]

### Proof

From

\[
J^{-1}=B^{-1}D^{-1}A^{-1},
\]

multiplication by \(h^{2m-1}\) removes every diagonal inverse term except the unique deepest coordinate. The limit is

\[
B(0)^{-1}e_{i_{\max}}e_{i_{\max}}^{\mathsf T}A(0)^{-1},
\]

which is the displayed rank-one operator. \(\square\)

This identifies the deepest vectors previously computed in the repository with the terminal right and left modes of the maximal root system.

---

## 9. Exterior powers and root wedges

Let \(I_k=\{i_1,\ldots,i_k\}\) be the indices of the \(k\) deepest packet exponents and set

\[
S_k=\sum_{i\in I_k}\alpha_i.
\]

Define

\[
R_{I_k}
:=
r_{i_1}(0)\wedge\cdots\wedge r_{i_k}(0)
\]

and

\[
L_{I_k}
:=
\ell_{i_1}\wedge\cdots\wedge\ell_{i_k}.
\]

### Theorem 9.1 - root-wedge exterior limit

\[
\boxed{
h^{S_k}\bigwedge^kJ(h)^{-1}
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

After multiplication by \(h^{S_k}\), the unique deepest \(k\)-coordinate of

\[
\bigwedge^kD^{-1}
\]

survives. Applying the exterior powers of \(B(0)^{-1}\) and \(A(0)^{-1}\) gives the two displayed root wedges. \(\square\)

### Corollary 9.2 - metric refinement of the root hierarchy

The exact cumulative and individual singular-value constants proved elsewhere in the repository are Euclidean volume invariants of the maximal right and left root systems.

After ordering the roots from deepest to shallowest and orthogonally removing all deeper directions, the constant at each exponent is

\[
\boxed{
c_k
=
\frac1{\|\widehat r_k\|\,\|\widehat\ell_k\|}.
}
\]

Thus the exterior-power constant hierarchy is the metric refinement of the classical maximal-root-function hierarchy.

---

## 10. Rescaled tangent interpretation

The cluster-rescaled tangent frame is

\[
T(h)=B(h)^{-1}D(h)^{-1}.
\]

Its \(i\)-th column is

\[
\boxed{
T_i(h)=h^{-\alpha_i}r_i(h).
}
\]

Moreover,

\[
J(h)T_i(h)=A(h)e_i
\longrightarrow
A(0)e_i\ne0.
\]

Therefore the rescaled tangent bundle is obtained by dividing every Smith-frame root function by the power prescribed by its exact local partial multiplicity.

The intrinsic interpretation is:

> Each canonical graded root direction is promoted to a finite boundary vector by desingularizing a distinguished root representative at its exact order.

The local Smith form supplies the exponents and filtration. The Hermite transform supplies explicit lifts. The realization metric supplies the boundary inner products.

---

## 11. Claim boundary

The following are classical in general analytic matrix theory:

- local Smith partial multiplicities;
- root functions and maximal root systems;
- equality between maximal root orders and nonzero partial multiplicities;
- translation between root functions and Jordan chains;
- left-right root systems and Laurent inversion.

The packet-specific results established here are:

1. the explicit roots are the coefficient-corrected Vandermonde-dual and Hermite coefficient-extraction modes;
2. their exact orders are
   \[
   1,2,\ldots,m-1,m+1,\ldots,2m-1;
   \]
3. their first surviving images are explicit moment jets;
4. duplication of \(M^{(m)}(x)\) explains the omitted Hermite mode \(V_m\);
5. every positive associated-graded packet root space is one-dimensional;
6. the exterior singular constants are norms of wedges of right and left root modes;
7. the rescaled tangent frame is the maximal root system divided by its exact orders.

A safe summary is:

> The Hermite-dual packet modes form an explicit maximal system of root functions for the coalescing Prony Jacobian. Their orders are the packet local Smith partial multiplicities, their Taylor coefficients generate maximal Jordan chains, and their leading classes form canonical one-dimensional graded root spaces. The rescaled tangent bundle desingularizes these roots order by order, while the exact singular constants measure Euclidean volumes of the corresponding right-left root wedges.

---

## References

- I. Gohberg, M. A. Kaashoek, and F. van Schagen, *On the local theory of regular analytic matrix functions*, Linear Algebra and its Applications 182 (1993), 9-25. DOI: `10.1016/0024-3795(93)90488-A`.
- M. Franchi and P. Paruolo, *Inversion of regular analytic matrix functions: Local Smith form and subspace duality*, Linear Algebra and its Applications 435 (2011), 2896-2912. DOI: `10.1016/j.laa.2011.05.005`.
- F. M. Dopico and V. Noferini, *Root polynomials and their role in the theory of matrix polynomials*, Linear Algebra and its Applications 584 (2020), 37-78. DOI: `10.1016/j.laa.2019.09.006`.
- J. Wilkening, *An algorithm for computing Jordan chains and inverting analytic matrix functions*, Linear Algebra and its Applications 427 (2007), 6-25. DOI: `10.1016/j.laa.2007.06.012`.
