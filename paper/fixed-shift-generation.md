# A quantitative fixed-shift corollary

## Status

This note supplies the remaining quantitative step after the Shell-Fourier Factorization Theorem. The qualitative result gives, for each fixed width, a punctured neighborhood of the origin on which every same-parity matrix element is nonzero. Here we record an explicit tail estimate that produces a common admissible shift interval from the first nonzero Taylor coefficient of each coupling.

## 1. Setup

Let

\[
T_t(i,j)
=
-\sigma\sqrt\pi
\left[
 e^{-(x_i-x_j-t)^2/(4\sigma^2)}
+
 e^{-(x_i-x_j+t)^2/(4\sigma^2)}
\right]
\]

on a symmetric set of distinct real nodes. Fix \(\tau=\sigma^2>0\), and let \(u_r,u_s\) be distinct same-parity eigenvectors of \(T_0\). Define

\[
f_{rs}(t):=\langle u_r,T_tu_s\rangle.
\]

By the Shell-Fourier Factorization Theorem,

\[
f_{rs}\not\equiv0.
\]

Since the paired family is even in \(t\), there is a least integer \(m_{rs}\ge1\) such that

\[
a_{rs}
:=
\frac{f_{rs}^{(2m_{rs})}(0)}{(2m_{rs})!}
\neq0.
\]

Thus

\[
f_{rs}(t)=a_{rs}t^{2m_{rs}}+R_{rs}(t).
\]

## 2. Exact finite-exponential form

For the shell sums

\[
S_{rs}(d)
=
\sum_{x_i-x_j=d}u_r(i)u_s(j),
\]

set

\[
b_d
:=
-2\sigma\sqrt\pi\,e^{-d^2/(4\sigma^2)}S_{rs}(d).
\]

Equal parity gives \(S_{rs}(-d)=S_{rs}(d)\), hence

\[
f_{rs}(t)
=
e^{-t^2/(4\sigma^2)}
\sum_{d\in\Delta} b_d e^{td/(2\sigma^2)}.
\tag{2.1}
\]

Write

\[
D:=\max_{d\in\Delta}|d|
\]

and

\[
B_{rs}:=\sum_{d\in\Delta}|b_d|.
\]

Then for complex \(z\),

\[
|f_{rs}(z)|
\le
B_{rs}
\exp\!\left(
\frac{|z|^2}{4\sigma^2}
+
\frac{D|z|}{2\sigma^2}
\right).
\tag{2.2}
\]

## 3. Cauchy estimate for the Taylor tail

Fix \(\rho>0\). Let

\[
M_{rs}(\rho)
:=
B_{rs}
\exp\!\left(
\frac{\rho^2}{4\sigma^2}
+
\frac{D\rho}{2\sigma^2}
\right).
\]

By Cauchy's estimate, if

\[
f_{rs}(t)=\sum_{k=0}^{\infty}c_k t^k,
\]

then

\[
|c_k|\le \frac{M_{rs}(\rho)}{\rho^k}.
\]

Because \(c_k=0\) for odd \(k\) and for \(k<2m_{rs}\), the tail satisfies, whenever \(|t|<\rho\),

\[
\begin{aligned}
|R_{rs}(t)|
&\le
\sum_{k=2m_{rs}+1}^{\infty}|c_k||t|^k\\
&\le
M_{rs}(\rho)
\sum_{k=2m_{rs}+1}^{\infty}
\left(\frac{|t|}{\rho}\right)^k\\
&=
M_{rs}(\rho)
\frac{(|t|/\rho)^{2m_{rs}+1}}{1-|t|/\rho}.
\end{aligned}
\tag{3.1}
\]

A parity-refined version starts the sum at \(2m_{rs}+2\), but (3.1) is already sufficient.

## 4. An explicit nonvanishing radius

Choose \(0<\delta_{rs}<\rho\) such that

\[
M_{rs}(\rho)
\frac{(\delta_{rs}/\rho)^{2m_{rs}+1}}{1-\delta_{rs}/\rho}
\le
\frac{|a_{rs}|}{2}\,\delta_{rs}^{2m_{rs}}.
\tag{4.1}
\]

Equivalently, it is enough that

\[
\frac{M_{rs}(\rho)}{\rho^{2m_{rs}+1}}
\frac{\delta_{rs}}{1-\delta_{rs}/\rho}
\le
\frac{|a_{rs}|}{2}.
\tag{4.2}
\]

For example, imposing \(\delta_{rs}\le\rho/2\), the simpler sufficient condition

\[
\delta_{rs}
\le
\frac{|a_{rs}|\rho^{2m_{rs}+1}}{4M_{rs}(\rho)}
\tag{4.3}
\]

works. Thus one may take

\[
\boxed{
\delta_{rs}(\rho)
:=
\min\!\left\{
\frac{\rho}{2},
\frac{|a_{rs}|\rho^{2m_{rs}+1}}{4M_{rs}(\rho)}
\right\}.
}
\tag{4.4}
\]

Then, for every \(0<|t|<\delta_{rs}(\rho)\),

\[
\begin{aligned}
|f_{rs}(t)|
&\ge
|a_{rs}|\,|t|^{2m_{rs}}-|R_{rs}(t)|\\
&\ge
\frac{|a_{rs}|}{2}|t|^{2m_{rs}}>0.
\end{aligned}
\tag{4.5}
\]

## 5. Common shift interval

There are finitely many distinct same-parity pairs. Define

\[
\delta(\tau;\rho)
:=
\min_{\substack{r<s\\ \varepsilon_r=\varepsilon_s}}
\delta_{rs}(\rho).
\]

Each \(\delta_{rs}(\rho)\) is positive, hence

\[
\delta(\tau;\rho)>0.
\]

Therefore every same-parity coupling is nonzero for every

\[
0<|t|<\delta(\tau;\rho).
\]

The graph of \(T_t\) in the \(T_0\)-eigenbasis is consequently complete on each parity sector. By the graph criterion and the bicommutant theorem,

\[
\operatorname{Comm}(T_0,T_t)=\operatorname{span}\{I,J\}
\]

and

\[
\operatorname{alg}^*(T_0,T_t)
=
M_{N_+}(\mathbf C)\oplus M_{N_-}(\mathbf C)
\]

throughout the same punctured interval.

## 6. Theorem

> **Quantitative fixed-shift theorem.** Fix a symmetric finite set of distinct nodes and a width \(\tau=\sigma^2>0\). For every same-parity pair \((r,s)\), let \(2m_{rs}\) be the first nonzero Taylor order of \(f_{rs}(t)=\langle u_r,T_tu_s\rangle\), and define \(a_{rs}\), \(B_{rs}\), \(D\), \(M_{rs}(\rho)\), and \(\delta_{rs}(\rho)\) as above. Then
> \[
> \delta(\tau;\rho)
> =
> \min_{r<s,\,\varepsilon_r=\varepsilon_s}\delta_{rs}(\rho)
> >0,
> \]
> and every fixed shift satisfying
> \[
> 0<|t|<\delta(\tau;\rho)
> \]
> generates the full parity-preserving algebra together with \(T_0\).

This strengthens the qualitative isolated-zero argument by supplying an explicit common lower bound in terms of the first nonzero Taylor coefficient and a finite shell norm.

## 7. Scope

The theorem is quantitative for each fixed width. It does not claim a width-uniform radius on an unbounded interval of \(\tau\). A uniform theorem over a compact width range would require lower bounds for the leading coefficients \(|a_{rs}(\tau)|\) and upper bounds for the shell norms that remain uniform over that range.
