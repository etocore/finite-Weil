# Metric volume and structural identities for packet collisions

## Status

This note records the geometric consequences of the established Jacobian factorization and determinant formula for the finite exponential moment map

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

## 1. Exact realization-metric volume form

### Theorem 1.1

In interleaved coordinates,

\[
\det J
=
\left(\prod_{j=1}^N u_j\right)
\prod_{1\le i<j\le N}(x_j-x_i)^4.
\]

Therefore

\[
\boxed{
\det G
=
\left(\prod_{j=1}^N|u_j|^2\right)
\prod_{1\le i<j\le N}|x_j-x_i|^8.
}
\]

On a real parameter slice, the associated Riemannian volume density is

\[
\boxed{
d\operatorname{vol}_G
=
\left(\prod_{j=1}^N|u_j|\right)
\prod_{1\le i<j\le N}|x_j-x_i|^4\,d\theta.
}
\]

Here \(d\theta\) denotes the Euclidean coordinate density on the chosen real slice.

### Proof

For every square complex matrix \(J\),

\[
\det(J^*J)
=
\det(J^*)\det(J)
=
\overline{\det J}\,\det J
=
|\det J|^2.
\]

Substituting the exact packet determinant gives

\[
\det G
=
\left|\left(\prod_{j=1}^N u_j\right)
\prod_{i<j}(x_j-x_i)^4\right|^2,
\]

which is the displayed determinant formula. Taking the positive square root gives the real Riemannian volume density. \(\square\)

### Corollary 1.2

Across a simple collision hyperplane \(x_i=x_j\), with all other factors nonzero,

\[
d\operatorname{vol}_G
\sim
|x_i-x_j|^4\,d\theta.
\]

Hence every simple collision divisor has fourth-order volume vanishing.

For an \(m\)-node common-scale collision

\[
x_j=x+h\xi_j,
\]

one has

\[
\prod_{1\le i<j\le m}|x_j-x_i|^4
=
|h|^{4\binom m2}
\prod_{1\le i<j\le m}|\xi_j-\xi_i|^4,
\]

so the volume density collapses at order

\[
\boxed{|h|^{2m(m-1)}.}
\]

This is the square-root counterpart of the metric-determinant collapse order

\[
|h|^{4m(m-1)}.
\]

---

## 2. Canonical exponent filtration and chart invariance

Let the adapted diagonal normal form be

\[
D(h)=\operatorname{diag}(h^{e_1},\ldots,h^{e_{2N}}),
\qquad
0\le e_1\le\cdots\le e_{2N}.
\]

For each threshold \(q\), define

\[
F^q
=
\operatorname{span}\{e_i:e_i\ge q\}
\]

in the model rescaled fiber.

### Theorem 2.1

The subspaces \(F^q\) define an intrinsic filtration of the ordered packet-rescaled tangent bundle. Under an overlap map between ordered blow-up charts, the transition matrix preserves every filtration level.

### Proof

In an ordered chart \(\alpha\), let

\[
J=A_\alpha D_\alpha B_\alpha,
\qquad
T_\alpha=B_\alpha^{-1}D_\alpha^{-1}.
\]

On an overlap with a chart \(\beta\), both rescaled frames represent the same lifted realization differential, so

\[
J T_\alpha=A_\alpha,
\qquad
J T_\beta=A_\beta.
\]

Hence

\[
T_\beta=T_\alpha G_{\alpha\beta},
\qquad
G_{\alpha\beta}=A_\alpha^{-1}A_\beta,
\]

up to the fixed convention for left-versus-right frame matrices. Since \(A_\alpha\) and \(A_\beta\) extend analytically and invertibly to the collision face, \(G_{\alpha\beta}\) is an analytic invertible gauge.

The filtration is characterized by asymptotic realization order: a rescaled vector lies in \(F^q\) precisely when its ordinary representative acquires at least \(q\) powers of the collision scale before applying the bounded analytic factors. This order is independent of the chosen adapted chart because the overlap gauge is bounded and invertible at the boundary. Therefore each \(G_{\alpha\beta}\) maps \(F^q_\beta\) isomorphically onto \(F^q_\alpha\). \(\square\)

### Corollary 2.2

For an \(m\)-node common-scale cluster, the nonzero filtration exponents are

\[
\boxed{
1,2,\ldots,m-1,m+1,\ldots,2m-1.
}
\]

The absence of exponent \(m\) is therefore a chart-independent structural feature, not an artifact of one normal-form calculation.

---

## 3. Metric eigenvalues and singular values

### Proposition 3.1

Let

\[
\sigma_1(J)\ge\cdots\ge\sigma_n(J)\ge0
\]

be the singular values of \(J\), and let

\[
\lambda_1(G)\ge\cdots\ge\lambda_n(G)\ge0
\]

be the eigenvalues of \(G=J^*J\). Then

\[
\boxed{
\lambda_i(G)=\sigma_i(J)^2,
\qquad 1\le i\le n.
}
\]

### Proof

Take an SVD

\[
J=U\Sigma V^*.
\]

Then

\[
G=J^*J=V\Sigma^2V^*,
\]

so the eigenvalues of \(G\) are the squared singular values of \(J\). \(\square\)

