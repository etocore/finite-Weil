# Proved equation inventory for packet conditioning

## Scope

This note collects the main proved equations and direct corollaries currently established for the finite exponential moment map

\[
\mathcal R_N(X,u)
=
(a_0,\ldots,a_{2N-1}),
\qquad
a_k=\sum_{j=1}^N u_jx_j^k.
\]

Write

\[
M(z)=(1,z,z^2,\ldots,z^{2N-1})^{\mathsf T}.
\]

In interleaved coordinates

\[
(u_1,x_1,\ldots,u_N,x_N),
\]

the Jacobian is

\[
J(X,u)
=
\bigl[
M(x_1),u_1M'(x_1),\ldots,M(x_N),u_NM'(x_N)
\bigr].
\]

The results below concern nonzero coefficients, pairwise-distinct exterior nodes, common-scale clusters with nondegenerate normalized shape, and the ordered common-scale blow-up atlas. They do not establish the unordered quotient, simultaneous or nested clusters, curvature, a Lie algebroid structure, or a global novelty claim.

---

## 1. Exact determinant and singular locus

In interleaved coordinates,

\[
\boxed{
\det J(X,u)
=
\left(\prod_{j=1}^N u_j\right)
\prod_{1\le i<j\le N}(x_j-x_i)^4.
}
\]

In grouped value-then-position coordinates,

\[
\boxed{
\det J_{\mathrm{grouped}}(X,u)
=
(-1)^{N(N-1)/2}
\left(\prod_{j=1}^N u_j\right)
\prod_{i<j}(x_j-x_i)^4.
}
\]

Hence

\[
\boxed{
J(X,u)\in GL(2N,\mathbb C)
\iff
\left(\prod_j u_j\right)
\left(\prod_{i<j}(x_j-x_i)\right)\ne0.
}
\]

---

## 2. Common-scale cluster normal form

Assume

\[
x_j(h)=x+h\xi_j,
\qquad 1\le j\le m,
\]

with

\[
\xi_i\ne\xi_j,
\qquad
u_j(h)\to u_j(0)\ne0,
\]

and all exterior nodes separated from \(x\). Then

\[
\boxed{
J(h)=A(h)D_m(h)B(h),
}
\]

where

\[
A(0),B(0)\in GL(2N,\mathbb C),
\]

and, after ordering adapted directions by exponent,

\[
\boxed{
D_m(h)
=
\operatorname{diag}
\left(
\underbrace{1,\ldots,1}_{2N-2m+2},
 h,h^2,\ldots,h^{m-1},
 h^{m+1},\ldots,h^{2m-1}
\right).
}
\]

Thus the complete exponent sequence is

\[
\boxed{
\underbrace{0,\ldots,0}_{2N-2m+2},
1,2,\ldots,m-1,m+1,\ldots,2m-1.
}
\]

The collapsing exponent set is

\[
\boxed{
\mathcal E_m
=
\{1,\ldots,m-1\}
\cup
\{m+1,\ldots,2m-1\}.
}
\]

In particular, the exponent \(m\) is absent.

---

## 3. Collision rank and corank

At \(h=0\),

\[
\boxed{
\operatorname{rank}J(0)
=
2+2(N-m)
=
2N-2m+2,
}
\]

and

\[
\boxed{
\operatorname{corank}J(0)=2m-2.
}
\]

For smooth source and target changes with invertible boundary derivatives,

\[
D(\Psi\circ\mathcal R_N\circ\Phi)(0)
=
D\Psi(0)J(0)D\Phi(0),
\]

so

\[
\boxed{
\operatorname{rank}D(\Psi\circ\mathcal R_N\circ\Phi)(0)
=
2N-2m+2.
}
\]

Therefore ordinary diffeomorphic coordinate changes cannot remove the collision rank defect.

---

## 4. Singular-value and condition-number hierarchy

Let

\[
\sigma_1(J(h))\ge\cdots\ge\sigma_{2N}(J(h)).
\]

The \(2m-2\) collapsing singular values have exponents

\[
\boxed{
1,2,\ldots,m-1,m+1,\ldots,2m-1.
}
\]

In particular,

\[
\boxed{
\sigma_{2N}(J(h))\asymp |h|^{2m-1},
}
\]

and for

\[
\kappa_{\mathrm{abs}}(J)=\|J^{-1}\|,
\]

\[
\boxed{
\kappa_{\mathrm{abs}}(J(h))
\asymp
|h|^{-(2m-1)}.
}
\]

The exponent sum is

