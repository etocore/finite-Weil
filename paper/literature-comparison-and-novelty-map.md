# Literature comparison and novelty map for finite packet collisions

## Purpose

This note records the first theorem-level comparison between the packet-conditioning program in this repository and nearby work on Prony maps, confluent Vandermonde systems, collision compactifications, and rescaled tangent geometries.

The goal is not to make a final novelty claim. The goal is to separate:

1. structures that are clearly classical or strongly anticipated;
2. structures that appear technically adjacent but not identical;
3. structures that remain plausible candidates for a new contribution.

The current conservative summary is:

> The collision compactification and confluent-coordinate philosophy are classical or closely anticipated. The strongest possible novelty lies in the packet-specific singular-value filtration, exact asymptotic constants, realization-induced rescaled tangent bundle, and extended pullback metric.

---

## 1. Classical Prony geometry

The finite exponential moment map considered here is

\[
\mathcal R_N(X,u)
=
\left(\sum_{j=1}^N u_jx_j^k\right)_{k=0}^{2N-1}.
\]

This is the classical square Prony map.

Batenkov and Yomdin study the global geometry and singularities of this map, emphasizing node collisions and the passage from ordinary spikes to confluent distributions involving derivatives of delta functions. Their work also develops finite-difference bases that remain meaningful as nodes collide.

### What should be regarded as known

- node collisions are a primary singularity of the Prony map;
- collided configurations are naturally represented by confluent distributions;
- finite differences provide stable coordinates or bases near collision;
- the Prony space has a bundle-like structure over node configurations;
- the Prony map is closely related to Vieta and Vandermonde maps.

### Relation to the present factorization

The repository normal form

\[
J=A D B
\]

should be viewed as refining this classical collision-resolution philosophy.

The analytic factor \(B\) is closely related in spirit to finite-difference or Hermite-adapted changes of basis. The new issue is not merely to find coordinates in which collided distributions remain finite, but to extract the exact anisotropic order of every tangent mode and then use that order to define

\[
T=B^{-1}D^{-1},
\qquad
JT=A.
\]

No novelty claim should be attached to confluent resolution alone.

---

## 2. Error amplification for near-colliding nodes

The near-collision Prony literature proves that reconstruction error grows polynomially in the inverse cluster scale and that the exponent depends on cluster multiplicity.

This is directly relevant to the result

\[
\|J(h)^{-1}\|\asymp h^{-(2m-1)}.
\]

### Conservative interpretation

The worst exponent \(2m-1\) may be anticipated by known local reconstruction bounds. It should not be presented in isolation as if collision amplification were unknown.

### Stronger repository result

The repository determines the complete common-scale singular hierarchy

\[
1,2,\ldots,m-1,m+1,\ldots,2m-1,
\]

including the absence of exponent \(m\), rather than only the deepest inverse-growth exponent.

It also derives exact asymptotic constants for individual collapsing singular values.

Thus the stronger novelty candidate is:

> the complete singular flag of the square value-and-node Jacobian, including exact constants and the missing exponent \(m\).

---

## 3. Ordinary clustered Vandermonde matrices

There is substantial literature on singular values of clustered rectangular Vandermonde and partial Fourier matrices.

Known themes include:

- approximate decoupling of separated clusters;
- estimates for all singular values;
- dependence on local cluster cardinality;
- dependence on normalized cluster shape;
- reduction of multi-cluster conditioning to local cluster blocks.

These results are close to the repository's separation of scale and shape.

### Decisive distinction

An ordinary Vandermonde block has columns of the form

\[
M(x_j).
\]

The packet Jacobian has paired value and derivative columns

\[
J=
\bigl[
M(x_1),u_1M'(x_1),\ldots,
M(x_N),u_NM'(x_N)
\bigr].
\]

It is therefore a weighted confluent Vandermonde-type matrix tied to the differential of the nonlinear Prony realization map.

The main unresolved literature question is:

> Has the coalescing singular spectrum of this exact value-plus-derivative block already been computed, with exponent multiset
> \[
> 0,\ldots,0,
> 1,2,\ldots,m-1,m+1,\ldots,2m-1?
> \]

