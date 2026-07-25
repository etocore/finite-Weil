# Varying-shape analytic cluster normal form

## Status

This note upgrades the fixed-shape common-scale cluster factorization to a full local theorem in the normalized shape variables.

For an ordered cluster of size \(m\ge2\), write

\[
x_j=x+h\xi_j,
\qquad 1\le j\le m,
\]

where the normalized shape \(\xi=(\xi_1,\ldots,\xi_m)\) varies in the configuration space

\[
\operatorname{Conf}_m(\mathbb C)
=
\{\xi\in\mathbb C^m:\xi_i\ne\xi_j\text{ for }i\ne j\}.
\]

The main conclusion is that the previously constructed factorization

\[
J(h,\xi)=A(h,\xi)D_m(h)B(h,\xi)
\]

can be chosen jointly holomorphic in \((h,\xi)\) on every sufficiently small product neighborhood of a nondegenerate shape. The diagonal exponent matrix is independent of \(\xi\), while the regular factors and their inverses are locally uniformly bounded.

This promotes all fixed-shape singular-value, rescaled-differential, and renormalized-metric statements to open neighborhoods in shape space.

---

## 1. Parameter domain

Fix a base configuration

\[
(x_0,\xi^0,u^0,y^0,v^0)
\]

such that

1. \(\xi_i^0\ne\xi_j^0\) for \(i\ne j\);
2. the exterior nodes \(y_{m+1}^0,\ldots,y_N^0\) are pairwise distinct and separated from \(x_0\);
3. every limiting coefficient is nonzero.

Choose neighborhoods

\[
\mathcal U_x,\quad
\mathcal U_\xi,\quad
\mathcal U_u,\quad
\mathcal U_{\rm ext}
\]

whose closures are compact and satisfy the uniform separation conditions

\[
\inf_{\xi\in\overline{\mathcal U_\xi}}
|\xi_i-\xi_j|>0,
\qquad i\ne j,
\]

and

\[
\inf
|y_\ell-x|>0,
\qquad
\inf
|y_\ell-y_r|>0
\]

over the chosen compact parameter set.

Let \(|h|<\varepsilon\), with \(\varepsilon\) small enough that the physical nodes remain distinct whenever \(h\ne0\).

The full parameter tuple is denoted

\[
p=(x,\xi,u,y,v).
\]

---

## 2. Analyticity of the Vandermonde-dual derivative weights

Let

\[
V_\xi=(\xi_j^q)_{0\le q\le m-1,\ 1\le j\le m}.
\]

Its determinant is the Vandermonde product

\[
\det V_\xi
=
\pm\Delta(\xi),
\qquad
\Delta(\xi)=\prod_{i<j}(\xi_j-\xi_i).
\]

Hence \(V_\xi\) is invertible throughout \(\mathcal U_\xi\), and

\[
V_\xi^{-1}
=
\frac{\operatorname{adj}(V_\xi)}{\det V_\xi}
\]

is holomorphic in \(\xi\).

For \(0\le q\le m-1\), let \(b^{(q)}(\xi)\) be the dual Vandermonde weights defined by

\[
\sum_{j=1}^m b_j^{(q)}(\xi)\xi_j^s
=
\delta_{qs},
\qquad 0\le s\le m-1.
\]

Thus every component of \(b^{(q)}(\xi)\) is holomorphic on \(\operatorname{Conf}_m(\mathbb C)\), and the family is uniformly bounded on \(\overline{\mathcal U_\xi}\).

Define

\[
D_q(h,p)
=
\sum_{j=1}^m b_j^{(q)}(\xi)M'(x+h\xi_j).
\]

The Taylor identity

\[
D_q(h,p)
=
\sum_{s\ge0}
\frac{h^s}{s!}
\left(\sum_j b_j^{(q)}(\xi)\xi_j^s\right)
M^{(s+1)}(x)
\]

shows that the first nonzero term occurs at \(s=q\). Therefore

\[
\widehat D_q(h,p)
:=
h^{-q}D_q(h,p)
\]

extends holomorphically to \(h=0\), with

\[
\widehat D_q(0,p)
=
\frac1{q!}M^{(q+1)}(x).
\]

The extension is jointly holomorphic in \((h,p)\).

