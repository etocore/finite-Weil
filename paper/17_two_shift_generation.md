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

Because the paired translation is even in its shift parameter,

\[
T_{-s}=T_s,
\]

the nondegeneracy condition must be \(s^2\neq t^2\), rather than merely \(s\neq t\).

### Conjecture 17.1 (two-shift generation)

For shifts satisfying \(s^2\neq t^2\),

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

That would make both parity graphs complete. Initial numerical experiments, however, indicate that individual same-parity matrix elements can vanish at isolated values of \(t\). For example, with \(h=\sigma=1\), \(N=4\), and \(s=1\), one odd-sector off-diagonal entry appears to cross zero near

\[
t\approx 3.4878498984.
\]

Similar isolated zeros occur in larger dimensions. These computations are not a proof of an exact zero, but they strongly indicate that complete coupling is too strong to serve as the main theorem.

The correct target is therefore connectivity rather than entrywise nonvanishing. Isolated missing edges are harmless provided each parity graph remains connected.

## 17.5 The analytic rank certificate

Let

\[
E_\pm=\ker(J\mp I),
\qquad
n_\pm=\dim E_\pm,
\]

and write \(T_r^\pm\) for the restriction of \(T_r\) to \(E_\pm\). Define the parity-sector commutator maps

\[
\mathcal L_{s,t}^\pm:M_{n_\pm}(\mathbb C)
\longrightarrow
M_{n_\pm}(\mathbb C)\oplus M_{n_\pm}(\mathbb C)
\]

by

\[
\mathcal L_{s,t}^\pm(X)
=
\bigl([X,T_s^\pm],[X,T_t^\pm]\bigr).
\]

The scalar matrices always lie in \(\ker\mathcal L_{s,t}^\pm\). Therefore

\[
\operatorname{rank}\mathcal L_{s,t}^\pm\le n_\pm^2-1.
\]

### Proposition 17.4 (rank criterion)

The following are equivalent:

1. \(\operatorname{alg}^*(T_s,T_t)=\mathfrak G_N\).
2. \(\{T_s,T_t\}'=\operatorname{span}\{I,J\}\).
3. For both signs,
   \[
   \ker\mathcal L_{s,t}^\pm=\mathbb C I_{E_\pm}.
   \]
4. For both signs,
   \[
   \operatorname{rank}\mathcal L_{s,t}^\pm=n_\pm^2-1.
   \]

### Proof

Every matrix commuting with \(J\) decomposes uniquely into an even block and an odd block. Since both \(T_s\) and \(T_t\) commute with \(J\), their joint commutant inside \(\{J\}'\) is

\[
\ker\mathcal L_{s,t}^+\oplus\ker\mathcal L_{s,t}^-.
\]

This equals \(\operatorname{span}\{I,J\}\) precisely when each parity-sector kernel consists only of scalar matrices. Rank-nullity then gives the fourth condition. The bicommutant theorem gives the equivalence with generation. \(\square\)

Choose bases of the two matrix spaces and represent \(\mathcal L_{s,t}^\pm\) by matrices \(L_\pm(s,t)\). Their entries are real-analytic functions of \((s,t)\), because every entry of \(T_r\) is real analytic in \(r\).

A maximal minor

\[
\Delta_\pm(s,t)
\]

of size \((n_\pm^2-1)\times(n_\pm^2-1)\) is therefore real analytic. If, for one witness pair \((s_0,t_0)\),

\[
\Delta_+(s_0,t_0)\Delta_-(s_0,t_0)\neq0,
\]

then neither determinant is identically zero. Consequently the exceptional set

\[
\mathcal E_N
=
\{(s,t):\operatorname{alg}^*(T_s,T_t)\neq\mathfrak G_N\}
\]

is contained in the proper real-analytic set

\[
\{\Delta_+\Delta_-=0\}.
\]

This proves generic two-shift generation once a single pair is rigorously certified.

### Corollary 17.5 (generic generation from one witness)

If there exists one pair \((s_0,t_0)\) for which

\[
\operatorname{rank}\mathcal L_{s_0,t_0}^\pm=n_\pm^2-1
\]

in both parity sectors, then two-shift generation holds on an open dense subset of the parameter plane, and its failure is confined to a proper real-analytic determinantal set.

This is the first rigorous target. It is weaker than the all-pairs conjecture, but it converts numerical evidence into a theorem as soon as one exact or interval-certified witness is found.

## 17.6 Functional-equation meaning of the certificate

Let

\[
\Phi(v)(z)=\sum_j v_j\widehat g_j(z),
\qquad
\widehat g_j(z)=\sigma\sqrt{2\pi}\,e^{-\sigma^2z^2/2}e^{-izc_j}.
\]

For a symmetric center set, let \(j'\) denote the reflected index, so that \(c_{j'}=-c_j\). Then

\[
\widehat g_{j'}(z)=\widehat g_j(-z).
\]

If \(R\) denotes reflection on the transform side,

\[
(Rh)(z)=h(-z),
\]

then

\[
\boxed{\Phi J=R\Phi.}
\]

Indeed,

\[
(\Phi Jv)(z)
=
\sum_j v_j\widehat g_{j'}(z)
=
\sum_j v_j\widehat g_j(-z)
=
(R\Phi v)(z).
\]

Because the frequencies \(c_j\) are distinct, \(\Phi\) is injective. Thus the coefficient-space reflection \(J\) is exactly intertwined with the involution \(z\mapsto-z\), equivalently \(s\mapsto1-s\) in critical-line coordinates \(s=\tfrac12+iz\).

Accordingly,

\[
\Phi(E_+)=\Phi(\mathbb C^N)\cap\{h:h(z)=h(-z)\},
\]

and

\[
\Phi(E_-)=\Phi(\mathbb C^N)\cap\{h:h(z)=-h(-z)\}.
\]

The analytic rank certificate therefore has a precise functional-equation interpretation. If

\[
\operatorname{rank}\mathcal L_{s,t}^\pm=n_\pm^2-1,
\]

then the two translations act irreducibly inside each symmetric or antisymmetric functional-equation sector. Equivalently, the only operators commuting with both translations are independent scalars on the two sectors. Transported back to coefficient coordinates, these are exactly

\[
aI+bJ.
\]

Thus a successful rank certificate proves more than two-generator minimality:

> Within the finite packet compression, the functional-equation involution is the unique nontrivial symmetry surviving the joint action of the two Gaussian translations.

This conclusion depends on both ingredients:

- the rank certificate proves uniqueness of the surviving symmetry;
- the intertwining theorem identifies that symmetry as the compressed functional-equation involution.

Neither theorem implies the other, but together they give the algebraic statement its analytic meaning.

## 17.7 Immediate research tasks

The reduction above isolates four concrete tasks.

1. **Exact witness.** Find one pair \((s_0,t_0)\) for each \(N\), preferably with algebraic or rationally controlled parameters, for which both maximal ranks can be certified exactly or by interval arithmetic.

2. **Simple spectrum.** Determine for which shifts \(s\) the matrix \(T_s\) has simple spectrum in each parity sector, or prove that any degeneracies are isolated.

3. **Connectivity certificate.** Find a fixed collection of matrix entries, such as a spanning tree inside each parity block, and prove that those entries cannot vanish simultaneously when \(s^2\neq t^2\).

4. **Exceptional set.** Determine whether the proper analytic exceptional set contains anything beyond the unavoidable diagonal loci \(t=\pm s\), or exhibit a genuine exceptional pair.

## 17.8 Current status

The graph criterion and analytic rank criterion are exact. The functional-equation intertwining is exact. Together they identify the desired theorem as follows:

\[
\boxed{
\text{two generic Gaussian translations leave only the functional-equation symmetry.}
}
\]

What remains unproved is the existence of a rigorously certified witness uniformly in \(N\), and the stronger claim that no exceptional pairs exist away from \(t=\pm s\). The next computational step is to construct the parity-sector commutator matrices \(L_\pm(s,t)\), locate stable maximal minors, and certify one nonzero pair without relying solely on floating-point rank.