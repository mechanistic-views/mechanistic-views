---
title: "Intervention Limits"
---

# Do ablations tell the truth?

Ablation is the workhorse of mechanistic interpretability. Zero out an attention head, measure the performance drop, conclude the head is necessary for the task. The logic is clean: if removing a component breaks behavior, that component is part of the mechanism. But three problems undermine this logic, and all three are structural limits of the [Object view](/mechanistic-views/views/object/) rather than bugs in any particular method.

**Reconfiguration.** Ablating a component doesn't just remove it — it changes the input distribution to everything downstream. The remaining network may reconfigure to compensate, making the ablated component look less important than it is. Or it may fail in ways unrelated to the component's actual function, making it look more important. The ablation result tells you about the *reconfigured* network, not the original. Sharkey et al. (2026, §2.1.4) and McGrath et al. (2023) document this problem extensively.

**Multi-component interactions.** Single-component ablation assumes components contribute independently. But attention heads interact: head A's output is head B's input, and ablating A changes what B sees. Pairwise and higher-order interactions can be superadditive (ablating both heads together is worse than the sum of individual ablations) or subadditive (the network has redundancy). Single-component ablation misses this entirely.

**Side effects.** Ablating a component that serves multiple tasks breaks all of them, not just the target task. The ablation tells you the component is necessary for your task, but it doesn't tell you whether the effect is specific to your task or collateral damage. Intervention side effects are measured by essentially no current circuit discovery method.

## The view ceiling

These are not problems with specific ablation techniques. They are structural limits of the Object view's approach to evidence. The Object view treats components as independent units and tests them in isolation. When components are interdependent — which they always are in neural networks — isolation-based evidence is systematically misleading.

The [Structural view](/mechanistic-views/views/structural/) partially resolves this: instead of testing individual components, it characterizes computation in terms of gauge-invariant properties (holonomy, composition scores) that don't require isolating components. The [Subspace view](/mechanistic-views/views/subspace/) offers a different resolution: DAS/IIA interventions target subspaces rather than components, and subspace interventions can be designed to be orthogonal (non-interfering) by construction.

## Mechanistic validity impact

| Criterion | Status | Why |
|---|---|---|
| [I2 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity/) | **Unreliable** — reconfiguration inflates or deflates necessity scores | Ablation tests necessity of the component *in the original network*, but reconfiguration means you're testing a different network |
| [I1 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency/) | **Unreliable** — multi-component interactions mean a "sufficient" subset may only work because of interactions with the complement | Sufficiency of a subset requires the subset to function independently, but independence is exactly what fails |
| [I4 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control/) | **Violated** — side effects are uncontrolled confounds | Every ablation confounds "this component contributes to the target task" with "this component is needed for network stability" |
| [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | **Untested** — ablation studies rarely measure effects on non-target tasks | Without specificity testing, you can't distinguish "this head does IOI" from "this head does everything" |

## Sources

- **Sharkey et al. (2026)** §2.1.4: Ablation reconfiguration, multi-component interactions ([arXiv:2501.16496](https://arxiv.org/abs/2501.16496))
- **Sharkey et al. (2026)** §3.2: Intervention side effects
- **McGrath et al. (2023)**: The hydra effect in ablation studies
- **Chan et al. (2022)**: Causal scrubbing (proposed as a stricter alternative to ablation)
- **ICML 2026 (Orgad, Barez et al.)**: Comparative advantage of MI over non-MI methods ([arXiv:2605.11161](https://arxiv.org/abs/2605.11161))
