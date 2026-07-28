# Prime-cutoff geometry in the Gaussian packet model

## 1. Scope, status, and supersession notice

This chapter records a historical cutoff experiment and the geometric lesson that
survived it.

The numerical table below was produced with the principal character \(D=1\) and
with the completed-zeta pole block deliberately omitted. In the current code this
historical convention is explicit:

```python
WeilOperator(..., include_pole=False)
```

Therefore the displayed negative eigenvalues are **not** eigenvalues of the
correctly assembled completed-zeta Weil form. They are spectra of the historical
pole-free matrix

\[
A_{\mathrm{hist}}(N)
=
A_{\mathrm{cond}}+A_\Gamma+A_{\mathrm{prime}}(N),
\]

whereas the corrected principal-character assembly is

\[
A_{\zeta}(N)
=
A_{\mathrm{cond}}+A_\Gamma+A_{\mathrm{prime}}(N)+P.
\]

`paper/12_pole_term.md` derives \(P\), and
`paper/13_pole_cancellation.md` shows numerically that adding \(P\) removes the
large negative spectrum at resolved cutoffs and restores agreement with the
independently computed zero side.

The historical data are retained only because they isolate an important numerical
fact: the prime cutoff must be deep enough to resolve the translation geometry of
the packet family. No result in this chapter is evidence for a negative Weil
direction, a failure of Weil positivity, or a failure of the prime series to
converge.

## 2. The geometric cutoff mechanism

For packet centers \(t_i,t_j\), the implemented universal prime kernel contains
terms of the form

\[
\exp\!\left[-\frac{(t_i-t_j-\log n)^2}{4\sigma^2}\right]
+
\exp\!\left[-\frac{(t_i-t_j+\log n)^2}{4\sigma^2}\right].
\]

Writing

\[
\delta=t_i-t_j,
\]

the Gaussian envelopes are centered near

\[
\log n=\pm\delta.
\]

Since \(n\ge 1\), the relevant positive arithmetic scale is approximately

\[
\log n\approx |\delta|.
\]

This is an entrywise localization statement about the Gaussian factors. It does
not by itself locate the maximum of the fully weighted prime-power summand, which
also contains arithmetic coefficients and logarithmic weights.

If all centers lie in \([-E,E]\), then

\[
|\delta|\le 2E.
\]

For the historical experiment \(E=6\), so the largest center separation is \(12\)
and the corresponding geometric scale is

\[
e^{12}\approx 1.63\times 10^5.
\]

A cutoff \(N=1000\), with

\[
\log 1000\approx 6.91,
\]

therefore ends before the Gaussian envelopes associated with the most widely
separated packet pairs have reached their centers. The drift observed between
cutoffs \(50\) and \(1000\) was consequently insufficient evidence for divergence.
That geometric conclusion remains valid after the pole correction.

## 3. Historical pole-free deep-cutoff experiment

The historical computation used:

- principal quadratic character \(D=1\);
- packet width \(\sigma=0.5\);
- equally spaced centers in \([-6,6]\);
- dimensions \(8,16,32\);
- sharp prime-power cutoffs;
- Gram whitening with relative tolerance \(10^{-12}\);
- `include_pole=False`.

Prime powers were enumerated by the repository's sieve and the matrix entries were
assembled in floating-point arithmetic. The enumeration is discrete and explicit,
but the resulting spectra are floating-point observations, not exact or certified
values.

The smallest generalized eigenvalues of the historical pole-free matrix were:

| Cutoff | Dimension 8 | Dimension 16 | Dimension 32 |
|---:|---:|---:|---:|
| \(10^3\) | -77.261251 | -81.809745 | -84.013169 |
| \(10^4\) | -184.321091 | -193.097891 | -198.802181 |
| \(10^5\) | -460.784957 | -490.688205 | -510.838588 |
| \(3\times10^5\) | -725.191698 | -743.991921 | -790.844860 |
| \(10^6\) | -895.488179 | -903.030325 | -1142.492673 |
| \(3\times10^6\) | -903.739890 | -911.500808 | -1204.569757 |
| \(10^7\) | -903.790915 | -911.553565 | -1205.255819 |

For each fixed retained packet space, the pole-free sequence changed much less
between \(3\times10^6\) and \(10^7\) than at earlier cutoffs. The changes in the
reported minima were approximately

- \(0.0510\) for dimension \(8\);
- \(0.0528\) for dimension \(16\);
- \(0.6861\) for dimension \(32\).

These observations show stabilization of the **historical truncated matrix** over
that final cutoff interval. They do not prove convergence of the infinite prime
series and do not describe the spectrum of the corrected completed-zeta form.

