# Variational foundation of the finite packet problem

## 1. Purpose and claim boundary

This note isolates the part of the finite Weil construction that can be proved
without assuming that an infinite-dimensional Weil operator has already been
defined.

The result is abstract. It applies to any finite packet space on which the
candidate Weil form is represented by a real symmetric matrix. In particular,
it explains exactly what the generalized eigenproblem

\[
A c = \lambda B c
\]

means and what it does not mean.

The note proves the following finite-dimensional facts:

1. the matrix pencil \((A,B)\) is the coordinate representation of a Rayleigh
   quotient on the packet space;
2. its generalized eigenvalues are the stationary values of that quotient;
3. its smallest generalized eigenvalue is the exact minimum of the quotient on
   the chosen finite space;
4. nested finite spaces obey the usual Rayleigh-Ritz monotonicity;
5. a zero coordinate residual proves stationarity only inside the finite trial
   space;
6. Gram truncation changes the trial space and must be recorded as part of the
   approximation.

This note does **not** prove that the full conductor-gamma-prime form is densely
defined, semibounded, closable, or represented by a self-adjoint operator on
\(L^2(\mathbb R)\). Those are separate questions.

## 2. Abstract setting

Let \(H\) be a real Hilbert space with inner product
\(\langle\cdot,\cdot\rangle_H\). Let

\[
V=\operatorname{span}\{g_1,\ldots,g_m\}\subset H,
\]

where \(g_1,\ldots,g_m\) are linearly independent. Let

\[
Q:V\times V\longrightarrow \mathbb R
\]

be a symmetric bilinear form:

\[
Q(f,g)=Q(g,f).
\]

Define the Gram and form matrices by

\[
B_{ij}=\langle g_i,g_j\rangle_H,
\qquad
A_{ij}=Q(g_i,g_j).
\]

For \(c=(c_1,\ldots,c_m)^T\in\mathbb R^m\), write

\[
f_c=\sum_{j=1}^m c_j g_j.
\]

Linearity gives the two coordinate identities

\[
\|f_c\|_H^2=c^T Bc,
\qquad
Q(f_c,f_c)=c^T Ac.
\]

Because the packets are linearly independent,

\[
c^T Bc=\|f_c\|_H^2>0
\]

for every nonzero \(c\). Thus \(B\) is symmetric positive definite.

## 3. The packet Rayleigh quotient

For nonzero \(f\in V\), define

\[
\mathcal R_V(f)=\frac{Q(f,f)}{\|f\|_H^2}.
\]

In packet coordinates,

\[
\mathcal R_V(f_c)=\frac{c^T Ac}{c^T Bc}.
\]

This equality is the precise bridge between the quadratic form and the matrix
pencil. It contains no approximation: once \(A_{ij}=Q(g_i,g_j)\) and
\(B_{ij}=\langle g_i,g_j\rangle_H\), the matrix quotient is exactly the form
quotient restricted to \(V\).

## 4. Variational theorem

### Theorem 4.1 - Generalized eigenvalues are stationary Rayleigh values

Let \(V\), \(Q\), \(A\), and \(B\) be as above. Then:

1. a nonzero vector \(c\) is a stationary point of
   \(c\mapsto c^T Ac\) subject to \(c^T Bc=1\) if and only if

   \[
   Ac=\lambda Bc
   \]

   for some real \(\lambda\);

2. at such a point,

   \[
   \lambda=\frac{c^T Ac}{c^T Bc}=\mathcal R_V(f_c);
   \]

3. all generalized eigenvalues are real, and there is a basis of generalized
   eigenvectors that is orthonormal for the \(B\)-inner product

   \[
   \langle c,d\rangle_B=c^T Bd;
   \]

4. if

   \[
   \lambda_1\le\lambda_2\le\cdots\le\lambda_m
   \]

   are the generalized eigenvalues, then

   \[
   \lambda_1
   =
   \min_{0\ne f\in V}\mathcal R_V(f)
   =
   \min_{c^T Bc=1} c^T Ac.
   \]

#### Proof

Since \(B\) is positive definite, the constraint set

\[
S_B=\{c\in\mathbb R^m:c^T Bc=1\}
\]

is compact. Therefore the continuous function \(c\mapsto c^T Ac\) attains a
minimum and a maximum on \(S_B\).

Introduce the Lagrangian

\[
L(c,\lambda)=c^T Ac-\lambda(c^T Bc-1).
\]

Because \(A\) and \(B\) are symmetric,

\[
\nabla_c L=2Ac-2\lambda Bc.
\]

Thus the constrained stationary-point equation is exactly

\[
Ac=\lambda Bc.
\]

Multiplying on the left by \(c^T\) gives

\[
c^T Ac=\lambda c^T Bc.
\]

