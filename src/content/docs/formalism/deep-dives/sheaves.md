---
title: Sheaf Cohomology
---

# Sheaf Cohomology

This is the full mathematical treatment of cosheaf cohomology for circuit localizability, relevant to the [structural view](/mechanistic-views/views/structural/) and [stratified view](/mechanistic-views/views/stratified/). Related to the [fiber bundle quotient formalism](/mechanistic-views/formalism/fiber-bundle-quotient/).

Sheaf cohomology answers a specific question: can local descriptions of a mechanism be consistently assembled into a global one?

This is a topological question about the mechanism's structure. If the answer is no, then no method will produce a complete localization, because none exists.

> **Formal status key**: **[Definition]** standard mathematical definition. **[Theorem]** established result. **[Conjecture]** plausible but unproven. **[Open]** open question.

## Sheaves vs cosheaves: why a cosheaf

A **sheaf** is contravariant: it assigns data to open sets and restricts data from larger sets to smaller ones — the maps go *against* the direction of containment. Classical sheaves model situations where you lose information when you zoom in to a subregion.

A **cosheaf** is covariant: it assigns data to open sets and extends data from smaller sets to larger ones — the maps go *with* the direction of containment. Cosheaves model situations where local data is transported forward to contribute to larger-scale descriptions.

The transformer circuit is modelled with a **cosheaf** because information flows forward: a representation at layer $l$ is transported (via weight matrices) to layer $l+1$. The extension map $\text{ext}_{u \to v}: \mathcal{F}(u) \to \mathcal{F}(v)$ follows the computational graph. Forcing a sheaf structure would require restricting information backwards, which reverses causality. The correct object is the cosheaf, and cohomology is computed on its cochain complex.

## Terminological note

The construction here is a **cellular cosheaf on a directed graph**, following Hansen and Ghrist (2021). Data is assigned to vertices and edges, with coboundary maps going *forward* along edges. "Sheaf" is used as shorthand in the literature; this note clarifies the categorical choice.

## The cochain complex for a directed graph

The transformer's layer graph is a directed acyclic graph $G = (V, E)$. It has no triangular faces or higher-dimensional cells. For a graph, the cochain complex has exactly two non-trivial levels:

$$0 \to C^0(G, \mathcal{F}) \xrightarrow{\delta^0} C^1(G, \mathcal{F}) \to 0$$

**The complex terminates at $C^1$.** There is no $C^2$ unless the graph is augmented with 2-cells (triangles). Consequently:

- $H^0(\mathcal{F}) = \ker(\delta^0)$
- $H^1(\mathcal{F}) = C^1(G, \mathcal{F}) / \mathrm{im}(\delta^0)$ — a direct quotient
- $H^n(\mathcal{F}) = 0$ for $n \geq 2$, without 2-cells

## Computational tractability

**[$H^0$ — tractable]** $H^0(\mathcal{F}) = \ker(\delta^0)$ reduces to checking consistency of local sections under transport. Equivalent to a least-squares system; computable for circuits of practical size (tens of components). Cost scales as $O(|E| \cdot k^2)$ where $|E|$ is the number of edges in the circuit and $k$ is the subspace dimension.

**[$H^1$ — tractable for small circuits]** $H^1(\mathcal{F}) = C^1 / \mathrm{im}(\delta^0)$ requires computing the image of $\delta^0$ and the quotient. For circuits with $|V| < 50$ nodes and $k \leq 16$, this is a routine linear algebra computation. For full transformer circuits at scale ($|V| \sim 10^3$–$10^4$, $k \sim 64$), it is not yet tractable without approximation.

**[Cosheaf construction — partially tractable]** The base sections (recovered subspaces at each site) require DAS or weight-based subspace recovery, which carries its own computational cost. The main bottleneck is constructing the cosheaf, not computing its cohomology once built.

**[Spectral sequence — not yet practical]** The spectral sequence for augmented circuits with 2-cells has no standardized implementation. Theoretical tool only at this point.

## The construction and its linearization

A **cellular cosheaf** $\mathcal{F}$ on $G$ assigns:
- To each $v \in V$: a vector space $\mathcal{F}(v)$
- To each directed edge $e = (u \to v) \in E$: a coboundary map $\mathcal{F}(u) \to \mathcal{F}(v)$

**The linearization.** The Grassmannian $\mathrm{Gr}(k,d)$ is a manifold, not a vector space. To form a cochain complex we need a vector space at each site. The natural choice is the tangent space $T_{S_v}\mathrm{Gr}(k,d)$ at a **base section** $S_v$ — the DAS-recovered subspace at site $v$.

The coboundary map is then the linearized transport: the derivative $d\tau_{W_e}|_{S_u}: T_{S_u}\mathrm{Gr}(k,d) \to T_{S_v}\mathrm{Gr}(k,d)$.

This means the cosheaf and its cohomology are defined **relative to a choice of base sections** $(S_v)_{v \in V}$. Different base sections give different cosheaves and potentially different cohomology groups. Base sections should be stated explicitly in any empirical application.

The coboundary map $\delta^0$ sends $(v_s)_{s \in V}$ to the edge discrepancies $(d\tau_{W_e}(v_u) - v_v)_{(u,v) \in E}$.

