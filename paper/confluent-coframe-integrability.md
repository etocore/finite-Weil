# Integrability of the confluent coframe and the collision-face quotient

## Status

This note resolves the integrability question raised by the cluster-rescaled geometry of the finite exponential moment map

\[
\mathcal R_N(X,u)
=
\left(\sum_{j=1}^N u_jx_j^k\right)_{k=0}^{2N-1}.
\]

The answer has two distinct parts.

1. **Positive result.** The rescaled coframe is holonomic up to a bounded invertible change of coframe. In fact, target-normalized moment coordinates provide an exact coframe in its bounded `GL(2N)` class.
2. **Obstruction.** No such exact coframe can simultaneously be an ordinary boundary-resolving coordinate chart. Every bounded-gauge primitive has vanishing ordinary Jacobian determinant at the collision and necessarily collapses the internal collision face.

The pullback-metric completion therefore remembers the limiting aggregate confluent packet, not the full cluster shape and coefficient splitting.

---

## 1. Cluster normal form

Let an ordered cluster of size \(m\ge2\) approach a common center at scale \(h\):

\[
x_j=x+h\xi_j,
\qquad 1\le j\le m,
\]

where the offsets are pairwise distinct. The remaining nodes stay separated from the center, and all packet coefficients have nonzero limits.

On the punctured cluster chart, the previously proved normal form is

\[
\boxed{
J(h)=A(h)D(h)B(h),
}
\]

where \(A(h)\), \(B(h)\), and their inverses extend continuously, and analytically in the fixed-shape variables, to \(h=0\). The diagonal exponent matrix is

\[
D(h)=\operatorname{diag}(h^{e_1},\ldots,h^{e_{2N}}),
\]

with exponent list

\[
\underbrace{0,\ldots,0}_{2N-2m+2},
1,2,\ldots,m-1,
m+1,m+2,\ldots,2m-1.
\]

The sum of the positive exponents is

\[
\boxed{
E_m
:=
\sum_i e_i
=
2m(m-1).
}
\]

Let \(\theta\) denote the ordinary packet parameters in the ordering used for the factorization. Define the cluster-rescaled coframe

\[
\boxed{
\omega(h):=D(h)B(h)\,d\theta.
}
\]

Then

\[
d\mathcal R_N
=
J(h)d\theta
=
A(h)\omega(h).
\]

---

## 2. Bounded-gauge integrability

Fix the collision value

\[
R_0:=\mathcal R_N(\theta(0))
\]

and write

\[
A_0:=A(0).
\]

Define target-normalized moment functions

\[
\boxed{
Y(\theta)
:=
A_0^{-1}\bigl(\mathcal R_N(\theta)-R_0\bigr).
}
\]

These are honest functions on the punctured packet space and extend continuously, indeed polynomially in the node variables, to the collision.

### Theorem 2.1 - exact coframe in the bounded gauge class

The differential of \(Y\) satisfies

\[
\boxed{
dY=C(h)\omega(h),
\qquad
C(h):=A_0^{-1}A(h).
}
\]

Moreover,

\[
\boxed{
C(h)\longrightarrow I
}
\]

and both \(C(h)\) and \(C(h)^{-1}\) remain uniformly bounded near the collision.

### Proof

Using the normal form,

\[
\begin{aligned}
dY
&=A_0^{-1}d\mathcal R_N\\
&=A_0^{-1}J(h)d\theta\\
&=A_0^{-1}A(h)D(h)B(h)d\theta\\
&=C(h)\omega(h).
\end{aligned}
\]

Since \(A(h)\to A_0\) and \(A_0\) is invertible, \(C(h)\to I\), with uniformly bounded inverse. \(\square\)

### Consequence 2.2

The integrability problem

\[
d\eta=C\omega,
\qquad
C,C^{-1}=O(1),
\]

has an explicit solution:

\[
\boxed{
\eta=Y.
}
\]

