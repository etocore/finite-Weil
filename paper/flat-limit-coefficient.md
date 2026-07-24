# The flat-limit chain coefficient: statement and proof

### Closes the remaining generic-width obligation of issue #9

### STATUS: proof draft after line-by-line internal pass; bibliographic hardening and integration into the main chapter remain

## 0. Conventions

Let

\[
x_1<\cdots<x_N
\]

be distinct nodes, invariant under \(x\mapsto -x\), with \(N\ge2\), and put

\[
R:=\max_i|x_i|.
\]

Define

\[
K(v)_{ij}=e^{-v(x_i-x_j)^2/2},\qquad v>0.
\]

The width variables are

\[
\tau=\sigma^2,\qquad v=\frac1{2\tau},
\]

and

\[
A=T_0=-2\sqrt\pi\,\tau^{1/2}K(v).
\]

Let

\[
M=T_0''=\partial_\tau A-\tau^{-1}A,
\]

where the width-derivative identity has been proved earlier in the chapter.

The Gaussian kernel matrix is positive definite and strictly totally positive on distinct ordered nodes. Hence its eigenvalues are positive and simple for every \(v>0\). Write them in decreasing order as

\[
\mu_0(v)>\mu_1(v)>\cdots>\mu_{N-1}(v)>0,
\]

with corresponding real unit eigenvectors \(u_s(v)\). The matrices \(A\) and \(K\) have the same eigenvectors.

Let

\[
m_k=(x_i^k)_{i=1}^N
\]

and let \(p_0,\ldots,p_{N-1}\) be the discrete orthonormal polynomials obtained by Gram-Schmidt from \(m_0,\ldots,m_{N-1}\) in the Euclidean inner product. Put

\[
\gamma_s:=\|(I-\Pi_{s-1})m_s\|>0,
\qquad
p_s=\frac{(I-\Pi_{s-1})m_s}{\gamma_s},
\qquad
c_s:=\frac{\gamma_s^2}{s!}.
\]

Here \(\Pi_{s-1}\) denotes orthogonal projection onto \(\operatorname{span}\{m_0,\ldots,m_{s-1}\}\), with the empty-span convention at \(s=0\).

For sufficiently small \(v\), Lemma D below gives \(u_s(v)=p_s+O(v)\). In that regime we choose the sign by

\[
\langle p_s,u_s(v)\rangle>0.
\]

This is only a flat-limit gauge. Global statements use gauge-invariant quantities such as \(g_r^2\).

Because the node set is symmetric, the three-term recurrence has no diagonal term:

\[
Xp_s=a_{s+1}p_{s+1}+a_sp_{s-1}.
\]

Comparing leading coefficients gives

\[
a_s=\frac{\gamma_s}{\gamma_{s-1}}>0.
\]

Therefore

\[
\langle p_r,X^2p_{r+2}\rangle
=
\langle Xp_r,Xp_{r+2}\rangle
=
a_{r+1}a_{r+2}>0.
\]

## 1. Theorem

For every \(0\le r\le N-3\), define

\[
g_r(\tau):=\langle u_r,M u_{r+2}\rangle.
\]

Then, in the flat-limit gauge above, as \(\tau\to\infty\),

\[
\boxed{
 g_r(\tau)
 =-C_r\,\tau^{-(r+3/2)}\bigl(1+O(\tau^{-1})\bigr)
}
\]

with

\[
\boxed{
C_r
=
\frac{\sqrt\pi}{2}\,2^{-r}c_ra_{r+1}a_{r+2}>0.
}
\]

Consequently \(g_r\not\equiv0\). Since the spectrum is simple for every \(\tau>0\), the rank-one spectral projections are real analytic, and therefore \(g_r^2\) is real analytic on \((0,\infty)\). Its zero set is discrete. Thus

\[
Z_N:=\bigcup_{r=0}^{N-3}\{\tau>0:g_r(\tau)=0\}
\]

is discrete.

For every \(\tau\notin Z_N\), there is \(\varepsilon>0\) such that for every \(0<|t|<\varepsilon\), both parity-chain graphs are connected. Hence, by the graph lemma and the bicommutant theorem,

