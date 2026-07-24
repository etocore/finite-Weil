# Width-rotation chain lemma for local two-shift generation

## Setup

Let

\[
A(\tau):=T_0,
\qquad
\tau:=\sigma^2,
\qquad
X:=\operatorname{diag}(x_1,\ldots,x_N),
\qquad
x_1<\cdots<x_N,
\]

with

\[
A(\tau)_{ij}
=-2\sqrt\pi\,\tau^{1/2}
\exp\!\left(-\frac{(x_i-x_j)^2}{4\tau}\right).
\]

Assume the nodes are symmetric about their midpoint so that the reflection operator \(J\) is defined and commutes with \(A(\tau)\). The unsigned Gaussian matrix \(-A(\tau)\) is strictly totally positive for every finite \(\tau>0\), hence \(A(\tau)\) has simple spectrum for every \(\tau>0\).

Choose a real orthonormal analytic eigenbasis on each simply connected parameter interval,

\[
A(\tau)u_r(\tau)=\lambda_r(\tau)u_r(\tau),
\]

ordered by oscillation number. Each \(u_r\) has definite parity.

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
=-\sqrt\pi\,\tau^{1/2}
\exp\!\left(-\frac{(x_i-x_j)^2}{4\tau}\right)
\left(
\frac{(x_i-x_j)^2}{2\tau^2}-\frac1\tau
\right).
\]

Equivalently,

\[
M=-\frac1{2\tau}A+\frac1{4\tau^2}[X,[X,A]].
\]

The key identity is

\[
\boxed{
M=\frac{\partial A}{\partial\tau}-\frac1\tau A.
}
\]

Indeed,

\[
\frac{\partial A}{\partial\tau}
=
\frac1{2\tau}A
+
\frac1{4\tau^2}[X,[X,A]].
\]

For \(r\ne s\), orthogonality gives

\[
\boxed{
\langle u_r,Mu_s\rangle
=
\left\langle u_r,\frac{\partial A}{\partial\tau}u_s\right\rangle.
}
\]

Differentiating the eigenvalue equation and pairing with \(u_r\) yields

\[
\boxed{
\langle u_r,Mu_s\rangle
=
(\lambda_s-\lambda_r)
\left\langle u_r,\frac{\partial u_s}{\partial\tau}\right\rangle.
}
\]

Thus the coupling is exactly the angular velocity of the Gaussian-kernel eigenbasis as the width varies.

## Minimal graph target

The graph lemma requires only a connected graph in each parity block. It is enough to use the parity chains

\[
0-2-4-\cdots,
\qquad
1-3-5-\cdots.
\]

Define

\[
g_r(\tau)
:=
\langle u_r(\tau),M(\tau)u_{r+2}(\tau)\rangle,
\qquad
r=0,\ldots,N-3.
\]

The former pointwise chain lemma

\[
g_r(\tau)\ne0\quad\text{for every }\tau>0
\]

is stronger than necessary. The analytic theorem only needs

\[
\boxed{
g_r\not\equiv0
\quad\text{for every }r.
}
\]

Because \(A(\tau)\) has simple spectrum for every finite \(\tau>0\), each \(g_r\) is real analytic. Therefore, once \(g_r\not\equiv0\), its zero set is discrete.

Set

\[
Z_N:=\bigcup_{r=0}^{N-3}\{\tau>0:g_r(\tau)=0\}.
\]

Then \(Z_N\) is discrete. For every \(\tau\notin Z_N\), all parity-chain edges are nonzero simultaneously.

## Consequence for two-shift generation

For each chain edge,

\[
\langle u_r,T_tu_{r+2}\rangle
=
\frac{t^2}{2}g_r(\tau)+O(t^4).
\]

Fix \(\tau\notin Z_N\). Since there are finitely many chain edges, there is one \(\varepsilon(\tau)>0\) such that all of them remain nonzero whenever

\[
0<|t|<\varepsilon(\tau).
\]

The graph of \(T_t\) in the simple-spectrum eigenbasis of \(A(\tau)\) is then connected in each parity block. Hence

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

## Flat-limit proof program

Write

\[
K_\tau(i,j)
:=
\exp\!\left(-\frac{(x_i-x_j)^2}{4\tau}\right).
\]

Using

\[
K_\tau(i,j)
=
\exp\!\left(-\frac{x_i^2}{4\tau}\right)
\exp\!\left(-\frac{x_j^2}{4\tau}\right)
\exp\!\left(\frac{x_ix_j}{2\tau}\right),
\]

we obtain the exact expansion

\[
K_\tau(i,j)
=
\exp\!\left(-\frac{x_i^2}{4\tau}\right)
\exp\!\left(-\frac{x_j^2}{4\tau}\right)
\sum_{k=0}^{\infty}
\frac{x_i^k x_j^k}{k!(2\tau)^k}.
\]

For fixed distinct nodes, the flat-limit eigenvectors converge to the discrete orthogonal polynomials \(p_r\) obtained by Gram-Schmidt from

\[
1,x,x^2,\ldots
\]

with respect to the counting measure on the node set. The eigenvalues satisfy

\[
\lambda_r(\tau)
\sim
\alpha_r\tau^{1/2-r},
\qquad
\alpha_r\ne0.
\]

The expected first nontrivial eigenvector correction has the form

\[
u_{r+2}(\tau)
=
p_{r+2}
+
\frac1\tau
\left(
\beta_r p_r+	ext{components orthogonal to }p_r
\right)
+
O(\tau^{-2}).
\]

Consequently,

\[
\frac{\partial u_{r+2}}{\partial\tau}
=
-\beta_r\tau^{-2}p_r+O(\tau^{-3}),
\]

and therefore

\[
\boxed{
g_r(\tau)
=C_r\tau^{-(r+3/2)}
\left(1+O(\tau^{-1})\right),
}
\]

with

\[
C_r=-\alpha_r\beta_r.
\]

Numerics support the exponent \(r+3/2\) exactly. The remaining symbolic task is to compute \(\beta_r\) from the polynomial-moment expansion and prove

\[
\boxed{C_r\ne0.}
\]

A formula in terms of discrete-orthogonal-polynomial norms is expected. Proving this coefficient nonzero for each \(r\) establishes \(g_r\not\equiv0\), which completes the analytic argument above.

## Route that should not be used

The cross-parity matrix

\[
C=U_+^{\mathsf T}XU_-
\]

does not exhibit a stable global entry-sign pattern numerically. A proof based on strict entrywise sign regularity is therefore unsupported and appears false as stated.

Likewise, apparent sign changes of \(g_r\) across parameter scans are not meaningful unless the eigenvector gauge is fixed continuously. Only \(|g_r|\) is gauge invariant. Numerical certificates must either use gauge-invariant quantities or specify and verify a continuous sign convention.

## Certified fallback

For fixed \(N\), node set, and \(\tau\), one may certify the chain by enclosing the \(N-2\) scalars

\[
g_r(\tau),
\qquad r=0,\ldots,N-3,
\]

provided the simple eigenpairs of \(A(\tau)\) are enclosed rigorously. This is cheaper than certifying all pairwise couplings or the rank of a full commutator map.

## Honest status

The width-derivative identity, eigenvector-rotation formula, analyticity reduction, graph deduction, and flat-limit exponent are established or numerically verified as indicated above. The all-\(N\) theorem is reduced to one symbolic coefficient calculation: derive the leading flat-limit constant \(C_r\) and prove \(C_r\ne0\) for every admissible \(r\). Until that coefficient is derived rigorously, the generic-width theorem remains conditional.