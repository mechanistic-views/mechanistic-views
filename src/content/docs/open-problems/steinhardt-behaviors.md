---
title: "Steinhardt: Evaluating Behaviors"
---

# Steinhardt: "The Case for Evaluating Model Behaviors"

[Steinhardt (2026)](https://www.lesswrong.com/posts/J5KkwYnnaeNX7hL2s/the-case-for-evaluating-model-behaviors) argues that the field over-invests in capability evaluation (measuring peak performance) and under-invests in behavior evaluation (measuring tendencies and propensities). A model can *have the capability* to answer truthfully while *having the propensity* to confabulate. Current evaluation frameworks mostly measure the former.

This distinction maps cleanly onto the views framework: capability findings are [Instrumental](/mechanistic-views/views/instrumental/) (this mechanism *can* produce this behavior), while propensity findings require at least [Role](/mechanistic-views/views/role/) evidence (this mechanism *typically* produces this behavior in the model's normal operation). The gap between capability and propensity is a view-level gap.

## Key claims and their view mappings

| Steinhardt claim | View translation | Validity criteria |
|---|---|---|
| "Propensity ≠ capability" — models can do X but don't reliably do X | Instrumental evidence (capability) ≠ Role evidence (propensity). Showing a circuit *can* do a task isn't showing it *does* the task | [C1 Operationalization](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/operationalization/) — are we measuring the right thing? |
| "Behavioral distributions matter, not just averages" | Average behavior = Instrumental summary. Distribution of behavior = requires understanding of when mechanisms fire and when they don't = Role or Subspace evidence | [E3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/specificity/) — does the mechanism fire specifically for this task? |
| "Reward hacking exploits shortcuts" | A reward-hacking circuit uses positional or statistical features instead of semantic ones. The Object view finds the circuit; whether it's a shortcut requires Role-level understanding of what the circuit *should* be doing | [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion/) — is there an alternative (shortcut) mechanism? |
| "Circuit knowledge should predict behavior" | If your mechanistic understanding is correct, it should predict when the model succeeds and fails on held-out data. This is predictive validity — the bridge from mechanistic to behavioral | [E1 Task transfer](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/task-transfer/), [E2 Distribution shift](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/distribution-shift/) |
| "The field studies what models can do, not what they tend to do" | The Instrumental view measures *capability*. Propensity requires understanding the mechanism's activation conditions — when it fires and why — which is at minimum Role-level evidence | [Instrumental](/mechanistic-views/views/instrumental/) ceiling |

## The core view-level insight

Steinhardt's argument reduces to: **Instrumental evidence is insufficient for safety.** Knowing that a model *can* be truthful (Instrumental) doesn't tell you when it *will* be truthful (Role) or *why* it sometimes isn't (Subspace/Structural). Safety requires propensity guarantees, and propensity guarantees require higher-commitment views than the field typically operates at.

This is the same conclusion as the [safety evidence gaps](/mechanistic-views/open-problems/safety-evidence-gaps/) analysis, arrived at from a different direction. Steinhardt comes at it from the evaluation side (we're measuring the wrong thing). The views framework comes at it from the evidence side (we're collecting the wrong kind of evidence). The diagnosis converges: the field's default view level is too low for the conclusions being drawn.

## Mechanistic validity impact

Steinhardt's behavioral evaluation framework maps onto three mechval criteria that are systematically undertested in current MI work:

| Criterion | Current status | What Steinhardt adds |
|---|---|---|
| [C1 Operationalization](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/operationalization/) | Usually operationalized as "circuit that *can* produce behavior X" | Should be "circuit that *reliably* produces behavior X under specified conditions" |
| [E3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/specificity/) | Rarely tested — most circuit studies don't measure effects on non-target behaviors | Propensity measurement inherently requires specificity: when does the mechanism fire vs. not fire? |
| [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability/) | Test-retest reliability of circuit discovery is largely unreported | Behavioral propensity is inherently a distributional measure — reliability is built into the operationalization |

## Sources

- **[Steinhardt (2026)](https://www.lesswrong.com/posts/J5KkwYnnaeNX7hL2s/the-case-for-evaluating-model-behaviors)**: The case for evaluating model behaviors
- **Coverage analysis**: `mechanistic-validity-experiments/experiments/15_unsolved_problems/steinhardt_behaviors/` — behavioral propensity measurement, reward hacking circuit scan, circuit-to-behavior prediction experiments
