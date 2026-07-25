# Derived metric identities for packet collisions

## Status

This note proves several consequences that follow directly from the established Jacobian factorization and determinant formula for the finite exponential moment map

\[
\mathcal R_N(X,u)
=
\left(\sum_{j=1}^N u_jx_j^k\right)_{k=0}^{2N-1}.
\]

Let

\[
J=D\mathcal R_N,
\qquad
G=J^*J.
\]

Assume throughout that the ordinary parameter and moment spaces carry their standard Hermitian inner products.

---

## 1. Exact determinant of the pullback metric

### Proposition 1.1

For every square complex matrix \(J\),

\[
\boxed{
\det(J^*J)=|\det J|^2.
}
\]

### Proof

Using multiplicativity of the determinant,

\[
\det(J^*J)
=
\det(J^*)\det(J).
\]

Since

\[
\det(J^*)=\overline{\det J},
\]

we obtain

\[
\det(J^*J)
=
\overline{\det J}\,\det J
=
|\det J|^2.
\]

This proves the identity. \(\square\)

Applying the exact packet determinant formula gives the following.

### Corollary 1.2

In interleaved coordinates,

\[
\det J
=
\left(\prod_{j=1}^N u_j\right)
\prod_{1\le i<j\le N}(x_j-x_i)^4,
\]

and therefore

\[
\boxed{
\det G
=
\left(\prod_{j=1}^N|u_j|^2\right)
\prod_{1\le i<j\le N}|x_j-x_i|^8.
}
\]

The same formula holds in grouped coordinates because the coordinate-ordering sign disappears after taking absolute value squared.

---

## 2. Equality of metric eigenvalues and squared singular values

### Proposition 2.1

Let

\[
\sigma_1(J)\ge\cdots\ge\sigma_n(J)\ge0
\]

be the singular values of \(J\), and let

\[
\lambda_1(G)\ge\cdots\ge\lambda_n(G)\ge0
\]

be the eigenvalues of

\[
G=J^*J.
\]

Then

\[
\boxed{
\lambda_i(G)=\sigma_i(J)^2,
\qquad 1\le i\le n.
}
\]

### Proof

Take a singular-value decomposition

\[
J=U\Sigma V^*,
\]

where \(U,V\) are unitary and

\[
\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_n).
\]

Then

\[
G
=
J^*J
=
V\Sigma^*U^*U\Sigma V^*
=
V\Sigma^2V^*.
\]

Thus \(G\) is unitarily similar to

\[
\operatorname{diag}(\sigma_1^2,\ldots,\sigma_n^2),
\]

which proves the claim. \(\square\)

### Corollary 2.2

If the collapsing singular-value exponents for an \(m\)-node common-scale cluster are

\[
1,2,\ldots,m-1,m+1,\ldots,2m-1,
\]

then the collapsing pullback-metric eigenvalue exponents are

\[
\boxed{
2,4,\ldots,2m-2,
2m+2,2m+4,\ldots,4m-2.
}
\]

---

## 3. Equality of Jacobian rank and metric rank

### Proposition 3.1

For every complex matrix \(J\),

\[
\boxed{
\ker(J^*J)=\ker J.
}
\]

Hence

\[
\boxed{
\operatorname{rank}(J^*J)=\operatorname{rank}J.
}
\]

### Proof

If \(Jv=0\), then clearly

\[
J^*Jv=0.
\]

Conversely, if

\[
J^*Jv=0,
\]

then

\[
0
=
v^*J^*Jv
=
\|Jv\|^2.
\]

Therefore \(Jv=0\). Thus the kernels agree. Equality of ranks follows from rank-nullity. \(\square\)

### Corollary 3.2

At an \(m\)-node common-scale collision,

\[
\operatorname{rank}J(0)=2N-2m+2,
\]

so

\[
\boxed{
\operatorname{rank}G(0)=2N-2m+2,
}
\]

and

\[
\boxed{
\operatorname{corank}G(0)=2m-2.
}
\]

---

## 4. Exact determinant of the renormalized metric

Assume the proved cluster normal form

\[
J(h)=A(h)D(h)B(h)
\]

and define

\[
T(h)=B(h)^{-1}D(h)^{-1}.
\]

The renormalized pullback metric is

\[
\widetilde G(h)
=
T(h)^*J(h)^*J(h)T(h).
\]

The established exact identity is

\[
\widetilde G(h)=A(h)^*A(h).
\]

### Proposition 4.1

\[
\boxed{
\det\widetilde G(h)
=
|\det A(h)|^2.
}
\]

### Proof

By the exact renormalized metric identity,

\[
\det\widetilde G(h)
=
\det(A(h)^*A(h)).
\]

Applying Proposition 1.1 with \(J=A(h)\) gives

\[
\det(A(h)^*A(h))
=
|\det A(h)|^2.
\]

This proves the result. \(\square\)

### Corollary 4.2

Since \(A(h)\) extends continuously or analytically to \(h=0\), and

\[
A(0)=A_0\in GL(2N,\mathbb C),
\]

we have

\[
\boxed{
\det\widetilde G(0)
=
|\det A_0|^2
>0.
}
\]

Hence the renormalized metric is nondegenerate at the collision face.

---

## 5. Positive definiteness of the boundary metric

### Proposition 5.1

If

\[
\widetilde G(0)=A_0^*A_0
\]

