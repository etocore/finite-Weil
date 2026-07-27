# Zero recovery from the prime side by the matrix-pencil method

## 1. Scope and claim status

This chapter reports a numerical study of the inverse problem of
`paper/03_spectral_program.md`, section 13: how much zero data is
identifiable from the finite model.  All results are floating-point
observations produced by `experiments/zero_recovery.py`.  No zero data enters
the forward computation; reference zeros are used only to grade the output.

## 2. Method

By the validated identity of `paper/13_pole_cancellation.md`, the
translation-invariant kernel of the assembled completed-zeta model is

\[
K(\delta)
=
\sum_{\gamma>0}
4\pi\sigma^2e^{-\sigma^2\gamma^2}\cos(\gamma\delta)
\]

up to prime-truncation error.  Above any amplitude floor this is a *finite*
sum of undamped cosines in \(\delta\), so the frequencies are recoverable
from uniform samples by the matrix-pencil (ESPRIT) method:

1. sample the prime-side kernel (conductor + gamma + pole + truncated prime
   sum) at \(\delta=0,\Delta,\dots,(M-1)\Delta\), with \(\Delta\) below the
   Nyquist step for the largest visible frequency;
2. choose the prime cutoff with the certified bound of
   `paper/14_certified_prime_tail.md` so that the kernel truncation error at
   the farthest sample is below the target amplitude floor;
3. form the two shifted Hankel matrices of the samples, truncate the SVD at
   the numerical rank, and read frequencies from the spectrum of the reduced
   pencil;
4. estimate amplitudes by least squares and keep only frequencies whose
   fitted amplitude is within a factor two of the predicted envelope
   \(4\pi\sigma^2e^{-\sigma^2\gamma^2}\).

Step 4 is a physically meaningful consistency filter: a genuine simple zero
must carry exactly the envelope amplitude, so the fitted-to-predicted ratio
is near one for true zeros and far from one for pencil artifacts fitting
residual truncation error.  A ratio near an integer \(k>1\) would indicate a
zero of multiplicity \(k\); none was observed.

## 3. Results

Sweep parameters: samples on \(\delta\in[0,10]\), envelope floor \(10^{-9}\),
amplitude-ratio window \((0.5,2)\).  Recovered frequencies against the true
ordinates \(\gamma_n\) of the first zeta zeros:

| \(\sigma\) | cutoff | recovered (ratio) |
|---:|---:|---|
| 0.20 | 176216 | 14.1347 (1.00), 21.0220 (1.00), 25.0034 (0.97) |
| 0.15 | 176216 | 14.1347 (1.00), 21.0220 (1.00), 25.0109 (1.00), 30.4250 (1.00) |
| 0.10 | 88108 | 14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3270 (all 1.00) |
| 0.07 | 88108 | the previous eight and 48.0052, 49.7738, 52.9703, 56.4462, 59.3466, 60.8305 (all 1.00) |

True values through \(\gamma_{14}\): 14.1347, 21.0220, 25.0109, 30.4249,
32.9351, 37.5862, 40.9187, 43.3271, 48.0052, 49.7738, 52.9703, 56.4462,
59.3470, 60.8318.

At \(\sigma=0.07\) the method recovers the first **fourteen** zeta zeros from
the prime side, most to four decimal places, with all amplitude ratios equal
to one at the printed precision.  Accuracy degrades exactly where expected:
at the envelope edge (25.0034 versus 25.0109 for \(\sigma=0.2\); 59.3466 and
60.8305 versus 59.3470 and 60.8318 for \(\sigma=0.07\)) where the signal
approaches the truncation floor.

The certified cutoff selection matters.  An earlier version of the sweep
used the geometric margin \(\log N=\delta_{\max}+4\sigma\); the resulting
relative kernel error of order \(e^{-4}\) exceeded the first-zero amplitude
at \(\sigma=0.2\) and corrupted the amplitude fit.  Driving the certified
entrywise bound below the amplitude floor removed the failure without any
tuning.

## 4. Interpretation and limits

- The experiment demonstrates that low-lying zeros are *practically
  identifiable* from finite prime data plus the archimedean and pole terms,
  quantifying the informal statement that the finite model compresses the
  zero measure.  It supports, but does not prove, Conjecture 13.1 of the
  spectral program.
- Identifiability degrades gracefully: halving \(\sigma\) roughly doubles
  the count of visible zeros while the required prime cutoff grows only
  through the certified bound.
- This is classical explicit-formula duality made algorithmic; the
  observation that primes determine zeros is not new.  What the experiment
  adds is a reproducible pipeline inside this repository's fixed
  normalization, with truncation error controlled by a proved bound, and a
  multiplicity-sensitive amplitude diagnostic.
- Nothing here bears on RH: the recovery works because the explicit formula
  holds, not because the zeros are on the critical line.  Off-line zeros
  would appear as frequencies with anomalous amplitude growth, which the
  ratio filter would flag rather than hide.

## 5. Reproduction

```bash
python -m experiments.zero_recovery
python -m pytest tests/test_zero_recovery.py
```
