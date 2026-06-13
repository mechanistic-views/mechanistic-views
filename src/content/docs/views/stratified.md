---
title: Stratified View
---

# Stratified View

Some mechanisms are single directions. Some are multi-dimensional subspaces. Some are curved manifolds. Some are distributed across the entire residual stream with no finite-dimensional description. These are not the same kind of object, and treating them as if they were is where a large class of interpretability confusions come from.

The stratified view is the meta-view. It says there is no single correct answer to "what is a mechanism?" because different mechanisms live in different geometric types — different *strata* of a structured space. The other views each describe one kind of mechanism well: the [object view](/mechanistic-views/views/object/) handles localized components, the [subspace view](/mechanistic-views/views/subspace/) handles linear subspaces, the [structural view](/mechanistic-views/views/structural/) handles gauge-invariant structure. The stratified view organizes these into a hierarchy and says: the first job of any mechanistic analysis is to figure out what kind of object you're looking at, because the right methods, metrics, and evidence standards all depend on the answer.

## Thesis

Mechanisms come in different geometric types. The type determines the correct methods, metrics, identity criteria, and evidence standards. Different interpretability methods are coordinate charts on a stratified mechanism space — method disagreement is often chart disagreement, not empirical disagreement.

## The strata

The space of mechanisms is not a flat list but a nested filtration — each stratum includes the ones below it as limiting cases. A curved manifold mechanism is "approximately linear" near its center. A distributed mechanism may have a locally consistent approximation in some regions. Stratum assignment is a question of resolution: at what zoom level does the mechanism's specific geometric character become the leading-order description?

- **Directions ($\mathcal{M}_1$):** Single directions in the residual stream (the main vector that flows through the transformer, read and written by each layer). SAE-recovered (sparse autoencoder) channels and directional probes. The simplest and most common type. Identity: angular distance between directions.

- **Linear subspaces ($\mathcal{M}_k$):** $k$-dimensional causal subspaces. Identified by DAS (distributed alignment search — a method that finds subspaces where swapping activations reproduces causal effects). The mechanism is a point on the Grassmannian $\mathrm{Gr}(k,d)$ — the space of all $k$-dimensional linear subspaces of $\mathbb{R}^d$ — invariant under orthogonal rotation within the subspace. Identity: principal angles (the canonical set of angles measuring the difference between two subspaces).

- **Flags:** Nested sequences of subspaces $S_1 \subset \cdots \subset S_m$. Relevant for hierarchical attention patterns where query/key structure refines value subspaces at multiple resolution levels.

- **Curved manifolds ($\mathcal{M}_\Sigma$):** Mechanisms with nonlinear encoding structure. The grokking circle ($S^1$), concept manifolds in LLMs. Linear methods fail here — the correct metric comes from pulling back the behavioral output metric to the activation manifold. Recent work on manifold steering suggests that geodesic interventions along curved manifolds can outperform linear steering.

- **Fiber bundles ($\mathcal{M}_\Phi$):** Mechanisms where the neural implementation of a concept varies systematically with context. Polysemanticity is nontrivial holonomy — the rotation a direction accumulates when you trace it through different contexts, so that its "meaning" twists depending on where you look. Emerging and largely theoretical.

- **Distributed ($\mathcal{M}_D$):** Mechanisms that cannot be decomposed into locally consistent pieces. Dark matter in circuits. When local circuit descriptions fail to glue into a global account, there is a genuine distributed mechanism that no finite set of components captures.

## Methods as charts

The most important idea in the stratified view: different interpretability methods are *coordinate charts* on mechanism space. Each chart gives a local, partial, coordinate-dependent view.

SAEs (sparse autoencoders) chart $\mathcal{M}_1$ — they find directions that explain activation variance with sparse codes. DAS charts $\mathcal{M}_k$ — it finds subspaces where interchange interventions reproduce causal effects. Circuit discovery methods (ACDC, EAP, activation patching) chart the component space of the [object view](/mechanistic-views/views/object/). Manifold steering charts $\mathcal{M}_\Sigma$ — it finds curved paths along which interventions produce smooth behavioral changes.

When two methods disagree about "the mechanism," the first question is: are they charting the same stratum? If an SAE decomposes a 3-dimensional subspace into multiple 1-dimensional features, it is not wrong — it is projecting an $\mathcal{M}_k$ mechanism into $\mathcal{M}_1$ coordinates, which necessarily fragments the picture. The *dilution ratio* (number of SAE features per intrinsic dimension) quantifies this fragmentation.

When two methods *do* agree — when DAS and weight-space SVD converge on the same Grassmannian point, or when multiple SAE architectures find the same directions — that convergence is evidence that something real and method-independent is being tracked. Convergence across charts is the strongest evidence the stratified view recognizes.

