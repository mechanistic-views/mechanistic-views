---
title: Stratification
---

# Stratification

> **Formal status key**: **[Definition]** standard mathematical definition. **[Theorem]** established result. **[Conjecture]** plausible but unproven. **[Open]** open question.

This is the full mathematical treatment of the [Whitney stratification formalism](/mechanistic-views/formalism/stratification/), which underpins the [stratified view](/mechanistic-views/views/stratified/). For the accessible overview, start with the [parent page](/mechanistic-views/formalism/stratification/).

A **stratified space** is a topological space decomposed into smooth pieces called strata, arranged so that the strata fit together in a controlled way.

## Why the mechanism space is not a manifold

The Grassmannian $\mathrm{Gr}(k, d)$ is a smooth manifold. But the full mechanism space contains mechanisms of qualitatively different types. A *sequence* of $k$-dimensional subspaces $\{S_n\} \subset \mathrm{Gr}(k,d)$ can converge (in the topology of subspace convergence) to a $(k-1)$-dimensional subspace: write $S_n = \mathrm{span}(v_1^n, \ldots, v_k^n)$ where the vectors converge but $v_k^n \to 0$ — the limit has only $k-1$ independent vectors and lives in $\mathrm{Gr}(k-1, d)$, not $\mathrm{Gr}(k, d)$. (Note: this is a property of a sequence converging, not of a single subspace. "Principal angles" are always defined between *two specific subspaces*, not within one.)

A stratified space accommodates mechanisms of different dimensionalities in a single ambient structure.

## Whitney stratification

A **Whitney stratification** of $X$ is a decomposition $X = \bigsqcup_\alpha S_\alpha$ into smooth manifolds satisfying:

1. **Local finiteness**: every point has a neighborhood meeting finitely many strata.
2. **Frontier condition**: if $S_\beta \cap \overline{S_\alpha} \neq \emptyset$, then $S_\beta \subseteq \overline{S_\alpha}$. Concretely for mechanism space: $\mathcal{M}_j \subset \overline{\mathcal{M}_k}$ for $j < k$, meaning every lower-dimensional mechanism is a limit of $k$-dimensional mechanisms. This reflects the dimension-drop convergence described in the introduction: a sequence of $k$-dimensional subspaces can converge to a $(k-1)$-dimensional subspace as one direction collapses.
3. **Whitney condition A**: if $x_i \in S_\alpha$ converges to $y \in S_\beta \subset \overline{S_\alpha}$ and $T_{x_i}S_\alpha \to \tau$, then $T_y S_\beta \subseteq \tau$.
4. **Whitney condition B**: if $x_i \in S_\alpha$ and $y_i \in S_\beta$ both converge to $y \in S_\beta$, and the secant lines $\overline{x_i y_i} \to \ell$ while $T_{x_i}S_\alpha \to \tau$, then $\ell \subseteq \tau$.

Conditions A and B prevent the strata from meeting in geometrically wild ways and ensure the stratification behaves predictably under perturbation.

## The mechanism space stratification

$$\mathcal{M} = \mathcal{M}_1 \sqcup \mathcal{M}_2 \sqcup \cdots \sqcup \mathcal{M}_d \sqcup \mathcal{M}_\infty$$

where $\mathcal{M}_k = \mathrm{Gr}(k, d) / \mathcal{G}$ is the gauge quotient of the $k$-dimensional Grassmannian.

**What is established.** Each $\mathrm{Gr}(k, d)$ is a smooth compact manifold. The gauge quotients $\mathcal{M}_k$ are smooth manifolds at generic points (where $\mathcal{G}$ acts freely — see the [Gauge and Holonomy](gauge-holonomy/) page) and orbifolds at fixed points. The natural closure relation $\overline{\mathcal{M}_k} \supseteq \mathcal{M}_j$ for $j < k$ holds: lower-dimensional mechanisms are at the boundary of higher-dimensional ones.

