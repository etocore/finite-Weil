# Theorem-level audit of Prony collision and Vandermonde literature

## Status

This note records a second, narrower literature pass for the finite packet-conditioning program.

The first comparison note separated broad areas of overlap. This note instead asks, theorem by theorem, which parts of the repository are already present in nearby work and which parts remain distinct.

The search was conducted through 2026-07-27 and focused on primary papers, journal versions, and recent reviews. It is not an exhaustive priority search and must not be used as the sole basis for a formal novelty claim.

The main conclusion is:

> The existence of an analytic diagonal factorization of a one-parameter singular matrix family belongs to classical local Smith-form theory. The packet contribution is therefore not the abstract existence of a factorization \(J=A D B\), but the explicit computation of its partial multiplicities, the packet-specific missing exponent, exact singular-value constants, realization-induced metric, and compatibility across collision charts.

This conclusion narrows the novelty claim but gives the project a much stronger mathematical placement.

---

## 1. Object being compared

For the square finite moment realization

\[
\mathcal R_N(X,u)
=
\left(
\sum_{j=1}^N u_jx_j^k
\right)_{k=0}^{2N-1},
\]

the ordinary Jacobian has paired value and node columns

\[
J
=
\bigl[
M(x_1),u_1M'(x_1),\ldots,
M(x_N),u_NM'(x_N)
\bigr].
\]

For a common-scale collision of \(m\) nodes, the repository proves an analytic factorization

\[
J(h)=A(h)D(h)B(h),
\]

where \(A(0)\) and \(B(0)\) are invertible and

\[
D(h)
=
\operatorname{diag}
\left(
1,\ldots,1,
 h,h^2,\ldots,h^{m-1},
 h^{m+1},\ldots,h^{2m-1}
\right).
\]

There are \(2N-2m+2\) unit entries. The nonzero exponent multiset is

\[
\boxed{
1,2,\ldots,m-1,m+1,\ldots,2m-1.
}
\]

The audit must distinguish five different levels of statement:

1. a Jacobian can be expressed using a confluent Vandermonde matrix;
2. collisions can be represented with finite differences or confluent distributions;
3. an analytic singular matrix family admits a local Smith form;
4. the packet Jacobian has the displayed explicit partial multiplicities;
5. the Euclidean singular values have exact asymptotic constants and define an extended realization metric.

The first three levels have substantial precedent. The fourth and fifth are the strongest repository-specific claims.

---

## 2. Batenkov and Yomdin: local accuracy for confluent Prony systems

### Source

D. Batenkov and Y. Yomdin, *On the Accuracy of Solving Confluent Prony Systems*, SIAM Journal on Applied Mathematics 73 (2013), arXiv:1106.1137.

### 2.1 Exact Jacobian factorization already present

Lemma 4.2 factors the Jacobian of a general confluent Prony map as

\[
J_{\mathcal P_S}(x)
=
U(\xi_1,l_1+1,\ldots,\xi_K,l_K+1)
\operatorname{diag}(D_1,\ldots,D_K),
\]

where \(U\) is a confluent Vandermonde matrix and the blocks \(D_i\) contain the amplitude parameters.

This is direct prior art for the statement that the Prony Jacobian is a confluent Vandermonde factor times a coefficient-dependent block matrix.

Therefore the repository should not claim novelty for:

- recognizing the Jacobian as confluent Vandermonde type;
- separating node dependence from amplitude dependence;
- obtaining the critical set from invertibility of those factors;
- writing the inverse Jacobian using the inverse confluent Vandermonde matrix.

### 2.2 Critical locus already identified

Corollary 4.3 states that the confluent Prony map is critical precisely when either:

1. two support nodes coincide; or
2. a highest-order confluent coefficient vanishes.

For the ordinary square Prony map this specializes to the familiar node-collision and zero-weight locus.

The repository's exact determinant formula is stronger in explicitness, but the qualitative critical-locus description is classical.

### 2.3 Inverse Jacobian already decomposed

Corollary 4.4 writes

\[
J_{\mathcal P_S}^{-1}
=
\operatorname{diag}(D_1^{-1},\ldots,D_K^{-1})
U^{-1}.
\]

This is close in spirit to the repository's use of Hermite interpolation and dual polynomials to describe \(J^{-1}\).

The distinction is that the repository follows a prescribed coalescing family and extracts exact powers of the scale \(h\), including rank-one limits after renormalization.

### 2.4 Local accuracy theorem does not compute the coalescence spectrum

