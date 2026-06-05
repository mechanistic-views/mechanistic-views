---
title: Stratified View
---

# Stratified View

The stratified view treats mechanism space as a stratified space. A mechanism's nature — what it is, how it is individuated, what evidence identifies it — depends on which stratum of mechanism space it occupies.

## Thesis

There is no single correct description of what a mechanism is. The appropriate description, identity criterion, and evidence standard depend on which stratum the mechanism occupies.

## The strata

$$\mathcal{M} = \mathcal{M}_1 \sqcup \mathcal{M}_2 \sqcup \cdots \sqcup \mathcal{M}_d \sqcup \mathcal{M}_\infty$$

- **$\mathcal{M}_1$**: single feature direction; a point in $\mathrm{Gr}(1, d) \cong \mathbb{RP}^{d-1}$. SAE features and directional probes.
- **$\mathcal{M}_k$ for $k \geq 2$**: $k$-dimensional causal subspace; point in $\mathrm{Gr}(k,d)/\mathcal{G}$.
- **Flag strata**: nested sequences $S_1 \subset \cdots \subset S_m$; relevant for attention patterns with hierarchical structure.
- **Nonlinear manifold strata**: mechanisms with nonlinear encoding structure within a flat Grassmannian stratum, e.g., the circular Fourier structure in grokking (which lives in $\mathcal{M}_2$ but encodes the causal variable on $S^1 \subset \mathcal{M}_2$ rather than linearly); require Riemannian geometry on the embedded submanifold, not just Grassmannian geometry.
- **$\mathcal{M}_\infty$**: genuinely distributed mechanisms; no finite-dimensional representative. Working hypothesis (see [Stratification](/formalism/stratification/)).

## What exists

A pluralist ontology. A model may contain mechanisms at several strata simultaneously, and none is more real than the others.

## Identity

| Stratum | Identity criterion |
|---|---|
| $\mathcal{M}_1$ | Geodesic distance on $\mathrm{Gr}(1,d)$ |
| $\mathcal{M}_k$ | Geodesic distance on $\mathrm{Gr}(k,d)$ |
| Flag | Distance on flag manifold |
| Nonlinear manifold | Riemannian distance on the manifold |
| $\mathcal{M}_\infty$ | Cosheaf quasi-isomorphism (necessary condition: $H^\bullet(\mathcal{F}_1) \cong H^\bullet(\mathcal{F}_2)$; sufficient condition requires chain-level equivalence) |

Applying the wrong criterion across strata produces incorrect conclusions.

## Evidence by stratum

- $\mathcal{M}_1$: feature direction recovery plus causal ablation
- $\mathcal{M}_k$: DAS and weight-space subspace recovery with cross-domain triangulation
- $\mathcal{M}_\infty$: $H^0 = 0$ and $H^1 \neq 0$ in the circuit cosheaf (with the caveats on the Sheaf Cohomology page)

Multi-domain triangulation applies at every stratum.

## Formalism

Grassmannian and flag manifolds, gauge quotients, holonomy, cellular cosheaf cohomology, spectral sequences, Whitney stratifications. See the [Formalisms](/formalism/index/) section.

## What it explains

Why different methods can simultaneously be partly right. Circuit diagrams capture $\mathcal{M}_k$ components. Cosheaf analysis captures $\mathcal{M}_\infty$ components. The dark matter gap may correspond to $\mathcal{M}_\infty$ contributions.

## What it lets you prove

- **Conditional theorems**: under the assumption that the mechanism is in $\mathcal{M}_k$, specific identity and evidence criteria follow
- **Cohomological localizability**: from the circuit cosheaf (subject to open conditions)
- **Dark matter as $H^1$** (conjecture): relationship between dark matter ratio and first cohomology

## Failure modes

**Overhead without payoff.** Cosheaf cohomology is useful only when it is computable. Not yet practical at scale.

**Wrong stratum assignment.** No canonical algorithm. Incorrect assignment produces incorrect identity criteria and incorrect conclusions.

**$\mathcal{M}_\infty$ is a working hypothesis.** The Whitney stratification is established for the finite strata; $\mathcal{M}_\infty$ lacks the smooth structure required for full stratification theory.

## Physics reading: renormalization group analogy

For readers from physics: the stratification of mechanism space has a structural analogy to the renormalization group (RG). In RG, different degrees of freedom matter at different length/energy scales — a coarse-graining operation maps a theory at one scale to an effective theory at a lower scale. The fixed points of the RG flow correspond to scale-invariant theories.

In the stratified view, different strata correspond to different resolution levels of mechanistic description: $\mathcal{M}_1$ (single-direction features) is the coarsest description; $\mathcal{M}_k$ for large $k$ is finer; $\mathcal{M}_\infty$ (distributed) is the finest. The Thom-Mather retraction $\pi_k: T_k \to \mathcal{M}_k$ is analogous to a coarse-graining map: it approximates a mechanism in the neighborhood of a stratum boundary by its best lower-dimensional description.

The analogy is structural, not literal. There is no Hamiltonian, no partition function, and no notion of energy scale. But the intuition — that what a mechanism "is" depends on the resolution at which you look — carries over directly. A mechanism that looks like a single feature from one measurement procedure may resolve into a 3-dimensional subspace under finer analysis, just as a coarse-grained field theory reveals constituent degrees of freedom at higher energy.

## Relationship to MechVal

Allows MechVal evidence standards to vary by mechanism type. The stratum assignment is an input to the MechVal audit.
