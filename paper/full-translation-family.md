# The full translated family and the true obstruction set

## Status

This note replaces the incorrect commutator-spanning heuristic with an exact shell decomposition and a Fourier factorization theorem for

\[
f_{rs}(t):=\langle u_r,T_tu_s\rangle.
\]

The result is definitive: for every symmetric finite set of distinct nodes, every nonzero same-parity pair has a nontrivial translated coupling. Equivalently, the family-level obstruction set is empty at every width.

## 1. Raw translated Gaussian

Let

\[
(T_t)_{ij}=\kappa\exp\!\left(-\frac{(x_i-x_j-t)^2}{4\sigma^2}\right),
\]

where \(\kappa\neq0\), \(\sigma>0\), and the nodes \(x_1,\dots,x_N\) are distinct and reflection-symmetric.

For vectors \(u_r,u_s\in\mathbf R^N\), define

\[
f_{rs}(t):=\langle u_r,T_tu_s\rangle.
\]

Expanding the square gives

\[
(T_t)_{ij}
=
\kappa e^{-t^2/(4\sigma^2)}
 e^{-(x_i-x_j)^2/(4\sigma^2)}
 e^{t(x_i-x_j)/(2\sigma^2)}.
\]

Hence

\[
f_{rs}(t)
=
\kappa e^{-t^2/(4\sigma^2)}
\sum_{i,j}
 u_r(i)u_s(j)
 e^{-(x_i-x_j)^2/(4\sigma^2)}
 e^{t(x_i-x_j)/(2\sigma^2)}.
\]

Let

\[
\Delta:=\{x_i-x_j:1\le i,j\le N\}
\]

be the finite difference set, and define the shell coefficient

\[
S_{rs}(d):=
\sum_{x_i-x_j=d}u_r(i)u_s(j),
\qquad d\in\Delta.
\]

Grouping by differences yields the exact identity

\[
\boxed{
 f_{rs}(t)
 =
 \kappa e^{-t^2/(4\sigma^2)}
 \sum_{d\in\Delta}
 e^{-d^2/(4\sigma^2)}
 S_{rs}(d)
 e^{td/(2\sigma^2)}.
}
\tag{1.1}
\]

No factor of \(1/2\) appears: the signed shells partition the ordered pairs \((i,j)\).

## 2. Finite exponential independence

The functions

\[
t\longmapsto e^{td/(2\sigma^2)},\qquad d\in\Delta,
\]

are linearly independent because the exponents are distinct. Therefore:

> **Proposition 2.1.**
> \[
> f_{rs}(t)\equiv0
> \quad\Longleftrightarrow\quad
> S_{rs}(d)=0
> \text{ for every }d\in\Delta.
> \]

Thus full-family vanishing is equivalent to simultaneous cancellation on every displacement shell.

## 3. Parity selection rule

Let \(J\) be reflection on the node set, and suppose

\[
Ju_r=\varepsilon_r u_r,
\qquad
Ju_s=\varepsilon_s u_s,
\qquad
\varepsilon_r,\varepsilon_s\in\{\pm1\}.
\]

Reflecting each ordered pair \((x_i,x_j)\mapsto(-x_i,-x_j)\) gives

\[
\boxed{
S_{rs}(-d)=\varepsilon_r\varepsilon_s S_{rs}(d).
}
\tag{3.1}
\]

Hence:

- if \(u_r,u_s\) have the same parity, then \(S_{rs}\) is even;
- if they have opposite parity, then \(S_{rs}\) is odd.

For same-parity pairs, (1.1) becomes

\[
f_{rs}(t)
=
\kappa e^{-t^2/(4\sigma^2)}
\left[
S_{rs}(0)
+
2\sum_{d>0}
 e^{-d^2/(4\sigma^2)}
 S_{rs}(d)
 \cosh\!\left(\frac{td}{2\sigma^2}\right)
\right].
\]

For opposite-parity pairs, the corresponding symmetrized expression contains \(\sinh\), as expected from the exact parity selection rule.

## 4. Fourier generating function of the shells

Define the finite Fourier sums