\[
\boxed{
\sum_{e\in\mathcal E_m}e
=
\sum_{r=1}^{m-1}r+
\sum_{r=m+1}^{2m-1}r
=
2m(m-1)
=
4\binom m2.
}
\]

Since

\[
\prod_{1\le i<j\le m}(x_j-x_i)^4
=
h^{4\binom m2}
\prod_{i<j}(\xi_j-\xi_i)^4,
\]

the singular-value exponent sum agrees exactly with the determinant collision order.

---

## 5. Vandermonde-dual derivative modes

Let

\[
V_\xi=(\xi_j^q)_{
\substack{0\le q\le m-1\\1\le j\le m}}.
\]

For \(0\le q\le m-1\), define \(b^{(q)}\) by

\[
\boxed{
\sum_{j=1}^m b_j^{(q)}\xi_j^s
=
\delta_{qs},
\qquad 0\le s\le m-1.
}
\]

Set

\[
D_q(h)
=
\sum_{j=1}^m b_j^{(q)}M'(x+h\xi_j).
\]

Then

\[
\boxed{
D_q(h)
=
\frac{h^q}{q!}M^{(q+1)}(x)
+O(h^{q+1}),
}
\]

and therefore

\[
\boxed{
h^{-q}D_q(h)
\longrightarrow
\frac1{q!}M^{(q+1)}(x).
}
\]

These modes supply the exponents

\[
\boxed{0,1,2,\ldots,m-1.}
\]

---

## 6. Hermite interpolation identities

Let

\[
\ell_j(z)
=
\prod_{i\ne j}
\frac{z-x_i}{x_j-x_i}.
\]

Define

\[
H_j(z)
=
\left[1-2\ell_j'(x_j)(z-x_j)\right]\ell_j(z)^2,
\]

\[
K_j(z)
=
(z-x_j)\ell_j(z)^2.
\]

Then

\[
\boxed{
H_j(x_i)=\delta_{ij},
\qquad
H_j'(x_i)=0,
}
\]

\[
\boxed{
K_j(x_i)=0,
\qquad
K_j'(x_i)=\delta_{ij}.
}
\]

If

\[
p(z)=\sum_{k=0}^{2N-1}c_kz^k,
\qquad
\operatorname{coeff}p=(c_0,\ldots,c_{2N-1})^{\mathsf T},
\]

then

\[
(\operatorname{coeff}p)^{\mathsf T}M(t)=p(t),
\qquad
(\operatorname{coeff}p)^{\mathsf T}M'(t)=p'(t).
\]

Consequently, the inverse-Jacobian rows are

\[
\boxed{
(J^{-1})_{u_j,\cdot}
=
(\operatorname{coeff}H_j)^{\mathsf T},
}
\]

\[
\boxed{
(J^{-1})_{x_j,\cdot}
=
\frac1{u_j}(\operatorname{coeff}K_j)^{\mathsf T}.
}
\]

---

## 7. Cluster polynomial and Lagrange asymptotics

Define

\[
q_\xi(t)=\prod_{j=1}^m(t-\xi_j),
\]

\[
d_j=q_\xi'(\xi_j)
=
\prod_{i\ne j}(\xi_j-\xi_i),
\]

and

\[
s_j=
\sum_{i\ne j}\frac1{\xi_j-\xi_i}.
\]

Then

\[
\boxed{
q_\xi''(\xi_j)
=
2q_\xi'(\xi_j)s_j,
}
\]

so

\[
\boxed{
s_j
=
\frac{q_\xi''(\xi_j)}{2q_\xi'(\xi_j)}.
}
\]

Let

\[
E(z)=\prod_{\ell=m+1}^N(z-y_\ell),
\qquad
L(z)=\frac{(z-x)^{m-1}E(z)}{E(x)}.
\]

Then coefficient-wise,

\[
\boxed{
h^{m-1}\ell_j^{(h)}(z)
\longrightarrow
\frac1{d_j}L(z).
}
\]

For the packet-specific Hermite value-weight block \(A_m\),

\[
\boxed{
\det A_m
=
\pm\frac{m!}{\Delta(\xi)^3},
\qquad
\Delta(\xi)=\prod_{i<j}(\xi_j-\xi_i).
}
\]

Hence

\[
\boxed{
\det A_m\ne0
\iff
\Delta(\xi)\ne0.
}
\]

---

## 8. Exact deepest singular-value constant

Define

\[
P(z)
=
(z-x)^{2m-1}
\left(\frac{E(z)}{E(x)}\right)^2,
\]

and

\[
\boxed{
\Gamma(\xi)
=
\left(
\sum_{j=1}^m
\left|
\frac{q_\xi''(\xi_j)}{q_\xi'(\xi_j)^3}
\right|^2
\right)^{1/2}.
}
\]

The inverse has the rank-one leading limit

\[
\boxed{
h^{2m-1}J(h)^{-1}
\longrightarrow
r_\xi(\operatorname{coeff}P)^{\mathsf T},
}
\]

where the cluster-value entries of \(r_\xi\) are

\[
-\frac{q_\xi''(\xi_j)}{q_\xi'(\xi_j)^3}.
\]

Therefore

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
h^{2m-1}\|J(h)^{-1}\|
=
\Gamma(\xi)\,\|\operatorname{coeff}P\|_2.
}
\]

The deepest constant is independent of all nonzero packet coefficients in the fixed Euclidean parameter metric.

---

## 9. Exterior-power filtration

Suppose more generally that

\[
J(h)=A(h)D(h)B(h),
\]

with

\[
D(h)=\operatorname{diag}(h^{e_1},\ldots,h^{e_n}),
\qquad
0\le e_1\le\cdots\le e_n.
\]

For the \(k\) deepest scales define

\[
I_k=\{n-k+1,\ldots,n\},
\qquad
S_k=\sum_{i\in I_k}e_i.
\]

Then

\[
\boxed{
h^{S_k}\bigwedge^kJ(h)^{-1}
\longrightarrow
\left(\bigwedge^kB_0^{-1}\right)e_{I_k}
\left[
\left(\bigwedge^kA_0^{-*}\right)e_{I_k}
\right]^*.
}
\]

The limiting operator has rank one.

Define

\[
R_k=
\left\|
\left(\bigwedge^kB_0^{-1}\right)e_{I_k}
\right\|,
\]

\[
L_k=
\left\|
\left(\bigwedge^kA_0^{-*}\right)e_{I_k}
\right\|,
\]

\[
C_k=R_kL_k,
\qquad C_0=1.
\]

Then

\[
\boxed{
\lim_{h\to0^+}
h^{S_k}
\left\|\bigwedge^kJ(h)^{-1}\right\|
=
C_k.
}
\]

---

## 10. Exact constants for every collapsing singular value

The cumulative product satisfies

\[
\boxed{
\lim_{h\to0^+}
\frac{
\displaystyle\prod_{j=0}^{k-1}\sigma_{n-j}(J(h))
}{h^{S_k}}
=
\frac1{C_k}.
}
\]

If

\[
0<f_1<\cdots<f_s
\]

are the positive exponents, then

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_{n-k+1}(J(h))}{h^{f_{s-k+1}}}
=
\frac{C_{k-1}}{C_k}.
}
\]

