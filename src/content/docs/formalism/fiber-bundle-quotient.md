---
title: Fiber Bundle Quotient
---

# Fiber Bundle Quotient

The formalism for the [structural view](/mechanistic-views/views/structural/).

## What it is

A fiber bundle is a space that locally looks like a product of two spaces — a *base space* and a *fiber* — but may have nontrivial global structure. The base space represents the distinct states of the system; the fiber represents redundant degrees of freedom at each state.

A *quotient* by a group action collapses all points related by the group's symmetries into a single equivalence class. The fiber bundle quotient $\mathcal{W}/\mathcal{G}$ divides the space of all weight configurations $\mathcal{W}$ by the gauge group $\mathcal{G}$ — the symmetries that preserve the model's input-output function. Each point in the quotient represents a functionally distinct model, with all redundant parameterizations collapsed.

See [Fiber bundle](https://en.wikipedia.org/wiki/Fiber_bundle) and [Quotient space](https://en.wikipedia.org/wiki/Quotient_space_(topology)) on Wikipedia.

## Gauge symmetries in transformers

Transformers have symmetries that leave the input-output function unchanged:

- **Permutation symmetry**: swapping two attention heads and their weight matrices preserves function.
- **Rescaling symmetry**: simultaneously rescaling query and key weights by inverse factors preserves attention scores.
- **Rotation symmetry** (approximate): rotating the residual stream basis and all weight matrices that read from or write to it. Exact without LayerNorm; approximate with it.

These are the *gauge transformations*. Two weight configurations related by a gauge transformation implement the same computation — they are in the same fiber.

## How the structural view uses it

Under the structural view, a mechanism is a gauge-invariant property of the weights: something that depends only on the equivalence class $[\theta] \in \mathcal{W}/\mathcal{G}$, not on any particular representative $\theta$. Singular values of [OV circuits](https://learnmechinterp.com/topics/qk-ov-circuits/) $W^{OV}$, principal angles between subspaces, and effective rank are gauge-invariant. [Composition scores](https://learnmechinterp.com/topics/composition-and-virtual-heads/) are invariant under head permutations but not under the full rotation symmetry. Individual neuron activations and head indices are not gauge-invariant.

Two structural descriptions refer to the same mechanism when they lie in the same gauge orbit — when one can be transformed into the other by a sequence of gauge transformations.

The fiber bundle quotient also supports *holonomy*: a gauge-invariant fingerprint computed by parallel-transporting a subspace around a closed loop in weight space. Isomorphic holonomy groups are a necessary condition for cross-model mechanism identity.

## Deep dive

For the full mathematical treatment — fiber bundle construction, connection choices, holonomy computation, the freeness requirement, and tractability — see the [Gauge Quotients and Holonomy deep dive](/mechanistic-views/formalism/deep-dives/gauge-holonomy/).

## Relationship to other formalisms

The fiber bundle quotient is the most structurally rich formalism in the framework. The [Grassmannian](/mechanistic-views/formalism/grassmannian/) captures subspace identity but not the full gauge structure; the quotient captures both. The [Whitney stratification](/mechanistic-views/formalism/stratification/) organizes mechanisms by dimensionality within the stratified view, while the fiber bundle quotient organizes them by gauge orbit within the structural view — related but distinct classification schemes.