## 4. Corrected interpretation

The later pole analysis identifies the large negative spectrum. At
\(\sigma=0.5\), the zero-side Gaussian envelope suppresses the first zeta zero by
roughly \(e^{-\sigma^2\gamma_1^2}\), making the exact zero-side matrix numerically
negligible at the tested precision. Consequently,

\[
A_{\mathrm{hist}}(\infty)
=
Z-P
\approx -P,
\]

while

\[
A_{\zeta}(\infty)
=
Z
\approx 0.
\]

The historical minima near \(-903.8\), \(-911.6\), and \(-1205.3\) are therefore
associated with minus the rank-two pole block in the corresponding Gram geometries.
They are not candidate counterexamples to Weil positivity.

The dimension dependence is likewise no longer an unexplained sign of spectral
instability. It reflects how the fixed pole vectors are represented and whitened in
different packet spaces, together with the retained-rank rule used by the numerical
solver.

The corrected comparison in `paper/13_pole_cancellation.md` gives, at cutoff
\(10^7\):

| Dimension | Pole-free \(\lambda_{\min}\) | Corrected \(\lambda_{\min}\) | Corrected \(\lambda_{\max}\) |
|---:|---:|---:|---:|
| 8 | -903.790915 | -0.000017 | 0.000017 |
| 16 | -911.553565 | -0.000026 | 0.000026 |

These corrected values are still floating-point and cutoff-dependent. Their role is
to demonstrate cancellation and consistency with the zero-side envelope, not to
certify exact positivity or exact vanishing.

## 5. What the experiment actually establishes

The defensible conclusion is limited and useful:

1. Packet geometry predicts which logarithmic prime scales must be sampled before
   widely separated packet correlations are resolved.
2. A cutoff with \(\log N<2E\) necessarily truncates before some Gaussian kernel
   centers when packets occupy \([-E,E]\).
3. Apparent stabilization at a few cutoff values is only a numerical observation.
4. Cutoff refinement and packet-space refinement are mathematically distinct
   operations and must not be conflated.
5. For the principal character, all present-day spectral conclusions must use the
   pole-corrected assembly.

The earlier statement that the prime-cutoff problem was "primarily" insufficient
arithmetic depth was too broad. Insufficient depth explained the early cutoff drift,
but the large limiting negative spectrum came from the omitted pole block.

## 6. Cutoff guidance and rigorous tail control

The inequality

\[
\log N>2E
\]

is a useful geometric screening condition: it places the cutoff beyond the centers
of all packet-pair Gaussian envelopes. It is not a convergence theorem and is not
sufficient for a requested error tolerance. The remaining tail depends on

- the packet width \(\sigma\);
- the distance of \(\log N\) beyond each center separation;
- the arithmetic weights;
- the matrix dimension and Gram conditioning;
- the norm in which the truncation error is measured.

The historical notation

\[
\log N\gg 2E
\]

should therefore be read only as informal guidance, not as a quantified rule.

The theorem-facing tail analysis is no longer future work. It is developed in
`paper/14_certified_prime_tail.md`, which gives an analytic entrywise tail bound and
a corresponding generalized-eigenvalue perturbation budget on a fixed packet
space. Numerical evaluation of that chain is not automatically an interval
certificate unless every bound is evaluated with directed rounding or another
verified enclosure method.

## 7. Dependency and supersession map

**Depends on**

- the Gaussian packet and prime-kernel definitions used by the implementation;
- the generalized eigenvalue and Gram-whitening conventions;
- `paper/12_pole_term.md` for the corrected principal-character operator;
- `paper/13_pole_cancellation.md` for the corrected numerical interpretation;
- `paper/14_certified_prime_tail.md` for rigorous truncation control.

**Supersedes**

- the interpretation that the large negative deep-cutoff eigenvalues might be
  genuine negative Weil directions;
- the claim that their dimension dependence remained unexplained;
- the statement that deriving a prime-tail estimate was the next theorem-facing
  task.

**Used by later work only for**

- the geometric separation of cutoff refinement from packet-space refinement;
- the warning that common shallow cutoffs can compare differently resolved matrix
  entries;
- reproduction of the intentionally pole-free historical table.

No later work may cite the negative table as a property of the corrected
completed-zeta operator.

## 8. Reproduction

The historical table is reproduced by

```bash
python -m experiments.deep_cutoff
```

The script explicitly sets `include_pole=False` and writes

```text
artifacts/deep-cutoff.csv
```

The corrected pole comparison is reproduced separately by

```bash
python -m experiments.pole_cancellation
```

with committed output documented in `paper/13_pole_cancellation.md` and
`paper/data/pole-cancellation.csv`.
