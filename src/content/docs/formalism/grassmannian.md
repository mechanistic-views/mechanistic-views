---
title: Grassmannian Geometry
---

# Grassmannian Geometry

> **Formal status key**: **[Definition]** standard mathematical definition. **[Theorem]** established result. **[Conjecture]** plausible but unproven. **[Open]** open question. Applies to all Formalisms pages.

The Grassmannian is the natural ambient space for mechanism claims under the subspace and structural views.

## Concrete intuition before the definitions

If you have not seen a Grassmannian before, start here.

Consider all the flat 2-dimensional planes through the origin in 3-dimensional space — not tilted planes, but planes through the center. There are infinitely many: the $xy$-plane, the $xz$-plane, and all the planes in between. The set of all such planes is the Grassmannian $\mathrm{Gr}(2, 3)$. Each plane is a *point* in this space, and nearby points are nearly parallel planes. It is a smooth curved space (a manifold), like a sphere, except the points are planes rather than tips of arrows.

Now scale up: in a transformer with residual stream dimension $d = 512$, the Grassmannian $\mathrm{Gr}(k, 512)$ is the space of all $k$-dimensional subspaces of $\mathbb{R}^{512}$. A mechanism under the subspace view is a specific $k$-dimensional direction in this space — say, the 2-dimensional subspace that encodes the subject/object distinction in the IOI task. Two experiments that recover different basis matrices $Q$ and $Q'$ but the same column span are measuring the same mechanism; they are the same point in the Grassmannian.

The reason this is useful: distance between mechanisms (are these two models implementing the same mechanism?) becomes a geometric question — how far apart are two points in the Grassmannian? — with a precise, computable answer via principal angles.

## Why subspaces, not vectors

Distributed alignment search (DAS) recovers a matrix $Q \in \mathbb{R}^{d \times k}$ such that intervening on $QQ^\top x$ transfers a causal variable. But $Q$ and $QR$ produce the same projector $QQ^\top$ for any $R \in O(k)$. DAS identifies an equivalence class under right-multiplication by $O(k)$ — that class is the column span: a $k$-dimensional subspace of $\mathbb{R}^d$.

A mechanism claim under the subspace view is a claim about a point in the space of $k$-dimensional subspaces of $\mathbb{R}^d$. That space is the Grassmannian.

## Definition

The **Grassmannian** $\mathrm{Gr}(k, d)$ is the set of all $k$-dimensional linear subspaces of $\mathbb{R}^d$.

It is a smooth compact manifold of dimension $k(d-k)$.

Compact means sequences of subspaces always have convergent subsequences — claims about convergence of subspace estimates are well-posed.

## Representing points

A point $S \in \mathrm{Gr}(k, d)$ can be represented as:
- The column span of $Q \in \mathbb{R}^{d \times k}$ with $Q^\top Q = I_k$
- The projection matrix $P = QQ^\top$ with $P^2 = P$ and $\mathrm{rank}(P) = k$
- A point in the Stiefel manifold $\mathrm{St}(k,d)$ modulo the right action of $O(k)$

For computation, the projection matrix is most convenient.

## Distance: principal angles

Given $S_1, S_2 \in \mathrm{Gr}(k, d)$ with projection matrices $P_1, P_2$, the **principal angles** $0 \leq \theta_1 \leq \cdots \leq \theta_k \leq \pi/2$ between the two subspaces are:

$$\cos\theta_i = \sigma_i(P_1 P_2)$$

Principal angles are a property of the pair $(S_1, S_2)$, not of either subspace alone.

The **geodesic distance** is:

$$d(S_1, S_2) = \left(\sum_{i=1}^k \theta_i^2\right)^{1/2}$$

This is invariant to simultaneous orthogonal transformation: $d(US_1, US_2) = d(S_1, S_2)$ for $U \in O(d)$.

**Computing from matrix representatives** $Q_1, Q_2$:
1. Compute $M = Q_1^\top Q_2 \in \mathbb{R}^{k \times k}$
2. SVD: $M = U\Sigma V^\top$, giving singular values $\sigma_1 \geq \cdots \geq \sigma_k \geq 0$
3. $\theta_i = \arccos(\sigma_i)$ (singular values are in $[0,1]$ when $Q_1, Q_2$ have orthonormal columns)

Note: the formula $\cos\theta_i = \sigma_i(P_1 P_2)$ in the definition above uses the fact that the nonzero singular values of $P_1 P_2 = Q_1 Q_1^\top Q_2 Q_2^\top$ equal those of $Q_1^\top Q_2$. Computing from $Q_1, Q_2$ directly is numerically preferable.

## Transport maps

For $W \in \mathbb{R}^{d_\text{out} \times d_\text{in}}$, the induced **transport map** is:

$$\tau_W: \mathrm{Gr}(k, d_\text{in}) \to \mathrm{Gr}(k', d_\text{out}), \quad \tau_W(S) = \overline{\mathrm{span}(WS)}$$

where $k' = \mathrm{rank}(W|_S)$. For nonlinear modules, transport is approximated via the expected Jacobian: $\tau_f(S) \approx \overline{\mathrm{span}(\mathbb{E}[J_f(x)] \cdot S)}$ where the expectation is over the input distribution. This is an approximation; its accuracy degrades when the nonlinearity is large relative to the distribution width, or when the Jacobian varies substantially across the distribution.

The **G-SCM** uses transport maps as edges: nodes are subspaces, edges are weight-induced transports. An alignment that does not respect transport structure violates the causal independence assumptions of the SCM.

## Computational tractability

**[Theorem — tractable]** Principal angles and geodesic distance are computable in $O(kd^2)$ via the SVD of $Q_1^\top Q_2$. The Fréchet mean on $\mathrm{Gr}(k,d)$ is computable via iterative algorithms (gradient descent on the manifold) in $O(nkd)$ per step, where $n$ is the number of samples. Both scale to residual stream dimensions used in practice ($d = 512$–$4096$, $k = 1$–$32$).

**[Practical status]** DAS-based subspace recovery (the primary method for identifying $\mathcal{M}_k$ mechanisms) runs at training cost. Cross-seed Fréchet variance computation is feasible post-hoc. Transport map estimation via expected Jacobian is the bottleneck for nonlinear layers; cost scales with sample size for the Jacobian expectation.

## Fréchet mean and variance

For comparing subspace estimates across seeds or prompts, the Fréchet (Riemannian) mean and variance provide summary statistics:

**Fréchet mean**: $\bar{S} = \arg\min_{S} \sum_i d(S, S_i)^2$ (the factor $1/n$ does not affect the argmin)

**Fréchet variance**: $\sigma^2_F = \frac{1}{n}\sum_i d(\bar{S}, S_i)^2$

MechVal's measurement validity criterion can be operationalized as Fréchet variance below threshold $\epsilon_M$ across seeds and prompts.
