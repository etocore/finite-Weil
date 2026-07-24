# Exact frame-Schur proof of graded orthogonality

## Setup

Let

\[
K(v)=\sum_{k=0}^{N-1} d_k(v)\,w_k(v)w_k(v)^{\mathsf T},
\qquad
d_k(v):=\frac{v^k}{k!},
\qquad
w_k(v):=E(v)m_k,
\]

where

\[
E(v)=e^{-vX^2/2},
\qquad
m_k=(x_1^k,\ldots,x_N^k)^{\mathsf T},
\]

and the nodes \(x_1,\ldots,x_N\) are distinct. Let the eigenvalues be ordered

\[
\mu_0(v)\ge \mu_1(v)\ge\cdots\ge\mu_{N-1}(v)>0,
\]

and choose normalized eigenvectors

\[
K(v)u_s(v)=\mu_s(v)u_s(v).
\]

Define the frame coefficients

\[
\theta_k(v):=\langle w_k(v),u_s(v)\rangle
\]

and the frame Gram matrix

\[
W_{\ell k}(v):=\langle w_\ell(v),w_k(v)\rangle.
\]

The purpose of this note is to prove, for every \(k<s\),

\[
\boxed{\theta_k(v)=O\!\left(v^{s-k}\right).}
\]

In particular, with \(s=r+2\) and \(k=r\),

\[
\boxed{\langle E(v)m_r,u_{r+2}(v)\rangle=O(v^2).}
\]

This is the graded-orthogonality estimate needed in the flat-limit chain argument.

## 1. Exact frame equations

Taking the inner product of the eigenvalue equation with \(w_\ell(v)\) gives, for every \(\ell\),

\[
\boxed{
\mu_s(v)\theta_\ell(v)
=
\sum_{k=0}^{N-1}d_k(v)W_{\ell k}(v)\theta_k(v).
}
\]

No approximation has been used.

## 2. Two-sided eigenvalue scale

Write

\[
K_{<s}(v):=\sum_{k=0}^{s-1}d_k(v)w_k(v)w_k(v)^{\mathsf T},
\qquad
K_{\ge s}(v):=\sum_{k=s}^{N-1}d_k(v)w_k(v)w_k(v)^{\mathsf T}.
\]

Since \(\operatorname{rank}K_{<s}\le s\), the min-max principle gives

\[
\mu_s(v)\le \|K_{\ge s}(v)\|.
\]

The vectors \(w_k(v)\) remain bounded as \(v\to0\), hence

\[
\|K_{\ge s}(v)\|
\le
\sum_{k=s}^{N-1}d_k(v)\|w_k(v)\|^2
=O(v^s).
\]

Therefore

\[
\mu_s(v)=O(v^s).
\]

For the matching lower bound, let

\[
K_{\le s}(v):=\sum_{k=0}^{s}d_k(v)w_k(v)w_k(v)^{\mathsf T}.
\]

Because the nodes are distinct, \(m_0,\ldots,m_s\) are linearly independent. Since \(E(v)\) is invertible, \(w_0(v),\ldots,w_s(v)\) are also linearly independent. Their synthesis matrix

\[
B_s(v):=[w_0(v)\ \cdots\ w_s(v)]
\]

has smallest singular value bounded below for sufficiently small \(v\). Thus

\[
K_{\le s}(v)=B_s(v)D_s(v)B_s(v)^{\mathsf T},
\]

where

\[
D_s(v)=\operatorname{diag}(d_0(v),\ldots,d_s(v)).
\]

Its smallest nonzero eigenvalue satisfies

\[
\lambda_s(K_{\le s}(v))
\ge
\sigma_{\min}(B_s(v))^2\min_{0\le k\le s}d_k(v)
\ge c_sv^s
\]

for small \(v\). Since \(K(v)\succeq K_{\le s}(v)\), the min-max principle yields

\[
\mu_s(v)\ge c_sv^s.
\]

Hence

\[
\boxed{\mu_s(v)\asymp v^s.}
\]

## 3. Schur solve for the lower frame coefficients

