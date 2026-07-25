# Transition maps for ordered cluster blow-up charts

## Status

This note constructs the overlap maps between ordered blow-up charts for a common-scale `m`-node cluster. It proves that the coordinate changes are rational in the normalized shape variables, extend analytically to the collision face `h=0`, satisfy the cocycle identities, and preserve the aggregate boundary packet.

The remaining geometric problem is to identify the precise induced transformation law on the rescaled tangent filtration and its associated graded bundle.

---

## 1. Ordered reference-pair charts

Let the physical cluster nodes be

\[
 z_1,\ldots,z_m,
\]

with pairwise distinct values away from the collision face.

For every ordered pair of distinct labels

\[
(a,b),\qquad a\ne b,
\]

define the chart `\beta_{ab}` by

\[
 x^{ab}=z_a,
 \qquad
 h^{ab}=z_b-z_a,
\]

and normalized shape coordinates

\[
 \xi_j^{ab}
 =
 \frac{z_j-z_a}{z_b-z_a}.
\]

Thus

\[
 \xi_a^{ab}=0,
 \qquad
 \xi_b^{ab}=1,
\]

and

\[
 z_j=x^{ab}+h^{ab}\xi_j^{ab}.
\]

The independent shape coordinates are the `m-2` entries with

\[
 j\notin\{a,b\}.
\]

The cluster coefficients remain attached to the physical labels:

\[
 u_j^{ab}=u_j.
\]

Exterior nodes and coefficients are unchanged unless one also applies a relabeling permutation.

---

## 2. General overlap formula

Consider two ordered reference pairs

\[
(a,b)
\quad\text{and}\quad
(c,d),
\]

with `a\ne b` and `c\ne d`.

On their overlap, the second reference scale is nonzero:

\[
 z_d-z_c\ne0.
\]

In the `(a,b)` chart,

\[
 z_c=x^{ab}+h^{ab}\xi_c^{ab},
\]

and

\[
 z_d=x^{ab}+h^{ab}\xi_d^{ab}.
\]

Therefore

\[
 \boxed{
 x^{cd}
 =
 x^{ab}+h^{ab}\xi_c^{ab}
 }
\]

and

\[
 \boxed{
 h^{cd}
 =
 h^{ab}
 \bigl(
 \xi_d^{ab}-\xi_c^{ab}
 \bigr).
 }
\]

For every label `j`,

\[
 \xi_j^{cd}
 =
 \frac{z_j-z_c}{z_d-z_c}.
\]

Substitution gives

\[
 \boxed{
 \xi_j^{cd}
 =
 \frac{
 \xi_j^{ab}-\xi_c^{ab}
 }{
 \xi_d^{ab}-\xi_c^{ab}
 }.
 }
\]

This includes the identities

\[
 \xi_c^{cd}=0,
 \qquad
 \xi_d^{cd}=1.
\]

Hence the overlap map is

\[
 \boxed{
 \Phi_{ab}^{cd}:
 (x,h,\xi,u,\mathrm{ext})
 \longmapsto
 \left(
 x+h\xi_c,
 h(\xi_d-\xi_c),
 \left(
 \frac{\xi_j-\xi_c}{\xi_d-\xi_c}
 \right)_j,
 u,
 \mathrm{ext}
 \right).
 }
\]

The denominator is exactly the normalized separation of the new reference pair.

---

## 3. Analytic extension to the collision face

The shape transformation depends only on the normalized variables and not on `h`.

On the overlap domain

\[
 \xi_d^{ab}-\xi_c^{ab}\ne0,
\]

all transition formulas are rational and therefore holomorphic.

At the collision face `h^{ab}=0`, one has

\[
 x^{cd}=x^{ab},
 \qquad
 h^{cd}=0,
\]

while

\[
 \xi_j^{cd}
 =
 \frac{
 \xi_j^{ab}-\xi_c^{ab}
 }{
 \xi_d^{ab}-\xi_c^{ab}
 }
\]

remains well-defined.

Thus the transition extends analytically to `h=0`:

\[
 \boxed{
 \Phi_{ab}^{cd}|_{h=0}
 :
 (x,0,\xi,u,\mathrm{ext})
 \longmapsto
 \left(
 x,0,
 \frac{\xi-\xi_c}{\xi_d-\xi_c},
 u,
 \mathrm{ext}
 \right).
 }
\]

