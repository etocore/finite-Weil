# The full translated family and the true obstruction set

## Status

This note replaces the incorrect commutator-spanning heuristic with an exact exponential-sum formula for the matrix element

\[
f_{rs}(t):=\langle u_r,T_tu_s\rangle.
\]

It proves that full-family vanishing is equivalent to a finite set of shell-sum identities indexed by node differences. The remaining problem is no longer an infinite Taylor-series question.

## 1. Raw translated Gaussian

Let

\[
(T_t)_{ij}=\kappa\exp\!\left(-\frac{(x_i-x_j-t)^2}{4\sigma^2}\right),
\]

where \(\kappa\neq0\) is the fixed scalar prefactor and the nodes are distinct and reflection-symmetric.

For eigenvectors \(u_r,u_s\) of \(T_0\), define

\[
f_{rs}(t):=\langle u_r,T_tu_s\rangle.
\]

Expanding the square gives

\[
(T_t)_{ij}
=
\kappa e^{-t^2/(4\sigma^2)}
 e^{-(x_i-x_j)^2/(4\sigma^2)}
 e^{t(x_i-x_j)/(2\sigma^2)}.
\]

Hence

\[
f_{rs}(t)
=
\kappa e^{-t^2/(4\sigma^2)}
\sum_{i,j}
 u_r(i)u_s(j)
 e^{-(x_i-x_j)^2/(4\sigma^2)}
 e^{t(x_i-x_j)/(2\sigma^2)}.
\]

Let

\[
\Delta:=\{x_i-x_j:1\le i,j\le N\}
\]

be the finite set of distinct node differences, and for each \(d\in\Delta\) define the shell coefficient

\[
S_{rs}(d)
:=
\sum_{x_i-x_j=d}
 u_r(i)u_s(j).
\]

Since the Gaussian factor depends only on \(d\), we obtain the exact formula

\[
\boxed{
 f_{rs}(t)
 =
 \kappa e^{-t^2/(4\sigma^2)}
 \sum_{d\in\Delta}
 e^{-d^2/(4\sigma^2)}
 S_{rs}(d)
 e^{td/(2\sigma^2)}.
}
\tag{1.1}
\]

## 2. Finite exponential independence

The functions

\[
t\longmapsto e^{td/(2\sigma^2)},\qquad d\in\Delta,
\]

are linearly independent because the exponents are distinct. Therefore (1.1) gives:

> **Proposition 2.1.**
> \[
> f_{rs}(t)\equiv0
> \quad\Longleftrightarrow\quad
> S_{rs}(d)=0
> \text{ for every }d\in\Delta.
> \]

Thus the true obstruction set is characterized by a finite family of identities.

Equivalently, if

\[
q_{rs}(z)
:=
\sum_{d\in\Delta}S_{rs}(d)z^d
\]

is viewed formally when the nodes lie on an affine lattice, then full-family vanishing is exactly the vanishing of every coefficient of this cross-correlation polynomial.

## 3. Correlation interpretation

Define reflected vectors by

\[
\widetilde u_s(x_i):=u_s(-x_i).
\]

Then \(S_{rs}(d)\) is the discrete cross-correlation of \(u_r\) with \(u_s\), grouped by geometric displacement:

\[
S_{rs}(d)
=
\sum_{x_i-x_j=d}u_r(i)u_s(j).
\]

Therefore:

> **Corollary 3.1.** The full translated family fails to produce the edge \((r,s)\) exactly when the displacement correlation of \(u_r\) and \(u_s\) vanishes on every difference shell.

This is strictly weaker than coordinatewise disjointness. The earlier diagonal-polynomial argument does not follow from full-family vanishing.

## 4. Same-parity symmetry

If \(u_r,u_s\) have the same reflection parity, then

\[
S_{rs}(-d)=S_{rs}(d).
\]

Consequently

\[
f_{rs}(t)
=
\kappa e^{-t^2/(4\sigma^2)}
\left[
S_{rs}(0)
+
2\sum_{d>0}
 e^{-d^2/(4\sigma^2)}
 S_{rs}(d)
 \cosh\!\left(\frac{td}{2\sigma^2}\right)
\right].
\]

Since distinct positive \(d\)'s give linearly independent \(\cosh\)-functions, same-parity full-family vanishing is equivalent to

\[
S_{rs}(d)=0
\qquad\text{for every }d\ge0.
\]

## 5. Immediate consequence for generic node differences

Suppose every positive node difference occurs for exactly one ordered pair up to reflection; that is, for each \(d>0\) there are exactly the two pairs

\[
(x_i,x_j),\qquad(-x_j,-x_i)
\]

with difference \(d\).

For same-parity eigenvectors of parity \(\varepsilon\in\{\pm1\}\), these two contributions are equal, so

\[
S_{rs}(d)=2u_r(i)u_s(j).
\]

Hence, if every eigenvector coordinate is nonzero, then no same-parity matrix element can vanish identically.

> **Proposition 5.1.** Under unique positive differences up to reflection, and assuming the relevant eigenvectors have no zero coordinates,
> \[
> f_{rs}\not\equiv0
> \]
> for every same-parity pair \(r\ne s\).

This proves emptiness of the true obstruction set for a large generic class of symmetric node configurations.

## 6. Five-node odd block

For

\[
\{-a,-b,0,b,a\},\qquad a>b>0,
\]

the odd block has basis \(f_a,f_b\). Let its two normalized eigenvectors be

\[
y_+=(p,q),\qquad y_-=(-q,p),
\]

with \(p,q\neq0\).

Consider the largest positive difference

\[
d=a+b.
\]

Only the ordered pairs \((a,-b)\) and \((b,-a)\) contribute. A direct parity-basis computation gives

\[
S_{+-}(a+b)
=
-p^2+q^2.
\]

Thus full-family vanishing would force \(p^2=q^2\). For a real symmetric block

\[
B=\begin{pmatrix}A&C\\C&D\end{pmatrix},
\]

this occurs only when \(A=D\). But in the five-node family

\[
A(v)-D(v)=e^{-2b^2v}-e^{-2a^2v}>0
\]

for every \(v>0\). Therefore

\[
S_{+-}(a+b)\neq0
\]

for every width.

> **Theorem 6.1.** For every five-node family
> \[
> \{-a,-b,0,b,a\},\qquad a>b>0,
> \]
> the odd coupling function
> \[
> \langle u_1,T_tu_3\rangle
> \]
> is not identically zero for any width. Hence every second-order exceptional width in this family is repaired by some higher even Taylor coefficient.

This proves higher-order recovery for the explicit counterexample from `paper/exceptional-widths.md`, without computing the fourth derivative.

## 7. The remaining all-node problem

The exact obstruction is now:

\[
S_{r,r+2}(d)=0
\qquad\forall d\in\Delta.
\]

To prove \(\widetilde Z_N=\varnothing\) for arbitrary symmetric distinct nodes, one must rule out total cancellation across every repeated-difference shell.

The hard cases are therefore configurations with additive coincidences

\[
x_i-x_j=x_k-x_\ell.
\]

This identifies the correct next routes:

1. prove that an extreme nonzero shell contains too few terms to cancel;
2. use oscillation and parity to control the sign of shell sums near the boundary;
3. treat repeated-difference configurations through additive-combinatorial stratification;
4. search for a counterexample by solving the finite shell system rather than truncating the Taylor series.

## 8. Conclusion

The infinite Hermite tower collapses to a finite correlation problem. The true obstruction set is empty whenever at least one displacement shell has nonzero cross-correlation. For the five-node odd block, the shell at \(a+b\) proves this for every width.