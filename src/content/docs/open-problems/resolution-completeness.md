---
title: "Resolution & Completeness"
---

# What are we missing?

Mechanistic interpretability has produced detailed accounts of induction heads, indirect object identification, greater-than comparison, and a handful of other circuits. How much of a model's behavior does this cover? The Apollo Research "complete model understanding" project (#31, #32) calls the unexplained fraction "dark matter" — model behavior that has no known mechanistic explanation. The honest answer is that known circuits explain a small fraction of what even GPT-2 Small does.

But "how much do we understand?" is not a well-posed question without specifying resolution. At a coarse resolution, you might say "we understand that layer 0 does token embedding, layers 1-5 build contextual representations, and layers 6-11 do task-specific computation." That's nearly 100% coverage at the resolution of "what does each layer group do?" Zoom in and ask "what does each attention head do?" and coverage drops. Zoom in further — "what does each feature in each head do on each input?" — and coverage is effectively zero. Both "we understand most of it" and "we understand almost none of it" are correct at different resolutions.

This is compounded by the distinction between capability and propensity. Steinhardt (2026) argues that the field measures *capabilities* (what the model can do at peak performance) but not *propensities* (what the model tends to do across a distribution of inputs). A model might have the capability to answer truthfully (there exists a mechanism for truthful recall) while having a propensity to confabulate (the mechanism fires inconsistently). Circuit analysis that shows "this circuit does truthful recall when active" is a capability finding. Whether the circuit actually fires when it should is a propensity finding — and almost no current work measures propensity.

## The view territory

Resolution-dependence is the defining feature of the [Stratified view](/mechanistic-views/views/stratified/). The Stratified view says: mechanisms exist at multiple resolutions simultaneously, and different resolutions reveal different structure. An attention head is a mechanism at one resolution. The QK circuit within that head is a mechanism at a finer resolution. The individual feature interactions within the QK circuit are mechanisms at a finer resolution still. Completeness is resolution-relative — always "complete at resolution X," never just "complete."

The capability-propensity distinction maps onto the [Instrumental](/mechanistic-views/views/instrumental/) vs. [Role](/mechanistic-views/views/role/) boundary. Capability findings are Instrumental: this mechanism can produce this behavior. Propensity findings require at least Role-level evidence: this mechanism is the one that *typically* produces this behavior in the model's normal operation, not just when experimentally activated.

## Mechanistic validity impact

| Criterion | Current status | What's missing |
|---|---|---|
| [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | **Unknown** — no systematic measure of how much behavior is explained | Requires resolution specification: "complete at which granularity?" |
| [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | **Incomplete** — mechanism boundaries depend on resolution | The same mechanism has different boundaries at different resolutions; current work doesn't specify which |
| [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability) | **Confused** — capability and propensity are conflated | "This circuit does X" conflates "can do X" with "tends to do X" — different operationalizations with different validity requirements |
| [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | **Untested** at most resolutions | A mechanism that is specific at one resolution may be non-specific at another |
| [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | **Resolution-dependent** — finer resolution means less parsimonious | There's a natural Pareto frontier between resolution and parsimony that the field hasn't characterized |

## Sources

- **Apollo Research (2024)** #31, #32: Complete model understanding, "dark matter" ([45+ MI Projects](https://www.alignmentforum.org/posts/KfkpgXdgRheSRWDy8))
- **[Steinhardt (2026)](https://www.lesswrong.com/posts/J5KkwYnnaeNX7hL2s/the-case-for-evaluating-model-behaviors)**: The case for evaluating model behaviors
- **Sharkey "Sparsify" (2024)**: Hierarchical abstraction, decompilation fidelity ([Sparsify agenda](https://www.alignmentforum.org/posts/64MizJXzyvrYpeKqm))
- **Sharkey et al. (2026)** §3.5: Microscope AI — extracting latent knowledge ([arXiv:2501.16496](https://arxiv.org/abs/2501.16496))
- **Nanda (2022)** §9: Learned features — functional types, universality, completeness ([200 Open Problems](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability))
