# Corrected collision moments and the Vandermonde-cubic determinant

## 1. Scope and claim boundary

This note establishes the finite algebra governing infinitesimal collisions of an ordered weighted node cluster. It proves an exact determinant formula for the corrected higher-moment map.

The proved result identifies the natural nondegenerate open stratum

\[
\mathcal B_m^\circ
=
\left\{
(\xi,u):
\xi_i\ne\xi_j\text{ for }i\ne j,
\quad
u_j\ne0\text{ for every }j
\right\}.
\]

No nonvanishing condition is imposed on the base moments

\[
U_r=\sum_{j=1}^m u_j\xi_j^r.
\]

This note does **not** yet prove the complete collision Smith spectrum, the missing-grade statement, the global filtration theorem, or descent to unordered clusters. Those require an additional identification of the affine or gauge direction removed by the normalized collision chart.

## 2. Ordered weighted cluster

Fix an integer \(m\ge1\). Let

\[
\xi=(\xi_1,\ldots,\xi_m)\in\mathbb C^m
\]

have pairwise distinct entries, and let

\[
u=(u_1,\ldots,u_m)\in(\mathbb C^\times)^m.
\]

Define the weighted moments

\[
U_r=\sum_{j=1}^m u_j\xi_j^r,
\qquad r\ge0.
\]

The node polynomial is

\[
q_\xi(t)=\prod_{j=1}^m(t-\xi_j).
\]

Write

\[
q_\xi(t)
=t^m-e_1t^{m-1}+e_2t^{m-2}-\cdots+(-1)^me_m,
\]

where \(e_k=e_k(\xi)\) is the \(k\)-th elementary symmetric polynomial.

Since \(q_\xi(\xi_j)=0\) for every \(j\), the moment sequence satisfies the exact Newton recurrence

\[
\boxed{
U_{m+s}
=e_1U_{m+s-1}-e_2U_{m+s-2}
+\cdots+(-1)^{m-1}e_mU_s
}
\]

for every \(s\ge0\).

This recurrence explains why moments of degree at least \(m\) are not independent when the node shape is held fixed.

## 3. Infinitesimal moment functional

Let

\[
(\delta\xi,\delta u)
\in\mathbb C^m\times\mathbb C^m
\]

be an infinitesimal variation. Define the induced variation of polynomial evaluation by

\[
\delta L(p)
=
\sum_{j=1}^m \delta u_j\,p(\xi_j)
+
\sum_{j=1}^m u_jp'(\xi_j)\,\delta\xi_j.
\]

For the monomial \(p(t)=t^r\),

\[
\delta L(t^r)=\delta U_r,
\]

where

\[
\delta U_r
=
\sum_{j=1}^m \xi_j^r\delta u_j
+r\sum_{j=1}^m u_j\xi_j^{r-1}\delta\xi_j.
\]

## 4. Unique lower-moment correction

For a fixed node variation \(\delta\xi\), seek a weight correction \(\delta u\) satisfying

\[
\delta U_0=\delta U_1=\cdots=\delta U_{m-1}=0.
\]

The coefficient matrix of \(\delta u\mapsto(\delta U_0,\ldots,\delta U_{m-1})\) is the Vandermonde matrix

\[
V(\xi)
=
\begin{pmatrix}
1&\cdots&1\\
\xi_1&\cdots&\xi_m\\
\vdots&&\vdots\\
\xi_1^{m-1}&\cdots&\xi_m^{m-1}
\end{pmatrix}.
\]

Its determinant is

\[
\det V(\xi)=\prod_{1\le i<j\le m}(\xi_j-\xi_i).
\]

Pairwise distinctness therefore implies that, for every \(\delta\xi\), there is a unique \(\delta u\) annihilating all moments below degree \(m\).

### Proposition 4.1 - Base-moment nonvanishing is irrelevant

The existence and uniqueness of the lower-moment correction depend only on pairwise distinctness of the nodes. They do not depend on whether any base moment \(U_r\) vanishes.

In particular, conditions of the form

\[
U_r\ne0
\]

are not part of the nondegenerate collision stratum.

## 5. Polynomial quotient basis

For each \(s\ge0\), divide \(t^{m+s}\) by \(q_\xi(t)\):

\[
t^{m+s}=q_\xi(t)H_s(t)+R_s(t),
\qquad
\deg R_s<m.
\]

The quotient \(H_s\) is monic of degree \(s\). Explicitly,

\[
H_s(t)
=t^s+h_1(\xi)t^{s-1}+\cdots+h_s(\xi),
\]

where \(h_k(\xi)\) is the complete homogeneous symmetric polynomial of degree \(k\).

Because a corrected variation annihilates every polynomial of degree less than \(m\),

\[
\delta L(R_s)=0.
\]

Therefore

\[
\delta U_{m+s}
=
\delta L(q_\xi H_s).
\]

At every node \(\xi_j\),

\[
q_\xi(\xi_j)=0.
\]

Hence the weight-variation term vanishes, while

\[
(q_\xi H_s)'(\xi_j)
=q_\xi'(\xi_j)H_s(\xi_j).
\]

This gives the exact corrected higher-moment formula.

### Theorem 5.1 - Corrected higher moments

After the unique lower-moment correction,

\[
\boxed{
\delta U_{m+s}
=
\sum_{j=1}^m
u_jq_\xi'(\xi_j)H_s(\xi_j)\,\delta\xi_j
}
\]

for every \(s\ge0\).

No approximation or asymptotic expansion is used.

## 6. The full corrected position matrix

For \(0\le s\le m-1\), define

