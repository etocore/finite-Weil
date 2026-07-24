# Complete singular-value constants for a common-scale packet cluster

## Status

This note completes the Euclidean singular-value asymptotics for the common-scale cluster normal form of the finite exponential moment map

\[
\mathcal R_N(X,u)
=
(a_0,\ldots,a_{2N-1}),
\qquad
 a_k=\sum_{j=1}^N u_jx_j^k.
\]

For an \(m\)-node cluster

\[
x_j(h)=x+h\xi_j,
\qquad 1\le j\le m,
\]

with fixed pairwise distinct offsets, the preceding normal-form theorem proves that the collapsing singular-value exponents are

\[
1,2,\ldots,m-1,m+1,m+2,\ldots,2m-1.
\]

The preceding inverse-Hermite calculation identifies the exact constant only for the deepest exponent \(2m-1\). The purpose of this note is to identify the exact leading constant at every exponent.

The main device is the exterior-power filtration of an analytic diagonal normal form. It yields:

1. exact limits for every cumulative product of the smallest singular values;
2. exact individual constants by taking successive ratios;
3. a Gram-minor formula;
4. an equivalent successive orthogonal-projection formula.

The argument is finite-dimensional and self-contained once the cluster normal form is known.

---

## 1. Abstract analytic diagonal normal form

Let \(n\ge1\), and suppose that for \(h>0\)

\[
J(h)=A(h)D(h)B(h),
\]

where \(A(h)\) and \(B(h)\) extend continuously to \(h=0\), and

\[
A_0:=A(0),
\qquad
B_0:=B(0)
\]

are invertible.

Assume

\[
D(h)=\operatorname{diag}
\bigl(h^{e_1},\ldots,h^{e_n}\bigr),
\qquad
0\le e_1\le\cdots\le e_n.
\]

Suppose that the positive exponents are distinct. Write them as

\[
0<f_1<f_2<\cdots<f_s,
\]

so that

\[
e_{n-s+r}=f_r,
\qquad 1\le r\le s.
\]

For \(1\le k\le s\), define the index set of the \(k\) deepest scales

\[
I_k:=\{n-k+1,\ldots,n\}
\]

and their exponent sum

\[
S_k:=\sum_{i\in I_k}e_i
=
\sum_{r=s-k+1}^s f_r.
\]

Let \(e_I\) denote the standard exterior basis vector in \(\bigwedge^k\mathbb C^n\) associated with an increasing index set \(I\).

Define

\[
R_k
:=
\left\|
\left(\bigwedge^k B_0^{-1}\right)e_{I_k}
\right\|,
\]

\[
L_k
:=
\left\|
\left(\bigwedge^k A_0^{-*}\right)e_{I_k}
\right\|,
\]

and

\[
C_k:=R_kL_k.
\]

Here

\[
A_0^{-*}:=(A_0^{-1})^*.
\]

Set

\[
C_0:=1.
\]

---

## 2. Rank-one limits of exterior powers

### Theorem 2.1 - exterior-power filtration

For every \(1\le k\le s\),

\[
\boxed{
 h^{S_k}\bigwedge^k J(h)^{-1}
 \longrightarrow
 \left(\bigwedge^k B_0^{-1}\right)e_{I_k}
 \left[
 \left(\bigwedge^k A_0^{-*}\right)e_{I_k}
 \right]^*
}
\]

in operator norm.

The limiting operator has rank one, and

\[
\boxed{
\lim_{h\to0^+}
 h^{S_k}
 \left\|\bigwedge^k J(h)^{-1}\right\|
 =C_k.
}
\]

### Proof

Since

\[
J(h)^{-1}
=
B(h)^{-1}D(h)^{-1}A(h)^{-1},
\]

functoriality of exterior powers gives

\[
\bigwedge^k J(h)^{-1}
=
\left(\bigwedge^k B(h)^{-1}\right)
\left(\bigwedge^k D(h)^{-1}\right)
\left(\bigwedge^k A(h)^{-1}\right).
\]

