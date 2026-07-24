# Exceptional widths are real: an explicit five-node family

## Status

This note answers the question left open after the generic-width theorem: the set

\[
Z_N=\bigcup_{r=0}^{N-3}\{\tau>0:g_r(\tau)=0\}
\]

need not be empty for arbitrary symmetric node sets.

The result does **not** show that local two-shift generation fails at such a width. It shows only that the second-order parity-chain certificate can fail. Higher even derivatives may restore the missing edge.

## 1. Five symmetric nodes

Take

\[
\{-a,-b,0,b,a\},\qquad a>b>0,
\]

and write

\[
K(v)_{ij}=e^{-v(x_i-x_j)^2/2},\qquad v=\frac1{2\tau}.
\]

The odd subspace has dimension two. In the normalized odd basis

\[
f_a=\frac{e_a-e_{-a}}{\sqrt2},\qquad
f_b=\frac{e_b-e_{-b}}{\sqrt2},
\]

the restriction of \(K(v)\) is

\[
B(v)=
\begin{pmatrix}
A(v)&C(v)\\
C(v)&D(v)
\end{pmatrix},
\]

where

\[
A(v)=1-e^{-2a^2v},
\qquad
D(v)=1-e^{-2b^2v},
\]

and

\[
C(v)
=e^{-(a-b)^2v/2}-e^{-(a+b)^2v/2}
=2e^{-(a^2+b^2)v/2}\sinh(abv).
\]

Since \(a>b\), one has

\[
\Delta(v):=A(v)-D(v)>0,
\qquad
C(v)>0
\]

for every \(v>0\). Thus the two eigenvalues of \(B(v)\) are simple.

By strict total positivity and the parity/oscillation ordering, these two odd eigenmodes are the global modes \(u_1\) and \(u_3\).

## 2. Exact zero criterion

For a real symmetric matrix

\[
B=
\begin{pmatrix}A&C\\C&D\end{pmatrix},
\]

let \(y_+,y_-\) be unit eigenvectors for the larger and smaller eigenvalues. Writing

\[
\Delta=A-D,
\]

a direct rotation-angle computation gives

\[
\left|\langle y_-,B' y_+\rangle\right|
=
\frac{|F(v)|}{\sqrt{\Delta(v)^2+4C(v)^2}},
\]

where

\[
\boxed{
F(v):=\Delta(v)C'(v)-C(v)\Delta'(v).
}
\]

Therefore

\[
\langle u_1,K'(v)u_3\rangle=0
\quad\Longleftrightarrow\quad
F(v)=0.
\]

For distinct eigenvectors,

\[
g_1(\tau)
=4\sqrt\pi\,\tau^{1/2}v^2
\langle u_1,K'(v)u_3\rangle,
\]

so \(g_1(\tau)=0\) is equivalent to \(F(v)=0\).

## 3. Sign change

As \(v\downarrow0\),

\[
\Delta(v)
=2(a^2-b^2)v-2(a^4-b^4)v^2+O(v^3),
\]

and

\[
C(v)
=2abv-ab(a^2+b^2)v^2+O(v^3).
\]

Consequently

\[
\boxed{
F(v)
=2ab(a^4-b^4)v^2+O(v^3)>0
}
\]

for all sufficiently small \(v>0\).

On the other hand, as \(v\to\infty\),

\[
\Delta(v)
=e^{-2b^2v}(1+o(1)),
\]

and

\[
C(v)
=e^{-(a-b)^2v/2}(1+o(1)).
\]

Hence

\[
\frac{F(v)}{\Delta(v)C(v)}
=
\frac{C'(v)}{C(v)}-
\frac{\Delta'(v)}{\Delta(v)}
\longrightarrow
2b^2-\frac{(a-b)^2}{2}
=
\frac{(a+b)(3b-a)}{2}.
\]

If

\[
\boxed{a>3b,}
\]

this limit is negative. Since \(\Delta C>0\), one has \(F(v)<0\) for all sufficiently large \(v\).

By continuity, \(F\) has at least one zero on \((0,\infty)\). Therefore:

> **Proposition.** For the five-node set
> \[
> \{-a,-b,0,b,a\}
> \]
> with \(a>3b>0\), the chain exceptional set \(Z_5\) is nonempty. In fact, the odd chain coefficient \(g_1\) vanishes at at least one finite width.

This disproves the conjecture that \(Z_N\) is empty for every symmetric set of distinct nodes.

## 4. Explicit example

For

\[
a=3,\qquad b=0.7,
\]

the equation \(F(v)=0\) has a root

\[
v_*=0.2871948612121286360981934411\ldots,
\]

corresponding to

\[
\boxed{
\tau_*=\frac1{2v_*}
=1.7409782260368811523899241099\ldots.
}
\]

For example,

\[
F(0.28)>0,
\qquad
F(0.30)<0.
\]

A direct raw-matrix computation gives

\[
g_1(\tau_*)=0
\]

up to numerical precision, while all eigenvalue gaps remain far from zero.

## 5. What this changes

The generic-width theorem remains correct and is now seen to be sharp as a theorem based on the second derivative \(M=T_0''\): one cannot remove \(Z_N\) for arbitrary symmetric nodes by proving every \(g_r\) is nonzero.

However, \(Z_N\) is not yet proved to be the true obstruction set for local two-shift generation. At the explicit width above, the fourth derivative coupling is numerically nonzero:

\[
\langle u_1,T_0^{(4)}u_3\rangle
\approx -0.2680772904462992.
\]

Thus the missing odd edge appears to return at order \(t^4\):

\[
\langle u_1,T_tu_3\rangle
=
\frac{t^4}{4!}
\langle u_1,T_0^{(4)}u_3\rangle
+O(t^6).
\]

The next problem is therefore not whether \(Z_N\) is empty. It is to determine whether every zero of a second-order chain coefficient is repaired by a higher even derivative, or whether a genuine width exists at which the full translated family leaves a chain edge identically zero.

## 6. Next targets

1. Prove analytically, in the \(2\times2\) odd block above, that \(F(v)=0\) implies the fourth-order coefficient is nonzero, except possibly on an explicitly classifiable algebraic-transcendental locus in \(a/b\).
2. Study uniqueness and location of the root when \(a>3b\).
3. Determine whether \(a\le3b\) implies \(F(v)>0\) for all \(v>0\).
4. Replace the second-order exceptional set by the true family-level obstruction set
   \[
   \widetilde Z_N
   :=
   \left\{\tau:
   \langle u_r,T_tu_{r+2}\rangle
   \equiv0\text{ as a function of }t
   \text{ for some }r
   \right\}.
   \]
5. Test whether \(\widetilde Z_N\) is empty for every symmetric set of distinct nodes.
