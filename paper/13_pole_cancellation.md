# Pole cancellation and independent zero-side validation

## 1. Scope and claim status

This chapter reports the implementation of the finite pole matrix derived in
`paper/12_pole_term.md`, and two computational results obtained with it:

1. adding the pole matrix cancels the large negative deep-cutoff eigenvalues
   previously observed for the principal character;
2. the fully assembled finite matrices agree with independently computed
   zero-side matrices to machine precision, for the principal character and
   for every tested primitive quadratic character.

Both results are floating-point observations reproducible from this
repository. They validate the project's normalization chain end to end. They
do not prove convergence of any infinite-dimensional limit, and they carry no
implication for RH or GRH beyond consistency.

## 2. The zero-side prediction

Fix the packet family \(g_j(x)=\exp(-(x-c_j)^2/2\sigma^2)\). Under the
project's Fourier convention,

\[
\widehat g_i(t)\overline{\widehat g_j(t)}
=
2\pi\sigma^2 e^{-\sigma^2t^2}e^{it(c_j-c_i)}.
\]

The Weil explicit formula, in exactly the convention fixed by
`docs/FOURIER_CONVENTION.md` and `paper/06_gamma_term.md`, states that for
each primitive quadratic character the zero side equals the assembled
arithmetic side. Writing \(\gamma\) for the imaginary parts of the
nontrivial zeros of \(L(s,\chi)\) and using the symmetry \(\gamma\mapsto-\gamma\),

\[
Z_{ij}
=
\sum_{\gamma>0}
4\pi\sigma^2
e^{-\sigma^2\gamma^2}
\cos\bigl(\gamma(c_i-c_j)\bigr),
\]

and the prediction is

\[
A_{\mathrm{cond}}
+
A_\Gamma
+
A_{\mathrm{prime}}(\infty)
+
[\,P\ \text{if}\ q=1\,]
=
Z .
\]

Two structural consequences follow immediately.

**Gaussian zero-side envelope.** Every entry of \(Z\) is bounded by
\(4\pi\sigma^2\sum_{\gamma>0}e^{-\sigma^2\gamma^2}\). For \(\sigma=0.5\) and
\(q=1\), the lowest zero \(\gamma_1\approx14.13\) gives
\(e^{-\sigma^2\gamma_1^2}\approx2\times10^{-22}\): the exact assembled matrix
is numerically **zero**. The finite model at these widths is a statement
about near-perfect cancellation among terms of order \(10^2\)–\(10^3\).

**The deep-cutoff mystery.** The deep-cutoff experiments of
`paper/09_prime_cutoff_geometry.md` omitted the pole matrix. Their limiting
smallest eigenvalues (about \(-903.8\), \(-911.6\), \(-1205.3\) for dimensions
8, 16, 32) are therefore not evidence of a negative Weil direction; they are
the spectrum of \(Z - P\approx -P\), i.e. of minus the rank-two pole matrix in
the Gram metric. The dimension dependence that chapter listed as unresolved
is the dependence of the pole vectors' Gram geometry on the packet family.

## 3. Deep-cutoff cancellation experiment

`experiments/pole_cancellation.py` recomputes the Gram-whitened extreme
eigenvalues for \(D=1\), \(\sigma=0.5\), centers on \([-6,6]\), with and
without the pole matrix. Representative values:

| Dimension | Cutoff | \(\lambda_{\min}\) without pole | \(\lambda_{\min}\) with pole | \(\lambda_{\max}\) with pole |
|---:|---:|---:|---:|---:|
| 8 | \(10^5\) | -460.784957 | -648.004694 | 648.004694 |
| 8 | \(10^6\) | -895.488179 | -10.254007 | 10.254007 |
| 8 | \(10^7\) | -903.790915 | -0.000017 | 0.000017 |
| 16 | \(10^5\) | -490.688205 | -678.616485 | 678.604623 |
| 16 | \(10^6\) | -903.030325 | -15.353470 | 15.351551 |
| 16 | \(10^7\) | -911.553565 | -0.000026 | 0.000026 |

At cutoff \(10^7\) the **entire** whitened spectrum of the assembled operator
collapses to \(\pm3\times10^{-5}\), as the zero-side envelope predicts. At
under-resolved cutoffs the with-pole spectrum is dominated by the unbalanced
pole block, which explains why adding the pole helps only once the prime sum
covers the packet-translation range \(\log n\lesssim 2E\).

The same collapse occurs for non-principal characters without any pole term:
for \(D=5,-3,8,13\) at dimension 8 and cutoff \(10^7\), the smallest
eigenvalue is \(0\) to seven digits and the largest is the small positive
zero-side mass of the low-lying zeros (for example \(1.3555\) for \(D=13\),
whose lowest zero \(\gamma_1\approx3.119\) is well inside the packet
bandwidth).

## 4. Machine-precision zero-side agreement

