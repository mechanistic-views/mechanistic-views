---
title: Role Graph
---

# Role Graph

The formalism for the [role view](/views/role/).

## What it is

A role graph is a directed graph whose nodes are functional roles rather than specific components. Where a circuit graph (the [object view's formalism](/formalism/directed-graph/)) labels nodes with concrete component identities (head 9.9, MLP 10), a role graph labels nodes with the function each component performs — "duplicate token detector", "S-inhibition head", "name mover."

The edges in a role graph represent functional dependencies: the output of one role feeds into another. The structure is the same as a directed graph, but the semantics are different — the nodes are abstract roles that any component could fill, not fixed component identities.

See [Functional decomposition](https://en.wikipedia.org/wiki/Functional_decomposition) on Wikipedia for the general idea of decomposing a system into functional roles.

## How the role view uses it

Under the role view, a mechanism is a functional decomposition: a set of roles and the dependencies between them. The role graph is the natural formalism because it represents the functional structure while abstracting away which specific components fill each role.

Two role-level descriptions refer to the same mechanism when they have the same role graph — the same functional roles connected by the same dependencies — regardless of which components fill those roles. Head 9.9 in model A and head 7.3 in model B can be the same mechanism if they play the same role in the same functional structure.

This is what makes the role view useful for cross-model comparison: the role graph can be the same across models even when the component identities are completely different. It is also what makes role claims harder to falsify — the functional labels must be independently specified, not just read off the same activations used to identify the components.

## Relationship to other formalisms

The role graph and the [directed graph](/formalism/directed-graph/) are structurally identical (both are DAGs). The difference is semantic: directed graph nodes are component identities (head 9.9), role graph nodes are functional labels (name-mover). The [causal graph](/formalism/causal-graph/) is more abstract still — its nodes are high-level causal variables (subject gender), not model components or functional roles. See the [IOI case study](/cases/ioi/) for a concrete example where the same circuit is described at all three levels.
