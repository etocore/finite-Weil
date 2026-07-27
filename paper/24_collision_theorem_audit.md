# Collision theorem audit before further finite-Weil work

## Purpose

This note freezes the current state of the collision project before any attempt to interpret the missing Smith grade inside the finite-Weil quadratic form.

The audit separates four logically distinct claims:

1. the generic Smith spectrum of the raw polynomial moment Jacobian;
2. the behavior under changes of collision source coordinates;
3. transfer from polynomial moments to Gaussian packet synthesis;
4. transfer from synthesis to the Gram/Weil matrix pipeline.

Only the first item is currently proved in general.

## 1. Confirmed theorem

For

\[
M_r=\sum_{j=1}^m u_jx_j^r,
\qquad
x_j=h\xi_j,
\qquad
0\le r<2m,
\]

and the Jacobian with respect to

\[
(u_1,\ldots,u_m,x_1,\ldots,x_m),
\]

the generic determinantal valuations are

\[
\nu_k=\frac{k(k-1)}2-\min(m,k-1).
\]

The generic Smith exponents are therefore

\[
0,0,1,\ldots,m-1,m+1,\ldots,2m-1.
\]

The proof consists of:

- an exact entry-grade formula;
- a two-case lower bound depending on whether row zero is selected;
- explicit confluent-Vandermonde witnesses for \(k\le m+1\);
- a real ordered Birkhoff-interpolation specialization for \(k>m+1\).

## 2. Corrected proof concern

The first version of the theorem incorrectly used

\[
p\le \min(m,k-1)
\]

for every nonzero minor. That restriction follows from the zero position row only when row zero is selected.

If row zero is omitted, a minor may contain \(k\) position columns when \(k\le m\). The theorem remains correct because omitting row zero raises the minimum row sum from

\[
0+\cdots +(k-1)
\]

to

\[
1+\cdots+k.
\]

The corrected proof now treats the two cases separately.

## 3. Meaning of “intrinsic”

The missing grade is intrinsic only after the source and target lattices are fixed.

The proved source lattice uses physical node variables \(x_j\). Passing to normalized shape variables through

\[
x_j=h\xi_j
\]

multiplies shape columns by \(h\). Multiplication by \(h\) is not a unit in \(\mathbb C\{h\}\), so it is not a Smith-preserving coordinate change.

Consequently, the following statements are different:

- the Smith spectrum of the map in \((u,x)\) coordinates;
- the Smith spectrum of the map in \((u,\xi)\) coordinates;
- the Smith spectrum after adjoining center and scale variables;
- the spectrum after quotienting translation or normalization directions.

No future note should call the spectrum coordinate-free without proving the relevant source transformations are analytic and unimodular.

## 4. Generic versus universal

The large witness argument proves that its determinant polynomial is not identically zero. Therefore the stated spectrum holds on a nonempty Zariski-open set.

It does not yet prove that every configuration with pairwise distinct complex nodes and nonzero weights has the same determinantal valuations.

Two different exceptional phenomena must be distinguished:

1. the chosen canonical witness may vanish while another minor still attains the generic valuation;
2. all minors at the generic valuation may vanish, causing an actual Smith jump.

The present work has not classified either locus.

A stronger universal theorem would require either:

- a witness family covering every distinct-node configuration;
- an explicit description of the determinantal ideal;
- or a proof that the generic initial minor ideal has no additional vanishing inside the distinct-node, nonzero-weight stratum.

## 5. Polynomial moments versus Gaussian synthesis

For \(m=3\), arbitrary-precision numerics show the same exponent list for Gaussian packet synthesis and the exact polynomial moment Jacobian.

That is strong evidence but not a general equivalence theorem.

To prove transfer for arbitrary \(m\), one needs an analytic jet map from the first \(2m\) moments into the Gaussian synthesis target whose leading \(2m\times2m\) block is a unit over the local ring. Informally, the Gaussian Taylor expansion suggests such a triangular map, but the following must be checked:

- the target topology and finite truncation;
- uniform control of the Taylor remainder;
- whether projection modulo exterior packet directions is unimodular;
- whether the chosen sampled or continuous synthesis target retains all first \(2m\) jets;
- whether amplitude conventions match the moment weights.

