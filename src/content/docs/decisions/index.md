---
title: Decisions
---

# Decisions

Mechanistic interpretability forces you to make choices about what kind of thing a "mechanism" is before you run your first experiment. These choices are often implicit -- buried in method selection or inherited from a prior paper. The decision pages make them explicit.

Each page examines a fork where different views lead to different experiments, different claims, and different failure modes. They are organized around the practical question: **given my research goal, which view should I adopt?**

- **[Object vs. Role](object-vs-role/)** -- Is the mechanism a specific component (head 9.1) or the functional role it plays (name-moving)? This determines whether your findings generalize across model seeds and architectures.

- **[Subspace vs. Structural](subspace-vs-structural/)** -- Is subspace proximity sufficient for mechanism identity, or do you need gauge-invariant characterization? This matters whenever you compare mechanisms across models that may differ by an internal symmetry transformation.

- **[Localized vs. Distributed](localized-vs-distributed/)** -- Can the mechanism be assigned to a compact circuit, or is it spread across the network? This determines whether circuit discovery methods can recover your mechanism at all.

- **[Single-Method vs. Triangulated](single-vs-triangulated/)** -- When is one strong experiment enough, and when do you need converging evidence from independent domains? This determines the strength of the claims you can make.

- **[Static vs. Process](static-vs-process/)** -- Should the mechanism be described as a final-state object, or does its formation history matter? This determines whether you need checkpoint data and dynamics-domain evidence.
