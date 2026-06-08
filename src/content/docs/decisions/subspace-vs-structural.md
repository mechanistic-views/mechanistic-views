---
title: Subspace vs. Structural
---

# Subspace vs. Structural

**The fork.** Is Grassmannian identity (geodesic distance on $\mathrm{Gr}(k,d)$) sufficient, or is a gauge-invariant characterization required?

## Option A: [Subspace](/views/subspace/) identity

Two mechanisms are the same when their subspaces are close on $\mathrm{Gr}(k,d)$. See the [Grassmannian formalism](/formalism/grassmannian/) for the distance metric.

**When it goes wrong.** Two models in different gauge orbits may have nearby-looking subspaces because of basis coincidence — false positive. Two models in the same orbit may look different due to basis choice — false negative.

## Option B: [Structural](/views/structural/) identity

Two mechanisms are the same when they lie in the same gauge orbit. See the [fiber bundle quotient formalism](/formalism/fiber-bundle-quotient/).

**Technical conditions.** The fiber bundle structure (needed for holonomy) holds only when $\mathcal{G}$ acts freely — i.e., at generic points. At non-generic points (identical heads), only the quotient space structure applies, not the bundle. The holonomy criterion also depends on the connection choice.

**When it goes wrong.** If gauge normalization is impractical or holonomy cannot be computed, the structural view demands something the current toolkit cannot deliver.

## Distinguishing experiments

**Gauge normalization test.** Measure cross-seed Grassmannian distance before and after head-permutation alignment. If distance drops significantly, raw Grassmannian distance was confounded by gauge redundancy.

**Functional test.** Take two mechanisms with close Grassmannian distance but suspected different gauge orbits. Do they respond identically to the same causal queries? Behavioral divergence shows the Grassmannian distance was misleading.

## Recommended default

[Subspace view](/views/subspace/) for single-model claims and preliminary cross-model comparisons, with gauge normalization applied. [Structural view](/views/structural/) (with holonomy and generic-position check) for strong cross-model identity claims where computational cost is acceptable.