Theorem 4.5 gives componentwise first-order accuracy bounds in terms of:

- the inverse confluent Vandermonde matrix;
- the node configuration;
- ratios involving the highest confluent coefficients.

It does not, as stated, compute the full singular-value spectrum of a family in which several ordinary nodes approach one another at a common scale.

In particular, this theorem does not display the packet exponent multiset

\[
1,2,\ldots,m-1,m+1,\ldots,2m-1,
\]

nor exact constants for each singular value.

### Audit result

| Claim | Status after this source |
|---|---|
| Prony Jacobian is confluent Vandermonde times coefficient blocks | Known |
| Collision and vanishing top coefficient define criticality | Known |
| Inverse Jacobian uses inverse confluent Vandermonde | Known |
| Full common-scale singular hierarchy for ordinary packets | Not found here |
| Missing exponent \(m\) | Not found here |
| Exact singular constants | Not found here |
| Rescaled tangent bundle and metric | Not found here |

---

## 3. Batenkov and Yomdin: geometry and singularities of the Prony map

### Source

D. Batenkov and Y. Yomdin, *Geometry and Singularities of the Prony Mapping*, Journal of Singularities 10 (2014), arXiv:1301.1336.

### 3.1 Prony space as a vector bundle is known

The paper defines a Prony space whose fiber over a possibly repeated node tuple is spanned by delta distributions and their derivatives. It also defines the corresponding Stieltjes space and proves that the Stieltjes transform gives a bundle isomorphism.

Therefore the idea that collision data should be enlarged from ordinary spikes to confluent distributions is classical in this setting.

### 3.2 Finite-difference collision bases are known

Section 6 develops global finite-difference bases and states explicitly that these bases resolve the linear part of collision singularities. In such coordinates, coefficients that blow up in the ordinary delta basis remain bounded as nodes collide.

This is a close precursor of the analytic basis factor \(B(h)\) in the repository.

A safe interpretation is:

> The finite-difference literature supplies collision-stable coordinates in the signal fiber. The repository refines that idea at the differential level by computing the precise vanishing order of each parameter-space tangent mode.

### 3.3 Multiplicity-restricted stability bounds are known

Theorem 4.4 proves local invertibility for a fixed multiplicity pattern and gives error bounds depending on node separation and confluent coefficients.

This confirms that separation-dependent instability and multiplicity-sensitive local inversion are established parts of Prony theory.

### 3.4 What remains distinct

The paper says its finite-difference bases resolve at least the linear part of the collision problem. It does not construct the repository's object

\[
T=B^{-1}D^{-1}
\]

as a rescaled tangent frame for the nonlinear realization differential, and it does not introduce

\[
\widetilde G=T^*J^*JT=A^*A
\]

as an extended pullback metric.

### Audit result

| Claim | Status after this source |
|---|---|
| Confluent collision space | Known |
| Bundle over node configurations | Known |
| Finite-difference basis stable at collision | Known |
| Exact tangent-mode exponent filtration | Not found here |
| Positive-definite boundary realization metric | Not found here |
| Ordered-chart metric cocycle | Not found here |

---

## 4. Spectral theory of clustered ordinary Vandermonde matrices

### Source

D. Batenkov, B. Diederichs, G. Goldman, and Y. Yomdin, *The Spectral Properties of Vandermonde Matrices with Clustered Nodes*, Linear Algebra and its Applications 609 (2021), arXiv:1909.01927.

### 4.1 All singular-value scales are known for an ordinary cluster

For an approximately uniform cluster of \(s\) ordinary Vandermonde columns, Theorem 2.3 gives

\[
\sigma_j(V_N(X))
\asymp
N^{1/2}(Nh)^{j-1},
\qquad
j=1,\ldots,s.
\]

Thus the ordinary clustered Vandermonde exponent list is consecutive:

\[
0,1,\ldots,s-1.
\]

This is the closest existing analogue to the repository's complete singular hierarchy.

### 4.2 Multi-cluster spectral decoupling is known

Theorem 2.2 compares the full singular spectrum of a multi-cluster Vandermonde matrix with the collection of singular spectra of its individual cluster submatrices. The error is controlled by cluster separation and cluster diameter.

This means a future packet theorem for simultaneous separated clusters should be framed as a confluent or value-plus-derivative extension of an established decoupling principle, not as the first occurrence of clusterwise spectral reduction.

### 4.3 Exact difference from the packet Jacobian

The ordinary matrix has one value column per node. The packet Jacobian has two coupled columns per node:

