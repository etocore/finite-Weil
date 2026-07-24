# Packet-conditioning research checklist

This checklist tracks the transition from local identifiability to quantitative packet geometry for

\[
\mathcal R_N(X,u)
=
\left(\sum_{j=1}^N u_jx_j^k\right)_{k=0}^{2N-1}.
\]

## Completed

- [x] Prove Jacobian invertibility on the reduced packet space by Hermite interpolation.
- [x] Prove local holomorphic invertibility and local bi-Lipschitz stability.
- [x] Define the absolute packet condition number
  \[
  \kappa_{\mathrm{abs}}=\|J^{-1}\|.
  \]
- [x] Define the pullback metric
  \[
  G=J^*J.
  \]
- [x] Identify the exact singular locus as node collisions or vanishing coefficients.
- [x] Prove condition-number blow-up along convergent sequences approaching the singular locus.
- [x] Prove the exact determinant formula
  \[
  \det J
  =
  (-1)^{N(N-1)/2}
  \left(\prod_j u_j\right)
  \left(\prod_{i<j}(x_j-x_i)^4\right)
  \]
  in grouped coordinates, with positive sign in interleaved coordinates.
- [x] Prove the two-node collision normal form
  \[
  J(h)=A(h)\operatorname{diag}(1,\ldots,1,h,h^3)B(h)
  \]
  with uniformly invertible regular factors.
- [x] Derive the exact two-node constants for the linear and cubic singular scales.
- [x] Derive the exact leading constant of \(h^3\kappa_{\mathrm{abs}}\).
- [x] Generalize the collision construction to an arbitrary common-scale \(m\)-node cluster
  \[
  x_j=x+h\xi_j,
  \qquad
  \xi_i\ne\xi_j.
  \]
- [x] Prove the bounded-equivalence exponent hierarchy
  \[
  0,0,1,2,\ldots,m-1,m+1,\ldots,2m-1.
  \]
- [x] Prove that the collapsing singular-value exponents are
  \[
  1,2,\ldots,m-1,m+1,\ldots,2m-1.
  \]
- [x] Prove the general condition-number law
  \[
  \kappa_{\mathrm{abs}}(J(h))\asymp|h|^{-(2m-1)}.
  \]
- [x] Verify compatibility with the determinant order
  \[
  \sum e_r=2m(m-1)=4\binom m2.
  \]
- [x] Derive the exact deepest singular-value constant from the rank-one inverse limit
  \[
  h^{2m-1}J(h)^{-1}
  \longrightarrow
  r_\xi(\operatorname{coeff}P)^{\mathsf T}.
  \]
- [x] Separate the deepest constant into a cluster-shape factor and a projected highest-jet factor.
- [x] Prove the exterior-power filtration theorem for an analytic diagonal normal form.
- [x] Derive exact cumulative constants for every product of the smallest cluster singular values.
- [x] Derive exact leading constants for all \(2m-2\) collapsing singular values.
- [x] Express every constant as a successive orthogonal-projection ratio
  \[
  c_k
  =
  \frac1{\|\widehat r_k\|\,\|\widehat\ell_k\|}.
  \]
- [x] Express every constant as a ratio of principal Gram minors.
- [x] Compute the complete symmetric three-node spectrum
  \[
  \sigma_3\sim2\sqrt2\,h,
  \qquad
  \sigma_4\sim\sqrt6\,h^2,
  \qquad
  \sigma_5\sim\sqrt{\frac23}\,h^4,
  \qquad
  \sigma_6\sim\frac{2\sqrt2}{3}h^5.
  \]
- [x] Prove that the ordinary collision Jacobian has corank \(2m-2\).
- [x] Prove that no ordinary smooth source or target coordinate change can remove the collision rank defect.
- [x] Define the cluster-rescaled tangent frame
  \[
  T(h)=B(h)^{-1}D(h)^{-1}.
  \]
- [x] Prove the exact rescaled differential identity
  \[
  J(h)T(h)=A(h),
  \]
  so the lifted realization differential extends invertibly to the collision face.
- [x] Prove that the ordinary pullback metric cannot extend nondegenerately in ordinary coordinates.
- [x] Prove the exact renormalized metric identity
  \[
  T(h)^*G(h)T(h)=A(h)^*A(h)
  \]
  and the positive-definite boundary value
  \[
  \widetilde G(0)=A_0^*A_0.
  \]
