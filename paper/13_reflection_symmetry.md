# Reflection symmetry, parity sectors, and the finite Weil operator system

## 1. Scope

This chapter records the reflection symmetry of the finite Gaussian-packet Weil model and the resulting parity decomposition of the generalized eigenproblem.

Let the packet centers satisfy

\[
\{c_1,\dots,c_N\}=-\{c_1,\dots,c_N\}.
\]

Because the centers are pairwise distinct, there is a unique involution \(\pi\) such that

\[
c_{\pi(i)}=-c_i.
\]

Let \(J\) be the corresponding permutation matrix,

\[
Je_i=e_{\pi(i)}.
\]

Then

\[
J^T=J,\qquad J^2=I.
\]

The coefficient space decomposes into the even and odd sectors

\[
E_+=\ker(J-I),\qquad E_-=\ker(J+I).
\]

The purpose of this chapter is to prove that the Gram matrix, conductor block, gamma block, paired prime block, and completed-zeta pole block all preserve this decomposition.

## 2. Gram symmetry

For equal-width Gaussian packets,

\[
B_{ij}
=
\sqrt{\pi}\sigma
\exp\left(-\frac{(c_i-c_j)^2}{4\sigma^2}\right).
\]

Under simultaneous reflection of both indices,

\[
\begin{aligned}
B_{\pi(i),\pi(j)}
&=
\sqrt{\pi}\sigma
\exp\left(-\frac{(c_{\pi(i)}-c_{\pi(j)})^2}{4\sigma^2}\right)\\
&=
\sqrt{\pi}\sigma
\exp\left(-\frac{(-c_i+c_j)^2}{4\sigma^2}\right)\\
&=B_{ij}.
\end{aligned}
\]

Hence

\[
J^TBJ=B.
\]

Since \(J^T=J=J^{-1}\),

\[
\boxed{JB=BJ.}
\]

## 3. Conductor symmetry

The conductor contribution is a real scalar multiple of the Gram matrix,

\[
A_{\mathrm{cond}}=\alpha B.
\]

Therefore

\[
\boxed{JA_{\mathrm{cond}}=A_{\mathrm{cond}}J.}
\]

## 4. Gamma symmetry

The gamma entries have the form

\[
(A_\Gamma)_{ij}=K_\Gamma(c_j-c_i),
\]

where

\[
K_\Gamma(\delta)
=
2\sigma^2
\int_0^\infty
\omega_a(t)e^{-(\sigma t)^2}\cos(\delta t)\,dt.
\]

Because cosine is even,

\[
K_\Gamma(-\delta)=K_\Gamma(\delta).
\]

Also,

\[
c_{\pi(j)}-c_{\pi(i)}=-(c_j-c_i).
\]

Thus

\[
(A_\Gamma)_{\pi(i),\pi(j)}=(A_\Gamma)_{ij},
\]

and hence

\[
\boxed{JA_\Gamma=A_\Gamma J.}
\]

## 5. Paired translation symmetry

For a shift \(s\), let

\[
C_s(i,j)
=
\sqrt{\pi}\sigma
\exp\left(-\frac{(c_i-c_j-s)^2}{4\sigma^2}\right).
\]

The paired translation block is

\[
T_s=-(C_s+C_{-s}).
\]

Equivalently,

\[
(T_s)_{ij}=K_s(c_i-c_j),
\]

with

\[
K_s(\delta)
=
-\sqrt{\pi}\sigma
\left[
\exp\left(-\frac{(\delta-s)^2}{4\sigma^2}\right)
+
\exp\left(-\frac{(\delta+s)^2}{4\sigma^2}\right)
\right].
\]

The two summands exchange under \(\delta\mapsto-\delta\), so

\[
K_s(-\delta)=K_s(\delta).
\]

Therefore

\[
(T_s)_{\pi(i),\pi(j)}=(T_s)_{ij},
\]

and

\[
\boxed{JT_s=T_sJ.}
\]

The pairing of \(+s\) and \(-s\) is essential. A one-sided translation matrix does not generally commute with reflection.

## 6. Prime block symmetry

The finite prime block is a real linear combination of paired translation blocks,

\[
A_{\mathrm{prime}}
=
\sum_n \beta_n T_{\log n}.
\]

Since every \(T_{\log n}\) commutes with \(J\),

\[
\boxed{JA_{\mathrm{prime}}=A_{\mathrm{prime}}J.}
\]

## 7. Full no-pole operator

Let

\[
A
=
A_{\mathrm{cond}}+A_\Gamma+A_{\mathrm{prime}}.
\]

Then

\[
\boxed{JA=AJ}
\]

and

\[
\boxed{JB=BJ.}
\]

Consequently, in a parity-adapted basis,

\[
A=
\begin{pmatrix}
A_+&0\\
0&A_-
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
B_+&0\\
0&B_-
\end{pmatrix}.
\]

The generalized eigenproblem

\[
Av=\lambda Bv
\]

splits into two independent problems,

\[
A_+v=\lambda B_+v,
\qquad
A_-v=\lambda B_-v.
\]

## 8. Pole parity decomposition

For the completed-zeta pole vectors,

\[
(p_+)_i=K e^{c_i/2},
\qquad
(p_-)_i=K e^{-c_i/2},
\]

where

\[
K=\sigma\sqrt{2\pi}e^{\sigma^2/8}.
\]

