# Chapter 17. Two-Shift Generation

## 17.1 The minimal-generator problem

Let

\[
\mathfrak G_N=\operatorname{alg}^*\{T_s:s\in\mathbb R\}
\]

be the finite Gaussian translation algebra on an equally spaced symmetric packet grid. By the structure theorem,

\[
\mathfrak G_N=\{J\}'\cong M_{\lceil N/2\rceil}(\mathbb C)\oplus M_{\lfloor N/2\rfloor}(\mathbb C),
\]

and

\[
\mathfrak G_N'=\operatorname{span}_{\mathbb C}\{I,J\}.
\]

The next question is whether two paired Gaussian translations already generate the full algebra.

### Conjecture 17.1 (two-shift generation)

For distinct shifts \(s\neq t\),

\[
\operatorname{alg}^*(T_s,T_t)=\mathfrak G_N.
\]

Equivalently,

\[
\{T_s,T_t\}'=\operatorname{span}_{\mathbb C}\{I,J\}.
\]

The equivalence follows from the finite-dimensional bicommutant theorem.

## 17.2 Reduction to a graph-connectivity problem

Fix \(s\) and assume that \(T_s\) has simple spectrum. Choose an orthonormal eigenbasis

\[
T_su_i=\lambda_i u_i,
\qquad i=1,\dots,N,
\]

and let \(U\) be the unitary matrix with columns \(u_i\). Since \(T_s\) commutes with reflection \(J\), and its eigenspaces are one-dimensional, every \(u_i\) has definite reflection parity:

\[
Ju_i=\varepsilon_i u_i,
\qquad \varepsilon_i\in\{+1,-1\}.
\]

Set

\[
B=U^*T_tU.
\]

### Lemma 17.2 (commutant graph criterion)

Let \(G(s,t)\) be the graph with vertex set \(\{1,\dots,N\}\), with an edge between distinct vertices \(i\) and \(j\) whenever

\[
B_{ij}\neq0.
\]

Then

\[
\dim\{T_s,T_t\}'
=
\#\{\text{connected components of }G(s,t)\}.
\]

More precisely, in the eigenbasis of \(T_s\), the joint commutant consists exactly of diagonal matrices that are constant on each connected component of \(G(s,t)\).

### Proof

Because \(T_s\) has simple spectrum, any matrix \(X\) commuting with \(T_s\) is diagonal in the chosen eigenbasis:

\[
U^*XU=D_x:=\operatorname{diag}(x_1,\dots,x_N).
\]

The second commutation relation is

\[
D_xB=BD_x.
\]

Entrywise,

\[
(x_i-x_j)B_{ij}=0
\]

for all \(i,j\). Therefore \(x_i=x_j\) along every edge of \(G(s,t)\), hence on every connected component. Conversely, any diagonal matrix constant on each connected component satisfies the same entrywise equations and therefore commutes with \(B\). The dimension is consequently the number of connected components. \(\square\)

## 17.3 Parity decomposition of the graph

Since \(T_t\) also commutes with \(J\),

\[
(\varepsilon_i-\varepsilon_j)B_{ij}=0.
\]

Thus

\[
B_{ij}=0
\qquad\text{whenever}\qquad
\varepsilon_i\neq\varepsilon_j.
\]

The graph therefore splits as

\[
G(s,t)=G_+(s,t)\sqcup G_-(s,t),
\]

where \(G_+\) and \(G_-\) are the induced graphs on the even and odd eigenspaces of \(T_s\).

This gives the exact reformulation of the two-shift conjecture.

### Corollary 17.3 (connectivity formulation)

Assume \(T_s\) has simple spectrum. Then

\[
\{T_s,T_t\}'=\operatorname{span}_{\mathbb C}\{I,J\}
\]

if and only if both parity graphs \(G_+(s,t)\) and \(G_-(s,t)\) are connected.

### Proof

The two parity classes are always distinct connected components, so the graph has at least two components. By Lemma 17.2, the joint commutant has dimension two exactly when each parity subgraph is connected. Since \(I\) and \(J\) always belong to the joint commutant and are linearly independent, any two-dimensional joint commutant must equal their span. \(\square\)

## 17.4 A stronger route, and why it is probably false

A sufficient condition for Corollary 17.3 would be the complete-coupling statement

\[
B_{ij}\neq0
\quad\text{for every distinct same-parity pair }i,j.
\]

That would make both parity graphs complete. Initial numerical experiments, however, indicate that individual same-parity matrix elements can vanish at isolated values of \(t\neq s\). For example, with \(h=\sigma=1\), \(N=4\), and \(s=1\), one odd-sector off-diagonal entry appears to cross zero near

\[
t\approx 3.4878498984.
\]

Similar isolated zeros occur in larger dimensions. These computations are not a proof of an exact zero, but they strongly indicate that complete coupling is too strong to serve as the main theorem.

The correct target is therefore connectivity rather than entrywise nonvanishing. Isolated missing edges are harmless provided each parity graph remains connected.

## 17.5 Immediate research tasks

The reduction above isolates three concrete tasks.

1. **Simple spectrum.** Determine for which shifts \(s\) the matrix \(T_s\) has simple spectrum in each parity sector, or prove that any degeneracies are isolated.

2. **Connectivity certificate.** Find a fixed collection of matrix entries, such as a spanning tree inside each parity block, and prove that those entries cannot vanish simultaneously for distinct \(s,t\).

3. **Exceptional set.** Treat the commutant equations directly as an analytic rank problem in \((s,t)\). The failure of two-shift generation is the vanishing of all \((N^2-2)\)-rank certificates of the joint commutator map

\[
X\longmapsto([X,T_s],[X,T_t]).
\]

Because the matrix entries depend real-analytically on \((s,t)\), the exceptional set is a real-analytic determinantal set. Proving one pair has minimal commutant establishes generic two-shift generation, even before the stronger all-distinct-pairs conjecture is resolved.

## 17.6 Current status

The graph criterion is exact. The statement that every same-parity entry is nonzero is not presently supported and is likely false. The next rigorous milestone should therefore be one of the following:

- prove generic two-shift generation by exhibiting one analytically or rigorously certified pair;
- prove connectivity through a sparse set of protected edges;
- or find a genuine exceptional pair, which would force a correction of Conjecture 17.1.