- [x] Prove that fixed-shape common-scale collision paths reach the boundary in finite ordinary pullback length.
- [x] Solve the bounded-gauge integrability problem for
  \[
  \omega=D(h)B(h)d\theta
  \]
  by the exact target-normalized moment coframe
  \[
  dY=(A_0^{-1}A(h))\omega.
  \]
- [x] Prove that every primitive boundedly equivalent to \(\omega\) has ordinary Jacobian determinant vanishing like
  \[
  h^{2m(m-1)},
  \]
  so no such primitive can be an ordinary boundary-resolving chart.
- [x] Construct an explicit ordered local blow-up chart with center, scale, normalized shape, coefficients, and exterior packet variables.
- [x] Identify the boundary restriction of the realization map as the aggregate packet
  \[
  U M(x)+\sum_{\ell>m}u_\ell M(y_\ell),
  \qquad
  U=\sum_{j=1}^m u_j.
  \]
- [x] Prove the local metric-completion collapse: within one compact ordered chart, boundary configurations with the same center, aggregate coefficient, and exterior packet have zero pullback distance.

## Main notes

- `paper/packet-conditioning.md`
- `paper/two-node-collision-normal-form.md`
- `paper/exact-two-node-collision-constants.md`
- `paper/m-node-cluster-normal-form.md`
- `paper/exact-m-node-deepest-constant.md`
- `paper/complete-cluster-constant-hierarchy.md`
- `paper/confluent-rescaled-geometry.md`
- `paper/confluent-coframe-integrability.md`

## Immediate theorem queue

- [ ] Extend the cluster normal form smoothly over a full ordered blow-up chart with varying center, scale, shape, and coefficients.
- [ ] Construct transition functions between overlapping ordered cluster charts.
- [ ] Determine the permutation-group action on the blow-up and rescaled tangent structures.
- [ ] Globalize the local metric-completion quotient across overlapping charts.
- [ ] Determine whether the rescaled tangent bundles define a natural Lie algebroid over the full collision compactification.
- [ ] Construct simultaneous-cluster and nested-cluster charts.
- [ ] Handle nonuniform collision paths with different pairwise powers of \(h\).
- [ ] Compute curvature of the extended rescaled metric in low-dimensional cases.
- [ ] Formulate a canonical unitary cluster normal form from the exterior filtration.
- [ ] Derive closed scalar cluster-polynomial formulas for the intermediate constants.

## Quantitative global bounds

- [ ] Bound \(\sigma_{\min}(J)\) below using
  \[
  \Delta(X)=\min_{i\ne j}|x_i-x_j|,
  \qquad
  u_{\min}=\min_i|u_i|,
  \qquad
  R=\max_i|x_i|.
  \]
- [ ] Compare determinant-based bounds with inverse-Hermite-interpolation bounds.
- [ ] Separate coefficient loss from geometric collision.
- [ ] Make cluster-shape dependence explicit through
  \[
  \Delta(\xi)=\prod_{i<j}(\xi_j-\xi_i).
  \]
- [ ] Determine useful scale-invariant relative condition numbers.

## Metric geometry

- [ ] Compute the block entries of \(G=J^*J\) explicitly.
- [ ] Derive translation and scaling laws for \(G\).
- [ ] Globalize the metric completion near multiplicity-\(2m\) confluent strata.
- [ ] Analyze curvature in low-dimensional packet manifolds.
- [ ] Compare ordinary, rescaled, and quotient metrics on the collision face.

## Optimization

- [ ] Fix normalization constraints removing translation and scale degeneracy.
- [ ] Numerically search for configurations minimizing \(\kappa_{\mathrm{abs}}\).
- [ ] Compare equally spaced, symmetric, Fekete-type, and roots-of-unity configurations.
- [ ] Prove existence of minimizers under compact separation and diameter constraints.

## Literature boundary

Before claiming novelty, review primary literature on:

- Prony maps and Prony varieties;
- confluent Vandermonde conditioning;
- exponential fitting and matrix-pencil methods;
- super-resolution near colliding nodes;
- finite-rate-of-innovation reconstruction;
- Hermite interpolation stability;
- singular perturbation of structured matrices;
- singular spectra of clustered Vandermonde and confluent Vandermonde matrices;
- analytic matrix pencils, Smith forms, and exterior-power singular asymptotics;
- weighted blow-ups, edge geometry, rescaled tangent bundles, and Lie algebroids.

Classical ingredients should be cited as classical. New claims should be restricted to packet-specific formulations, geometric synthesis, or genuinely new quantitative results.
