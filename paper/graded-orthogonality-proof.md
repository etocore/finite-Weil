# Graded orthogonality from analytic QR

This note proves the remaining estimate in the width-rotation argument.

## Statement

Let

\[
K(v)_{ij}=\exp\!\left(-\frac v2(x_i-x_j)^2\right),
\qquad v>0,
\]

on \(N\) distinct real nodes. Put

\[
E(v)=e^{-vX^2/2},
\qquad
m_k=(x_1^k,\ldots,x_N^k)^{\mathsf T}.
\]

Let \(u_n(v)\) be the normalized eigenvector whose eigenvalue satisfies

\[
\mu_n(v)=c_nv^n+O(v^{n+1}),
\qquad c_n>0.
\]

Then, for every \(k<n\),

\[
\boxed{
\langle E(v)m_k,u_n(v)\rangle=O(v^{n-k}).
}
\]

In particular, with \(n=r+2\),

\[
\boxed{
\langle E(v)m_r,u_{r+2}(v)\rangle=O(v^2).
}
\]

This is stronger than the estimate previously required.

## 1. Exact finite feature reduction

Let

\[
V=[m_0\;m_1\;\cdots\;m_{N-1}].
\]

Because the nodes are distinct, \(V\) is invertible. Every \(m_k\), including \(k\ge N\), has a unique representation

\[
m_k=Va_k,
\]

where \(a_k=e_k\) for \(0\le k<N\). The exact Gaussian feature expansion gives

\[
K(v)=E(v)\left(\sum_{k\ge0}\frac{v^k}{k!}m_km_k^{\mathsf T}\right)E(v).
\]

Set

\[
W(v)=E(v)V.
\]

Then

\[
\boxed{
K(v)=W(v)C(v)W(v)^{\mathsf T},
}
\]

where

\[
C(v)=\sum_{k\ge0}\frac{v^k}{k!}a_ka_k^{\mathsf T}.
\]

Since \(a_k=e_k\) for \(k<N\),

\[
C(v)
=
\operatorname{diag}\!\left(1,v,\frac{v^2}{2!},\ldots,\frac{v^{N-1}}{(N-1)!}\right)
+O(v^N)
\]

entrywise as \(v\to0^+\).

## 2. Analytic QR basis

Take the QR factorization with positive diagonal,

\[
W(v)=Q(v)R(v).
\]

Because \(W(v)\) is analytic and invertible near \(v=0\), both \(Q(v)\) and \(R(v)\) are analytic there. The matrix \(R(v)\) is upper triangular with nonzero diagonal.

Write \(q_j(v)\) for the columns of \(Q(v)\). Since the first \(j+1\) columns of \(W(v)\) span the first \(j+1\) columns of \(Q(v)\),

\[
E(v)m_k\in\operatorname{span}\{q_0(v),\ldots,q_k(v)\}.
\]

Equivalently,

\[
\boxed{
\langle E(v)m_k,q_j(v)\rangle=0
\quad\text{whenever }j>k.
}
\]

At \(v=0\), the \(q_j(0)\) are the discrete orthonormal polynomials \(p_j\).

In the \(Q(v)\)-basis,

\[
H(v):=Q(v)^{\mathsf T}K(v)Q(v)=R(v)C(v)R(v)^{\mathsf T}.
\]

The triangularity of \(R(v)\) and the graded diagonal of \(C(v)\) imply

\[
\boxed{
H_{ij}(v)=O\!\left(v^{\max(i,j)}\right).
}
\]

Moreover,

\[
H_{ii}(v)=c_iv^i+O(v^{i+1}),
\qquad
c_i=\frac{R_{ii}(0)^2}{i!}>0.
\]

## 3. Graded inverse bound

Fix \(n\), and split indices into

\[
L=\{0,\ldots,n-1\},
\qquad
H=\{n,\ldots,N-1\}.
\]

The leading part of the lower principal block has the factorization

\[
H_{LL}(v)
=
R_L(v)D_L(v)R_L(v)^{\mathsf T}+O(v^n),
\]

where \(R_L(v)\) is invertible upper triangular and

\[
D_L(v)=\operatorname{diag}\!\left(1,v,\ldots,\frac{v^{n-1}}{(n-1)!}\right).
\]

For the unperturbed graded factor,

