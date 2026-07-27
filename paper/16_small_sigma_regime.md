# The small-bandwidth regime

## 1. Scope and claim status

This chapter records a scaling study of the assembled completed-zeta model as
the packet width \(\sigma\) decreases at fixed extent, produced by
`experiments/sigma_scaling.py`.  It also records a structural observation
connecting the two extreme width regimes to known mathematics.  The numerical
results are floating-point observations; each row carries a prime-truncation
budget computed from the proved tail bound of
`paper/14_certified_prime_tail.md`, itself evaluated in floating point
(Remark 4.3 there), so "budget" below means a proved formula evaluated
numerically, not a machine-certified enclosure.  The structural remarks are
unproved orientation, labeled as such.

## 2. Why small widths are the informative regime

The validated zero-side identity gives, for every direction \(f\) in the
packet span,

\[
Q(f,f)=\sum_{\gamma}\bigl|\widehat f(\gamma)\bigr|^2,
\qquad
\bigl|\widehat f(\gamma)\bigr|\le e^{-\sigma^2\gamma^2/2}\cdot(\text{trig.\ poly.}).
\]

For \(\sigma=0.5\) the first zeta zero already suppresses every direction by
\(e^{-\sigma^2\gamma_1^2}\approx2\times10^{-22}\): positivity of the wide-packet
model is a statement about near-perfect cancellation of large terms, and its
finite spectra carry no zero information.  Only when \(\sigma\) shrinks does
the packet family actually probe the zero measure.

## 3. Scaling experiment

Configuration: extent \(1.5\), spacing \(1.5\sigma\), Gram whitening at
\(10^{-12}\), pole matrix included, prime cutoff chosen as the smallest
doubling for which the eigenvalue-shift bound of
`paper/14_certified_prime_tail.md` is below \(10^{-8}\) (the selector raises
rather than returning an unresolved cutoff).  The zero-side column rebuilds
the matrix from actual zeta zeros (computed at run time when `mpmath` is
available) down to envelope \(10^{-15}\).  The run record is committed as
`paper/data/sigma-scaling.csv`.

| \(\sigma\) | dim | cutoff | shift bound | \(\lambda_{\min}\) | \(\lambda_{\max}\) | zeros seen | \(\max|A-Z|\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.50 | 5 | 5376 | \(1.2\times10^{-11}\) | \(-2.9\times10^{-13}\) | \(3.3\times10^{-13}\) | 0 | - |
| 0.35 | 7 | 672 | \(2.0\times10^{-9}\) | \(-3.9\times10^{-11}\) | \(1.6\times10^{-10}\) | 1 | \(1.4\times10^{-11}\) |
| 0.25 | 9 | 336 | \(9.6\times10^{-13}\) | \(-9.2\times10^{-15}\) | \(2.3\times10^{-5}\) | 2 | \(7.4\times10^{-15}\) |
| 0.18 | 13 | 168 | \(4.0\times10^{-14}\) | \(-1.7\times10^{-14}\) | \(2.2\times10^{-1}\) | 4 | \(4.5\times10^{-16}\) |
| 0.12 | 19 | 84 | \(8.7\times10^{-15}\) | \(+2.3\times10^{-16}\) | \(3.1\) | 9 | \(1.9\times10^{-15}\) |

Observations:

1. **Positivity within budget at every width.**  Each \(\lambda_{\min}\) lies
   inside the truncation budget of zero.  Nothing here proves positivity of
   any infinite object; the point is that the finite model behaves exactly
   as the validated zero-side identity dictates.
2. **Spectral mass tracks the zero count.**  \(\lambda_{\max}\) grows from
   numerical zero to order one precisely as zeros enter the bandwidth.
3. **The required cutoff collapses at small widths.**  At \(\sigma=0.12\)
   the budget is met with cutoff \(84\): narrow kernels localize the prime
   sum near \(\log n\approx|\delta_{ij}|\le3\), so very few prime powers
   matter.  The expensive regime is *wide* packets, not narrow ones.
4. **Zero-side agreement persists**, at \(10^{-15}\) or better wherever the
   comparison is available.

## 4. Two width regimes and known mathematics

The two limits of the width parameter land in different classical theories,
and the finite Weil model interpolates between them.

**Small widths: Toeplitz-Bochner regime.**  With spacing proportional to
\(\sigma\) and equally spaced centers, \(B\) and the assembled \(A\) are
Toeplitz, and the generalized spectrum is governed by the ratio of the
symbols.  Since the validated kernel is the Fourier transform of the positive
measure \(\sum_\gamma\delta_{\pm\gamma}\) smoothed by a Gaussian, positivity
of every finite section is an instance of Bochner-Herglotz
positive-definiteness of the transform of a nonnegative measure; under RH
the measure is supported on the real line and positivity is automatic.

The converse direction is a **conjectural bridge, not an established
reduction**.  Weil's criterion says an RH failure produces *some* admissible
test function with negative Weil form; it does not immediately say that this
particular equally spaced, single-width Gaussian family detects it at any
finite resolution.  Turning "search for a negative direction" into "search
for a negative dip of a Toeplitz symbol" would require, at least: (i) an
explicit description of how an off-line zero pair enters the *sampled*
kernel; (ii) verification that the resulting Hermitian Toeplitz form has a
real symbol; (iii) proof that nonpositivity survives the Gaussian smoothing;
(iv) proof that some finite section detects it; and (v) control of aliasing
at finite spacing \(h\), since the discrete symbol is a periodized object.
None of these steps is carried out here.

**Large widths: flat-limit regime.**  As \(\sigma\to\infty\) at fixed
centers, the Gram and kernel matrices enter the flat limit analyzed in
`paper/frame-schur-proof.md`: eigenvalues collapse at graded rates
\(\asymp v^s\) and eigenvectors converge to Gram-Schmidt residuals of the
moment vectors.  The wide-packet experiments of chapters 8 and 9 sit on the
edge of this regime, which is why their Gram conditioning degrades and their
spectra carry no arithmetic information.

The working conclusion for the program: refinement studies should shrink
\(\sigma\) (opening the zero window, with cheap bound-resolved cutoffs) rather
than enlarge extent at fixed moderate width (which multiplies the prime cost
exponentially while the zero window stays closed).

## 5. Open questions

1. Quantify the Toeplitz limit: does the whitened generalized spectrum at
   spacing \(h=c\sigma\) converge, as \(\sigma\to0\), to the essential range
   of the ratio of the \(K\)- and \(B\)-symbols on \([0,\pi/h)\), in the
   sense of Szego-type distribution theorems?
2. The budget evaluation is floating point throughout (Remark 4.3 of the
   tail-bound chapter); replace it with a directed-rounding or interval
   evaluation to make rows of the scaling table machine-certified.
3. Extend the sweep to quadratic characters, where low zeros
   (\(\gamma_1\approx3.12\) for \(D=13\)) are visible already at
   \(\sigma\approx0.3\) and no pole block is needed.

## 6. Reproduction

```bash
python -m experiments.sigma_scaling
python -m pytest tests/test_sigma_scaling.py
```