\[
\Phi_r(\omega):=\sum_{i=1}^N u_r(i)e^{i\omega x_i},
\qquad
\Phi_s(\omega):=\sum_{j=1}^N u_s(j)e^{i\omega x_j}.
\]

The shell generating function is

\[
G_{rs}(\omega)
:=
\sum_{d\in\Delta}S_{rs}(d)e^{i\omega d}.
\]

By the definition of \(S_{rs}(d)\),

\[
\begin{aligned}
G_{rs}(\omega)
&=
\sum_{i,j}u_r(i)u_s(j)e^{i\omega(x_i-x_j)}\\
&=
\left(\sum_i u_r(i)e^{i\omega x_i}\right)
\left(\sum_j u_s(j)e^{-i\omega x_j}\right).
\end{aligned}
\]

Therefore

\[
\boxed{
G_{rs}(\omega)=\Phi_r(\omega)\Phi_s(-\omega).
}
\tag{4.1}
\]

For real vectors, \(\Phi_s(-\omega)=\overline{\Phi_s(\omega)}\) on the real axis.

If \(u\) is even, then

\[
\Phi_u(\omega)=\sum_i u(i)\cos(\omega x_i)
\]

is real and even. If \(u\) is odd, then

\[
\Phi_u(\omega)=i\sum_i u(i)\sin(\omega x_i)
\]

is purely imaginary and odd. Consequently, for same-parity vectors,

\[
\boxed{
\sum_{d\in\Delta}S_{rs}(d)\cos(\omega d)
=
\begin{cases}
\Phi_r(\omega)\Phi_s(\omega),&\varepsilon_r=\varepsilon_s=+1,\\[4pt]
-\Phi_r(\omega)\Phi_s(\omega),&\varepsilon_r=\varepsilon_s=-1,
\end{cases}
}
\tag{4.2}
\]

where in the odd case the right side is real because both factors are purely imaginary. Equivalently, writing

\[
C_u(\omega):=\sum_i u(i)\cos(\omega x_i),
\qquad
S_u(\omega):=\sum_i u(i)\sin(\omega x_i),
\]

one has

\[
\sum_d S_{rs}(d)\cos(\omega d)
=
\begin{cases}
C_{u_r}(\omega)C_{u_s}(\omega),&\text{even-even},\\
S_{u_r}(\omega)S_{u_s}(\omega),&\text{odd-odd}.
\end{cases}
\tag{4.3}
\]

This is the shell-Fourier factorization.

## 5. A finite exponential sum cannot vanish identically

> **Lemma 5.1.** Let \(x_1,\dots,x_N\) be distinct real numbers. If
> \[
> \sum_{i=1}^N c_i e^{i\omega x_i}\equiv0
> \]
> as an entire function of \(\omega\), then \(c_i=0\) for every \(i\).

**Proof.** Differentiate at \(\omega=0\) for orders \(0,1,\dots,N-1\):

\[
\sum_{i=1}^N c_i(i x_i)^k=0,
\qquad k=0,\dots,N-1.
\]

The coefficient matrix is a Vandermonde matrix in the distinct nodes \(x_i\), hence invertible. Therefore all \(c_i\) vanish. \(\square\)

Thus \(\Phi_u\equiv0\) implies \(u=0\).

## 6. Elimination of the full-family obstruction

> **Theorem 6.1 (Shell-Fourier nonvanishing).** Let \(u_r,u_s\in\mathbf R^N\) be nonzero vectors of the same reflection parity on a symmetric finite set of distinct nodes. Then
> \[
> f_{rs}(t)=\langle u_r,T_tu_s\rangle
> \]
> is not identically zero.

**Proof.** Suppose \(f_{rs}\equiv0\). By Proposition 2.1,

\[
S_{rs}(d)=0
\qquad\forall d\in\Delta.
\]

Hence the shell generating function vanishes identically:

\[
G_{rs}(\omega)=\sum_d S_{rs}(d)e^{i\omega d}\equiv0.
\]

By (4.1),

\[
\Phi_r(\omega)\Phi_s(-\omega)\equiv0.
\]