Thus the rescaled coframe need not itself be closed. Its bounded `GL(2N)` equivalence class already contains the exact coframe \(dY\).

In the cluster-rescaled tangent category, \(Y\) is a holonomic coordinate system and

\[
[dY]_{\mathrm{cl}}
=
A_0^{-1}A(h)
\longrightarrow I.
\]

---

## 3. Why this does not produce an ordinary boundary chart

The preceding theorem solves integrability in the rescaled category. It does not make \(Y\) an ordinary local diffeomorphism at \(h=0\).

### Theorem 3.1 - determinant obstruction

Let \(\eta\) be any collection of \(2N\) functions satisfying

\[
d\eta=C(h)\omega(h)
\]

where \(C(h)\) and \(C(h)^{-1}\) remain bounded as \(h\to0\). Then, relative to ordinary packet coordinates,

\[
\boxed{
\det D_\theta\eta
=
\det C(h)\det B(h)\,h^{E_m}.
}
\]

Consequently,

\[
\boxed{
\det D_\theta\eta
=O\bigl(h^{2m(m-1)}\bigr)
\longrightarrow0.
}
\]

Therefore \(\eta\) cannot be an ordinary smooth coordinate chart with invertible boundary derivative.

### Proof

The coefficient matrix of \(d\eta\) relative to \(d\theta\) is

\[
C(h)D(h)B(h).
\]

Taking determinants gives

\[
\det D_\theta\eta
=
\det C(h)\det D(h)\det B(h).
\]

The regular factors have nonzero bounded limits, while

\[
\det D(h)
=
h^{\sum_i e_i}
=
h^{2m(m-1)}.
\]

This proves the claim. \(\square\)

### Interpretation

There is no contradiction between Theorems 2.1 and 3.1.

- The functions \(Y\) are coordinates for the **rescaled tangent geometry**.
- They are not coordinates that separate every point of the ordinary blown-up collision face.
- Any exact coframe boundedly equivalent to \(\omega\) must have the same determinant collapse.

Hence a boundary-resolving blow-up atlas must retain additional face variables, but those additional variables cannot enter an exact coframe boundedly equivalent to \(\omega\) without singular weights.

---

## 4. Explicit ordered blow-up chart

Locally choose two ordered cluster nodes to fix translation and scale:

\[
x_1=x,
\qquad
x_2=x+h,
\]

and write

\[
x_j=x+h\xi_j,
\qquad
3\le j\le m.
\]

The blow-up variables are

\[
\beta
=
\bigl(
 x,h,\xi_3,\ldots,\xi_m,
 u_1,\ldots,u_m,
 \text{exterior packet variables}
\bigr).
\]

Their number is

\[
1+1+(m-2)+m+2(N-m)=2N.
\]

The boundary face is \(h=0\). The ordinary realization map extends there, but its boundary restriction forgets most of the face variables.

Let

\[
U:=\sum_{j=1}^m u_j.
\]

At \(h=0\), the cluster contribution is

\[
\sum_{j=1}^m u_jM(x+h\xi_j)
\longrightarrow
U M(x).
\]

Therefore

\[
\boxed{
\mathcal R_N\big|_{h=0}
=
U M(x)
+
\sum_{\ell=m+1}^N u_\ell M(y_\ell).
}
\]

The boundary value is independent of

1. the normalized cluster shape \((\xi_3,\ldots,\xi_m)\);
2. the individual coefficient splitting \((u_1,\ldots,u_m)\) beyond the sum \(U\).

For fixed \(x\), exterior packet, and \(U\), the boundary fiber has dimension

\[
(m-2)+(m-1)=2m-3.
\]

The remaining missing direction in the ordinary corank \(2m-2\) is the normal scale direction \(h\).

---

## 5. Local metric-completion quotient

The ordinary pullback metric is

\[
G=J^*J.
\]

The length of a parameter path equals the Euclidean length of its realization image.

