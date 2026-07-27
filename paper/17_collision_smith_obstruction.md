# Correction: the missing collision grade is intrinsic

## Status

This note supersedes the earlier conclusion that the isolated collision block has consecutive exponents. That conclusion came from replacing the raw moment Jacobian germ by the reduced model

\[
D_m(h)C|_{E_0}.
\]

The replacement does not preserve the determinantal ideals of the raw confluent Jacobian. Its Smith data therefore cannot be used to decide whether the grade \(m\) is present.

## Exact result for \(m=3\)

For the raw moment Jacobian, exact rational minor computation gives determinantal-divisor valuations

\[
\boxed{\nu=(0,0,1,3,7,12)}.
\]

Taking successive differences gives the Smith exponents

\[
\boxed{(0,0,1,2,4,5)}.
\]

Thus grade \(3=m\) is absent. This is an exact statement about the matrix germ, not a fitted singular-value observation.

The same exponent list is obtained from the Gaussian synthesis realization at 100 decimal digits. The moment and Gaussian models therefore agree in the resolved computation.

## What failed in the earlier reduction

The prior calculation of

\[
D_m(h)C|_{E_0}
\]

was internally correct for that particular matrix. The invalid step was treating it as Smith-equivalent to the raw Jacobian germ. Row grading alone does not capture cancellations among coupled weight and center columns. Those cancellations change the determinantal ideals and remove grade \(m\).

Accordingly, the statements

- "the simplified collision block has consecutive exponents," and
- "the missing grade must arise from exterior nodes or a later matrix pipeline"

are withdrawn as claims about the actual collision Jacobian.

## Precision failure

Double-precision singular-value regression is unreliable for this problem. For \(m=3\), the deepest scale behaves like \(h^5\). At \(h=10^{-5}\), this is approximately \(10^{-25}\), far below binary64 resolution relative to an order-one leading singular value.

Once the singular values cross the floating-point floor, fitted slopes become arbitrary. Numerical slope lists obtained in that regime are not evidence about the Smith spectrum.

## Correct conclusion

The current evidence supports:

1. the missing grade is intrinsic to the isolated \(m\)-cluster;
2. it occurs in the raw moment Jacobian itself;
3. it is independent of exterior nodes;
4. it is reproduced by the Gaussian synthesis map at sufficient precision;
5. it does not require the Gram, Weil, whitening, or generalized-eigenvalue pipeline.

## Remaining theorem target

Let \(J_m(h)\) denote the raw confluent moment Jacobian germ. For each \(k\), define

\[
\nu_k(J_m)
=
\min\{\operatorname{ord}_h \det M(h): M(h)\text{ is a nonzero }k\times k\text{ minor}\}.
\]

The next objective is to determine \(\nu_k(J_m)\) for general \(m\), then recover the Smith exponents from

\[
e_k=\nu_k-\nu_{k-1}.
\]

This is a determinantal-ideal problem. Floating-point singular-value fitting may be used only as a secondary check.

## Claim ledger

| Statement | Status |
|---|---|
| Exact \(m=3\) valuations are \((0,0,1,3,7,12)\) | Established by exact rational minor computation in the reported run |
| Exact \(m=3\) Smith exponents are \((0,0,1,2,4,5)\) | Immediate from the valuations |
| Grade \(m=3\) is missing intrinsically | Established for the computed germ |
| Exterior nodes create the missing grade | False |
| A later \(A/B\) or whitening stage is required | False |
| Closed formula for all \(m\) | Open |
