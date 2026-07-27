# Correction: Gaussian synthesis reproduces the intrinsic missing grade

## Status

The earlier version of this note reported consecutive exponents for the Gaussian synthesis map and concluded that the missing grade must arise later in the matrix pipeline. That conclusion was caused by double-precision loss of the deepest singular directions.

It is withdrawn.

## High-precision result

For a three-node collision, the Gaussian synthesis Jacobian computed at 100 decimal digits has exponents

\[
\boxed{(0,0,1,2,4,5)}.
\]

Their sum is numerically \(11.9999\), consistent with the exact total valuation \(12\).

This agrees with the exact rational result for the raw moment Jacobian:

\[
\nu=(0,0,1,3,7,12),
\qquad
\nu_k-\nu_{k-1}=(0,0,1,2,4,5).
\]

Thus the polynomial moment realization and the Gaussian synthesis realization have the same resolved collision spectrum.

## Why binary64 failed

At cluster scale \(h\), the deepest singular direction for \(m=3\) behaves like \(h^5\). At

\[
h=10^{-5},
\]

this is of order

\[
10^{-25}.
\]

The matrix simultaneously has singular values of order one. Binary64 cannot resolve a relative scale of \(10^{-25}\), so the smallest singular values are replaced by roundoff noise. Log-log regression then fits the noise rather than the matrix germ.

The previously reported consecutive lists

\[
0,1,\ldots,2m-2
\]

were therefore precision artifacts.

## Exterior nodes

The corrected conclusion is not that exterior nodes create the gap. The gap is already present for the isolated cluster. Exterior-node experiments remain useful only for checking stability of the intrinsic spectrum under embedding.

The current evidence supports exterior independence:

- cluster alone: missing grade \(m\);
- cluster with separated nodes: same missing grade;
- square and rectangular target truncations: same missing grade;
- polynomial moment and Gaussian synthesis realizations: same spectrum.

## Methodological rule

Collision exponents must be established by one of:

1. exact determinantal-divisor valuations when the entries are polynomial or rational in \(h\);
2. arbitrary-precision singular values with a precision budget comfortably exceeding the deepest expected order;
3. both, when two realizations are being compared.

Double-precision slope fitting is not admissible as primary evidence once the expected dynamic range exceeds approximately \(10^{14}\).

## Revised role of the pipeline experiment

The \(A/B\), whitening, and generalized-eigenvalue stages are no longer candidates for the origin of the missing grade. They remain worth studying because nonlinear normalization can shift or merge orders, but those are downstream effects acting on an already singularly filtered cluster.

## Current conclusion

\[
\boxed{
\text{The missing grade is intrinsic to the confluent cluster Jacobian germ.}
}
\]

The sharp remaining target is a general formula for the determinantal valuations \(\nu_k(J_m)\).