\[
M(x_j),
\qquad
u_jM'(x_j).
\]

For an \(m\)-node packet cluster, the repository obtains \(2m\) local modes, of which two remain noncollapsing and the remaining exponents are

\[
1,2,\ldots,m-1,m+1,\ldots,2m-1.
\]

The omission of \(m\) does not follow from the ordinary Vandermonde theorem.

### Audit result

| Claim | Status after this source |
|---|---|
| All singular-value orders for ordinary clustered Vandermonde matrices | Known |
| Consecutive ordinary exponent list \(0,\ldots,s-1\) | Known |
| Multi-cluster spectral decoupling | Known |
| Value-plus-derivative packet exponent list | Not covered |
| Missing exponent \(m\) | Not covered |
| Exact constants for packet singular values | Not covered |

---

## 5. Cluster-shape dependence of the smallest singular value

### Source

S. Kunis and D. Nagel, *On the Smallest Singular Value of Multivariate Vandermonde Matrices with Clustered Nodes*, Linear Algebra and its Applications 604 (2020), arXiv:1907.07119.

This work proves that the smallest singular value depends on products of intracluster distances and, for larger clusters, on the geometric configuration within the cluster.

Therefore normalized shape dependence is not itself new.

The repository should frame its shape quantities as exact packet-specific realizations of a broader known principle:

\[
\text{singular scale}
=
\text{power of cluster diameter}
\times
\text{normalized-shape constant}.
\]

The possible new content is the exact formula for the packet shape constant, its relation to Hermite-dual modes, and the constants for the entire singular hierarchy rather than only the smallest singular value.

---

## 6. Confluent Vandermonde inversion and condition-number literature

### Sources

- W. Gautschi, *On Inverses of Vandermonde and Confluent Vandermonde Matrices*, Numerische Mathematik 4 (1962).
- R.-C. Li, *Lower Bounds for the Condition Number of a Real Confluent Vandermonde Matrix*, Mathematics of Computation 75 (2006).
- J. S. Respondek, *History of Confluent Vandermonde Matrices and Inverting Them Algorithms*, arXiv:2407.15696.

This literature contains explicit inverses, interpolation formulas, numerical algorithms, and global or dimension-dependent condition-number bounds.

It substantially reduces the novelty available for:

- explicit inversion of confluent Vandermonde matrices;
- Hermite interpolation formulas in isolation;
- general statements that confluent Vandermonde matrices can be badly conditioned.

The review literature located in this pass is oriented toward inversion algorithms and historical formulas. It does not advertise a theorem computing the complete coalescence singular spectrum of the exact square value-plus-derivative Prony Jacobian.

That negative finding is provisional, not exhaustive.

---

## 7. Local Smith form of analytic matrix functions

### Sources

- I. Gohberg, M. A. Kaashoek, and F. van Schagen, *On the Local Theory of Regular Analytic Matrix Functions*, Linear Algebra and its Applications 182 (1993), 9-25.
- J. Wilkening and J. Yu, *A Local Construction of the Smith Normal Form of a Matrix Polynomial*, Journal of Symbolic Computation 46 (2011), arXiv:0809.2978.
- M. Franchi and P. Paruolo, *Inversion of Regular Analytic Matrix Functions: Local Smith Form and Subspace Duality*, Linear Algebra and its Applications 435 (2011), 2896-2912.

### 7.1 Abstract existence of \(A D B\) is classical

For a regular one-parameter analytic matrix function \(M(h)\), local Smith-form theory gives analytic invertible factors and a diagonal power matrix

\[
M(h)
=
E(h)
\operatorname{diag}
\left(
 h^{\alpha_1},\ldots,h^{\alpha_n}
\right)
F(h),
\]

where the nonnegative integers \(\alpha_i\) are the local partial multiplicities.

Consequently, the abstract statement

\[
\text{analytic singular family}
=
\text{invertible analytic factor}
\times
\text{diagonal powers}
\times
\text{invertible analytic factor}
\]

is not new.

The repository's factorization should now be identified explicitly as a computed local Smith form, or as a local Smith form up to the convention used for left and right factors.

### 7.2 What the packet proof adds

Local Smith theory does not automatically tell us the partial multiplicities for a concrete matrix family. The packet calculation gives them explicitly:

\[
\boxed{
0^{\times(2N-2m+2)},
1,2,\ldots,m-1,m+1,\ldots,2m-1.
}
\]

This has several consequences.

1. The missing exponent \(m\) is a local analytic-equivalence invariant.
2. The determinant order is the sum of the partial multiplicities:
   \[
   2m(m-1).
   \]
