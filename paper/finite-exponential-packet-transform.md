# Finite exponential packet transforms

## Status

This note begins a self-contained theory of the finite exponential packet transform

\[
\Phi_X[u](z):=\sum_{i=1}^N u_i e^{z x_i},
\qquad z\in\mathbb C,
\]

for a fixed ordered node set

\[
X=(x_1,\ldots,x_N)\in\mathbb R^N
\]

with distinct entries and coefficient vector \(u\in\mathbb C^N\).

The purpose is not to infer anything about RH. The purpose is to identify the intrinsic analytic structure already present in the finite Gaussian and Weil-section programs.

The guiding principle is:

> Geometry is the probe space; arithmetic is the state.

Here the node geometry \(X\) determines a finite-dimensional space of entire functions. Later arithmetic constructions may define quadratic forms on that space, but the transform theory is independent of them.

---

## 1. The transform space

Define

\[
\mathcal E_X
:=
\operatorname{span}\{e^{x_1 z},\ldots,e^{x_N z}\}
\subset \operatorname{Hol}(\mathbb C).
\]

The packet transform is the linear map

\[
\mathcal T_X:\mathbb C^N\to \mathcal E_X,
\qquad
\mathcal T_Xu=\Phi_X[u].
\]

### Proposition 1.1 - injectivity

If the nodes \(x_i\) are distinct, then \(\mathcal T_X\) is injective. Consequently,

\[
\dim \mathcal E_X=N.
\]

### Proof

Suppose

\[
\sum_{i=1}^N u_i e^{x_i z}=0
\]

for every \(z\in\mathbb C\). Differentiating at \(z=0\) gives

\[
\sum_{i=1}^N u_i x_i^k=0,
\qquad k=0,\ldots,N-1.
\]

This is the Vandermonde system

\[
V_Xu=0,
\qquad
(V_X)_{k i}=x_i^k.
\]

Because the nodes are distinct, \(V_X\) is invertible, hence \(u=0\). \(\square\)

### Consequence

Any identity proved for coefficient vectors can be transported without loss into \(\mathcal E_X\), and conversely every element of \(\mathcal E_X\) has a unique coefficient vector.

---

## 2. Moments, jets, and grade

For every integer \(k\ge0\),

\[
\Phi_X[u]^{(k)}(0)
=
\sum_{i=1}^N u_i x_i^k.
\]

Define the moment vectors

\[
m_k(X):=(x_1^k,\ldots,x_N^k)^{\mathsf T}.
\]

Then

\[
\Phi_X[u]^{(k)}(0)=u^{\mathsf T}m_k(X).
\]

The first \(N\) derivatives determine \(u\) uniquely.

### Definition 2.1 - transform grade

For nonzero \(u\), define

\[
\operatorname{gr}_X(u)
:=
\operatorname{ord}_{z=0}\Phi_X[u](z).
\]

Equivalently,

\[
\operatorname{gr}_X(u)=r
\]

if and only if

\[
u^{\mathsf T}m_0=\cdots=u^{\mathsf T}m_{r-1}=0,
\qquad
u^{\mathsf T}m_r\ne0.
\]

Because the first \(N\) moments form an invertible Vandermonde system,

\[
0\le \operatorname{gr}_X(u)\le N-1.
\]

### Definition 2.2 - jet filtration

Let

\[
F_X^r
:=
\{u\in\mathbb C^N:
\Phi_X[u]^{(k)}(0)=0\text{ for }0\le k<r\}.
\]

Then

\[
\mathbb C^N=F_X^0\supset F_X^1\supset\cdots\supset F_X^N=\{0\},
\]

and, by Vandermonde rank,

\[
\dim F_X^r=N-r.
\]

This filtration is the intrinsic transform form of the polynomial-moment hierarchy used in the Gaussian flat limit.

---

## 3. Canonical graded basis

Equip \(\mathbb C^N\) with its standard Hermitian inner product. Apply Gram-Schmidt to

\[
m_0,m_1,\ldots,m_{N-1}
\]

