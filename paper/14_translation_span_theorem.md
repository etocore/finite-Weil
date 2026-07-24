# Paired Gaussian translations span the symmetric Toeplitz operator system

## 1. Scope

This chapter proves a finite-dimensional structural theorem for the paired Gaussian translation matrices used in the finite Weil construction.

The result is independent of arithmetic coefficients, prime sums, gamma factors, and pole terms. It concerns only the universal geometry of equally spaced Gaussian packets.

The theorem proved here is:

> For an equally spaced packet grid, the real linear span of the continuous paired-translation family is exactly the space of real symmetric Toeplitz matrices.

This chapter does **not** yet prove the subsequent commutant theorem. In particular, the identification of the common commutant with `span{I,J}` remains a separate linear-algebra problem.

## 2. Equally spaced packet grid

Fix an integer \(N\ge 1\), spacing \(h>0\), and packet width \(\sigma>0\). Let

\[
c_j=c_0+jh,
\qquad j=0,1,\dots,N-1.
\]

Only center differences enter the paired-translation kernels, so the offset \(c_0\) is irrelevant.

For each real shift \(s\), define the matrix \(T_s\in M_N(\mathbb R)\) by

\[
(T_s)_{ij}
=
\exp\!\left(-\frac{(c_i-c_j-s)^2}{4\sigma^2}\right)
+
\exp\!\left(-\frac{(c_i-c_j+s)^2}{4\sigma^2}\right).
\]

An overall nonzero scalar or a global minus sign does not affect the span theorem, so this normalization is sufficient.

Since

\[
c_i-c_j=(i-j)h,
\]

and the kernel is even in \(i-j\), every \(T_s\) is real symmetric Toeplitz.

## 3. Symmetric Toeplitz basis

For \(k=0,1,\dots,N-1\), define \(H_k\in M_N(\mathbb R)\) by

\[
(H_k)_{ij}
=
\begin{cases}
1,& |i-j|=k,\\
0,& |i-j|\ne k.
\end{cases}
\]

Then \(H_0=I\), and

\[
\mathcal T_N^{\mathrm{sym}}
:=
\{\text{real symmetric Toeplitz }N\times N\text{ matrices}\}
=
\operatorname{span}_{\mathbb R}\{H_0,\dots,H_{N-1}\}.
\]

The matrices \(H_0,\dots,H_{N-1}\) have disjoint diagonal supports and are linearly independent. Hence

\[
\dim \mathcal T_N^{\mathrm{sym}}=N.
\]

For each \(s\), write

\[
T_s=\sum_{k=0}^{N-1}a_k(s)H_k,
\]

where

\[
a_k(s)
=
\exp\!\left(-\frac{(kh-s)^2}{4\sigma^2}\right)
+
\exp\!\left(-\frac{(kh+s)^2}{4\sigma^2}\right).
\]

Completing the square gives

\[
a_k(s)
=
2\exp\!\left(-\frac{s^2}{4\sigma^2}\right)
\exp\!\left(-\frac{k^2h^2}{4\sigma^2}\right)
\cosh\!\left(\frac{khs}{2\sigma^2}\right).
\]

Set

\[
\alpha=\frac{h}{2\sigma^2}>0,
\qquad
\beta_k=\exp\!\left(-\frac{k^2h^2}{4\sigma^2}\right)>0.
\]

Then

\[
a_k(s)=2e^{-s^2/(4\sigma^2)}\beta_k\cosh(k\alpha s).
\]

Thus, up to a common nonzero factor in \(s\) and nonzero coordinate scalings in \(k\), the coefficient family is

\[
1,\cosh(\alpha s),\cosh(2\alpha s),\dots,\cosh((N-1)\alpha s).
\]

## 4. Linear independence lemma

### Lemma

For every \(\alpha>0\), the functions

\[
1,\cosh(\alpha s),\cosh(2\alpha s),\dots,\cosh((N-1)\alpha s)
\]

are linearly independent over \(\mathbb R\) on every interval with nonempty interior.

### Proof

Suppose

\[
\sum_{k=0}^{N-1}d_k\cosh(k\alpha s)=0
\]

for every \(s\) in an interval with nonempty interior.

The left-hand side is real analytic, so it vanishes for every real \(s\).

Let

\[
z=e^{\alpha s}>0.
\]

For \(k\ge 1\),

\[
\cosh(k\alpha s)=\frac{z^k+z^{-k}}{2}.
\]

Therefore

\[
d_0+\frac12\sum_{k=1}^{N-1}d_k(z^k+z^{-k})=0
\]

for every \(z>0\).

Multiplying by \(2z^{N-1}\) gives the polynomial identity

\[
2d_0z^{N-1}
+
\sum_{k=1}^{N-1}d_k
\left(z^{N-1+k}+z^{N-1-k}\right)
=0
\]

for every \(z>0\).

A polynomial vanishing on an infinite set is identically zero. Its highest-degree term is

\[
d_{N-1}z^{2N-2},
\]

so \(d_{N-1}=0\). Repeating downward gives

