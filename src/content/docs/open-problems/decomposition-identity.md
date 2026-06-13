---
title: "Decomposition Identity"
---

# Which decomposition is real?

Train a sparse autoencoder with 4,096 features and you find a "Python code" feature. Train one with 32,768 features on the same model and that feature splits into "Python imports," "Python f-strings," "Python list comprehensions," and a dozen more. Scale down and they merge back. Which is the real decomposition — the coarse one or the fine one?

This is the decomposition identity problem, and it is arguably the most consequential open question in mechanistic interpretability. Anthropic's scaling monosemanticity program (Templeton et al. 2024) trained SAEs at massive scale on Claude 3.5 Sonnet and found millions of interpretable features. But the features you find depend on the dictionary width, the sparsity penalty, and the training procedure. Change these hyperparameters and you get a different decomposition of the same model. The features are not unique.

The problem goes deeper than hyperparameter sensitivity. SAEs can find interpretable-looking features even in random activations. The Apollo Research random direction baseline (project idea #7) showed that arbitrary directions in activation space can receive plausible natural-language explanations — the interpretability is partly in the labeling procedure, not the direction. If your method always finds features regardless of whether there's real structure, the features it finds in a real model need stronger validation than "they look interpretable."

## The view confusion

The [Object view](/mechanistic-views/views/object/) assumes mechanisms are discrete, identifiable components. Under this view, features are the fundamental units of neural network computation, and the goal of interpretability is to enumerate them. Feature splitting is a problem because it means the enumeration depends on resolution — there is no single correct list of features.

The [Subspace view](/mechanistic-views/views/subspace/) resolves this: the *subspace* spanned by a cluster of split features is what's real. How you decompose that subspace into basis directions is gauge freedom — like choosing Cartesian vs. polar coordinates to describe the same space. The subspace is invariant; the basis is a choice. Under this view, feature splitting is not a problem but a *prediction*: rotating between equivalent bases of the same subspace should yield the same downstream effects.

The [Perspectival view](/mechanistic-views/views/perspectival/) offers a sharper critique: if SAEs find features in noise, then what they find in real models is at least partly method artifact. The decomposition is not "in the model" — it's a projection of the analysis procedure onto the model. Under this view, the right response isn't to find the "correct" decomposition but to measure which aspects of the decomposition are robust across methods.

## Mechanistic validity impact

| Criterion | Under Object view | Under Subspace view |
|---|---|---|
| [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/) | **Impossible** — different SAE widths yield different features, no convergence | **Possible** — different decompositions should span the same subspace |
| [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance/) | **Impossible** — features change with hyperparameters | **Covered** — subspace is hyperparameter-invariant (testable via Grassmannian distance) |
| [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | **Violated** — SAEs find features in noise, can't discriminate real from artifact | **Possible** — real subspaces should be distinguishable from random subspaces by stability |
| [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality) | **Violated** — no principled boundary between one feature and its splits | **Possible** — subspace dimensionality gives a natural boundary |

The decomposition identity problem makes four validity criteria impossible or violated under the Object view. All four become possible or covered under the Subspace view. This is the single largest validity gain from moving up one level on the commitment ladder.

## Sources

- **Sharkey et al. (2026)** §2.1.2: SDL limitations, reconstruction errors, sparsity as proxy ([arXiv:2501.16496](https://arxiv.org/abs/2501.16496))
- **Nanda (2022)** §4: Polysemanticity and superposition problems ([200 Open Problems](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability))
- **Apollo Research (2024)** #7, #18, #19: Feature splitting structure, continuous vs. discrete ([45+ MI Projects](https://www.alignmentforum.org/posts/KfkpgXdgRheSRWDy8))
- **Sharkey "Sparsify" (2024)**: Decompilation fidelity, hierarchical abstraction ([Sparsify agenda](https://www.alignmentforum.org/posts/64MizJXzyvrYpeKqm))
- **Templeton et al. (2024)**: Scaling monosemanticity on Claude 3.5 Sonnet
- **Bricken et al. (2023)**: Towards monosemanticity (original SAE features paper)
- **Cunningham et al. (2023)**: Sparse autoencoders find interpretable features in language models
- **Williams, Oldenburg, Dhar et al. (2026)**: "MI Needs Philosophy" §2.1 — no single correct decomposition; "explanatory pluralism" ([full mapping](/mechanistic-views/open-problems/barez-philosophy/))
