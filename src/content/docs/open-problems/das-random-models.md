---
title: "DAS in Random Models"
---

# Why Does DAS Find Subspaces in Untrained Models?

**The question.** Distributed Alignment Search finds subspaces that pass interchange-intervention accuracy in models that have learned nothing. Sutter et al. (2025) show that unrestricted nonlinear alignment achieves 100% IIA on randomly initialized transformers, which means a high IIA score by itself certifies nothing about the model.

**What the framework says.** This is a [Perspectival view](/mechanistic-views/views/perspectival/) prediction, not an anomaly. Unrestricted nonlinear alignment always finds structure, because the alignment map has enough degrees of freedom to map any activations onto any target variable. What the score measures is the map's flexibility. What it finds in a real model therefore needs stronger validation than the score itself supplies.

**What follows for the subspace view.** A [Subspace view](/mechanistic-views/views/subspace/) claim stands only under a restricted alignment class — either linear alignment, or alignment constrained to respect the transport structure induced by the weight matrices — with the eigenvalue gap reported alongside. Without that restriction the identity criterion has no content: any two subspaces can be made to agree.

## Resolution status: **Clarified**

The question becomes answerable once the view is specified. Under the perspectival view a high IIA on a random model is the expected reading of an unconstrained instrument. Under the subspace view it is a control that the claim must clear, and clearing it requires naming the alignment class before the measurement.

## Sources

- **Sutter et al. (2025)**: The non-linear representation dilemma — is causal abstraction enough for mechanistic interpretability? ([NeurIPS 2025](https://arxiv.org/abs/2507.08802))
- **Geiger et al. (2024)**: DAS / Boundless DAS / causal abstraction with linear subspaces
