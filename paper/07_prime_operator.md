# The truncated prime-power operator

## 1. Status of this chapter

This chapter records the prime-term convention currently implemented by the
library. It is a precise finite definition, not yet a theorem giving a certified
error bound for the omitted tail. Statements about convergence as the cutoff
tends to infinity therefore remain research targets.

## 2. Arithmetic coefficient

Let \(\chi\) be a primitive quadratic Dirichlet character. For an integer
\(n\ge 2\), define

\[
\beta_\chi(n)=\frac{\Lambda(n)\chi(n)}{\sqrt n},
\]

where \(\Lambda\) is the von Mangoldt function. Only prime powers contribute.
The factor \(n^{-1/2}\) places the arithmetic term on the critical-line
normalization used throughout the current reconstruction.

The implementation is

```text
finite_weil.explicit_formula.quadratic_prime_power_coefficient
```

## 3. Universal translation matrix

For a Gaussian packet family \(\{g_j\}\), write

\[
C(a)_{ij}=\langle g_i,g_j(\cdot-a)\rangle.
\]

The library defines the symmetric two-sided translation contribution

\[
T_n=-\bigl(C(\log n)+C(-\log n)\bigr).
\]

Thus the sign of the classical two-sided prime term is contained in \(T_n\).
For translated equal-width Gaussian packets, the entries are available in
closed form through

\[
\langle g_i,g_j(\cdot-a)\rangle
=
\sqrt\pi\,\sigma
\exp\!\left(
-\frac{(c_i-c_j-a)^2}{4\sigma^2}
\right).
\]

The implementation is

```text
finite_weil.explicit_formula.universal_prime_operator
```

and ultimately uses

```text
finite_weil.packets.GaussianPacketFamily.translated_correlation
```

## 4. Finite cutoff

For cutoff \(N\ge 2\), define

\[
A_{\mathrm{prime}}(N)
=
\sum_{2\le n\le N}
\beta_\chi(n)T_n.
\]

Because \(\Lambda(n)=0\) away from prime powers, the implemented sum skips all
zero terms. Each \(T_n\) is real symmetric, and \(\beta_\chi(n)\) is real for a
quadratic character, so \(A_{\mathrm{prime}}(N)\) is real symmetric.

The implementation is

```text
finite_weil.explicit_formula.assemble_prime_operator
```

## 5. Complete finite matrix

With the conductor and gamma normalizations fixed elsewhere, the current finite
coordinate matrix is

\[
A_N
=
A_{\mathrm{cond}}
+
A_\Gamma
+
A_{\mathrm{prime}}(N).
\]

It is exposed by

```text
finite_weil.weil_operator.WeilOperator.matrix
```

The Gaussian packet basis is nonorthonormal. Consequently, intrinsic spectral
quantities are obtained from

\[
A_Nv=\lambda Bv,
\]

where \(B\) is the packet Gram matrix, rather than from the ordinary eigenvalues
of \(A_N\).

## 6. Open analytic obligations

The following points are deliberately not claimed as proved here:

1. a uniform bound for the cutoff tail;
2. convergence of \(A_{\mathrm{prime}}(N)\) in an operator or form topology;
3. interchange of the infinite prime-power sum with packet projection;
4. spectral convergence of the resulting generalized eigenproblems;
5. certified control of floating-point and quadrature errors.

These are requirements for turning finite experiments into rigorous statements.
Until they are supplied, the cutoff operator should be described as a
well-defined computational reconstruction of the chosen explicit-formula
convention, not as a certified approximation theorem.