In the standard exterior basis,

\[
\left(\bigwedge^k D(h)^{-1}\right)e_I
=
h^{-E_I}e_I,
\qquad
E_I:=\sum_{i\in I}e_i.
\]

Because the positive exponents are distinct, the unique \(k\)-element index set maximizing \(E_I\) is

\[
I_k=\{n-k+1,\ldots,n\},
\]

and the maximum is \(S_k\). Therefore

\[
h^{S_k}\bigwedge^k D(h)^{-1}
\longrightarrow
e_{I_k}e_{I_k}^*.
\]

The exterior powers of \(A(h)^{-1}\) and \(B(h)^{-1}\) converge to the corresponding exterior powers of \(A_0^{-1}\) and \(B_0^{-1}\). Multiplying the limits gives

\[
 h^{S_k}\bigwedge^k J(h)^{-1}
 \longrightarrow
 \left(\bigwedge^k B_0^{-1}\right)e_{I_k}
 e_{I_k}^*
 \left(\bigwedge^k A_0^{-1}\right).
\]

The right covector is represented by

\[
\left(\bigwedge^k A_0^{-*}\right)e_{I_k}.
\]

Thus the limit is the stated rank-one operator. The norm of a rank-one operator \(ab^*\) is \(\|a\|\|b\|\), yielding \(C_k\). \(\square\)

---

## 3. Cumulative products and individual constants

The singular values of an exterior power are all products of \(k\) singular values of the original operator. In particular,

\[
\left\|\bigwedge^k J(h)^{-1}\right\|
=
\prod_{j=1}^k\sigma_j(J(h)^{-1})
=
\frac1{\prod_{j=0}^{k-1}\sigma_{n-j}(J(h))}.
\]

Combining this identity with Theorem 2.1 gives the cumulative product theorem.

### Theorem 3.1 - exact cumulative constants

For every \(1\le k\le s\),

\[
\boxed{
\lim_{h\to0^+}
\frac{
\displaystyle
\prod_{j=0}^{k-1}\sigma_{n-j}(J(h))
}{h^{S_k}}
=
\frac1{C_k}.
}
\]

### Corollary 3.2 - complete individual constant hierarchy

For \(1\le k\le s\), the singular value whose exponent is

\[
f_{s-k+1}
\]

satisfies

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_{n-k+1}(J(h))}{h^{f_{s-k+1}}}
=
\frac{C_{k-1}}{C_k}.
}
\]

### Proof

Let

\[
P_k(h)
:=
\prod_{j=0}^{k-1}\sigma_{n-j}(J(h)).
\]

Theorem 3.1 gives

\[
P_k(h)
\sim
\frac{h^{S_k}}{C_k}.
\]

Since

\[
\sigma_{n-k+1}(J(h))
=
\frac{P_k(h)}{P_{k-1}(h)},
\]

and

\[
S_k-S_{k-1}=f_{s-k+1},
\]

taking the ratio yields the result. \(\square\)

Thus every collapsing singular value has an exact leading constant. No recursive singular-vector perturbation is required.

---

## 4. Successive orthogonal-projection formula

Order the positive-scale coordinates from deepest to shallowest. Let

\[
i_k:=n-k+1,
\qquad 1\le k\le s.
\]

Define right and left graded vectors

\[
r_k:=B_0^{-1}e_{i_k},
\qquad
\ell_k:=A_0^{-*}e_{i_k}.
\]

Set

\[
\widehat r_1:=r_1,
\qquad
\widehat\ell_1:=\ell_1,
\]

and for \(k\ge2\),

\[
\widehat r_k
:=
P_{\operatorname{span}(r_1,\ldots,r_{k-1})^\perp}r_k,
\]

\[
\widehat\ell_k
:=
P_{\operatorname{span}(\ell_1,\ldots,\ell_{k-1})^\perp}\ell_k.
\]

Because \(A_0\) and \(B_0\) are invertible, every projected vector is nonzero.

