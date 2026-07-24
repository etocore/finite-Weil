# Realization and minimality for finite exponential packet transforms

## Status

This note develops the inverse theory of the finite exponential packet transform

\[
F(z)=\Phi_X[u](z)=\sum_{j=1}^N u_j e^{x_j z},
\]

with distinct nodes \(x_j\in\mathbb C\) and nonzero coefficients \(u_j\in\mathbb C\).

The results are classical at the level of exponential polynomials and constant-coefficient differential equations. Their purpose here is to isolate the exact realization, uniqueness, and minimality statements needed by the finite packet-transform program, while separating those established facts from later geometric optimization questions.

The central conclusion is stronger than the informal claim that a packet transform may have many exact finite realizations. After zero coefficients and duplicate nodes are removed, the finite exponential representation is unique up to permutation. The nontrivial freedom begins with approximate realization, confluent limits, normalization, and optimization over external sampling or kernel geometry.

---

## 1. Reduced packet realizations

### Definition 1.1 - packet realization

A finite packet realization of an entire function \(F\) is a pair

\[
(X,u),\qquad
X=(x_1,\ldots,x_N)\in\mathbb C^N,
\qquad
u=(u_1,\ldots,u_N)\in\mathbb C^N,
\]

such that

\[
F(z)=\sum_{j=1}^N u_j e^{x_jz}.
\]

A realization is **reduced** when

1. the nodes \(x_j\) are pairwise distinct; and
2. every coefficient \(u_j\) is nonzero.

Every finite realization reduces to one by deleting zero coefficients and combining terms with equal nodes.

### Definition 1.2 - packet length

For nonzero \(F\), define the packet length

\[
\ell(F)
:=
\min\left\{N:
F(z)=\sum_{j=1}^N u_j e^{x_jz}
\text{ for some }x_j,u_j\in\mathbb C
\right\}.
\]

Set \(\ell(0)=0\).

---

## 2. Linear independence of distinct exponential modes

### Proposition 2.1

If \(\lambda_1,\ldots,\lambda_M\in\mathbb C\) are distinct and

\[
\sum_{j=1}^M c_j e^{\lambda_j z}=0
\qquad\text{for every }z\in\mathbb C,
\]

then \(c_1=\cdots=c_M=0\).

### Proof

Differentiate at \(z=0\) for orders \(k=0,\ldots,M-1\). This gives

\[
\sum_{j=1}^M c_j\lambda_j^k=0.
\]

Equivalently,

\[
V(\lambda_1,\ldots,\lambda_M)c=0,
\]

where \(V\) is the Vandermonde matrix. Since the nodes are distinct,

\[
\det V=\prod_{1\le i<j\le M}(\lambda_j-\lambda_i)\ne0.
\]

Hence \(c=0\). \(\square\)

### Corollary 2.2 - uniqueness of reduced realization

Suppose

\[
F(z)=\sum_{j=1}^N u_j e^{x_jz}
=\sum_{k=1}^M v_k e^{y_kz}
\]

are two reduced realizations. Then \(N=M\), and there is a permutation \(\pi\) such that

\[
y_{\pi(j)}=x_j,
\qquad
v_{\pi(j)}=u_j.
\]

### Proof

Move all terms to one side and combine any exponent appearing in both lists. The resulting exponential sum has distinct exponents and vanishes identically. Proposition 2.1 forces every combined coefficient to vanish. Thus the two node sets and their corresponding coefficients coincide. \(\square\)

### Consequence

There is no nontrivial family of exact reduced finite realizations of a fixed exponential polynomial. The reduced realization is already canonical up to relabeling.

---

## 3. Differential-operator characterization

Let \(D=d/dz\).

### Theorem 3.1 - simple-root realization theorem

For an entire function \(F\), the following are equivalent.

1. \(F\) admits a reduced packet realization
   \[
   F(z)=\sum_{j=1}^N u_j e^{x_jz}
   \]
   with pairwise distinct nodes.

2. There is a nonzero polynomial \(p\in\mathbb C[t]\) with only simple roots such that
   \[
   p(D)F=0.
   \]

