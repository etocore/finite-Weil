# Packet conditioning research checklist

This checklist tracks the quantitative geometry of the finite exponential moment map

\[
\mathcal R_N(X,u)
=
\left(\sum_j u_jx_j^k\right)_{k=0}^{2N-1}.
\]

The companion note `paper/packet-conditioning.md` proves local identifiability, local Lipschitz stability, and blow-up of the absolute condition number near the singular boundary. The items below separate established facts from the next calculations.

## A. Exact Jacobian determinant

- [ ] Fix one coordinate ordering and sign convention.
- [ ] Factor \(u_j\) from each node-motion column.
- [ ] Reduce to the standard multiplicity-two confluent Vandermonde matrix.
- [ ] Prove the collision factor has exponent four for every pair.
- [ ] Determine the global sign for the chosen column ordering.
- [ ] Check the formula symbolically for \(N=1,2,3,4\).

Target formula, subject to sign:

\[
\det J(X,u)
=
\pm
\left(\prod_{j=1}^N u_j\right)
\left(\prod_{1\le i<j\le N}(x_j-x_i)^4\right).
\]

Do not promote this to a theorem until the ordering and sign are proved.

## B. Smallest-singular-value estimates

- [ ] Define
  \[
  \Delta=\min_{i\ne j}|x_i-x_j|,
  \quad
  R=\max_i|x_i|,
  \quad
  \nu=\min_i|u_i|.
  \]
- [ ] Bound \(\|J\|\) above in terms of \(N,R,\max_i|u_i|\).
- [ ] Use determinant and singular-value products to obtain a first non-sharp lower bound for \(\sigma_{\min}(J)\).
- [ ] Compare determinant-based bounds with direct inverse-Hermite bounds.
- [ ] Express rows of \(J^{-1}\) through fundamental Hermite polynomials.
- [ ] Estimate coefficients of those polynomials from node separation.

## C. Two-node collision asymptotics

- [ ] Set
  \[
  x_1=x-h/2,
  \qquad
  x_2=x+h/2.
  \]
- [ ] Replace \((u_1,u_2)\) by symmetric and antisymmetric coefficient coordinates.
- [ ] Expand the moment map in powers of \(h\).
- [ ] Identify the tangent direction that collapses fastest.
- [ ] Compute the leading order of \(\sigma_{\min}(J)\).
- [ ] Compare with the fourth-order determinant zero.
- [ ] Determine dependence on cancellations such as \(u_1+u_2=0\).

## D. Confluent coordinates

- [ ] Introduce collision-adapted coordinates that converge to coefficients of
  \[
  e^{xz},\qquad ze^{xz}.
  \]
- [ ] Rewrite the realization map in those coordinates.
- [ ] Show that the confluent Jacobian remains nonsingular at the collision point.
- [ ] Determine which part of ordinary condition-number blow-up is a coordinate singularity.
- [ ] Extend to clusters of multiplicity \(m\).

## E. Pullback geometry

- [ ] Compute the block form of
  \[
  G=J^*J.
  \]
- [ ] Derive explicit formulas for the coefficient-coefficient, coefficient-node, and node-node blocks.
- [ ] Check invariance under permutations.
- [ ] Study translations and scalings of nodes and derive transformation laws.
- [ ] Define normalized metrics that remove trivial scale dependence.
- [ ] Determine whether the metric completion naturally adds confluent packets.

## F. Optimization problems

- [ ] Choose a normalization, since unnormalized conditioning is coordinate dependent.
- [ ] For real nodes in a fixed interval, numerically minimize \(\kappa_{\mathrm{abs}}\).
- [ ] Compare equally spaced, Chebyshev, Fekete, and optimized nodes.
- [ ] Study equal coefficients before allowing coefficient optimization.
- [ ] Determine whether minimizers are unique modulo symmetry.
- [ ] Formulate only evidence-backed conjectures.

## G. Numerical experiments

- [ ] Implement stable Jacobian construction.
- [ ] Compute singular values with arbitrary precision near collisions.
- [ ] Plot \(\log\kappa\) against \(\log\Delta\) to estimate exponents.
- [ ] Test generic and cancellation-heavy coefficient choices separately.
- [ ] Compare ordinary coordinates with confluent coordinates.
- [ ] Store reproducible scripts and machine-readable results.

## H. Literature boundary

- [ ] Review classical confluent Vandermonde determinant formulas.
- [ ] Review Prony-map conditioning and super-resolution collision asymptotics.
- [ ] Review inverse Hermite interpolation estimates.
- [ ] Distinguish classical results from packet-specific reformulations.
- [ ] Identify which normalization and geometric questions are genuinely not standard.
