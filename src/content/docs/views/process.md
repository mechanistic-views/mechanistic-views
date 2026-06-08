---
title: Process View
---

# Process View

The process view treats mechanisms as temporally extended processes with characteristic formation histories. The current circuit is the end state of a training process; that process is part of the mechanism's description.

## Thesis

A mechanism is a process that forms over training and is individuated in part by its formation history: when it forms, what it depends on, what must precede it.

## What exists

Checkpoint trajectories, formation events, developmental prerequisites. The mechanism at time $t$ is the state of the process at $t$, not the static object it converges to.

## Identity

Two mechanisms are the same if they have the same formation process — specifically, if they share the same formation event type, developmental prerequisites, and formation criterion timing. This must be cashed out concretely: "same formation process" is not defined by loss trajectory similarity alone (many distinct mechanisms can share a loss curve shape) but by convergence of the process-view evidence: same AGOP subspace trajectory, same formation criterion timing across seeds, same developmental dependency structure.

Cross-seed identity under the process view requires: the formation event (phase transition, AGOP convergence, weight-space asymptote) occurs at the same relative training step, in the same order relative to other events, with the same prerequisites. Two mechanisms that form by different routes to the same final static structure are distinct under the process view but identical under the static views — this is a genuine empirical disagreement between views, not just a terminological one.

## Evidence

- **Checkpoint analysis**: subspace estimates ([DAS](https://learnmechinterp.com/topics/causal-abstraction/) or [AGOP](https://arxiv.org/abs/2110.04005)) measured across training steps
- **AGOP trajectories**: convergence to eventual causal subspace — empirically observed to precede behavioral detection in some cases (Nanda et al., grokking), but whether this generalises to arbitrary mechanisms is not established
- **Phase transitions**: sudden changes in IIA, [composition score](https://learnmechinterp.com/topics/composition-and-virtual-heads/), or behavior
- **Knockout retraining**: train a model with a proposed prerequisite component permanently ablated (a *training-time* intervention, not inference-time ablation) — if the target mechanism then fails to form, the prerequisite is established; if it forms anyway via a different route, the prerequisite claim is falsified

The **formation criterion** must be stated explicitly, because different criteria (behavioral threshold, AGOP convergence, weight-space structure) can disagree in timing. The process view should specify which criterion is used.

## Formalism

[Dynamical systems](/formalism/dynamical-system/) on weight space, [AGOP](https://arxiv.org/abs/2110.04005), training-time subspace estimation. The formation event corresponds to a trajectory crossing a boundary in mechanism space $\mathcal{M}$.

## What it explains

[Grokking](/cases/grokking/): the phase transition is the formation event of the Fourier generalization mechanism, preceded by a memorization phase. [Induction head](/cases/induction/) emergence: the sudden formation corresponds to a developmental event with a prerequisite (previous-token head formation). These phenomena are not visible from static views.

## What it lets you prove

- **Formation order**: mechanism A forms before mechanism B across seeds
- **Developmental prerequisite**: ablating component X prevents mechanism Y from forming
- **Lead time**: AGOP convergence precedes behavioral detection by $\Delta t$ steps

## Failure modes

**Computationally expensive.** Requires checkpoint analysis across many training runs.

**Formation criterion ambiguity.** Different criteria give different formation times; the choice changes the claim.

**Overreach.** Describing the training trajectory is not always part of explaining the final mechanism. The process view is needed when the phenomenon is inherently dynamic, not by default.

## Relationship to Mechanistic Validity

Adds a dimension that static views cannot address: the explanatory relevance of training history. Required for claims about emergence, phase transitions, or developmental dependencies. Formation criteria should be part of the construct validity statement.

## Further reading

- Nanda et al., "Progress measures for grokking via mechanistic interpretability" (2023) — AGOP-like progress measures track mechanism formation before behavioral detection, see [Grokking case study](/cases/grokking/)
- Olsson et al., "In-context Learning and Induction Heads" (2022) — induction head formation as a developmental event with prerequisites, see [Induction case study](/cases/induction/)
- For related views: [Object view](/views/object/) and [Subspace view](/views/subspace/) describe the static end-state; the process view describes how it got there. [Stratified view](/views/stratified/) also tracks mechanism dimensionality but at a fixed time point, not across training
