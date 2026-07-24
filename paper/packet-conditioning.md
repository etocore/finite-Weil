# Conditioning and local stability of finite exponential packet realizations

## Status

This note develops the local differential geometry of the finite exponential moment map

\[
\mathcal R_N(X,u)
=
(a_0,\ldots,a_{2N-1}),
\qquad
 a_k=\sum_{j=1}^N u_jx_j^k,
\]

on the reduced parameter space

\[
\mathcal P_N
=
\{(X,u)\in\mathbb C^N\times\mathbb C^N:
 x_i\neq x_j\ (i\neq j),\ u_j\neq0\}.
\]

The principal results are:

1. a coordinate-free proof that the Jacobian is invertible;
2. a rigorous local bi-Lipschitz stability theorem;
3. the definition of an absolute packet condition number;
4. the induced pullback metric and volume form;
5. a precise description of the singular boundary where conditioning can fail.

The invertibility result is classical in content and is equivalent to nonsingularity of a confluent Vandermonde matrix. The formulation through atomic-plus-dipole distributions and Hermite interpolation is adapted to the packet-transform program.

---

## 1. The realization map and its differential

For a tangent vector

\[
(\delta X,\delta u)
=
(\delta x_1,\ldots,\delta x_N,
 \delta u_1,\ldots,\delta u_N),
\]

the differential of the moment coordinates is

\[
\delta a_k
=
\sum_{j=1}^N x_j^k\,\delta u_j
+
\sum_{j=1}^N k u_jx_j^{k-1}\,\delta x_j,
\qquad 0\le k\le 2N-1.
\]

Thus, in the ordered coordinates

\[
(\delta u_1,\ldots,\delta u_N,
 \delta x_1,\ldots,\delta x_N),
\]

the Jacobian is the \(2N\times2N\) matrix

\[
J(X,u)
=
\begin{bmatrix}
1&\cdots&1&0&\cdots&0\\
x_1&\cdots&x_N&u_1&\cdots&u_N\\
x_1^2&\cdots&x_N^2&2u_1x_1&\cdots&2u_Nx_N\\
\vdots&&\vdots&\vdots&&\vdots\\
x_1^{2N-1}&\cdots&x_N^{2N-1}&
(2N-1)u_1x_1^{2N-2}&\cdots&(2N-1)u_Nx_N^{2N-2}
\end{bmatrix}.
\]

Equivalently,

