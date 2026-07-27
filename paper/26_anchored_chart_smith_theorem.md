# Generic Smith spectrum in the anchored collision chart

## 1. Statement

Fix an ordered cluster with affine anchors

\[
\xi_0=0,
\qquad
\xi_1=1,
\]

and write

\[
x_j=c+h\xi_j.
\]

Use source coordinates

\[
(u_0,\ldots,u_{m-1},c,h,\xi_2,\ldots,\xi_{m-1}).
\]

Let

\[
M_r=\sum_{j=0}^{m-1}u_jx_j^r,
\qquad
0\le r<2m,
\]

and evaluate the Jacobian along the collision curve \(c=0\), with the anchored
shape fixed and pairwise distinct.

For \(m\ge2\), on a nonempty Zariski-open set of anchored nodes and weights, the
determinantal valuations are

\[
\boxed{
\nu_1=\nu_2=0,
\qquad
\nu_k=\frac{k(k-1)}2-2
\quad(3\le k\le2m).
}
\]

Consequently the generic Smith exponents are

\[
\boxed{
0,0,1,3,4,\ldots,2m-1.
}
\]

For \(m\ge3\), grade \(2\) is absent.

## 2. Column grades

At \(c=0\), the weight columns are

\[
W_j(r)=h^r\xi_j^r.
\]

The center and scale columns are

\[
C(r)=r h^{r-1}\sum_j u_j\xi_j^{r-1},
\]

and

\[
S(r)=r h^{r-1}\sum_j u_j\xi_j^r.
\]

For \(j\ge2\), the shape columns are

\[
X_j(r)=r u_jh^r\xi_j^{r-1}.
\]

Thus the center and scale columns have grade offset one, while every weight and
shape column has grade offset zero.

For a minor with row set \(R\) and with \(a\in\{0,1,2\}\) selected columns among
\(C,S\), every determinant term has order

\[
\operatorname{ord}_h=\sum_{r\in R}r-a,
\]

provided the coefficient determinant is nonzero.

## 3. Universal lower bound

For \(k\ge3\), the smallest sum of \(k\) distinct nonnegative row indices is

\[
0+1+\cdots+(k-1)=\frac{k(k-1)}2.
\]

At most two selected columns have offset one. Therefore every nonzero \(k\)-minor
satisfies

\[
\nu_k\ge\frac{k(k-1)}2-2.
\]

For \(k=1\), a weight entry in row zero gives valuation zero.

For \(k=2\), the formal grade estimate would be negative if both offset-one
columns were selected, but both center and scale entries vanish in row zero. A
nonzero two-minor therefore has valuation at least zero. Two distinct weight
columns in rows zero and one attain zero.

Hence

\[
\nu_1,\nu_2\ge0,
\qquad
\nu_k\ge\frac{k(k-1)}2-2
\quad(k\ge3).
\]

## 4. Derivative-evaluation interpretation

Remove the explicit powers of \(h\). Let

\[
D_j(p)=u_jp'(\xi_j).
\]

The coefficient functionals represented by the non-weight columns are

\[
C=\sum_{j=0}^{m-1}D_j,
\qquad
S=\sum_{j=0}^{m-1}\xi_jD_j,
\qquad
X_j=D_j\quad(j\ge2).
\]

Because \(\xi_0=0\) and \(\xi_1=1\), after subtracting the selected shape
functionals from \(C\) and \(S\), the remaining pair is

\[
D_0+D_1,
\qquad
D_1.
\]

For nonzero \(u_0,u_1\), this pair is constant-column equivalent to

\[
D_0,D_1.
\]

Thus the center, scale, and selected shape columns can be analyzed as ordinary
first-derivative evaluation conditions at the corresponding anchored nodes.

## 5. Witnesses for \(3\le k\le m+1\)

Use rows

\[
0,1,\ldots,k-1.
\]

Select the columns

\[
W_0,
\quad C,
\quad S,
\quad X_2,\ldots,X_{k-2}.
\]

There are \(k\) columns. To prove that the coefficient determinant is not
identically zero, specialize the unused weights to zero. The selected functionals
then become constant-column equivalent to

