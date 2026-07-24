# Confluent rescaled geometry for packet-collision strata

## Status

This note begins the passage from ordinary node coordinates to a geometric structure adapted to packet collisions.

For a fixed-shape common-scale cluster, the ordinary realization Jacobian loses rank at the collision. No ordinary smooth coordinate change on the source or target can remove that rank defect. However, the previously proved cluster normal form canonically defines an anisotropically rescaled tangent bundle on which

1. the realization differential extends invertibly to the collision face;
2. the pullback metric extends to a positive-definite limit;
3. the ordinary collision boundary remains at finite pullback distance along the common-scale path.

The result is a differential-geometric desingularization. It does **not** yet prove that the rescaled coframe integrates to a holonomic coordinate chart.

---

## 1. Setup

Let

\[
\mathcal R_N(X,u)
=
\left(\sum_{j=1}^N u_jx_j^k\right)_{k=0}^{2N-1}
\]

and write

\[
M(z)=(1,z,z^2,\ldots,z^{2N-1})^{\mathsf T}.
\]

Fix an integer

\[
2\le m\le N.
\]

Let the first \(m\) nodes form a common-scale cluster

\[
x_j(h)=x+h\xi_j,
\qquad
1\le j\le m,
\]

where the offsets \(\xi_1,\ldots,\xi_m\) are fixed and pairwise distinct. The remaining nodes stay fixed, pairwise distinct, and separated from \(x\). Assume

\[
u_j(h)\longrightarrow u_j(0)\ne0.
\]

We work for real

\[
h>0,
\qquad
h\to0^+.
\]

Let

\[
J(h)=D\mathcal R_N(X(h),u(h))
\]

be the ordinary Jacobian in any fixed parameter ordering.

The common-scale cluster theorem gives an exact factorization

\[
\boxed{
J(h)=A(h)D(h)B(h),
}
\]

where \(A(h)\), \(B(h)\), and their inverses extend continuously, in fact analytically along the fixed-shape path, to \(h=0\), and

\[
A_0:=A(0),
\qquad
B_0:=B(0)
\]

are invertible.

After ordering the adapted directions by exponent,

\[
D(h)
=
\operatorname{diag}
\bigl(h^{e_1},\ldots,h^{e_{2N}}\bigr),
\]

with

\[
\boxed{
\underbrace{0,\ldots,0}_{2N-2m+2},
1,2,\ldots,m-1,
m+1,m+2,\ldots,2m-1.
}
\]

---

## 2. The ordinary rank defect is coordinate invariant

