# The Shell-Fourier Factorization Theorem

## Status

This note gives the publication-form proof of the family-level nonvanishing theorem needed to resolve Issue #10. The proof is organized around the complex shell generating function, which avoids the unnecessary cosine-independence detour in the core implication.

## 0. Hypotheses and conventions

Let

\[
x_1<\cdots<x_N\in\mathbf R
\]

be distinct nodes. For the parity corollaries, assume the node set is symmetric under \(x\mapsto -x\). Let \(\sigma>0\). Define the paired translated Gaussian family

\[
T_t(i,j)
=
-\sigma\sqrt\pi
\left[
 e^{-(x_i-x_j-t)^2/(4\sigma^2)}
+
 e^{-(x_i-x_j+t)^2/(4\sigma^2)}
\right].
\]

Let

\[
\Delta:=\{x_i-x_j:1\le i,j\le N\}
\]

be the finite signed difference set. For real vectors \(u,w\in\mathbf R^N\), define

\[
S_{u,w}(d)
:=
\sum_{x_i-x_j=d}u(i)w(j),
\qquad d\in\Delta,
\]

and

\[
f_{u,w}(t):=\langle u,T_tw\rangle.
\]

No eigenvector hypothesis is used until Section 5.

## 1. Exact shell decomposition

For each ordered pair with difference \(d=x_i-x_j\),

\[
e^{-(d\mp t)^2/(4\sigma^2)}
=
e^{-d^2/(4\sigma^2)}
e^{-t^2/(4\sigma^2)}
e^{\pm td/(2\sigma^2)}.
\]

Grouping the double sum by difference shells gives

\[
\boxed{
 f_{u,w}(t)
 =
 -\sigma\sqrt\pi\,e^{-t^2/(4\sigma^2)}
 \sum_{d\in\Delta}
 e^{-d^2/(4\sigma^2)}S_{u,w}(d)
 \left(e^{td/(2\sigma^2)}+e^{-td/(2\sigma^2)}\right).
}
\tag{1.1}
\]

The signed shells partition the ordered pairs, so no factor \(1/2\) appears.

## 2. Parity identity

Assume now that the node set is symmetric. Let \(R\) be the reflection permutation, so \(x_{\bar i}=-x_i\). If

\[
u(\bar i)=\varepsilon_u u(i),
\qquad
w(\bar i)=\varepsilon_w w(i),
\qquad
\varepsilon_u,\varepsilon_w\in\{\pm1\},
\]

then

\[
\boxed{
S_{u,w}(-d)=\varepsilon_u\varepsilon_w S_{u,w}(d).
}
\tag{2.1}
\]

Indeed, \((i,j)\mapsto(\bar i,\bar j)\) maps the shell \(d\) bijectively to the shell \(-d\), and multiplies each summand by \(\varepsilon_u\varepsilon_w\).

Hence opposite-parity vectors satisfy

\[
f_{u,w}(t)\equiv0,
\]

while for equal parity the coefficient of \(e^{td/(2\sigma^2)}\) in (1.1) is

\[
2e^{-d^2/(4\sigma^2)}S_{u,w}(d).
\]

## 3. Independence of finite exponential families

### Lemma 3.1

Let \(\mu_1,\ldots,\mu_M\in\mathbf C\) be distinct. If

\[
\sum_{m=1}^M c_me^{\mu_m t}=0
\]

for all \(t\) in a set with an accumulation point, then \(c_m=0\) for every \(m\).

### Proof

The exponential sum is entire, hence vanishes identically. Evaluating its first \(M\) derivatives at \(t=0\) gives

\[
\sum_{m=1}^M c_m\mu_m^k=0,
\qquad k=0,\ldots,M-1.
\]

The coefficient matrix is Vandermonde on the distinct \(\mu_m\), hence invertible. Therefore all \(c_m\) vanish. \(\square\)

For equal-parity vectors, (1.1), (2.1), and Lemma 3.1 imply

\[
\boxed{
 f_{u,w}(t)\equiv0
 \iff
 S_{u,w}(d)=0
 \text{ for every }d\in\Delta.
}
\tag{3.1}
\]

## 4. Complex shell generating function

Define the finite exponential profiles

\[
\Phi_u(z):=\sum_{i=1}^N u(i)e^{zx_i},
\qquad
\Phi_w(z):=\sum_{j=1}^N w(j)e^{zx_j}.
\]

Also define the shell generating function

\[
G_{u,w}(z):=\sum_{d\in\Delta}S_{u,w}(d)e^{zd}.
\]

Then

\[
\begin{aligned}
G_{u,w}(z)
&=
\sum_{i,j}u(i)w(j)e^{z(x_i-x_j)}\\
&=
\left(\sum_i u(i)e^{zx_i}\right)
\left(\sum_j w(j)e^{-zx_j}\right).
\end{aligned}
\]

Therefore

\[
\boxed{
G_{u,w}(z)=\Phi_u(z)\Phi_w(-z).
}
\tag{4.1}
\]

This identity is purely finite-dimensional and does not use parity or the Gaussian.

### Theorem 4.1 - Shell-Fourier factorization

For arbitrary real or complex vectors \(u,w\) on distinct real nodes, the following are equivalent:

1. \(S_{u,w}(d)=0\) for every \(d\in\Delta\);
2. \(G_{u,w}(z)\equiv0\) as an entire function;
3. \(u=0\) or \(w=0\).