Consider two boundary configurations in the same ordered blow-up chart with

- the same center \(x\);
- the same exterior packet;
- the same aggregate coefficient \(U\);
- possibly different shape and internal coefficient splitting.

Assume they can be joined by a bounded \(C^1\) path

\[
s\longmapsto(\xi(s),u(s))
\]

through pairwise distinct normalized shapes, with

\[
\sum_{j=1}^m u_j(s)=U.
\]

For fixed \(h=\varepsilon>0\), define

\[
R_\varepsilon(s)
:=
\sum_{j=1}^m
u_j(s)M\bigl(x+\varepsilon\xi_j(s)\bigr)
+
R_{\mathrm{ext}}.
\]

Differentiating gives

\[
\frac{dR_\varepsilon}{ds}
=
\sum_j \dot u_j(s)
M\bigl(x+\varepsilon\xi_j(s)\bigr)
+
\varepsilon
\sum_j u_j(s)\dot\xi_j(s)
M'\bigl(x+\varepsilon\xi_j(s)\bigr).
\]

Since \(\sum_j\dot u_j=0\), the first sum can be rewritten as

\[
\sum_j \dot u_j(s)
\left[
M\bigl(x+\varepsilon\xi_j(s)\bigr)-M(x)
\right].
\]

On a bounded compact family of shapes and coefficients, both terms are uniformly \(O(\varepsilon)\). Hence

\[
\boxed{
\operatorname{Length}(R_\varepsilon)
=O(\varepsilon).
}
\]

The radial segments from \(h=0\) to \(h=\varepsilon\) also have length \(O(\varepsilon)\). Therefore the pullback distance between the two boundary configurations tends to zero.

### Theorem 5.1 - local completion collapse

Within a single compact ordered cluster chart, all boundary configurations with the same

\[
\boxed{
(x,U,\text{exterior packet})
}
\]

represent the same point of the ordinary pullback-metric completion.

Conversely, configurations with distinct limiting realization vectors remain separated by at least the Euclidean distance between those vectors, because every pullback path has length at least the distance between its image endpoints.

Thus the local metric-completion quotient of the collision face is precisely the limiting aggregate packet data, subject to any additional identifications already present in the realization map.

---

## 6. Final answer to the integrability question

The question must be divided into two meanings of “coordinates.”

### Rescaled or weighted coordinates

Yes. The target-normalized moments

\[
Y=A_0^{-1}(\mathcal R_N-R_0)
\]

satisfy

\[
\boxed{
dY=(A_0^{-1}A)\omega,}
\]

with bounded invertible gauge tending to the identity. The rescaled tangent structure is holonomic up to bounded gauge.

### Ordinary coordinates resolving the full collision face

No. Any primitive satisfying

\[
d\eta=C\omega,
\qquad
C,C^{-1}=O(1),
\]

has determinant vanishing like

\[
h^{2m(m-1)}.
\]

It cannot be an ordinary boundary chart. The exact weighted coordinates necessarily collapse the internal shape and coefficient-splitting directions.

The canonical geometry is therefore:

1. a full blow-up face retaining center, scale, shape, and coefficients;
2. a cluster-rescaled tangent bundle over that face;
3. exact target-moment coordinates on the rescaled tangent bundle;
4. a metric-completion quotient that forgets internal face data invisible to the limiting aggregate packet.

---

## 7. What remains open

The basic integrability question is resolved. The next tasks are more global:

- construct compatible ordered blow-up charts and permutation transition maps;
- extend the normal form smoothly with varying shape, rather than along one fixed-shape path;
- identify simultaneous and nested cluster faces;
- determine whether the rescaled tangent bundles form a natural Lie algebroid over the full compactification;
- compute the curvature and second fundamental data of the extended rescaled metric;
- compare the construction with weighted real blow-ups, edge tangent bundles, and compactified Prony spaces before making novelty claims.