The exterior-volume identity gives

\[
R_k
=
R_{k-1}\|\widehat r_k\|,
\qquad
L_k
=
L_{k-1}\|\widehat\ell_k\|.
\]

Therefore Corollary 3.2 becomes:

### Theorem 4.1 - successive filtration formula

For the singular value with exponent \(f_{s-k+1}\),

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_{n-k+1}(J(h))}{h^{f_{s-k+1}}}
=
\frac1{
\|\widehat r_k\|
\|\widehat\ell_k\|
}.
}
\]

This is the desired complete effective-map filtration. Each scale is the reciprocal product of:

1. the new right-domain volume surviving after removing all deeper parameter directions;
2. the new left-codomain volume surviving after removing all deeper moment covectors.

---

## 5. Gram-minor formula

The same constants can be computed without explicitly performing Gram-Schmidt.

Let

\[
G_k^R
:=
\left[
(B_0^{-*}B_0^{-1})_{ij}
\right]_{i,j\in I_k},
\]

and

\[
G_k^L
:=
\left[
(A_0^{-1}A_0^{-*})_{ij}
\right]_{i,j\in I_k}.
\]

Then

\[
R_k^2=\det G_k^R,
\qquad
L_k^2=\det G_k^L.
\]

Consequently,

\[
\boxed{
C_k^2
=
\det G_k^R\det G_k^L
}
\]

and

\[
\boxed{
\lim_{h\to0^+}
\frac{\sigma_{n-k+1}(J(h))}{h^{f_{s-k+1}}}
=
\left(
\frac{
\det G_{k-1}^R\det G_{k-1}^L
}{
\det G_k^R\det G_k^L
}
\right)^{1/2},
}
\]

with the convention that the zero-dimensional determinants equal \(1\).

This gives a finite, exact, machine-checkable formula for the entire collapsing spectrum.

---

## 6. Application to the packet-cluster normal form

For the packet cluster, the positive exponents are

\[
\boxed{
f_1,\ldots,f_{2m-2}
=
1,2,\ldots,m-1,m+1,m+2,\ldots,2m-1.
}
\]

The transformed columns in increasing exponent order are

\[
D_1,\ldots,D_{m-1},
V_{m+1},\ldots,V_{2m-1}.
\]

Thus the deepest-to-shallowest order used in Theorem 4.1 is

\[
\boxed{
V_{2m-1},V_{2m-2},\ldots,V_{m+1},
D_{m-1},D_{m-2},\ldots,D_1.
}
\]

From the exact factorization in `paper/m-node-cluster-normal-form.md`,

\[
J(h)=A(h)D_m(h)B(h),
\qquad
B(h)=P(h)^{-1}U(h).
\]

Therefore

\[
B_0^{-1}=U_0^{-1}P_0.
\]

For every positive-scale transformed coordinate \(i_k\), define

\[
r_k
=
U_0^{-1}P_0e_{i_k},
\qquad
\ell_k
=
A_0^{-*}e_{i_k}.
\]

Successively project these vectors away from the deeper vectors as in Section 4. The exact constant at the corresponding cluster exponent is

\[
\boxed{
 c_{i_k}
 =
 \frac1{
 \|P_{\operatorname{span}(r_1,\ldots,r_{k-1})^\perp}r_k\|
 \|P_{\operatorname{span}(\ell_1,\ldots,\ell_{k-1})^\perp}\ell_k\|
 }.
}
\]

This formula exhibits the coefficient dependence precisely:

- the value-Hermite modes are unaffected by \(U_0^{-1}\), so the deepest value-side scales are coefficient independent;
- the derivative-dual modes pass through the motion-coordinate entries of \(U_0^{-1}\), so their constants generally depend on the nonzero cluster coefficients;
- the left factors depend only on the limiting confluent jet geometry and the exterior nodes.

The deepest case \(k=1\) recovers the previously proved rank-one inverse constant.

---

