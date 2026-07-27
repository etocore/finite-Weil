# Physical nodes versus an anchored collision chart

## 1. Purpose

The raw moment Smith theorem was proved for physical source coordinates

\[
(u_1,\ldots,u_m,x_1,\ldots,x_m).
\]

The finite-collision geometry is more naturally described by center, scale, and
shape variables. This note compares those source lattices exactly before any
attempt is made to interpret a missing graded direction in the finite-Weil
pipeline.

## 2. Anchored affine chart

Fix the affine normalization

\[
\xi_1=0,
\qquad
\xi_2=1,
\]

and use

\[
\eta=(\xi_3,\ldots,\xi_m)
\]

as the remaining shape coordinates. Write

\[
x_j=c+h\xi_j.
\]

The node part of the source transformation is

\[
(c,h,\eta_3,\ldots,\eta_m)
\longmapsto
(x_1,\ldots,x_m).
\]

Its Jacobian columns are

\[
\mathbf 1,
\qquad
\xi,
\qquad
h e_3,\ldots,h e_m.
\]

After removing one factor of \(h\) from each shape column, the coefficient
matrix is

\[
T_0=
\begin{pmatrix}
1&0&0&\cdots&0\\
1&1&0&\cdots&0\\
1&\xi_3&1&&0\\
\vdots&\vdots&&\ddots&\\
1&\xi_m&0&&1
\end{pmatrix}.
\]

Subtracting the first row from the others and then eliminating the second
column gives

\[
\det T_0=1.
\]

Therefore the exact source-change determinant is

\[
\boxed{\det T(h)=h^{m-2}.}
\]

The source transformation is invertible for every fixed \(h\ne0\), but it is
not unimodular over \(\mathbb C\{h\}\) when \(m>2\).

## 3. Immediate consequence

The physical and collision-chart Jacobians satisfy

\[
J_{\mathrm{chart}}(h)=J_{\mathrm{physical}}(h)T(h).
\]

Because \(T(h)\) has determinant \(h^{m-2}\), its inverse contains negative
powers of \(h\). Thus the two matrices are not Smith-equivalent over the local
analytic ring.

This confirms the main concern from the audit: the phrase "intrinsic missing
grade" is meaningful only after a source lattice has been specified.

## 4. Exact chart columns at a centered collision

Set \(c=0\), so \(x_j=h\xi_j\). For

\[
M_r=\sum_j u_jx_j^r,
\]

the chart derivatives are

\[
\frac{\partial M_r}{\partial u_j}=h^r\xi_j^r,
\]

\[
\frac{\partial M_r}{\partial c}
=r h^{r-1}\sum_j u_j\xi_j^{r-1},
\]

\[
\frac{\partial M_r}{\partial h}
=r h^{r-1}\sum_j u_j\xi_j^r,
\]

and, for \(j\ge3\),

\[
\frac{\partial M_r}{\partial \eta_j}
=r u_j h^r\xi_j^{r-1}.
\]

Thus:

- weight columns have row grade \(r\);
- center and scale columns have row grade \(r-1\);
- normalized-shape columns have row grade \(r\).

The normalized-shape columns are exactly one order higher than the
corresponding physical position columns.

## 5. Exact small-dimensional data

Exhaustive rational minor calculations give the following chart valuations.

For \(m=2\):

\[
\nu=(0,0,1,4),
\qquad
E=(0,0,1,3).
\]

For \(m=3\):

\[
\nu=(0,0,1,4,8,13),
\qquad
E=(0,0,1,3,4,5).
\]

For \(m=4\):

\[
\nu=(0,0,1,4,8,13,19,26),
\qquad
E=(0,0,1,3,4,5,6,7).
\]

For \(m\ge3\), these computations suggest

\[
\boxed{
E_m^{\mathrm{chart}}
=
\{0,0,1,3,4,\ldots,2m-1\}.
}
\]

The missing grade is therefore \(2\), not \(m\), in this anchored collision
chart.

This pattern has been checked exactly for multiple generic rational
specializations through \(m=4\). It is not yet proved for arbitrary \(m\).

## 6. Determinant consistency

The total physical valuation is

\[
\nu_{2m}^{\mathrm{physical}}=2m(m-1).
\]

Multiplication by the source-change matrix contributes

\[
\operatorname{ord}_h\det T=m-2.
\]

Hence

\[
\nu_{2m}^{\mathrm{chart}}
=
2m(m-1)+(m-2)
=
2m^2-m-2.
\]

The proposed chart exponents sum to exactly this value:

\[
0+0+1+\sum_{r=3}^{2m-1}r
=2m^2-m-2.
\]

For \(m=3\) and \(m=4\), this gives \(13\) and \(26\), matching the exact
minor calculations.

## 7. What this resolves

The lattice comparison confirms:

1. physical node and normalized collision coordinates are not related by a
   Smith-preserving source transformation;
2. the non-unimodularity has exact determinant order \(m-2\);
3. source normalization can relocate the missing grade rather than merely add
   a uniform shift;
4. a degree-\(m\) defect in physical coordinates cannot be imported directly
   into the collision chart;
5. the exact chart must be fixed before the finite-Weil associated graded is
   interpreted.

## 8. What remains open

The current anchored chart is mathematically clean but may not be the chart
used by the finite-Weil construction. Other normalizations may impose:

- weighted center zero rather than \(\xi_1=0\);
- unit variance or another scale condition rather than \(\xi_2=1\);
- quotient coordinates rather than anchored coordinates;
- amplitude normalization such as fixed total mass;
- unordered-cluster descent.

Each choice produces a different source transformation that must be analyzed
explicitly.

The chart-spectrum formula

\[
\{0,0,1,3,4,\ldots,2m-1\}
\]

is currently an exact small-case conjecture, not a theorem.

## 9. Next target

The next task is to recover the exact collision chart used in the finite-Weil
model and factor its source Jacobian into:

\[
T(h)=U(h)D(h)V(h),
\]

where \(U\) and \(V\) are analytic unimodular and \(D\) records all
non-unimodular powers of \(h\).

Only then should the chart Jacobian be compared with Gaussian synthesis, the
Gram matrix, or the Weil form.
