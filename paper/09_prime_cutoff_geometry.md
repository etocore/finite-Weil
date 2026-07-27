# Prime-cutoff geometry in the Gaussian packet model

## Historical status and supersession

This chapter records a useful prime-cutoff geometry experiment, but its `D = 1` spectra were computed before the completed-zeta pole block was implemented. The negative eigenvalues in the historical table are therefore **not** eigenvalues of the completed-zeta Weil form.

For the principal character, the corrected assembly is

\[
A_\zeta(N)
=
A_{\mathrm{cond}}
+
A_\Gamma
+
A_{\mathrm{prime}}(N)
+
P,
\]

where

\[
P_{ij}
=
4\pi\sigma^2e^{\sigma^2/4}
\cosh\!\left(\frac{c_i-c_j}{2}\right).
\]

Papers 12 and 13 show that the historical pole-free matrix approached `Z-P`, so its large stabilized negative direction is the Gram-metric signature of the omitted rank-at-most-two pole contribution. The table below is retained only to document the failure mode and the arithmetic depth required to resolve the packet geometry.

## 1. Why shallow cutoffs drift

For packet centers \(c_i,c_j\), the universal prime kernel contains

\[
\exp\!\left[-\frac{(c_i-c_j-\log n)^2}{4\sigma^2}\right]
+
\exp\!\left[-\frac{(c_i-c_j+\log n)^2}{4\sigma^2}\right].
\]

For the center difference

\[
\delta=c_i-c_j,
\]

the contribution is largest near

\[
\log n\approx |\delta|.
\]

When the centers fill \([-6,6]\), the largest difference is \(12\), corresponding to

\[
e^{12}\approx1.63\times10^5.
\]

A cutoff of \(1000\), with \(\log 1000\approx6.91\), stops before many off-diagonal packet correlations reach their dominant prime range. The drift between cutoffs \(50\) and \(1000\) is therefore expected from packet geometry and does not diagnose divergence.

This geometric explanation remains valid after the pole correction.

## 2. Historical pole-free deep-cutoff experiment

The sharp prime sum was computed for the trivial quadratic character `D = 1`, packet width \(\sigma=0.5\), centers on \([-6,6]\), and dimensions \(8,16,32\). Prime powers were enumerated by sieve, matrices were assembled in vectorized chunks, and spectra were computed after Gram whitening at relative tolerance \(10^{-12}\).

The script now pins `include_pole=False` explicitly so that these historical values remain reproducible.

| Cutoff | Dimension 8 | Dimension 16 | Dimension 32 |
|---:|---:|---:|---:|
| \(10^3\) | -77.261251 | -81.809745 | -84.013169 |
| \(10^4\) | -184.321091 | -193.097891 | -198.802181 |
| \(10^5\) | -460.784957 | -490.688205 | -510.838588 |
| \(3\times10^5\) | -725.191698 | -743.991921 | -790.844860 |
| \(10^6\) | -895.488179 | -903.030325 | -1142.492673 |
| \(3\times10^6\) | -903.739890 | -911.500808 | -1204.569757 |
| \(10^7\) | -903.790915 | -911.553565 | -1205.255819 |

For each fixed packet dimension, the pole-free sharp-cutoff sequence is numerically stable by the deepest cutoffs. That stabilization established that the prime sum was resolving the fixed packet geometry. It did **not** establish a negative Weil direction.

After adding \(P\), the dimension-8 and dimension-16 spectra collapse toward the tiny zero-side mass, as recorded in `paper/13_pole_cancellation.md` and `paper/data/pole-cancellation.csv`.

## 3. Correct interpretation of the dimension dependence

The differing pole-free limits across dimensions were originally listed as unresolved. The dominant explanation is now known: the omitted pole block has packet-coordinate vectors

\[
(p_\pm)_j
=
\sigma\sqrt{2\pi}\,e^{\sigma^2/8}e^{\pm c_j/2},
\]

and its generalized spectrum depends on the Gram geometry of those vectors inside the chosen packet family. Changing dimension or center placement changes that geometry.

This does not settle every possible packet-refinement question. It does settle the specific interpretation of the large negative `D = 1` values in this chapter.

## 4. Arithmetic refinement versus packet refinement

Two limits must still be separated:

1. arithmetic refinement \(N\to\infty\) at fixed packet space;
2. packet-space refinement after the arithmetic sum is resolved for that space.

Comparing dimensions at a common shallow cutoff mixes these limits. The fixed-space arithmetic tail is now controlled by the explicit inequality in `paper/14_certified_prime_tail.md`. Its formula is rigorous; the current code evaluates it in ordinary floating point rather than directed rounding.

## 5. Current cutoff rule

The old heuristic

\[
\log N\gg 2E
\]

for centers in \([-E,E]\) remains a useful geometric orientation, but it is no longer the repository's error bound. Current experiments choose cutoffs by evaluating the analytic entrywise tail formula and, when needed, the induced generalized-eigenvalue perturbation budget.

The expensive \(N=10^7\) regime in this chapter is associated with wide packets over a large extent. Paper 16 shows that shrinking \(\sigma\) both opens the zero bandwidth and sharply reduces the required prime cutoff.

## 6. Reproduction

Run

```bash
python -m experiments.deep_cutoff
```

The default output is

```text
artifacts/deep-cutoff.csv
```

The resulting `D = 1` matrices are intentionally pole-free historical artifacts. Use `experiments.pole_cancellation`, `experiments.dirichlet_zero_side`, or a default `WeilOperator` for the corrected completed-zeta assembly.
