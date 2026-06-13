---
title: Subspace View
---

# Subspace View

The object and role views both suffer from a coordinate problem: different methods recover different circuits, and rotating the basis moves "the mechanism" to different neurons without changing the computation. The subspace view resolves this by stepping up one level of abstraction — the mechanism is not a component or a role, but a low-dimensional subspace of the residual stream.

Subspaces are coordinate-free. They don't depend on which basis you use, which means two methods that disagree about which heads matter can agree about which subspace the computation lives in. DAS (distributed alignment search) is the primary tool — it finds the subspace where swapping activations between two inputs makes the model behave as if one causal variable changed.

## Thesis

A mechanism is a subspace $S \in \mathrm{Gr}(k, d)$ such that intervening on the projection of the residual stream onto $S$ causes the model to behave as if the corresponding high-level variable had changed.

## What it explains

**Why methods disagree about components but may agree about subspaces.** Different circuit-discovery methods project the same underlying subspace onto different component bases. The disagreement at the component level is expected and does not indicate that the methods found different mechanisms — it indicates that the mechanism is more naturally described as a subspace than as a set of components.

**How a causal variable can be distributed across many neurons while remaining localized.** A $k$-dimensional subspace is low-dimensional (localized in representation space) even though it may project onto many neurons in any particular basis. Superposition is the natural state of a model packing many variables into a residual stream: each variable gets a low-dimensional subspace, and the subspaces overlap.

**Why SAE channels and DAS subspaces can disagree.** SAE channels are recovered by optimizing for sparse reconstruction of activations — the directions that best explain activation variance with sparse codes. DAS subspaces are recovered by optimizing for causal interventional consistency (IIA) — the directions that best predict downstream behavior under controlled swaps. A direction can explain activation variance without being causally active (a channel that is expressed but inert for the target task), and a direction can be causally active without being the sparsest activation description (a polysemantic direction).

## What this view says

The mechanism is a point on the Grassmannian $\mathrm{Gr}(k, d)$ — the space of $k$-dimensional linear subspaces of $\mathbb{R}^d$. DAS identifies a projector $QQ^\top$ that is invariant under $Q \mapsto QR$ for any $R \in O(k)$: a subspace, not a specific matrix. Two mechanisms are the same when they are the same point on the Grassmannian — equivalently, when their principal angles are all zero.

The Grassmannian comes with a canonical distance (principal angles), a notion of averaging (Frechet mean), and baseline distributions from random matrix theory (Marchenko-Pastur). This gives the subspace view precise, falsifiable identity criteria: you can measure how close two claimed subspaces are, whether convergence across methods is statistically significant, and whether the subspace is distinguishable from random noise.

