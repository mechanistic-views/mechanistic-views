---
title: "Safety Evidence Gaps"
---

# Does steering find mechanisms?

Arditi et al. (2024) found a direction in activation space that, when ablated, removes refusal behavior from LLMs. The result is widely cited as "finding the refusal mechanism." Zou et al. (2023) found directions for truthfulness, power-seeking, and other behavioral traits via representation engineering. Turner et al. (2023) demonstrated activation steering for personality traits. These results are being seriously considered for deployment-time safety monitoring: find the "deception direction," monitor it during inference, flag when it activates.

The evidence in every case is [Instrumental](/mechanistic-views/views/instrumental/): intervening on the direction changes behavior. This establishes that the direction is a sufficient lever for behavioral control. It does not establish that the direction *is* the mechanism responsible for that behavior. The distinction matters enormously for safety.

A lever can work for reasons unrelated to the mechanism. The refusal direction might disrupt a shared computational pathway that many behaviors depend on — ablating it removes refusal because it removes everything, not because it specifically targets refusal. The truthfulness direction might correlate with the actual mechanism without being the mechanism itself — a confound rather than a cause. Redundant mechanisms are another failure mode: the model might have multiple pathways for refusal, and the direction captures only one. A safety monitor built on an Instrumental finding has Instrumental-level guarantees: it predicts and controls behavior *on the distribution tested*. It says nothing about whether the mechanism generalizes, whether it's the only mechanism, or whether it's robust to adversarial inputs designed to evade monitoring.

## The view gap

Safety monitoring requires more than [Instrumental](/mechanistic-views/views/instrumental/) evidence. At minimum, it requires [Object](/mechanistic-views/views/object/) evidence — the mechanism exists as an identifiable, necessary component. Ideally, it requires [Subspace](/mechanistic-views/views/subspace/) evidence — the mechanism is a stable subspace that generalizes across distributions and is robust to measurement. The gap between what the field has (Instrumental) and what safety applications need (Object or Subspace) is the central evidence gap in AI safety interpretability.

The [Schmidt Sciences 2026 "Trustworthy AI" research agenda](https://www.schmidtsciences.org/trustworthy-ai-research-agenda/) focuses on exactly this gap: detecting deceptive behaviors (sycophancy, harmful advice, selective omission) and steering for truthfulness with tools that *generalize beyond academic benchmarks*. Generalization is an [external validity](/mechanistic-views/views/subspace/#evidence) requirement that Instrumental evidence cannot satisfy.

## Mechanistic validity impact

| Criterion | Instrumental evidence | Object evidence needed | Subspace evidence needed |
|---|---|---|---|
| [I1 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency/) | Covered (steering works) | Covered (ablation shows necessity + sufficiency) | Covered |
| [I2 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity/) | Not tested | Covered (ablation) | Covered |
| [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion/) | **Impossible** | Possible | Covered (subspace uniqueness) |
| [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | **Not tested** | Possible but not standard | Testable via subspace stability |
| [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | **Not tested** | Possible but not standard | Testable via Grassmannian distance |
| [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | **Not tested** | Testable via targeted ablation | Testable via subspace orthogonality |

The pattern: Instrumental evidence covers sufficiency (the lever works) but leaves necessity, alternative exclusion, and all external validity criteria untested. A safety case built on Instrumental evidence has at least five untested validity criteria. Moving to Object evidence fills necessity and makes external criteria testable. Moving to Subspace evidence covers alternative exclusion and makes external criteria measurable.

## Sources

- **[Schmidt Sciences (2026)](https://www.schmidtsciences.org/trustworthy-ai-research-agenda/)**: "Trustworthy AI" agenda §2.1–2.2 — evaluation validity, mechanistic interventions, deception detection
- **Sharkey et al. (2026)** §3.2: Safety monitoring and auditing ([arXiv:2501.16496](https://arxiv.org/abs/2501.16496))
- **Apollo Research (2024)**: Deception evaluation framework ([45+ MI Projects](https://www.alignmentforum.org/posts/KfkpgXdgRheSRWDy8))
- **Arditi et al. (2024)**: Refusal in language models is mediated by a single direction
- **Zou et al. (2023)**: Representation engineering: a top-down approach to AI transparency
- **Turner et al. (2023)**: Activation addition: steering language models without optimization
