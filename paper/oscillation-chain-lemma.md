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

## Flat-limit variables and exact factorization

Set

\[
v:=\frac1{2\tau},
\qquad
K(v)_{ij}:=e^{-v(x_i-x_j)^2/2},
\]

so that

\[
A(\tau)=-2\sqrt\pi\,\tau^{1/2}K(v).
\]

Let

\[
E(v):=e^{-vX^2/2},
\qquad
m_k:=(x_1^k,\ldots,x_N^k)^{\mathsf T}.
\]

Then the Gaussian kernel admits the exact graded factorization

\[
\boxed{
K(v)=E(v)
\left(
\sum_{k=0}^{\infty}\frac{v^k}{k!}m_km_k^{\mathsf T}
\right)
E(v).
}
\]

For any eigenvectors \(K(v)u_j(v)=\mu_j(v)u_j(v)\), the double commutator has the exact decomposition

\[
\boxed{
\langle u_r,[X,[X,K]]u_s\rangle
=
(\mu_r+\mu_s)\langle u_r,X^2u_s\rangle
-2\langle Xu_r,KXu_s\rangle.
}
\]

The second term can be expanded exactly through the graded factorization:

\[
\langle Xu_r,KXu_s\rangle
=
\sum_{k=0}^{\infty}
\frac{v^k}{k!}
\langle E m_k,Xu_r\rangle
\langle E m_k,Xu_s\rangle.
\]

For symmetric nodes, \(m_k\) has parity \((-1)^k\), \(E\) is even, and \(Xu_j\) has the opposite parity of \(u_j\). Hence all parity-forbidden summands vanish exactly.

## Discrete orthogonal polynomials

Let \(p_0,\ldots,p_{N-1}\) be the orthonormal polynomials obtained by Gram-Schmidt from

\[
1,x,x^2,\ldots
\]

with respect to counting measure on the nodes. Write their three-term recurrence as

\[
\boxed{
xp_j=a_{j+1}p_{j+1}+b_jp_j+a_jp_{j-1},}
\]

with \(a_j>0\) for every admissible index.

Applying the recurrence twice gives the exact selection rule

\[
\begin{aligned}
xp_{r+2}
&=a_{r+3}p_{r+3}+b_{r+2}p_{r+2}+a_{r+2}p_{r+1},\\
x^2p_{r+2}
&=a_{r+2}a_{r+1}p_r
+\text{terms orthogonal to }p_r.
\end{aligned}
\]

Therefore

\[
\boxed{
\langle p_r,x^2p_{r+2}\rangle=a_{r+1}a_{r+2}>0.
}
\]

If one uses the shifted convention

\[
xp_j=a_jp_{j+1}+b_jp_j+a_{j-1}p_{j-1},
\]

the same coefficient is written \(a_ra_{r+1}\). The proof is identical; only the indexing changes.

## Flat-limit eigenvalue coefficients

Let \(q_r\) denote the component of \(m_r\) orthogonal to polynomials of degree at most \(r-1\):

\[
q_r:=(I-\Pi_{r-1})m_r.
\]

The graded Gram expansion implies

\[
\boxed{
\mu_r(v)=c_rv^r+O(v^{r+1}),
\qquad
c_r=\frac{\|q_r\|^2}{r!}>0.
}
\]

This positivity is elementary: the nodes are distinct, so \(m_r\) does not lie in the span of \(m_0,\ldots,m_{r-1}\), hence \(q_r\ne0\).

## Candidate leading chain coefficient

The exact double-commutator decomposition isolates two contributions for \(s=r+2\):

\[
D_r(v)
:=
(\mu_r+\mu_{r+2})
\langle u_r,X^2u_{r+2}\rangle,
\]

and

\[
S_r(v)
:=
2\langle Xu_r,KXu_{r+2}\rangle.
\]

Using

\[
u_j(v)=p_j+O(v),
\qquad
\mu_r(v)=c_rv^r+O(v^{r+1}),
\]

and the recurrence selection rule gives

\[
\boxed{
D_r(v)
=
c_r a_{r+1}a_{r+2}v^r+O(v^{r+1}).
}
\]

