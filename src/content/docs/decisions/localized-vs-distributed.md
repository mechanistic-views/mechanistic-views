---
title: Localized vs. Distributed
---

# Localized vs. Distributed

**The fork.** Can the mechanism be assigned to a specific circuit, or is it genuinely distributed?

## Dark matter ratio: definition

The **dark matter ratio** is:

$$r = \frac{\text{full model logit difference}}{\text{circuit logit difference}}$$

on the target task and prompt distribution. A ratio of 1.0 means the circuit fully accounts for the model's behavior. A ratio above 1.0 means the circuit explains less (larger $r$, worse circuit).

**Convention note.** Some papers define the ratio as (circuit) / (full model), giving $r < 1$ for incomplete coverage. Check which convention a paper uses before comparing ratios.

**Degenerate cases.** If the circuit logit difference is near zero or negative — which can happen when circuit components interfere destructively — the ratio is undefined or flips sign and is not informative as a summary statistic. In these cases, report the raw logit differences directly.

## The two interpretations of persistent high $r$

**(A) Incomplete recovery.** A localized mechanism exists but the circuit proposal misses part of it. Dark matter is a measurement artifact; more circuit recovery work would close the gap.

**(B) Genuine distribution.** No finite localized description captures the mechanism. The circuit cosheaf has $H^1 \neq 0$, indicating topological obstruction.

These are not equivalent. Conflating them leads to wrong conclusions: (A) calls for more circuit recovery work; (B) calls for cohomological analysis. Both remain live hypotheses when $r > 1$.

## Distinguishing experiments

**Dark matter ratio.** No principled threshold separates "incomplete recovery" from "genuinely distributed." The ratio is a diagnostic, not a decision boundary. Use it in combination with the iterative expansion and cross-method convergence tests below.

**Iterative circuit expansion.** Repeatedly add the next most important component. If the circuit grows to cover most of the model before $r$ approaches 1.0, localization is failing.

**Cross-method convergence.** If DAS, activation patching, and SAE features all recover different locations and none substantially reduces $r$, this is convergent evidence for distribution.

**Cohomological test.** Build the circuit cosheaf and estimate $H^1$. Non-zero $H^1$ establishes obstruction in *this* specific cosheaf proposal. It does not establish that no description has $H^1 = 0$. This gap should be acknowledged.

## Recommended default

Default to localization for well-studied tasks. Treat distribution as the working hypothesis when $r$ is persistently high despite multiple recovery attempts. Do not treat $H^1 \neq 0$ for one cosheaf proposal as proof of irreducible distribution.
