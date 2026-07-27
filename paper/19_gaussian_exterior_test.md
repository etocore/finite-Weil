# Exterior packets in the concrete Gaussian feature map

## 1. Question

The relative-spectrum hypothesis proposes that an isolated cluster has consecutive collision exponents, while embedding the cluster beside one or more separated packets removes the grade equal to the cluster size.

The first concrete test should use the actual translated Gaussian feature map rather than an abstract target space.

Let

\[
g_c(x)=\exp\left(-\frac{(x-c)^2}{2\sigma^2}\right)
\]

and consider

\[
\Phi(u,x)=\sum_{j=1}^m u_jg_{x_j}.
\]

For a collision

\[
x_j=h\xi_j,
\]

the cluster Jacobian contains:

- weight columns \(g_{h\xi_j}\);
- centered position columns obtained from \(hu_j\partial_cg_{h\xi_j}\) after removing common translation.

Each separated exterior packet at center \(a_k\) contributes the two columns

\[
g_{a_k},\qquad \partial_cg_{a_k}.
\]

The relative cluster matrix is obtained by projecting the cluster columns to the quotient by the exterior column span.

## 2. Numerical experiment

The implementation

```text
experiments.gaussian_relative_collision
```

samples the Gaussian functions on a dense real grid, computes singular values for a sequence of collision scales, and fits their logarithmic slopes.

The experiment varies:

- cluster sizes \(m=2,3,4\);
- exterior counts \(n=0,1,2,3\);
- exterior distances from the cluster;
- collision scales in a range where the sampled matrices remain numerically resolved.

## 3. Observation

For every tested configuration, both the isolated and exterior-relative slopes are approximately

\[
\boxed{0,1,\ldots,2m-2}.
\]

In particular:

\[
m=2:\quad 0,1,2,
\]

\[
m=3:\quad 0,1,2,3,4,
\]

\[
m=4:\quad 0,1,2,3,4,5,6.
\]

Adding one, two, or three exterior packets does not shift the exponent \(m\), and moving the exterior packets farther away does not change the fitted list.

## 4. Interpretation

This falsifies the strongest form of the exterior-absorption hypothesis for the underlying Gaussian function map.

Separated translated Gaussians and their center derivatives do not generically absorb the cluster derivative jet of order \(m\). The relative quotient preserves the consecutive collision slopes.

Therefore, if the previously observed finite-Weil Jacobian has a gap at grade \(m\), that gap must come from additional structure beyond the packet synthesis map itself. Candidate mechanisms now include:

1. the nonlinear map from packet parameters to Gram or Weil matrix entries;
2. Gram whitening or quotienting by a nearly singular metric;
3. a generalized-eigenvalue or matrix-pencil normalization;
4. symmetry reduction in the matrix target;
5. a Schur complement involving operator and Gram blocks together, rather than packet columns alone;
6. numerical rank truncation in the original singular-value experiment.

## 5. Claim boundary

The sampled Gaussian computation is a numerical diagnostic, not an exact Smith theorem. It does, however, provide a direct countercheck against the claim that exterior Gaussian packets alone force the missing grade.

The next experiment should differentiate the actual pair

\[
(A(c),B(c))
\]

with respect to colliding packet centers and weights, then perform the same quotient or whitening used in the original numerical run. Testing only the synthesis map \(\Phi\) is no longer sufficient.

## 6. Current conclusion

The evidence now supports the following separation:

- the isolated corrected-moment model has consecutive exponents;
- the concrete Gaussian synthesis map, even relative to separated packets, also has consecutive exponents;
- the reported gap must arise later in the pipeline, after packet synthesis.

The exact original generalized-matrix Jacobian is therefore the critical missing object.