Fix \(s\), and restrict the exact frame equations to \(0\le\ell<s\). Set

\[
M_s(v):=(W_{\ell k}(v))_{0\le\ell,k<s},
\qquad
D_{<s}(v):=\operatorname{diag}(d_0(v),\ldots,d_{s-1}(v)),
\]

and

\[
\Theta_{<s}(v):=(\theta_0(v),\ldots,\theta_{s-1}(v))^{\mathsf T}.
\]

Then

\[
M_s(v)D_{<s}(v)\Theta_{<s}(v)=R_s(v),
\]

where the \(\ell\)-th component of \(R_s(v)\) is

\[
R_{s,\ell}(v)
=
\mu_s(v)\theta_\ell(v)
-
\sum_{k=s}^{N-1}d_k(v)W_{\ell k}(v)\theta_k(v).
\]

Because \(u_s(v)\) is normalized and the \(w_k(v)\) are bounded,

\[
\theta_k(v)=O(1)
\]

uniformly in \(k\). Together with \(\mu_s(v)=O(v^s)\), this gives

\[
R_s(v)=O(v^s).
\]

Moreover,

\[
M_s(v)\longrightarrow M_s(0)
=
(\langle m_\ell,m_k\rangle)_{0\le\ell,k<s}.
\]

The limiting matrix is the Gram matrix of the linearly independent vectors \(m_0,\ldots,m_{s-1}\), hence it is positive definite. Therefore \(M_s(v)^{-1}\) is uniformly bounded for sufficiently small \(v\). Consequently,

\[
D_{<s}(v)\Theta_{<s}(v)
=
M_s(v)^{-1}R_s(v)
=O(v^s).
\]

The \(k\)-th component is

\[
\frac{v^k}{k!}\theta_k(v)=O(v^s),
\]

so

\[
\boxed{
\theta_k(v)=O\!\left(v^{s-k}\right),
\qquad 0\le k<s.
}
\]

Taking \(s=r+2\) and \(k=r\) proves

\[
\boxed{
\langle E(v)m_r,u_{r+2}(v)\rangle=O(v^2).
}
\]

Thus the formerly mysterious first-order cancellation is not an independent perturbation identity. It is one component of the exact lower-frame Schur estimate.

## 4. Identification of the flat-limit eigenvector

Let

\[
\mathcal P_{s-1}:=\operatorname{span}\{m_0,\ldots,m_{s-1}\}.
\]

The estimate above implies

\[
\theta_k(v)\to0,
\qquad k<s.
\]

Hence every accumulation point \(u_*\) of \(u_s(v)\) as \(v\to0\) is orthogonal to \(\mathcal P_{s-1}\).

Use the exact reconstruction formula

\[
\mu_s(v)u_s(v)
=
\sum_{k=0}^{N-1}d_k(v)\theta_k(v)w_k(v).
\]

Since \(\mu_s(v)\asymp v^s\), the terms with \(k>s\) are \(O(v^{s+1})\), while the terms with \(k\le s\) lie in a space converging to \(\operatorname{span}\{m_0,\ldots,m_s\}\). Therefore every accumulation point also belongs to \(\operatorname{span}\{m_0,\ldots,m_s\}\).

The intersection

\[
\operatorname{span}\{m_0,\ldots,m_s\}
\cap
\mathcal P_{s-1}^{\perp}
\]

is one-dimensional and is spanned by the normalized Gram-Schmidt residual

\[
p_s:=\frac{q_s}{\gamma_s},
\qquad
q_s:=(I-\Pi_{s-1})m_s,
\qquad
\gamma_s:=\|q_s\|>0.
\]

After fixing the eigenvector sign by \(\langle u_s(v),p_s\rangle>0\),

\[
\boxed{u_s(v)\to p_s.}
\]

In particular,

\[
\theta_s(v)=\langle w_s(v),u_s(v)\rangle\to\langle m_s,p_s\rangle=\gamma_s.
\]

## 5. Leading Schur coefficient and Gram-Schmidt projection

Let

\[
h_s:=(\langle m_0,m_s\rangle,\ldots,\langle m_{s-1},m_s\rangle)^{\mathsf T}
\]