\[
J(X,u)
=
\bigl[V(X)\mid V'(X)\operatorname{diag}(u)\bigr],
\]

where

\[
V(X)_{kj}=x_j^k,
\qquad
V'(X)_{kj}=kx_j^{k-1},
\qquad 0\le k\le2N-1.
\]

---

## 2. Distributional form of the tangent map

Associate to a tangent vector the distribution

\[
\mu_{\delta X,\delta u}
=
\sum_{j=1}^N \delta u_j\,\delta_{x_j}
-
\sum_{j=1}^N u_j\delta x_j\,\delta'_{x_j}.
\]

Because

\[
\delta'_{x_j}(p)=-p'(x_j),
\]

we have, for every polynomial \(p\),

\[
\mu_{\delta X,\delta u}(p)
=
\sum_{j=1}^N \delta u_jp(x_j)
+
\sum_{j=1}^N u_j\delta x_jp'(x_j).
\]

In particular,

\[
\mu_{\delta X,\delta u}(z^k)=\delta a_k.
\]

Hence the kernel of the Jacobian consists exactly of tangent distributions that annihilate all polynomials of degree at most \(2N-1\).

---

## 3. Hermite duality and local identifiability

### Theorem 3.1 - Jacobian invertibility

For every \((X,u)\in\mathcal P_N\), the Jacobian

\[
J(X,u)=D\mathcal R_N(X,u)
\]

is invertible.

### Proof

Assume

\[
J(X,u)(\delta X,\delta u)=0.
\]

Then

\[
\mu_{\delta X,\delta u}(p)=0
\]

for every polynomial \(p\) of degree at most \(2N-1\).

Fix an index \(i\). By classical Hermite interpolation, there exists a polynomial \(H_i\) of degree at most \(2N-1\) satisfying

\[
H_i(x_i)=1,
\qquad
H_i'(x_i)=0,
\]

and

\[
H_i(x_j)=H_i'(x_j)=0
\qquad (j\neq i).
\]

Therefore

\[
0=\mu_{\delta X,\delta u}(H_i)=\delta u_i.
\]

Again by Hermite interpolation, there exists a polynomial \(K_i\) of degree at most \(2N-1\) satisfying

\[
K_i(x_i)=0,
\qquad
K_i'(x_i)=1,
\]

and

\[
K_i(x_j)=K_i'(x_j)=0
\qquad (j\neq i).
\]

Hence

\[
0=\mu_{\delta X,\delta u}(K_i)=u_i\delta x_i.
\]

Since \(u_i\neq0\), we obtain \(\delta x_i=0\). As \(i\) was arbitrary,

\[
\delta X=0,
\qquad
\delta u=0.
\]

Thus \(\ker J(X,u)=\{0\}\). Since the Jacobian is square, it is invertible. \(\square\)

### Corollary 3.2 - local realization coordinates

The first \(2N\) moments

\[
(a_0,\ldots,a_{2N-1})
\]

form a local holomorphic coordinate system on \(\mathcal P_N\).

This follows immediately from the complex inverse function theorem.

---

## 4. Local bi-Lipschitz stability

Equip parameter space and moment space with fixed norms. For concreteness, use the Euclidean norm on \(\mathbb C^{2N}\).

### Theorem 4.1 - local Lipschitz stability

Fix \(\theta_0=(X_0,u_0)\in\mathcal P_N\). There exist neighborhoods

\[
U\ni\theta_0,
\qquad
V\ni\mathcal R_N(\theta_0),
\]

such that

\[
\mathcal R_N:U\to V
\]

is bijective, with a continuously differentiable inverse. Moreover, after shrinking \(U\) if necessary, there exists \(C>0\) such that

\[
\|\theta_1-\theta_2\|
\le
C\,
\|\mathcal R_N(\theta_1)-\mathcal R_N(\theta_2)\|
\]

for all \(\theta_1,\theta_2\in U\).

### Proof

By Theorem 3.1, \(D\mathcal R_N(\theta_0)\) is invertible. The inverse function theorem gives neighborhoods \(U,V\) and a \(C^1\) inverse

\[
\mathcal S_N:=\mathcal R_N^{-1}:V\to U.
\]

Shrink \(V\) to a convex neighborhood whose closure is compact and contained in the original inverse-function neighborhood. Continuity of \(D\mathcal S_N\) gives

\[
M:=\sup_{a\in V}\|D\mathcal S_N(a)\|<\infty.
\]

For \(a,b\in V\), integrate the derivative along the segment from \(a\) to \(b\):

\[
\mathcal S_N(a)-\mathcal S_N(b)
=
\int_0^1
D\mathcal S_N\bigl(b+t(a-b)\bigr)(a-b)\,dt.
\]

Therefore

\[
\|\mathcal S_N(a)-\mathcal S_N(b)\|
\le M\|a-b\|.
\]

Taking \(a=\mathcal R_N(\theta_1)\) and \(b=\mathcal R_N(\theta_2)\) proves the claim with \(C=M\). \(\square\)

### Remark 4.2

The theorem is local. It does not assert a uniform stability constant over all reduced packets. Such a global constant cannot persist near node collisions or vanishing coefficients, where the reduced parameterization approaches its singular boundary.

---

## 5. Absolute packet condition number

### Definition 5.1

For \(\theta=(X,u)\in\mathcal P_N\), define the absolute packet condition number

\[
\boxed{
\kappa_{\mathrm{abs}}(X,u)
:=
\|J(X,u)^{-1}\|.
}
\]

Under Euclidean norms,

\[
\boxed{
\kappa_{\mathrm{abs}}(X,u)
=
\frac{1}{\sigma_{\min}(J(X,u))}.
}
\]

This is the first-order amplification factor from moment perturbations to parameter perturbations.

Indeed, if

\[
\delta a=J\,\delta\theta,
\]

then

\[
\|\delta\theta\|
\le
\kappa_{\mathrm{abs}}(X,u)\,\|\delta a\|.
\]

The inequality is sharp at the linearized level.

### Definition 5.2 - local forward condition number

The corresponding forward sensitivity is

\[
\kappa_{\mathrm{fwd}}(X,u):=\|J(X,u)\|.
\]

The usual Jacobian condition number is

\[
\operatorname{cond}J(X,u)
=
\|J(X,u)\|\,\|J(X,u)^{-1}\|.
\]

These quantities depend on the chosen coordinates and norms. They are therefore metric data, not bare algebraic invariants.

---

## 6. Pullback metric and geometric interpretation

The Euclidean Hermitian metric on moment space pulls back through \(\mathcal R_N\) to

\[
\boxed{
 g_{(X,u)}(v,w)
=
\langle J(X,u)v,J(X,u)w\rangle.
}
\]

In matrix form,

\[
\boxed{
G(X,u)=J(X,u)^*J(X,u).
}
\]

By Theorem 3.1, \(G(X,u)\) is positive definite on \(\mathcal P_N\).

The extremal eigenvalues satisfy

\[
\lambda_{\min}(G)=\sigma_{\min}(J)^2,
\qquad
\lambda_{\max}(G)=\sigma_{\max}(J)^2.
\]

Hence

\[
\boxed{
\kappa_{\mathrm{abs}}(X,u)
=
\lambda_{\min}(G(X,u))^{-1/2}.
}
\]

Poor conditioning is therefore equivalent to near-degeneracy of the pullback metric.

### Volume density

The induced volume density in the ordered parameter coordinates is

\[
\sqrt{\det G}
=
|\det J|.
\]

Thus the Jacobian determinant, when explicitly evaluated, measures the local volume distortion between packet parameters and moment coordinates.

---

## 7. Singular boundary

The reduced parameter space excludes two types of degeneration:

1. coefficient loss:
   \[
   u_i\to0;
   \]
2. node collision:
   \[
   x_i-x_j\to0.
   \]

At either event, the ordinary \(N\)-packet chart ceases to represent a reduced packet of length \(N\).

### Proposition 7.1 - exact singular locus in the ambient chart

Consider the same Jacobian formula on all of \(\mathbb C^{2N}\). Then

\[
J(X,u)
\]

is singular whenever

\[
\prod_{i=1}^N u_i
\prod_{1\le i<j\le N}(x_j-x_i)=0.
\]

### Proof

If \(u_i=0\), the column corresponding to \(\delta x_i\) vanishes.

If \(x_i=x_j\), the columns corresponding to \(\delta u_i\) and \(\delta u_j\) coincide. Hence the Jacobian is singular. \(\square\)

Combined with Theorem 3.1, this identifies the singular locus exactly:

\[
\boxed{
\det J(X,u)=0
\iff
\left(\prod_i u_i\right)
\left(\prod_{i<j}(x_j-x_i)\right)=0.
}
\]

This statement identifies the zero set but not yet the exact multiplicities of its irreducible factors.

### Corollary 7.2 - blow-up along convergent singular sequences

Let \(\theta_m\in\mathcal P_N\) converge in \(\mathbb C^{2N}\) to a point \(\theta_*\) on the singular locus. Then

\[
\sigma_{\min}(J(\theta_m))\to0,
\]

and therefore

\[
\boxed{
\kappa_{\mathrm{abs}}(\theta_m)\to\infty.
}
\]

### Proof

The Jacobian depends continuously on the parameters. Since \(J(\theta_*)\) is singular, its smallest singular value is zero. Continuity of singular values gives the result. \(\square\)

This proves divergence of the absolute condition number near collisions and vanishing coefficients without requiring an explicit determinant formula.

---

## 8. Permutation symmetry

The symmetric group \(S_N\) acts on \(\mathcal P_N\) by simultaneous permutation of nodes and coefficients. The realization map is invariant under this action.

If \(P_\pi\) denotes the corresponding permutation matrix on parameter coordinates, then

\[
J(\pi\cdot(X,u))
=
J(X,u)P_\pi.
\]

Since \(P_\pi\) is unitary under the Euclidean norm,

\[
\sigma_{\min}(J(\pi\cdot(X,u)))
=
\sigma_{\min}(J(X,u)).
\]

Therefore

\[
\boxed{
\kappa_{\mathrm{abs}}(\pi\cdot(X,u))
=
\kappa_{\mathrm{abs}}(X,u).
}
\]

The condition number descends to the unordered reduced packet manifold

\[
\mathcal P_N/S_N.
\]

---

## 9. Explicit small cases

### Case \(N=1\)

The map is

\[
(a_0,a_1)=(u,ux),
\]

with Jacobian, in coordinates \((u,x)\),

\[
J=
\begin{bmatrix}
1&0\\
x&u
\end{bmatrix}.
\]

Thus

\[
\det J=u.
\]

The inverse map is explicit:

\[
u=a_0,
\qquad
x=\frac{a_1}{a_0}.
\]

The singular boundary is exactly \(u=0\).

### Case \(N=2\)

The Jacobian has columns

\[
\begin{aligned}
&[1,x_1,x_1^2,x_1^3]^\mathsf T,
&&[1,x_2,x_2^2,x_2^3]^\mathsf T,\\
&[0,u_1,2u_1x_1,3u_1x_1^2]^\mathsf T,
&&[0,u_2,2u_2x_2,3u_2x_2^2]^\mathsf T.
\end{aligned}
\]

Its determinant vanishes precisely when

\[
u_1u_2(x_2-x_1)=0.
\]

The exact exponent of the collision factor belongs to the general confluent Vandermonde determinant calculation developed in the companion checklist below.

---

## 10. Research objectives

The immediate quantitative problem is to replace the qualitative blow-up theorem by explicit estimates.

### Problem A - separation bounds

Find constants or asymptotic estimates for

\[
\sigma_{\min}(J(X,u))
\]

in terms of quantities such as

\[
\Delta(X):=\min_{i\neq j}|x_i-x_j|,
\qquad
u_{\min}:=\min_i|u_i|,
\qquad
R:=\max_i|x_i|.
\]

### Problem B - collision asymptotics

For a controlled two-node collision

\[
x_2=x_1+h,
\qquad h\to0,
\]

determine the leading asymptotic order of

\[
\sigma_{\min}(J)
\]

and hence of

\[
\kappa_{\mathrm{abs}}.
\]

### Problem C - optimal geometry

Under normalization constraints, identify configurations minimizing

\[
\kappa_{\mathrm{abs}}(X,u).
\]

Possible constraints include fixed centroid, fixed diameter, fixed coefficient norm, or confinement to a real interval or circle.

### Problem D - confluent compactification

Replace the singular ordinary chart at collisions by confluent coordinates involving

\[
e^{xz},\ ze^{xz},\ z^2e^{xz},\ldots
\]

and determine whether the induced metric extends after a suitable renormalization.

---

## 11. Proven versus open

### Proven here

- Jacobian invertibility on the reduced packet space.
- Local holomorphic coordinates given by the first \(2N\) moments.
- Local bi-Lipschitz stability.
- Exact characterization of the singular locus as collisions or vanishing coefficients.
- Divergence of the absolute condition number along convergent sequences approaching that locus.
- Pullback metric interpretation.
- Permutation invariance.

### Open in this note

- exact determinant formula, including multiplicities and sign;
- sharp lower bounds for \(\sigma_{\min}(J)\);
- precise collision exponents for the smallest singular value;
- global minimizers of the condition number under normalization;
- metric completion through confluent packets.

These open problems mark the transition from classical local identifiability to the quantitative geometry of packet realization.