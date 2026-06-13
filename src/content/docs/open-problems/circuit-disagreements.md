---
title: "Circuit Disagreements"
---

# Which circuit is correct?

The indirect object identification (IOI) task has been analyzed by at least four independent groups using different methods. Wang et al. (2022) found the circuit manually. Conmy et al. (2023) used ACDC (automated circuit discovery via computational graph pruning). Syed et al. (2023) used attribution patching (gradient-weighted activation differences). Hanna et al. (2023) used a related approach for the greater-than task and found circuits with very different sizes. The circuits don't agree. The field treats this as a replication problem — which method got the right answer?

The problem is not replication. The problem is that each method asks a different question, and the question determines the answer. Ablation-based methods (ACDC, activation patching) test which components are *necessary* — remove them and performance degrades. Attribution methods estimate which components *contribute most* — their gradient-weighted effect on the output. Manual analysis identifies which components fill *functional roles* — name movers, backup name movers, induction heads. Necessity, contribution, and functional role are three different things, and they give three legitimately different circuit boundaries.

A component can be highly contributory (large attribution) but not necessary (the network compensates when it's removed). A component can be necessary but fill no identifiable functional role (it's needed but we can't say what it does). A component can fill a clear role but contribute little to the output on average (it's the backup that rarely fires). These are not bugs in the methods. They are different views' answers to the question "what is this circuit?"

## The view confusion

Ablation tests (ACDC, activation patching) operate at the [Object view](/mechanistic-views/views/object/): mechanisms are concrete components, identity is component overlap, evidence is necessity and sufficiency. Attribution methods are closer to the [Instrumental view](/mechanistic-views/views/instrumental/): mechanisms are whatever predicts behavior, no commitment to components being "real." Manual circuit analysis operates at the [Role view](/mechanistic-views/views/role/): mechanisms are functional roles, identity is role equivalence, evidence is that the same role is filled.

When papers disagree about circuit size or membership, they are often comparing answers from different views without recognizing this. The disagreement is real in the sense that the answers differ, but it is not a conflict — it's a consequence of asking different questions.

## Mechanistic validity impact

| Criterion | The confusion | Resolution |
|---|---|---|
| [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/) | Different methods "fail to converge" on the same circuit | Convergence should be checked *within* a view, not across views. ACDC and activation patching should converge (both Object). ACDC and manual role analysis need not |
| [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance/) | Circuit membership changes with method | Method invariance is a within-view criterion. Cross-view variation is expected |
| [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | No principled circuit boundary — threshold-dependent | Each view implies a different natural boundary. Object: necessity threshold. Role: role membership. Subspace: subspace dimension |
| [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion/) | Can't exclude that a different circuit is equally valid | The "alternative" is often the same mechanism described at a different view level — not a competing explanation but a complementary one |

The key insight: convergent validity (C5) and invariance (M2) should be tested *within* a view, not across views. Papers that report "failure to replicate" across methods using different views are making a category error.

## Sources

- **Sharkey et al. (2026)** §2.1.4: Validation of descriptions ([arXiv:2501.16496](https://arxiv.org/abs/2501.16496))
- **Nanda (2022)** §2: Circuits in the wild ([200 Open Problems](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability))
- **Wang et al. (2022)**: Interpretability in the wild: a circuit for indirect object identification in GPT-2 small
- **Conmy et al. (2023)**: Towards automated circuit discovery for mechanistic interpretability (ACDC)
- **Syed et al. (2023)**: Attribution patching outperforms automated circuit discovery (EAP)
- **Hanna et al. (2023)**: How does GPT-2 compute greater-than?
