# Uniform witness minors for the raw moment Jacobian

## 1. Setup

Let

\[
M_r=\sum_{j=1}^m u_jx_j^r,
\qquad x_j=h\xi_j,
\qquad 0\le r<2m.
\]

The raw Jacobian has weight columns

\[
W_j(r)=h^r\xi_j^r
\]

and position columns

\[
P_j(r)=r u_jh^{r-1}\xi_j^{r-1}.
\]

For a minor using row degrees \(R\) and \(p\) position columns, every determinant term has the same order

\[
\operatorname{ord}_h=\sum_{r\in R}r-p.
\]

Thus the determinantal-ideal problem separates into a grade lower bound and a coefficient nonvanishing problem.

## 2. Universal lower bound

For a \(k\times k\) minor, the smallest possible sum of distinct row degrees is

\[
0+1+\cdots +(k-1)=\frac{k(k-1)}2.
\]

There are at most \(m\) position columns. In addition, whenever the minimal row set contains row zero, a nonzero minor cannot consist entirely of position columns because

\[
P_j(0)=0
\]

for every \(j\). Therefore at least one weight column is required, and the number of position columns is at most \(k-1\).

Consequently

\[
\nu_k\ge
\frac{k(k-1)}2-\min(m,k-1).
\]

Equivalently,

\[
\boxed{
\nu_k\ge
\begin{cases}
\dfrac{(k-1)(k-2)}2, & 1\le k\le m+1,\\[6pt]
\dfrac{k(k-1)}2-m, & m+2\le k\le 2m.
\end{cases}}
\]

This is exactly the valuation sequence observed in the exact computations.

## 3. Canonical witness family

The experiment `experiments/raw_moment_witnesses.py` uses the first \(k\) rows

\[
R_k=\{0,1,\ldots,k-1\}.
\]

For \(k\le m+1\), it chooses one weight column and \(k-1\) position columns:

\[
C_k=\{W_1,P_1,\ldots,P_{k-1}\}.
\]

For \(k>m+1\), it chooses all \(m\) position columns and \(k-m\) weight columns:

\[
C_k=\{W_1,\ldots,W_{k-m},P_1,\ldots,P_m\}.
\]

These choices attain the lower-bound grade exactly. Hence proving their coefficient determinants are nonzero on a Zariski-open set gives equality in every determinantal valuation.

## 4. Resulting Smith sequence

If the canonical coefficient minors are generically nonzero, then

\[
\nu_k=
\frac{k(k-1)}2-\min(m,k-1).
\]

Taking successive differences gives

\[
e_1=0,
\qquad e_2=0,
\]

followed by

\[
1,2,\ldots,m-1
\]

and then

\[
m+1,m+2,\ldots,2m-1.
\]

Thus

\[
\boxed{
E_m=\{0,0,1,2,\ldots,m-1,m+1,\ldots,2m-1\}.
}
\]

The grade \(m\) is missing.

## 5. Exact checks

The canonical minors are nonzero for generic rational specializations through at least \(m=5\). The tests verify:

\[
\begin{aligned}
m=2 &: (0,0,1,4),\\
m=3 &: (0,0,1,3,7,12),\\
m=4 &: (0,0,1,3,6,11,17,24).
\end{aligned}
\]

The associated Smith exponents are

\[
\begin{aligned}
m=2 &: (0,0,1,3),\\
m=3 &: (0,0,1,2,4,5),\\
m=4 &: (0,0,1,2,3,5,6,7).
\end{aligned}
\]

## 6. Remaining proof obligation

The lower bound is complete. The sharp remaining target is:

> Prove that each canonical coefficient determinant is a nonzero polynomial in the distinct nodes and nonzero weights.

There are two likely routes.

1. Identify the minors as partial confluent Vandermonde determinants and invoke or derive their factorization.
2. Exhibit one symbolic specialization for every \(m,k\) with a closed nonzero determinant formula.

The second route may be shortest. Choosing structured nodes such as

\[
\xi_j=j
\]

and simple nonzero weights may reduce the canonical determinants to products of factorials and Vandermonde factors. Once one such specialization is proved nonzero, generic nonvanishing follows immediately.

## 7. Claim ledger

| Statement | Status |
|---|---|
| Every minor has grade \(\sum R-p\) | Exact |
| Universal lower bound for \(\nu_k\) | Proved |
| Canonical witnesses attain the lower-bound grade | Exact by construction |
| Canonical coefficients are nonzero through \(m=5\) | Exact computation |
| Canonical coefficients are generically nonzero for all \(m,k\) | Open |
| General missing-grade Smith theorem | Reduced to canonical nonvanishing |