3. The pole order of the inverse is the largest partial multiplicity:
   \[
   2m-1.
   \]
4. The dimensions of the order filtration are invariant under analytic changes of source and target frame.

These are the correct invariant statements behind the packet exponent filtration.

### 7.3 Singular exponents versus exact singular constants

If

\[
J=A D B
\]

with \(A,B\) and their inverses uniformly bounded near \(h=0\), then the Euclidean singular values have the same power exponents as the diagonal entries of \(D\).

However, the exact leading singular constants are not determined by the local Smith form alone. They depend on the limiting Euclidean geometry of the left and right factors.

This makes the exact constants a stronger metric result than the partial-multiplicity calculation.

### 7.4 Consequence for novelty language

Avoid:

> We discover that the singular Jacobian can be diagonalized into powers of the collision scale.

Prefer:

> We compute the local Smith partial multiplicities of the packet realization Jacobian and then refine this analytic-equivalence classification to exact Euclidean singular-value asymptotics and an extended realization metric.

---

## 8. Recent geometry of the Vandermonde map

### Source

J. Acevedo, G. Blekherman, S. Debus, and C. Riener, *The Wonderful Geometry of the Vandermonde Map*, Foundations of Computational Mathematics, published online 2025, arXiv:2303.09512.

The paper studies images of nonnegative orthants and probability simplices under power-sum maps, including weighted variants. Its principal geometry concerns Vandermonde cells, their boundaries, cyclic-polytope combinatorics, limits in the number of variables, and applications to positivity and undecidability.

It is relevant because it confirms that weighted power-sum maps remain an active geometric subject and that the term "Vandermonde geometry" already has a current literature.

It does not study the same local object as the repository:

- its variables are node coordinates with fixed positive weights or simplex weights;
- its focus is the image and boundary of the power-sum map;
- it does not analyze a square value-and-node Prony Jacobian at a coalescing packet;
- it does not construct the packet-rescaled tangent metric.

The paper should be cited for broader Vandermonde-map geometry, but it is not currently a direct duplication risk for the local singular-spectrum theorem.

---

## 9. Claim-by-claim status matrix

| Repository statement | Current literature status |
|---|---|
| The moment map is the classical square Prony map | Classical |
| The Jacobian is confluent Vandermonde type | Classical |
| The critical locus is collision plus zero weight | Classical in qualitative form; exact determinant formula standard or close to standard |
| Finite differences stabilize collision coordinates | Classical Prony collision method |
| Confluent distributions represent collided packets | Classical |
| An analytic \(A D B\) form exists for a one-parameter regular matrix family | Classical local Smith-form theory |
| The packet partial multiplicities are \(0,\ldots,0,1,\ldots,m-1,m+1,\ldots,2m-1\) | Not located in prior work |
| Exponent \(m\) is absent | Not located in prior work |
| All packet singular values have these exact exponents | Not located in prior work |
| Exact leading constant for the deepest singular value | Not located in prior work |
| Exact leading constants for every collapsing singular value | Not located in prior work |
| Ordinary clustered Vandermonde singular values scale consecutively | Known |
| Cluster-shape dependence | Known in broader Vandermonde theory |
| Multi-cluster decoupling for ordinary Vandermonde matrices | Known |
| Packet-rescaled tangent bundle induced by \(J\) | Not located in prior work |
| Extended metric \(\widetilde G=A^*A\) | Not located in prior work |
| Exact realization-volume density | Determinant algebra likely classical; geometric packaging not located |
| Ordered collision chart transitions | Classical in configuration compactification form |
| Packet frame and metric cocycles on those charts | Not located in prior work |

"Not located" means only that this audit did not find the statement. It does not mean the statement has never appeared.

---

## 10. Revised mathematical positioning

The project now has three layers.

### Layer I: classical collision and interpolation structure

- Prony map;
- confluent Vandermonde matrices;
- Hermite interpolation;
- finite-difference collision bases;
- collision critical locus;
- configuration-space blow-ups.

### Layer II: classical analytic classification, explicitly computed here

- local Smith form of the one-parameter Jacobian family;
- partial multiplicities;
- inverse pole order;
- invariant exponent filtration.

The theory of local Smith forms is classical. The explicit packet partial multiplicities are the packet-specific calculation.

### Layer III: metric refinement

- exact singular-value constants;
- exterior-power limits;
- rescaled tangent frame tied to the realization map;
- positive-definite boundary metric;
- exact pullback-volume density;
- metric-compatible chart cocycles.

