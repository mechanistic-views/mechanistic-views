---
title: Role View
---

# Role View

The object view identifies mechanisms with specific components: head 5.1, neuron 347, this set of edges. But what happens when the same computation appears in multiple models implemented by completely different components? The role view answers: the mechanism is not the component, it's the job. "Name mover" is the mechanism; head 5.1 is just one way it happens to be realized in one particular model.

This is the first step beyond the object view. It lets you say "this model has a name mover" without specifying which head, and it lets you compare mechanisms across models with different architectures. Many of the field's important high-level claims are implicitly role-view claims — claims about what functional job is being done, not about which specific component does it.

## Thesis

A mechanism is a role in a computational structure: a specification of what functional job needs to be done, which can be instantiated by different components in different models.

## What it explains

**Cross-model claims.** When researchers observe induction-like behavior across many transformer models, they are noting that the same functional role is realized by different components in different architectures. Only the role view can express the claim "these models all do the same thing" without requiring them to use the same heads. The observation that induction heads appear across diverse model families — a claim about functional role, not about any specific head — is a role-view claim, regardless of whether the original authors framed it that way.

**Why circuit labels like "name mover" or "S-inhibition head" are useful.** These labels describe functional roles, not intrinsic properties of specific heads. The role view explains why these labels transfer across model instances and training seeds even when the specific component assignments change.

**What "multiple realization" means for interpretability.** The same role can be implemented by different components, by different numbers of components, or by different architectural structures. The role view makes this a feature, not a bug — it is exactly the level of description needed for cross-model comparison.

## What this view says

The role view distinguishes between *role specifications* and *role realizers*. The role (e.g., "name-mover" in the IOI task) is abstract — it specifies a functional job. A particular head or set of heads is a realizer of that role in a specific model. Two mechanisms are the same when they occupy the same role in isomorphic computational structures, even if different components realize the role.

The cost is precision. Role labels like "name mover" must be specified precisely enough to be falsifiable — if the label is so vague that almost any component qualifies, the role view collapses into triviality. A role specification should include: what information the component must receive, what transformation it must perform, and what downstream effect it must have. "Roughly moves the relevant token" is too vague; "copies the indirect object token's identity from the IO position to the end position, increasing the logit of the IO token by at least $\delta$ on IOI prompts" is testable.

## When it works and when it doesn't

The role view is strongest when the same behavior appears across models or training seeds via different components. Cross-seed comparison — different training seeds implement the same behavior via different components, but the same role partition covers all of them — is the cleanest evidence.

**Vague roles.** The central risk. A role like "roughly processes the relevant context" is satisfied by almost any component that weakly affects the output. Post-hoc role assignment is especially dangerous: if you observe what a head does and then name that the "role," you have described the head, not discovered a functional category. Roles must be specified before looking at which components realize them, or the assignment is unfalsifiable.

**Role inflation.** If every component is assigned its own unique role, the role view collapses to the object view and adds no explanatory power.

**Multiple roles per component.** A component may realize different roles under different prompt conditions, making role assignment context-dependent. Head 4.4 might be a name-mover on IOI prompts and something entirely different on arithmetic prompts.

**Roles are still tested via components.** Evidence for role claims comes from component-level interventions in a specific basis. The role view inherits many of the object view's measurement limitations — it adds a layer of functional abstraction on top.

---

## Technical details

### Evidence

- **Cross-seed comparison**: different training seeds implement the same behavior via different components, but the same role partition covers all of them
- **Component transplant**: replacing component $h_1$ from $M_1$ with $h_2$ from $M_2$ preserves behavior iff both realize the same role
- **[Linear probing](https://learnmechinterp.com/topics/probing-classifiers/)**: tests whether a concept is linearly accessible, though probing establishes presence not causal use (see [linear classifier formalism](/mechanistic-views/formalism/linear-classifier/))
- **Role-partitioned circuit search**: restricting edge search to role-respecting edges achieves comparable precision and recall to unrestricted search, where precision and recall are measured against a *behavioral* ground truth (necessity and sufficiency on held-out prompts)

### What it lets you prove

- **Multiple realization**: the same role can be implemented by different components
- **Role transfer**: if component $h_1$ in $M_1$ realizes role $R$, transplanting $h_1$ into $M_2$ (replacing $M_2$'s role-$R$ component) preserves the role-$R$ behavior
- **Role-reduction**: circuit search constrained by role partition is not less accurate than unconstrained search (under a well-specified role partition)

### Formalism

[Role graph](/mechanistic-views/formalism/role-graph/), graph homomorphism, [causal abstraction](https://learnmechinterp.com/topics/causal-abstraction/). The role view operates at Marr's level 2 — the algorithm and representation level. [DAS/IIA](https://learnmechinterp.com/topics/causal-abstraction/) is the primary method for testing role claims via interchange interventions.

### Relationship to Mechanistic Validity

The role view gains cross-model identity that the object view lacks, but cannot establish coordinate-independent convergence or measurement invariance.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity) | [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | 2/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency) | [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity), [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 2/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | — | 3/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation) | [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability), [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance) | 1/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | 2/5 |

**Why cross-architecture (E6) is now possible.** The role view's main upgrade over the object view: "name mover" can be found in GPT-2 and Llama because the identity criterion is the role, not the component.

**Why measurement invariance (M2) is still impossible.** Roles are tested by intervening on specific components in a specific basis. Rotating the basis changes which components realize which roles. The [subspace view](/mechanistic-views/views/subspace/) resolves this.

### Further reading

- Geiger et al., "Causal Abstraction for Faithful Model Interpretation" (2021) — formalizes causal abstraction and interchange intervention
- Geiger et al., "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations" (2024) — DAS, the primary tool for discovering role-subspace alignments
- Wang et al., "Interpretability in the Wild" (2022) — the IOI circuit's role labels (name-movers, S-inhibition heads)
- For related views: [Object view](/mechanistic-views/views/object/) (identifies mechanisms with specific components), [Subspace view](/mechanistic-views/views/subspace/) (locates roles in geometric subspaces)
