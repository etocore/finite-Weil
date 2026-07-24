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

The exact-constant proof is recorded in `paper/exact-two-node-collision-constants.md`.

## Immediate theorem queue

- [ ] Generalize the divided-difference construction to an \(m\)-node cluster.
- [ ] Determine the full hierarchy of cluster singular-value exponents.
- [ ] Test the candidate multiplicity-\(m\) exponent pattern against \(m=3\) symbolic and high-precision examples.
- [ ] Formulate a canonical unitary collision normal form.
- [ ] Express cluster constants through successive orthogonal projections of higher jets.
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

## Metric geometry

- [ ] Compute the block entries of \(G=J^*J\) explicitly.
- [ ] Derive translation and scaling laws for \(G\).
- [ ] Determine geodesic distance to the collision boundary.
- [ ] Study whether confluent boundary strata lie at finite or infinite metric distance.
- [ ] Analyze curvature in low-dimensional packet manifolds.

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
- singular perturbation of structured matrices.

The established ingredients should be cited as classical. New claims should be restricted to packet-specific formulations, geometric synthesis, or genuinely new quantitative results.