---

## 3. Analyticity of the Hermite coefficient-extraction weights

Let \(H_\xi\) be the \(2m\times2m\) confluent Hermite matrix in the monomial basis,

\[
H_\xi p
=
\bigl(
 p(\xi_1),\ldots,p(\xi_m),
 p'(\xi_1),\ldots,p'(\xi_m)
\bigr).
\]

Its determinant satisfies

\[
\det H_\xi
=
\pm\Delta(\xi)^4.
\]

Thus \(H_\xi^{-1}\) is holomorphic on \(\operatorname{Conf}_m(\mathbb C)\).

For

\[
R_m=\{0\}\cup\{m+1,\ldots,2m-1\},
\]

let \(a^{(r)}(\xi)\) and \(c^{(r)}(\xi)\) be the Hermite weights representing coefficient extraction:

\[
[t^r]p
=
\sum_j a_j^{(r)}(\xi)p(\xi_j)
+
\sum_j c_j^{(r)}(\xi)p'(\xi_j).
\]

All entries of these weights are holomorphic functions of \(\xi\).

Define

\[
V_r(h,p)
=
\sum_j a_j^{(r)}(\xi)M(x+h\xi_j)
+
h\sum_j c_j^{(r)}(\xi)M'(x+h\xi_j).
\]

The coefficient-extraction identities give

\[
V_r(h,p)
=
\frac{h^r}{r!}M^{(r)}(x)+O(h^{2m}).
\]

Consequently

\[
\widehat V_r(h,p)
:=
h^{-r}V_r(h,p)
\]

extends jointly holomorphically through \(h=0\), with

\[
\widehat V_r(0,p)
=
\frac1{r!}M^{(r)}(x).
\]

---

## 4. The analytic column transformation

Let \(P_m(h,\xi)\) be the cluster-column transformation whose columns produce

\[
V_0,
D_0,D_1,\ldots,D_{m-1},
V_{m+1},\ldots,V_{2m-1}.
\]

Every entry of \(P_m\) is polynomial in \(h\) and holomorphic in \(\xi\).

At \(h=0\), after fixed permutations,

\[
P_m(0,\xi)
\sim
\begin{pmatrix}
A_m(\xi)&0\\
0&B_m(\xi)
\end{pmatrix},
\]

where \(B_m\) is the dual Vandermonde matrix and

\[
\det A_m(\xi)
=
\pm\frac{m!}{\Delta(\xi)^3}.
\]

Hence

\[
\det P_m(0,\xi)\ne0
\]

throughout \(\mathcal U_\xi\).

By compactness of \(\overline{\mathcal U_\xi}\), there exists \(\varepsilon>0\) such that

\[
\inf_{
|h|\le\varepsilon,
\xi\in\overline{\mathcal U_\xi}}
|\det P_m(h,\xi)|>0.
\]

Therefore \(P_m\) and \(P_m^{-1}\) are jointly holomorphic and locally uniformly bounded.

Extend \(P_m\) by the identity on all exterior columns and call the full transformation \(P(h,p)\).

---

## 5. The analytic regular factor

Form \(A(h,p)\) from the normalized transformed cluster columns

\[
\widehat V_0,
\widehat D_0,
\ldots,
\widehat D_{m-1},
\widehat V_{m+1},
\ldots,
\widehat V_{2m-1},
\]

followed by the unmodified exterior value and derivative columns.

Every entry of \(A(h,p)\) is jointly holomorphic.

At \(h=0\), its cluster columns are, up to factorial factors,

\[
M(x),M'(x),\ldots,M^{(2m-1)}(x),
\]

and its exterior columns are

\[
M(y_\ell),M'(y_\ell),
\qquad \ell>m.
\]

Thus \(A(0,p)^\mathsf T\) is the generalized Hermite data map with multiplicity \(2m\) at \(x\) and multiplicity \(2\) at every exterior node.

The uniform node-separation assumptions imply

\[
\det A(0,p)\ne0
\]

throughout the compact boundary parameter set. Consequently, after possibly shrinking the neighborhood,

\[
\inf|\det A(h,p)|>0.
\]

Hence \(A\) and \(A^{-1}\) are jointly holomorphic and locally uniformly bounded.

