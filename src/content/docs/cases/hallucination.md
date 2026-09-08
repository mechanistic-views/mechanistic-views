---
title: Case Study — Hallucination
---

# Case Study — Hallucination

**The phenomenon.** Language models generate confident, fluent, factually incorrect outputs. Simhi et al. (2024) separate two mechanistically distinct failure modes: cases where the model "does not hold the correct answer in its parameters" (HK⁻) and cases where it has the knowledge and errs anyway (HK⁺). They report HK⁺ hallucinations are prevalent across models and datasets, which makes retrieval failure a mechanism to explain rather than an edge case.

## [Object view](/mechanistic-views/views/object/)

A set of components retrieves the correct fact; a competing mechanism promoting the incorrect candidate wins. Evidence: activation patching studies showing specific layers or heads produce the correct answer when patched from a correct pass.

**Limitation.** Correct and incorrect mechanisms do share components: Cheang et al. (2025) report that hallucinations produced from learned associations are "mechanistically similar to those of factual recall." The [object view](/mechanistic-views/views/object/) therefore cannot cleanly localize the failure — this is a measured finding rather than a hypothetical.

## [Role view](/mechanistic-views/views/role/)

The mechanism is the *fact-retrieval role*: whatever promotes the correct entity as answer candidate when it is correct. Hallucination is a role-competition failure: the retrieval role and a distributional-prior role both activate, and the latter dominates.

The [role view](/mechanistic-views/views/role/) predicts that the same components may play different roles on different prompts. Role-substitution experiments distinguish this from simple ablation.

## [Subspace view](/mechanistic-views/views/subspace/)

The causal variable is "which entity is currently promoted as the answer candidate." This occupies a subspace at the final layers. In the hallucinating case, the wrong entity has higher projection onto the answer-readout subspace.

Evidence: [DAS](/mechanistic-views/views/subspace/#evidence) on minimal pairs where the correct entity is known and the prompts vary in structure, searching for the subspace whose swap changes the answer from incorrect to correct.

**Outstanding.** Systematic [DAS](/mechanistic-views/views/subspace/#evidence) analysis with IIA reported for factual recall hallucination has not been published.

## [Structural view](/mechanistic-views/views/structural/)

Hypothesis: facts encoded with *higher* effective-rank weight structure hallucinate more frequently under retrieval competition, since low-effective-rank storage concentrates a fact into a robust attractor while high-effective-rank storage spreads it thinly enough to be overridden by a competing candidate. A test: measure effective rank of the fact-encoding component in $W^{OV}$ of implicated heads, correlate with hallucination frequency on ambiguous prompts.

## Current evidence state

Tiers below are the [Mechanistic Validity](/mechanistic-views/mechval-interface/) ladder, not this framework's verdict vocabulary.

- **Tier 2** for the [object](/mechanistic-views/views/object/) and [role](/mechanistic-views/views/role/) views: patching studies localize factual recall to mid-to-late layers; cross-seed consistency not reported
- **Tier 1** for [subspace](/mechanistic-views/views/subspace/) and [structural](/mechanistic-views/views/structural/) views

## What a second family would need to show

- [DAS](/mechanistic-views/views/subspace/#evidence) on factual recall tasks with IIA reported and cross-prompt consistency established
- Weight-space evidence: effective rank and composition score analysis of heads identified by patching
- Mechanistic discrimination of knowledge-absence from retrieval-failure at the circuit level

## Further reading

Simhi, A., Herzig, J., Szpektor, I., Belinkov, Y. "Distinguishing Ignorance from Error in LLM Hallucinations." [arXiv:2410.22071](https://arxiv.org/abs/2410.22071), 2024. — the HK⁻ / HK⁺ split this page rests on.

Cheang, C. S., Chan, H. P., Zhang, W., Deng, Y. "Do LLMs Really Know What They Don't Know? Internal States Mainly Reflect Knowledge Recall Rather Than Truthfulness." [arXiv:2510.09033](https://arxiv.org/abs/2510.09033), 2025. — reports that hallucinations produced from learned associations are mechanistically similar to factual recall.

Meng, K., Bau, D., Andonian, A., Belinkov, Y. "Locating and Editing Factual Associations in GPT." [NeurIPS 2022. arXiv:2202.05262](https://arxiv.org/abs/2202.05262). — background on where factual associations are stored.

Li, K., Patel, O., Viégas, F., Pfister, H., Wattenberg, M. "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model." [NeurIPS 2023. arXiv:2306.03341](https://arxiv.org/abs/2306.03341). — an instrumental-view intervention on the same phenomenon.
