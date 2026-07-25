# Ordered cluster-chart transitions

## Status

This note constructs the overlap maps between ordered common-scale cluster charts for the finite exponential packet realization

\[
\mathcal R_N(X,u)
=
\left(\sum_{j=1}^N u_jx_j^k\right)_{k=0}^{2N-1}.
\]

Fix an ordered cluster of size \(m\). For an ordered reference pair \((a,b)\), define the normalized chart by

\[
x_a=x,
\qquad
x_b=x+h,
\qquad
x_j=x+h\xi_j
\quad(j\ne a,b),
\]

with the conventions

\[
\xi_a=0,
\qquad
\xi_b=1.
\]

The main result is that the transition between any two such charts is rational and extends holomorphically to the collision face \(h=0\) on the overlap where the new reference pair remains distinct.

---

## 1. General transition formula

Let \((a,b)\) and \((c,d)\) be two ordered reference pairs. In the \((a,b)\)-chart, every cluster node has the form

\[
x_j=x+h\xi_j,
\]

with \(\xi_a=0\) and \(\xi_b=1\).

The \((c,d)\)-chart is defined by

\[
\widetilde x=x_c,
\qquad
\widetilde h=x_d-x_c,
\qquad
x_j=\widetilde x+\widetilde h\,\widetilde\xi_j,
\]

with \(\widetilde\xi_c=0\) and \(\widetilde\xi_d=1\).

Substitution gives

\[
\boxed{
\widetilde x=x+h\xi_c,
}
\]

\[
\boxed{
\widetilde h=h(\xi_d-\xi_c),
}
\]

and

\[
\boxed{
\widetilde\xi_j
=
\frac{\xi_j-\xi_c}{\xi_d-\xi_c}.
}
\]

The transition is defined precisely on the overlap

\[
\xi_d-\xi_c\ne0,
\]

which is equivalent to the physical nodes \(x_c\) and \(x_d\) being distinct for \(h\ne0\).

Cluster coefficients are attached to labeled physical nodes and therefore transform only by the permutation used to order the new chart. Exterior nodes and coefficients are unchanged unless the chart convention also reorders them.

---

## 2. Inverse transition

The inverse map is obtained by exchanging the two reference pairs. Explicitly,

\[
x=\widetilde x+\widetilde h\,\widetilde\xi_a,
\]

\[
h=\widetilde h(\widetilde\xi_b-\widetilde\xi_a),
\]

and

\[
\xi_j
=
\frac{\widetilde\xi_j-\widetilde\xi_a}
{\widetilde\xi_b-\widetilde\xi_a}.
\]

Since the new chart satisfies

\[
\widetilde\xi_c=0,
\qquad
\widetilde\xi_d=1,
\]

these formulas are rational on the same overlap domain.

Thus the overlap map is a biholomorphism between nondegenerate ordered shape charts.

---

## 3. Extension to the collision face

The formulas

\[
\widetilde x=x+h\xi_c,
\qquad
\widetilde h=h(\xi_d-\xi_c),
\qquad
\widetilde\xi_j
=
\frac{\xi_j-\xi_c}{\xi_d-\xi_c}
\]

remain meaningful at \(h=0\).

At the boundary,

\[
\widetilde x=x,
\qquad
\widetilde h=0,
\]

while the normalized shape transforms by the affine-projective action

\[
\boxed{
\xi_j\longmapsto
\frac{\xi_j-\xi_c}{\xi_d-\xi_c}.
}
\]

Therefore the collision face carries a natural atlas modeled on configurations of ordered distinct points modulo affine transformations.

On compact overlap subcharts satisfying

\[
|\xi_d-\xi_c|\ge\delta>0,
\]

all derivatives of the transition and its inverse are uniformly bounded.

---

## 4. Cocycle property

Let \((a,b)\), \((c,d)\), and \((e,f)\) be three ordered reference pairs. Denote the corresponding shape-normalization maps by

\[
\phi_{cd}(z)
=
\frac{z-\xi_c}{\xi_d-\xi_c}.
\]

Then the transition from \((a,b)\) to \((e,f)\) is the composition of the transitions through \((c,d)\):

\[
\Phi_{ab}^{ef}
=
\Phi_{cd}^{ef}\circ\Phi_{ab}^{cd}.
\]

This follows because both sides send every physical node coordinate \(x_j\) to the uniquely normalized coordinate in which the \(e\)-node is \(0\) and the \(f\)-node is \(1\).

Equivalently, the affine normalizations satisfy the exact cocycle identity

\[
\phi_{ef}^{(cd)}\circ\phi_{cd}^{(ab)}
=
\phi_{ef}^{(ab)}.
\]

Hence the ordered charts form a genuine analytic atlas on the common-scale blow-up region.

---

## 5. Boundary aggregate packet

At \(h=0\), the realization restricts to

\[
\mathcal R_N
=
UM(x)
+
\sum_{\ell>m}u_\ell M(y_\ell),
\qquad
U=\sum_{j=1}^m u_j.
\]

Under a chart transition,

\[
\widetilde x=x,
\qquad
\widetilde U=U.
\]

Thus the boundary aggregate packet is chart-independent.

The normalized shape variables transform nontrivially, but they remain invisible to the ordinary boundary realization map.