This third layer currently appears furthest from the located literature.

---

## 11. Immediate theorem to add to the repository

The next note should promote the normal form to the established language of local analytic matrix theory.

### Proposed theorem

Let \(J(h)\) be the packet realization Jacobian along an \(m\)-node common-scale collision, with nonzero limiting weights and nondegenerate normalized shape. Then \(J\) has local Smith partial multiplicities

\[
0^{\times(2N-2m+2)},
1,2,\ldots,m-1,m+1,\ldots,2m-1.
\]

Consequently:

\[
\operatorname{ord}_{h=0}\det J
=
2m(m-1),
\]

\[
\operatorname{poleord}_{h=0}J^{-1}
=
2m-1,
\]

and the missing exponent \(m\) is invariant under analytic source and target frame changes.

The proof is immediate from the already established analytic factorization \(J=A D B\), but the theorem is conceptually important because it states precisely which part of the normal form belongs to classical classification and which part has been computed for packets.

---

## 12. Next research targets

### A. Search specifically for packet partial multiplicities

Queries should combine:

- Prony Jacobian;
- confluent Vandermonde;
- local Smith form;
- partial multiplicities;
- coalescing nodes;
- value and derivative columns.

### B. Audit exact asymptotic constants

Search for papers using:

- exterior powers of clustered Vandermonde matrices;
- wedge-product singular asymptotics;
- rank-one limits of rescaled inverses;
- asymptotic SVD of analytic matrix functions.

### C. Relate the exponent filtration to root functions

Local Smith theory describes partial multiplicities using canonical systems of root functions or Jordan chains. The repository's Hermite-dual tangent modes should be compared explicitly with those root functions.

A successful identification would turn the packet tangent filtration into a concrete canonical root-function filtration.

### D. Extend ordinary multi-cluster decoupling

The correct next spectral theorem is not merely "two clusters factor." It is:

> separated packet clusters have a spectrum asymptotic to the union of the spectra of their local value-plus-derivative cluster blocks, with an explicit interaction error.

This would directly extend the known ordinary Vandermonde decoupling theorem.

### E. Compare exact metric constants under local Smith gauges

The exponents are analytic-equivalence invariants. The constants depend on the Hermitian structures and limiting gauges. The repository should state clearly which constants are coordinate invariant, frame covariant, or normalization dependent.

---

## 13. References

1. D. Batenkov and Y. Yomdin, *On the Accuracy of Solving Confluent Prony Systems*, SIAM Journal on Applied Mathematics 73 (2013), arXiv:1106.1137.
2. D. Batenkov and Y. Yomdin, *Geometry and Singularities of the Prony Mapping*, Journal of Singularities 10 (2014), arXiv:1301.1336.
3. D. Batenkov, B. Diederichs, G. Goldman, and Y. Yomdin, *The Spectral Properties of Vandermonde Matrices with Clustered Nodes*, Linear Algebra and its Applications 609 (2021), arXiv:1909.01927.
4. S. Kunis and D. Nagel, *On the Smallest Singular Value of Multivariate Vandermonde Matrices with Clustered Nodes*, Linear Algebra and its Applications 604 (2020), arXiv:1907.07119.
5. W. Gautschi, *On Inverses of Vandermonde and Confluent Vandermonde Matrices*, Numerische Mathematik 4 (1962), 117-123.
6. R.-C. Li, *Lower Bounds for the Condition Number of a Real Confluent Vandermonde Matrix*, Mathematics of Computation 75 (2006), 1987-1995.
7. J. S. Respondek, *History of Confluent Vandermonde Matrices and Inverting Them Algorithms*, arXiv:2407.15696.
8. I. Gohberg, M. A. Kaashoek, and F. van Schagen, *On the Local Theory of Regular Analytic Matrix Functions*, Linear Algebra and its Applications 182 (1993), 9-25.
9. J. Wilkening and J. Yu, *A Local Construction of the Smith Normal Form of a Matrix Polynomial*, Journal of Symbolic Computation 46 (2011), 1-22, arXiv:0809.2978.
10. M. Franchi and P. Paruolo, *Inversion of Regular Analytic Matrix Functions: Local Smith Form and Subspace Duality*, Linear Algebra and its Applications 435 (2011), 2896-2912.
11. J. Acevedo, G. Blekherman, S. Debus, and C. Riener, *The Wonderful Geometry of the Vandermonde Map*, Foundations of Computational Mathematics (2025), arXiv:2303.09512.
