---
title: "Validation Methodology"
---

# Can we trust our methods?

Three problems threaten the foundations of mechanistic interpretability evidence, and all three are best understood through the [Perspectival view](/mechanistic-views/views/perspectival/) — the view that says what you find depends on how you look.

**Validation circularity.** A circuit is discovered on a dataset, then validated on the same dataset (or a dataset drawn from the same distribution). The validation confirms the discovery, but can't distinguish "the circuit is real" from "the circuit fits this data." Cross-distribution validation — testing on a genuinely different distribution — is rare. The few studies that do it find that circuits often fail to transfer, suggesting that some discoveries are distribution-specific artifacts rather than real mechanisms.

**Interpretability illusions.** A neuron or SAE feature looks interpretable: its top-activating examples share an obvious pattern, it gets a clean natural-language label, and the label predicts which inputs activate it. But the interpretability can be distribution-dependent. On one text corpus, a neuron cleanly detects "sports vocabulary." On another, the same neuron fires on "competitive contexts" more broadly. On a third, it fires on seemingly random inputs. The "sports" interpretation was real for the first distribution but was an illusion created by the distribution's structure, not the neuron's function. Nanda (2022, problems 6.37 and 9.58) identified this as a critical open problem.

**Random baselines.** SAEs find interpretable-looking features. Linear probes find linearly separable concepts. But how much of this structure is real, and how much would you find in a random model? The Apollo Research random direction baseline project (#7) showed that random directions in activation space can receive plausible natural-language explanations — the labeling procedure itself introduces apparent interpretability. Without proper random baselines, every method risks claiming to find structure that isn't there.

## The Perspectival diagnosis

These three problems are exactly what the Perspectival view predicts. If mechanisms are not method-independent objects but projections of analysis procedures onto models, then:

- Validation on the discovery distribution is circular *by construction* — you're testing whether the projection is self-consistent, not whether it's real
- Interpretability depends on distribution *by construction* — the projection changes when the data changes
- Random models yield interpretable features *by construction* — the projection maps onto human categories regardless of whether the model encodes them

The Perspectival view doesn't say interpretability is impossible. It says that single-method, single-distribution findings are structurally unreliable, and the fix is **cross-method convergence**: if multiple independent methods (probing, ablation, DAS, circuit discovery) applied to multiple distributions find the same mechanism, the mechanism is probably real. This is the difference between a method artifact and a robust finding.

## Mechanistic validity impact

| Criterion | Status | Problem |
|---|---|---|
| [I4 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control/) | **Violated** — discovery-validation circularity is an uncontrolled confound | The discovery procedure biases the validation |
| [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | **Untested** — most studies don't test cross-distribution | Without distribution shift testing, interpretability illusions go undetected |
| [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | **Violated** — without random baselines, can't distinguish real from artifactual | If random models also yield "features," the method can't discriminate |
| [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/) | **Untested** — single-method studies dominate | Cross-method convergence is the strongest defense against method artifacts, but is rarely tested |
| [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability/) | **Unknown** — few studies test whether the same method finds the same mechanism on re-run | Test-retest reliability of circuit discovery methods is largely unreported |

The fix for all three problems is the same: convergent evidence across methods, distributions, and runs. This is what higher-commitment views (Subspace and above) require by construction — they build cross-method convergence into their evidence standards rather than treating it as optional.

## Sources

- **Sharkey et al. (2026)** §2.1.4: Validation circularity, no standardized evaluation ([arXiv:2501.16496](https://arxiv.org/abs/2501.16496))
- **Nanda (2022)** §6.37, §9.58: Interpretability illusions ([200 Open Problems](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability))
- **Apollo Research (2024)** #7: Random direction baseline ([45+ MI Projects](https://www.alignmentforum.org/posts/KfkpgXdgRheSRWDy8))
- **ICML 2026 (Orgad, Barez et al.)**: Comparative advantage — MI vs. non-MI baselines ([arXiv:2605.11161](https://arxiv.org/abs/2605.11161))
- **Bolukbasi et al. (2021)**: An interpretability illusion for BERT (distribution-dependent explanations)