On a compact overlap satisfying

\[
 |\xi_d-\xi_c|\ge\delta>0,
\]

all derivatives of the transition and inverse transition are uniformly bounded.

---

## 4. Explicit inverse

The inverse overlap is obtained by swapping the reference pairs.

From the `(c,d)` shape variables,

\[
 \xi_j^{ab}
 =
 \frac{
 \xi_j^{cd}-\xi_a^{cd}
 }{
 \xi_b^{cd}-\xi_a^{cd}
 }.
\]

Similarly,

\[
 x^{ab}
 =
 x^{cd}+h^{cd}\xi_a^{cd},
\]

and

\[
 h^{ab}
 =
 h^{cd}
 \bigl(
 \xi_b^{cd}-\xi_a^{cd}
 \bigr).
\]

Therefore

\[
 \boxed{
 (\Phi_{ab}^{cd})^{-1}
 =
 \Phi_{cd}^{ab}.
 }
\]

Each overlap map is an analytic diffeomorphism between its chart domains, including their portions of the boundary face.

---

## 5. Cocycle identity

Take three ordered reference pairs

\[
(a,b),
\qquad
(c,d),
\qquad
(e,f).
\]

The normalized shape transformation is the affine renormalization

\[
 T_{cd}(t)
 =
 \frac{t-\xi_c^{ab}}{
 \xi_d^{ab}-\xi_c^{ab}
 }.
\]

In the `(c,d)` coordinates, changing to `(e,f)` applies

\[
 T_{ef}^{cd}(s)
 =
 \frac{s-\xi_e^{cd}}{
 \xi_f^{cd}-\xi_e^{cd}
 }.
\]

Direct substitution gives

\[
 T_{ef}^{cd}
 \circ
 T_{cd}^{ab}
 =
 T_{ef}^{ab}.
\]

Therefore

\[
 \boxed{
 \Phi_{cd}^{ef}
 \circ
 \Phi_{ab}^{cd}
 =
 \Phi_{ab}^{ef}.
 }
\]

The ordered charts satisfy the atlas cocycle condition exactly.

---

## 6. Transformation of node differences

For any labels `i,j`,

\[
 z_j-z_i
 =
 h^{ab}
 \bigl(
 \xi_j^{ab}-\xi_i^{ab}
 \bigr).
\]

Using the transition formulas,

\[
 h^{cd}
 \bigl(
 \xi_j^{cd}-\xi_i^{cd}
 \bigr)
 =
 h^{ab}
 \bigl(
 \xi_j^{ab}-\xi_i^{ab}
 \bigr).
\]

Thus the physical pairwise difference is chart-independent:

\[
 \boxed{
 h^{cd}
 (\xi_j^{cd}-\xi_i^{cd})
 =
 h^{ab}
 (\xi_j^{ab}-\xi_i^{ab}).
 }
\]

Consequently, the cluster discriminant transforms as

\[
 \Delta(\xi^{cd})
 =
 \frac{
 \Delta(\xi^{ab})
 }{
 (\xi_d^{ab}-\xi_c^{ab})^{\binom m2}
 },
\]

up to the sign induced by any reordering of labels.

Combining this with

\[
 h^{cd}
 =
 h^{ab}
 (\xi_d^{ab}-\xi_c^{ab}),
\]

gives the chart-invariant identity

\[
 \boxed{
 (h^{cd})^{\binom m2}
 \Delta(\xi^{cd})
 =
 (h^{ab})^{\binom m2}
 \Delta(\xi^{ab}),
 }
\]

again up to label-order sign.

The fourth power appearing in the packet Jacobian determinant removes that sign.

---

## 7. Boundary realization and metric quotient

Let

\[
 U=\sum_{j=1}^m u_j.
\]

At `h=0`, every ordered chart gives

\[
 \mathcal R_N
 =
 U M(x)
 +
 \sum_{\ell>m}
 u_\ell M(y_\ell).
\]

Under a chart transition,

\[
 x^{cd}=x^{ab}
\]

on the boundary, while the coefficients and exterior packet are unchanged. Therefore the aggregate boundary packet is invariant:

\[
 \boxed{
 (x,U,\mathrm{exterior})
 \text{ is independent of the ordered reference pair.}
 }
\]

The local equivalence relation used in the metric-completion quotient is therefore compatible with all ordered-chart overlaps.