to obtain an orthonormal basis

\[
p_0,p_1,\ldots,p_{N-1},
\]

where

\[
p_r\in
\operatorname{span}\{m_0,\ldots,m_r\}
\cap
\operatorname{span}\{m_0,\ldots,m_{r-1}\}^{\perp}.
\]

### Proposition 3.1

For every \(r\),

\[
\operatorname{ord}_0\Phi_X[p_r]=r.
\]

### Proof

For \(k<r\), the vector \(m_k\) belongs to

\[
\operatorname{span}\{m_0,\ldots,m_{r-1}\},
\]

so

\[
p_r^{\mathsf T}m_k=0.
\]

At \(k=r\), the Gram-Schmidt residual is nonzero and

\[
p_r^{\mathsf T}m_r\ne0.
\]

Thus the first nonzero Taylor coefficient occurs at degree \(r\). \(\square\)

This identifies the flat-limit grading with order of vanishing of the transform, without reference to a Gaussian kernel.

---

## 4. Natural actions

The transform linearizes several operations on packet data.

### 4.1 Coefficient operators

For any matrix \(A\in\mathbb C^{N\times N}\), define the induced operator

\[
\widehat A_X:\mathcal E_X\to\mathcal E_X,
\qquad
\widehat A_X\Phi_X[u]:=\Phi_X[Au].
\]

Injectivity makes this well-defined. The assignment

\[
A\mapsto\widehat A_X
\]

is an algebra isomorphism between \(M_N(\mathbb C)\) and \(\operatorname{End}(\mathcal E_X)\).

Thus every finite matrix problem on packet coefficients has an equivalent entire-function representation.

### 4.2 Translation of all nodes

For \(a\in\mathbb R\), let

\[
X+a=(x_1+a,\ldots,x_N+a).
\]

Then

\[
\Phi_{X+a}[u](z)=e^{az}\Phi_X[u](z).
\]

Global translation of geometry is multiplication by a zero-free exponential.

In particular,

\[
\operatorname{ord}_0\Phi_{X+a}[u]
=
\operatorname{ord}_0\Phi_X[u].
\]

### 4.3 Scaling of nodes

For \(b\in\mathbb R\),

\[
\Phi_{bX}[u](z)=\Phi_X[u](bz).
\]

Thus bandwidth or geometric dilation acts by rescaling the transform variable.

### 4.4 Permutation covariance

For a permutation matrix \(P\),

\[
\Phi_{PX}[Pu](z)=\Phi_X[u](z).
\]

The transform depends on the labeled packet only through the paired data \((x_i,u_i)\).

### 4.5 Reflection

Suppose the node set is reflection-symmetric: there is a permutation matrix \(J\) such that

\[
JX=-X.
\]

Then

\[
\boxed{
\Phi_X[Ju](z)=\Phi_X[u](-z).
}
\]

Hence the \(+1\) and \(-1\) eigenspaces of \(J\) map respectively to even and odd entire functions in \(\mathcal E_X\).

This is the finite packet reflection law. Any later comparison with an \(s\mapsto1-s\) symmetry must be made only after the relevant normalization and change of variables are stated.

---

## 5. Differentiation and multiplication operators

Let

\[
D:=\frac{d}{dz}.
\]

Then

\[
D\Phi_X[u](z)
=
\sum_i x_i u_i e^{zx_i}
=
\Phi_X[X_\mathrm{diag}u](z),
\]

where

\[
X_\mathrm{diag}:=\operatorname{diag}(x_1,\ldots,x_N).
\]

Therefore differentiation on \(\mathcal E_X\) corresponds exactly to multiplication of coefficients by node position:

\[
D=\widehat{X_\mathrm{diag}}_X.
\]

Consequently,

\[
D^k\Phi_X[u]=\Phi_X[X_\mathrm{diag}^k u].
\]

Since \(X_\mathrm{diag}\) has distinct eigenvalues, \(D|_{\mathcal E_X}\) is diagonalizable with spectrum