The functions \(\Phi_r\) and \(\Phi_s(-\cdot)\) are entire. The ring of entire functions has no zero divisors: if their product vanishes identically, one factor must vanish identically. By Lemma 5.1, that factor's coefficient vector is zero. This contradicts the assumption that both vectors are nonzero. Therefore \(f_{rs}\not\equiv0\). \(\square\)

In particular, this applies to every same-parity pair of nonzero eigenvectors of \(T_0\).

Define the true family-level obstruction set

\[
\widetilde Z_N
:=
\left\{
\tau>0:
\langle u_r,T_tu_{r+2}\rangle\equiv0
\text{ in }t
\text{ for some }r
\right\}.
\]

Then:

> **Corollary 6.2.** For every symmetric finite set of distinct nodes,
> \[
> \boxed{\widetilde Z_N=\varnothing.}
> \]

Thus every parity-chain edge appears at some finite even Taylor order, at every width.

## 7. Relation to the second-order exceptional set

The second-order set

\[
Z_N
=
\bigcup_r\{\tau:g_r(\tau)=0\}
\]

can be nonempty. The five-node family

\[
\{-a,-b,0,b,a\},\qquad a>3b,
\]

provides an explicit example.

But Corollary 6.2 shows that such zeros are only cancellations in a particular Taylor coefficient. They are never genuine obstructions for the full translated family.

Equivalently, if

\[
\langle u_r,T_0''u_{r+2}\rangle=0,
\]

then there exists some \(m\ge2\) such that

\[
\langle u_r,T_0^{(2m)}u_{r+2}\rangle\neq0.
\]

The theorem is qualitative: it guarantees a finite recovery order but does not yet bound the smallest such \(m\).

## 8. Five-node worked certificate

For

\[
\{-a,-b,0,b,a\},\qquad a>b>0,
\]

let the two normalized odd-block eigenvectors be

\[
y_+=(p,q),\qquad y_-=(-q,p).
\]

At the shell \(d=a+b\), only \((a,-b)\) and \((b,-a)\) contribute, and

\[
S_{+-}(a+b)=q^2-p^2.
\]

If this vanished, the symmetric odd block would have equal diagonal entries. But

\[
A(v)-D(v)=e^{-2b^2v}-e^{-2a^2v}>0
\]

for every \(v>0\). Hence

\[
S_{+-}(a+b)\neq0
\]

at every width.

For the explicit exceptional width associated with

\[
\{-3,-0.7,0,0.7,3\},
\]

the second-order coefficient vanishes while the shell certificate remains nonzero; numerically,

\[
S_{13}(3.7)\approx0.376.
\]

This is the local, single-shell face of the global factorization theorem.

## 9. Consequence for local two-shift generation

The parity-chain argument no longer requires exclusion of a width set. For each adjacent same-parity pair \((u_r,u_{r+2})\), Theorem 6.1 gives an even integer \(2m_r\) such that

\[
\langle u_r,T_0^{(2m_r)}u_{r+2}\rangle\neq0.
\]

Since the algebra generated by \(T_0\) and \(T_t\) for all sufficiently small \(t\) contains the Taylor coefficients of the analytic family, every adjacent parity edge is present. With simple spectrum in each parity block, the standard chain-generation argument yields

\[
M_{N_+}(\mathbf C)\oplus M_{N_-}(\mathbf C).
\]

Therefore the local translated-family generation theorem holds for every width and every symmetric configuration of distinct nodes.

A separate formulation may still be needed if the theorem is required for one fixed nonzero shift \(t\), rather than for the local analytic family or for all sufficiently small shifts. The present result removes the width obstruction at the family level.

## 10. Conclusion

The infinite Hermite tower and the repeated-difference shell problem are two descriptions of the same finite object.

The shell decomposition is the local \(t\)-side description:

\[
f_{rs}\equiv0
\iff
S_{rs}(d)=0\quad\forall d.
\]

The Fourier factorization is the global \(\omega\)-side description:

\[
\sum_d S_{rs}(d)e^{i\omega d}
=
\Phi_r(\omega)\Phi_s(-\omega).
\]

Because nonzero finite exponential sums cannot vanish identically, simultaneous shell cancellation is impossible. Hence

\[
\boxed{\widetilde Z_N=\varnothing}
\]

for all symmetric finite sets of distinct nodes.