## Global sections: H⁰ (linearized vs. affine)

The linearized cosheaf has two related but distinct questions:

**Linearized question** ($H^0$ of the homogeneous complex): does there exist a consistent *direction* of perturbation away from all base sections simultaneously? $H^0 \neq 0$ means yes — the base sections can be jointly deformed in a consistent direction.

**Affine question** (is the original base section assignment globally consistent?): are the base sections themselves consistent — does $\tau_{W_e}(S_u) = S_v$ hold at every edge? This is not captured by $H^0$ of the linearized complex. It is captured by asking whether the affine discrepancy lies in $\mathrm{im}(\delta^0)$. The discrepancy at edge $e = (u \to v)$ is the tangent vector $c_e = \log_{S_v}(\tau_{W_e}(S_u)) \in T_{S_v}\mathrm{Gr}(k,d)$, where $\log_{S_v}$ is the Riemannian log map at $S_v$ — the inverse of the exponential map, expressing $\tau_{W_e}(S_u)$ as a tangent vector at the base section $S_v$. (Naive subtraction $S_v - \tau_{W_e}(S_u)$ is not defined since $S_v$ and $\tau_{W_e}(S_u)$ are points on a manifold, not vectors.) With this definition, $c \in C^1$. If $c \in \mathrm{im}(\delta^0)$: there exists a global adjustment making all local descriptions consistent. If $[c] \neq 0$ in $H^1$: no such adjustment exists.

In practice it is the **affine question** that captures whether the DAS-recovered local subspaces are mutually consistent, and the answer lives in $H^1$ (whether the affine discrepancy class is zero), not in $H^0$.

## The obstruction: H¹

$$H^1(\mathcal{F}) = C^1(G, \mathcal{F}) / \mathrm{im}(\delta^0)$$

Non-zero $H^1$: there exist edge-level discrepancies between adjacent-layer subspace descriptions that cannot all be simultaneously resolved by any global assignment.

**Conjecture.** Genuinely distributed mechanisms produce non-zero $H^1$.

*Status.* A conjecture. Two conditions are required:

(a) **Linearization accuracy**: the linearized cosheaf faithfully captures the nonlinear obstruction — requires the base sections to be close enough to a would-be global section that linearization is valid.

(b) **Proposal independence**: non-zero $H^1$ for *this* cosheaf proposal implies no *other* cosheaf proposal has $H^1 = 0$. This is the more serious gap. $H^1 \neq 0$ establishes obstruction in a specific cosheaf built from specific sites and transport maps. A different proposal with different structure might have $H^1 = 0$ for the same underlying mechanism. Establishing genuine non-localizability requires showing obstruction across all reasonable proposals, not just one.

## Coverage equivalence

**Definition.** $C_1$ and $C_2$ are **coverage-equivalent** if $H^\bullet(\mathcal{F}_1) \cong H^\bullet(\mathcal{F}_2)$.

**Important caveat.** Isomorphic cohomology groups are a weak equivalence. Two cosheaves can have isomorphic cohomology while having entirely different stalks and transport maps, describing different mechanisms. Coverage equivalence does not imply that two circuit proposals are non-contradictory in any strong sense — only that they have the same cohomological *rank structure*. The stronger claim that two coverage-equivalent proposals "describe the same underlying causal structure" would require quasi-isomorphism of cosheaves (chain-level equivalence), not just cohomology-level isomorphism. The definition here is therefore a *necessary condition* for non-contradiction, not a sufficient one.

## Spectral sequences and the 2-cell augmentation

For a complex $0 \to C^0 \to C^1 \to 0$, any associated spectral sequence degenerates at $E_2$ trivially — there is no room for higher differentials. The open question about degeneration page (OQ 5.6) only becomes non-trivial if the layer graph is **augmented with 2-cells**: triangles attached wherever three sites form a circuit. With 2-cells, a $C^2$ term appears, higher cohomology becomes possible, and the spectral sequence of the filtered complex can degenerate at pages $E_r$ for $r > 2$.

Whether to augment the layer graph with 2-cells is a modeling choice. Without augmentation, $H^1$ is all there is and OQ 5.6 is trivially resolved. With augmentation, the question is genuine.

**Open question** (OQ 5.6, conditioned on 2-cell augmentation). At which page does the spectral sequence of the augmented circuit cosheaf degenerate for natural transformer mechanisms?

## Further reading

Hansen, J. and Ghrist, R. (2021). "Toward a spectral theory of cellular sheaves." *Journal of Applied and Computational Topology* 5(1): 1–55.

## See also

- [Structural view](/mechanistic-views/views/structural/) — uses cosheaf cohomology for coverage equivalence
- [Stratified view](/mechanistic-views/views/stratified/) — the $\mathcal{M}_\infty$ stratum is characterized by non-zero $H^1$
- [Gauge Quotients and Holonomy deep dive](gauge-holonomy/) — complementary gauge-invariant characterization
- [Stratification deep dive](stratification/) — spectral sequences for augmented circuit complexes
- [Localized vs. Distributed decision](/mechanistic-views/decisions/localized-vs-distributed/) — practical implications of $H^1 \neq 0$
