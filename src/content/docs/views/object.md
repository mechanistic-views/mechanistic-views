---
title: Object View
---

# Object View

The object view is the default stance in most interpretability work today. When someone says "head 9.1 is a name mover" or "this SAE feature fires on French text," they are making an object-view claim: the mechanism is a specific, concrete part of the network, and you study it by poking at it — ablating it, patching it, measuring what happens when it's gone.

This is the simplest realist position. It says mechanisms are real things you can point to: this head, that neuron, these edges in a circuit graph. The evidence is causal and direct — remove the component, see if the behavior breaks. Most circuit discovery work (ACDC, activation patching, EAP) operates in this view, producing directed graphs of components as output.

The object view works well when computation is sparse and localized. It breaks down when mechanisms are distributed across many components, when backup circuits mask ablation effects, or when the "important component" is an artifact of the coordinate system rather than a genuine computational unit. When these failures dominate, the [subspace](/mechanistic-views/views/subspace/) or [structural](/mechanistic-views/views/structural/) views may be more appropriate. But for much of the field's current practice — finding circuits, characterizing heads, interpreting SAE features — the object view is where the work lives.

## Thesis

A mechanism is a localized object or collection of objects whose activity or weights are responsible for a target behavior.

## What exists

Architectural or learned units: heads, neurons, [SAE features](https://learnmechinterp.com/topics/sparse-autoencoders/). The view is strongest when the relevant computation is sparse, stable across prompts and seeds, and concentrated in a small number of components.

## Identity

Two mechanisms are the same when they share the same relevant parts, or when their parts are functionally interchangeable under a well-specified criterion.

## Evidence

Intervention on the proposed component:
- [Ablation](https://learnmechinterp.com/topics/activation-patching/) and mean-ablation (necessity — removing component destroys behavior)
- [Activation patching](https://learnmechinterp.com/topics/activation-patching/) (replacing a component's activations from one forward pass into another; tests whether the source-pass behavior is sufficient to cause target-pass output change)
- [Path patching](https://learnmechinterp.com/topics/activation-patching/#path-patching) (tests specific information-flow paths; note this is also used under the role view for path-level role attribution, not just component-level testing)
- Scaling tests (partially ablating a component to check whether the effect is graded, not just on/off)
- Minimal sufficiency tests (finding the smallest component set that still produces the behavior)

A claim is stronger when independent intervention protocols converge on the same component set.

## Formalism

[Directed graph](/mechanistic-views/formalism/directed-graph/) or set-theoretic circuit description. Standard causal graphs (Pearl, 2009) apply directly. Circuit discovery methods like [ACDC](https://learnmechinterp.com/topics/attribution-patching/), [activation patching](https://learnmechinterp.com/topics/activation-patching/), and [EAP](https://learnmechinterp.com/topics/attribution-patching/) all produce directed graphs as output.

## What it explains

Causal-mechanical explanations: which parts matter, and how changing them changes behavior.

## What it lets you prove

- **Necessity**: removing the component destroys the target behavior
- **Sufficiency**: transplanting the component is sufficient to produce the behavior
- **Minimality**: no proper subset suffices
- **Circuit recovery**: under the object view, edge recovery achieves high precision and recall when mechanisms are genuinely sparse and localized — the prerequisite for component-level circuit description. If a role partition is required to achieve high precision/recall, this indicates the role view is more appropriate (see [Role View](role/))

## Semantics of object-view claims

The claim "head 4.4 implements name-moving" should be read as a *dispositional* claim, not a categorical one. It means: head 4.4 reliably activates in name-moving contexts *and* its ablation impairs name-moving performance. It does not mean the head is in some intrinsic state of "name-moving-ness" independent of the context. The two conditions together establish a bi-directional dependency that is the nearest practical analogue to constitutive relevance.

This matters because the purely correlational reading ("head 4.4 is active when name-moving occurs") is much weaker and does not support causal claims. The dispositional reading requires both the observational condition (activation pattern) and the interventional condition (ablation effect). A claim that cites only one of these is underdetermined: high activation without ablation evidence might reflect correlation with a correlated variable; ablation evidence without activation evidence might reflect indirect effects.

## Failure modes

**Distributed mechanisms.** If computation is distributed, no single object will be both necessary and sufficient.

**Coordinate artifacts.** A neuron may look privileged because of parameterization, not because computation is intrinsically localized there. Rotating the basis can move the apparent mechanism without changing the function. When this is the primary concern, the [subspace view](/mechanistic-views/views/subspace/) or [structural view](/mechanistic-views/views/structural/) may be more appropriate.

**Backup circuits.** Ablating one component may not impair behavior because a backup engages, producing false negatives for necessity.

## Relationship to Mechanistic Validity

The object view gives you strong causal evidence — ablation tests necessity, patching tests sufficiency — but it cannot establish cross-architecture identity, measurement invariance, or coordinate-independent convergence. These are not gaps in practice; they are structural limitations of identifying mechanisms with specific components.

Validity profile against the 27 [Mechanistic Validity](https://mechanistic-validity.github.io/mechanistic-validity/) criteria:

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability) | [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | 1/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency) | [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity), [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 2/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | 1/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation) | [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability), [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance) | 1/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | 1/5 |

**Covered** = the view's standard methods directly produce this evidence. **Possible** = testable under this view, but not standard practice. **Impossible** = the view's ontology structurally cannot satisfy this criterion.

**Why convergent validity (C5) is impossible.** Different circuit-discovery methods (ACDC, EAP, activation patching) recover different component sets for the same task. Under the object view, this is method disagreement. Under the [subspace view](/mechanistic-views/views/subspace/), it is expected — each method projects the same underlying subspace onto a different component basis — and convergence can be measured via principal angles on the Grassmannian.

**Why cross-architecture (E6) is impossible.** Head 9.1 in GPT-2 does not exist in Llama. Component identity cannot cross architectures. The [role view](/mechanistic-views/views/role/) can express "same role, different components" via role equivalence; the [structural view](/mechanistic-views/views/structural/) can express it via gauge-orbit isomorphism.

**Why measurement invariance (M2) is impossible.** Components are coordinate-dependent: rotating the basis moves "the mechanism" to different neurons without changing the computation. The [subspace view](/mechanistic-views/views/subspace/) resolves this because subspaces are invariant under rotation.

**Why alternative exclusion (V4) is impossible.** The object view cannot rule out that a completely different component set implements the same behavior equally well. Exhaustive search over all possible subsets is intractable. The [structural view](/mechanistic-views/views/structural/) addresses this by identifying mechanisms with gauge orbits — if two component sets are in the same orbit, they are the same mechanism by definition.

For [Tier 3 evidence](/mechanistic-views/mechval-interface/#minimal-triangulation-for-tier-3) under the object view, Mechanistic Validity requires convergent evidence from at least two independent domains.

## Further reading

- Elhage et al., "A Mathematical Framework for Transformer Circuits" (2021) — foundational circuits work using the object view
- Wang et al., "Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small" (2022) — the canonical IOI circuit, see [IOI case study](/mechanistic-views/cases/ioi/)
- Conmy et al., "Towards Automated Circuit Discovery for Mechanistic Interpretability" (2023) — ACDC, automated circuit discovery producing directed graphs
- For related views: [Role view](/mechanistic-views/views/role/) (abstracts away from specific components), [Subspace view](/mechanistic-views/views/subspace/) (replaces components with subspaces), [Structural view](/mechanistic-views/views/structural/) (identifies mechanisms with gauge orbits rather than component sets)
