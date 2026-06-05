---
title: Case Study — IOI
---

# Case Study: Indirect Object Identification

**The phenomenon.** Given "When Mary and John went to the store, John gave a drink to", a transformer predicts "Mary". Wang et al. (2023) identified the relevant circuit in GPT-2 Small.

## Object view

The mechanism is the component set: name-movers, backup name-movers, negative name-movers, S-inhibition heads, duplicate token heads, and induction heads. Activation patching and path patching show these heads are necessary and approximately sufficient for the logit difference between indirect object and subject names.

**Limitation.** The circuit accounts for roughly 70–80% of the full model's logit difference on standard prompts, leaving a persistent gap. Whether this gap reflects incomplete recovery or genuine distribution is an open question.

## Role view

The mechanism is the role structure: S-inhibition role, duplicate-token role, name-mover role. Different seeds realize these roles with different specific heads. Cross-seed role transfer qualitatively established; systematic role partition search not published.

## Subspace view

The IOI mechanism is a set of causal subspaces, one per relevant variable. Each is a point on $\mathrm{Gr}(k, d)$.

**Outstanding.** Systematic Grassmannian distance measurement between weight-space SVD subspaces and DAS-recovered subspaces across seeds has not been published.

## Structural view

Competing IOI circuit proposals may be coverage-equivalent — same cosheaf cohomology — in which case the apparent disagreement is a measurement artifact.

**Open question.** Are the competing proposals coverage-equivalent, accounting for the base-section and cosheaf-construction dependence of $H^\bullet$?

## Current evidence state

- **Tier 3** under the object view for standard prompts
- **Tier 2** under the subspace and role views
- **Tier 1** under the structural view

## What would move to higher tiers

**Subspace view, Tier 3 → 4** (three-domain triangulation + cross-architecture generalization):
- Systematic DAS recovery with IIA reported across seeds and architectures
- Cross-seed Grassmannian distance measurement between weight-space SVD and DAS subspaces
- AGOP trajectory analysis of IOI mechanism formation

**Role view, Tier 2 → 3** (two-domain + cross-model consistency):
- Systematic role partition search with precision/recall against behavioral ground truth
- Cross-architecture role transfer with transplant experiments

**All views**: dark matter accounting — close the $r$ gap or establish cosheaf obstruction with base sections specified

## Further reading

Wang, K., Variengien, A., Conmy, A., Shlegeris, B., Steinhardt, J. "Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small." ICLR 2023. arXiv:2211.00593.
