# Generic Smith spectrum of the raw moment Jacobian

## 1. Statement

Let

\[
M_r=\sum_{j=1}^m u_j x_j^r,\qquad 0\le r<2m,
\]

and place the nodes on the collision curve

\[
x_j=h\xi_j.
\]

Let \(J_m(h)\) be the \(2m\times 2m\) Jacobian with respect to
\((u_1,\ldots,u_m,x_1,\ldots,x_m)\). Assume the nodes are pairwise distinct and the
weights are nonzero. On a nonempty Zariski-open set of such parameters, the
\(h\)-adic Smith exponents are

\[
\boxed{
0,0,1,2,\ldots,m-1,m+1,m+2,\ldots,2m-1.
}
\]

Thus the grade \(m\) is intrinsically absent from the raw confluent moment
Jacobian germ.

## 2. Entry grades

The two column types are

\[
\frac{\partial M_r}{\partial u_j}=h^r\xi_j^r,
\qquad
\frac{\partial M_r}{\partial x_j}=r u_jh^{r-1}\xi_j^{r-1}.
\]

For a minor with row set \(R\) and \(p\) position columns, every determinant
term has the same order

\[
\operatorname{ord}_h=\sum_{r\in R}r-p,
\]

provided its coefficient determinant is nonzero.

## 3. Universal lower bound

For a \(k\)-minor, the least possible sum of distinct row indices is

\[
0+1+\cdots +(k-1)=\frac{k(k-1)}2.
\]

There are at most \(m\) position columns. Moreover, when the minimal row set
contains row zero, a nonzero minor must contain at least one weight column,
because every position entry in row zero vanishes. Therefore

\[
p\le \min(m,k-1).
\]

Hence every nonzero \(k\)-minor satisfies

\[
\boxed{
\nu_k\ge \frac{k(k-1)}2-\min(m,k-1).
}
\]

## 4. Canonical witnesses for \(k\le m+1\)

Use rows

\[
0,1,\ldots,k-1
\]

and columns

\[
W_1,P_1,\ldots,P_{k-1},
\]

where \(W_j\) is the weight column at \(\xi_j\) and \(P_j\) is the position
column at \(\xi_j\).

After expanding along row zero and factoring the weights, the coefficient is,
up to sign,

\[
(k-1)!\left(\prod_{j=1}^{k-1}u_j\right)
\prod_{1\le a<b\le k-1}(\xi_b-\xi_a).
\]

It is nonzero whenever the selected nodes are distinct and the selected weights
are nonzero. Its valuation is

\[
\frac{k(k-1)}2-(k-1)=\frac{(k-1)(k-2)}2.
\]

This attains the lower bound.

## 5. Canonical witnesses for \(k>m+1\)

Write

\[
q=k-m,
\qquad 2\le q\le m.
\]

Use rows \(0,1,\ldots,k-1\), all \(m\) position columns, and the first \(q\)
weight columns.

We prove that this coefficient determinant is not identically zero by choosing
real ordered nodes

\[
\xi_1<\xi_2<\cdots<\xi_m
\]

and nonzero weights.

Suppose a polynomial \(p\) of degree less than \(k=m+q\) lies in the kernel of
these interpolation functionals. Then

\[
p(\xi_i)=0\quad(1\le i\le q),
\qquad
p'(\xi_j)=0\quad(1\le j\le m).
\]

Let

\[
Q(x)=\prod_{j=1}^m(x-\xi_j).
\]

Since \(p'\) vanishes at all \(m\) nodes,

\[
p'(x)=Q(x)s(x)
\]

for a polynomial \(s\) satisfying

\[
\deg s\le q-2.
\]

For every \(1\le i<q\),

\[
0=p(\xi_{i+1})-p(\xi_i)
 =\int_{\xi_i}^{\xi_{i+1}}Q(t)s(t)\,dt.
\]

On each open interval \((\xi_i,\xi_{i+1})\), the polynomial \(Q\) has a fixed
nonzero sign. Therefore the vanishing integral forces \(s\) to have a zero in
that interval. The \(q-1\) disjoint intervals produce \(q-1\) distinct roots of
\(s\), but \(\deg s\le q-2\). Thus \(s=0\), so \(p'=0\), and then
\(p(\xi_1)=0\) gives \(p=0\).

The interpolation functionals are therefore independent for this ordered real
specialization. Consequently the canonical determinant polynomial is not
identically zero, and it is nonzero on a nonempty Zariski-open parameter set.
Its valuation is

\[
\frac{k(k-1)}2-m,
\]

again attaining the lower bound.

## 6. Determinantal valuations

Combining the lower bound with the witnesses gives

\[
\boxed{
\nu_k=\frac{k(k-1)}2-\min(m,k-1),
\qquad 1\le k\le 2m.
}
\]

Equivalently,

\[
\nu_k=
\begin{cases}
\dfrac{(k-1)(k-2)}2, & 1\le k\le m+1,\\[6pt]
\dfrac{k(k-1)}2-m, & m+1\le k\le 2m.
\end{cases}
\]

## 7. Smith exponents

Taking successive differences, with \(\nu_0=0\), gives

\[
e_k=\nu_k-\nu_{k-1}.
\]

The resulting multiset is

\[
\boxed{
\{0,0,1,2,\ldots,m-1,m+1,m+2,\ldots,2m-1\}.
}
\]

At full rank,

\[
\nu_{2m}=2m(m-1),
\]

in agreement with the weighted confluent Vandermonde determinant.

## 8. Scope

The theorem is generic over the node and weight parameters. The small-witness
family is nonzero for every distinct selected node configuration with nonzero
weights. For the large-witness family, the argument proves nonvanishing on a
real ordered specialization and hence generic nonvanishing algebraically.
Special complex configurations may lie on the witness determinant's vanishing
locus without changing the generic determinantal ideal.
