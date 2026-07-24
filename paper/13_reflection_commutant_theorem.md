# The reflection commutant theorem for uniform Gaussian packet grids

## 1. Scope

This chapter proves the common-commutant statement for the paired Gaussian translation family on an equally spaced symmetric packet grid. The result is exact and finite-dimensional.

Let

\[
c_j=h\left(j-\frac{N+1}{2}\right),\qquad j=1,\dots,N,
\]

with spacing \(h>0\), and let \(J\) be the reversal matrix

\[
Je_j=e_{N+1-j}.
\]

For \(s\ge 0\), define the paired Gaussian translation matrix

\[
(T_s)_{ij}
=
-\sqrt\pi\,\sigma
\left[
\exp\left(-\frac{(c_i-c_j-s)^2}{4\sigma^2}\right)
+
\exp\left(-\frac{(c_i-c_j+s)^2}{4\sigma^2}\right)
\right].
\]

The main theorem is

\[
\boxed{
\{T_s:s\ge 0\}'=\operatorname{span}_{\mathbb C}\{I,J\}.
}
\]

Consequently, any larger universal finite Weil family containing all \(T_s\) and commuting with reflection has the same common commutant, and the unital \(*\)-algebra it generates is the full parity-preserving matrix algebra.

## 2. Symmetric Toeplitz basis

For \(k=0,\dots,N-1\), define

\[
(H_k)_{ij}=\mathbf 1_{\{|i-j|=k\}}.
\]

Thus \(H_0=I\), \(H_1\) is the adjacency matrix of the path graph on \(N\) vertices, and \(H_{N-1}\) has ones only in the two opposite corners.

Since

\[
c_i-c_j=h(i-j),
\]

we may rewrite the paired kernel as

\[
(T_s)_{ij}
=
-2\sqrt\pi\,\sigma
\exp\left(-\frac{s^2+h^2(i-j)^2}{4\sigma^2}\right)
\cosh\left(\frac{hs(i-j)}{2\sigma^2}\right).
\]

Because the right-hand side depends only on \(|i-j|\),

\[
T_s=\sum_{k=0}^{N-1}a_k(s)H_k,
\]

where

\[
a_k(s)
=
-2\sqrt\pi\,\sigma
\exp\left(-\frac{s^2+h^2k^2}{4\sigma^2}\right)
\cosh\left(\frac{hks}{2\sigma^2}\right).
\]

## 3. Linear independence of the translation coefficients

### Lemma 3.1

The functions

\[
s\longmapsto a_k(s),\qquad k=0,\dots,N-1,
\]

are linearly independent over \(\mathbb C\).

### Proof

The common factor

\[
-2\sqrt\pi\,\sigma\exp\left(-\frac{s^2}{4\sigma^2}\right)
\]

never vanishes. Therefore it is enough to prove linear independence of

\[
\exp\left(-\frac{h^2k^2}{4\sigma^2}\right)
\cosh\left(\frac{hks}{2\sigma^2}\right),
\qquad k=0,\dots,N-1.
\]

The nonzero constants depending on \(k\) may also be removed, so it is enough to prove that

\[
1,\cosh(\alpha s),\cosh(2\alpha s),\dots,
\cosh((N-1)\alpha s)
\]

are linearly independent, where

\[
\alpha=\frac{h}{2\sigma^2}>0.
\]

Using the Chebyshev identity

\[
\cosh(kx)=T_k(\cosh x),
\]

where \(T_k\) is a polynomial of degree \(k\), any relation

\[
\sum_{k=0}^{N-1}b_k\cosh(k\alpha s)=0
\]

would give a polynomial

\[
\sum_{k=0}^{N-1}b_kT_k(y)
\]

vanishing for every \(y=\cosh(\alpha s)\in[1,\infty)\). Hence the polynomial is identically zero. Since the \(T_k\) have distinct degrees, every \(b_k=0\). ∎

### Corollary 3.2

The linear span of the family \(\{T_s:s\ge 0\}\) is the full space of symmetric Toeplitz matrices:

\[
\operatorname{span}\{T_s:s\ge0\}
=
\operatorname{span}\{H_0,\dots,H_{N-1}\}.
\]

### Proof

If the coefficient vectors

\[
(a_0(s),\dots,a_{N-1}(s))
\]

failed to span \(\mathbb C^N\), there would be a nonzero vector \(b\) orthogonal to all of them, producing a nontrivial linear relation among the functions \(a_k(s)\). Lemma 3.1 rules this out. ∎

Therefore

\[
\{T_s:s\ge0\}'
=
\{H_0,\dots,H_{N-1}\}'.
\]

## 4. The commutant of the symmetric Toeplitz family

### Lemma 4.1

The path adjacency matrix \(H_1\) has simple spectrum.

### Proof

Its normalized eigenvectors are