\[
\operatorname{Comm}(T_0,T_t)=\operatorname{span}\{I,J\},
\]

and

\[
\operatorname{alg}^*(T_0,T_t)
=
M_{N_+}(\mathbf C)\oplus M_{N_-}(\mathbf C).
\]

No uniform-spacing, overlap, or genericity-in-nodes hypothesis is used beyond distinctness and reflection symmetry. Genericity remains only in the width parameter through the discrete exceptional set \(Z_N\).

## 2. Lemma A: Mercer frame and derivative identity

Let

\[
E(v)=\operatorname{diag}(e^{-vx_i^2/2}),
\qquad
w_k:=E(v)m_k.
\]

Then

\[
\boxed{
K(v)=\sum_{k\ge0}\frac{v^k}{k!}w_kw_k^{\mathsf T}.
}
\]

Indeed,

\[
e^{-v(x_i-x_j)^2/2}
=e^{-vx_i^2/2}e^{-vx_j^2/2}e^{vx_ix_j},
\]

and one expands the last factor.

Differentiating gives the exact identity

\[
\partial_vK
=
\sum_{k\ge1}\frac{v^{k-1}}{(k-1)!}w_kw_k^{\mathsf T}
-rac12(X^2K+KX^2).
\tag{A.1}
\]

Since

\[
\frac{dv}{d\tau}=-2v^2
\]

and the off-diagonal matrix element of \(K\) between distinct eigenvectors vanishes, one obtains

\[
\boxed{
 g_r
 =4\sqrt\pi\,\tau^{1/2}v^2
 \left[
 S_r-rac12(\mu_r+\mu_{r+2})
 \langle u_r,X^2u_{r+2}\rangle
 \right],
}
\tag{A.2}
\]

where

\[
S_r
:=
\sum_{k\ge1}\frac{v^{k-1}}{(k-1)!}
\langle u_r,w_k\rangle
\langle w_k,u_{r+2}\rangle.
\]

## 3. Lemma B: tail/Weyl upper bound

For \(0<v\le1\) and every \(0\le s\le N-1\),

\[
\boxed{
\mu_s(v)
\le
\sum_{k\ge s}\frac{v^k}{k!}\|w_k\|^2
\le
\frac{NR^{2s}}{s!}e^{R^2}v^s.
}
\]

### Proof

Split

\[
K=K_{<s}+K_{\ge s}
\]

by frame index. Since \(\operatorname{rank}K_{<s}\le s\), its \(s\)-th eigenvalue in decreasing order is zero. Weyl's inequality gives

\[
\mu_s(K)\le\|K_{\ge s}\|.
\]

The frame terms are positive semidefinite, so

\[
\|K_{\ge s}\|
\le
\sum_{k\ge s}\frac{v^k}{k!}\|w_k\|^2.
\]

Because \(\|w_k\|\le\|m_k\|\le\sqrt N R^k\),

\[
\sum_{k\ge s}\frac{v^k}{k!}\|w_k\|^2
\le
NR^{2s}v^s
\sum_{j\ge0}\frac{R^{2j}}{(s+j)!}
\le
\frac{NR^{2s}}{s!}e^{R^2}v^s.
\]

This proves the claim. \(\square\)

## 4. Lemma C: graded frame-component bound

Fix \(0\le s\le N-1\), set

\[
u=u_s(v),\qquad \mu=\mu_s(v),\qquad
\theta_k:=\langle w_k,u\rangle.
\]

Then for every \(0\le k<s\),

\[
\boxed{
\theta_k=O(v^{s-k})
\qquad(v\downarrow0).
}
\]

The implied constant depends only on the nodes and on \(s\).

### Proof

Pairing \(Ku=\mu u\) with \(w_\ell\) gives the exact frame equations

\[
\mu\theta_\ell
=
\sum_{k\ge0}\frac{v^k}{k!}W_{\ell k}(v)\theta_k,
\qquad
W_{\ell k}(v):=\langle w_\ell,w_k\rangle.
\]

Let

\[
S=\{0,\ldots,s-1\},
\qquad
D_S(v)=\operatorname{diag}\left(\frac{v^k}{k!}\right)_{k<s},
\]

