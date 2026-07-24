# Oscillation-chain lemma for local two-shift generation

## Setup

Let

\[
A:=T_0,
\qquad
X:=\operatorname{diag}(x_1,\ldots,x_N),
\qquad
x_1<\cdots<x_N,
\]

with

\[
A_{ij}=-2\sigma\sqrt\pi\,
\exp\!\left(-\frac{(x_i-x_j)^2}{4\sigma^2}\right).
\]

Let \(J\) denote reflection about the midpoint of the grid. Then \(A\) commutes with \(J\). The unsigned Gaussian matrix \(-A\) is strictly totally positive, so \(A\) has simple spectrum. Choose a real orthonormal eigenbasis

\[
Au_r=\lambda_r u_r
\]

ordered by oscillation number, so that \(u_r\) has exactly \(r\) sign changes. Each \(u_r\) has definite parity.

For the symmetric translated Gaussian family,

\[
T_t=T_{-t},
\qquad
T_t=A+\frac{t^2}{2}M+O(t^4),
\qquad
M:=T''_0.
\]

Direct differentiation gives

\[
M_{ij}
=-\sigma\sqrt\pi\,
\exp\!\left(-\frac{(x_i-x_j)^2}{4\sigma^2}\right)
\left(
\frac{(x_i-x_j)^2}{2\sigma^4}-\frac1{\sigma^2}
\right).
\]

Equivalently,

\[
\boxed{
M=-\frac1{2\sigma^2}A+\frac1{4\sigma^4}[X,[X,A]].
}
\]

Since \(\langle u_r,Au_s\rangle=0\) for \(r\ne s\),

\[
\boxed{
\langle u_r,Mu_s\rangle
=\frac1{4\sigma^4}
\langle u_r,[X,[X,A]]u_s\rangle.
}
\]

The same quantity has the entrywise form

\[
\langle u_r,Mu_s\rangle
=\frac1{4\sigma^4}
\sum_{i,j=1}^N
u_r(i)u_s(j)(x_i-x_j)^2A_{ij}.
\]

## Minimal remaining lemma

The graph lemma does not require every same-parity coupling to be nonzero. It is enough to establish a spanning path in each parity block.

> **Oscillation-chain lemma.** For every \(r=0,\ldots,N-3\),
> \[
> \boxed{
> \langle u_r,Mu_{r+2}\rangle\ne0.
> }
> \]

The indices \(r,r+2\) have the same parity. Thus these couplings provide the path edges

\[
0-2-4-\cdots
\qquad\text{and}\qquad
1-3-5-\cdots.
\]

## Consequence of the chain lemma

For every chain edge,

\[
\langle u_r,T_tu_{r+2}\rangle
=\frac{t^2}{2}\langle u_r,Mu_{r+2}\rangle+O(t^4).
\]

There are finitely many chain edges. If the chain lemma holds, there is one \(\varepsilon>0\) such that all of them remain nonzero whenever

\[
0<|t|<\varepsilon.
\]

The graph of \(T_t\) in the simple-spectrum eigenbasis of \(A\) is then connected in each parity block. Hence

\[
\operatorname{Comm}(A|_{H_\pm},T_t|_{H_\pm})
=\mathbf C I_{H_\pm}.
\]

Therefore

\[
\operatorname{Comm}(T_0,T_t)=\operatorname{span}\{I,J\},
\]

and by finite-dimensional bicommutant theory,

\[
\operatorname{alg}^*\{T_0,T_t\}
=M_{N_+}(\mathbf C)\oplus M_{N_-}(\mathbf C).
\]

## Route that should not be used

The cross-parity matrix

\[
C=U_+^{\mathsf T}XU_-
\]

does not exhibit a stable global entry-sign pattern in numerical experiments. Therefore a proof based on strict sign regularity of all entries of \(C\) is not currently justified and appears false as stated.

Likewise, proving all same-parity entries \(\langle u_r,Mu_s\rangle\) nonzero is unnecessary. The chain lemma alone is sufficient.

## Analytic proof program

A successful proof should derive the chain nonvanishing directly from oscillation theory rather than from a signed sum over the full spectrum. The useful input is expected to be:

1. \(-A\) is strictly totally positive;
2. the eigenvectors have exact nodal counts and interlacing;
3. \(X\) is a strictly increasing multiplier and reverses parity;
4. \([X,[X,A]]_{ij}=(x_i-x_j)^2A_{ij}\).

The precise missing step is to rule out

\[
\sum_{i,j}
 u_r(i)u_{r+2}(j)(x_i-x_j)^2A_{ij}=0.
\]

A plausible route is to establish a discrete Chebyshev-system statement for the pair \(u_r,u_{r+2}\), then apply strict total positivity of the Gaussian kernel to the quadratic coordinate difference. This implication has not yet been proved and must not be treated as automatic from nodal counts alone.

## Certified fallback

For fixed \(N,h,\sigma\), the chain lemma requires only \(N-2\) scalar nonvanishing certificates. Interval arithmetic can certify enclosures for

\[
\langle u_r,Mu_{r+2}\rangle,
\qquad r=0,\ldots,N-3,
\]

provided the simple eigenpairs of \(A\) are themselves enclosed rigorously. This is substantially cheaper than certifying all pairwise couplings or the rank of a full commutator map.

## Honest status

The derivative formula, double-commutator identity, graph reduction, and sufficiency of the chain are proved. Numerical evidence supports the chain lemma. The all-\(N\), all-parameter analytic nonvanishing statement remains open.