---
title: Role View
---

# Role View

When interpretability researchers say "induction heads appear in every model we've checked," they are making a role-view claim. The mechanism is not head 5.1 in GPT-2 — it's the *induction role*, which happens to be realized by head 5.1 in this model and by different heads in other models. The role view says: the mechanism is the job, not the worker.

This is the first step beyond the object view. It lets you say "this model has a name mover" without specifying which head, and it lets you compare mechanisms across models that have completely different architectures. Most of the field's important high-level claims — "transformers implement induction," "there are S-inhibition heads" — are implicitly role-view claims, even when the evidence is collected at the object level.

The cost is precision. Role labels like "name mover" can be vague enough that almost anything qualifies. If every component gets its own unique role, the role view collapses back to the object view. And roles are still tested by poking at specific components in a specific basis, so the view inherits many of the object view's measurement limitations.

## Thesis

A mechanism is a role in a computational structure: a specification of what functional job needs to be done, which can be instantiated by different components in different models.

## What exists

Role specifications and role realizers. The role (e.g., "name-mover" in IOI) is abstract; a particular head or set of heads is a realizer of that role in a specific model.

## Identity

Two mechanisms are the same when they occupy the same role in isomorphic computational structures, even if different components realize the role.

## Evidence

- **Cross-seed comparison**: different training seeds implement the same behavior via different components, but the same role partition covers all of them
- **Component transplant**: replacing component $h_1$ from $M_1$ with $h_2$ from $M_2$ preserves behavior iff both realize the same role
- **[Linear probing](https://learnmechinterp.com/topics/probing-classifiers/)**: tests whether a concept is linearly accessible, though probing establishes presence not causal use (see [linear classifier formalism](/mechanistic-views/formalism/linear-classifier/))
- **Role-partitioned circuit search**: restricting edge search to role-respecting edges achieves comparable precision and recall to unrestricted search, where precision and recall are measured against a *behavioral* ground truth (necessity and sufficiency on held-out prompts), not against the unrestricted search result itself. Measuring precision/recall against the unrestricted result would be circular

## Formalism

[Role graph](/mechanistic-views/formalism/role-graph/), graph homomorphism, [causal abstraction](https://learnmechinterp.com/topics/causal-abstraction/). The role view operates at Marr's level 2 — the algorithm and representation level, describing *how* the computation is organized into functional roles — rather than level 1 (the abstract task) or level 3 (the specific weights). [DAS/IIA](https://learnmechinterp.com/topics/causal-abstraction/) is the primary method for testing role claims via interchange interventions.

## What it explains

Cross-model and cross-seed claims. When the same mechanism appears in different models via different components, only the role view can express the cross-model identity claim without saying the mechanisms are different.

## What it lets you prove

- **Multiple realization**: the same role can be implemented by different components
- **Role transfer**: if component $h_1$ in $M_1$ realizes role $R$, transplanting $h_1$ into $M_2$ (replacing $M_2$'s role-$R$ component) preserves the role-$R$ behavior — testable by measuring whether the target behavior transfers and whether the transplanted component activates in role-appropriate contexts in $M_2$
- **Role-reduction**: circuit search constrained by role partition is not less accurate than unconstrained search (under a well-specified role partition)

## Semantics of role-view claims

A role-view claim like "head 4.4 is a name-mover" is a *functional* claim: the head realizes the name-mover role in this model. The truth conditions are: (a) the head's outputs transfer information about the indirect object name to positions where it influences the output logit, and (b) this transfer is causally active — ablating the head degrades name-moving performance, and transplanting it into a model lacking a name-mover improves it.

The role claim is stronger than the object claim in one way (it specifies *what function* the component plays) and weaker in another (it does not require the specific component — only that *some* component plays the role). A sentence like "the model has a name-mover mechanism" is a purely role-level claim with no component specification; it is true as long as the role is realized by some circuit component.

## Failure modes

**Vague roles.** A role like "roughly moves the relevant token" is satisfied by almost any component that weakly affects the output. Role specifications must be precise enough to be falsifiable.

**Role inflation.** If every component is assigned its own unique role, the role view collapses to the object view.

**Multiple roles per component.** A component may realize different roles under different prompt conditions, making role assignment context-dependent.

## Relationship to Mechanistic Validity

The role view gains cross-model identity that the object view lacks, but it cannot establish coordinate-independent convergence or measurement invariance — roles are still tested via component-level interventions in a specific basis.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity) | [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | 2/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency) | [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity), [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 2/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | — | 3/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation) | [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability), [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance) | 1/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | 2/5 |

**Covered** = the view's standard methods directly produce this evidence. **Possible** = testable under this view, but not standard practice. **Impossible** = the view's ontology structurally cannot satisfy this criterion.

**Why cross-architecture (E6) is now possible.** The role view's main upgrade over the object view: "name mover" can be found in GPT-2 and Llama because the identity criterion is the role, not the component. Cross-seed and cross-architecture transfer tests are natural.

**Why convergent validity (C5) is still impossible.** Role assignments are still tested via component-level interventions. Different methods may assign different role partitions to the same model, and the role view provides no coordinate-free way to measure agreement between them.

**Why measurement invariance (M2) is still impossible.** Roles are tested by intervening on specific components in a specific basis. Rotating the basis changes which components realize which roles, and the role view has no invariance guarantee across basis changes. The [subspace view](/mechanistic-views/views/subspace/) resolves this.

**Why alternative exclusion (V4) is still impossible.** Multiple distinct role partitions may explain the same behavior equally well. The role view cannot rule out alternative role decompositions without exhaustive search.

## Further reading

- Geiger et al., "Causal Abstraction for Faithful Model Interpretation" (2021) — formalizes causal abstraction and interchange intervention
- Geiger et al., "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations" (2024) — DAS, the primary tool for discovering role-subspace alignments
- Wang et al., "Interpretability in the Wild" (2022) — the IOI circuit's role labels (name-movers, S-inhibition heads) are role-view claims, see [IOI case study](/mechanistic-views/cases/ioi/)
- For related views: [Object view](/mechanistic-views/views/object/) (identifies mechanisms with specific components rather than roles), [Subspace view](/mechanistic-views/views/subspace/) (locates roles in geometric subspaces)
