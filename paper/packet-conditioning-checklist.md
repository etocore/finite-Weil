# Packet-conditioning research checklist

This checklist tracks the transition from local identifiability to quantitative packet geometry for

\[
\mathcal R_N(X,u)
=
\left(\sum_{j=1}^N u_jx_j^k\right)_{k=0}^{2N-1}.
\]

## Completed

- [x] Prove Jacobian invertibility on the reduced packet space by Hermite interpolation.
- [x] Prove local holomorphic invertibility.
- [x] Prove local bi-Lipschitz stability.
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
  J(h)=A(h)D(h)B(h),
  \qquad
  D(h)=\operatorname{diag}(1,\ldots,1,h,h^3),
  \]
  with uniformly invertible regular factors.
- [x] Deduce
  \[
  \sigma_{2N-1}(J(h))\asymp|h|,
  \qquad
  \sigma_{2N}(J(h))\asymp|h|^3,
  \qquad
  \kappa_{\mathrm{abs}}(J(h))\asymp|h|^{-3}.
  \]
- [x] Derive the exact linear singular-value constant
  \[
  \lim_{h\to0}\frac{\sigma_{2N-1}(J(h))}{|h|}
  =
  \frac{\|P_0m''(x)\|}
  {\sqrt{|u_1|^{-2}+|u_2|^{-2}}}.
  \]
- [x] Derive the exact cubic singular-value constant
  \[
  \lim_{h\to0}\frac{\sigma_{2N}(J(h))}{|h|^3}
  =
  \frac1{12\sqrt2}
  \left\|
  P_{\mathcal L_0\cap(P_0m''(x))^\perp}m'''(x)
  \right\|.
  \]
- [x] Deduce the exact leading inverse-condition constant
  \[
  \lim_{h\to0}|h|^3\kappa_{\mathrm{abs}}(J(h))
  =
  \frac{12\sqrt2}
  {\left\|P_{\mathcal L_0\cap(P_0m''(x))^\perp}m'''(x)\right\|}.
  \]
- [x] Derive the exact leading coefficients of the two collapsing metric eigenvalues.
- [x] Generalize the collision construction to an arbitrary \(m\)-node cluster
  \[
  x_j=x+h\xi_j,
  \qquad
  \xi_i\ne\xi_j.
  \]
- [x] Prove the bounded-equivalence normal form with cluster exponents
  \[
  0,0,1,2,\ldots,m-1,m+1,\ldots,2m-1.
  \]
- [x] Prove that the collapsing singular-value exponents are
  \[
  1,2,\ldots,m-1,m+1,\ldots,2m-1.
  \]
- [x] Prove the general cluster condition-number law
  \[
  \kappa_{\mathrm{abs}}(J(h))\asymp|h|^{-(2m-1)}.
  \]
- [x] Verify compatibility with the determinant order
  \[
  \sum e_r=2m(m-1)=4\binom m2.
  \]
- [x] Specialize the theorem to the three-node hierarchy
  \[
  1,2,4,5.
  \]

The exact two-node constants are recorded in `paper/exact-two-node-collision-constants.md`.

The general cluster theorem is recorded in `paper/m-node-cluster-normal-form.md`.

## Immediate theorem queue

- [ ] Derive exact leading constants for the \(2m-2\) collapsing singular values of a general cluster.
- [ ] Express those constants through successive effective maps or orthogonal projections of the jets
  \[
  m''(x),m'''(x),\ldots,m^{(2m-1)}(x).
  \]
- [ ] Formulate a canonical unitary cluster normal form.
- [ ] Handle multiple clusters collapsing simultaneously at one common scale.
- [ ] Handle nonuniform cluster paths in which pairwise distances vanish at different powers of \(h\).
- [ ] Introduce confluent packet coordinates and test smooth or renormalized extension of the pullback metric.

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
- [ ] Separate the effects of coefficient loss and geometric collision.
- [ ] Determine whether useful scale-invariant relative condition numbers exist.
- [ ] Make cluster-shape dependence explicit through the offset Vandermonde
  \[
  \Delta(\xi)=\prod_{i<j}(\xi_j-\xi_i).
  \]

## Metric geometry

- [ ] Compute the block entries of \(G=J^*J\) explicitly.
- [ ] Derive translation and scaling laws for \(G\).
- [ ] Determine geodesic distance to the collision boundary.
- [ ] Study whether confluent boundary strata lie at finite or infinite metric distance.
- [ ] Analyze curvature in low-dimensional packet manifolds.
- [ ] Determine whether the anisotropically renormalized metric extends across multiplicity-\(2m\) confluent strata.

## Optimization

- [ ] Fix normalization constraints that remove translation and scale degeneracy.
- [ ] Numerically search for configurations minimizing \(\kappa_{\mathrm{abs}}\).
- [ ] Test equally spaced, symmetric, Fekete-type, and roots-of-unity configurations.
- [ ] Prove existence of minimizers under compact separation and diameter constraints.
- [ ] Determine whether symmetry is forced or merely favorable.

## Literature boundary

Before claiming novelty, review primary literature on:

- Prony maps and Prony varieties;
- confluent Vandermonde conditioning;
- exponential fitting and matrix-pencil methods;
- super-resolution near colliding nodes;
- finite-rate-of-innovation reconstruction;
- Hermite interpolation stability;
- singular perturbation of structured matrices;
- full singular spectra of clustered Vandermonde and confluent Vandermonde matrices.

The established ingredients should be cited as classical. New claims should be restricted to packet-specific formulations, geometric synthesis, or genuinely new quantitative results.