### Corollary 3.2

If the collapsing singular-value exponents are

\[
1,2,\ldots,m-1,m+1,\ldots,2m-1,
\]

then the collapsing metric-eigenvalue exponents are

\[
\boxed{
2,4,\ldots,2m-2,
2m+2,2m+4,\ldots,4m-2.
}
\]

---

## 4. Kernel and rank identities

### Proposition 4.1

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

If \(Jv=0\), then \(J^*Jv=0\). Conversely, if \(J^*Jv=0\), then

\[
0=v^*J^*Jv=\|Jv\|^2,
\]

so \(Jv=0\). Rank equality follows from rank-nullity. \(\square\)

### Corollary 4.2

At an \(m\)-node common-scale collision,

\[
\operatorname{rank}J(0)=2N-2m+2,
\]

and therefore

\[
\boxed{
\operatorname{rank}G(0)=2N-2m+2,
\qquad
\operatorname{corank}G(0)=2m-2.
}
\]

---

## 5. Renormalized metric determinant and positivity

Assume the proved cluster normal form

\[
J(h)=A(h)D(h)B(h)
\]

and define the rescaled tangent frame

\[
T(h)=B(h)^{-1}D(h)^{-1}.
\]

Then

\[
J(h)T(h)=A(h)
\]

and the renormalized pullback metric is

\[
\widetilde G(h)
=
T(h)^*J(h)^*J(h)T(h)
=
A(h)^*A(h).
\]

### Proposition 5.1

\[
\boxed{
\det\widetilde G(h)=|\det A(h)|^2.
}
\]

If \(A(0)=A_0\in GL(2N,\mathbb C)\), then

\[
\boxed{
\det\widetilde G(0)=|\det A_0|^2>0.
}
\]

### Proof

Apply the identity

\[
\det(C^*C)=|\det C|^2
\]

with \(C=A(h)\). \(\square\)

### Proposition 5.2

The boundary metric is positive definite:

\[
\boxed{
\widetilde G(0)=A_0^*A_0>0.
}
\]

### Proof

For every nonzero \(v\),

\[
v^*\widetilde G(0)v
=
\|A_0v\|^2>0,
\]

because \(A_0\) is invertible. \(\square\)

---

## 6. Rescaled-frame differential identities

The ordinary differential at the collision face is

\[
d\mathcal R_N\big|_{h=0}=J(0),
\]

which is rank-deficient. The invertible limit appears only after reading the differential in the rescaled tangent frame.

### Proposition 6.1

Let \(\mathsf X\) denote the ordered packet-rescaled tangent frame represented by \(T(h)\). Then

\[
\boxed{
[d\mathcal R_N]_{\mathsf X}
=
J(h)T(h)
=
A(h).
}
\]

Consequently,

\[
\boxed{
[d\mathcal R_N]_{\mathsf X,h=0}
=
A_0:
{}^{\mathrm{cl}}T_0\longrightarrow\mathbb C^{2N},
}
\]

and this boundary map is an isomorphism.

### Proof

This is the exact normal-form identity

\[
J(h)B(h)^{-1}D(h)^{-1}=A(h),
\]

followed by analytic continuation to \(h=0\). \(\square\)

### Corollary 6.2

After target normalization

\[
Y=A_0^{-1}(\mathcal R_N-R_0),
\]

one has

\[
\boxed{
[dY]_{\mathsf X}
=
A_0^{-1}A(h),
}
\]

and therefore

\[
\boxed{
[dY]_{\mathsf X,h=0}=I.
}
\]

These are rescaled-frame statements. They do not assert that the ordinary coordinate differential at \(h=0\) is invertible.

---

## 7. Exact determinant collapse and renormalization

For an \(m\)-node common-scale cluster,

\[
\det D(h)=h^{2m(m-1)}.
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
\det J=\det A\,\det D\,\det B,
\]

we have

\[
\det G=|\det A|^2|\det D|^2|\det B|^2.
\]

Using

\[
|\det D(h)|^2=|h|^{4m(m-1)}
\]

gives the formula. \(\square\)

### Corollary 7.2

The renormalized metric removes exactly the collapsing determinant factor:

\[
\boxed{
\det\widetilde G(h)
=
\frac{\det G(h)}{|\det D(h)|^2|\det B(h)|^2}
=
|\det A(h)|^2.
}
\]

Thus the ordinary metric determinant collapses at order

\[
|h|^{4m(m-1)},
\]

while the renormalized determinant converges to

\[
|\det A_0|^2>0.
\]

---

## 8. Geometric interpretation

The identities above separate two distinct structures.

The ordinary realization metric records the singular geometry of packet collisions through the explicit density

\[
\left(\prod_j|u_j|\right)|\Delta(X)|^4.
\]

The packet-rescaled tangent bundle removes precisely the realization-induced anisotropic collapse. In that frame, the differential and metric extend as

\[
[d\mathcal R_N]_{\mathsf X}=A(h),
\qquad
\widetilde G=A(h)^*A(h),
\]

with nondegenerate boundary values.

Accordingly, the collision blow-up and the spectral rescaling should be distinguished:

- the blow-up resolves node-configuration geometry;
- the exponent filtration and renormalized metric are induced by the Prony realization map.
