---
title: Case Study — Superposition
---

# Case Study — Superposition

The hypothesis that neural networks represent more features than they have dimensions — *superposition* — has become one of the central organizing problems in mechanistic interpretability. Substantial engineering effort has been directed at "solving" superposition, primarily through sparse autoencoders (SAEs) that project activations into higher-dimensional spaces where features are disentangled. But whether superposition is a *problem to be solved* depends on which mechanistic view one adopts. The framework reveals that the field's framing presupposes an ontological commitment that is rarely stated and never defended.

## Object view

Under the [Object view](/mechanistic-views/views/object/), features are discrete, countable parts of the model's representation. Superposition occurs when these parts are "compressed" into fewer dimensions than there are features, entangling them in the activation space. SAEs exist to undo this compression: by training a wide autoencoder with a sparsity penalty, one recovers a dictionary of monosemantic units, each corresponding to a single feature.

This framing encounters a difficulty it lacks the internal resources to resolve. Different SAE widths yield different feature sets: a single "San Francisco" feature in a 1M-latent SAE splits into two features at 4M and eleven fine-grained ones at 34M. Which width gives the "right" features? The Object view requires a determinate inventory of parts, but the inventory changes with dictionary width. No principled criterion within the view selects a canonical width.

## Subspace view

The [Subspace view](/mechanistic-views/views/subspace/) reframes features as subspaces rather than individual directions. Superposition is geometric: subspaces can overlap, and in high-dimensional spaces, approximate orthogonality is abundant enough that substantial overlap is expected. The question shifts from "how do we disentangle features?" to "how much do representational subspaces interfere, and does that interference degrade downstream computation?"

This reframing turns the SAE width problem into a measurable quantity. Different SAE widths correspond to different granularities of subspace decomposition, and the relationship between them can be characterized by Grassmannian distances between the recovered subspaces across widths and random seeds. If subspaces converge, they identify robust geometric structure; if they fragment, the decomposition at that granularity is an artifact.

## Structural view

If mechanistic structure is constituted by computational relationships rather than any particular parameterization, then superposition is a *gauge choice*: a consequence of the coordinate system in which we inspect the model, not an intrinsic property of the computation. Two models with different superposition patterns may implement identical input-output mappings and preserve identical computational invariants. What matters structurally is which computation is invariant under changes of basis.

## Perspectival view

The claim "neural networks are in superposition" presupposes that there exist discrete features being compressed into fewer dimensions — but this is the [Object view](/mechanistic-views/views/object/)'s ontology imposed as a universal empirical assumption. The canonical demonstration of superposition uses toy models trained to reconstruct sparse, known input features. In that setting, superposition is rigorously defined because the ground-truth features are specified by construction. But large language models were not trained to reconstruct a sparse feature dictionary; they were trained to predict tokens.

The [Perspectival view](/mechanistic-views/views/perspectival/) flags this as a circularity risk: SAEs are trained with a sparsity prior that *enforces* decomposition into discrete units, then the resulting dictionaries are taken as evidence that discrete features exist.

## Analysis

Each view gives a different answer to "what is superposition?":

| View | Superposition is... | Implication |
|---|---|---|
| [Object](/mechanistic-views/views/object/) | Real compression that must be solved | But the decomposition is *underdetermined* — no criterion selects the correct SAE width |
| [Subspace](/mechanistic-views/views/subspace/) | Testable geometry | Measure Grassmannian distances across widths and seeds to find which subspaces are robust |
| [Structural](/mechanistic-views/views/structural/) | A gauge choice | The productive question is what computation is invariant under reparameterization |
| [Perspectival](/mechanistic-views/views/perspectival/) | Theory-laden | The claim imports the Object view's ontology as an unstated assumption |

The field's substantial investment in "solving superposition" is coherent under the Object view, but it assumes that view is correct — an assumption that is rarely stated and never defended.

See also: [Superposition as open problem](/mechanistic-views/open-problems/superposition/) for how the framework clarifies the apparent disagreement in the literature.
