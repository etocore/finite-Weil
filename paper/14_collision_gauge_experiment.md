# Normalized collision gauge experiment

## 1. Status and claim boundary

This note records the next computational step after the corrected collision determinant theorem. It restricts the corrected higher-moment map to scale and normalized shape directions and computes the resulting one-dimensional relation among target moments.

The construction is exact finite-dimensional linear algebra once the collision chart is chosen. The observed coefficients are not yet promoted to a symbolic missing-grade theorem.

This note does **not** claim:

- the complete Smith spectrum;
- an intrinsic root filtration;
- a proof that the missing relation is independent of weights;
- extension to nested collisions;
- descent from ordered to unordered clusters.

## 2. Centered normalized coordinates

Let

\[
\xi=(\xi_1,\ldots,\xi_m)
\]

be an ordered node shape. Translate it to arithmetic mean zero:

\[
\sum_{j=1}^m\xi_j=0.
\]

The translation direction is

\[
\mathbf 1=(1,\ldots,1)^{\mathsf T}.
\]

The radial scale direction is

\[
\xi=(\xi_1,\ldots,\xi_m)^{\mathsf T}.
\]

For real nodes with Euclidean scale normalization, the normalized shape tangent space is

\[
T_\xi
=
\left\{
\delta\xi:\
\sum_j\delta\xi_j=0,
\quad
\sum_j\xi_j\delta\xi_j=0
\right\}.
\]

For complex nodes, the experiment uses the corresponding Hermitian orthogonality condition

\[
\sum_j\overline{\xi_j}\,\delta\xi_j=0.
\]

Thus

\[
\dim T_\xi=m-2,
\]

and the scale-plus-shape source space

\[
\operatorname{span}\{\xi\}\oplus T_\xi
\]

has dimension \(m-1\).

## 3. Restricted corrected map

Let

\[
C^{\mathrm{full}}_{sj}
=
 u_jq_\xi'(\xi_j)H_s(\xi_j),
\qquad
0\le s\le m-1,
\]

be the corrected collision matrix proved in `paper/13_collision_moment_determinant.md`.

Choose an orthonormal basis

\[
T=(t_1,\ldots,t_{m-2})
\]

of \(T_\xi\), and define the source frame

\[
F_\xi
=
\begin{bmatrix}
\xi/\|\xi\|&T
\end{bmatrix}.
\]

The restricted map is

\[
C^{\mathrm{red}}
=
C^{\mathrm{full}}F_\xi.
\]

It is an \(m\times(m-1)\) matrix. On the nondegenerate collision stratum, the expected rank is \(m-1\). Consequently its left kernel is one-dimensional.

## 4. The missing target relation

Let

\[
\lambda=(\lambda_0,\ldots,\lambda_{m-1})^{\mathsf T}
\]

span the left kernel:

\[
\lambda^*C^{\mathrm{red}}=0.
\]

Then every corrected scale-and-shape variation satisfies

\[
\boxed{
\lambda_0\delta U_m
+
\lambda_1\delta U_{m+1}
+
\cdots
+
\lambda_{m-1}\delta U_{2m-1}
=0.
}
\]

The experiment normalizes the phase of \(\lambda\) deterministically by making its largest-magnitude coordinate real and positive.

The first calculations show that the relation is generally not the coordinate statement

\[
\delta U_m=0.
\]

Instead, the missing target line appears as a nontrivial triangular combination of the rows \(m,\ldots,2m-1\). This supports the corrected formulation of the missing-grade problem: find an intrinsic target-coordinate change that identifies this relation with the absent grade-\(m\) coordinate.

## 5. Reproducible implementation

The experiment is implemented in

```text
experiments/collision_gauge.py
```

Run the default three-node example with

```bash
python -m experiments.collision_gauge
```

or specify data explicitly:

```bash
python -m experiments.collision_gauge \
  --nodes=-2,-0.25,0.75,1.5 \
  --weights=1,2,3,4
```

The program prints:

- centered nodes;
- the normalized left-kernel relation;
- the residual norm \(\|\lambda^*C^{\mathrm{red}}\|\).

## 6. Tests

The regression tests verify:

1. centering removes the arithmetic mean;
2. the computed shape basis satisfies the center and scale constraints;
3. the scale-shape frame spans the full centered node space;
4. the restricted corrected map has rank \(m-1\) in representative cases;
5. the computed relation has a small residual;
6. common rescaling of all weights leaves the projective relation unchanged.

These are structural tests. They do not identify the symbolic coefficients of the relation.

## 7. Next symbolic target

The next theorem-facing task is to derive \(\lambda\) without singular-value decomposition.

Candidate descriptions to test include:

- coefficients of the node polynomial \(q_\xi\);
- complete homogeneous symmetric polynomials;
- derivatives of \(q_\xi\);
- a residue functional at infinity;
- the dual polynomial to the removed translation direction under the corrected moment pairing.

A successful identity should explain why the relation is independent of the arbitrary basis chosen for \(T_\xi\), and how a triangular target transformation converts it into the literal missing grade

\[
\operatorname{gr}_m=0.
\]

## 8. Claim ledger

| Statement | Status |
|---|---|
| Scale plus normalized shape has dimension \(m-1\) | Proved from the constraints |
| Restricted corrected matrix has one more row than column | Proved |
| Representative nondegenerate examples have rank \(m-1\) | Numerical observation with tests |
| A one-dimensional target relation is recovered numerically | Numerical observation with residual check |
| The relation is generally not literal \(\delta U_m=0\) | Numerical observation |
| Closed symbolic formula for the relation | Open |
| Relation yields the missing Smith grade | Open |
