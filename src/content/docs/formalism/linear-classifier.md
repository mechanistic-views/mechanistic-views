---
title: Linear Classifier
---

# Linear Classifier

A method-level formalism used by linear probing.

## What it is

A linear classifier is a function $f(x) = \text{sign}(w^\top x + b)$ (for binary classification) or $f(x) = \text{softmax}(Wx + b)$ (for multi-class), where $x$ is an activation vector. It partitions the representation space into regions separated by hyperplanes.

The key idea: if a linear classifier trained on a model's internal activations can predict a high-level variable (e.g., "is the subject plural?"), then the information about that variable is *linearly accessible* at that layer — it can be read off by a simple projection without nonlinear decoding.

See [Linear classifier](https://en.wikipedia.org/wiki/Linear_classifier) on Wikipedia.

## How it is used in interpretability

Linear probing trains a linear classifier on a model's intermediate activations to test whether a concept is linearly represented. High probe accuracy is taken as evidence that the model encodes the concept at that layer.

The limitation: linear accessibility is observational, not causal. A probe can achieve high accuracy on information the model does not actually use in its computation. Probing establishes that information is *present*, not that it is *causally active*. Causal methods like DAS or activation patching are needed to establish the latter.