\[
\{x_1,\ldots,x_N\}.
\]

### Proposition 5.1 - annihilating differential equation

Every \(F\in\mathcal E_X\) satisfies

\[
\boxed{
\prod_{i=1}^N(D-x_i)F=0.
}
\]

Conversely, the entire solutions of this constant-coefficient differential equation are exactly the functions in \(\mathcal E_X\).

This gives an intrinsic characterization of the packet-transform space independent of coefficient coordinates.

---

## 6. Evaluation vectors and the reproducing kernel

Transport the standard coefficient inner product to \(\mathcal E_X\):

\[
\langle \Phi_X[u],\Phi_X[v]\rangle_{\mathcal E_X}
:=
\langle u,v\rangle_{\mathbb C^N}.
\]

For \(w\in\mathbb C\), define the coefficient evaluation vector

\[
k_w
:=
\big(e^{\overline w x_1},\ldots,e^{\overline w x_N}\big)^{\mathsf T}.
\]

Then

\[
\Phi_X[u](w)=\langle u,k_w\rangle_{\mathbb C^N}.
\]

Thus \(\mathcal E_X\) is a finite-dimensional reproducing-kernel Hilbert space with kernel

\[
\boxed{
K_X(z,w)
=
\sum_{i=1}^N e^{z x_i}e^{\overline w x_i}
=
\sum_{i=1}^N e^{(z+\overline w)x_i}.
}
\]

Indeed,

\[
F(w)=\langle F,K_X(\cdot,w)\rangle_{\mathcal E_X}.
\]

### Derivative evaluation kernels

For every \(r\ge0\),

\[
F^{(r)}(w)
=
\left\langle
F,
\partial_{\overline w}^{\,r}K_X(\cdot,w)
\right\rangle_{\mathcal E_X}.
\]

At \(w=0\), the derivative evaluation vector corresponds to the moment vector \(m_r(X)\).

Therefore the jet filtration is the nested orthogonal-complement filtration generated by derivative kernel vectors at the origin.

---

## 7. Sampling and Gram matrices

Choose sample points

\[
Z=(z_1,\ldots,z_M)\in\mathbb C^M.
\]

Define the sampling matrix

\[
S_{Z,X}
:=
\big(e^{z_a x_i}\big)_{1\le a\le M,\,1\le i\le N}.
\]

Then

\[
\big(\Phi_X[u](z_1),\ldots,\Phi_X[u](z_M)\big)^{\mathsf T}
=S_{Z,X}u.
\]

The sample Gram matrix is

\[
G_{Z,X}=S_{Z,X}S_{Z,X}^{*}
=
\big(K_X(z_a,z_b)\big)_{a,b}.
\]

The coefficient-side Gram matrix is

\[
H_{Z,X}=S_{Z,X}^{*}S_{Z,X}.
\]

This makes conditioning a transform-space sampling question. A small Gram floor means that the chosen sample functionals nearly fail to distinguish some direction in \(\mathcal E_X\).

### Proposition 7.1

If \(M=N\) and the sample points \(z_a\) are distinct real numbers, then \(S_{Z,X}\) is a generalized exponential Vandermonde matrix. Its invertibility is not automatic for arbitrary complex data, but it is guaranteed in several ordered real regimes by strict total positivity of the exponential kernel. The precise hypotheses required for each application must be stated rather than assumed.

This proposition is intentionally cautious: total-positivity claims will be isolated and proved under explicit ordering assumptions in a later note.

---

## 8. Bilinear shell transform

For \(u,w\in\mathbb C^N\), define

\[
G_{u,w}(z)
:=
\sum_{i,j=1}^N u_iw_j e^{z(x_i-x_j)}.
\]

Then

\[
\boxed{
G_{u,w}(z)
=
\Phi_X[u](z)\Phi_X[w](-z).
}
\]

### Proof

\[
\Phi_X[u](z)\Phi_X[w](-z)
=
\left(\sum_i u_i e^{zx_i}\right)
\left(\sum_j w_j e^{-zx_j}\right)
=
\sum_{i,j}u_iw_j e^{z(x_i-x_j)}.
\]

