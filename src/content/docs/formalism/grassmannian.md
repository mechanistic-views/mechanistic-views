---
title: Grassmannian
---

# Grassmannian

The formalism for the [subspace view](/views/subspace/).

## What it is

The Grassmannian $\mathrm{Gr}(k, d)$ is the space of all $k$-dimensional linear subspaces of $\mathbb{R}^d$. Each point in this space is an entire subspace — not a single vector, but a $k$-dimensional flat plane through the origin.

The Grassmannian is a smooth, compact manifold of dimension $k(d-k)$. It has a natural notion of distance: the *geodesic distance* between two subspaces, computed from their [principal angles](https://en.wikipedia.org/wiki/Principal_angles). Two subspaces are close when they are nearly parallel; they are far apart when they are nearly orthogonal.

See [Grassmannian](https://en.wikipedia.org/wiki/Grassmannian) on Wikipedia.

## Why subspaces, not vectors

Distributed alignment search (DAS) recovers a matrix $Q \in \mathbb{R}^{d \times k}$ such that intervening on $QQ^\top x$ transfers a causal variable. But $Q$ and $QR$ produce the same projector for any rotation $R \in O(k)$. The method identifies a subspace — a column span — not a specific basis. The natural space of such objects is the Grassmannian.

## How the subspace view uses it

Under the subspace view, a mechanism is a point in $\mathrm{Gr}(k, d)$: a $k$-dimensional subspace of the residual stream that causally mediates a high-level variable. Two descriptions refer to the same mechanism when they identify the same (or nearby) point in the Grassmannian — when the geodesic distance $d_{\mathrm{Gr}}$ between them is below a threshold.

Distance in the Grassmannian gives cross-model comparison a precise meaning: "do these two models represent the same variable?" becomes "how far apart are the recovered subspaces?" — a number, not a judgment call.

## Subspace stability

A mechanism claim under the subspace view is only as strong as the stability of the recovered subspace. If the subspace changes substantially across random seeds, prompt distributions, or model checkpoints, the claim is not about a stable structure — it is about an artifact of a particular run.

Stability is measured using the *Fréchet variance* on the Grassmannian: recover the subspace under multiple conditions, compute the Fréchet mean (the subspace minimizing total squared geodesic distance to all estimates), and report the variance. Low Fréchet variance means the subspace is stable; high variance means the evidence is unreliable.

Cross-seed consistency (same training data, different random seeds) tests measurement reliability. Cross-prompt consistency (same model, different input distributions) tests whether the subspace generalizes beyond the distribution used to find it. Both are required for a subspace claim to be considered established.

See the [deep dive](/formalism/deep-dives/grassmannian/#fréchet-mean-and-variance) for the mathematical definition and computation.

## Deep dive

For the full mathematical treatment — principal angles, transport maps, Fréchet mean and variance, computational tractability — see the [Grassmannian Geometry deep dive](/formalism/deep-dives/grassmannian/).
