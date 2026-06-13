---
title: Structural View
---

# Structural View

You can permute the heads of a transformer, rotate the residual stream basis, and rescale the weights — and the model computes exactly the same function. These are gauge symmetries: transformations that change the parameterization without changing the computation. The structural view says: the mechanism is whatever is invariant under these transformations. Everything else is artifact.

This is the strongest static realist position. It resolves nearly every problem the lower views face. Cross-architecture identity? Two models implement the same mechanism if their gauge orbits are isomorphic — no need to match specific heads. Convergent validity? Different methods recovering different circuits is expected if the circuits are in the same gauge orbit. Alternative exclusion? If two component sets are gauge-equivalent, they are the same mechanism by definition.

The cost is computational. Holonomy, cosheaf cohomology, and gauge-orbit comparison are hard to compute at scale. The view also requires specifying the right symmetry group — LayerNorm breaks the full rotation symmetry, and using the wrong gauge group produces wrong identity judgments. In practice, the structural view is more of a theoretical ceiling than a practical toolkit: it tells you what the right answer looks like, even when you can't compute it yet.

## Thesis

A mechanism is an equivalence class: the gauge orbit of all weight configurations that implement the same input-output function. The phrase 'same way' does not add content here — gauge equivalence captures functional identity, not procedural similarity.

## The qua-problem and the justification for gauge orbits

The structural view must answer why the gauge orbit is the right identity criterion rather than, say, component overlap, behavioral equivalence, or cohomology class. This is a version of the *qua-problem*: head-4.4 is the same *qua* gauge orbit as head-7.2 in another model, but different *qua* component index. Any identity claim is implicitly relative to a description level.

The argument for gauge orbits is functional: gauge transformations preserve the input-output function exactly. Two configurations in the same orbit compute the same thing. Any property distinguishing them is a property of the parameterization, not of the computation. If the goal is to characterize computational structure, the gauge orbit is the minimal equivalence class eliminating purely representational variation.

This presupposes that the goal is characterizing computation rather than parameterization-level structure. For safety applications concerned with actual model weights (e.g., detecting when a fine-tuned model has the same dangerous mechanism as a reference), the gauge orbit may be the right level. For applications concerned with computational function (e.g., cross-architecture replication claims), it is the appropriate choice.

Behavioral equivalence is coarser: two mechanisms can compute differently but have the same output distribution. Cohomology class is also coarser: different gauge orbits can have isomorphic cohomology. The gauge orbit is finer than both and is therefore the appropriate choice when the claim is specifically about computational identity.

## What exists

Invariants, transport maps, and equivalence classes:
- **Gauge orbits**: sets of weight configurations related by function-preserving transformations
- **Holonomy fingerprints**: accumulated rotations from parallel-transporting a subspace around a closed loop (connection-dependent; see [Gauge and Holonomy](/mechanistic-views/formalism/deep-dives/gauge-holonomy/))
- **Cosheaf cohomology classes**: topological invariants tracking localizability (linearization-dependent; see [Sheaf Cohomology](/mechanistic-views/formalism/deep-dives/sheaves/))
- **Coverage equivalence classes**: circuit hypotheses with isomorphic cosheaf cohomology

## Identity

Two mechanisms are the same when they lie in the same gauge orbit. Isomorphic holonomy groups are a necessary condition (established) but not a sufficient one (open). Same cohomological equivalence class is a coarser criterion than same gauge orbit.

## Evidence

