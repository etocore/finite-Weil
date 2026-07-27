# Correction and supersession ledger

This file records interpretations that appeared in earlier repository chapters but were changed by later derivations or implementation audits. Historical files and data are retained for reproducibility; this ledger governs how they may be cited in current work.

## 1. Principal-character pole omission

### Affected material

- historical convergence sweeps involving `D = 1`;
- `paper/09_prime_cutoff_geometry.md`;
- any downstream discussion that treated the stabilized negative eigenvalues near `-903`, `-912`, or `-1205` as candidate negative Weil directions;
- any dimension-dependence interpretation built from those pole-free values.

### Correction

The completed Riemann zeta function has poles at `s = 0` and `s = 1`. In the repository's Gaussian packet convention their finite contribution is

\[
P=p_-p_+^T+p_+p_-^T,
\qquad
P_{ij}=4\pi\sigma^2e^{\sigma^2/4}\cosh\!\left(\frac{c_i-c_j}{2}\right).
\]

The earlier `D = 1` matrices omitted `P`. They therefore approximated `Z-P`, not the completed-zeta zero-side matrix `Z`. The large stabilized negative eigenvalues are explained by the Gram-metric spectrum of `-P` and are not negative Weil certificates.

### Current rule

`WeilOperator(include_pole=None)` includes the pole automatically exactly when the conductor is one. Pole-free `D = 1` assembly is allowed only when explicitly reproducing a labeled historical experiment.

## 2. Prime-cutoff convergence

The historical geometric rule `log N >> max |c_i-c_j|` was a useful heuristic but is no longer the governing error statement. `paper/14_certified_prime_tail.md` proves an explicit fixed-space tail inequality. The code evaluates that formula in floating point; it is not yet a directed-rounding enclosure.

Current work must distinguish:

- the proved analytic inequality;
- its ordinary floating-point numerical evaluation;
- a future interval-certified evaluation.

The words `certified cutoff` or `certified budget` must not be used for the current floating-point evaluation unless the surrounding sentence explicitly says that only the formula, not its numerical value, is rigorous.

## 3. Zero-side validation

Agreement between arithmetic-side and zero-side matrices has been reproduced for `D = 1, 5, -3, 8, 13` and recorded in committed scripts and CSV artifacts. These comparisons are floating-point observations. They validate the normalization chain on the tested finite packet spaces but do not prove RH, GRH, convergence on an infinite-dimensional class, or completeness of the zero lists beyond the stated envelope threshold.

A zero-side matrix assembled from critical-line ordinates is positive semidefinite by construction. Its positivity is not an independent RH test; the substantive observation is the agreement of the independently assembled arithmetic side with that matrix.

## 4. Off-critical zeros and matrix-pencil recovery

The original real-frequency recovery pipeline was suitable for sums of undamped cosines. An off-critical zero pair would introduce exponential or hyperbolic modulation in the sample coordinate, not merely a cosine with an anomalous scalar amplitude.

The current matrix pencil therefore reports complex modes

\[
z_j=e^{(\alpha_j+i\omega_j)\Delta},
\qquad
\alpha_j=\frac{\log|z_j|}{\Delta}.
\]

Synthetic tests show that an off-circle mode can be recovered when inserted. This establishes representation capability only. The repository does not yet claim a sensitivity theorem, a false-positive bound, or a validated detector for off-critical zeros.

## 5. Small-bandwidth Toeplitz interpretation

Equally spaced Gaussian packet matrices are Toeplitz because their entries depend on center differences. Under a critical-line positive zero measure, Bochner-Herglotz explains finite-section positivity.

The stronger idea that RH failure must produce a negative dip in the sampled Toeplitz symbol is conjectural. A proof would still need to establish:

1. the exact sampled-kernel form of an off-critical contribution;
2. Hermitian reality of the relevant symbol;
3. survival of nonpositivity under Gaussian smoothing;
4. detection by a finite section;
5. control of aliasing and spacing.

## 6. Collision and flat-limit work

The Gaussian collision filtration, local Smith-normal-form calculations, and flat-limit packet geometry are mathematically separate from the pole omission. They remain valid unless a specific theorem depends on the old pole-free `D = 1` spectral interpretation.

They must not be presented as explaining an RH counterexample. Their current significance is geometric: they describe how nearly colliding packet coordinates decompose into graded directions and how Gram whitening amplifies small modeling errors in poorly resolved grades.

## 7. Citation rule for historical chapters

A current chapter may cite a historical pole-free `D = 1` table only when it states, in the same paragraph, that:

- the pole block was omitted;
- the values are retained solely for reproduction or diagnosis;
- the completed-zeta interpretation is superseded by papers 12 and 13.

Current mathematical claims should cite the corrected assembly and committed run records rather than the old negative spectra.
