---
title: Causal Graph
---

# Causal Graph

A method-level formalism used by causal scrubbing and causal abstraction.

## What it is

A causal graph (or structural causal model, SCM) is a directed acyclic graph where nodes represent variables and edges represent direct causal relationships. Each node's value is determined by its parents in the graph plus an independent noise term. The graph encodes which interventions are possible and what their effects should be.

The key idea: the graph separates the *structure* of causal relationships (which variables influence which) from the *mechanisms* that implement each relationship (the functional form). Intervening on a node means setting its value regardless of its parents — the do-operator in Pearl's framework.

See [Structural causal model](https://en.wikipedia.org/wiki/Structural_causal_model) and [Causal graph](https://en.wikipedia.org/wiki/Causal_graph) on Wikipedia.

## How it is used in interpretability

Causal scrubbing and causal abstraction both require a *pre-specified* causal graph — a hypothesis about the high-level computation the model performs. The method then tests whether the model's internal activations are consistent with this graph by performing interventions that should be independent under the graph and checking whether the model's behavior respects those independences.

The formalism does not discover the graph; it tests a proposed one. The result depends on which graph is proposed — a different graph produces a different verdict. This is both the method's strength (it tests a specific structural hypothesis) and its limitation (the result is conditional on the hypothesis).

## Relationship to other formalisms

The causal graph is a high-level formalism — its nodes are variables like "subject gender" or "indirect object identity", not model components. The [directed graph](/formalism/directed-graph/) used by the [object view](/views/object/) places model components (heads, MLPs) as nodes instead. The [role graph](/formalism/role-graph/) is intermediate: its nodes are functional roles that abstract away from specific components but are more fine-grained than causal variables.

## Further reading

- Pearl, *Causality* (2009) — the foundational treatment of SCMs and the do-operator
- Geiger et al., "Causal Abstraction for Faithful Model Interpretation" (2021) — applies causal graphs to neural network interpretability
- See the [methods page](/methods/) for how causal graphs are used in [DAS/IIA](https://learnmechinterp.com/topics/causal-abstraction/) and [causal scrubbing](https://learnmechinterp.com/topics/causal-abstraction/)
