# Verification checklist for packet-transform realization theory

This checklist is meant to prevent the realization chapter from overstating what is new or what follows automatically.

## Established theorem package

- [x] Distinct exponential modes are linearly independent.
- [x] Every finite realization reduces by combining duplicate nodes and removing zero coefficients.
- [x] Reduced ordinary realizations are unique up to permutation.
- [x] Ordinary packet transforms are exactly the entire solutions of square-free constant-coefficient differential equations.
- [x] General constant-coefficient ODE solutions require confluent modes \(z^q e^{xz}\).
- [x] The minimal annihilator of a reduced packet is \(\prod_j(t-x_j)\).
- [x] Packet length equals minimal-annihilator degree.
- [x] Packet length equals derivative-orbit dimension.
- [x] Packet length equals infinite Hankel rank in the ordinary reduced case.
- [x] Generic exact recovery is available through a Prony/Hankel system.

## Claims that must not be made

- [ ] Do not claim that a fixed ordinary exponential polynomial has many reduced exact realizations.
- [ ] Do not treat translation or scaling as symmetries of a fixed function without defining a quotient or equivalence relation.
- [ ] Do not infer numerical stability from exact uniqueness.
- [ ] Do not infer positivity from a complex bilinear Hankel factorization.
- [ ] Do not claim that the realization theorem itself is new.
- [ ] Do not conflate repeated nodes with duplicate ordinary exponentials; repeated-root information belongs to confluent modes.
- [ ] Do not claim that the first \(2N\) jets always yield a well-conditioned reconstruction.

## New-work frontier

- [ ] Quantitative conditioning under node separation and coefficient floors.
- [ ] Optimal observation design for jets, real samples, and imaginary-frequency samples.
- [ ] Reflection-symmetric and parity-reduced reconstruction.
- [ ] Confluent compactification of collision strata.
- [ ] Approximate packet length and existence of constrained minimizers.
- [ ] Interaction between Hankel rank and weighted-shell rank.
- [ ] Stability of geometry optimization under perturbation.

## Immediate next proof

Prove a local nonsingularity theorem for the \(2N\)-jet realization map

\[
\mathcal R_N(X,u)
=
\left(\sum_j u_jx_j^k\right)_{k=0}^{2N-1}
\]

at every reduced configuration. The Jacobian is a confluent Vandermonde matrix with coefficient scaling. Its determinant should be computed explicitly, giving the exact algebraic degeneracy locus:

\[
\prod_j u_j\prod_{i<j}(x_j-x_i)^4=0
\]

up to a nonzero sign and convention-dependent constant. This will turn the qualitative stability discussion into a precise local-identifiability theorem.