## What it explains

**Why methods disagree.** Not because some are wrong, but because they chart different strata. SAEs and DAS disagreeing about "the IOI mechanism" may reflect SAEs projecting a multi-dimensional subspace into multiple directions — a chart mismatch, not an empirical contradiction.

**Why dark matter exists in circuits.** Mechanisms in $\mathcal{M}_D$ have no finite-dimensional representative. Component-level methods structurally cannot see them. The dark matter gap is not a measurement failure — it is a stratum mismatch between the method's chart and the mechanism's geometry.

**Why the Linear Representation Hypothesis works but misleads.** Many mechanisms are approximately linear (low distortion ratio), making $\mathcal{M}_1$ tools work well enough in practice. But the mechanisms where linearity breaks are exactly where interventions go wrong — curved manifolds require geodesic steering, and the error from ignoring curvature is quantifiable.

**The Sutter vacuousness problem.** Arbitrary nonlinear alignment maps make causal abstraction vacuous — any model can be mapped to any algorithm with 100% IIA (interchange intervention accuracy) (Sutter et al., 2025). The stratified view offers a resolution: unrestricted maps can permute strata freely, destroying geometric structure. Restricting to *stratum-preserving maps* — linear for $\mathcal{M}_k$, smooth with bounded curvature for $\mathcal{M}_\Sigma$, bundle morphisms for $\mathcal{M}_\Phi$ — should restore non-vacuousness. This is the stratified view's most distinctive theoretical prediction, but it remains an untested conjecture.

**Level misalignment.** The most common error in MI papers: claiming algorithmic-level understanding from implementational-level evidence. The docstring variable-binding circuit is the canonical example — the implementational evidence (specific heads attend from docstring to function positions) is solid, but the algorithmic claim (variable binding rather than positional copying) is underdetermined by that evidence. The stratified view makes this visible by requiring that evidence and claims live at the same level.

## The genuine competitor: perspectivalism

The [perspectival view](/mechanistic-views/views/perspectival/) is the only view that cannot be absorbed into the stratified account. The stratified view makes a realist commitment: there are facts about which geometric type a mechanism is, independent of how you measure it. Perspectivalism denies this — it says the "mechanism" looks different from different methods, and there is no method-independent ground truth.

The evidence bears on this debate directly. When independent methods with non-overlapping assumptions converge on the same geometric object (as in grokking, where weight decomposition, activation probing, and training dynamics all identify the same Fourier structure), that convergence is evidence against perspectivalism. When methods persistently diverge (as in IOI under different ablation methods), perspectivalism gains ground.

The stratified view predicts: methods converge when evidence is collected at the right stratum, and diverge when it is not. Perspectivalism predicts divergence as the baseline. This would be a testable distinction if stratum assignment were independent of the convergence outcome — a caveat the Duhem-Quine problem below makes concrete.

## When it works and when it doesn't

The stratified view is strongest when methods disagree and you need to understand why, when the mechanism might not be linear, when you need to choose between competing methods, or when safety analysis requires knowing what kind of structure to look for.

It struggles with stratum assignment — there is no canonical algorithm for determining which stratum a mechanism occupies. Three diagnostics exist (distortion ratio, dilution ratio, sheaf inconsistency score), but their thresholds are empirical, not principled. The higher strata ($\mathcal{M}_\Phi$, $\mathcal{M}_D$) are computationally expensive to work with and largely untested on real LLMs. And the Duhem-Quine problem (the observation that a failed prediction can always be blamed on auxiliary assumptions rather than the core hypothesis) haunts every prediction: if a hypothesis fails, "we assigned the wrong stratum" is always available as an escape. The fix is pre-registered stratum assignments from independent diagnostics before running behavioral tests.

---

## Technical details

### Stratum assignment diagnostics

Three computable diagnostics exist, none with principled thresholds yet:

- **Distortion ratio** $R = d_\text{geo}/d_\text{Euc}$ (Curveball Steering). $R \approx 1$ means locally Euclidean ($\mathcal{M}_k$ or $\mathcal{M}_1$). $R \gg 1$ means substantial curvature ($\mathcal{M}_\Sigma$).
- **Dilution ratio** $N_\text{features}/k_\text{intrinsic}$ (concept manifold analysis). High dilution means an SAE needs far more features than the mechanism's intrinsic dimension — evidence of $\mathcal{M}_\Sigma$, not $\mathcal{M}_1$.
- **EICS score** (sheaf inconsistency from local Jacobians). High inconsistency means local circuit descriptions fail to glue — evidence of $\mathcal{M}_D$.