and write \(\Theta_S=(\theta_k)_{k<s}\). Restricting to \(\ell<s\) and moving the tail to the right gives

\[
W_S(v)D_S(v)\Theta_S=\rho,
\]

where

\[
\rho_\ell
=
\mu\theta_\ell
-
\sum_{k\ge s}\frac{v^k}{k!}W_{\ell k}(v)\theta_k.
\]

By Lemma B, \(\mu=O(v^s)\). Also

\[
|\theta_k|\le\|w_k\|,
\qquad
|W_{\ell k}|\le\|w_\ell\|\|w_k\|,
\]

so, for each fixed \(\ell<s\),

\[
\sum_{k\ge s}\frac{v^k}{k!}|W_{\ell k}\theta_k|
\le
\|w_\ell\|
\sum_{k\ge s}\frac{v^k}{k!}\|w_k\|^2
=O(v^s).
\]

Hence

\[
\rho=O(v^s).
\]

At \(v=0\),

\[
W_S(0)=\bigl[\langle m_\ell,m_k\rangle\bigr]_{\ell,k<s}
\]

is the moment Gram matrix of \(m_0,\ldots,m_{s-1}\). These vectors are linearly independent because the nodes are distinct and the corresponding Vandermonde matrix has full column rank. Thus \(W_S(0)\) is positive definite. Since \(W_S(v)=W_S(0)+O(v)\), its inverse is uniformly bounded for sufficiently small \(v\).

Therefore

\[
D_S(v)\Theta_S=W_S(v)^{-1}\rho=O(v^s).
\]

Componentwise,

\[
\frac{v^k}{k!}\theta_k=O(v^s),
\]

which is equivalent to

\[
\theta_k=O(v^{s-k}).
\]

For \(s=0\) the statement is vacuous. \(\square\)

In particular, taking \(s=r+2\) and \(k=r\),

\[
\boxed{
\langle E(v)m_r,u_{r+2}(v)\rangle=O(v^2).
}
\]

This is the previously missing graded cancellation. It follows directly from the exact frame system and does not require nondegenerate perturbation theory at the rank-one matrix \(K(0)\).

## 5. Lemma D: leading eigenvalue and eigenvector asymptotics

For every \(0\le s\le N-1\),

\[
\boxed{
\mu_s(v)=c_sv^s(1+O(v)),
}
\tag{D.1}
\]

and, in the flat-limit gauge,

\[
\boxed{
 u_s(v)=p_s+O(v).
}
\tag{D.2}
\]

### Proof of (D.1)

Let

\[
\sigma_k=e_k(\mu_0,\ldots,\mu_{N-1})
=
\sum_{|I|=k}\det K_I,
\]

where \(K_I\) denotes the principal minor indexed by \(I\).

Apply Cauchy-Binet to the frame factorization, first to a finite truncation and then pass to the limit using absolute convergence. For a fixed \(k\)-element node set \(I\),

\[
\det K_I
=
\sum_{T\subset\mathbf Z_{\ge0},\ |T|=k}
\left(\prod_{t\in T}\frac{v^t}{t!}\right)
\det([x_i^t]_{i\in I,t\in T})^2
\left(\prod_{i\in I}e^{-vx_i^2}\right).
\]

The unique set of distinct nonnegative integers with minimal sum is

\[
T_0=\{0,1,\ldots,k-1\},
\]

whose exponent is \(k(k-1)/2\). Every other admissible \(T\) has total degree at least one larger. The corresponding determinant is a nonzero Vandermonde determinant.

Summing the leading coefficient over \(I\) and applying Cauchy-Binet in reverse gives

\[
\sum_{|I|=k}
\det([x_i^t]_{i\in I,\ 0\le t<k})^2
=
\det\bigl[\langle m_\ell,m_j\rangle\bigr]_{\ell,j<k}
=
\prod_{j<k}\gamma_j^2.
\]

Since \(\prod_{t=0}^{k-1}t!\) is the factorial denominator, it follows that

\[
\boxed{
\sigma_k
=
v^{k(k-1)/2}
\left(\prod_{j<k}c_j\right)
(1+O(v)).
}
\tag{D.3}
\]

Let

\[
P_k:=\mu_0\mu_1\cdots\mu_{k-1}.
\]

