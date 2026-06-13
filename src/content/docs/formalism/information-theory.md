---
title: Information Theory
---

# Information Theory

A cross-cutting formalism used by the [object](/mechanistic-views/views/object/), [role](/mechanistic-views/views/role/), and [subspace](/mechanistic-views/views/subspace/) views.

## What it is

Information theory quantifies how much one variable tells you about another. The central quantity is mutual information: $I(X; Y) = H(X) - H(X \mid Y)$, the reduction in uncertainty about $X$ when you observe $Y$. Channel capacity is the maximum mutual information achievable over all input distributions. Entropy $H(X) = -\sum_x p(x) \log p(x)$ measures the intrinsic uncertainty of a variable.

These are distribution-level quantities. They describe what a system *can* transmit, not what it *does* transmit on any particular input. This distinction matters in interpretability: a component may have high capacity for transmitting gender information but rarely use it.

See [Information theory](https://en.wikipedia.org/wiki/Information_theory) on Wikipedia.

## How it is used in interpretability

Information-theoretic measures appear in several roles. Probing mutual information asks how much a representation at layer $l$ tells you about a target variable (syntax, entity type, sentiment). Information bottleneck methods compress representations to find the minimal sufficient statistic for a downstream task. Causal information flow measures how much a component's output changes the model's uncertainty about the answer.

The limitation: mutual information is symmetric, non-negative, and observational. High $I(\text{hidden state}; \text{concept})$ means the concept is *encoded* in the representation, not that the model *uses* it. A representation can carry information about gender, part of speech, and token frequency simultaneously, and probing for any one of them yields high mutual information. Causal tests (ablation, patching) are needed to establish that the information is actually read out downstream.

Information-theoretic measures also depend on the choice of target variable, which is defined by the researcher, not the model. The same representation has different mutual information with different targets.

## Relationship to other formalisms

Information theory quantifies what the [linear classifier](/mechanistic-views/formalism/linear-classifier/) detects: a probe with high accuracy implies high mutual information, but the converse is not always true (information may be encoded nonlinearly). The [Grassmannian](/mechanistic-views/formalism/grassmannian/) provides a geometric view of the same structure: a $k$-dimensional subspace that maximizes explained variance for a concept is closely related to the subspace that maximizes mutual information with it.

The [dictionary](/mechanistic-views/formalism/dictionary/) formalism decomposes activations into sparse features, each of which can be evaluated information-theoretically: how much mutual information does feature $i$ carry about concept $c$?

## Further reading

- Voita et al., "Information-Theoretic Probing with Minimum Description Length" (2020) -- MDL probing as a tighter information bound
- Hewitt and Liang, "Designing and Interpreting Probes with Control Tasks" (2019) -- selectivity as the gap between task and control probe accuracy
- Geiger et al., "Causal Abstraction for Faithful Model Interpretation" (2021) -- causal information flow via interchange interventions
- See the [methods page](/mechanistic-views/methods/) for how information-theoretic probing relates to other evidence types