Deriving null distributions from random matrix theory is the most important missing piece for statistical validity. Without knowing what these metrics look like under the null (random/structureless activations), the diagnostics are descriptive statistics, not hypothesis tests.

### Evidence

- $\mathcal{M}_1$: feature direction recovery plus causal ablation
- $\mathcal{M}_k$: DAS/IIA with cross-domain triangulation (weight-space SVD, AGOP)
- $\mathcal{M}_\Sigma$: manifold steering outperforms linear steering; distortion ratio $R \gg 1$
- $\mathcal{M}_\Phi$: contextuality index from holonomy computation; polysemanticity patterns
- $\mathcal{M}_D$: $H^0 = 0$ and $H^1 \neq 0$ in the circuit cosheaf

Multi-domain triangulation applies at every stratum.

### Formalisms

The stratified view can be expressed through multiple competing mathematical frameworks — this view does not have a single canonical formalism:

- **[Whitney stratification](/mechanistic-views/formalism/stratification/)** — mechanism space decomposes into smooth manifold pieces satisfying frontier conditions. Thom-Mather retractions give well-defined coarse-graining between strata. Mathematically precise; not yet verified for mechanism strata specifically.
- **Filtered categories** — strata as a nested filtration rather than discrete bins. More honest about the continuity between geometric types.
- **Atlas / coordinate charts** — methods as charts on mechanism space; stratification shows up in chart transition maps. The most intuitive formalism for practitioners.
- **[Grassmannian geometry](/mechanistic-views/formalism/grassmannian/)** — for the linear strata specifically. Principal angles, $O(k)$ gauge freedom, Frechet statistics.
- **[Sheaf cohomology](/mechanistic-views/formalism/deep-dives/sheaves/)** — for the distributed stratum. EICS score, $H^1$ as dark matter obstruction.
- **Information geometry** — for curved strata. Chentsov's uniqueness theorem (Fisher metric is the only statistically invariant Riemannian metric) provides the canonical behavioral metric; the pullback to activation space gives the metric on $\mathcal{M}_\Sigma$.

See the [Formalisms](/mechanistic-views/formalism/) section and the [Stratification deep dive](/mechanistic-views/formalism/deep-dives/stratification/).

### Falsifiable predictions

The strongest predictions the stratified view generates:

- **Grokking stratum transition:** The Grassmannian distance from pre-grokking to post-grokking representation should be significantly larger than zero, and the distortion ratio should increase post-grokking. Testable on existing checkpoints.
- **Linear steering degrades with curvature:** The advantage of manifold/geodesic steering over linear steering should increase monotonically with distortion ratio $R$. Testable with existing codebases (Curveball, Manifold Steering).
- **Pullback metric sufficiency:** Two mechanisms with identical behavioral output distributions should be at the same Grassmannian point. If two mechanisms produce identical outputs but live at different Grassmannian positions, the core identity criterion is wrong. The strongest single falsifier of the entire framework.
- **SAE dilution predicts failure:** For concepts with dilution ratio $> 10$ (fragmented SAE coverage of a manifold), the faithfulness of SAE-based explanations should be significantly lower than for concepts with dilution ratio $< 2$.

### Relationship to Mechanistic Validity

The stratified view addresses the most validity criteria — it inherits the structural view's criteria and adds resolution-dependent evidence standards. Its unique contribution is that validity criteria themselves vary by stratum: an $\mathcal{M}_1$ mechanism requires different evidence than an $\mathcal{M}_k$ or $\mathcal{M}_D$ mechanism. Its limitations are practical: cosheaf cohomology is not yet computable at scale, and stratum assignment has no canonical algorithm.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity) | — | 4/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency), [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity) | [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 3/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | — | 3/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability), [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation) | [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | — | 3/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | — | 3/5 |

**No impossible criteria.** The stratified view inherits the structural view's full coverage and adds resolution-dependence. Every criterion is at least possible in principle. Its practical limitations are computational: cosheaf cohomology is expensive, stratum assignment is not automated, and the $\mathcal{M}_D$ stratum lacks the smooth structure needed for full stratification theory.

### Further reading

- The [Subspace view](/mechanistic-views/views/subspace/) and [Structural view](/mechanistic-views/views/structural/) each apply within individual strata; the stratified view organizes them into a hierarchy
- The [Stratification deep dive](/mechanistic-views/formalism/deep-dives/stratification/) covers Whitney conditions, frontier conditions, and Thom-Mather control data
- Sutter et al. (2025) — the vacuousness result that motivates stratum-preserving alignment maps
- See the [Formalisms](/mechanistic-views/formalism/) section for the mathematical frameworks that express this view
