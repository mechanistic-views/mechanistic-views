---
title: Subspace vs. Structural
---

# Subspace vs. Structural

**The fork.** When comparing mechanisms across models, is it enough to check that their subspaces are close, or do you need a characterization that accounts for internal symmetries of the network?

This decision matters whenever you compare two models that may represent the same computation in different coordinate systems. Transformers have internal symmetries -- you can permute attention heads within a layer, or apply certain rotations to weight matrices, without changing the model's input-output behavior. These symmetry transformations form what is called a *gauge orbit*: the set of all weight configurations that compute the same function.

## When you face this decision

Suppose you have trained two copies of GPT-2 Small from different seeds. You run DAS (Distributed Alignment Search) on both and find subspaces for a "gender" variable in the residual stream. The two subspaces are close on the Grassmannian (the mathematical space of linear subspaces -- measured by the angles between them). Can you conclude the two models represent gender the same way?

Maybe. Or maybe the proximity is a coincidence of the coordinate systems the two models happened to land in. Without accounting for the gauge symmetry, you cannot distinguish "genuinely similar representation" from "similar-looking by accident of basis."

## Option A: Subspace identity

Two mechanisms are the same when their subspaces are close on the Grassmannian $\mathrm{Gr}(k, d)$, measured by principal angles. This is the natural criterion for DAS-style analyses: DAS finds a projector $QQ^\top$ that is already invariant under rotations *within* the subspace, so the subspace itself is a coordinate-free object.

**What it buys you.** Practical tractability. Grassmannian distance is straightforward to compute, has well-understood statistics (random matrix baselines from Marchenko-Pastur theory), and integrates directly with existing DAS tooling.

**What goes wrong.** Two models in different gauge orbits may have nearby-looking subspaces because of basis coincidence -- a false positive. Conversely, two models in the *same* gauge orbit may look different because their weight matrices happen to put the same subspace in different coordinates -- a false negative. Raw Grassmannian distance without gauge alignment conflates representational similarity with coordinate similarity.

## Option B: Structural identity

Two mechanisms are the same when they lie in the same gauge orbit -- that is, when one can be transformed into the other by applying the network's internal symmetries (head permutations, certain rotational symmetries). This is captured formally by the fiber bundle quotient construction: the space of weight configurations modulo gauge transformations.

**What it buys you.** A characterization that is genuinely invariant to internal symmetries. If two models are in the same gauge orbit, they compute the same function in a strong sense, and any subspace-level comparison that says otherwise is misleading.

**What goes wrong.** Computing gauge orbits and holonomy (a measure of how the gauge connection "twists" around the orbit) is expensive and currently requires specialized tooling that most practitioners do not have. The fiber bundle structure also breaks down at non-generic points -- for example, when two attention heads in the same layer have identical weights, the gauge group does not act freely, and the bundle formalism does not apply cleanly. If you cannot actually compute the structural characterization, demanding it just blocks progress.

## Distinguishing experiments

**Gauge normalization test.** Measure cross-seed Grassmannian distance before and after head-permutation alignment (reordering heads to minimize distance). If the distance drops significantly after alignment, the raw Grassmannian distance was confounded by gauge redundancy, and the subspace view alone was misleading.

**Functional divergence test.** Find two mechanisms with close Grassmannian distance but suspected different gauge orbits. Run the same causal interventions (e.g., activation patching on the same prompts) on both. If they respond differently despite similar subspaces, the Grassmannian distance was a false positive -- the subspace similarity did not reflect functional similarity.

## Recommended default

Use the **subspace view** for single-model analyses and preliminary cross-model comparisons. It is the more practical starting point, and for many research questions it is sufficient. Apply gauge normalization (head-permutation alignment) before comparing across seeds or models -- this is cheap and eliminates the most common source of false positives.

Use the **structural view** for strong cross-model identity claims where you need to rule out basis coincidence. This is warranted when the stakes are high (e.g., claiming that two architectures implement the same mechanism) and when the computational cost of gauge-orbit analysis is acceptable. Be honest about the current limitations: if you cannot compute holonomy or verify the generic-position condition, say so.