Positivity and monotone ordering imply

\[
P_k\le\sigma_k\le {N\choose k}P_k.
\]

Combining this with (D.3) gives

\[
P_k=\Theta\bigl(v^{k(k-1)/2}\bigr).
\]

Hence

\[
\mu_j=\frac{P_{j+1}}{P_j}=\Theta(v^j),
\]

and therefore

\[
\frac{\mu_j}{\mu_{j-1}}=O(v)
\qquad(j\ge1).
\]

Every term in \(\sigma_k-P_k\) contains at least one replacement of an eigenvalue among \(\mu_0,\ldots,\mu_{k-1}\) by an eigenvalue no larger than \(\mu_k\). Thus

\[
\sigma_k=P_k(1+O(v)).
\]

Using (D.3),

\[
P_k
=
v^{k(k-1)/2}
\left(\prod_{j<k}c_j\right)
(1+O(v)).
\]

Taking the quotient \(P_{s+1}/P_s\) gives

\[
\mu_s(v)=c_sv^s(1+O(v)).
\]

### Proof of (D.2)

Return to the lower-block equation from Lemma C. Write

\[
d_k:=\frac{v^k}{k!}\theta_k.
\]

For \(\ell<s\), Lemma C and (D.1) give

\[
\mu\theta_\ell
=O(v^{2s-\ell})=O(v^{s+1}).
\]

The tail with \(k\ge s+1\) is also \(O(v^{s+1})\). Keeping the \(k=s\) term therefore yields

\[
W_S(v)d_{<s}
=-d_s h(v)+O(v^{s+1}),
\]

where

\[
h(v)=\bigl(W_{\ell s}(v)\bigr)_{\ell<s}.
\]

Since \(W_S(v)^{-1}=W_S(0)^{-1}+O(v)\) and \(h(v)=h(0)+O(v)\),

\[
d_{<s}
=-d_s\beta+O(v^{s+1}),
\qquad
\beta:=W_S(0)^{-1}h(0).
\tag{D.4}
\]

The normal equations show that \(\beta\) is exactly the monomial-coordinate vector of the orthogonal projection of \(m_s\) onto \(\operatorname{span}\{m_0,\ldots,m_{s-1}\}\):

\[
\Pi_{s-1}m_s=\sum_{k<s}\beta_km_k.
\]

Now reconstruct the eigenvalue equation through the frame:

\[
\mu u
=
Ku
=
\sum_{k\ge0}d_kw_k.
\]

Using (D.4), \(w_k=m_k+O(v)\), the fact that every \(d_k\) with \(k<s\) is \(O(v^s)\), and the exponential tail estimate for \(k\ge s+1\), one gets

\[
\sum_{k<s}d_kw_k
=-d_s\Pi_{s-1}m_s+O(v^{s+1}),
\]

\[
d_sw_s=d_sm_s+O(v^{s+1}),
\]

and

\[
\sum_{k\ge s+1}d_kw_k=O(v^{s+1}).
\]

Therefore

\[
\mu u
=d_s(m_s-\Pi_{s-1}m_s)+O(v^{s+1})
=d_s\gamma_sp_s+O(v^{s+1}).
\]

Since \(\mu\asymp v^s\), division gives

\[
u=\alpha_s(v)p_s+O(v)
\]

for some real scalar \(\alpha_s(v)\). Unit norm gives \(|\alpha_s(v)|=1+O(v)\), and the flat-limit gauge gives \(\alpha_s(v)>0\) for sufficiently small \(v\). Hence

\[
u_s(v)=p_s+O(v).
\]

This proves (D.2). \(\square\)

### Parity corollary

Since \(K(v)\) commutes with reflection and has simple spectrum, each eigenvector has definite reflection parity. By (D.2), for sufficiently small \(v\) that parity equals the parity of \(p_s\), namely \((-1)^s\). Simplicity prevents a parity change as \(v\) varies, so this parity assignment holds for every \(v>0\).

## 6. Proof of the theorem

We first prove

\[
\boxed{S_r(v)=O(v^{r+1}).}
\]

For \(1\le k\le r\), Lemma C applied to \(u_r\) and \(u_{r+2}\) gives