For packets with \(\sigma=0.15\) on \([-1.5,1.5]\) (dimension 7), the
envelope keeps roughly the first seven to twenty-three zeros visible above
\(10^{-18}\), and the prime sum resolves at cutoff \(2000\).

For \(D=1\), building \(Z\) from the first seven zeta zeros gives

\[
\max_{ij}\bigl|A^{\mathrm{full}}_{ij}-Z_{ij}\bigr|
=4.3\times10^{-16},
\]

with generalized spectra agreeing to eight digits and every generalized
eigenvalue strictly positive. This comparison is enshrined as the regression
test `tests/test_poles.py::test_zeta_operator_with_pole_matches_zero_side_matrix`.

For \(D=5,-3,8,13\), zeros of \(L(s,\chi_D)\) are computed independently via
the Hurwitz-zeta representation of \(L\) and sign changes of the real-valued
completed function \(\Lambda(\tfrac12+it,\chi)\). This comparison is
committed as `experiments/dirichlet_zero_side.py`, with the run recorded in
`paper/data/dirichlet-zero-side.csv` and an mpmath-gated regression test for
\(D=5\) in `tests/test_dirichlet_zero_side.py`. The entrywise agreement is
at the \(10^{-16}\)–\(10^{-15}\) level, and all generalized eigenvalues are
strictly positive:

| \(D\) | zeros used (\(\gamma\le42\)) | first zeros | \(\max|A-Z|\) | \(\lambda_{\min}\) |
|---:|---:|---|---:|---:|
| 5 | 17 | 6.6485, 9.8314, 11.9588 | \(3.5\times10^{-16}\) | \(7.6\times10^{-3}\) |
| -3 | 13 | 8.0397, 11.2492, 15.7046 | \(1.8\times10^{-16}\) | \(2.4\times10^{-3}\) |
| 8 | 20 | 4.9000, 7.6284, 10.8066 | \(2.5\times10^{-16}\) | \(8.3\times10^{-3}\) |
| 13 | 23 | 3.1193, 7.2316, 8.6254 | \(2.2\times10^{-16}\) | \(1.6\times10^{-1}\) |

This settles, numerically, the research-map row "Identification of
`A_prime` with the classical explicit-formula prime term": the implemented
conductor, gamma, prime, and pole matrices jointly reproduce the classical
symmetric explicit formula in the project's fixed convention, entry by entry,
at machine precision.

## 5. What the finite operator is

The validated identity gives the finite model a direct interpretation. The
translation-invariant kernel of the assembled operator,

\[
K(\delta)
=
\sum_{\gamma>0}4\pi\sigma^2e^{-\sigma^2\gamma^2}\cos(\gamma\delta),
\]

is the Gaussian-smoothed cosine transform of the zero-counting measure. The
finite Weil matrices are Gram compressions of the positive-semidefinite
(under GRH) kernel of the zero point process, and the generalized eigenvalues
measure the spectral mass of the low-lying zeros captured by the packet
bandwidth.

As a demonstration, a windowed cosine periodogram of the **prime-side**
kernel (conductor + gamma + pole + prime sum, no zero data used) over
\(\delta\in[0,10]\) with \(\sigma=0.07\) recovers the first seven zeta zeros:

| Recovered | 14.145 | 21.038 | 25.030 | 30.448 | 32.959 | 37.615 | 40.951 |
|---|---|---|---|---|---|---|---|
| True | 14.135 | 21.022 | 25.011 | 30.425 | 32.935 | 37.586 | 40.919 |

The uniform small upward shift is Hann-window leakage bias; the near-equal
peak heights after envelope flattening independently indicate that each
recovered zero is simple.

## 6. Claim boundary

- The pole matrix is implemented exactly as derived in
  `paper/12_pole_term.md` and gated to the principal character.
- `WeilOperator` resolves `include_pole=None` automatically: the pole block
  is included exactly for the principal character, so the default assembly
  is the mathematically correct completed function. The historical sweep
  scripts (`experiments/convergence.py`, `experiments/deep_cutoff.py`,
  `experiments/compare_regularizations.py`) pass `include_pole=False`
  explicitly so the tables of chapters 8 and 9 remain reproducible.
- All statements in this chapter about cancellation and agreement are
  floating-point observations at stated cutoffs, not certified enclosures.
  Interval versions of the zero-side comparison are a natural next
  certification target.
- Nothing here bears on the infinite-dimensional questions listed in
  `paper/11_variational_foundation.md`, and nothing here is evidence for or
  against RH beyond consistency of the computed finite objects with the
  classical explicit formula.

## 7. Reproduction

```bash
python -m experiments.pole_cancellation
python -m experiments.dirichlet_zero_side
python -m pytest tests/test_poles.py tests/test_dirichlet_zero_side.py
```

Committed run records: `paper/data/pole-cancellation.csv` and
`paper/data/dirichlet-zero-side.csv`.
