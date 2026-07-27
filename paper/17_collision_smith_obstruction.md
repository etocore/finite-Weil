# Determinantal obstruction in the simplified collision model

## 1. Purpose

This note computes the h-adic invariant factors of the simplified centered upper block

\[
D_m(h)C|_{E_0},
\]

where

\[
D_m(h)=\operatorname{diag}(h^m,h^{m+1},\ldots,h^{2m-1}).
\]

The calculation shows that this model generically contains exponent \(m\). Therefore it cannot explain a universal spectrum with the exponent \(m\) missing.

## 2. Determinantal valuations

Let

\[
K=C|_{E_0}
\]

be represented as an \(m\times(m-1)\) constant matrix of full column rank.

The weighted matrix is

\[
A(h)=D_m(h)K.
\]

For each \(1\le k\le m-1\), the valuation of the k-th determinantal divisor is the minimum valuation among all nonzero \(k\times k\) minors.

A minor using rows

\[
r_1<\cdots<r_k
\]

has h-order

\[
(m+r_1)+\cdots+(m+r_k),
\]

provided the corresponding constant minor of \(K\) is nonzero.

For a generic full-rank matrix \(K\), the minors using the first \(k\) rows are nonzero. Hence

\[
\nu_k
=
\sum_{r=0}^{k-1}(m+r)
=
km+\frac{k(k-1)}2.
\]

The successive invariant-factor exponents are

\[
\nu_k-\nu_{k-1}
=
m+k-1.
\]

Therefore the generic upper exponents are

\[
\boxed{m,m+1,\ldots,2m-2}.
\]

## 3. Consequence

Combining this with the lower weight exponents

\[
0,1,\ldots,m-1
\]

gives the simplified full list

\[
\boxed{0,1,\ldots,2m-2}.
\]

There is no missing grade in this model.

Thus at least one ingredient used by the original singular-value experiments is absent from

\[
D_m(h)C|_{E_0}.
\]

## 4. Small cases

For \(m=2\), the centered upper block is one column with generic exponent

\[
2.
\]

For \(m=3\), the generic upper exponents are

\[
3,4.
\]

For \(m=4\), they are

\[
4,5,6.
\]

These outcomes directly contradict the proposed upper lists

\[
3,
\qquad
4,5,
\qquad
5,6,7,
\]

that would follow from omitting exponent \(m\).

## 5. Interpretation

The translation relation

\[
\lambda^{\mathsf T}K=0
\]

is a relation among the unweighted rows of \(K\). It does not force the first row of \(K\) to vanish, and it does not increase the minimum determinantal valuation after multiplication by \(D_m(h)\).

The observed missing grade must therefore come from additional structure in the actual Jacobian, such as:

1. a source normalization depending analytically on \(h\);
2. coupling with center or scale columns;
3. a Schur complement formed before the center variable is removed;
4. an additional constraint on weights or moments;
5. a different matrix being measured in the numerical experiments.

## 6. Reproduction

The diagnostic is implemented in

```text
experiments/collision_smith_diagnostic.py
```

It computes determinantal-divisor valuations from nonzero minors of the constant centered matrix.

Representative runs are

```bash
python -m experiments.collision_smith_diagnostic \
  --nodes=-1,0,1 \
  --weights=1,2,3
```

and

```bash
python -m experiments.collision_smith_diagnostic \
  --nodes=-2,-0.5,0.75,1.75 \
  --weights=1,2,-1,3
```

## 7. Revised next step

The immediate task is no longer to globalize a local Smith theorem. It is to recover the exact matrix used in the original flat-limit singular-value experiments and compare it term by term with the simplified block.

For each source column, the reconstruction must record:

- whether center and scale are independent variables;
- whether weight corrections depend on \(h\);
- which normalization constraints are imposed;
- which target coordinates are projected out;
- whether the matrix is a raw Jacobian, Gram-normalized Jacobian, Schur complement, or singular-value equivalent.

Only after that audit can the missing exponent be stated as a theorem target again.

## 8. Claim ledger

| Statement | Status |
|---|---|
| Simplified upper block is \(D_m(h)C|_{E_0}\) | Definition of the diagnostic model |
| Generic upper exponents are \(m,\ldots,2m-2\) | Proved by determinantal valuations |
| Translation relation removes exponent \(m\) in this model | False |
| Simplified model reproduces the observed missing grade | False |
| Exact experimental Jacobian has been reconstructed | Open |
| Universal missing-grade theorem | Open |
