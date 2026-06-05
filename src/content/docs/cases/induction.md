---
title: Case Study — Induction Heads
---

# Case Study: Induction Heads

**The phenomenon.** Induction heads implement prefix matching: given $[A][B]\ldots[A]$, predict $[B]$. Olsson et al. (2022) described them in detail and proposed they underlie in-context learning.

## Object view

A previous-token head writes the previous token's identity to the residual stream; an induction head queries for tokens whose preceding context matches the current position. Ablating identified heads impairs next-token prediction on repeated sequences; composition score between the pair is high.

## Role view

A two-role structure: (copy-previous role, attend-to-matching-prefix role). Different models implement these roles with different specific heads. Cross-model role transfer qualitatively established.

## Subspace view

The induction variable is approximately the identity of the token to be predicted. This occupies a subspace at the output of the induction head's OV circuit.

**Outstanding.** DAS has not been systematically applied to recover this subspace and measure its Grassmannian distance from the $W^{OV}$ SVD subspace.

## Process view

Olsson et al. (2022) showed induction heads form suddenly at a specific training step — a phase transition with a sharp loss decrease. Before, in-context learning is near-absent; after, it is present.

The process-view claim: this corresponds to a formation event — the mechanism appears suddenly rather than accumulating smoothly, suggesting a phase transition in the weight-space trajectory rather than gradual construction. The pre-transition state is not necessarily distributed (it may simply be the absence of the mechanism); the stratum-change interpretation requires evidence that the pre-transition model has a different positive mechanism rather than the absence of one. AGOP trajectories are the natural evidence source for distinguishing these.

**Formation criterion.** The transition is detected behaviorally (IIA threshold). AGOP convergence may precede this; characterizing the lead time is open.

## Current evidence state

- **Tier 3** under the object and role views: necessity, sufficiency, and cross-model role transfer well-established
- **Tier 2** under the process view: phase transition documented; full dynamical account preliminary
- **Tier 1** under the subspace and structural views

## Further reading

Olsson, C., Elhage, N., Nanda, N. et al. "In-context Learning and Induction Heads." arXiv:2209.11895, 2022.