At \(h=0\), all cluster value columns equal \(M(x)\), and all cluster motion columns are scalar multiples of \(M'(x)\). The noncluster value and motion columns remain independent by generalized Hermite interpolation.

Therefore

\[
\boxed{
\operatorname{rank}J(0)
=
2+2(N-m)
=
2N-2m+2.
}
\]

The ordinary corank is

\[
\boxed{
\operatorname{corank}J(0)=2m-2.
}
\]

### Proposition 2.1 - impossibility of ordinary coordinate desingularization

Let \(\Phi\) be a \(C^1\) source-coordinate change and \(\Psi\) a \(C^1\) target-coordinate change, both having invertible derivatives at the collision point. Then

\[
D(\Psi\circ\mathcal R_N\circ\Phi)(0)
=
D\Psi(0)\,J(0)\,D\Phi(0),
\]

so

\[
\boxed{
\operatorname{rank}D(\Psi\circ\mathcal R_N\circ\Phi)(0)
=
2N-2m+2.
}
\]

Thus no ordinary smooth coordinate chart with bounded invertible Jacobian can turn the collision realization map into a local diffeomorphism.

### Proof

Left and right multiplication by invertible matrices preserve rank. \(\square\)

This establishes that the singularity is not an artifact of a poor but regular coordinate choice. Any successful desingularization must use a singular or blown-up change of scale.

---

## 3. The confluent-rescaled tangent frame

Define

\[
T(h)
:=
B(h)^{-1}D(h)^{-1}.
\]

For \(h>0\), let

\[
X_i(h):=T(h)e_i,
\qquad
1\le i\le2N,
\]

where \(e_i\) is the standard basis of \(\mathbb C^{2N}\).

The vectors \(X_i(h)\) form a basis of the ordinary tangent space for every \(h>0\). Directions with positive exponent \(e_i\) grow like \(h^{-e_i}\) in ordinary parameter coordinates. Rather than regarding this growth as a divergence, define an abstract rank-\(2N\) vector bundle over \([0,\varepsilon)\), denoted

\[
{}^{\mathrm{cl}}T,
\]

whose local frame is

\[
\mathsf X_1,\ldots,\mathsf X_{2N},
\]

and whose identification with the ordinary tangent bundle for \(h>0\) is

\[
\mathsf X_i\longmapsto X_i(h).
\]

We call this the **cluster-rescaled tangent bundle**.

Its dual coframe over \(h>0\) is

\[
\boxed{
\omega(h)
=
D(h)B(h)\,d\theta,
}
\]

where \(d\theta\) is the ordinary parameter coframe.

The coframe \(\omega(h)\) is adapted to the exponent filtration. It is not asserted here to be exact.

---

## 4. Exact desingularization of the realization differential

Define the renormalized Jacobian

\[
\mathcal J_{\mathrm{ren}}(h)
:=
J(h)T(h).
\]

Using the normal form,

\[
\mathcal J_{\mathrm{ren}}(h)
=
A(h)D(h)B(h)B(h)^{-1}D(h)^{-1}
=
A(h).
\]

Hence we have an exact identity.

### Theorem 4.1 - rescaled differential extension

The realization differential, viewed as a bundle map

\[
d\mathcal R_N:
{}^{\mathrm{cl}}T
\longrightarrow
\mathbb C^{2N},
\]

extends continuously, and analytically along the fixed-shape path, through \(h=0\). In the rescaled frame,

\[
\boxed{
[d\mathcal R_N]_{\mathsf X}
=
A(h),
}
\]

so at the collision face

\[
\boxed{
[d\mathcal R_N]_{h=0}
=
A_0,
}
\]

which is invertible.

Equivalently,

\[
\boxed{
d\mathcal R_N(X_i(h))=A(h)e_i.}
\]

### Proof

The exact normal form gives

\[
J(h)B(h)^{-1}D(h)^{-1}=A(h).
\]

By construction, the columns of \(B(h)^{-1}D(h)^{-1}\) are the rescaled frame vectors. Since \(A(h)\to A_0\) and \(A_0\) is invertible, the bundle map extends invertibly. \(\square\)

Thus the ordinary differential degenerates, but its lift to the cluster-rescaled tangent bundle does not.

---

## 5. Target-normalized form

Let

\[
R_0:=\mathcal R_N(X(0),u(0)).
\]

Apply the fixed invertible target transformation

\[
Y
:=
A_0^{-1}(\mathcal R_N-R_0).
\]

Then

\[
dY(X_i(h))
=
A_0^{-1}A(h)e_i.
\]

Therefore

\[
\boxed{
[dY]_{\mathsf X}
=
A_0^{-1}A(h)
\longrightarrow
I.
}
\]

In target-normalized coordinates, the lifted realization differential tends to the identity on the collision face.

This is the precise differential sense in which the collision is resolved.

---

## 6. Pullback metric and its ordinary degeneration

Equip moment space with its standard Hermitian metric. The ordinary pullback metric is

\[
G(h)=J(h)^*J(h).
\]

At \(h=0\),

\[
\operatorname{rank}G(0)
=
\operatorname{rank}J(0)
=
2N-2m+2.
\]

Hence the ordinary metric has a \((2m-2)\)-dimensional nullspace at the collision.

No bounded invertible source-coordinate change can produce a positive-definite limit, because congruence by an invertible matrix preserves rank.

The previously proved singular-value hierarchy gives the collapsing metric eigenvalue exponents

\[
\boxed{
2,4,\ldots,2m-2,
2m+2,2m+4,\ldots,4m-2.
}
\]

---

## 7. Exact extension of the renormalized metric

Measure the pullback metric in the rescaled frame. Define

\[
\widetilde G(h)
:=
T(h)^*G(h)T(h).
\]

Then

\[
\begin{aligned}
\widetilde G(h)
&=
D(h)^{-*}B(h)^{-*}
J(h)^*J(h)
B(h)^{-1}D(h)^{-1}\\
&=
A(h)^*A(h).
\end{aligned}
\]

### Theorem 7.1 - positive-definite metric extension

The anisotropically renormalized pullback metric extends through the collision face, with

\[
\boxed{
\widetilde G(h)=A(h)^*A(h)
}
\]

and

\[
\boxed{
\widetilde G(0)=A_0^*A_0>0.
}
\]

In particular, the collision metric is nondegenerate on the cluster-rescaled tangent bundle.

### Proof

The displayed identity is exact. Since \(A(h)\to A_0\) and \(A_0\) is invertible, \(A_0^*A_0\) is positive definite. \(\square\)

This determines the level at which the singularity disappears:

- it does not disappear in ordinary parameter coordinates;
- it does disappear for the realization differential on the rescaled tangent bundle;
- the ordinary pullback metric remains degenerate;
- the anisotropically renormalized pullback metric extends positively.

---

## 8. Finite pullback distance to the collision face

Let

\[
\theta(h)=(X(h),u(h))
\]

be the fixed-shape cluster path, and assume the coefficient functions are \(C^1\) through \(h=0\). Its pullback-metric length is

\[
L
=
\int_0^{h_0}
\sqrt{
\theta'(h)^*G(h)\theta'(h)
}
\,dh.
\]

Because \(G=J^*J\),

\[
\sqrt{
\theta'(h)^*G(h)\theta'(h)
}
=
\left\|
\frac d{dh}\mathcal R_N(\theta(h))
\right\|_2.
\]

The realization path is polynomial in the nodes and \(C^1\) in the coefficients, so its derivative is bounded near \(h=0\).

### Corollary 8.1 - finite-distance accessibility

Every such fixed-shape common-scale collision is reachable by a path of finite ordinary pullback length:

\[
\boxed{L<\infty.}
\]

Thus the collision face is not infinitely far away in the ordinary packet metric.

This does not yet characterize which boundary parameters are identified in the metric completion.

---

## 9. Relation to the singular-value constants

The rescaled metric limit

\[
A_0^*A_0
\]

is not generally diagonal in the exponent frame. The exact singular-value constants obtained from exterior powers arise from the interaction of

1. the limiting left geometry \(A_0\);
2. the limiting right geometry \(B_0\);
3. the exponent filtration in \(D(h)\).

The rescaled metric theorem packages the same information geometrically: \(A_0^*A_0\) is the finite metric on the blown-up tangent fiber, while \(B_0\) specifies how ordinary parameter directions approach that fiber.

---

## 10. What is proved and what remains open

### Proved here

- The ordinary collision Jacobian has corank \(2m-2\).
- The rank defect cannot be removed by ordinary smooth source or target coordinate changes.
- The cluster normal form defines a canonical rescaled tangent frame along each fixed-shape common-scale path.
- The lifted realization differential extends invertibly to the collision face.
- After a fixed target normalization, the lifted differential tends to the identity.
- The ordinary pullback metric cannot extend nondegenerately in ordinary coordinates.
- The anisotropically renormalized metric extends exactly to \(A_0^*A_0\).
- The collision face is reachable at finite ordinary pullback distance along the common-scale path.

### Still open

- Whether the rescaled coframe
  \[
  \omega(h)=D(h)B(h)d\theta
  \]
  integrates to an actual holonomic coordinate system.
- Construction of a full blow-up atlas allowing the cluster center, scale, shape, and coefficients to vary simultaneously.
- Compatibility of overlapping cluster charts and permutations.
- Identification of the metric-completion quotient on the collision face.
- Curvature of the extended rescaled metric.
- Several simultaneous clusters and nonuniform collision trees.
- Comparison with standard edge, weighted blow-up, Prony, and confluent-Vandermonde geometric frameworks before making novelty claims.

The next theorem target is the integrability problem: construct explicit confluent packet coordinates whose differential reproduces the rescaled coframe up to a bounded invertible transformation, or prove that only a nonholonomic rescaled tangent structure is canonical.