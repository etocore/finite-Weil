# Global collision filtration and descent to unordered clusters

## 1. Purpose

The local Smith spectrum in every regular affine collision gauge is

\[
0,0,1,3,4,\ldots,2m-1.
\]

A local Smith basis is not canonical and need not vary analytically. The correct
global object is instead the divisibility filtration defined directly by the
collision Jacobian. This note proves that the filtration is independent of the
regular affine gauge, is equivariant under permutation of node-weight pairs, and
descends to the regular unordered common-scale collision face.

## 2. Ordered regular collision face

Let \(\mathcal B_m^{\mathrm{ord}}\) denote the ordered common-scale boundary face
consisting of node-weight shapes

\[
(u_1,\ldots,u_m;\xi_1,\ldots,\xi_m)
\]

with pairwise distinct nodes, nonzero weights, and a regular affine gauge fixing
translation and dilation. Restrict further to the nonempty Zariski-open subset
\(\mathcal B_m^{\mathrm{gen}}\) on which the generic determinantal valuations are
attained.

Let \(R=\mathcal O_{\mathcal B_m^{\mathrm{gen}}}\{h\}\). The collision Jacobian is
an analytic bundle morphism

\[
J:E_R\longrightarrow Y_R,
\]

where \(E\) is the rank-\(2m\) source bundle and \(Y\) is the rank-\(2m\) moment
jet bundle.

## 3. Divisibility filtration

For every integer \(r\ge0\), define the source lattice

\[
\Lambda_r
=
\{v\in E_R:Jv\in h^rY_R\}.
\]

Its boundary fiber is

\[
F_r
=
\frac{\Lambda_r+hE_R}{hE_R}
\subset E_R/hE_R.
\]

Equivalently, \(F_r\) consists of boundary source directions whose image under
the collision map vanishes to order at least \(r\).

If the local Smith exponents are \(e_1,\ldots,e_{2m}\), then

\[
\dim F_r
=
\#\{i:e_i\ge r\}.
\]

For the affine-gauge spectrum

\[
0,0,1,3,4,\ldots,2m-1,
\]

we obtain

\[
\dim F_0=2m,
\qquad
\dim F_1=2m-2,
\qquad
\dim F_2=2m-3,
\qquad
\dim F_3=2m-3,
\]

and for \(4\le r\le2m-1\),

\[
\dim F_r=2m-r.
\]

The equality

\[
F_2=F_3
\]

is the coordinate-free expression of the missing grade \(2\).

## 4. Local freeness on the generic stratum

The conditions defining \(\Lambda_r\) are finite systems of analytic linear
equations obtained by requiring the coefficients below order \(r\) in \(Jv\) to
vanish. On \(\mathcal B_m^{\mathrm{gen}}\), the ranks of these systems are
constant because the determinantal valuations are constant.

Therefore each \(F_r\) is an analytic vector subbundle of the boundary source
bundle. The inclusions

\[
E=F_0\supset F_1\supset F_2=F_3\supset F_4\supset\cdots\supset F_{2m}=0
\]

define a global filtered vector bundle on the ordered generic face.

The associated graded pieces are

\[
\operatorname{Gr}_rF=F_r/F_{r+1}.
\]

Their ranks are the multiplicities of the Smith exponents:

\[
\operatorname{rank}\operatorname{Gr}_0F=2,
\]

\[
\operatorname{rank}\operatorname{Gr}_1F=1,
\]

\[
\operatorname{rank}\operatorname{Gr}_2F=0,
\]

and

\[
\operatorname{rank}\operatorname{Gr}_rF=1
\quad(3\le r\le2m-1).
\]

This construction does not choose Smith generators and therefore avoids all
monodromy and basis-selection ambiguities.

## 5. Independence of affine gauge

Let \(J\) and \(J'\) be the Jacobians in two regular affine gauges. The gauge
invariance theorem gives

\[
J'=JU,
\]

where \(U\in\operatorname{GL}_{2m}(R)\) is analytic and unimodular.

Then

\[
v\in\Lambda_r(J')
\iff
JUv\in h^rY_R
\iff
Uv\in\Lambda_r(J).
\]

Hence

\[
\Lambda_r(J')=U^{-1}\Lambda_r(J).
\]

Reducing modulo \(h\), the unit \(U\) identifies the filtered boundary bundles.
Thus the filtration is intrinsic to the regular affine-gauge collision blowup,
not to a particular normalization.

## 6. Permutation equivariance

The symmetric group \(S_m\) acts on the ordered collision face by simultaneous
permutation of node-weight pairs:

\[
\sigma\cdot(u_j,\xi_j)
=
(u_{\sigma^{-1}(j)},\xi_{\sigma^{-1}(j)}).
\]

The moment map is invariant under this action. Its Jacobian therefore satisfies

\[
J(\sigma b)
=
J(b)P_\sigma^{-1},
\]

where \(P_\sigma\) is the source permutation matrix acting simultaneously on the
weight and node directions. Since \(P_\sigma\) is constant and unimodular,

\[
\Lambda_r(\sigma b)
=
P_\sigma\Lambda_r(b).
\]

Consequently every \(F_r\) and every associated graded bundle is naturally
\(S_m\)-equivariant.

Exact coefficient-matrix checks are implemented in

```text
experiments/collision_permutation_equivariance.py
```

and tested in

```text
tests/test_collision_permutation_equivariance.py
```

## 7. Descent to the unordered face

On the distinct-node stratum, the action of \(S_m\) on ordered node-weight pairs
is free. Let

\[
\mathcal B_m^{\mathrm{unord}}
=
\mathcal B_m^{\mathrm{gen}}/S_m.
\]

A finite free group action together with an equivariant vector bundle gives a
vector bundle on the quotient. Therefore the full filtration

\[
F_0\supset F_1\supset F_2=F_3\supset\cdots
\]

descends to \(\mathcal B_m^{\mathrm{unord}}\).

### Theorem 7.1

On the generic regular unordered common-scale collision face, the raw moment
Jacobian defines a canonical filtered source bundle whose graded ranks are

\[
2,1,0,1,1,\ldots,1
\]

in degrees

\[
0,1,2,3,4,\ldots,2m-1.
\]

In particular, the missing grade \(2\) is well defined after quotienting by node
permutations.

## 8. What does not yet follow

The descent theorem establishes the filtered bundle and graded multiplicities.
It does not prove that the one-dimensional graded pieces are globally trivial.
They may carry nontrivial permutation characters or braid-group monodromy on the
unordered configuration space.

It also does not yet address:

- extension across nested collisions where nodes cease to be distinct;
- compatibility between different collision-tree faces;
- transfer of the filtered bundle to Gaussian synthesis;
- the quadratic pairing induced by the finite Weil form.

## 9. Next theorem target

The next task is to determine the transition character of each rank-one graded
piece under permutations. Concretely, one should construct canonical local
witness generators and compute whether

\[
\operatorname{Gr}_rF
\]

descends as a trivial line, a sign-twisted line, or a more general local system.
That representation-theoretic information is required before a global graded
Weil quadratic form can be written without choosing an ordering.
