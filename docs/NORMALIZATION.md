# Normalization ledger

This document is the source of truth for every sign, Fourier convention, packet normalization, and matrix coordinate convention used by the code.

## 1. Status

The packet and finite prime-power conventions below are implemented and tested. The conductor and archimedean terms are not yet implemented. Therefore the repository currently constructs a rigorously defined **truncated prime matrix**, not a complete Weil explicit-formula operator.

## 2. Hilbert-space convention

The ambient pairing is the ordinary real inner product

\[
\langle f,g\rangle = \int_{\mathbb R} f(x)g(x)\,dx.
\]

Complex conjugation will be added when complex packet families are introduced.

## 3. Gaussian packets

For center \(t_j\in\mathbb R\) and bandwidth \(\sigma>0\),

\[
g_j(x)=\exp\!\left(-\frac{(x-t_j)^2}{2\sigma^2}\right).
\]

These packets have unit amplitude, not unit \(L^2\)-norm. Their Gram matrix is

\[
B_{ij}=\langle g_i,g_j\rangle
=\sqrt{\pi}\,\sigma\,
\exp\!\left(-\frac{(t_i-t_j)^2}{4\sigma^2}\right).
\]

## 4. Translation convention

Define

\[
(\tau_u g)(x)=g(x-u).
\]

The translated correlation matrix is

\[
C(u)_{ij}=\langle g_i,\tau_u g_j\rangle
=\sqrt{\pi}\,\sigma\,
\exp\!\left(-\frac{(t_i-t_j-u)^2}{4\sigma^2}\right).
\]

It satisfies \(C(-u)=C(u)^\mathsf{T}\).

## 5. Universal prime-power matrix

For an integer \(n\ge2\), define

\[
T_n=-\bigl(C(\log n)+C(-\log n)\bigr).
\]

Thus \(T_n\) is real symmetric. The minus sign is included in \(T_n\), not in the arithmetic coefficient.

## 6. Primitive quadratic character

For a fundamental discriminant \(D\),

\[
\chi_D(n)=\left(\frac{D}{n}\right)
\]

is evaluated using the Kronecker symbol. Its conductor is \(|D|\), and its parity is 0 for \(D>0\) and 1 for \(D<0\).

## 7. Arithmetic coefficient

For the current reconstruction,

\[
\beta_D(n)=\frac{\Lambda(n)\chi_D(n)}{\sqrt n},
\]

where \(\Lambda(n)=\log p\) if \(n=p^k\) and is zero otherwise.

The truncated prime matrix is

\[
A_{\mathrm{prime}}(N;D)
=\sum_{2\le n\le N}\beta_D(n)T_n.
\]

This identity is exact by definition for the implemented finite sum.

## 8. Coordinate convention

Matrices store sesquilinear-form entries in the nonorthogonal packet basis. Spectral calculations therefore use the generalized problem

\[
A v=\lambda Bv,
\]

where \(B\) is the packet Gram matrix. Ordinary eigenvalues of \(A\) are not basis-invariant and should not be interpreted as operator eigenvalues.

## 9. Deliberately unresolved conventions

Before a complete finite Weil operator is implemented, the following must be independently derived and recorded:

- Fourier transform sign and \(2\pi\) factors;
- the exact completed \(L\)-function normalization;
- the conductor contribution;
- gamma-factor and parity contributions;
- the admissible test-function class;
- the relationship between the packet variable and the explicit-formula transform variable;
- rigorous truncation and interval-error bounds.

Historical scripts may be used as comparison data, but they are not authoritative for any of these choices.