3. The derivative orbit
   \[
   \mathcal O_D(F):=
   \operatorname{span}\{F,F',F'',\ldots\}
   \]
   is finite-dimensional and the restriction
   \[
   D|_{\mathcal O_D(F)}
   \]
   is diagonalizable.

When these conditions hold, the nodes are exactly the eigenvalues of \(D|_{\mathcal O_D(F)}\) that occur with nonzero spectral component in \(F\).

### Proof

#### \((1)\Rightarrow(2)\)

Set

\[
p(t)=\prod_{j=1}^N(t-x_j).
\]

Since \((D-x_j)e^{x_jz}=0\), every term is annihilated by \(p(D)\), hence \(p(D)F=0\).

#### \((2)\Rightarrow(1)\)

Write

\[
p(t)=c\prod_{j=1}^N(t-x_j)
\]

with distinct roots. The solution space of the constant-coefficient ODE \(p(D)G=0\) has basis

\[
e^{x_1z},\ldots,e^{x_Nz}.
\]

Therefore

\[
F(z)=\sum_{j=1}^N u_j e^{x_jz}.
\]

Deleting zero coefficients gives a reduced realization.

#### \((1)\Rightarrow(3)\)

The derivative orbit lies in

\[
\operatorname{span}\{e^{x_1z},\ldots,e^{x_Nz}\}.
\]

On this space, differentiation is diagonal in the exponential basis, with eigenvalues \(x_j\).

#### \((3)\Rightarrow(1)\)

Let \(V=\mathcal O_D(F)\). Since \(D|_V\) is diagonalizable, choose an eigenbasis \(g_j\) with

\[
Dg_j=x_jg_j.
\]

Every entire solution of \(g_j'=x_jg_j\) has the form

\[
g_j(z)=c_je^{x_jz}.
\]

Expanding \(F\) in this eigenbasis gives a finite exponential representation. \(\square\)

---

## 4. Repeated roots and confluent packets

The simple-root condition is essential.

### Theorem 4.1 - confluent realization theorem

An entire function satisfies some nonzero constant-coefficient differential equation if and only if it is an exponential polynomial of the form

\[
F(z)=
\sum_{j=1}^s P_j(z)e^{x_jz},
\]

where the \(x_j\) are distinct and each \(P_j\) is a polynomial.

If the characteristic root \(x_j\) has multiplicity \(m_j\), then one may take

\[
\deg P_j<m_j.
\]

Thus ordinary packet transforms correspond exactly to the semisimple case. Repeated nodes do not produce a new ordinary realization after combination; their meaningful limit is a **confluent packet** containing modes

\[
z^q e^{xz},
\qquad 0\le q<m.
\]

### Example 4.2

The function

\[
F(z)=ze^{xz}
\]

satisfies

\[
(D-x)^2F=0,
\qquad
(D-x)F\ne0.
\]

It is not a finite sum of pure exponentials with distinct exponents. It appears as the collision limit

\[
ze^{xz}
=
\lim_{h\to0}
\frac{e^{(x+h)z}-e^{xz}}{h}.
\]

This identifies node collision as a passage from ordinary to confluent realization, not as nonuniqueness of reduced ordinary packets.

---

## 5. Minimal annihilator and packet length

### Definition 5.1 - minimal annihilating polynomial

For a nonzero exponential polynomial \(F\), let \(m_F\) be the monic polynomial of least degree satisfying

\[
m_F(D)F=0.
\]

### Theorem 5.2

If

\[
F(z)=\sum_{j=1}^N u_j e^{x_jz}
\]

is reduced, then

\[
\boxed{
 m_F(t)=\prod_{j=1}^N(t-x_j).
}
\]

Consequently,

\[
\boxed{
\ell(F)=\deg m_F=N.
}
\]

### Proof

The displayed product annihilates \(F\), so \(m_F\) divides it. Conversely, if \(q(D)F=0\), then

\[
0=q(D)F
=
\sum_{j=1}^N u_j q(x_j)e^{x_jz}.
\]

Linear independence of the distinct exponentials implies

\[
u_jq(x_j)=0
\]

for every \(j\). Since \(u_j\ne0\), every \(x_j\) is a root of \(q\). Hence the product divides every annihilator and is therefore minimal. Its degree is \(N\). Uniqueness of reduced realization then shows no representation with fewer than \(N\) nodes exists. \(\square\)

### Corollary 5.3 - derivative-orbit dimension

For a reduced ordinary packet transform,

\[
\boxed{
\ell(F)=\dim\mathcal O_D(F).
}
\]

### Proof

The derivative orbit is spanned by the \(N\) modes \(e^{x_jz}\). It contains all of them because the vectors of coefficients of

\[
F,F',\ldots,F^{(N-1)}
\]

form a Vandermonde-scaled system with nonzero diagonal coefficient matrix. Hence its dimension is \(N\). \(\square\)

---

## 6. Jet recurrences and Hankel rank

Let

\[
a_k:=F^{(k)}(0).
\]

For a reduced realization,

\[
a_k=\sum_{j=1}^N u_jx_j^k.
\]

Thus the derivative jet is a finite exponential moment sequence.

### Proposition 6.1 - recurrence

If

\[
m_F(t)=t^N+c_{N-1}t^{N-1}+\cdots+c_0,
\]

then

\[
\boxed{
a_{k+N}+c_{N-1}a_{k+N-1}+\cdots+c_0a_k=0
}
\]

for every \(k\ge0\).

### Proof

Differentiate \(m_F(D)F=0\) exactly \(k\) times and evaluate at zero. \(\square\)

Define the infinite Hankel matrix

\[
H_F=(a_{r+s})_{r,s\ge0}.
\]

### Theorem 6.2 - Hankel-rank characterization

For a nonzero entire function \(F\), the following are equivalent.

1. \(F\) is a finite exponential polynomial.
2. The jet sequence \((a_k)\) satisfies a finite linear recurrence.
3. The infinite Hankel matrix \(H_F\) has finite rank.

For an ordinary reduced packet transform with \(N\) distinct nodes and nonzero coefficients,

\[
\boxed{\operatorname{rank}H_F=N.}
\]

### Proof sketch

A finite recurrence gives a finite-dimensional shift orbit of the sequence, hence finite Hankel rank. Conversely, finite Hankel rank produces a nontrivial dependence among Hankel columns, which is a recurrence. The exponential-polynomial form follows from the characteristic polynomial of that recurrence, with polynomial factors when roots repeat.

In the ordinary reduced case,

\[
H_F=V\,\operatorname{diag}(u_1,\ldots,u_N)V^{\mathsf T},
\]

where

\[
V_{rj}=x_j^r.
\]

Every finite \(N\times N\) leading Vandermonde block is invertible, and the coefficient diagonal is invertible, so the rank is \(N\). \(\square\)

### Caution

For complex coefficients, \(H_F\) is a bilinear Hankel matrix, not a positive moment matrix in general. No positivity conclusion follows without additional assumptions.

---

## 7. Exact reconstruction from finitely many derivatives

Assume \(F\) has packet length \(N\).

### Proposition 7.1 - annihilator recovery

If the relevant Hankel system is nonsingular, the coefficients of

\[
m_F(t)=t^N+c_{N-1}t^{N-1}+\cdots+c_0
\]

are determined by

\[
\begin{pmatrix}
a_0&a_1&\cdots&a_{N-1}\\
a_1&a_2&\cdots&a_N\\
\vdots&\vdots&\ddots&\vdots\\
a_{N-1}&a_N&\cdots&a_{2N-2}
\end{pmatrix}
\begin{pmatrix}
c_0\\c_1\\\vdots\\c_{N-1}
\end{pmatrix}
=
-\begin{pmatrix}
a_N\\a_{N+1}\\\vdots\\a_{2N-1}
\end{pmatrix}.
\]

The nodes are the roots of \(m_F\). Once the nodes are known, the coefficients are recovered from

\[
\begin{pmatrix}
1&\cdots&1\\
x_1&\cdots&x_N\\
\vdots&\ddots&\vdots\\
x_1^{N-1}&\cdots&x_N^{N-1}
\end{pmatrix}
\begin{pmatrix}
u_1\\\vdots\\u_N
\end{pmatrix}
=
\begin{pmatrix}
a_0\\\vdots\\a_{N-1}
\end{pmatrix}.
\]

This is the exact Prony reconstruction scheme in derivative-jet coordinates.

### Corollary 7.2

In generic reduced position, the first \(2N\) derivatives

\[
F^{(0)}(0),\ldots,F^{(2N-1)}(0)
\]

determine the entire function, its node set, and all coefficients.

### Qualification

The count \(2N\) is a sufficient generic reconstruction bound, not a universal numerical-stability claim. Singular or nearly singular Hankel systems require shifted blocks, structured methods, or additional samples.

---

## 8. Translation, scaling, and identifiability

The transform covariances do not create two representations of the same fixed function. They relate different functions.

If

\[
F(z)=\Phi_X[u](z),
\]

then

\[
\Phi_{X+a}[u](z)=e^{az}F(z),
\]

and

\[
\Phi_{bX}[u](z)=F(bz).
\]

Therefore global translation and scaling become symmetries only after one passes to an explicitly defined equivalence class of functions, for example modulo multiplication by \(e^{az}\) or reparameterization \(z\mapsto bz\). For exact realization of a fixed \(F\), the reduced nodes remain identifiable.

---

## 9. Stability is distinct from uniqueness

Exact uniqueness does not imply stable recovery.

The inverse map from jets or samples to nodes becomes ill-conditioned when

- two nodes nearly collide;
- a coefficient becomes small;
- the observation window is too narrow;
- Vandermonde or Hankel matrices approach singularity;
- modes become nearly indistinguishable under the chosen sampling functionals.

This is the first place where geometry contributes genuinely nontrivial structure.

### Definition 9.1 - local realization map

For fixed length \(N\), define

\[
\mathcal R_N(X,u)
:=
(a_0,\ldots,a_{2N-1}),
\qquad
a_k=\sum_{j=1}^N u_jx_j^k.
\]

Its Jacobian contains the columns

\[
\frac{\partial a_k}{\partial u_j}=x_j^k,
\qquad
\frac{\partial a_k}{\partial x_j}=ku_jx_j^{k-1}.
\]

This is a confluent Vandermonde structure. Loss of separation or vanishing coefficients drives the Jacobian toward rank deficiency.

### Research problem 9.2 - intrinsic condition number

Define and compare condition numbers for realization from

1. derivative jets at one point;
2. values at multiple real points;
3. values on an imaginary-frequency window;
4. RKHS-normalized evaluation data;
5. Gaussian-weighted shell measurements.

A canonical geometry should be sought through stability of an observation model, not through nonexistent exact nonuniqueness.

---

## 10. Corrected geometric frontier

The classical realization theorem settles existence and exact uniqueness. The packet-transform program can add structure in the following directions.

### 10.1 Stable geometry design

For a prescribed admissible node region and observation system, optimize

\[
\sigma_{\min}(J_{\mathcal R_N}),
\qquad
\kappa(J_{\mathcal R_N}),
\qquad
\sigma_{\min}(S_{Z,X}),
\]

or a noise-aware Cramér-Rao-type functional.

### 10.2 Confluent compactification

Adjoin collision strata represented by

\[
z^qe^{xz}
\]

so that the space of packet realizations has a meaningful boundary. Study whether the ordinary configuration space admits a natural compactification by confluent packets.

### 10.3 Approximate packet length

For a normed function class and tolerance \(\varepsilon\), define

\[
\ell_\varepsilon(F)
:=
\min\left\{N:
\left\|F-\sum_{j=1}^N u_je^{x_jz}\right\|\le\varepsilon
\right\}.
\]

Unlike exact packet length, approximate packet length may have many competing near-minimizers and a rich geometry.

### 10.4 Structured node classes

Impose real, symmetric, lattice, bounded-diameter, separated, or arithmetic node constraints. A function realizable over unrestricted complex nodes may fail to be realizable in a structured class, and constrained best approximation becomes nontrivial.

### 10.5 Observation-dependent canonical realization

When only incomplete or noisy data are available, define a canonical estimator by minimizing a stated objective, such as

\[
\|\mathcal M(\Phi_X[u])-d\|^2
+\lambda\,\mathcal P(X,u),
\]

where \(\mathcal M\) is the measurement operator and \(\mathcal P\) encodes separation, norm, or geometry priors.

---

## 11. The theorem package

The inverse theory can be summarized as follows.

### Exact realization

\[
F\text{ is an ordinary finite packet transform}
\iff
F\text{ is annihilated by a square-free polynomial in }D.
\]

### Exact uniqueness

A reduced realization is unique up to permutation.

### Minimality

\[
\ell(F)
=
\deg m_F
=
\dim\mathcal O_D(F)
=
\operatorname{rank}H_F
\]

for ordinary reduced packets.

### Reconstruction

Generically, \(2N\) derivative samples determine a packet of length \(N\).

### Boundary

Repeated characteristic roots correspond to confluent modes \(z^qe^{xz}\).

### Research frontier

The unresolved geometry concerns stability, constrained realization, approximation, observation design, and confluent limits - not multiplicity of exact reduced representations.

---

## 12. Immediate theorem queue

1. Prove a quantitative lower bound for the smallest singular value of the realization Jacobian under node separation and coefficient-floor assumptions.
2. Derive the parity-reduced Prony system for reflection-symmetric real node sets.
3. Construct the confluent compactification for one and two node collisions.
4. Compare jet-based and multi-point sampling condition numbers.
5. Define approximate packet length in the finite RKHS norm and prove existence of minimizers under compact node constraints.
6. Connect the Hankel-rank realization invariant to the weighted-shell finite-rank decomposition.

These are the first questions in the realization program that are not exhausted by classical constant-coefficient ODE theory.