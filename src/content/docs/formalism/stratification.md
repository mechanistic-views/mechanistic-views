---
title: Whitney Stratification
---

# Whitney Stratification

The formalism for the [stratified view](/mechanistic-views/views/stratified/).

## What it is

A stratified space is a topological space decomposed into smooth pieces called *strata*, arranged so they fit together in a controlled way. A *Whitney stratification* adds two regularity conditions (Whitney A and B) that prevent the strata from meeting in geometrically pathological ways — they ensure the decomposition behaves predictably under perturbation.

The canonical example: consider all subspaces of $\mathbb{R}^d$ of all dimensions simultaneously. The 1-dimensional subspaces form one smooth piece, the 2-dimensional subspaces form another, and so on. A sequence of 2-dimensional subspaces can converge to a 1-dimensional subspace (as one direction collapses), so these pieces are not disjoint manifolds — they are strata of a single stratified space.

See [Whitney conditions](https://en.wikipedia.org/wiki/Whitney_conditions) and [Stratification](https://en.wikipedia.org/wiki/Stratification_(mathematics)) on Wikipedia.

## How the stratified view uses it

Under the stratified view, mechanism space is not a single manifold but a stratified space:

$$\mathcal{M} = \mathcal{M}_1 \sqcup \mathcal{M}_2 \sqcup \cdots \sqcup \mathcal{M}_d \sqcup \mathcal{M}_\infty$$

Each $\mathcal{M}_k$ contains mechanisms that live in a $k$-dimensional subspace; $\mathcal{M}_\infty$ contains genuinely distributed mechanisms with no finite-dimensional representative. A mechanism's identity depends on which stratum it occupies: two mechanisms in $\mathcal{M}_k$ are compared by Grassmannian distance, but a mechanism in $\mathcal{M}_2$ and one in $\mathcal{M}_5$ are not comparable in the same way — they live in different strata with different local geometry.

The stratified view is resolution-relative: the same computation may appear as a point in $\mathcal{M}_k$ at one resolution and $\mathcal{M}_{k'}$ at another. The Whitney conditions ensure that moving between resolutions (crossing stratum boundaries) is geometrically well-behaved.

## Deep dive

For the full mathematical treatment — Whitney conditions A and B, the frontier condition, Thom-Mather control data, the $\mathcal{M}_\infty$ stratum, and computational tractability — see the [Stratification deep dive](/mechanistic-views/formalism/deep-dives/stratification/).