After converting from \(v=1/(2\tau)\) and from \([X,[X,K]]\) back to \(M\), this predicts

\[
\boxed{
g_r(\tau)
=
C_r\tau^{-(r+3/2)}
+O(\tau^{-(r+5/2)}),}
\]

with

\[
\boxed{
C_r
=
\frac{\sqrt\pi}{2}\,2^{-r}c_r a_{r+1}a_{r+2},
}
\]

or equivalently \((\sqrt\pi/2)2^{-r}c_ra_ra_{r+1}\) under the shifted recurrence convention.

Every displayed factor is strictly positive. Thus the only remaining issue is to prove that the sum term \(S_r(v)\) is one power smaller and cannot cancel the leading term in \(D_r(v)\).

## Graded-orthogonality lemma: remaining symbolic obligation

The exact graded expansion shows that the dangerous contribution to \(S_r(v)\) comes from the lowest parity-allowed grade. The required estimate is:

> **Graded-orthogonality lemma.** For \(k\equiv r\pmod 2\) and \(k\le r\),
> \[
> \langle E(v)m_k,u_{r+2}(v)\rangle
> =O\!\left(v^{(r+2-k)/2}
> \right).
> \]
> In particular,
> \[
> \boxed{
> \langle E(v)m_r,u_{r+2}(v)\rangle=O(v^2).
> }
> \]

The exponent in the general statement records the graded separation between polynomial degree \(k\) and eigenmode \(r+2\). For the load-bearing case \(k=r\), naive counting gives only \(O(v)\); the theorem needs cancellation of the full linear term.

Write

\[
E(v)m_r=m_r-\frac v2X^2m_r+O(v^2),
\]

and

\[
u_{r+2}(v)=p_{r+2}+vq_{r+2}^{(1)}+O(v^2).
\]

Then

\[
\begin{aligned}
\langle E(v)m_r,u_{r+2}(v)\rangle
&=
\langle m_r,p_{r+2}\rangle\\
&\quad+v\left(
\langle m_r,q_{r+2}^{(1)}\rangle
-\frac12\langle X^2m_r,p_{r+2}\rangle
\right)
+O(v^2).
\end{aligned}
\]

The constant term vanishes by degree orthogonality. Therefore the lemma is equivalent to the explicit first-order cancellation identity

\[
\boxed{
\langle m_r,q_{r+2}^{(1)}\rangle
=
\frac12\langle X^2m_r,p_{r+2}\rangle.
}
\]

This is now the single unresolved symbolic line. It should follow either from first-order perturbation of the graded Gram eigenproblem or directly from differentiating the orthogonality relation that defines the flat-limit eigenbasis.

Once this identity is proved, parity and degree counting imply

\[
S_r(v)=O(v^{r+1}),
\]

while

\[
D_r(v)=c_ra_{r+1}a_{r+2}v^r+O(v^{r+1}).
\]

Hence

\[
C_r
=
\frac{\sqrt\pi}{2}\,2^{-r}c_ra_{r+1}a_{r+2}
>0,
\]

so \(g_r\not\equiv0\) for every admissible \(r\). Analyticity then gives a discrete exceptional set \(Z_N\), and the graph lemma completes generic-width local two-shift generation.

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

The width-derivative identity, eigenvector-rotation formula, analyticity reduction, graph deduction, exact graded Gaussian factorization, recurrence selection rule, and positivity formula

\[
c_r=\frac{\|(I-\Pi_{r-1})m_r\|^2}{r!}>0
\]

are established. The candidate leading coefficient is

\[
C_r
=
\frac{\sqrt\pi}{2}\,2^{-r}c_ra_{r+1}a_{r+2},
\]

up to recurrence-index convention. The all-\(N\) theorem is reduced to the first-order graded-orthogonality cancellation

\[
\langle m_r,q_{r+2}^{(1)}\rangle
=
\frac12\langle X^2m_r,p_{r+2}\rangle.
\]

Until that identity is proved symbolically, the generic-width theorem remains conditional.