\[
\left(R_LD_LR_L^{\mathsf T}\right)^{-1}
=R_L^{-\mathsf T}D_L^{-1}R_L^{-1}.
\]

Because \(R_L^{-1}\) is upper triangular, the \((i,j)\) entry contains only grades at most \(\min(i,j)\). Consequently,

\[
\left(R_LD_LR_L^{\mathsf T}\right)^{-1}_{ij}
=O\!\left(v^{-\min(i,j)}\right).
\]

The remainder \(O(v^n)\) changes this inverse by a convergent Neumann correction: multiplying an \(O(v^n)\) entry by the graded inverse produces at worst \(O(v)\) in the bottom grade. Hence

\[
\boxed{
\left(H_{LL}(v)-\mu_n(v)I\right)^{-1}_{ij}
=O\!\left(v^{-\min(i,j)}\right).
}
\]

Here subtracting \(\mu_n(v)I=O(v^n)I\) is absorbed into the same remainder.

## 4. Lower coordinates of the \(n\)-th eigenvector

Write the eigenvector in the QR basis:

\[
u_n(v)=Q(v)y^{(n)}(v),
\qquad
H(v)y^{(n)}(v)=\mu_n(v)y^{(n)}(v).
\]

Normalize the gauge so that \(y_n^{(n)}(v)\to1\). The high coordinates remain bounded.

The lower block of the eigenvalue equation is

\[
\left(H_{LL}-\mu_n I\right)y_L
=-H_{LH}y_H.
\]

For \(i<n\) and \(j\ge n\), the graded matrix estimate gives

\[
H_{ij}(v)=O(v^j)=O(v^n).
\]

Thus every component of \(H_{LH}y_H\) is \(O(v^n)\). Applying the graded inverse bound yields, for \(i<n\),

\[
\begin{aligned}
y_i^{(n)}(v)
&=
\sum_{j<n}
O\!\left(v^{-\min(i,j)}\right)O(v^n)\\
&=O(v^{n-i}).
\end{aligned}
\]

Therefore

\[
\boxed{
y_i^{(n)}(v)=O(v^{n-i})\quad(i<n).}
\]

This is the graded eigenvector-separation estimate.

## 5. Exact orthogonality estimate

Because

\[
E(v)m_k=W(v)e_k=Q(v)R(v)e_k,
\]

and \(R(v)e_k\) has support only in indices \(0,\ldots,k\),

\[
\begin{aligned}
\langle E(v)m_k,u_n(v)\rangle
&=
\sum_{i=0}^{k}R_{ik}(v)y_i^{(n)}(v)\\
&=
\sum_{i=0}^{k}O(v^{n-i})\\
&=O(v^{n-k}).
\end{aligned}
\]

Hence

\[
\boxed{
\langle E(v)m_k,u_n(v)\rangle=O(v^{n-k})
\qquad(k<n).
}
\]

Taking \(n=r+2\) and \(k=r\) proves

\[
\boxed{
\langle E(v)m_r,u_{r+2}(v)\rangle=O(v^2).
}
\]

Thus the apparent first-order cancellation is not accidental and does not require computing the correction vector \(q_{r+2}^{(1)}\). It follows from two exact facts:

1. analytic QR makes \(E(v)m_k\) lie exactly in the first \(k+1\) graded directions;
2. the \(n\)-th eigenvector enters the \(i\)-th lower graded direction only at order \(v^{n-i}\).

## 6. Consequence for the chain coefficient

The sum term in the double-commutator decomposition is therefore one power smaller than the \(X^2\) term. The leading chain coefficient is

\[
C_r
=
\frac{\sqrt\pi}{2}\,2^{-r}c_ra_{r+1}a_{r+2},
\]

under the recurrence convention

\[
xp_j=a_{j+1}p_{j+1}+b_jp_j+a_jp_{j-1}.
\]

Every factor is strictly positive. Therefore

\[
g_r\not\equiv0
\]

for every admissible \(r\). Combined with analyticity, the parity-chain graph argument yields generic-width local two-shift generation outside a discrete exceptional set.

## Audit point

The only step that merits an independent line-by-line check is the graded inverse estimate for the perturbed lower block. The estimate follows from the exact triangular factorization and a Neumann-series correction, but it should be expanded in the final paper if a referee requests explicit constants.