\[
v_r(j)=\sqrt{\frac{2}{N+1}}
\sin\left(\frac{rj\pi}{N+1}\right),
\qquad r=1,\dots,N,
\]

with eigenvalues

\[
\lambda_r=2\cos\left(\frac{r\pi}{N+1}\right).
\]

These eigenvalues are pairwise distinct. ∎

Consequently, every matrix commuting with \(H_1\) is diagonal in the basis \(\{v_r\}\). Write

\[
Xv_r=x_rv_r.
\]

Now use the opposite-corner matrix

\[
H_{N-1}=e_1e_N^*+e_Ne_1^*.
\]

The sine eigenvectors satisfy

\[
v_r(N)=(-1)^{r+1}v_r(1).
\]

Therefore

\[
\langle v_r,H_{N-1}v_t\rangle
=
v_r(1)v_t(1)
\left((-1)^{r+1}+(-1)^{t+1}\right).
\]

This matrix element is nonzero exactly when \(r\) and \(t\) have the same parity.

### Lemma 4.2

If \(X\) commutes with both \(H_1\) and \(H_{N-1}\), then the numbers \(x_r\) are constant on odd indices and constant on even indices.

### Proof

In the \(H_1\)-eigenbasis, the commutator equation

\[
XH_{N-1}=H_{N-1}X
\]

becomes

\[
(x_r-x_t)
\langle v_r,H_{N-1}v_t\rangle=0.
\]

Whenever \(r\) and \(t\) have the same parity, the matrix element is nonzero, so \(x_r=x_t\). ∎

Reflection acts on the same eigenvectors by

\[
Jv_r=(-1)^{r+1}v_r.
\]

Hence an operator taking one scalar value on odd \(r\) and another scalar value on even \(r\) has the form

\[
X=aI+bJ.
\]

This proves the central finite-dimensional theorem.

## 5. Main theorem

### Theorem 5.1 (reflection commutant theorem)

For \(N\ge2\), equally spaced symmetric packet centers, and the continuous paired Gaussian translation family \(\{T_s:s\ge0\}\),

\[
\boxed{
\{T_s:s\ge0\}'
=
\operatorname{span}_{\mathbb C}\{I,J\}.
}
\]

### Proof

By Corollary 3.2, any matrix commuting with every \(T_s\) commutes with every \(H_k\), in particular with \(H_1\) and \(H_{N-1}\). Lemmas 4.1 and 4.2 then imply that it has the form \(aI+bJ\).

Conversely, every symmetric Toeplitz matrix is centrosymmetric, so it commutes with \(J\). Therefore both \(I\) and \(J\) commute with every \(T_s\). ∎

## 6. Consequence for the finite Weil algebra

Let \(\mathfrak W_N\) be the unital \(*\)-algebra generated by the continuous paired translation family together with any additional finite Weil blocks that commute with reflection, including the Gram, conductor, gamma, and pole blocks.

Because the translation family is contained among the generators,

\[
\mathfrak W_N'
\subseteq
\{T_s:s\ge0\}'.
\]

Because every generator commutes with \(J\),

\[
\operatorname{span}\{I,J\}
\subseteq
\mathfrak W_N'.
\]

Theorem 5.1 gives equality:

\[
\boxed{
\mathfrak W_N'
=
\operatorname{span}_{\mathbb C}\{I,J\}.
}
\]

Since \(\mathfrak W_N\) is a finite-dimensional unital \(*\)-algebra, the finite-dimensional bicommutant theorem gives

\[
\mathfrak W_N
=
(\mathfrak W_N')'.
\]

Therefore

\[
\boxed{
\mathfrak W_N
=
\{J\}'
\cong
M_{N_+}(\mathbb C)\oplus M_{N_-}(\mathbb C),
}
\]

where

\[
N_+=\left\lceil\frac N2\right\rceil,
\qquad
N_-=\left\lfloor\frac N2\right\rfloor.
\]

Thus reflection is the complete exact symmetry of the universal continuous paired-translation geometry on a uniform finite packet grid. The even and odd sectors are irreducible under the generated algebra, and there is no further common invariant decomposition.

## 7. What has and has not been proved

The theorem is exact under the following hypotheses:

1. the packet centers form an equally spaced symmetric grid;
2. the full continuous family \(T_s\), \(s\ge0\), is admitted as a universal generator family;
3. matrices are considered over \(\mathbb C\).

The theorem does not yet prove the same statement for:

- arbitrary nonuniform symmetric centers;
- a fixed finite set of prime-power shifts;
- numerically truncated or rank-reduced whitened coordinates.

For a finite arithmetic shift set, the common commutant must be computed or certified separately. A natural next theorem is to identify explicit finite subsets \(\{s_1,\dots,s_m\}\) whose matrices already generate the full parity-preserving algebra.