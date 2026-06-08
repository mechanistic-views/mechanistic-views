---
title: Directed Graph
---

# Directed Graph

The formalism for the [object view](/views/object/).

## What it is

A directed graph (digraph) is a set of nodes connected by directed edges. Each edge has a source and a target, representing a one-way relationship. A *circuit* in the interpretability sense is a directed graph: the nodes are components (attention heads, MLP layers, embedding, unembedding) and the edges are information-flow paths through the residual stream.

See [Directed graph](https://en.wikipedia.org/wiki/Directed_graph) on Wikipedia.

## How the object view uses it

Under the object view, a mechanism is a concrete set of components in a specific model. The directed graph is the natural formalism because it represents exactly what the object view claims exists: particular components connected by particular information-flow paths.

The nodes are specific components — head 9.9 in layer 9, MLP 10, the embedding matrix. The edges represent which components' outputs are read by which downstream components. The circuit *is* the subgraph: the claim is that this set of nodes and edges, and no others, implements the behavior.

Two object-level descriptions refer to the same mechanism when they share sufficient component overlap — when the subgraphs have the same (or sufficiently overlapping) nodes and edges.

Circuit discovery methods like activation patching, ACDC, and edge attribution patching all produce directed graphs as output. This is why the object view is implicit in most circuit-discovery work: the methods already speak the language of the formalism.