---

## 6. Scale transformation and exponent filtration

The two scales are related by

\[
\widetilde h=\lambda(\xi)h,
\qquad
\lambda(\xi)=\xi_d-\xi_c.
\]

For a diagonal cluster scale matrix

\[
D_m(h)=\operatorname{diag}(h^{e_1},\ldots,h^{e_{2N}}),
\]

we have

\[
D_m(\widetilde h)
=
D_m(h)\Lambda_{cd}(\xi),
\]

where

\[
\boxed{
\Lambda_{cd}(\xi)
=
\operatorname{diag}
\bigl(
\lambda(\xi)^{e_1},\ldots,
\lambda(\xi)^{e_{2N}}
\bigr).
}
\]

On a nondegenerate overlap, \(\Lambda_{cd}\) and its inverse are holomorphic and bounded on compact subcharts.

Therefore the exponent filtration is independent of the chosen ordered reference pair. A chart change only multiplies each graded component by a nowhere-vanishing shape factor.

---

## 7. Transformation of the regular factors

Suppose in two overlapping charts we have analytic normal forms

\[
J_{ab}=A_{ab}D_m(h)B_{ab},
\]

and

\[
J_{cd}=A_{cd}D_m(\widetilde h)B_{cd}.
\]

Let

\[
Q_{ab}^{cd}=D\Phi_{ab}^{cd}
\]

be the ordinary coordinate-transition Jacobian. Since

\[
J_{ab}=J_{cd}Q_{ab}^{cd},
\]

we obtain

\[
A_{ab}D_m(h)B_{ab}
=
A_{cd}D_m(h)\Lambda_{cd}B_{cd}Q_{ab}^{cd}.
\]

Thus the two factorizations differ by bounded analytic gauges after the common diagonal powers are extracted.

In particular, the associated filtration by vanishing order is intrinsic, even though the matrices \(A\) and \(B\) are chart-dependent.

---

## 8. Rescaled tangent-frame transition

Define in each chart

\[
T_{ab}=B_{ab}^{-1}D_m(h)^{-1},
\]

\[
T_{cd}=B_{cd}^{-1}D_m(\widetilde h)^{-1}.
\]

The corresponding rescaled frames are related by a bounded analytic matrix on every compact overlap. Indeed, since

\[
J_{ab}T_{ab}=A_{ab},
\qquad
J_{cd}T_{cd}=A_{cd},
\]

and \(J_{ab}=J_{cd}Q_{ab}^{cd}\), one has

\[
Q_{ab}^{cd}T_{ab}
=
T_{cd}G_{ab}^{cd},
\]

where

\[
\boxed{
G_{ab}^{cd}
=
A_{cd}^{-1}A_{ab}.
}
\]

The matrix \(G_{ab}^{cd}\) is holomorphic and uniformly invertible on compact overlaps.

Therefore the local rescaled tangent frames glue to an analytic vector bundle over the ordered common-scale blow-up atlas.

This establishes bundle-level compatibility. Whether the resulting bundle has a canonical Lie-algebroid bracket remains open.

---

## 9. Renormalized metric compatibility

In the \((a,b)\)-chart, the renormalized metric is

\[
\widetilde G_{ab}=A_{ab}^*A_{ab}.
\]

On an overlap,

\[
A_{ab}=A_{cd}G_{ab}^{cd},
\]

so

\[
\boxed{
\widetilde G_{ab}
=
(G_{ab}^{cd})^*
\widetilde G_{cd}
G_{ab}^{cd}.
}
\]

Hence the extended positive-definite metric is globally compatible with the rescaled tangent-bundle transition functions.

---

## 10. Main theorem

### Theorem - ordered common-scale cluster atlas

For every ordered reference pair \((a,b)\), the normalized cluster variables

\[
(x,h,\xi,u,\text{exterior data})
\]

define a local chart on the common-scale cluster blow-up. On overlaps between the \((a,b)\)- and \((c,d)\)-charts, the transition is

\[
\widetilde x=x+h\xi_c,
\]

\[
\widetilde h=h(\xi_d-\xi_c),
\]

\[
\widetilde\xi_j
=
\frac{\xi_j-\xi_c}{\xi_d-\xi_c},
\]

with coefficient variables transformed by the induced label permutation.

These overlap maps:

1. are rational and biholomorphic on the nondegenerate overlap;
2. extend holomorphically to \(h=0\);
3. satisfy the cocycle condition;
4. preserve the boundary aggregate packet;
5. preserve the singular exponent filtration up to nowhere-vanishing graded factors;
6. glue the local cluster-rescaled tangent frames into an analytic vector bundle;
7. glue the renormalized metrics into a global positive-definite metric on that bundle.

---

## 11. What remains open

- Passing from ordered to unordered clusters by a precise symmetric-group quotient.
- Describing isotropy near partially symmetric configurations.
- Extending the atlas to simultaneous disjoint clusters.
- Extending it to nested and nonuniform collision trees.
- Globalizing the metric-completion quotient beyond one common-scale stratum.
- Determining whether the rescaled tangent bundle carries a canonical Lie-algebroid structure.

The immediate next step is the symmetric-group action and the quotient from labeled ordered charts to unordered packet configurations.