and

\[
G_s:=M_s(0)
=(\langle m_\ell,m_k\rangle)_{0\le\ell,k<s}.
\]

From the lower frame system,

\[
M_s(v)D_{<s}(v)\Theta_{<s}(v)
=
\mu_s(v)\Theta_{<s}(v)
-
\sum_{k=s}^{N-1}d_k(v)W_{<s,k}(v)\theta_k(v).
\]

The first term on the right is \(o(v^s)\), because

\[
\mu_s(v)\theta_\ell(v)
=O(v^s)O(v^{s-\ell})
=o(v^s)
\]

for every \(\ell<s\). The terms with \(k>s\) are also \(o(v^s)\). The sole leading tail term is \(k=s\), and therefore

\[
D_{<s}(v)\Theta_{<s}(v)
=
-\frac{\gamma_s}{s!}v^sG_s^{-1}h_s+o(v^s).
\]

The vector

\[
a_s:=G_s^{-1}h_s
\]

is exactly the coefficient vector of the orthogonal projection of \(m_s\) onto \(\mathcal P_{s-1}\), because the normal equations for

\[
\Pi_{s-1}m_s=\sum_{k=0}^{s-1}(a_s)_km_k
\]

are

\[
G_sa_s=h_s.
\]

Thus the lower-frame coefficients are forced, at leading order, to reconstruct minus the Gram-Schmidt projection.

Substituting into the eigenvector reconstruction gives

\[
\mu_s(v)u_s(v)
=
\frac{\gamma_s}{s!}v^s
\left(
 m_s-\Pi_{s-1}m_s
\right)
+o(v^s).
\]

Since

\[
m_s-\Pi_{s-1}m_s=q_s=\gamma_sp_s
\]

and \(u_s(v)\to p_s\), comparison along \(p_s\) yields

\[
\boxed{
\mu_s(v)
=
\frac{\gamma_s^2}{s!}v^s+o(v^s).
}
\]

Therefore

\[
\boxed{
c_s=\frac{\gamma_s^2}{s!}>0.}
\]

This derives both the flat-limit eigenvector and eigenvalue coefficient from the same exact frame system.

## 6. Consequence for the chain coefficient

For \(s=r+2\), the graded estimate gives

\[
\langle E(v)m_r,u_{r+2}(v)\rangle=O(v^2).
\]

Hence the potentially dangerous grade-\(r\) contribution to the sum term in the exact double-commutator decomposition is one power smaller than naive counting predicts. Degree and parity counting then give

\[
S_r(v)=O(v^{r+1}).
\]

Meanwhile,

\[
D_r(v)
=
\mu_r(v)\langle u_r(v),X^2u_{r+2}(v)\rangle
+O(v^{r+2}),
\]

and

\[
\mu_r(v)=c_rv^r+O(v^{r+1}),
\qquad
\langle u_r(v),X^2u_{r+2}(v)\rangle
\to
\langle p_r,x^2p_{r+2}\rangle
=a_{r+1}a_{r+2}>0.
\]

Therefore

\[
D_r(v)
=
c_ra_{r+1}a_{r+2}v^r+O(v^{r+1}),
\]

with strictly positive leading coefficient. After conversion from \(v=1/(2\tau)\) to the original width variable, the chain coupling has the form

\[
g_r(\tau)
=
C_r\tau^{-(r+3/2)}
+O(\tau^{-(r+5/2)}),
\]

where

\[
\boxed{
C_r
=
\frac{\sqrt\pi}{2}\,2^{-r}c_ra_{r+1}a_{r+2}>0.
}
\]

Thus \(g_r\not\equiv0\) for every admissible \(r\). Combined with analyticity, this gives a discrete exceptional set of widths and completes the generic-width parity-chain argument.

## Referee note

The proof uses no nondegenerate Kato expansion at \(v=0\). That would be invalid because \(K(0)\) has rank one and the zero eigenvalue is highly degenerate. The grading is handled directly through the exact frame equations, a finite positive-definite moment Gram matrix, and min-max estimates.