Reflection exchanges them:

\[
Jp_+=p_-,
\qquad
Jp_-=p_+.
\]

Define

\[
p_e=\frac{p_++p_-}{\sqrt2},
\qquad
p_o=\frac{p_+-p_-}{\sqrt2}.
\]

Then

\[
Jp_e=p_e,
\qquad
Jp_o=-p_o.
\]

Thus

\[
p_e\in E_+,
\qquad
p_o\in E_-.
\]

The pole matrix

\[
P=p_-p_+^*+p_+p_-^*
\]

can be rewritten as

\[
\boxed{P=p_ep_e^*-p_op_o^*.}
\]

Therefore

\[
P|_{E_+}=p_ep_e^*\succeq0,
\]

and

\[
P|_{E_-}=-p_op_o^*\preceq0.
\]

Hence the pole block is positive rank at most one on the even sector and negative rank at most one on the odd sector.

## 9. Sectorwise monotonicity

For \(v\in E_+\),

\[
v^*Pv=|p_e^*v|^2\ge0.
\]

Thus

\[
\frac{v^*(A+P)v}{v^*Bv}
\ge
\frac{v^*Av}{v^*Bv}.
\]

By the Courant-Fischer min-max principle on \(E_+\),

\[
\boxed{
\lambda_k^+(A+P,B)
\ge
\lambda_k^+(A,B).
}
\]

For \(v\in E_-\),

\[
v^*Pv=-|p_o^*v|^2\le0.
\]

Therefore

\[
\frac{v^*(A+P)v}{v^*Bv}
\le
\frac{v^*Av}{v^*Bv},
\]

and

\[
\boxed{
\lambda_k^-(A+P,B)
\le
\lambda_k^-(A,B).
}
\]

So every even generalized eigenvalue weakly increases after the pole is added, while every odd generalized eigenvalue weakly decreases.

## 10. Whitening preserves parity

Because \(B>0\) and \(JB=BJ\), every spectral function of \(B\) also commutes with \(J\). In particular,

\[
JB^{-1/2}=B^{-1/2}J.
\]

Hence the whitened matrix

\[
C=B^{-1/2}AB^{-1/2}
\]

and the whitened pole matrix

\[
R=B^{-1/2}PB^{-1/2}
\]

also commute with \(J\). Their restrictions satisfy

\[
R|_{E_+}=u_eu_e^*\succeq0,
\qquad
R|_{E_-}=-u_ou_o^*\preceq0,
\]

where

\[
u_e=B_+^{-1/2}p_e,
\qquad
u_o=B_-^{-1/2}p_o.
\]

Exact whitening therefore preserves the parity theorem.

## 11. Rank-one interlacing consequences

Since the pole restriction has rank at most one on each sector, the even and odd spectra satisfy rank-one interlacing.

For increasingly ordered even eigenvalues,

\[
\lambda_k^+
\le
\mu_k^+
\le
\lambda_{k+1}^+.
\]

For increasingly ordered odd eigenvalues,

\[
\lambda_{k-1}^-
\le
\mu_k^-
\le
\lambda_k^-.
\]

Thus the pole can move at most one even eigenvalue across zero upward and at most one odd eigenvalue across zero downward.

## 12. The finite Weil operator system

Let \(\mathscr S_N\) be the real linear span of the universal reflection-equivariant kernel matrices,

\[
\mathscr S_N
=
\operatorname{span}_{\mathbb R}
\{B,\Gamma_0,\Gamma_1,T_s,P\}.
\]

Every element of \(\mathscr S_N\) is symmetric and commutes with \(J\). Arithmetic data select particular elements of this universal geometric space by choosing scalar coefficients in front of the conductor, gamma, prime, and pole blocks.

The generated unital \(*\)-algebra is

\[
\mathfrak W_N
=
\operatorname{alg}^*(B,\Gamma_0,\Gamma_1,\{T_s\},P,J).
\]

Because every generator commutes with \(J\),

\[
\mathfrak W_N\subseteq\operatorname{Comm}(J).
\]

In a parity-adapted basis,

\[
\operatorname{Comm}(J)
\cong
M_{N_+}(\mathbb C)\oplus M_{N_-}(\mathbb C).
\]

The first structural question is whether

\[
\boxed{
\mathfrak W_N
=
M_{N_+}(\mathbb C)\oplus M_{N_-}(\mathbb C)
}
\]

or whether the common commutant contains additional symmetries beyond \(I\) and \(J\).

## 13. Computational program

The next implementation should:

1. build the reflection matrix \(J\) from a symmetric packet family;
2. verify numerically that \([J,B]\), \([J,A_\Gamma]\), \([J,T_s]\), \([J,A_{\mathrm{prime}}]\), and \([J,P]\) vanish to numerical precision;
3. construct parity-adapted bases and solve the generalized eigenproblem separately on \(E_+\) and \(E_-\);
4. verify the sectorwise monotonicity inequalities after adding the pole;
5. compute the common commutant dimension of selected generators;
6. test whether the commutant is exactly \(\operatorname{span}\{I,J\}\);
7. measure commutator defects between different kernel generators under geometric refinement.

## 14. Limits

This chapter establishes only finite-dimensional reflection symmetry and its consequences. It does not prove that the generated algebra is maximal, does not classify all possible hidden symmetries, and does not establish an infinite-dimensional self-adjoint operator or the Riemann hypothesis.
