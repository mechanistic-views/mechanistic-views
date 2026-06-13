---
title: Case Study — IOI
---

# Case Study — IOI

**The phenomenon.** Given "When Mary and John went to the store, John gave a drink to", a transformer predicts "Mary". [Wang et al. (2023)](https://learnmechinterp.com/topics/ioi-circuit/) identified the relevant circuit in GPT-2 Small.

## [Object view](/mechanistic-views/views/object/)

The mechanism is the component set: name-movers, backup name-movers, negative name-movers, S-inhibition heads, duplicate token heads, and induction heads. Activation patching and path patching show these heads are necessary and approximately sufficient for the logit difference between indirect object and subject names.

**Limitation.** The circuit accounts for roughly 70–80% of the full model's logit difference on standard prompts, leaving a persistent gap. Whether this gap reflects incomplete recovery or genuine distribution is an open question.

## [Role view](/mechanistic-views/views/role/)

The mechanism is the role structure: S-inhibition role, duplicate-token role, name-mover role. The backup name movers finding suggests roles are more stable than components — when name movers are knocked out, other heads compensate by taking on the same role (Wang et al., §3.4). However, systematic cross-seed or cross-model role transfer has not been published.

## [Subspace view](/mechanistic-views/views/subspace/)

The IOI mechanism is a set of causal subspaces, one per relevant variable. Each is a point on the [Grassmannian](/mechanistic-views/formalism/grassmannian/) $\mathrm{Gr}(k, d)$.

**Outstanding.** Systematic [Grassmannian](/mechanistic-views/formalism/grassmannian/) distance measurement between weight-space SVD subspaces and [DAS-recovered subspaces](/mechanistic-views/views/subspace/#evidence) across seeds has not been published.

## [Structural view](/mechanistic-views/views/structural/)

Competing IOI circuit proposals may be coverage-equivalent — same cosheaf cohomology — in which case the apparent disagreement is a measurement artifact.

**Open question.** Are the competing proposals coverage-equivalent, accounting for the base-section and cosheaf-construction dependence of $H^\bullet$?

## Current evidence state

- **Tier 3** under the [object view](/mechanistic-views/views/object/) for standard prompts
- **Tier 2** under the [subspace](/mechanistic-views/views/subspace/) and [role](/mechanistic-views/views/role/) views
- **Tier 1** under the [structural view](/mechanistic-views/views/structural/)

## What would move to higher tiers

**Subspace view, Tier 3 → 4** (three-domain triangulation + cross-architecture generalization):
- Systematic [DAS](/mechanistic-views/views/subspace/#evidence) recovery with IIA reported across seeds and architectures
- Cross-seed [Grassmannian](/mechanistic-views/formalism/grassmannian/) distance measurement between weight-space SVD and DAS subspaces
- AGOP trajectory analysis of IOI mechanism formation

**Role view, Tier 2 → 3** (two-domain + cross-model consistency):
- Systematic role partition search with precision/recall against behavioral ground truth
- Cross-architecture role transfer with transplant experiments

**All views**: dark matter accounting — close the $r$ gap or establish cosheaf obstruction with base sections specified

## Limitations acknowledged by the original paper

The authors explicitly note several gaps:

- "Though these criteria support our explanation, they also point to remaining gaps in our understanding." (Abstract)
- "We do not understand several components. Those include the attention patterns of the S-Inhibition Heads, and the effect of MLPs and layer norms." (§5)
- "To fully validate the claimed function of the Duplicate Token and Induction Heads, we would want to perform additional checks that we omitted due to time constraints." (§3.3)
- The backup name movers reveal that the circuit changes under intervention: "These new heads compensate for the loss of Name Movers Heads by replacing their role." (§3.4)
- GPT-2 Medium shows the roles don't transfer cleanly: "not all of these heads attend to IO and S, suggesting more complex behavior than the Name Movers Heads in GPT-2 small." (§5)

The faithfulness/completeness/minimality criteria test whether the *circuit* (the set of heads) matters, but not whether the *functional story* (the role assignments) is correct — the roles were assigned post-hoc from observed behavior, not predicted in advance.

## Further reading

Wang, K., Variengien, A., Conmy, A., Shlegeris, B., Steinhardt, J. "Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small." [ICLR 2023. arXiv:2211.00593](https://arxiv.org/pdf/2211.00593).