### Proof

The equivalence of (1) and (2) follows from Lemma 3.1 applied to the distinct exponents \(d\in\Delta\).

Assume (2). By (4.1),

\[
\Phi_u(z)\Phi_w(-z)\equiv0.
\]

The ring of entire functions is an integral domain, so

\[
\Phi_u\equiv0
\qquad\text{or}\qquad
\Phi_w\equiv0.
\]

Suppose \(\Phi_u\equiv0\). Applying Lemma 3.1 to the distinct exponents \(x_1,\ldots,x_N\) gives

\[
u(1)=\cdots=u(N)=0.
\]

Thus \(u=0\). The same argument applies to \(w\). Conversely, if \(u=0\) or \(w=0\), then every shell sum vanishes. \(\square\)

Combining (3.1) with Theorem 4.1 yields the main conclusion.

### Corollary 4.2 - Full family nonvanishing

Let the node set be symmetric, and let \(u,w\neq0\) have equal parity. Then

\[
\boxed{
\langle u,T_tw\rangle\not\equiv0.
}
\tag{4.2}
\]

Thus the only identically vanishing matrix elements of the paired family are the parity-forbidden ones.

### Real Fourier form

Setting \(z=i\omega\) gives

\[
\sum_{d\in\Delta}S_{u,w}(d)e^{i\omega d}
=
\Phi_u(i\omega)\Phi_w(-i\omega).
\]

For equal-parity real vectors, this reduces to the profile product

\[
\sum_{d\in\Delta}S_{u,w}(d)\cos(\omega d)
=
\phi_u(\omega)\phi_w(\omega),
\]

where

\[
\phi_u(\omega)
=
\begin{cases}
\sum_i u(i)\cos(\omega x_i),&u\text{ even},\\
\sum_i u(i)\sin(\omega x_i),&u\text{ odd}.
\end{cases}
\]

This is the real parity presentation of the complex factorization, not a separate ingredient in the proof.

## 5. Eigenvector corollaries

Let \(u_0,\ldots,u_{N-1}\) be an orthonormal eigenbasis of \(T_0\). For a symmetric distinct node set, strict total positivity gives simple spectrum, so the eigenvectors may be chosen with definite parity.

### Corollary 5.1 - Emptiness of the true obstruction set

For every width \(\tau=\sigma^2>0\), every same-parity pair \(r\neq s\) satisfies

\[
\langle u_r,T_tu_s\rangle\not\equiv0.
\]

Therefore

\[
\boxed{
\widetilde Z_N=\varnothing.
}
\]

### Corollary 5.2 - Local generation at every width

Fix \(\tau>0\). For each same-parity pair \(r\neq s\), the function

\[
f_{rs}(t)=\langle u_r,T_tu_s\rangle
\]

is entire, satisfies \(f_{rs}(0)=0\), and is not identically zero by Corollary 5.1. Hence its zero at \(t=0\) is isolated. Because there are finitely many same-parity pairs, there exists \(\varepsilon(\tau)>0\) such that

\[
f_{rs}(t)\neq0
\]

for every same-parity pair and every \(0<|t|<\varepsilon(\tau)\).

Thus the graph of \(T_t\) in the \(T_0\)-eigenbasis is complete on each parity block. By the graph criterion and bicommutant theorem,

\[
\operatorname{Comm}(T_0,T_t)=\operatorname{span}\{I,J\},
\]

and

\[
\operatorname{alg}^*(T_0,T_t)
=
M_{N_+}(\mathbf C)\oplus M_{N_-}(\mathbf C)
\]

for all sufficiently small nonzero \(t\).

No width is exceptional for the full translated family. The set \(Z_N\) detected by the second derivative records only failure of the order-\(t^2\) certificate.

### Corollary 5.3 - Discreteness in the shift

For fixed \(\tau\), generation can fail only when at least one same-parity coupling \(f_{rs}(t)\) vanishes. Since each \(f_{rs}\) is a nonzero entire function, each zero set is discrete. A finite union of such sets is discrete.

## 6. Five-node example

For the family

\[
\{-a,-b,0,b,a\},
\qquad a>b>0,
\]

Section 6 of `paper/full-translation-family.md` gives an explicit nonzero shell certificate in the odd block:

\[
S_{+-}(a+b)=q^2-p^2\neq0.
\]

The present theorem shows that this local shell witness is one instance of a universal fact: simultaneous cancellation of all shells is impossible for any pair of nonzero vectors.

## 7. Sharpness and scope

- Distinct nodes are essential for the Vandermonde step proving injectivity of \(u\mapsto\Phi_u\).
- Symmetry is needed only to identify the parity-forbidden and parity-allowed sectors of the paired family.
- The shell factorization (4.1) itself is independent of symmetry and independent of the Gaussian.
- The Gaussian is used only to turn the paired translation matrix element into a finite exponential family in \(t\).

## 8. Conclusion

The infinite Hermite tower and the finite shell system are two presentations of the same obstruction. The shell generating function factorizes as a product of finite exponential profiles, and finite exponential profiles have no nontrivial zero divisors. Therefore no nonzero same-parity pair can be annihilated identically by the paired translated Gaussian family.

This removes the width exception from the local generation theorem and resolves the family-level obstruction problem in Issue #10.