\[
\langle u_r,w_k\rangle=O(v^{r-k}),
\qquad
\langle w_k,u_{r+2}\rangle=O(v^{r+2-k}),
\]

so the \(k\)-th summand is

\[
O\bigl(v^{k-1+r-k+r+2-k}\bigr)
=O(v^{2r+1-k})
=O(v^{r+1}).
\]

For \(k=r+1\), the second factor is \(O(v)\) by Lemma C and the first is bounded, so the contribution is \(O(v^{r+1})\). For \(k=r+2\), both factors are bounded and the coefficient is \(O(v^{r+1})\). Finally,

\[
\sum_{k\ge r+3}\frac{v^{k-1}}{(k-1)!}
|\langle u_r,w_k\rangle|
|\langle w_k,u_{r+2}\rangle|
\le
\sum_{k\ge r+3}\frac{v^{k-1}}{(k-1)!}\|w_k\|^2
=O(v^{r+2}).
\]

The same argument covers \(r=0\), with the first range empty. Thus \(S_r=O(v^{r+1})\).

Next, Lemma D gives

\[
\langle u_r,X^2u_{r+2}\rangle
=
a_{r+1}a_{r+2}+O(v),
\]

and

\[
\frac12(\mu_r+\mu_{r+2})
=
\frac{c_r}{2}v^r(1+O(v)),
\]

because \(\mu_{r+2}=O(v^{r+2})\). Substituting into (A.2),

\[
\begin{aligned}
g_r
&=
4\sqrt\pi\,\tau^{1/2}v^2
\left[
-\frac{c_r}{2}a_{r+1}a_{r+2}v^r
+O(v^{r+1})
\right]\\
&=
-2\sqrt\pi\,c_ra_{r+1}a_{r+2}
\tau^{1/2}v^{r+2}
\bigl(1+O(v)\bigr).
\end{aligned}
\]

Using \(v=(2\tau)^{-1}\),

\[
\tau^{1/2}v^{r+2}
=
2^{-(r+2)}\tau^{-(r+3/2)},
\]

so

\[
g_r(\tau)
=
-\frac{\sqrt\pi}{2}\,2^{-r}
 c_ra_{r+1}a_{r+2}
\tau^{-(r+3/2)}
\bigl(1+O(\tau^{-1})\bigr).
\]

Every factor in the coefficient is positive. Therefore \(g_r\not\equiv0\).

The analytic-zero statement follows from analyticity of the simple spectral projections. For the two-shift consequence, reflection covariance gives

\[
JT_tJ=T_{-t}.
\]

Hence the matrix element between same-parity vectors is an even function of \(t\), and

\[
\langle u_r,T_tu_{r+2}\rangle
=
\frac{t^2}{2}g_r+O(t^4).
\]

For fixed \(\tau\notin Z_N\), finitely many nonzero chain coefficients admit one common \(\varepsilon>0\). The parity chains therefore remain connected for every \(0<|t|<\varepsilon\), and the graph lemma and bicommutant theorem give the asserted commutant and generated algebra. \(\square\)

## 7. Referee notes and verification status

The load-bearing proof is the exact lower-frame system in Lemma C. It proves

\[
\langle E(v)m_r,u_{r+2}(v)\rangle=O(v^2)
\]

without a first-order Kato expansion at the degenerate rank-one limit \(K(0)\).

Three corrections were incorporated during the line-by-line pass:

1. The parity assignment \((-1)^s\) is derived after the eigenvector limit, avoiding circular use of the flat-limit statement inside Lemma C.
2. The reconstruction tail in Lemma D is bounded directly by \(O(v^{s+1})\); Lemma C is not incorrectly applied to indices \(k>s\).
3. The estimate for \(S_r\) is summed explicitly. It does not require parity cancellation at \(k=r+1\).

The numerical ledger previously reported for this argument remains supporting evidence rather than part of the proof: high-precision checks of (A.2), the graded exponent, the projection coefficients, the eigenvalue products, and the final signed coefficient all agree with the asymptotic formulas. Exact bibliography entries and theorem numbers for strict total positivity, oscillation, and analytic spectral projections should be added during final paper integration.
