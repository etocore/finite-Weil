# Completed primitive Dirichlet L-function convention

Let `chi` be a primitive Dirichlet character of conductor `q`, and define

\[
a = \frac{1-\chi(-1)}{2}\in\{0,1\}.
\]

The project fixes the completed function

\[
\Lambda(s,\chi)
=\left(\frac{q}{\pi}\right)^{(s+a)/2}
\Gamma\!\left(\frac{s+a}{2}\right)L(s,\chi).
\]

For a primitive real quadratic character `chi_D(n) = (D/n)`, the conductor is
`q = |D|`, and `a = 0` for `D > 0` while `a = 1` for `D < 0`.

## Immediate logarithmic derivatives

The power prefactor contributes

\[
\frac{d}{ds}\log\left(\frac{q}{\pi}\right)^{(s+a)/2}
=\frac12\log\left(\frac{q}{\pi}\right).
\]

The gamma factor contributes

\[
\frac{d}{ds}\log\Gamma\!\left(\frac{s+a}{2}\right)
=\frac12\psi\!\left(\frac{s+a}{2}\right),
\]

where `psi = Gamma'/Gamma` is the digamma function.

## What is frozen by this note

- conductor `q = |D|` for primitive quadratic characters;
- parity parameter `a = (1-chi(-1))/2`;
- gamma factor `Gamma((s+a)/2)`;
- power prefactor `(q/pi)^((s+a)/2)`;
- the constant logarithmic derivative `0.5 log(q/pi)`.

## What is not yet frozen

This note does **not** yet identify the exact finite packet-basis matrices produced by the conductor and gamma terms. That requires a single explicit-formula convention for the test function, Fourier transform, and zero-side pairing. Until those are derived, the code exposes completed-function metadata only.

## Source check

This normalization agrees with the standard completed primitive Dirichlet L-function convention recorded by the NIST Digital Library of Mathematical Functions and the Encyclopedia of Mathematics. The repository still requires its own derivation of the finite matrix form rather than treating an external formula as a substitute for proof.
