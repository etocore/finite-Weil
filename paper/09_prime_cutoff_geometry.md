# Prime-cutoff geometry in the Gaussian packet model

## Correction to the first cutoff interpretation

The downward drift observed for cutoffs \(N\le 1000\) was initially described as
possible evidence that the sharp prime sum did not define a convergent numerical
scheme. That interpretation was premature.

For packet centers \(t_i,t_j\), the universal prime kernel contains

\[
\exp\!\left[-\frac{(t_i-t_j-\log n)^2}{4\sigma^2}\right]
+
\exp\!\left[-\frac{(t_i-t_j+\log n)^2}{4\sigma^2}\right].
\]

Consequently, the entry indexed by center difference

\[
\delta=t_i-t_j
\]

is largest near

\[
\log n\approx |\delta|.
\]

When centers fill \([-6,6]\), the largest difference is \(12\). The corresponding
arithmetic scale is

\[
e^{12}\approx 1.63\times 10^5.
\]

A cutoff of \(1000\), for which \(\log 1000\approx 6.91\), therefore stops before
many off-diagonal packet correlations reach their dominant prime range. The large
drift between \(50\) and \(1000\) is expected from packet geometry alone and does
not diagnose divergence.

## Exact deep-cutoff experiment

The sharp prime sum was recomputed for the trivial quadratic character \(D=1\),
packet width \(\sigma=0.5\), centers on \([-6,6]\), and dimensions \(8,16,32\).
Prime powers were enumerated exactly by a sieve, and matrix kernels were assembled
in vectorized chunks. Spectra were computed after Gram whitening at relative
tolerance \(10^{-12}\).

The smallest generalized eigenvalues were:

| Cutoff | Dimension 8 | Dimension 16 | Dimension 32 |
|---:|---:|---:|---:|
| \(10^3\) | -77.261251 | -81.809745 | -84.013169 |
| \(10^4\) | -184.321091 | -193.097891 | -198.802181 |
| \(10^5\) | -460.784957 | -490.688205 | -510.838588 |
| \(3\times10^5\) | -725.191698 | -743.991921 | -790.844860 |
| \(10^6\) | -895.488179 | -903.030325 | -1142.492673 |
| \(3\times10^6\) | -903.739890 | -911.500808 | -1204.569757 |
| \(10^7\) | -903.790915 | -911.553565 | -1205.255819 |

For each fixed packet dimension, the sharp-cutoff sequence is effectively stable
between \(3\times10^6\) and \(10^7\). The remaining change is approximately

- \(0.0510\) for dimension \(8\);
- \(0.0528\) for dimension \(16\);
- \(0.6861\) for dimension \(32\).

Thus the prime-cutoff problem is primarily one of insufficient arithmetic depth,
not failure of the exact Gaussian packet prime series to settle.

## What remains unresolved

The deep-cutoff experiment resolves only cutoff convergence for a fixed packet
space. It does **not** establish convergence as packet dimension increases. In
fact, the limiting values for dimensions \(8,16,32\) differ substantially, with
the dimension-32 minimum much lower than the dimension-16 minimum. This can arise
from newly resolved packet modes, edge effects, basis geometry, or the mathematical
normalization of the assembled form.

The next convergence study must therefore separate two limits:

1. arithmetic refinement \(N\to\infty\) at fixed packet space;
2. packet-space refinement after the arithmetic sum is resolved to the geometry of
   that space.

Comparing dimensions at a common small cutoff mixes these limits and can produce a
misleading picture.

## Practical cutoff rule

For centers contained in \([-E,E]\), the largest difference is \(2E\). A first
geometry-aware cutoff should satisfy

\[
\log N \gg 2E,
\]

with additional margin depending on \(\sigma\) and the desired Gaussian tail
suppression. The present experiment used \(E=6\), \(\sigma=0.5\), and found that
\(N=10^7\) was sufficient to stabilize the tested fixed spaces numerically.

This is an empirical resolution rule, not yet a certified tail bound. Deriving an
explicit matrix tail estimate from the Gaussian envelope is the next theorem-facing
task.

## Reproduction

Run

```bash
python -m experiments.deep_cutoff
```

The default output is

```text
artifacts/deep-cutoff.csv
```
