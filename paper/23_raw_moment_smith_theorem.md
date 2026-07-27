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

Let \(J_m(h)\) be the \(2m\times 2m\) Jacobian with respect to the source coordinates

\[
(u_1,\ldots,u_m,x_1,\ldots,x_m).
\]

Assume the nodes are pairwise distinct and the weights are nonzero. On a nonempty Zariski-open set of such parameters, the \(h\)-adic Smith exponents are

\[
\boxed{
0,0,1,2,\ldots,m-1,m+1,m+2,\ldots,2m-1.
}
\]

Thus grade \(m\) is absent from the generic raw confluent moment Jacobian over this specified source lattice.

The source-lattice qualification matters. Replacing the physical node coordinates \(x_j\) by normalized shape coordinates \(\xi_j\) multiplies the corresponding columns by \(h\), which is not a unimodular source transformation over \(\mathbb C\{h\}\). Such a reparameterization can change Smith exponents.

## 2. Entry grades

The two column types are

\[
\frac{\partial M_r}{\partial u_j}=h^r\xi_j^r,
\qquad
\frac{\partial M_r}{\partial x_j}=r u_jh^{r-1}\xi_j^{r-1}.
\]

For a minor with row set \(R\) and \(p\) position columns, every determinant term has the same order

\[
\operatorname{ord}_h=\sum_{r\in R}r-p,
\]

provided its coefficient determinant is nonzero.

## 3. Universal lower bound

Fix a nonzero \(k\times k\) minor.

### Case A: row zero is selected

If \(0\in R\), then the row-zero entries in all position columns vanish. A nonzero minor must therefore contain at least one weight column, so

\[
p\le \min(m,k-1).
\]

Also,

\[
\sum_{r\in R}r\ge 0+1+\cdots +(k-1)=\frac{k(k-1)}2.
\]

Hence

\[
\operatorname{ord}_h\ge
\frac{k(k-1)}2-\min(m,k-1).
\]

### Case B: row zero is not selected

If \(0\notin R\), then

\[
\sum_{r\in R}r\ge 1+2+\cdots+k=\frac{k(k+1)}2.
\]

Here only the unconditional bound

\[
p\le \min(m,k)
\]

is available. Therefore

\[
\operatorname{ord}_h\ge
\frac{k(k+1)}2-\min(m,k).
\]

This is at least

\[
\frac{k(k-1)}2-\min(m,k-1).
\]

Indeed, when \(k\le m\) the difference is \(k-1\), and when \(k>m\) the difference is \(k\).

Combining the two cases gives the valid universal bound

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

where \(W_j\) is the weight column at \(\xi_j\) and \(P_j\) is the position column at \(\xi_j\).

After expanding along row zero and factoring the weights, the coefficient is, up to sign,

\[
(k-1)!\left(\prod_{j=1}^{k-1}u_j\right)
\prod_{1\le a<b\le k-1}(\xi_b-\xi_a).
\]

It is nonzero whenever the selected nodes are distinct and the selected weights are nonzero. Its valuation is

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

Use rows \(0,1,\ldots,k-1\), all \(m\) position columns, and the first \(q\) weight columns.

We prove that this coefficient determinant is not identically zero by choosing real ordered nodes

\[
\xi_1<\xi_2<\cdots<\xi_m
\]

and nonzero weights.

Suppose a polynomial \(p\) of degree less than \(k=m+q\) lies in the kernel of these interpolation functionals. Then

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

On each open interval \((\xi_i,\xi_{i+1})\), the polynomial \(Q\) has a fixed nonzero sign. If \(s\) had no zero in that interval, continuity would give it a fixed nonzero sign there as well, making the integral nonzero. Thus \(s\) has a zero in each of the \(q-1\) disjoint intervals.

But \(\deg s\le q-2\). Hence \(s=0\), so \(p'=0\), and then \(p(\xi_1)=0\) gives \(p=0\).

The interpolation functionals are therefore independent for this ordered real specialization. Consequently the canonical determinant polynomial is not identically zero and is nonzero on a nonempty Zariski-open parameter set. Its valuation is

\[
\frac{k(k-1)}2-m,
\]

again attaining the lower bound.

## 6. Determinantal valuations

Combining the lower bound with the witnesses gives, generically,

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

## 8. Scope and unresolved transfer questions

The theorem is generic over the node and weight parameters and is stated for the physical-coordinate source lattice \((u,x)\).

It does not yet prove:

1. that the same Smith spectrum holds for every distinct complex node configuration with nonzero weights;
2. invariance under non-unimodular collision reparameterizations involving \(x_j=h\xi_j\);
3. analytic equivalence between the polynomial moment Jacobian and the Gaussian synthesis Jacobian for arbitrary \(m\);
4. preservation of the filtration by the Gram, Weil, whitening, or generalized-eigenvalue stages;
5. any positivity or negativity statement for the finite Weil quadratic form.

Those are separate theorem targets and must not be inferred from the raw moment result alone.