Until then, “Gaussian synthesis has the same general Smith spectrum” remains unproved beyond tested cases.

## 6. Raw synthesis versus the finite-Weil pipeline

The raw moment theorem does not automatically determine the Smith filtration of:

\[
B(h),\quad A(h),\quad (A(h),B(h)),\quad B(h)^{-1/2}A(h)B(h)^{-1/2},
\]

or the generalized eigenvalues.

Specific hazards are:

- the Gram map is quadratic in synthesis columns;
- whitening is singular as the Gram matrix degenerates;
- \(B^{-1/2}\) generally contains negative powers of \(h\) in collision-adapted coordinates;
- eigenvalue ordering is not analytic through multiplicities;
- truncating small Gram modes is not a unimodular operation;
- a quadratic form may annihilate or couple associated-graded directions even when synthesis does not.

Therefore the missing raw grade cannot yet be interpreted as a null, positive, or negative Weil direction.

## 7. Stale-document audit

Several earlier notes are historically useful but mathematically stale.

### Paper 13

The corrected Vandermonde-cubic determinant remains valid. Its claim that the missing grade must be caused by center, scale, or gauge normalization is superseded by the raw moment theorem.

### Paper 16

The obstruction to using the unweighted translation relation as a Smith row operation remains valid. Its ledger entry “universal local Smith spectrum open” is superseded.

### Paper 17

The exact \(m=3\) correction remains valid. Its “closed formula open” status is superseded.

### Paper 18

Its relative-spectrum conjecture and claim that exterior packets create the gap are false as statements about the raw collision Jacobian. The note should be marked superseded, not used as current evidence.

### Paper 19

Its precision correction remains useful. Its general Gaussian-equivalence language should be read as evidence from the tested realization, not as a theorem for arbitrary \(m\).

### Paper 20

The stagewise pipeline remains a useful diagnostic, but its opening motivation is superseded. It should now be used to test preservation or transformation of an already-present raw filtration.

## 8. Computational concerns

The exact exhaustive minor search is reliable for the reported small cases, but it scales combinatorially and is not the proof.

Required CI checks are:

- Ruff passes on all new files;
- unit tests pass;
- canonical small-witness formula agrees with direct exact determinants;
- ordered-real large witnesses remain nonzero across several sizes;
- the corrected lower-bound implementation agrees with the theorem formula;
- no test silently uses binary64 slope fitting as primary evidence.

At the time of this audit, the connector exposed no completed status checks for the latest theorem commit. Runtime CI confirmation remains outstanding.

## 9. Literature classification

The large-witness matrix is a univariate Hermite-Birkhoff interpolation matrix: selected nodes carry value conditions and all nodes carry first-derivative conditions. The proof by factoring

\[
p'=Qs
\]

and counting interval zeros is consistent with the classical poisedness viewpoint for Birkhoff interpolation.

This classification is useful for terminology and potential stronger results, but the present theorem is self-contained and does not depend on importing a general interpolation theorem.

## 10. Safe conclusion

The strongest justified statement is:

> For the raw moment map in physical source coordinates \((u,x)\), the generic collision germ has Smith exponents
> \[
> 0,0,1,\ldots,m-1,m+1,\ldots,2m-1.
> \]
> This result is exact and explains the missing grade before any exterior, Gram, Weil, whitening, or eigenvalue stage.

The following are not yet justified:

- coordinate-free intrinsicness;
- universality on the full distinct-node stratum;
- general analytic equivalence with Gaussian synthesis;
- preservation through the finite-Weil matrix construction;
- any implication for Weil positivity or the Riemann hypothesis.

## 11. Recommended next theorem

Before computing a “missing degree-\(m\) direction,” first define the exact source lattice used by the finite-Weil collision chart and compare it with the proved \((u,x)\) lattice.

The next theorem target should be a lattice-comparison statement:

\[
J_{\mathrm{physical}}(h)
\quad\longleftrightarrow\quad
J_{\mathrm{collision\ chart}}(h),
\]

with every source and target transformation explicitly classified as:

- analytic unimodular;
- non-unimodular but controlled;
- quotient/projection;
- or genuinely nonlinear/singular.

Only after that comparison is established will an associated-graded defect have an invariant meaning for the finite-Weil problem.