## 7. Symmetric three-node cluster: all four constants

Take

\[
m=N=3,
\qquad
x=0,
\qquad
(\xi_1,\xi_2,\xi_3)=(-1,0,1),
\]

and

\[
u_1=u_2=u_3=1.
\]

Use grouped parameter coordinates

\[
(u_1,u_2,u_3,x_1,x_2,x_3).
\]

The positive exponents are

\[
1,2,4,5.
\]

The deepest-to-shallowest transformed modes are

\[
V_5,V_4,D_2,D_1.
\]

The corresponding right graded vectors are

\[
r_1
=
\left(\frac34,0,-\frac34,0,0,0\right)^{\mathsf T},
\]

\[
r_2
=
\left(-\frac12,1,-\frac12,0,0,0\right)^{\mathsf T},
\]

\[
r_3
=
\left(0,0,0,\frac12,-1,\frac12\right)^{\mathsf T},
\]

\[
r_4
=
\left(0,0,0,-\frac12,0,\frac12\right)^{\mathsf T}.
\]

These four vectors are mutually orthogonal. Their norms are

\[
\frac{3}{2\sqrt2},
\qquad
\sqrt{\frac32},
\qquad
\sqrt{\frac32},
\qquad
\frac1{\sqrt2}.
\]

At the origin, the normalized limiting jet columns are

\[
V_5\longmapsto e_6,
\qquad
V_4\longmapsto e_5,
\qquad
D_2\longmapsto3e_4,
\qquad
D_1\longmapsto2e_3.
\]

Hence the left graded vectors are mutually orthogonal with norms

\[
1,
\qquad
1,
\qquad
\frac13,
\qquad
\frac12.
\]

The complete collapsing spectrum is therefore

\[
\boxed{
\sigma_3(J(h))
\sim
2\sqrt2\,h,
}
\]

\[
\boxed{
\sigma_4(J(h))
\sim
\sqrt6\,h^2,
}
\]

\[
\boxed{
\sigma_5(J(h))
\sim
\sqrt{\frac23}\,h^4,
}
\]

and

\[
\boxed{
\sigma_6(J(h))
\sim
\frac{2\sqrt2}{3}\,h^5.
}
\]

The last formula agrees with the previously derived deepest constant.

As a consistency check, the product of the four constants is

\[
(2\sqrt2)(\sqrt6)
\left(\sqrt{\frac23}\right)
\left(\frac{2\sqrt2}{3}\right)
=
\frac{16}{3}.
\]

At \(h=0\), the two nonzero singular values of the collision Jacobian are both \(\sqrt3\), so their product is \(3\). The exact determinant coefficient for the nodes \((-h,0,h)\) is \(16h^{12}\). Hence

\[
3\cdot\frac{16}{3}=16,
\]

which matches the determinant theorem exactly.

---

## 8. What is proved and what remains open

### Proved here

- Every cumulative product of the smallest cluster singular values has an exact leading constant.
- Every individual collapsing singular value has an exact leading constant.
- The constants are finite exterior-volume ratios determined by \(A_0\) and \(B_0\).
- The same constants admit successive orthogonal-projection formulas.
- The same constants admit principal Gram-minor formulas.
- The construction is finite and machine-checkable for every fixed cluster shape, coefficient vector, center, and exterior geometry.
- The complete symmetric three-node spectrum is computed explicitly.

### Still open

- Closed scalar formulas for every intermediate constant comparable to the deepest shape formula \(\Gamma(\xi)^{-1}\).
- A basis-free interpretation of all intermediate right-side factors directly in terms of cluster polynomials.
- Several clusters collapsing simultaneously.
- Nonuniform paths in which different separations vanish at different powers of \(h\).
- Confluent coordinate extension and metric completion.
- Sharp global lower bounds away from a prescribed collection of cluster strata.

The next geometric target is to pass from ordinary node coordinates to confluent jet coordinates and determine whether the anisotropically renormalized pullback metric extends across the collision strata.