This is the highest-priority duplication risk.

---

## 4. Confluent Prony conditioning

Existing work on confluent Prony systems studies multiplicities, local accuracy, inverse formulas, and confluent Vandermonde conditioning.

This literature may already contain close relatives of:

- the Jacobian determinant;
- Hermite interpolation inverses;
- coefficient-dependent local bounds;
- multiplicity-sensitive conditioning exponents.

What has not yet been located in the first pass is a theorem giving all of the following together:

1. the full individual singular-value hierarchy;
2. exact constants for every collapsing singular value;
3. rank-one limits of suitably rescaled inverse or exterior-power operators;
4. a rescaled tangent bundle;
5. an extended pullback metric.

The confluent-conditioning literature must be audited theorem by theorem before a final novelty statement is made.

---

## 5. Configuration-space compactifications

The ordered collision coordinates

\[
x_j=x+h\xi_j
\]

and the reference-pair transition formulas

\[
x^{cd}=x^{ab}+h^{ab}\xi_c^{ab},
\]

\[
h^{cd}=h^{ab}(\xi_d^{ab}-\xi_c^{ab}),
\]

\[
\xi_j^{cd}
=
\frac{\xi_j^{ab}-\xi_c^{ab}}
{\xi_d^{ab}-\xi_c^{ab}}
\]

are closely related to screen coordinates in Fulton-MacPherson, wonderful, and polydiagonal compactifications of configuration spaces.

### Structures that should be treated as classical

- blow-up of collision diagonals;
- center-scale-shape coordinates;
- nested collision strata;
- tree-indexed boundary faces;
- permutation-compatible compactification;
- analytic transition maps between normalized shape charts.

### Likely new layer

Those compactifications resolve the geometry of node locations. They do not automatically encode the degeneration of the Prony realization differential.

The repository adds a realization-induced filtration and metric over the collision geometry:

\[
J=A D B,
\qquad
T=B^{-1}D^{-1},
\qquad
\widetilde G=A^*A.
\]

The correct conceptual split is therefore:

1. classical compactification of node configurations;
2. packet-specific filtered tangent and metric structure induced by the realization map.

The project should not claim invention of collision blow-ups themselves.

---

## 6. Rescaled tangent structures

The packet-rescaled frame resembles constructions from \(b\)-geometry, edge geometry, weighted tangent bundles, and filtered tangent structures.

A standard \(b\)-frame near a boundary variable \(h\) contains

\[
h\partial_h,
\qquad
\partial_{y_1},\ldots,\partial_{y_n}.
\]

The packet frame instead carries a highly anisotropic exponent list

\[
1,2,\ldots,m-1,m+1,\ldots,2m-1
\]

and a nontrivial analytic gauge \(B^{-1}\).

### Current comparison question

The right question is not whether the construction is literally the ordinary \(b\)-tangent bundle. It is:

> Is the packet-rescaled tangent bundle analytically isomorphic, after bounded gauge, to a known weighted, edge, filtered, or iteratively modified tangent bundle on the collision compactification?

A proof of equivalence would identify the correct established geometric language. A proof of obstruction would support a stronger novelty claim.

---

## 7. Exact realization-metric volume

The exact determinant identity

\[
\det G
=
\left(\prod_j|u_j|^2\right)
\prod_{i<j}|x_j-x_i|^8
\]

implies, on a real parameter slice,

\[
d\operatorname{vol}_G
=
\left(\prod_j|u_j|\right)
\prod_{i<j}|x_j-x_i|^4\,d\theta.
\]

The determinant follows algebraically from the confluent Vandermonde determinant, so the raw formula may not be new in isolation.

The geometric interpretation is nevertheless useful:

- each simple collision hyperplane has fourth-order volume vanishing;
- an \(m\)-node common-scale collision has volume-density order
  \[
  4\binom m2=2m(m-1);
  \]
- the metric determinant has twice that exponent;
- the renormalized metric removes exactly this collapse.

A publication claim should emphasize the realization-metric interpretation rather than imply that the underlying determinant was unknown.