\(\square\)

This is the primary shell-factorization identity. Cosine and sine shell formulas are real and imaginary, or even and odd, consequences of this entire-function identity.

### Corollary 8.1 - shell moments

For every \(k\ge0\),

\[
G_{u,w}^{(k)}(0)
=
\sum_{i,j}u_iw_j(x_i-x_j)^k.
\]

By the product rule,

\[
G_{u,w}^{(k)}(0)
=
\sum_{a=0}^k
(-1)^{k-a}
\binom{k}{a}
\Phi_X[u]^{(a)}(0)
\Phi_X[w]^{(k-a)}(0).
\]

Thus all difference-shell moments factor through the jets of the two packet transforms.

### Corollary 8.2 - order bound

If

\[
\operatorname{ord}_0\Phi_X[u]=r,
\qquad
\operatorname{ord}_0\Phi_X[w]=s,
\]

then

\[
\operatorname{ord}_0G_{u,w}=r+s.
\]

The leading coefficient is

\[
[z^{r+s}]G_{u,w}(z)
=
(-1)^s
[z^r]\Phi_X[u](z)
[z^s]\Phi_X[w](z).
\]

This gives an exact additive grading law for shell correlations.

---

## 9. Distinguished evaluation channels

For any \(a\in\mathbb C\), evaluation at \(a\) is the linear functional

\[
\operatorname{ev}_a(u)=\Phi_X[u](a).
\]

The pair

\[
\Phi_X[u](1/2),
\qquad
\Phi_X[u](-1/2)
\]

is distinguished in the zeta pole calculation already developed elsewhere in the repository. Within the transform theory itself, however, these are simply two bounded evaluation channels related by reflection.

For reflection-symmetric geometry:

- if \(Ju=u\), then
  \[
  \Phi_X[u](1/2)=\Phi_X[u](-1/2);
  \]
- if \(Ju=-u\), then
  \[
  \Phi_X[u](1/2)=-\Phi_X[u](-1/2).
  \]

Any interpretation as arithmetic pole channels belongs to the separate arithmetic layer.

---

## 10. Geometry-dependent extremal problems

The transform language exposes several finite variational problems that are independent of RH.

Let \(\|u\|_2=1\).

### Evaluation amplification

\[
\max_{\|u\|=1}|\Phi_X[u](a)|^2
=
K_X(a,a)
=
\sum_i e^{2\operatorname{Re}(a)x_i}.
\]

The unique maximizing direction up to phase is the normalized evaluation vector \(k_a\).

### Constrained evaluation amplification

On the grade-\(r\) subspace \(F_X^r\),

\[
\max_{u\in F_X^r,\ \|u\|=1}
|\Phi_X[u](a)|
=
\|P_{F_X^r}k_a\|.
\]

This is an exact projection problem.

### Balanced two-channel response

One natural geometry functional is

\[
B_X(u)
:=
\min\left\{
|\Phi_X[u](1/2)|,
|\Phi_X[u](-1/2)|
\right\}.
\]

Another is the quadratic channel energy

\[
C_X(u)
:=
|\Phi_X[u](1/2)|^2
+
|\Phi_X[u](-1/2)|^2.
\]

For fixed \(X\), maximizing \(C_X\) over a linear constraint subspace is a finite eigenvalue problem for the sum of two rank-one evaluation operators.

The harder problem is geometric: optimize these quantities over admissible node sets while imposing separation, symmetry, diameter, or Gram-floor constraints.

---

## 11. Relation to Gaussian packet matrices

For \(\tau>0\), define the Gaussian translation matrix

\[
K_\tau(t)_{ij}
:=
\exp\!\left(-\frac{(x_i-x_j-t)^2}{4\tau}\right).
\]

Using

\[
(x_i-x_j-t)^2
=(x_i-x_j)^2-2t(x_i-x_j)+t^2,
\]

we obtain

