# Conductor contribution to the finite Weil form

## Fixed conventions

Let `chi` be a primitive quadratic Dirichlet character of conductor `q` and
parity `a` in `{0, 1}`. The completed function is

```text
Lambda(s, chi)
    = (q / pi)^((s + a) / 2)
      Gamma((s + a) / 2)
      L(s, chi).
```

For packet-space functions `f` and `g`, use

```text
f_hat(t) = integral_R f(x) exp(-i t x) dx
```

and set the spectral test function

```text
h(t) = f_hat(t) conjugate(g_hat(t)).
```

Parseval's identity in this convention is

```text
(1 / 2 pi) integral_R h(t) dt = <f, g>.
```

## Proposition

Under the symmetric explicit-formula normalization used by this project, the
completed-function power prefactor contributes

```text
log(q / pi) <f, g>
```

to the Weil sesquilinear form. Therefore, on a packet basis with Gram matrix
`B`, its coordinate matrix is

```text
A_cond = log(q / pi) B.
```

## Derivation

The logarithmic derivative of the prefactor on one side of the functional
equation is

```text
d/ds [((s + a) / 2) log(q / pi)]
    = (1 / 2) log(q / pi).
```

The symmetric contour argument includes the corresponding term from both sides
of the functional equation. These two equal constant contributions add to

```text
log(q / pi).
```

Consequently the conductor part of the spectral explicit formula is

```text
(1 / 2 pi) integral_R h(t) log(q / pi) dt.
```

Applying Parseval gives

```text
log(q / pi) <f, g>.
```

If `g_1, ..., g_m` is the packet basis and

```text
B_ij = <g_i, g_j>,
```

then

```text
(A_cond)_ij = log(q / pi) B_ij.
```

This is implemented by `finite_weil.completed.conductor_matrix`.

## Independent numerical check

For the Gaussian packet

```text
g_j(x) = exp(-(x - t_j)^2 / (2 sigma^2)),
```

its Fourier transform is

```text
g_j_hat(u)
    = sqrt(2 pi) sigma exp(-sigma^2 u^2 / 2) exp(-i u t_j).
```

The tests numerically integrate

```text
(log(q / pi) / 2 pi)
    integral_R g_i_hat(u) conjugate(g_j_hat(u)) du
```

and compare the result against the analytic matrix entry

```text
log(q / pi) sqrt(pi) sigma
    exp(-(t_i - t_j)^2 / (4 sigma^2)).
```

The quadrature is independent of the packet-space Gram implementation.

## Scope

This proposition fixes only the power-prefactor contribution. The gamma-factor
matrix remains a separate derivation. No claim about the complete finite Weil
operator is made until the gamma and prime terms are assembled under the same
normalization.
