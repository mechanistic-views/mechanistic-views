---
title: Case Study — Self-Knowledge
---

# Case Study — Self-Knowledge

**The phenomenon.** Language models sometimes make accurate claims about their own uncertainty, capabilities, and knowledge boundaries. Whether these claims are causally driven by internal representations or by distributional pattern-matching is an open empirical question.

## Two mechanistically distinct phenomena

**Type 1: Distributional self-report.** The model produces hedges or capability claims based on statistical regularities — texts where uncertainty markers co-occur with similar question types. No mechanism accesses internal states. The output is a distributional reflex.

**Type 2: Introspection-like access.** The model's output is causally driven by its internal representations. A subspace for "current internal uncertainty" causes hedging, rather than merely correlating with outputs labeled as uncertain.

These are distinguishable empirically. The type distinction is a scientific question, not a philosophical one.

## [Object view](/views/object/)

If Type 2 self-knowledge exists, there is a component set mediating internal states to self-referential outputs. Test: ablating the proposed component should impair uncertainty tracking while preserving normal task performance.

**The counterfactual difficulty.** Constructing "same task, different internal uncertainty" as a minimal pair is hard without also changing distributional context.

## [Subspace view](/views/subspace/)

Hypothesis: a subspace $S_\text{self}$ in the [Grassmannian](/formalism/grassmannian/) $\mathrm{Gr}(k, d)$ whose projection tracks a property of internal state (uncertainty, representation quality) and causally influences self-referential outputs.

[DAS](/views/subspace/#evidence) can in principle recover this via minimal pairs: forward passes where internal uncertainty is high versus low. Activation steering on the hypothesized subspace is a cleaner approach (it bypasses prompt statistics).

## The distributional confound

This is the central obstacle. A model hedging on obscure-fact questions may have learned to associate hedging with question type rather than with internal uncertainty. Testing for Type 2 self-knowledge requires showing the proposed subspace causally affects outputs *independently of the prompt statistics* — achievable via activation steering rather than prompt manipulation.

## Relationship to hallucination

If $S_\text{self}$ causally suppresses confident-but-wrong outputs when its projection is high, then accurate self-knowledge is anti-hallucination infrastructure. If this holds, the self-knowledge mechanism has direct safety relevance: it would provide a causal account of when and why models produce calibrated self-assessments.

## Current evidence state

- **Tier 1** across all views: no published work applies [DAS](/views/subspace/#evidence) or systematic patching to self-knowledge with appropriate controls for the distributional confound

## What would move to Tier 2

- [DAS](/views/subspace/#evidence) on minimal pairs spanning known variation in model confidence, with IIA reported
- Activation steering showing the proposed subspace causally affects self-referential outputs independently of prompt statistics
- Weight-space analysis of the internal-state-to-output pathway

## Further reading

Kadavath, S., Conerly, T., Askell, A. et al. "Language Models (Mostly) Know What They Know." [arXiv:2207.05221](https://arxiv.org/abs/2207.05221), 2022.

Li, K., Patel, O., Vieira, F., Raber, N., Sachan, M., Riedel, S., Hajishirzi, H. "Representation Engineering: A Top-Down Approach to AI Transparency." [arXiv:2310.01405](https://arxiv.org/abs/2310.01405), 2023.