- **Gauge-invariant measurements**: singular values of [OV circuits](https://learnmechinterp.com/topics/qk-ov-circuits/) $W^{OV}$, principal angles, effective rank — invariant under both head permutations and (approximate) orthogonal rotations. [Composition scores](https://learnmechinterp.com/topics/composition-and-virtual-heads/) $\|W^{OV}_u \cdot W^{KQ}_v\|_F$ are invariant under head permutations but not under the orthogonal rotation symmetry (a residual-stream rotation $U$ transforms $W^{KQ} \to U W^{KQ}$, changing the score); they are gauge-invariant only with respect to the permutation subgroup
- **Holonomy**: estimates of the holonomy group (connection must be specified); isomorphic holonomy is necessary for identity
- **Cohomological tests**: $H^0$ and $H^1$ of the circuit cosheaf (relative to base sections and choice of cosheaf structure)

## Formalism

[Fiber bundle quotient](/mechanistic-views/formalism/fiber-bundle-quotient/) $\mathcal{W}/\mathcal{G}$, principal fiber bundles (at generic points), parallel transport, holonomy (connection-dependent), cellular cosheaf cohomology (base-section-dependent). See the [Gauge and Holonomy](/mechanistic-views/formalism/deep-dives/gauge-holonomy/) and [Sheaf Cohomology](/mechanistic-views/formalism/deep-dives/sheaves/) deep dives for the technical conditions under which these constructions are well-defined.

## What it explains

Portability. When the same mechanism appears across seeds or architectures, what is preserved is the structural invariants. Also explains apparent circuit disagreements: coverage-equivalent proposals (same cosheaf cohomology) have the same localizability structure and may not be contradicting each other — though coverage equivalence is a necessary, not sufficient, condition for non-contradiction (see [Sheaf Cohomology](/mechanistic-views/formalism/deep-dives/sheaves/)).

## What it lets you prove

- **Gauge-invariant identity**: same gauge orbit implies same mechanism (the substance is the argument that gauge orbits are the right level)
- **Holonomy as necessary condition**: same mechanism implies isomorphic holonomy groups
- **Cohomological localizability**: relative to the cosheaf construction and base sections

## Failure modes

**Computability.** Holonomy and cosheaf cohomology are difficult to compute at scale.

**Over-abstraction.** Too coarse an invariant conflates distinct mechanisms.

**Wrong symmetry group.** LayerNorm breaks the full $O(d)$ rotation symmetry; using the wrong $\mathcal{G}$ produces incorrect identity judgments.

**Gauge group non-freeness.** At non-generic points (identical heads), the bundle structure breaks down and holonomy is undefined.

**Connection dependence.** Different connections give different holonomy groups. Claims must specify the connection.

## Relationship to Mechanistic Validity

The structural view has the broadest validity coverage of any static view — gauge invariance gives it measurement invariance, cross-architecture identity, and convergent validity by construction. Its limitations are practical (computability) rather than ontological, and it cannot address formation or training dynamics.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity) | — | 4/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency), [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity) | [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 3/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | — | 3/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation), [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability) | [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | — | 3/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | — | 3/5 |

**Covered** = the view's standard methods directly produce this evidence. **Possible** = testable under this view, but not standard practice. **Impossible** = the view's ontology structurally cannot satisfy this criterion.

**Why alternative exclusion (V4) is now covered.** If two component sets are in the same gauge orbit, they are the same mechanism by definition. The structural view resolves the alternative-exclusion problem by absorbing it into the identity criterion — alternatives related by symmetry are not alternatives, they are the same thing.

**Why cross-architecture (E6) is now covered.** Two models implement the same mechanism if their gauge orbits are isomorphic. This does not require matching specific components — only matching invariant structure.

**Why minimality (C4) is now covered.** Cosheaf cohomology provides a formal criterion for minimality: the circuit is minimal when removing any edge changes the cohomology class. This replaces the intractable exhaustive search required under the object view.

**No impossible criteria.** Like the subspace view, the structural view has no structurally impossible criteria. Its limitations are computational: holonomy, cosheaf cohomology, and gauge-orbit comparison are expensive to compute and require careful specification of the gauge group and connection. The caveats about gauge freeness and connection choice must be stated alongside any validity assessment.

## Further reading

- Elhage et al., "A Mathematical Framework for Transformer Circuits" (2021) — composition scores and QK/OV decomposition as weight-space invariants
- Ainsworth et al., "Git Re-Basin: Merging Models modulo Permutation Symmetries" (2023) — permutation gauge symmetry in neural networks
- For related views: [Object view](/mechanistic-views/views/object/) (uses the same weight matrices but identifies mechanisms with components, not invariants), [Subspace view](/mechanistic-views/views/subspace/) (identifies mechanisms with Grassmannian points, a related but distinct geometric object)
