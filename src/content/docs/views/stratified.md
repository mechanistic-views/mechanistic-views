---
title: Stratified View
---

# Stratified View

Some mechanisms are single directions in activation space (SAE features). Some are multi-dimensional subspaces (DAS-recovered variables). Some are fully distributed across the entire residual stream and have no low-dimensional description at all. These are not the same kind of object, and they should not be evaluated by the same criteria.

The stratified view is the meta-view: it says there is no single correct answer to "what is a mechanism?" because different mechanisms live in different strata of a stratified space. A mechanism in $\mathcal{M}_1$ (a single direction) has different identity criteria, different evidence standards, and different mathematical descriptions than a mechanism in $\mathcal{M}_k$ (a $k$-dimensional subspace) or $\mathcal{M}_\infty$ (fully distributed). The other views are special cases — the object view operates in $\mathcal{M}_1$, the subspace view in $\mathcal{M}_k$, the structural view across strata via gauge invariance.

This is the highest-commitment view. It requires evidence not just that a mechanism exists, but that you have correctly identified which stratum it occupies — and different strata require different kinds of evidence. The payoff is that it explains why different methods give different answers (they are probing different strata) and why "dark matter" in circuits exists (it lives in $\mathcal{M}_\infty$, which component-level methods cannot see). The cost is that cosheaf cohomology and stratum assignment are not yet practical at scale.

## Thesis

There is no single correct description of what a mechanism is. The appropriate description, identity criterion, and evidence standard depend on which stratum the mechanism occupies.

## The strata

$$\mathcal{M} = \mathcal{M}_1 \sqcup \mathcal{M}_2 \sqcup \cdots \sqcup \mathcal{M}_d \sqcup \mathcal{M}_\infty$$

- **$\mathcal{M}_1$**: single feature direction; a point in $\mathrm{Gr}(1, d) \cong \mathbb{RP}^{d-1}$. [SAE features](https://learnmechinterp.com/topics/sparse-autoencoders/) and directional probes.
- **$\mathcal{M}_k$ for $k \geq 2$**: $k$-dimensional causal subspace; point in $\mathrm{Gr}(k,d)/\mathcal{G}$. Identified by [DAS](https://learnmechinterp.com/topics/causal-abstraction/).
- **Flag strata**: nested sequences $S_1 \subset \cdots \subset S_m$; relevant for attention patterns with hierarchical structure.
- **Nonlinear manifold strata**: mechanisms with nonlinear encoding structure within a flat [Grassmannian](/mechanistic-views/formalism/grassmannian/) stratum, e.g., the circular Fourier structure in [grokking](/mechanistic-views/cases/grokking/) (which lives in $\mathcal{M}_2$ but encodes the causal variable on $S^1 \subset \mathcal{M}_2$ rather than linearly); require Riemannian geometry on the embedded submanifold, not just Grassmannian geometry.
- **$\mathcal{M}_\infty$**: genuinely distributed mechanisms; no finite-dimensional representative. Working hypothesis (see [Stratification](/mechanistic-views/formalism/stratification/)).

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

## Evidence

- $\mathcal{M}_1$: feature direction recovery plus causal ablation
- $\mathcal{M}_k$: DAS and weight-space subspace recovery with cross-domain triangulation
- $\mathcal{M}_\infty$: $H^0 = 0$ and $H^1 \neq 0$ in the circuit cosheaf (with the caveats on the Sheaf Cohomology page)

Multi-domain triangulation applies at every stratum.

## Formalism

[Grassmannian](/mechanistic-views/formalism/grassmannian/) and flag manifolds, gauge quotients, holonomy, cellular cosheaf cohomology, spectral sequences, [Whitney stratifications](/mechanistic-views/formalism/stratification/). See the [Formalisms](/mechanistic-views/formalism/) section and the [Stratification deep dive](/mechanistic-views/formalism/deep-dives/stratification/).

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

## Relationship to Mechanistic Validity

The stratified view has the broadest validity coverage of any view — it subsumes the structural view's criteria and adds resolution-dependent evidence standards. Its unique contribution is that validity criteria themselves vary by stratum: a $\mathcal{M}_1$ mechanism requires different evidence than a $\mathcal{M}_k$ or $\mathcal{M}_\infty$ mechanism. Its limitations are practical: cosheaf cohomology is not yet computable at scale, and stratum assignment has no canonical algorithm.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity) | — | 4/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency), [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity) | [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 3/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | — | 3/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability), [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation) | [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | — | 3/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | — | 3/5 |

**Covered** = the view's standard methods directly produce this evidence. **Possible** = testable under this view, but not standard practice. **Impossible** = the view's ontology structurally cannot satisfy this criterion.

**No impossible criteria.** The stratified view inherits the structural view's full coverage and adds resolution-dependence. Every criterion is at least possible in principle. Its practical limitations are computational: cosheaf cohomology is expensive, stratum assignment is not automated, and the $\mathcal{M}_\infty$ stratum lacks the smooth structure needed for full stratification theory.

## Further reading

- The [Subspace view](/mechanistic-views/views/subspace/) and [Structural view](/mechanistic-views/views/structural/) each apply within individual strata; the stratified view is the meta-framework that organizes them
- See the [Grokking case study](/mechanistic-views/cases/grokking/) for an example of a nonlinear manifold stratum ($S^1 \subset \mathcal{M}_2$)
- The [Stratification deep dive](/mechanistic-views/formalism/deep-dives/stratification/) covers Whitney conditions, frontier condition, and Thom-Mather control data