**What is conjectured.** That these pieces assemble into a Whitney stratification satisfying conditions A and B. Verifying Whitney conditions for the gauge quotients $\mathrm{Gr}(k,d)/\mathcal{G}$ and their boundaries is a non-trivial geometric task not carried out here. Thom-Mather theory applies cleanly to the finite strata at generic points under this assumption.

**$\mathcal{M}_\infty$: the distributed stratum.** This stratum is defined negatively: mechanisms with no finite-dimensional representative. It currently has no smooth structure, no tangent space, and no verified Whitney conditions. Treating it as a stratum is a working hypothesis; it does not have the same mathematical status as the finite Grassmannian strata. In particular, Thom-Mather theory has not been extended to $\mathcal{M}_\infty$, and the closure and frontier conditions involving $\mathcal{M}_\infty$ are not established.

## Computational tractability

**[Stratum assignment — not yet standardized]** Assigning a mechanism to the correct stratum $\mathcal{M}_k$ requires determining the causal dimensionality $k$. No canonical algorithm exists. Current practice: try DAS for $k = 1, 2, \ldots$ and stop when IIA saturates. This is heuristic and can misclassify near-boundary mechanisms.

**[Finite strata — tractable in principle]** For a mechanism assigned to $\mathcal{M}_k$, geodesic distance and Fréchet mean are tractable (see [Grassmannian](grassmannian/)). Whitney condition verification for specific quotients is a mathematical problem, not a computational one.

**[$\mathcal{M}_\infty$ — no practical algorithm]** There is currently no algorithm for assigning a mechanism to $\mathcal{M}_\infty$ beyond heuristics based on dark matter (persistent coverage gaps and non-zero $H^1$). This is the main computational open problem for the stratified view.

## Thom-Mather theory (for the finite strata)

Mather (1973) and Thom (1969) developed **control data** for Whitney stratified spaces: tubular neighborhoods $T_k$, retraction maps $\pi_k: T_k \to \mathcal{M}_k$, and distance functions $\rho_k: T_k \to [0, \infty)$, with compatibility conditions between adjacent strata. The retraction $\pi_k$ provides a formal version of the intuition that "a circuit diagram is a $\mathcal{M}_k$ approximation to a mechanism" — it projects nearby mechanisms down to their best $k$-dimensional description.

This applies to the finite Grassmannian strata at generic points. Extension to $\mathcal{M}_\infty$ is open.

## Spectral sequences

For computing cosheaf cohomology on a stratified complex augmented with 2-cells, the natural tool is the spectral sequence of the filtered cochain complex (filtered by layer depth). For the unaugmented transformer layer graph — a DAG with no 2-cells — the cochain complex is $0 \to C^0 \to C^1 \to 0$, and any spectral sequence degenerates at $E_2$ trivially (there are no higher differentials). The open question is only non-trivial once 2-cells are attached.

**Open question** (OQ 5.6, conditioned on 2-cell augmentation). At which page does the spectral sequence of the augmented circuit cosheaf degenerate for natural transformer mechanisms?

## Evidence standards by stratum

- $\mathcal{M}_1$: feature direction recovery plus causal ablation
- $\mathcal{M}_k$, $k \geq 2$: DAS-based subspace recovery plus weight-space triangulation
- $\mathcal{M}_\infty$: demonstrating $H^0 = 0$ and $H^1 \neq 0$ (subject to caveats in the Sheaf Cohomology page)

Stratum assignment is a prior question. There is currently no canonical algorithm for it.

## See also

- [Whitney stratification formalism](/mechanistic-views/formalism/stratification/) — accessible overview without proofs
- [Stratified view](/mechanistic-views/views/stratified/) — the view that uses stratification as its organizing principle
- [Grassmannian deep dive](grassmannian/) — the geometry of individual strata $\mathcal{M}_k$
- [Sheaf Cohomology deep dive](sheaves/) — $H^1 \neq 0$ as evidence for the $\mathcal{M}_\infty$ stratum
- [Gauge Quotients and Holonomy deep dive](gauge-holonomy/) — gauge structure within each stratum
- [Grokking case study](/mechanistic-views/cases/grokking/) — example of a nonlinear manifold stratum ($S^1 \subset \mathcal{M}_2$)
