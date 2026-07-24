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

## Main notes

- `paper/packet-conditioning.md`
- `paper/two-node-collision-normal-form.md`
- `paper/exact-two-node-collision-constants.md`
- `paper/m-node-cluster-normal-form.md`
- `paper/exact-m-node-deepest-constant.md`
- `paper/complete-cluster-constant-hierarchy.md`

## Immediate theorem queue

- [ ] Introduce confluent packet coordinates for an \(m\)-node collision stratum.
- [ ] Rewrite the realization map in confluent jet coordinates.
- [ ] Determine whether the realization Jacobian extends nonsingularly across the confluent stratum.
- [ ] Pull back the Euclidean moment metric in confluent coordinates.
- [ ] Determine the anisotropic renormalization required for metric extension.
- [ ] Determine whether collision strata lie at finite or infinite geodesic distance.
- [ ] Formulate a canonical unitary cluster normal form from the exterior filtration.
- [ ] Derive closed scalar cluster-polynomial formulas for the intermediate constants.
- [ ] Handle several clusters collapsing simultaneously.
- [ ] Handle nonuniform cluster paths with different pairwise powers of \(h\).

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
- [ ] Study metric completion near multiplicity-\(2m\) confluent strata.
- [ ] Analyze curvature in low-dimensional packet manifolds.

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
- analytic matrix pencils, Smith forms, and exterior-power singular asymptotics.

Classical ingredients should be cited as classical. New claims should be restricted to packet-specific formulations, geometric synthesis, or genuinely new quantitative results.