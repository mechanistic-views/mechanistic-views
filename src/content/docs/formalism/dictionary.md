---
title: Dictionary
---

# Dictionary

A method-level formalism used by sparse autoencoders (SAEs) and dictionary learning.

## What it is

A dictionary is a set of vectors $\{d_1, \ldots, d_m\}$ in $\mathbb{R}^d$ (typically $m \gg d$, an overcomplete basis) such that any activation $x$ can be approximated as a sparse linear combination: $x \approx \sum_i c_i d_i$ where most coefficients $c_i$ are zero. Each dictionary element is a *feature direction*.

The key idea: the model's activations live in a $d$-dimensional space but the "true" features are more numerous than $d$ — they form a sparse, overcomplete code. The dictionary recovers these features by finding directions that are used sparsely but frequently across the data.

See [Sparse dictionary learning](https://en.wikipedia.org/wiki/Sparse_dictionary_learning) on Wikipedia.

## How it is used in interpretability

Sparse autoencoders (SAEs) learn a dictionary of features from a model's activations. Each feature is a direction in activation space, and the sparsity constraint encourages each activation to be explained by a small number of features. The hope is that these features correspond to interpretable concepts.

The limitation: the sparsity objective optimizes for *reconstruction* quality, not *causal* relevance. A feature that helps reconstruct activations may not be causally active in the model's computation. Feature splitting (one concept spread across multiple dictionary elements) and feature absorption (multiple concepts merged into one element) complicate the mapping between dictionary features and functional units. Causal validation — e.g., steering with a feature direction and observing the predicted behavioral change — is needed to establish that a dictionary feature is a mechanism, not just a statistical pattern.