Define

\[
r_k=B_0^{-1}e_{n-k+1},
\qquad
\ell_k=A_0^{-*}e_{n-k+1},
\]

and successively orthogonalize by

\[
\widehat r_k
=
P_{\operatorname{span}(r_1,\ldots,r_{k-1})^\perp}r_k,
\]

\[
\widehat\ell_k
=
P_{\operatorname{span}(\ell_1,\ldots,\ell_{k-1})^\perp}\ell_k.
\]

Then

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_{n-k+1}(J(h))}{h^{f_{s-k+1}}}
=
\frac1{\|\widehat r_k\|\,\|\widehat\ell_k\|}.
}
\]

Define the principal Gram blocks

\[
G_k^R
=
\left[(B_0^{-*}B_0^{-1})_{ij}\right]_{i,j\in I_k},
\]

\[
G_k^L
=
\left[(A_0^{-1}A_0^{-*})_{ij}\right]_{i,j\in I_k}.
\]

Then

\[
\boxed{
C_k^2
=
\det G_k^R\det G_k^L,
}
\]

and

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_{n-k+1}(J(h))}{h^{f_{s-k+1}}}
=
\left(
\frac{\det G_{k-1}^R\det G_{k-1}^L}
{\det G_k^R\det G_k^L}
\right)^{1/2}.
}
\]

For the complete collapsing block \(s=2m-2\),

\[
\boxed{
\prod_{j=0}^{s-1}\sigma_{2N-j}(J(h))
\sim
\frac{h^{2m(m-1)}}{C_s}.
}
\]

---

## 11. Exact two-node constants

For

\[
x_1=x,
\qquad
x_2=x+h,
\]

let \(P_0\) be orthogonal projection onto the orthogonal complement of the limiting regular range, and define