For a normalized vector \(c^T Bc=1\), this yields

\[
\lambda=c^T Ac.
\]

For arbitrary nonzero \(c\), it yields

\[
\lambda=\frac{c^T Ac}{c^T Bc}.
\]

To obtain the spectral statement, let \(B^{1/2}\) denote the positive square
root of \(B\) and set

\[
M=B^{-1/2}AB^{-1/2}.
\]

The matrix \(M\) is real symmetric. Hence it has real eigenvalues and an
orthonormal eigenbasis. The substitution

\[
y=B^{1/2}c
\]

transforms

\[
Ac=\lambda Bc
\]

into

\[
My=\lambda y.
\]

It also transforms the Rayleigh quotient into

\[
\frac{c^T Ac}{c^T Bc}
=
\frac{y^T My}{y^T y}.
\]

The ordinary Rayleigh-Ritz theorem for the symmetric matrix \(M\) therefore
implies

\[
\lambda_1
=
\min_{y\ne0}\frac{y^T My}{y^T y}
=
\min_{c\ne0}\frac{c^T Ac}{c^T Bc}.
\]

Mapping the eigenvectors of \(M\) back by \(c=B^{-1/2}y\) gives a generalized
eigenbasis satisfying

\[
c_i^T Bc_j=\delta_{ij}.
\]

This proves all four claims. \(\square\)

## 5. Min-max principle

The same change of coordinates gives the full Courant-Fischer characterization.
For \(1\le k\le m\),

\[
\lambda_k
=
\min_{\substack{S\subset V\\ \dim S=k}}
\max_{0\ne f\in S}
\frac{Q(f,f)}{\|f\|_H^2}.
\]

Equivalently,

\[
\lambda_k
=
\max_{\substack{S\subset V\\ \dim S=m-k+1}}
\min_{0\ne f\in S}
\frac{Q(f,f)}{\|f\|_H^2}.
\]

This identifies every generalized eigenvalue as an intrinsic quantity of the
pair \((Q|_V,\langle\cdot,\cdot\rangle_H|_V)\), independent of the chosen basis
of \(V\).

## 6. Basis invariance

Let \(S\in GL_m(\mathbb R)\) be a change-of-basis matrix. In the new basis,

\[
A'=S^TAS,
\qquad
B'=S^TBS.
\]

Then

\[
\det(A'-\lambda B')
=
\det(S)^2\det(A-\lambda B).
\]

Therefore the generalized eigenvalues are unchanged. The packet coefficients
change, but the represented function \(f\in V\), its Rayleigh quotient, and the
spectrum of the restricted form do not.

This is why Gram whitening is legitimate when it is an invertible coordinate
change on the whole packet space.

## 7. Nested-space monotonicity

### Proposition 7.1

Let \(V\subset W\subset H\), and suppose the same symmetric form \(Q\) is finite
on both spaces. Let

\[
\lambda_1(V)=\min_{0\ne f\in V}\frac{Q(f,f)}{\|f\|_H^2},
\]

and define \(\lambda_1(W)\) similarly. Then

\[
\lambda_1(W)\le\lambda_1(V).
\]

#### Proof

The minimization set for \(W\) contains the minimization set for \(V\). Hence
its infimum cannot be larger. \(\square\)

This simple fact is important for refinement studies. If the trial spaces are
truly nested and the matrix entries come from one fixed form \(Q\), the lowest
Ritz value can only move downward. Nonmonotone behavior means that at least one
of the following has changed:

- the spaces are not nested;
- the form itself changed, for example through a different prime cutoff;
- numerical truncation changed the effective space;
- the matrices are not exact restrictions of one common form.

Thus monotonicity is a diagnostic, not yet a convergence theorem.

## 8. What the finite residual proves

Suppose \((\lambda,c)\) satisfies

\[
Ac=\lambda Bc.
\]

For every \(d\in\mathbb R^m\), with

\[
h_d=\sum_j d_jg_j,
\]

we have

\[
d^T(Ac-\lambda Bc)=0.
\]

Using the coordinate identities, this is

\[
Q(h_d,f_c)-\lambda\langle h_d,f_c\rangle_H=0
\qquad
\text{for every }h_d\in V.
\]

Therefore a generalized eigenvector satisfies the weak eigenvalue equation
**against all test vectors in the finite trial space**.

This is the exact meaning of a zero coordinate residual.

It does not imply

\[
Q(h,f_c)-\lambda\langle h,f_c\rangle_H=0
\]

for every \(h\) in an infinite-dimensional form domain. Consequently, a small
finite residual is evidence of an accurately solved finite Ritz problem, not by
itself evidence of convergence to an eigenfunction of a limit operator.

## 9. Linearly dependent or nearly dependent packets

