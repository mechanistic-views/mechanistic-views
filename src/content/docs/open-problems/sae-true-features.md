---
title: "Case Study — Do SAEs Recover the 'True' Features?"
---

# Do SAEs Recover the "True" Features?

**The question.** Sparse autoencoders decompose neural network activations into interpretable directions. But the features change with SAE width, training seed, and architecture. Which features are "real"? Are any of them the "true" decomposition of what the model is doing?

This question is one of the most actively debated in mechanistic interpretability. We show that it is a view-level question: the answer depends entirely on what you mean by "feature."

## What each view says

### [Object view](/mechanistic-views/views/object/) — features are parts

Features are concrete, countable components of the model's computation. There is a fact of the matter about which features exist. An SAE at the "right" width recovers them; an SAE at the wrong width either splits genuine features or merges distinct ones.

**The problem.** Different SAE widths give different feature sets. [Bricken et al. (2023)](https://transformer-circuits.pub/2023/monosemantic-features/index.html) showed that increasing width progressively splits features into finer-grained variants. If there are true features, which width finds them? The Object view has no principled answer — it requires a ground truth that no one has access to.

### [Subspace view](/mechanistic-views/views/subspace/) — the subspace is what's real

Individual features are basis vectors. What's real is the *subspace* they span — a point on the [Grassmannian](/mechanistic-views/formalism/grassmannian/) $\mathrm{Gr}(k, d)$. Different SAE widths give different bases for overlapping subspaces. This is expected, not problematic.

**The test.** Measure [Grassmannian distance](/mechanistic-views/formalism/grassmannian/#subspace-stability) between SAE feature subspaces across widths and seeds. If the subspaces converge (small $d_{\mathrm{Gr}}$), the SAEs are finding real structure. If they don't, the decomposition is method-dependent. Which individual features you name is a gauge choice — like choosing a coordinate system for a vector space. The subspace is gauge-invariant; the basis is not.

### [Perspectival view](/mechanistic-views/views/perspectival/) — features are method projections

SAE features are not discoveries *in* the model — they are projections *of* the model through a particular method (sparse dictionary learning with a specific loss function, width, and training procedure). A different method projects different features. Neither is wrong; neither is "true."

**The implication.** Asking whether SAE features are "real" is like asking whether a Mercator projection is the "true" shape of a continent. The projection is mathematically valid and practically useful, but the shape is not "in" the territory. [Casper et al. (2023)](https://arxiv.org/abs/2312.09237) and others have shown that SAEs applied to random or shuffled activations still produce "interpretable" features — exactly what the Perspectival view predicts.

## The resolution

"Do SAEs recover the true features?" is not an empirical question with a single answer. It is three different questions depending on your view:

| View | Question | Answer |
|---|---|---|
| [Object](/mechanistic-views/views/object/) | Are these the real parts? | Underdetermined — no principled way to pick the "right" width |
| [Subspace](/mechanistic-views/views/subspace/) | Does the subspace converge? | Testable — measure $d_{\mathrm{Gr}}$ across widths and seeds |
| [Perspectival](/mechanistic-views/views/perspectival/) | Are these more than method artifacts? | Requires [discriminant validity](/mechanistic-views/views/perspectival/#evidence) — trained vs. control comparison |

The field argues because researchers at different views mean different things by "true." The Object-view researcher wants to know which features are real. The Subspace-view researcher wants to know if the subspace is stable. The Perspectival-view researcher wants to know if the method is imposing structure.

**The practical fix:** stop asking "are these the true features?" and start asking:
1. **Subspace convergence** — do SAEs at different widths span similar subspaces? (Grassmannian distance)
2. **Discriminant validity** — do SAEs find qualitatively different structure in trained vs. random models? (V3 Discriminant)
3. **Causal relevance** — do the features (or subspaces) have causal effects on model behavior? ([I1 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency/), [I2 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity/))

These are answerable. "Are these the true features?" is not.

## Mechanistic validity criteria

| Criterion | Status | What it tells you |
|---|---|---|
| [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/) | Central | Do different SAE configurations agree? |
| [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance/) | Central | Are features stable across measurement choices (width, seed)? |
| [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | Critical | Can you distinguish trained-model features from noise-model features? |
| [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | Relevant | Where does one feature end and another begin? |

## See also

- [Decomposition Identity](/mechanistic-views/open-problems/decomposition-identity/) — the broader open problem this question belongs to
- [Superposition](/mechanistic-views/open-problems/superposition/) — the related question of whether superposition is a problem or a property
- [Subspace view](/mechanistic-views/views/subspace/) — the view that resolves the convergence question
- [Perspectival view](/mechanistic-views/views/perspectival/) — the view that predicts method-dependence
- ["MI Needs Philosophy"](https://arxiv.org/abs/2506.18852) §2.2 — vehicle/content distinction maps onto Object/Role for features ([full mapping](/mechanistic-views/open-problems/barez-philosophy/))

## Feature absorption

A concrete instance of this problem: [Bricken et al. (2023)](https://transformer-circuits.pub/2023/monosemantic-features/index.html) and subsequent work showed that safety-relevant SAE features can be *absorbed* into more general features at higher SAE widths. A "deception" feature at width 4096 may disappear at width 16384 — not because deception stopped being represented, but because the representation was redistributed across finer-grained features.

Under the Object view, this is alarming: a feature you were monitoring vanished. Under the Subspace view, it's expected: the subspace is stable even as the basis changes. The safety question becomes: is the *subspace* still detectable, even if the individual feature isn't? If yes, monitor the subspace, not the feature. If no, the representation genuinely changed — a much more serious concern that requires [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) evidence.

## Resolution status: **Dissolved**

The framework dissolves the question. "True features" is an Object-view concept applied to a domain where the Subspace view is more appropriate. The answerable questions are: do subspaces converge? (Grassmannian distance), are they causally relevant? (DAS/IIA), are they more than artifacts? (discriminant validity). These replace the unanswerable question "which features are true?"
