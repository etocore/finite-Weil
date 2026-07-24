# Regularized prime-weight experiment

## Scope

This experiment compares three finite prime sums in the current Gaussian-packet
model:

\[
w_{\mathrm{sharp}}(n;N)=\mathbf 1_{n\le N},
\]

\[
w_{\exp}(n;N)=e^{-n/N},
\]

and

\[
w_{\log G}(n;N)
=
\exp\!\left[-\left(\frac{\log n}{\log N}\right)^2\right].
\]

The smooth sums were evaluated through \(8N\). Spectra were computed after Gram
whitening with relative tolerance \(10^{-12}\). These weights are numerical
regularizations only. They are not proved tail corrections for the Weil form.

The sweep used

- discriminants \(D=1,-3,5,8,13\);
- packet dimensions \(4,8,16,32\);
- widths \(\sigma=0.25,0.5,1.0\);
- prime scales \(N=50,100,250,500,1000\);
- packet centers evenly spaced on \([-6,6]\).

This gives 900 weighted spectral computations.

## Aggregate cutoff drift

For each fixed tuple \((D,m,\sigma,w)\), define

\[
\Delta_{50\to1000}
=
\lambda_{\min}(1000)-\lambda_{\min}(50).
\]

The mean absolute drift over all packet and character choices was:

| Weight | Mean absolute drift | Median absolute drift | Maximum absolute drift |
|---|---:|---:|---:|
| exponential | 8.924737 | 0.387135 | 62.058411 |
| log-Gaussian | 9.386776 | 0.349691 | 66.015781 |
| sharp | 10.048016 | 0.546299 | 70.217585 |

Both smooth weights reduce the aggregate drift relative to the sharp cutoff.
The exponential weight performs best by the mean and maximum criteria, while the
log-Gaussian weight has the smallest median drift. Neither regularization removes
the large negative drift in the most resolved cases.

## Baseline slice

For \(D=1\), dimension \(32\), and \(\sigma=0.5\), the smallest whitened
eigenvalues were:

| Prime scale | Sharp | Exponential | Log-Gaussian |
|---:|---:|---:|---:|
| 50 | -25.041713 | -21.693671 | -23.966442 |
| 100 | -32.750772 | -29.192417 | -31.861626 |
| 250 | -48.429273 | -42.630260 | -45.613050 |
| 500 | -64.383659 | -56.225676 | -59.104319 |
| 1000 | -84.013169 | -73.524848 | -76.173179 |

Smooth damping substantially reduces the magnitude of the negative eigenvalue,
but the sequence still moves downward as the prime scale increases. Thus the
observed instability is not merely a Gibbs-like artifact of the sharp boundary.

## Gram whitening

Whitening removed the direct generalized-eigensolver failures from the previous
experiment. For dimension \(32\), \(\sigma=1\), the Gram condition number is of
order \(10^{17}\). At tolerance \(10^{-12}\), 25 of the 32 packet modes are
retained. All other parameter combinations retain their full packet dimension.

This makes the reported spectra well-defined on the numerically stable packet
subspace, but it also changes the effective approximation space in the most
ill-conditioned regime. Results for dimension \(32\), \(\sigma=1\) must therefore
be interpreted as spectra of the truncated stable subspace, not of all nominal
packet coordinates.

## Conclusion

The experiment supports three numerical conclusions:

1. Gram whitening successfully stabilizes the packet-coordinate eigenproblem.
2. Smooth prime weights improve cutoff stability relative to the sharp sum.
3. The smallest eigenvalue still fails to stabilize in the highest-resolution
   slices, so smooth damping alone does not supply a convergent discretization.

The next mathematical task is therefore not to select the empirically best
weight. It is to derive a prime regularization from an admissible test-function
family or to establish a rigorous tail decomposition. Until that is done, the
prime-scale parameter remains part of the numerical model rather than a verified
convergence parameter.

## Reproduction

Run

```bash
python -m experiments.compare_regularizations
```

The default output is

```text
artifacts/regularized-comparison.csv
```