If the packet family is linearly dependent, then \(B\) is only positive
semidefinite. The coefficient vector is no longer a unique representation of a
function in \(V\), and the pencil \((A,B)\) must be reduced to the quotient by
\(\ker B\), or equivalently to an independent basis of \(V\).

Numerically, nearly dependent packets produce very small eigenvalues of \(B\).
If an eigenspace of \(B\) below a tolerance is discarded, the resulting problem
is the Rayleigh-Ritz problem on a smaller space

\[
V_\tau\subsetneq V.
\]

It is not merely a more stable computation of the original \(V\)-problem.
Accordingly, every whitened experiment must record at least

- the tolerance;
- the retained rank;
- the discarded Gram spectrum, or enough information to reconstruct it.

Comparisons across different retained ranks compare different trial spaces.

## 10. Application to the finite Weil matrices

For the current project, the intended finite form is decomposed as

\[
Q_{\chi,N}
=
Q_{\mathrm{cond},\chi}
+
Q_{\Gamma,\chi}
+
Q_{\mathrm{prime},\chi,N},
\]

where \(N\) is the finite prime cutoff or regularization scale. For a packet
family \(g_1,\ldots,g_m\), the assembled matrix must satisfy

\[
(A_{\chi,N})_{ij}=Q_{\chi,N}(g_i,g_j),
\qquad
B_{ij}=\langle g_i,g_j\rangle_{L^2}.
\]

Once these identities are verified term by term, Theorem 4.1 proves that the
smallest generalized eigenvalue is exactly

\[
\lambda_1(V;N)
=
\min_{0\ne f\in V}
\frac{Q_{\chi,N}(f,f)}{\|f\|_2^2}.
\]

The notation must retain both \(V\) and \(N\). Changing the packet space and
changing the prime cutoff are mathematically different operations.

## 11. What remains open before an infinite-dimensional operator can be claimed

The finite-dimensional theorem does not require a global operator. Passing to a
limit does.

A rigorous infinite-dimensional theory must answer the following questions in
this order.

### 11.1 Common domain

Find a dense vector space \(\mathcal D\subset L^2(\mathbb R)\) on which all
three contributions are simultaneously finite and sesquilinear or bilinear.

The current finite Gaussian calculations do not by themselves identify such a
maximal or natural domain.

### 11.2 Untruncated prime term

The finite prime contribution is well defined for every cutoff \(N\). An
untruncated series requires a separate convergence theorem. Convergence on each
finite Gaussian packet space does not automatically imply convergence on a
dense function class, nor does it identify the correct topology of convergence.

A mathematically derived test-function class or tail decomposition is needed.

### 11.3 Semiboundedness

To use the standard representation theorem for closed quadratic forms, one
usually needs a lower bound

\[
Q(f,f)\ge -C\|f\|_2^2
\qquad(f\in\mathcal D).
\]

No such global estimate has yet been proved for the assembled form in this
repository. Finite matrices always have a finite smallest eigenvalue; that fact
says nothing about uniform semiboundedness as the trial space grows.

### 11.4 Closability

A densely defined form \(Q\) is closable only if every sequence
\(f_n\in\mathcal D\) satisfying

\[
f_n\to0\text{ in }L^2,
\qquad
Q(f_n-f_m,f_n-f_m)\to0
\]

also satisfies

\[
Q(f_n,f_n)\to0.
\]

No finite-dimensional calculation can establish this condition by itself.

### 11.5 Self-adjoint representation

Only after a densely defined, closed, semibounded form has been obtained may one
invoke the quadratic-form representation theorem to produce a self-adjoint
operator \(\mathcal W\) satisfying

\[
Q(f,g)=\langle f,\mathcal W g\rangle
\]

on the appropriate operator domain.

Until those hypotheses are proved, \(\mathcal W\) should be described as a
candidate limit operator, not an established object.

## 12. Consequences for the research program

The next mathematical tasks are now sharply separated.

1. **Finite audit.** Verify, contribution by contribution, that every implemented
   matrix entry is exactly the value of a stated finite bilinear form on the
   packet pair.
2. **Admissible domain.** Choose a dense test-function class on which the
   untruncated conductor, gamma, and prime expressions are simultaneously
   meaningful.
3. **Uniform estimates.** Seek bounds independent of packet dimension and prime
   cutoff.
4. **Form convergence.** Only after the preceding steps should one formulate
   Mosco convergence, strong resolvent convergence, or another precise limiting
   statement.
5. **Numerics.** Use reconstructed minimizers and refinement diagnostics to test
   hypotheses suggested by the proved framework, not to replace it.

The finite generalized eigenproblem is therefore mathematically legitimate and
intrinsic. What remains unproved is whether a chosen sequence of such problems
converges to a single infinite-dimensional self-adjoint object.