---

## 6. Exact varying-shape factorization

Let \(U(p)\) be the diagonal coefficient matrix in grouped coordinates. Since all coefficients stay nonzero, \(U\) and \(U^{-1}\) are holomorphic and locally uniformly bounded.

The transformed-column identity is

\[
C(h,p)P(h,p)
=
A(h,p)D_m(h),
\]

where

\[
D_m(h)
=
\operatorname{diag}
\Bigl(
\underbrace{1,\ldots,1}_{2N-2m+2},
 h,h^2,\ldots,h^{m-1},
 h^{m+1},\ldots,h^{2m-1}
\Bigr).
\]

Since \(J=C U\), define

\[
B(h,p):=P(h,p)^{-1}U(p).
\]

Then

\[
\boxed{
J(h,p)
=
A(h,p)D_m(h)B(h,p).
}
\]

Both regular factors and their inverses are jointly holomorphic and locally uniformly bounded.

---

## 7. Main theorem

### Theorem 7.1 - local analytic varying-shape normal form

Let \(p_0\) be a nondegenerate ordered cluster configuration with pairwise distinct normalized offsets, nonzero coefficients, and exterior nodes separated from the cluster center and from one another.

Then there is a product neighborhood of \((h,p)=(0,p_0)\) on which

\[
\boxed{
J(h,p)=A(h,p)D_m(h)B(h,p),
}
\]

where

1. \(D_m(h)\) is independent of the shape and has exponent list
   \[
   \underbrace{0,\ldots,0}_{2N-2m+2},
   1,2,\ldots,m-1,
   m+1,\ldots,2m-1;
   \]
2. \(A\), \(B\), \(A^{-1}\), and \(B^{-1}\) are jointly holomorphic in all chart variables;
3. these four matrices are uniformly bounded on every compact subchart.

### Proof

Sections 2 and 3 establish joint holomorphic dependence of all interpolation weights and normalized transformed columns. Section 4 proves joint holomorphic invertibility of the column transformation. Section 5 proves joint holomorphic invertibility of the regular jet-exterior factor. Section 6 combines the exact transformed-column identity with the nonvanishing coefficient matrix. \(\square\)

---

## 8. Consequences

### 8.1 Uniform singular-value estimates on compact shape sets

On every compact subchart there exist constants \(0<c\le C<\infty\) such that

\[
c\,\sigma_k(D_m(h))
\le
\sigma_k(J(h,p))
\le
C\,\sigma_k(D_m(h))
\]

for every \(k\), every parameter \(p\) in the subchart, and sufficiently small \(h\).

Thus the exponent hierarchy is uniform over compact nondegenerate shape families.

### 8.2 Analytic rescaled differential

Define

\[
T(h,p)=B(h,p)^{-1}D_m(h)^{-1}.
\]

Then

\[
\boxed{
J(h,p)T(h,p)=A(h,p),
}
\]

so the lifted realization differential extends jointly holomorphically over the full varying-shape chart.

### 8.3 Analytic renormalized metric

For

\[
G(h,p)=J(h,p)^*J(h,p),
\]

one has

\[
\boxed{
T(h,p)^*G(h,p)T(h,p)
=
A(h,p)^*A(h,p).
}
\]

Over the real parameter locus, this gives a real-analytic positive-definite metric on the cluster-rescaled tangent bundle through \(h=0\).

### 8.4 Analytic dependence of exact constants

The exterior-power constants and Gram-minor ratios depend analytically on the regular factors wherever the relevant Gram determinants do not vanish. Since the exponent filtration has simple positive exponents, every individual leading singular-value constant varies continuously, and locally real-analytically on the real nondegenerate shape locus.

---

## 9. What this theorem does not yet prove

This theorem constructs one local ordered chart. It does not yet prove:

1. compatibility between charts using different node pairs to define center and scale;
2. compatibility with cluster-node permutations;
3. extension through degenerations of normalized shape, where some \(\xi_i=\xi_j\);
4. simultaneous or nested clusters;
5. a global manifold-with-corners or Lie-algebroid structure.

The next theorem target is to derive explicit transition maps between ordered blow-up charts and determine how the exponent filtration and rescaled tangent frame transform under those transitions.