\[
C^{\mathrm{full}}_{sj}(\xi,u)
=
 u_jq_\xi'(\xi_j)H_s(\xi_j).
\]

Then

\[
\begin{pmatrix}
\delta U_m\\
\delta U_{m+1}\\
\vdots\\
\delta U_{2m-1}
\end{pmatrix}
=
C^{\mathrm{full}}(\xi,u)
\begin{pmatrix}
\delta\xi_1\\
\vdots\\
\delta\xi_m
\end{pmatrix}.
\]

The matrix factors as

\[
C^{\mathrm{full}}
=
\bigl[H_s(\xi_j)\bigr]_{0\le s\le m-1,\,1\le j\le m}
\operatorname{diag}
\bigl(u_jq_\xi'(\xi_j)\bigr).
\]

## 7. Vandermonde-cubic determinant

Because each \(H_s\) is monic of degree \(s\), the transition from

\[
1,t,\ldots,t^{m-1}
\]

to

\[
H_0,H_1,\ldots,H_{m-1}
\]

is unit upper triangular. Consequently,

\[
\det\bigl[H_s(\xi_j)\bigr]
=
\prod_{i<j}(\xi_j-\xi_i).
\]

Also,

\[
q_\xi'(\xi_j)
=
\prod_{k\ne j}(\xi_j-\xi_k).
\]

Multiplying over \(j\) gives

\[
\prod_{j=1}^m q_\xi'(\xi_j)
=
(-1)^{m(m-1)/2}
\prod_{i<j}(\xi_j-\xi_i)^2.
\]

Therefore:

### Theorem 7.1 - Corrected collision determinant

\[
\boxed{
\det C^{\mathrm{full}}(\xi,u)
=
(-1)^{m(m-1)/2}
\left(\prod_{j=1}^m u_j\right)
\left(\prod_{i<j}(\xi_j-\xi_i)\right)^3
}
\]

up to the sign chosen for the Vandermonde ordering convention.

Equivalently,

\[
\boxed{
\det C^{\mathrm{full}}
=\pm\left(\prod_j u_j\right)\Delta(\xi)^3.
}
\]

### Corollary 7.2 - Exact nondegeneracy locus

The corrected map

\[
\delta\xi
\longmapsto
(\delta U_m,\ldots,\delta U_{2m-1})
\]

is an isomorphism exactly when

\[
\prod_j u_j\ne0
\]

and

\[
\Delta(\xi)=\prod_{i<j}(\xi_j-\xi_i)\ne0.
\]

Thus the algebraic nondegenerate ordered face is

\[
\boxed{
\mathcal B_m^\circ
=
\{\Delta(\xi)\ne0\}
\cap
\left\{\prod_j u_j\ne0\right\},
}
\]

before imposing the chosen center and scale normalization.

## 8. Boundary behavior

The determinant formula identifies two distinct degeneration mechanisms.

### 8.1 Vanishing weight

If one weight tends to zero while the nodes remain separated, one column of the corrected position matrix vanishes linearly:

\[
C^{\mathrm{full}}_{\bullet j}
=
 u_jq_\xi'(\xi_j)
\begin{pmatrix}
H_0(\xi_j)\\
\vdots\\
H_{m-1}(\xi_j)
\end{pmatrix}.
\]

Generically,

\[
\sigma_{\min}(C^{\mathrm{full}})\asymp |u_j|.
\]

This predicts numerical loss of resolution as an individual weight approaches zero without implying a Smith-spectrum jump at any nonzero weight.

### 8.2 Nested node collision

If \(\xi_i-\xi_j\to0\), then

\[
\det C^{\mathrm{full}}
=O\bigl((\xi_i-\xi_j)^3\bigr).
\]

The cubic loss explains the rapid onset of numerical instability near a nested collision. Such configurations lie outside the common-scale open stratum and require a separate multiscale or collision-tree analysis.

## 9. Relation to the missing grade

The full corrected matrix contains the rows

\[
\delta U_m,\delta U_{m+1},\ldots,\delta U_{2m-1}.
\]

It is invertible on the unrestricted node-variation space. Therefore the Newton recurrence alone does not imply

\[
\delta U_m=0
\]

for arbitrary shape variation.

The intended collision chart decomposes physical node variations as

\[
\delta x_j
=
\delta c+\xi_j\delta h+h\delta\xi_j,
\]

with center and scale separated from normalized shape. The complete Smith-spectrum theorem must identify the unique affine or gauge direction represented by the degree-\(m\) corrected moment and prove that it contributes no new associated-graded line after passing to normalized collision coordinates.

The remaining theorem target is therefore:

> identify explicitly the one-dimensional center, scale, or triangular correction responsible for removing the degree-\(m\) row from the normalized shape block.

Until that calculation is written, this note claims only the full corrected determinant theorem.

## 10. Claim ledger

| Statement | Status |
|---|---|
| Lower weight moments are independently controllable for distinct nodes | Proved |
| Base-moment nonvanishing is unnecessary | Proved |
| Corrected higher-moment formula using \(q_\xi' H_s\) | Proved |
| Full corrected determinant equals \(\pm(\prod u_j)\Delta^3\) | Proved |
| Nondegenerate open stratum is distinct nodes with nonzero individual weights | Proved for the unrestricted corrected position map |
| Numerical singular-value exponents equal the full Smith spectrum for every \(m\) | Not proved here |
| The degree-\(m\) associated grade vanishes | Open in this note |
| The collision root spaces globalize to holomorphic bundles | Open in this note |
| The construction descends to unordered clusters | Open in this note |