The subspace view assumes the mechanism is linearly encoded. When that assumption fails — nonlinear or context-switching representations, curved manifolds like the [grokking](https://arxiv.org/abs/2301.05217) circle — Riemannian geometry is needed instead of Grassmannian geometry. See the [stratified view](/mechanistic-views/views/stratified/) for how linear and nonlinear subspace structure relate.

## When it works and when it doesn't

The subspace view is strongest when the causal variable is linearly encoded in the residual stream. For many known circuits — IOI, gender bias, factual recall — DAS finds subspaces with high IIA, confirming that the linear encoding assumption holds.

**Linearity.** The central assumption. When the causal variable is encoded on a curved manifold (as in grokking, where the mechanism lives on $S^1$), linear subspace methods will miss the structure. The correct metric comes from the manifold geometry, not from the Grassmannian.

**Wrong $k$.** Too small a subspace dimension misses the variable; too large conflates multiple variables. Choosing $k$ requires either cross-validation or an independent estimate of the variable's intrinsic dimension.

**Prompt dependence.** A subspace with high IIA on one distribution may not transfer across distributions. A "gender" subspace found on English biographical text may not be the same subspace in French or in dialogue.

**Non-surgical interventions or wrong causal graph.** Low IIA has two interpretations: (A) the subspace swap disturbs variables other than the claimed one (non-surgical intervention), or (B) the proposed causal graph is incorrect and changing this variable *should* affect the measured variable (wrong graph). These produce the same IIA signal but require different responses — a better subspace candidate vs. a revised causal graph.

---

## Technical details

### Identity criterion

Geodesic distance on $\mathrm{Gr}(k, d)$:

$$d(S_1, S_2) = \left(\sum_{i=1}^k \theta_i^2\right)^{1/2}$$

where $\theta_1, \ldots, \theta_k$ are the principal angles between $S_1$ and $S_2$, computed as $\cos\theta_i = \sigma_i(P_1 P_2)$.

### Evidence

Three independently non-injective sources:

- **Activation-space interventional**: [DAS/IIA](https://learnmechinterp.com/topics/causal-abstraction/) (with IIA as surgical-intervention test)
- **Weight-space structural**: [SVD of $W^{OV} = W^O W^V$](https://learnmechinterp.com/topics/qk-ov-circuits/), invariant subspace decomposition
- **Dynamics-space**: AGOP convergence toward the eventual DAS subspace during training (Radhakrishnan et al., 2024)

Each domain is individually non-injective on mechanism space, but the joint map is conjectured to be injective under a general position condition.

### Interventionism and the surgical intervention condition

The definition is interventionist in the sense of Woodward (2003): a causal variable is identified with the subspace $S$ such that a surgical intervention on $S$ changes the model's output in the predicted way while leaving everything else unchanged.

IIA is not merely a measurement reliability condition — it is an empirical test bearing on the validity of the causal claim. Low IIA has two distinct interpretations:

**(A) Non-surgical intervention.** The subspace swap disturbs variables other than the claimed one — the intervention leaks into other parts of the causal graph.

**(B) Wrong causal graph.** The intervention may be perfectly surgical, but the causal graph assumed by the test is incorrect — the variable being swapped is causally upstream of what is being measured.

IIA should be reported as a diagnostic for intervention quality and graph validity, not just as a scalar accuracy metric.

### SAE channels and the subspace view

[SAEs](https://learnmechinterp.com/topics/sparse-autoencoders/) trained on residual stream activations learn a dictionary $D \in \mathbb{R}^{d \times n}$ ($n \gg d$) and sparse codes $a \in \mathbb{R}^n_{\geq 0}$ such that $x \approx Da$. Each column $d_i$ is a candidate one-dimensional subspace — a point in $\mathrm{Gr}(1, d)$.

Whether a given SAE channel corresponds to a genuine causal variable is a separate question from whether it is needed for reconstruction. SAE recovery should be treated as hypothesis generation: confirm with DAS/IIA that identified directions are causally active, not merely reconstruction-relevant. Divergence between SAE channels and DAS subspaces is informative — it indicates that sparse reconstruction and causal structure are picking out different things.

As dictionary size $n$ increases, some channels split into more specific ones (feature splitting). Whether the split channels are genuinely distinct mechanisms or coordinate choices within the same subspace is an identity question that requires causal testing to resolve.

### What it lets you prove

- **Convergence**: weight-space and activation-space subspaces converge on $\mathrm{Gr}(k, d)$
- **Non-vacuity** (theoretical): restricting to transport-respecting alignments (G-SCM) is expected to rule out degenerate solutions (Sutter et al., 2025), though this has not yet been empirically demonstrated
- **Flow bounds**: $\|W^{OV}_u \cdot W^{KQ}_v\|_F$ is a distribution-free upper bound on causal information flow
- **Triangulation necessity**: each evidence domain alone is non-injective; convergence across domains is required for unambiguous identification

### Formalism

[Grassmannian geometry](/mechanistic-views/formalism/grassmannian/). The **Grassmannian SCM (G-SCM)** extends Pearl's SCM with subspaces as nodes and weight-induced transport maps as edges. See the [Grassmannian deep dive](/mechanistic-views/formalism/deep-dives/grassmannian/) for the full mathematical treatment.

### Relationship to Mechanistic Validity

The subspace view resolves the coordinate-dependence problems of the object and role views — subspaces are invariant under rotation, so convergent validity and measurement invariance become possible.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | — | 3/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency), [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity) | [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 3/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | — | 2/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation), [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability) | [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | — | 3/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | — | 2/5 |

**Why convergent validity (C5) is now covered.** Principal angles on the Grassmannian measure agreement between subspaces recovered by different methods (DAS vs. weight SVD vs. SAE directions). Method disagreement at the component level can coexist with agreement at the subspace level.

**Why measurement invariance (M2) is now covered.** Subspaces are points on $\mathrm{Gr}(k,d)$, invariant under orthogonal rotation. Frechet variance across seeds quantifies stability directly on the manifold.

**No impossible criteria.** Every lens is at least partially addressable. The subspace view's limitations are practical (methods not yet developed) rather than ontological.

### Further reading

- Geiger et al., "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations" (2024) — DAS, the primary subspace-view method
- Elhage et al., "Toy Models of Superposition" (2022) — why representations may be in superposition, motivating the subspace view
- Cunningham et al., "Sparse Autoencoders Find Highly Interpretable Directions in Language Models" (2023) — SAE channels as candidate $\mathrm{Gr}(1, d)$ mechanisms
- For related views: [Object view](/mechanistic-views/views/object/) (identifies mechanisms with components), [Role view](/mechanistic-views/views/role/) (role equivalence as identity), [Structural view](/mechanistic-views/views/structural/) (invariant properties under gauge transformations)