---

## 8. Provisional novelty ranking

### Strongest candidates

1. **Complete packet-Jacobian singular hierarchy**

   \[
   1,2,\ldots,m-1,m+1,\ldots,2m-1.
   \]

2. **Exact constants for all collapsing singular values**

   including exterior-power and projection formulas.

3. **Realization-induced rescaled tangent bundle**

   \[
   T=B^{-1}D^{-1}.
   \]

4. **Extended realization metric**

   \[
   \widetilde G=A^*A,
   \]

   with positive-definite boundary value.

5. **Analytic bundle and metric cocycles across ordered collision charts.**

6. **Exact realization-metric volume density.**

### Classical or strongly anticipated

- Prony-map collision singularities;
- confluent distributions;
- finite-difference collision bases;
- Hermite interpolation formulas;
- confluent Vandermonde determinants;
- multiplicity-dependent error amplification;
- cluster-shape dependence;
- collision-diagonal blow-ups;
- center-scale-shape charts;
- nested collision trees.

---

## 9. Recommended paper framing

Avoid the broad claim:

> We construct a new blow-up of the Prony collision space.

A more defensible formulation is:

> On an ordered collision compactification of finite node configurations, the Prony realization map induces a nonstandard filtered tangent geometry. We compute its complete common-scale exponent spectrum, exact singular constants, extended metric, and exact volume density.

This formulation acknowledges the classical configuration-space geometry while isolating the packet-specific content.

---

## 10. Next literature tasks

### Task A: theorem audit of Prony collision papers

Extract every result involving:

\[
h^{-(2m-1)},
\quad
\text{finite differences},
\quad
\det J,
\quad
\text{collision coordinates}.
\]

### Task B: confluent Vandermonde singular-spectrum search

Search specifically for:

- singular values of coalescing confluent Vandermonde matrices;
- Smith exponents of Hermite-Vandermonde matrix pencils;
- asymptotic singular spectra under node coalescence;
- value-and-derivative Vandermonde blocks.

### Task C: explicit compactification comparison

Construct an explicit identification between the repository's ordered charts and standard screen charts in a Fulton-MacPherson or wonderful compactification.

### Task D: tangent-module comparison

Write the local packet module as

\[
\mathcal V_{\mathrm{packet}}
=
B^{-1}
\operatorname{span}_{C^\omega}
\{h^{-e_i}\partial_i\}
\]

and compare it with known weighted or filtered tangent modules.

### Task E: nested collision trees

Use an established configuration compactification as the base and seek a tree-dependent normal form

\[
J_{\mathcal T}
=
A_{\mathcal T}
D_{\mathcal T}
B_{\mathcal T},
\]

where

\[
D_{\mathcal T}
=
\operatorname{diag}
\left(
\prod_{v\in\mathcal T}h_v^{e_{iv}}
\right).
\]

The exponent vectors attached to a collision tree would then be a new realization-induced invariant over a classical boundary stratification.

---

## 11. References for the first audit

The first comparison pass should include at least the following works:

- D. Batenkov and Y. Yomdin, *Geometry and Singularities of the Prony Mapping*.
- G. Goldman, Y. Salman, and Y. Yomdin, *Geometry and Singularities of Prony Varieties*.
- A. Akinshin, G. Goldman, and Y. Yomdin, work on error amplification for near-colliding Prony nodes.
- D. Batenkov and Y. Yomdin, work on accuracy for confluent Prony systems.
- D. Batenkov, A. Diederichs, G. Goldman, and Y. Yomdin, work on spectral properties of clustered Vandermonde matrices.
- S. Kunis and D. Nagel, work on singular values of clustered Vandermonde matrices and cluster geometry.
- W. Fulton and R. MacPherson, compactification of configuration spaces.
- A. Ulyanov, polydiagonal compactification of configuration spaces.
- L. Li, wonderful compactifications of arrangements of subvarieties.
- R. Melrose and related literature on \(b\)-, edge-, and rescaled tangent structures.

This list is a starting point, not a complete bibliography.
