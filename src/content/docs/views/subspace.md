---
title: Subspace View
---

# Subspace View

The object and role views both suffer from a coordinate problem: different methods recover different circuits, and rotating the basis moves "the mechanism" to different neurons without changing the computation. The subspace view resolves this by stepping up one level of abstraction — the mechanism is not a component or a role, but a low-dimensional subspace of the residual stream.

Subspaces are coordinate-free. They don't depend on which basis you use, which means two methods that disagree about which heads matter can agree about which subspace the computation lives in. This is the key insight: method disagreement at the component level is *expected* when the underlying object is a subspace projected onto different component bases. DAS (distributed alignment search) is the primary tool — it finds the subspace where swapping activations between two inputs makes the model behave as if one causal variable changed.

The subspace view is where most of the mathematical structure in this framework begins to bite. The natural space of subspaces is the Grassmannian, which has a canonical metric (principal angles), a notion of averaging (Frechet mean), and a baseline distribution (Marchenko-Pastur). This gives the view precise, falsifiable identity criteria that the object and role views lack. The cost: it assumes the mechanism is linearly encoded, which fails for nonlinear or context-switching representations.

## Thesis

A mechanism is a subspace $S \in \mathrm{Gr}(k, d)$ such that intervening on the projection of the residual stream onto $S$ causes the model to behave as if the corresponding high-level variable had changed.

## Interventionism and the surgical intervention condition

The definition is interventionist in the sense of Woodward (2003): a causal variable is identified with the subspace $S$ such that a surgical intervention on $S$ changes the model's output in the predicted way while leaving everything else unchanged.

For this to be a genuine causal claim rather than a correlation, the intervention must be **surgical**: changing $S$ must not directly alter the values of other variables in the causal graph. In the DAS/IIA setting, the relevant test is the **IIA condition**: base-pass behavior is preserved on all variables other than the one being intervened on.

IIA is therefore not merely a measurement reliability condition. It is an empirical test bearing on the validity of the causal claim. However, low IIA has two distinct interpretations that must be distinguished:

**(A) Non-surgical intervention.** The subspace swap disturbs variables other than the claimed one — the intervention leaks into other parts of the causal graph. The intervention is not isolating the proposed variable.

**(B) Wrong causal graph.** The intervention may be perfectly surgical on the proposed variable, but the causal graph assumed by the test is incorrect — the variable being swapped is causally upstream of what is being measured, so changing it *should* change base-pass behavior of downstream variables. In this case low IIA is evidence of incorrect causal graph specification, not a non-surgical intervention.

These two interpretations produce the same IIA signal but require different responses: (A) calls for a better subspace candidate; (B) calls for revising the causal graph. IIA should be reported as a diagnostic for intervention quality and graph validity, not just as a scalar accuracy metric.

## What exists

A point on $\mathrm{Gr}(k, d)$. DAS identifies a projector $QQ^\top$ invariant under $Q \mapsto QR$ for any $R \in O(k)$ — a subspace, not a specific matrix. A mechanism also has transport structure: weight matrices induce maps between subspaces at different layers.

## Identity

Geodesic distance on $\mathrm{Gr}(k, d)$:

$$d(S_1, S_2) = \left(\sum_{i=1}^k \theta_i^2\right)^{1/2}$$

where $\theta_1, \ldots, \theta_k$ are the principal angles between $S_1$ and $S_2$, computed as $\cos\theta_i = \sigma_i(P_1 P_2)$.

## Evidence

Three independently non-injective sources:

- **Activation-space interventional**: [DAS/IIA](https://learnmechinterp.com/topics/causal-abstraction/) (with IIA as surgical-intervention test)
- **Weight-space structural**: [SVD of $W^{OV} = W^O W^V$](https://learnmechinterp.com/topics/qk-ov-circuits/), invariant subspace decomposition
- **Dynamics-space**: [AGOP](https://arxiv.org/abs/2110.04005) convergence toward the eventual DAS subspace during training

Each domain is individually non-injective on mechanism space, but the joint map is conjectured to be injective under a **general position condition** — the requirement that no pair of distinct mechanisms looks identical across all three domains simultaneously. This has not been formally verified for natural transformer mechanisms. See the [Single-Method vs. Triangulated Evidence](/mechanistic-views/decisions/single-vs-triangulated/) page for discussion.

## Formalism

[Grassmannian geometry](/mechanistic-views/formalism/grassmannian/). The **Grassmannian SCM (G-SCM)** extends Pearl's SCM with subspaces as nodes and weight-induced transport maps as edges. In principle, requiring alignment maps to respect transport structure addresses the Sutter et al. (2025) vacuity result, though the G-SCM has not yet been empirically validated on natural transformer circuits. See the [Grassmannian deep dive](/mechanistic-views/formalism/deep-dives/grassmannian/) for the full mathematical treatment.

## What it explains

How a high-level causal variable can be distributed across many neurons while remaining localized in a low-dimensional direction.

Why SAE features and DAS subspaces are not always the same object: SAE features are recovered by optimising for sparse reconstruction of activations — they are the directions that best explain activation variance with sparse codes. DAS subspaces are recovered by optimising for causal interventional consistency (IIA) — they are the directions that best predict the model's downstream behaviour under controlled swaps. A direction can explain activation variance without being causally active (e.g. a feature that is expressed but causally inert for the target task), and a direction can be causally active without being the sparsest description of the activations (e.g. a polysemantic direction). These are distinct optimisation objectives with distinct solutions in general.

## What it lets you prove

- **Convergence**: weight-space and activation-space subspaces converge on $\mathrm{Gr}(k, d)$
- **Non-vacuity** (theoretical): Sutter et al. (2025) show that for unrestricted nonlinear alignments, high IIA is achievable without genuine causal structure. Restricting to transport-respecting alignments (G-SCM) is expected to rule out these degenerate solutions, though this has not yet been empirically demonstrated on natural transformer circuits
- **Flow bounds**: $\|W^{OV}_u \cdot W^{KQ}_v\|_F$ is a distribution-free upper bound on causal information flow
- **Triangulation necessity**: each evidence domain alone is non-injective on mechanism space; convergence across domains is required for unambiguous identification

## SAE features and the subspace view

Sparse autoencoders (SAEs) have become the dominant practical method for recovering $\mathcal{M}_1$ features — single directions in the residual stream. The relationship between SAE features and subspace-view mechanisms is more subtle than it first appears.

**What SAEs recover.** An [SAE](https://learnmechinterp.com/topics/sparse-autoencoders/) trained on residual stream activations at layer $l$ learns a dictionary $D \in \mathbb{R}^{d \times n}$ ($n \gg d$) and sparse codes $a \in \mathbb{R}^n_{\geq 0}$ such that $x \approx Da$. Each column $d_i \in \mathbb{R}^d$ is a candidate feature direction — a point in $\mathrm{Gr}(1, d)$.

**The epistemological stance SAEs embed.** A feature $d_i$ is treated as real if it appears reliably in the sparse codes and has a human-interpretable activating pattern. This is a *sparse reconstruction criterion* for feature existence — a feature exists if it is needed to reconstruct the activations. This is not the same as the subspace-view *causal criterion* — a mechanism exists if intervening on the corresponding subspace changes the model's output as predicted.

**When they agree and when they don't.** A direction can be needed for sparse reconstruction without being causally active on any downstream task (a feature that is expressed but inert). A direction can be causally active without being the sparsest description of the activations (a polysemantic direction). In practice, high-IIA DAS features and SAE features often but not always identify the same directions.

**Feature splitting and polysemanticity.** As the SAE dictionary size $n$ increases, some features split into more specific ones (feature splitting). This corresponds to moving from $\mathcal{M}_k$ to $\mathcal{M}_1^n$ in the stratified view — resolving a multi-dimensional subspace into multiple one-dimensional ones. Whether the split features are genuinely distinct mechanisms or coordinate choices within the same subspace is an identity question that requires causal testing to resolve.

**Practical recommendation.** SAE features are valuable for discovering candidate $\mathcal{M}_1$ mechanisms efficiently. Treat SAE recovery as hypothesis generation. Confirm with DAS/IIA that the identified directions are causally active, not merely reconstruction-relevant. Report both the SAE-recovered direction and the IIA score; divergence between the two is informative.

## Failure modes

**Linearity.** Assumes the causal variable is linearly encoded. Nonlinear or context-switching encoding requires Riemannian geometry (as in the grokking case).

**Wrong $k$.** Too small misses the variable; too large conflates multiple variables.

**Prompt dependence.** A subspace with high IIA on one distribution may not transfer across distributions.

**Non-surgical interventions or wrong causal graph.** Low IIA has two interpretations: the intervention leaks into other variables (non-surgical), or the proposed causal graph is wrong and changing this variable should affect the measured variable (wrong graph). See the interventionism section above for how to distinguish them. High DAS accuracy does not by itself warrant the causal claim when IIA is low.

## Relationship to Mechanistic Validity

The subspace view resolves the object and role views' coordinate-dependence problems — subspaces are invariant under rotation, so convergent validity and measurement invariance become possible. It still cannot establish gauge-orbit identity or rule out alternative subspace decompositions without exhaustive search.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | — | 3/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency), [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity) | [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 3/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | — | 2/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation), [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability) | [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | — | 3/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | — | 2/5 |

**Covered** = the view's standard methods directly produce this evidence. **Possible** = testable under this view, but not standard practice. **Impossible** = the view's ontology structurally cannot satisfy this criterion.

**Why convergent validity (C5) is now covered.** Principal angles on the Grassmannian measure agreement between subspaces recovered by different methods (DAS vs. weight SVD vs. SAE directions). This is the subspace view's key advantage: method disagreement at the component level can coexist with agreement at the subspace level.

**Why measurement invariance (M2) is now covered.** Subspaces are points on $\mathrm{Gr}(k,d)$, invariant under orthogonal rotation. Changing the basis does not change the subspace. Fréchet variance across seeds quantifies stability directly on the manifold.

**Why specificity (I3) is now covered.** DAS/IIA directly tests whether the intervention is surgical — high IIA means the swap changed only the target variable. Low IIA diagnoses either non-surgical intervention or wrong causal graph.

**Why cross-architecture (E6) is only possible, not covered.** Cross-architecture geodesic distance on $\mathrm{Gr}(k,d)$ is well-defined in principle but requires matching embedding dimensions across architectures, which is non-trivial. The [structural view](/mechanistic-views/views/structural/) handles this more naturally via gauge-orbit isomorphism.

**No impossible criteria.** The subspace view has no structurally impossible criteria — every lens is at least partially addressable. Its limitations are practical (methods not yet developed or validated) rather than ontological.

## Further reading

- Geiger et al., "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations" (2024) — DAS, the primary subspace-view method
- Elhage et al., "Toy Models of Superposition" (2022) — why features may be represented in superposition, motivating the subspace rather than neuron view
- Cunningham et al., "Sparse Autoencoders Find Highly Interpretable Directions in Language Models" (2023) — SAE features as candidate $\mathrm{Gr}(1, d)$ mechanisms
- For related views: [Object view](/mechanistic-views/views/object/) (identifies mechanisms with components, not subspaces), [Role view](/mechanistic-views/views/role/) (uses subspaces as search space but role equivalence as identity), [Structural view](/mechanistic-views/views/structural/) (invariant properties of subspaces under gauge transformations)