\[
d_{N-2}=\cdots=d_1=0,
\]

and then the remaining coefficient gives \(d_0=0\).

Hence all coefficients vanish, proving linear independence. \(\square\)

## 5. Span theorem

### Theorem

Let \(T_s\) be the paired Gaussian translation matrices defined above on an equally spaced grid. Then

\[
\boxed{
\operatorname{span}_{\mathbb R}\{T_s:s\in\mathbb R\}
=
\mathcal T_N^{\mathrm{sym}}.
}
\]

The same conclusion holds if \(s\) is restricted to any interval with nonempty interior, including \([0,\infty)\).

### Proof

Every \(T_s\) is symmetric Toeplitz, so

\[
\operatorname{span}_{\mathbb R}\{T_s:s\in\mathbb R\}
\subseteq
\mathcal T_N^{\mathrm{sym}}.
\]

It remains to prove the reverse inclusion.

Let

\[
v(s)=\big(a_0(s),a_1(s),\dots,a_{N-1}(s)\big)\in\mathbb R^N
\]

be the coefficient vector of \(T_s\) in the basis \(H_0,\dots,H_{N-1}\).

Assume that the linear span of \(\{v(s):s\in I\}\) is a proper subspace of \(\mathbb R^N\), where \(I\) is any interval with nonempty interior. Then there exists a nonzero vector \(q=(q_0,\dots,q_{N-1})\) such that

\[
\sum_{k=0}^{N-1}q_ka_k(s)=0
\]

for every \(s\in I\).

Using

\[
a_k(s)=2e^{-s^2/(4\sigma^2)}\beta_k\cosh(k\alpha s),
\]

and dividing by the common nonzero factor \(2e^{-s^2/(4\sigma^2)}\), we obtain

\[
\sum_{k=0}^{N-1}(q_k\beta_k)\cosh(k\alpha s)=0
\]

for every \(s\in I\).

By the linear independence lemma,

\[
q_k\beta_k=0
\]

for every \(k\). Since every \(\beta_k>0\), it follows that \(q_k=0\) for every \(k\), contradicting the choice of \(q\ne0\).

Therefore

\[
\operatorname{span}\{v(s):s\in I\}=\mathbb R^N.
\]

Since the coordinate map

\[
(x_0,\dots,x_{N-1})
\longmapsto
\sum_{k=0}^{N-1}x_kH_k
\]

is an isomorphism from \(\mathbb R^N\) onto \(\mathcal T_N^{\mathrm{sym}}\), the matrices \(T_s\) span all of \(\mathcal T_N^{\mathrm{sym}}\). \(\square\)

## 6. Finite sampling corollary

### Corollary

There exist shifts

\[
s_0,\dots,s_{N-1}
\]

in any interval with nonempty interior such that

\[
T_{s_0},\dots,T_{s_{N-1}}
\]

form a basis of \(\mathcal T_N^{\mathrm{sym}}\).

### Proof

The coefficient vectors \(v(s)\) span \(\mathbb R^N\). Therefore one may select \(N\) of them that form a basis. Their corresponding matrices form a basis of the symmetric Toeplitz space. \(\square\)

Equivalently, for suitable shifts the sampling matrix

\[
M_{rk}=a_k(s_r)
\]

has nonzero determinant.

Because this determinant is a real-analytic function of the sample tuple \((s_0,\dots,s_{N-1})\) and is not identically zero, the set of tuples for which it vanishes has empty interior and Lebesgue measure zero. Thus a generic choice of \(N\) continuous shifts yields a basis.

## 7. Consequence for commutants

For any matrix \(X\in M_N(\mathbb C)\), the following are equivalent:

1. \(XT_s=T_sX\) for every real \(s\);
2. \(XT_s=T_sX\) for every \(s\) in one interval with nonempty interior;
3. \(XH_k=H_kX\) for every \(k=0,\dots,N-1\);
4. \(X\) commutes with every real symmetric Toeplitz matrix.

Indeed, the theorem identifies the real spans of the two matrix families, and commutation is linear in the second argument.

Therefore the continuous Gaussian problem has now been reduced completely to the finite linear-algebra problem

\[
\boxed{
(\mathcal T_N^{\mathrm{sym}})'
\stackrel{?}{=}
\operatorname{span}_{\mathbb C}\{I,J\}.
}
\]

That equality is not proved in this chapter.

## 8. Limits and next step

The equally spaced hypothesis is essential to the Toeplitz formulation. For a nonuniform symmetric packet set, the matrices remain reflection invariant but are not generally Toeplitz.

The theorem uses the full continuous shift family, or any shift set containing an interval. It does not imply that the finite arithmetic shift set

\[
\{\log(p^m)\}
\]

spans the symmetric Toeplitz space at a fixed prime cutoff. That is a separate sampling and rank question.

The next rigorous step is to determine the common commutant of the basis matrices \(H_0,\dots,H_{N-1}\), and in particular to prove or disprove

\[
(\mathcal T_N^{\mathrm{sym}})'
=
\operatorname{span}_{\mathbb C}\{I,J\}.
\]
