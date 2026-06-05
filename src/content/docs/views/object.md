---
title: Object View
---

# Object View

The object view treats mechanisms as concrete parts of a model: attention heads, neurons, features recovered by a sparse autoencoder, or small sets of such components.

## Thesis

A mechanism is a localized object or collection of objects whose activity or weights are responsible for a target behavior.

## What exists

Architectural or learned units: heads, neurons, SAE features. The view is strongest when the relevant computation is sparse, stable across prompts and seeds, and concentrated in a small number of components.

## Identity

Two mechanisms are the same when they share the same relevant parts, or when their parts are functionally interchangeable under a well-specified criterion.

## Evidence

Intervention on the proposed component:
- Ablation and mean-ablation (necessity — removing component destroys behavior)
- Activation patching (replacing a component's activations from one forward pass into another; tests whether the source-pass behavior is sufficient to cause target-pass output change)
- Path patching (tests specific information-flow paths; note this is also used under the role view for path-level role attribution, not just component-level testing)
- Dose-response tests (causal dependence is graded, not binary)
- Minimal sufficiency tests

A claim is stronger when independent intervention protocols converge on the same component set.

## Formalism

Graph or set-theoretic circuit description. Standard causal graphs (Pearl, 2009) apply directly.

## What it explains

Causal-mechanical explanations: which parts matter, and how changing them changes behavior.

## What it lets you prove

- **Necessity**: removing the component destroys the target behavior
- **Sufficiency**: transplanting the component is sufficient to produce the behavior
- **Minimality**: no proper subset suffices
- **Circuit recovery**: under the object view, edge recovery achieves high precision and recall when mechanisms are genuinely sparse and localized — the prerequisite for component-level circuit description. If a role partition is required to achieve high precision/recall, this indicates the role view is more appropriate (see [Role View](role/))

## Semantics of object-view claims

The claim "head 4.4 implements name-moving" should be read as a *dispositional* claim, not a categorical one. It means: head 4.4 reliably activates in name-moving contexts *and* its ablation impairs name-moving performance. It does not mean the head is in some intrinsic state of "name-moving-ness" independent of the context. The two conditions together establish a bi-directional dependency that is the nearest practical analogue to constitutive relevance.

This matters because the purely correlational reading ("head 4.4 is active when name-moving occurs") is much weaker and does not support causal claims. The dispositional reading requires both the observational condition (activation pattern) and the interventional condition (ablation effect). A claim that cites only one of these is underdetermined: high activation without ablation evidence might reflect correlation with a correlated variable; ablation evidence without activation evidence might reflect indirect effects.

## Failure modes

**Distributed mechanisms.** If computation is distributed, no single object will be both necessary and sufficient.

**Coordinate artifacts.** A neuron may look privileged because of parameterization, not because computation is intrinsically localized there. Rotating the basis can move the apparent mechanism without changing the function.

**Backup circuits.** Ablating one component may not impair behavior because a backup engages, producing false negatives for necessity.

## Relationship to MechVal

Aligns well with causal and internal validity criteria. Needs measurement validity (stability across seeds) and external validity (cross-context generalization).