\[
K_\tau(t)_{ij}
=
\exp\!\left(-\frac{(x_i-x_j)^2}{4\tau}\right)
\exp\!\left(\frac{t(x_i-x_j)}{2\tau}\right)
\exp\!\left(-\frac{t^2}{4\tau}\right).
\]

Therefore, for coefficient vectors \(u,w\),

\[
u^{\mathsf T}K_\tau(t)w
=
 e^{-t^2/(4\tau)}
\sum_{i,j}
 u_iw_j
 e^{-(x_i-x_j)^2/(4\tau)}
 e^{\frac{t}{2\tau}(x_i-x_j)}.
\]

The unweighted difference exponential is exactly the shell transform

\[
G_{u,w}\!\left(\frac{t}{2\tau}\right).
\]

The Gaussian factor introduces a geometry-dependent weight on differences. A later note should determine the cleanest weighted-transform formalism, rather than folding the weight into ad hoc shell coefficients.

---

## 12. A weighted extension

Let \(A=(A_{ij})\in\mathbb C^{N\times N}\). Define

\[
G^A_{u,w}(z)
:=
\sum_{i,j}u_iA_{ij}w_j e^{z(x_i-x_j)}.
\]

Equivalently,

\[
G^A_{u,w}(z)
=
\big(D_X(z)u\big)^{\mathsf T}
A
\big(D_X(-z)w\big),
\]

where

\[
D_X(z):=\operatorname{diag}(e^{zx_1},\ldots,e^{zx_N}).
\]

The unweighted factorization occurs when \(A\) is the all-ones matrix:

\[
A=\mathbf 1\mathbf 1^{\mathsf T}.
\]

The Gaussian packet matrix corresponds to a non-rank-one weight

\[
A_{ij}=e^{-(x_i-x_j)^2/(4\tau)}.
\]

This suggests that the correct general object is not only \(\Phi_X\), but the pair

\[
(\mathcal E_X,A),
\]

where \(A\) is a state or coupling form acting on the geometric probe space.

That is the finite-dimensional version of the guiding principle:

> the transform space is geometry; the bilinear form is state.

---

## 13. First structural questions

The next stage should answer the following in order.

1. **Completeness of transform observables.**  Which coefficient-side invariants can be written canonically in terms of jets, evaluations, zeros, and products of \(\Phi_X[u]\)?

2. **Weighted shell calculus.**  For which matrices \(A\) does \(G^A_{u,w}\) admit a useful factorization or finite-rank decomposition in transform space?

3. **Operator dictionary.**  Translate the commutator and double-commutator identities from the Gaussian operator theory into actions on \(\mathcal E_X\).

4. **Geometry optimization.**  Characterize node sets maximizing constrained evaluation or susceptibility functionals under a Gram-floor condition.

5. **Continuum limit.**  Determine conditions under which
   \[
   \Phi_X[u](z)=\sum_i u_i e^{zx_i}
   \]
   converges to a bilateral Laplace transform
   \[
   \Phi_f(z)=\int e^{zx}f(x)\,d\mu(x),
   \]
   and identify which finite identities survive.

6. **Kernel limits.**  Study convergence of
   \[
   K_X(z,w)=\sum_i e^{(z+\overline w)x_i}
   \]
   under weighted empirical measures and determine the resulting RKHS.

7. **Zero geometry.**  Relate node geometry and coefficient constraints to the zero sets of exponential polynomials in \(\mathcal E_X\), without presuming any connection to zeta zeros.

---

## 14. Immediate theorem queue

The next proofs to add are:

- exact projection formulas for constrained evaluation extrema;
- parity decomposition of the RKHS kernel for symmetric nodes;
- a weighted-shell singular-value decomposition;
- a transform-space statement of graded orthogonality;
- a precise Gaussian weighted-transform identity;
- continuity and compactness results for geometry optimization under separation and diameter constraints;
- a first continuum convergence theorem for weighted empirical packet measures.

These results will determine whether the packet transform is merely a convenient coordinate system or the natural category for the existing finite operator theory.