\[
p\longmapsto p(\xi_0),
\qquad
p\longmapsto p'(\xi_j)
\quad(0\le j\le k-2).
\]

Suppose \(p\) has degree less than \(k\) and lies in their common kernel. Then
\(p'\) has \(k-1\) distinct roots but degree at most \(k-2\). Hence \(p'=0\).
The condition \(p(\xi_0)=0\) then gives \(p=0\).

The interpolation functionals are independent at this specialization, so the
minor determinant polynomial is not identically zero. Its valuation is

\[
0+1+\cdots+(k-1)-2
=
\frac{k(k-1)}2-2.
\]

## 6. Witnesses for \(m+2\le k\le2m\)

Write

\[
q=k-m,
\qquad
2\le q\le m.
\]

Use rows \(0,1,\ldots,k-1\), select all of

\[
C,S,X_2,\ldots,X_{m-1},
\]

and select the first \(q\) weight columns.

The non-weight columns are constant-column equivalent to derivative evaluations
at all \(m\) nodes. Therefore the selected coefficient functionals are equivalent
to

\[
p(\xi_i)=0
\quad(0\le i<q),
\]

and

\[
p'(\xi_j)=0
\quad(0\le j<m).
\]

Choose a real ordered specialization

\[
\xi_0<\xi_1<\cdots<\xi_{m-1}.
\]

Let

\[
Q(x)=\prod_{j=0}^{m-1}(x-\xi_j).
\]

If a polynomial \(p\) of degree less than \(m+q\) lies in the kernel, then

\[
p'(x)=Q(x)s(x),
\qquad
\deg s\le q-2.
\]

For \(0\le i<q-1\),

\[
0=p(\xi_{i+1})-p(\xi_i)
 =\int_{\xi_i}^{\xi_{i+1}}Q(t)s(t)\,dt.
\]

The polynomial \(Q\) has a fixed nonzero sign on each open interval. Hence each
vanishing integral forces a root of \(s\) in that interval. This gives \(q-1\)
distinct roots, impossible for \(\deg s\le q-2\) unless \(s=0\). Thus \(p'=0\),
and the value conditions give \(p=0\).

The witness is therefore nonzero for one real specialization and hence generically
nonzero algebraically. Its valuation again equals

\[
\frac{k(k-1)}2-2.
\]

## 7. The boundary size \(k=m+1\)

The small-witness construction already covers \(k=m+1\). It uses one value
condition and derivative conditions at all \(m\) nodes. A polynomial of degree
less than \(m+1\) has derivative degree at most \(m-1\); vanishing at all \(m\)
distinct nodes forces the derivative to vanish identically.

This is why the large-witness interval argument only begins at \(q=2\).

## 8. Smith exponents

The witnesses attain the lower bound for every size. Therefore

\[
\nu_1=\nu_2=0,
\qquad
\nu_k=\frac{k(k-1)}2-2
\quad(k\ge3).
\]

Taking successive differences gives

\[
e_1=0,
\quad e_2=0,
\quad e_3=1,
\quad e_k=k-1\quad(k\ge4).
\]

Thus

\[
\boxed{
E_m^{\mathrm{anch}}
=
\{0,0,1,3,4,\ldots,2m-1\}.
}
\]

The full determinant valuation is

\[
\nu_{2m}=m(2m-1)-2=2m^2-m-2.
\]

This agrees with the physical determinant valuation

\[
2m(m-1)
\]

plus the source-change valuation

\[
m-2.
\]

## 9. Interpretation

The physical source lattice has generic missing grade \(m\), while this anchored
collision lattice has generic missing grade \(2\). The two spectra differ because
the source change has determinant

\[
h^{m-2},
\]

which is not a unit for \(m>2\).

Therefore the location of a missing Smith grade is not invariant under singular
collision normalization. It becomes meaningful for finite-Weil analysis only
after the exact source lattice used by that construction is fixed.

## 10. Scope

The theorem is generic. The witness arguments establish nonvanishing on a
nonempty Zariski-open set. They do not classify exceptional anchored complex
configurations where the determinantal valuations may jump.
