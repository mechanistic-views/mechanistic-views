---
title: Structural View
---

# Structural View

You can permute the heads of a transformer, rotate the residual stream basis, and rescale the weights — and the model computes exactly the same function. These are gauge symmetries: transformations that change the parameterization without changing the computation. The structural view says: the mechanism is whatever is invariant under these transformations. Everything else is artifact.

## Thesis

A mechanism is an equivalence class under gauge symmetry: all weight configurations that implement the same input-output function are the same mechanism.

## What it explains

**Why different methods can find different circuits that are all "correct."** If ACDC and EAP recover different component sets for the same task, the structural view asks: are these component sets related by a gauge transformation? If so, they are different descriptions of the same mechanism, not different mechanisms. Circuit disagreement is expected when the identity criterion is the gauge orbit, not the specific circuit.

**Cross-architecture identity.** Two models implement the same mechanism if their gauge orbits are isomorphic — no need to match specific heads. Head 9.1 in GPT-2 and whatever implements the same function in Llama can be identified as "the same mechanism" without requiring them to be the same component.

**Why the parameterization is not the mechanism.** A neuron may look special because of how the weights happen to be arranged, not because it is doing something computationally special. The structural view makes this distinction precise: anything that changes under a symmetry transformation is a property of the parameterization; anything that doesn't is a property of the mechanism.

## What this view says

A **gauge orbit** is the set of all weight configurations related to each other by function-preserving transformations. Think of it this way: if you take a trained transformer and permute its heads, rotate its residual stream basis, and rescale its weights in any way that preserves the input-output mapping, every configuration you can reach by doing this is in the same gauge orbit as the original. All these configurations compute exactly the same function — they differ only in how that function happens to be written down in the weights. The gauge orbit IS the mechanism: it captures everything about the computation while stripping away the arbitrary choices of how to parameterize it.

Two mechanisms are the same when they lie in the same gauge orbit. This resolves the alternative-exclusion problem that plagues the object view: if two component sets are gauge-equivalent, they are not alternative explanations — they are the same explanation expressed in different coordinates.

The structural view also uses **holonomy** — what happens when you transport a subspace through the network along a closed loop of weight matrices. If the subspace comes back rotated, that rotation (the holonomy) is a gauge-invariant fingerprint characterizing the mechanism. Two mechanisms with different holonomy groups are provably different, regardless of how their components are arranged.

The view's objects also include **cosheaf cohomology classes** — topological invariants that track whether a mechanism can be decomposed into locally consistent pieces. When the cohomology is nontrivial ($H^1 \neq 0$), the mechanism has genuinely distributed structure that no local circuit description captures.

This is the strongest static realist position. It resolves nearly every problem the lower views face: cross-architecture identity, convergent validity, alternative exclusion, measurement invariance. The cost is computational. Holonomy, cosheaf cohomology, and gauge-orbit comparison are hard to compute at scale. The view also requires specifying the right symmetry group — LayerNorm breaks the full rotation symmetry, and using the wrong gauge group produces wrong identity judgments. In practice, the structural view is more of a theoretical ceiling than a practical toolkit: it tells you what the right answer looks like, even when you can't compute it yet.

## When it works and when it doesn't

The structural view is strongest when you need cross-architecture comparison, when you need to resolve apparent circuit disagreements, or when you need to prove that two descriptions are actually the same mechanism.

**Computability.** The main limitation. Computing holonomy requires specifying a connection; computing cosheaf cohomology requires specifying base sections and a linearization. Both are expensive at scale.

**Wrong symmetry group.** LayerNorm breaks the full $O(d)$ rotation symmetry. The gauge group for a real transformer is more restricted than $O(d)$, and using the wrong group produces incorrect identity judgments. The correct gauge group for a given architecture must be determined empirically.

**Over-abstraction.** Too coarse an invariant conflates distinct mechanisms. Cohomology class is coarser than gauge orbit — different gauge orbits can have isomorphic cohomology. Using the wrong level of invariant loses real distinctions.

**No dynamics.** The structural view characterizes what the mechanism IS at a given checkpoint, not how it formed or why. For questions about training dynamics, phase transitions, or developmental prerequisites, the [process view](/mechanistic-views/views/process/) is needed.

---

## Technical details

### Identity criterion

Two mechanisms are the same when they lie in the same gauge orbit. Isomorphic holonomy groups are a necessary but not sufficient condition. Same cohomological equivalence class is a coarser criterion than same gauge orbit.

### The qua-problem

Why gauge orbits rather than component overlap, behavioral equivalence, or cohomology class? The argument is functional: gauge transformations preserve the input-output function exactly. Any property distinguishing two configurations in the same orbit is a property of the parameterization, not of the computation.

Behavioral equivalence is coarser: two mechanisms can compute differently but have the same output distribution. Cohomology class is also coarser: different gauge orbits can have isomorphic cohomology. The gauge orbit is finer than both and therefore the right choice when the claim is about computational identity.

### Evidence

- **Gauge-invariant measurements**: singular values of [OV circuits](https://learnmechinterp.com/topics/qk-ov-circuits/) $W^{OV}$, principal angles, effective rank — invariant under both head permutations and (approximate) orthogonal rotations. [Composition scores](https://learnmechinterp.com/topics/composition-and-virtual-heads/) $\|W^{OV}_u \cdot W^{KQ}_v\|_F$ are invariant under head permutations but not under the orthogonal rotation symmetry; they are gauge-invariant only with respect to the permutation subgroup
- **Holonomy**: estimates of the holonomy group (connection must be specified)
- **Cohomological tests**: $H^0$ and $H^1$ of the circuit cosheaf

### What it lets you prove

- **Gauge-invariant identity**: same gauge orbit implies same mechanism
- **Holonomy as necessary condition**: same mechanism implies isomorphic holonomy groups
- **Cohomological localizability**: relative to the cosheaf construction and base sections

### Formalism

[Fiber bundle quotient](/mechanistic-views/formalism/fiber-bundle-quotient/) $\mathcal{W}/\mathcal{G}$, principal fiber bundles, parallel transport, holonomy, cellular cosheaf cohomology. See the [Gauge and Holonomy](/mechanistic-views/formalism/deep-dives/gauge-holonomy/) and [Sheaf Cohomology](/mechanistic-views/formalism/deep-dives/sheaves/) deep dives.

### Relationship to Mechanistic Validity

The structural view has the broadest validity coverage of any static view — gauge invariance gives it measurement invariance, cross-architecture identity, and convergent validity by construction.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity) | — | 4/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency), [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity) | [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 3/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | — | 3/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation), [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability) | [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | — | 3/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | — | 3/5 |

**Why alternative exclusion (V4) is now covered.** If two component sets are in the same gauge orbit, they are the same mechanism by definition. Alternatives related by symmetry are not alternatives.

**Why minimality (C4) is now covered.** Cosheaf cohomology provides a formal criterion for minimality: the circuit is minimal when removing any edge changes the cohomology class.

**No impossible criteria.** All limitations are computational (holonomy, cohomology, gauge-orbit comparison are expensive) rather than ontological.

### Further reading

- Elhage et al., "A Mathematical Framework for Transformer Circuits" (2021) — composition scores and QK/OV decomposition as weight-space invariants
- Ainsworth et al., "Git Re-Basin: Merging Models modulo Permutation Symmetries" (2023) — permutation gauge symmetry in neural networks
- For related views: [Object view](/mechanistic-views/views/object/) (identifies mechanisms with components, not invariants), [Subspace view](/mechanistic-views/views/subspace/) (Grassmannian points, a related geometric object)
