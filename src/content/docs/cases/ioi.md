---
title: Case Study — IOI
---

# Case Study — IOI

**The phenomenon.** Given "When Mary and John went to the store, John gave a drink to", a transformer predicts "Mary". [Wang et al. (2023)](/mechanistic-views/glossary/#ioi-circuit) identified the relevant circuit in GPT-2 Small.

## [Object view](/mechanistic-views/views/object/)

The mechanism is the component set: name-movers, backup name-movers, negative name-movers, S-inhibition heads, duplicate token heads, and induction heads. Activation patching and path patching show these heads are necessary and approximately sufficient for the logit difference between indirect object and subject names.

**Limitation.** The circuit recovers 87% of the full model's logit difference (Wang et al., 2023), and still admits rival head sets of comparable faithfulness (Chen et al., 2026). The residual is not the only underdetermination: more than one head set clears the same faithfulness bar.

## [Role view](/mechanistic-views/views/role/)

The mechanism is the role structure: S-inhibition role, duplicate-token role, name-mover role. Knocking out the three main name movers leaves the logit difference only 5% lower, because other heads compensate "by replacing their role" (Wang et al., §3.4) — which the role view predicts, since multiple realizability is what a role predicts. But the class itself is fixed by an effect-size threshold the authors call arbitrary: of the eight backup name movers, four resemble name movers, two attend to and copy both candidate names, one prefers the subject token, and one tracks subjects of clauses. Half the class does not perform the function the class is named for, and systematic cross-seed or cross-model role transfer has not been published.

## [Subspace view](/mechanistic-views/views/subspace/)

The IOI mechanism is a set of causal subspaces, one per relevant variable. Each is a point on the [Grassmannian](/mechanistic-views/formalism/grassmannian/) $\mathrm{Gr}(k, d)$.

**Outstanding.** Systematic [Grassmannian](/mechanistic-views/formalism/grassmannian/) distance measurement between weight-space SVD subspaces and [DAS-recovered subspaces](/mechanistic-views/views/subspace/#evidence) across seeds has not been published.

## [Structural view](/mechanistic-views/views/structural/)

The relevant object is gauge-invariant information flow — the K-composition term for downstream heads reading from head 9.9 (Elhage et al., 2021). A computation-preserving reparameterization changes the weight matrices but not the composition score; a patching result that survives such reparameterization is structural, and one that does not is basis-dependent.

**Open question.** Do the competing circuit proposals survive a computation-preserving reparameterization of the implicated heads' weights? If a proposal's support changes under one, it was basis-dependent rather than structural.

## Current evidence state

The criterion returns **candidate**. Patching and the knockout dissociation are both identity-family evidence, so the support does not cross a family boundary — not because the evidence is weak, but because one family's characteristic artifact, a role asserted rather than operationalized, could produce all of it. The subspace and structural questions are posed rather than answered. What the later work adds is analyst-choice evidence that the object is foil-relative: Franco et al. (2026) obtain two circuit clusters from two template families, and Sun et al. (2026) find congruence collapsing across model families.

## What would cross a second family boundary

**Subspace view, Tier 3 → 4** (three-domain triangulation + cross-architecture generalization):
- Systematic [DAS](/mechanistic-views/views/subspace/#evidence) recovery with IIA reported across seeds and architectures
- Cross-seed [Grassmannian](/mechanistic-views/formalism/grassmannian/) distance measurement between weight-space SVD and DAS subspaces
- AGOP trajectory analysis of IOI mechanism formation

**Role view, Tier 2 → 3** (two-domain + cross-model consistency):
- Systematic role partition search with precision/recall against behavioral ground truth
- Cross-architecture role transfer with transplant experiments

**All views**: the subspace and structural questions are posed rather than answered — the circuit's support has not yet crossed a family boundary

## Limitations acknowledged by the original paper

The authors explicitly note several gaps:

- "Though these criteria support our explanation, they also point to remaining gaps in our understanding." (Abstract)
- "We do not understand several components. Those include the attention patterns of the S-Inhibition Heads, and the effect of MLPs and layer norms." (§5)
- "To fully validate the claimed function of the Duplicate Token and Induction Heads, we would want to perform additional checks that we omitted due to time constraints." (§3.3)
- The backup name movers reveal that the circuit changes under intervention: "These new heads compensate for the loss of Name Movers Heads by replacing their role." (§3.4)
- GPT-2 Medium shows the roles don't transfer cleanly: "not all of these heads attend to IO and S, suggesting more complex behavior than the Name Movers Heads in GPT-2 small." (§5)

The faithfulness/completeness/minimality criteria test whether the *circuit* (the set of heads) matters, but not whether the *functional story* (the role assignments) is correct — the roles were assigned post-hoc from observed behavior, not predicted in advance.

## Further reading

Wang, K., Variengien, A., Conmy, A., Shlegeris, B., Steinhardt, J. "Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small." [ICLR 2023. arXiv:2211.00593](https://arxiv.org/abs/2211.00593).