This does not yet prove the global metric-completion theorem, because one must still control paths crossing several charts and interactions between distinct collision strata. It does remove the coordinate-choice ambiguity from the local quotient.

---

## 8. Boundary shape space

The ordered boundary shape chart records a labeled configuration on the affine line modulo translation and nonzero scaling.

Changing reference pairs acts by

\[
 t
 \longmapsto
 \frac{t-\xi_c}{\xi_d-\xi_c}.
\]

Thus the boundary shape space is covered by affine-normalization charts with rational transition functions.

For a fixed labeling, this is the configuration space

\[
 \operatorname{Conf}_m(\mathbb C)
 /
 \operatorname{Aff}(1,\mathbb C),
\]

represented locally by setting two selected points equal to `0` and `1`.

The permutation group acts by relabeling before applying the corresponding affine renormalization.

---

## 9. Interaction with the exponent filtration

Every ordered chart has the same exponent list

\[
 0,0,1,2,\ldots,m-1,
 m+1,\ldots,2m-1.
\]

Under a reference-pair transition,

\[
 h^{cd}=\lambda(\xi)h^{ab},
 \qquad
 \lambda(\xi)
 =
 \xi_d^{ab}-\xi_c^{ab}.
\]

Hence a scalar mode of weight `r` transforms at the level of its leading scale by

\[
 (h^{cd})^r
 =
 \lambda(\xi)^r
 (h^{ab})^r.
\]

This shows that the exponent filtration is chart-independent and that the associated graded line of weight `r` acquires the scalar transition factor

\[
 \lambda^r.
\]

However, the concrete regular factors `A` and `B` depend on the chosen Vandermonde and Hermite bases. Therefore the full rescaled tangent frame need not transform diagonally; it may mix modes of equal or lower filtration order through a bounded analytic matrix.

The precise theorem still to prove is:

> The transition matrix between two rescaled tangent frames extends analytically to `h=0`, preserves the exponent filtration, and induces multiplication by `\lambda^{-r}` on the weight-`r` associated graded tangent component, up to the fixed basis convention used for the jet modes.

This is the next calculation.

---

## 10. Main theorem

### Theorem 10.1 - ordered blow-up atlas

For every ordered pair of distinct cluster labels `(a,b)`, let `\beta_{ab}` be the chart defined by

\[
 x=z_a,
 \qquad
 h=z_b-z_a,
 \qquad
 \xi_j=\frac{z_j-z_a}{z_b-z_a}.
\]

Then on the overlap of `\beta_{ab}` and `\beta_{cd}`, the transition map is

\[
 x^{cd}
 =
 x^{ab}+h^{ab}\xi_c^{ab},
\]

\[
 h^{cd}
 =
 h^{ab}
 (\xi_d^{ab}-\xi_c^{ab}),
\]

\[
 \xi_j^{cd}
 =
 \frac{
 \xi_j^{ab}-\xi_c^{ab}
 }{
 \xi_d^{ab}-\xi_c^{ab}
 }.
\]

These transitions:

1. are rational and holomorphic on their overlap domains;
2. extend holomorphically to `h=0`;
3. have inverse `\Phi_{cd}^{ab}`;
4. satisfy the cocycle identity;
5. preserve all physical node differences;
6. preserve the aggregate boundary packet and the local metric-completion equivalence relation;
7. preserve the singular exponent filtration.

Therefore the ordered common-scale blow-up charts form an analytic atlas near the nondegenerate `m`-node collision face.

---

## 11. Proven versus open

### Proven here

- The general transition formula between arbitrary ordered reference pairs.
- Analytic extension to the collision face.
- Explicit inverse maps.
- Exact cocycle identities.
- Transformation laws for pairwise differences and the normalized discriminant.
- Chart invariance of the aggregate boundary packet.
- Compatibility of the local metric quotient with ordered-chart overlaps.
- Chart independence of the exponent filtration.

### Still open

- The full analytic transition law for the rescaled tangent frame `T=B^{-1}D^{-1}`.
- The induced representation on every associated graded component.
- A coordinate-free construction of the filtered/rescaled tangent bundle.
- The complete permutation-group action on the chosen Hermite and Vandermonde mode bases.
- Global metric completion across multiple and nested collision strata.
- Simultaneous-cluster and collision-tree atlases.
