# Fourier and translation convention

This document freezes the transform convention used by the packet and prime-term code.

## Transform pair

For an integrable function `f` on the real line, define

```text
f_hat(u) = integral_R f(x) exp(-i u x) dx,
```

with inverse

```text
f(x) = (1 / 2 pi) integral_R f_hat(u) exp(i u x) du.
```

No hidden `2 pi` is placed in the frequency variable.

## Translation

For `tau_a f(x) = f(x - a)`,

```text
widehat(tau_a f)(u) = exp(-i u a) f_hat(u).
```

The packet correlation matrix already implemented as

```text
C(a)_{ij} = <g_i, g_j(. - a)>
```

therefore corresponds to this translation direction. The universal symmetric prime matrix is

```text
T_n = -(C(log n) + C(-log n)).
```

## Constant multiplication forms

A constant contribution `c` to a sesquilinear form acts on the packet span as

```text
(f, g) -> c <f, g>.
```

Its coordinate matrix is therefore exactly `c B`, where `B` is the packet Gram matrix. The implementation is `finite_weil.gram.scalar_form_matrix`.

## Boundary of the current claim

This convention determines translation phases and the matrix representation of constant forms. It does not by itself determine whether a completed-L prefactor enters the final Weil form with coefficient `log(q/pi)`, one half of that value, or another globally rescaled coefficient. That coefficient must be derived from the exact explicit-formula identity adopted by the project.

Until that derivation is committed, the code will not label any scalar Gram contribution as the final conductor matrix.
