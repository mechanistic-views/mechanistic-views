---
title: Role View
---

# Role View

The role view treats mechanisms as functional roles that can be multiply realized. The mechanism is not the specific component but the role it plays — the functional contribution it makes to the computation.

## Thesis

A mechanism is a role in a computational structure: a specification of what functional job needs to be done, which can be instantiated by different components in different models.

## What exists

Role specifications and role realizers. The role (e.g., "name-mover" in IOI) is abstract; a particular head or set of heads is a realizer of that role in a specific model.

## Identity

Two mechanisms are the same when they occupy the same role in isomorphic computational structures, even if different components realize the role.

## Evidence

- **Cross-seed comparison**: different training seeds implement the same behavior via different components, but the same role partition covers all of them
- **Component transplant**: replacing component $h_1$ from $M_1$ with $h_2$ from $M_2$ preserves behavior iff both realize the same role
- **[Linear probing](https://learnmechinterp.com/topics/probing-classifiers/)**: tests whether a concept is linearly accessible, though probing establishes presence not causal use (see [linear classifier formalism](/formalism/linear-classifier/))
- **Role-partitioned circuit search**: restricting edge search to role-respecting edges achieves comparable precision and recall to unrestricted search, where precision and recall are measured against a *behavioral* ground truth (necessity and sufficiency on held-out prompts), not against the unrestricted search result itself. Measuring precision/recall against the unrestricted result would be circular

## Formalism

[Role graph](/formalism/role-graph/), graph homomorphism, [causal abstraction](https://learnmechinterp.com/topics/causal-abstraction/). The role view operates at Marr's level 2 — the algorithm and representation level, describing *how* the computation is organized into functional roles — rather than level 1 (the abstract task) or level 3 (the specific weights). [DAS/IIA](https://learnmechinterp.com/topics/causal-abstraction/) is the primary method for testing role claims via interchange interventions.

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

Relevant to external validity (cross-model generalization expressed as role preservation) and interpretive validity (role descriptions are Marr-level-2 claims, requiring component- or subspace-level mechanistic evidence).

## Further reading

- Geiger et al., "Causal Abstraction for Faithful Model Interpretation" (2021) — formalizes causal abstraction and interchange intervention
- Geiger et al., "Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations" (2024) — DAS, the primary tool for discovering role-subspace alignments
- Wang et al., "Interpretability in the Wild" (2022) — the IOI circuit's role labels (name-movers, S-inhibition heads) are role-view claims, see [IOI case study](/cases/ioi/)
- For related views: [Object view](/views/object/) (identifies mechanisms with specific components rather than roles), [Subspace view](/views/subspace/) (locates roles in geometric subspaces)
