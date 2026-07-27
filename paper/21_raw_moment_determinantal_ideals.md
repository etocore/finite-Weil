# Raw moment determinantal ideals

## 1. Exact matrix germ

Let

\[
M_r(u,x)=\sum_{j=1}^m u_jx_j^r,
\qquad 0\le r\le 2m-1,
\]

and place the nodes on a collision curve

\[
x_j=h\xi_j,
\]

with pairwise distinct rational \(\xi_j\) and nonzero rational weights \(u_j\).
The raw Jacobian with columns ordered as weights and then positions is

\[
J_m(h)_{r,j}=h^r\xi_j^r,
\]

and

\[
J_m(h)_{r,m+j}
=
\begin{cases}
0,&r=0,\\
r u_jh^{r-1}\xi_j^{r-1},&r>0.
\end{cases}
\]

This is the matrix germ whose missing Smith grade was observed numerically.

## 2. Why exact minor valuations are inexpensive

Fix a minor with row set \(R\) and column set \(C\). Let \(p(C)\) be the
number of selected position columns. Every determinant term has the same
\(h\)-order

\[
\operatorname{ord}_h(R,C)
=
\sum_{r\in R}r-p(C).
\]

Therefore no polynomial determinant expansion is needed. One computes the
corresponding rational coefficient determinant. If it is nonzero, the displayed
integer is the exact valuation of that minor.

The experiment

```text
experiments/raw_moment_smith.py
```

enumerates exact minors, computes every determinantal valuation, and retains one
witness minor for each size.

## 3. Exact data

For generic rational nodes and nonzero weights, the first cases are:

\[
\begin{array}{c|c|c}
m& (\nu_1,\ldots,\nu_{2m})&(e_1,\ldots,e_{2m})\\
\hline
2&(0,0,1,4)&(0,0,1,3)\\
3&(0,0,1,3,7,12)&(0,0,1,2,4,5)\\
4&(0,0,1,3,6,11,17,24)&(0,0,1,2,3,5,6,7)
\end{array}
\]

where

\[
e_k=\nu_k-\nu_{k-1},\qquad \nu_0=0.
\]

The exponent equal to \(m\) is absent in every case.

## 4. Conjectured general Smith spectrum

The exact data suggest

\[
\boxed{
E_m=
\{0,0,1,2,\ldots,m-1,m+1,m+2,\ldots,2m-1\}.
}
\]

Equivalently, the determinantal valuations should be

\[
\nu_k=0,
\qquad 1\le k\le2,
\]

\[
\boxed{
\nu_k=\frac{(k-2)(k-1)}2,
\qquad 3\le k\le m+1,
}
\]

and

\[
\boxed{
\nu_k=
\frac{m(m-1)}2
+
\frac{(m+k)(k-m-1)}2,
\qquad m+2\le k\le2m.
}
\]

At full size this gives

\[
\nu_{2m}=2m(m-1).
\]

This agrees with the fourth power of the ordinary Vandermonde appearing in the
confluent Vandermonde determinant:

\[
\det J_m(h)
=
\left(\prod_j u_j\right)
\left(\prod_{i<j}(x_j-x_i)^4\right)
\]

up to an overall sign.

## 5. Proof program

For each \(k\), the theorem naturally splits into two inequalities.

### Upper bound

Exhibit a row set and column set whose rational coefficient determinant is
nonzero and whose grade is the conjectured \(\nu_k\). The witness minors emitted
by the experiment should reveal a uniform staircase pattern.

### Lower bound

Show that every nonzero \(k\)-minor has grade at least the conjectured value.
Since the grade is

\[
\sum_{r\in R}r-p(C),
\]

this is not merely an assignment problem: low-grade selections can have zero
coefficient determinant because weight and derivative columns become dependent
on too few moment rows. The lower bound must quantify this rank obstruction.

A likely formulation is a rank inequality for the truncated confluent
Vandermonde matrix. For the first \(q\) moment rows, determine the maximum number
of independent columns that can be selected from the value and derivative
columns. The jump in this rank profile should account exactly for the skipped
grade \(m\).

## 6. Current status

| Statement | Status |
|---|---|
| The missing grade occurs in the raw cluster Jacobian | Exact for tested cases |
| Gaussian synthesis has the same spectrum | Confirmed at high precision |
| Exterior nodes create the gap | False as a mechanism |
| Whitening or the Weil pipeline creates the gap | False as a mechanism |
| General spectrum is \(E_m\) above | Conjecture |
| Full determinant order is \(2m(m-1)\) | Confluent Vandermonde identity |
| All determinantal valuations satisfy the piecewise formula | Main theorem target |