\[
a=P_0M''(x),
\]

\[
b_\perp
=
P_{\operatorname{ran}(M_0)^\perp\cap a^\perp}M'''(x).
\]

Then

\[
\boxed{
\lim_{h\to0}
\frac{\sigma_{2N-1}(J(h))}{|h|}
=
\frac{\|a\|}
{\sqrt{|u_1|^{-2}+|u_2|^{-2}}}.
}
\]

Also,

\[
\boxed{
\lim_{h\to0}
\frac{\sigma_{2N}(J(h))}{|h|^3}
=
\frac{\|b_\perp\|}{12\sqrt2}.
}
\]

Therefore

\[
\boxed{
\lim_{h\to0}|h|^3\kappa_{\mathrm{abs}}(J(h))
=
\frac{12\sqrt2}{\|b_\perp\|}.
}
\]

The two collapsing pullback-metric eigenvalues satisfy

\[
\boxed{
\lambda_{2N-1}(J^*J)\asymp |h|^2,
\qquad
\lambda_{2N}(J^*J)\asymp |h|^6.
}
\]

---

## 12. Complete symmetric three-node spectrum

For

\[
m=N=3,
\qquad
x=0,
\qquad
(\xi_1,\xi_2,\xi_3)=(-1,0,1),
\]

\[
u_1=u_2=u_3=1,
\]

in grouped coordinates

\[
(u_1,u_2,u_3,x_1,x_2,x_3),
\]

the exact collapsing spectrum is

\[
\boxed{
\sigma_3(J(h))\sim2\sqrt2\,h,
}
\]

\[
\boxed{
\sigma_4(J(h))\sim\sqrt6\,h^2,
}
\]

\[
\boxed{
\sigma_5(J(h))\sim\sqrt{\frac23}\,h^4,
}
\]

\[
\boxed{
\sigma_6(J(h))\sim\frac{2\sqrt2}{3}h^5.
}
\]

The product of the four constants is

\[
\boxed{
(2\sqrt2)(\sqrt6)
\left(\sqrt{\frac23}\right)
\left(\frac{2\sqrt2}{3}\right)
=
\frac{16}{3}.
}
\]

At \(h=0\), the two nonzero singular values are both 

\[
\sqrt3,
\]

so

\[
\boxed{
3\cdot\frac{16}{3}=16,
}
\]

matching the exact determinant coefficient

\[
\boxed{\det J(h)=16h^{12}.}
\]

---

## 13. Rescaled tangent frame and differential

Define

\[
\boxed{
T(h)=B(h)^{-1}D(h)^{-1}.
}
\]

Then

\[
\boxed{
J(h)T(h)=A(h).
}
\]

Thus

\[
\boxed{
\lim_{h\to0}J(h)T(h)=A_0\in GL(2N,\mathbb C).
}
\]

The dual rescaled coframe is

\[
\boxed{
\omega(h)=D(h)B(h)d\theta.
}
\]

Let

\[
R_0=\mathcal R_N(\theta_0),
\qquad
Y=A_0^{-1}(\mathcal R_N-R_0).
\]

Then

\[
\boxed{
dY=(A_0^{-1}A(h))\omega.
}
\]

With

\[
C(h)=A_0^{-1}A(h),
\]

\[
\boxed{
C(h)\to I,
\qquad
C(h),C(h)^{-1}=O(1).
}
\]

---

## 14. Renormalized pullback metric

Let

\[
G(h)=J(h)^*J(h).
\]

Then

\[
\boxed{
\widetilde G(h)
:=
T(h)^*G(h)T(h)
=
A(h)^*A(h).
}
\]

Therefore

\[
\boxed{
\widetilde G(0)=A_0^*A_0>0.
}
\]

The collapsing metric eigenvalue exponents are

\[
\boxed{
2,4,\ldots,2m-2,
2m+2,2m+4,\ldots,4m-2.
}
\]

Equivalently, for each \(e\in\mathcal E_m\),

\[
\boxed{
\lambda_e(G(h))\asymp |h|^{2e}.
}
\]

For every nonzero \(v\),

\[
\boxed{
v^*\widetilde G(0)v
=
\|A_0v\|^2
>0.
}
\]

---

## 15. Finite ordinary pullback distance

For a fixed-shape common-scale path 

\[
\theta(h)=(X(h),u(h)),
\]

with \(C^1\) coefficients, define

\[
L
=
\int_0^{h_0}
\sqrt{\theta'(h)^*G(h)\theta'(h)}\,dh.
\]

Because

\[
\sqrt{\theta'(h)^*G(h)\theta'(h)}
=
\left\|
\frac d{dh}\mathcal R_N(\theta(h))
\right\|_2,
\]

and the realization derivative is bounded near \(h=0\),

\[
\boxed{L<\infty.}
\]

---

## 16. Obstruction to ordinary resolving primitives

Suppose

\[
d\eta=C(h)\omega,
\qquad
C(h),C(h)^{-1}=O(1).
\]

Then

\[
\boxed{
\det D_\theta\eta
=
\det C(h)\det D(h)\det B(h).
}
\]

Since

\[
\boxed{
\det D(h)=h^{2m(m-1)},
}
\]

we obtain

\[
\boxed{
\det D_\theta\eta
=
O\!\left(h^{2m(m-1)}\right).
}
\]

Hence

\[
\boxed{
\det D_\theta\eta\big|_{h=0}=0.
}
\]

Thus no primitive boundedly equivalent to the rescaled coframe can be an ordinary boundary-resolving coordinate chart.

---

## 17. Ordered blow-up coordinates

For an ordered reference pair \((a,b)\), define

\[
\boxed{
x^{ab}=z_a,
\qquad
h^{ab}=z_b-z_a,
\qquad
\xi_j^{ab}=
\frac{z_j-z_a}{z_b-z_a}.
}
\]

Then

\[
\boxed{
\xi_a^{ab}=0,
\qquad
\xi_b^{ab}=1,
\qquad
z_j=x^{ab}+h^{ab}\xi_j^{ab}.
}
\]

At the boundary, with

\[
U=\sum_{j=1}^m u_j,
\]

the realization restricts to

\[
\boxed{
\mathcal R_N\big|_{h=0}
=
UM(x)
+
\sum_{\ell=m+1}^N u_\ell M(y_\ell).
}
\]

Therefore

\[
\boxed{
\frac{\partial\mathcal R_N}{\partial\xi_j}\bigg|_{h=0}=0,
}
\]

and for internal coefficient variations satisfying

\[
\sum_{j=1}^m\delta u_j=0,
\]

\[
\boxed{
d\mathcal R_N(\delta u)\big|_{h=0}=0.
}
\]

Within one compact ordered chart, if two boundary approaches have the same center, aggregate coefficient, and exterior packet, then

\[
\boxed{
d_{\mathrm{pullback}}(p(h),p'(h))\longrightarrow0.}
\]

---

## 18. Varying-shape analytic normal form

Let

\[
p=(x,\xi,u,\text{exterior data}).
\]

On each compact nondegenerate ordered shape chart,

\[
\boxed{
J(h,p)=A(h,p)D_m(h)B(h,p).
}
\]

The exponent matrix is independent of \(p\), while

\[
A,
\quad B,
\quad A^{-1},
\quad B^{-1}
\]

are jointly holomorphic and uniformly bounded on compact subcharts:

\[
\boxed{
\sup
\left(
\|A\|+\|A^{-1}\|+\|B\|+\|B^{-1}\|
\right)<\infty.
}
\]

A sufficient compact nondegeneracy condition is

\[
\boxed{
\inf_{p\in K}
\min_{i\ne j}|\xi_i-\xi_j|>0.
}
\]

This yields uniform boundedness of the interpolation inverses:

\[
\boxed{
\sup_{p\in K}
\left(
\|V_\xi^{-1}\|+\|\mathcal H_\xi^{-1}\|
\right)<\infty.
}
\]

---

## 19. Ordered-chart transition maps

From chart \((a,b)\) to chart \((c,d)\),

\[
\boxed{
x^{cd}
=
x^{ab}+h^{ab}\xi_c^{ab},
}
\]

\[
\boxed{
h^{cd}
=
h^{ab}(\xi_d^{ab}-\xi_c^{ab}),
}
\]

\[
\boxed{
\xi_j^{cd}
=
\frac{\xi_j^{ab}-\xi_c^{ab}}
{\xi_d^{ab}-\xi_c^{ab}}.
}
\]

The inverse and cocycle identities are

\[
\boxed{
\Phi_{cd}^{ab}
=
(\Phi_{ab}^{cd})^{-1},
}
\]

\[
\boxed{
\Phi_{cd}^{ef}\circ\Phi_{ab}^{cd}
=
\Phi_{ab}^{ef}.
}
\]

Physical node differences are invariant:

\[
\boxed{
h^{cd}(\xi_j^{cd}-\xi_i^{cd})
=
h^{ab}(\xi_j^{ab}-\xi_i^{ab})
=
z_j-z_i.
}
\]

Let

\[
\lambda_{ab}^{cd}(\xi)
=
\xi_d^{ab}-\xi_c^{ab}.
\]

Then

\[
\boxed{
h^{cd}=\lambda_{ab}^{cd}(\xi)h^{ab}.}
\]

For each exponent \(e\),

\[
\boxed{
(h^{cd})^e
=
\lambda_{ab}^{cd}(\xi)^e(h^{ab})^e.
}
\]

Thus the exponent filtration is chart-independent up to nowhere-vanishing factors.

For

\[
\Delta(\xi)=\prod_{i<j}(\xi_j-\xi_i),
\]

\[
\boxed{
\Delta(\xi^{cd})
=
\lambda_{ab}^{cd}(\xi)^{-\binom m2}
\Delta(\xi^{ab})
}
\]

up to the sign induced by label ordering. Consequently,

\[
\boxed{
(h^{cd})^{4\binom m2}\Delta(\xi^{cd})^4
=
(h^{ab})^{4\binom m2}\Delta(\xi^{ab})^4.
}
\]

---

## 20. Rescaled tangent-bundle transition law

Let

\[
Q_{ab}^{cd}=D\Phi_{ab}^{cd}.
\]

Then

\[
\boxed{
Q_{ab}^{cd}T_{ab}
=
T_{cd}G_{ab}^{cd},
}
\]

where

\[
\boxed{
G_{ab}^{cd}
=
A_{cd}^{-1}A_{ab}.
}
\]

The transition matrices satisfy

\[
\boxed{
G_{ab}^{ab}=I,
}
\]

\[
\boxed{
G_{cd}^{ab}
=
(G_{ab}^{cd})^{-1},
}
\]

\[
\boxed{
G_{cd}^{ef}G_{ab}^{cd}
=
G_{ab}^{ef}.
}
\]

Therefore the local rescaled tangent frames glue to an analytic vector bundle over the ordered common-scale blow-up atlas.

---

## 21. Metric compatibility across chart overlaps

Let

\[
\widetilde G_{ab}
=
T_{ab}^*J_{ab}^*J_{ab}T_{ab}.
\]

Then

\[
\boxed{
\widetilde G_{ab}
=
(G_{ab}^{cd})^*
\widetilde G_{cd}
G_{ab}^{cd}.
}
\]

For three overlapping charts,

\[
\boxed{
\widetilde G_{ab}
=
(G_{ab}^{ef})^*
\widetilde G_{ef}
G_{ab}^{ef}.
}
\]

Thus the positive-definite extended metric is globally compatible over the ordered common-scale atlas.

---

## 22. Determinant expansion for a common-scale cluster

Since

\[
x_j-x_i=h(\xi_j-\xi_i),
\]

\[
\boxed{
\prod_{1\le i<j\le m}(x_j-x_i)^4
=
h^{2m(m-1)}\Delta(\xi)^4.
}
\]

Hence

\[
\boxed{
\det J(h)
=
h^{2m(m-1)}\mathcal D_0
+o\!\left(h^{2m(m-1)}\right),
}
\]

where

\[
\boxed{
\mathcal D_0
=
\pm
\left(\prod_j u_j(0)\right)
\Delta(\xi)^4
\prod_{\substack{i\le m\\\ell>m}}(y_\ell-x)^4
\prod_{m<i<j}(y_j-y_i)^4.
}
\]

If the noncollapsing singular values converge to

\[
\alpha_1,\ldots,\alpha_{2N-2m+2}>0,
\]

then

\[
\boxed{
|\det J(h)|
\sim
\left(\prod_{j=1}^{2N-2m+2}\alpha_j\right)
\frac{|h|^{2m(m-1)}}{C_{2m-2}}.
}
\]

This agrees with the exact Vandermonde determinant asymptotic.

---

## 23. Remaining theorem targets

The following are not included as proved equations in this inventory:

\[
\boxed{
\text{unordered }S_m\text{-quotient},
\quad
\text{global metric completion across all strata},
}
\]

\[
\boxed{
\text{simultaneous and nested clusters},
\quad
\text{nonuniform collision trees},
}
\]

\[
\boxed{
\text{curvature formulas},
\quad
\text{Lie algebroid structure},
\quad
\text{global lower bounds}.
}
\]

A line-by-line comparison with the Prony, confluent-Vandermonde, analytic matrix-pencil, weighted-blow-up, and edge-geometry literature remains necessary before broad novelty claims are made.