with \(A_0\in GL(2N,\mathbb C)\), then

\[
\boxed{
\widetilde G(0)>0.
}
\]

### Proof

For every nonzero vector \(v\),

\[
v^*\widetilde G(0)v
=
v^*A_0^*A_0v
=
\|A_0v\|^2.
\]

Because \(A_0\) is invertible,

\[
A_0v\ne0
\]

whenever \(v\ne0\). Therefore

\[
\|A_0v\|^2>0.
\]

Thus 

\[
\widetilde G(0)
\]

is positive definite. \(\square\)

---

## 6. Exact boundary differential isomorphism

The rescaled tangent frame satisfies

\[
J(h)T(h)=A(h).
\]

### Proposition 6.1

The lifted realization differential extends to an isomorphism at the collision face:

\[
\boxed{
[d\mathcal R_N]_{h=0}
=
A_0:
{}^{\mathrm{cl}}T_0
\longrightarrow
\mathbb C^{2N}.
}
\]

### Proof

For \(h>0\), the matrix of the realization differential in the rescaled frame is

\[
[d\mathcal R_N]_{\mathsf X}
=
J(h)T(h)
=
A(h).
\]

By continuity or analyticity,

\[
A(h)\to A_0.
\]

Since \(A_0\) is invertible, the limiting bundle map is an isomorphism. \(\square\)

### Corollary 6.2

After target normalization

\[
Y
=
A_0^{-1}(\mathcal R_N-R_0),
\]

we have

\[
\boxed{
[dY]_{h=0}=I.
}
\]

Indeed,

\[
[dY]_{\mathsf X}
=
A_0^{-1}A(h)
\longrightarrow
I.
\]

---

## 7. Exact metric-volume collapse and its renormalization

For an \(m\)-node common-scale cluster,

\[
\det D(h)
=
h^{2m(m-1)}.
\]

Since

\[
J=A D B,
\]

\[
\det J
=
\det A\,\det D\,\det B.
\]

Therefore

\[
\det G
=
|\det A|^2|\det D|^2|\det B|^2.
\]

### Proposition 7.1

\[
\boxed{
\det G(h)
=
|h|^{4m(m-1)}
|\det A(h)|^2
|\det B(h)|^2.
}
\]

### Proof

Since

\[
|\det D(h)|^2
=
|h|^{4m(m-1)},
\]

the result follows immediately from multiplicativity. \(\square\)

### Corollary 7.2

The renormalized metric removes exactly the collapsing volume factor:

\[
\boxed{
\det\widetilde G(h)
=
\frac{\det G(h)}
{|\det D(h)|^2|\det B(h)|^2}
=
|\det A(h)|^2.
}
\]

Thus the ordinary metric volume collapses at order

\[
|h|^{4m(m-1)},
\]

while the renormalized metric volume converges to the nonzero limit

\[
|\det A_0|^2.
\]

---

## 8. Canonical exponent filtration

Let the adapted diagonal normal form be

\[
D(h)=\operatorname{diag}(h^{e_1},\ldots,h^{e_{2N}}),
\qquad
0\le e_1\le\cdots\le e_{2N}.
\]

For each exponent threshold \(q\), define the model filtration subspace

\[
F^q
=
\operatorname{span}\{e_i:e_i\ge q\}.
\]

In the rescaled tangent bundle, define

\[
\mathcal F^q
=
T(h)F^q.
\]

### Proposition 8.1

Under an ordered-chart change with

\[
\widetilde h=\lambda(\xi)h,
\qquad
\lambda(\xi)\ne0,
\]

each graded factor transforms by multiplication with the nowhere-vanishing scalar

\[
\lambda(\xi)^e.
\]

Consequently, the ordered collection of exponent subspaces is chart-independent.

### Proof

For an exponent-\(e\) diagonal factor,

\[
\widetilde h^{\,e}
=
\lambda(\xi)^e h^e.
\]

Since 

\[
\lambda(\xi)^e\ne0,
\]

the one-dimensional graded line generated by the exponent-\(e\) factor is unchanged. Taking sums over all exponents at least \(q\) preserves the filtered subspace. \(\square\)

---

## 9. Summary of proved identities

The following are now explicit standalone propositions:

\[
\boxed{
\det G=|\det J|^2,
}
\]

\[
\boxed{
\det G
=
\left(\prod_j|u_j|^2\right)
\prod_{i<j}|x_j-x_i|^8,
}
\]

\[
\boxed{
\lambda_i(G)=\sigma_i(J)^2,
}
\]

\[
\boxed{
\ker G=\ker J,
\qquad
\operatorname{rank}G=\operatorname{rank}J,
}
\]

\[
\boxed{
\det\widetilde G=|\det A|^2,
\qquad
\widetilde G(0)=A_0^*A_0>0,
}
\]

\[
\boxed{
[d\mathcal R_N]_{h=0}=A_0,
\qquad
[dY]_{h=0}=I,
}
\]

\[
\boxed{
\det G(h)
=
|h|^{4m(m-1)}
|\det A(h)|^2
|\det B(h)|^2,
}
\]

and the exponent filtration is invariant under ordered-chart transitions up to nowhere-vanishing graded factors.

These results are direct consequences of the already proved packet normal form and do not address the still-open unordered quotient, nested clusters, simultaneous clusters, curvature, Lie algebroid, or global lower-bound problems.
