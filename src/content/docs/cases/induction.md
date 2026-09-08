---
title: Case Study — Induction Heads
---

# Case Study — Induction Heads

**The phenomenon.** Induction heads implement prefix matching: given $[A][B]\ldots[A]$, predict $[B]$. [Olsson et al. (2022)](/mechanistic-views/glossary/#induction-heads) described them in detail and proposed they underlie in-context learning.

## [Object view](/mechanistic-views/views/object/)

A previous-token head writes the previous token's identity to the residual stream; an induction head queries for tokens whose preceding context matches the current position. Ablating identified heads impairs next-token prediction on repeated sequences; composition score between the pair is high.

## [Role view](/mechanistic-views/views/role/)

A two-role structure: (copy-previous role, attend-to-matching-prefix role). Different models implement these roles with different specific heads. Cross-model role transfer qualitatively established.

## [Subspace view](/mechanistic-views/views/subspace/)

The induction variable is approximately the identity of the token to be predicted. This occupies a subspace at the output of the induction head's OV circuit.

**Outstanding.** [DAS](/mechanistic-views/views/subspace/#evidence) has not been systematically applied to recover this subspace and measure its [Grassmannian](/mechanistic-views/formalism/grassmannian/) distance from the $W^{OV}$ SVD subspace.

## [Process view](/mechanistic-views/views/process/)

Olsson et al. (2022) showed induction heads form suddenly at a specific training step — a phase transition with a sharp loss decrease. Before, in-context learning is near-absent; after, it is present.

The process-view claim: this corresponds to a formation event — the mechanism appears suddenly rather than accumulating smoothly, suggesting a phase transition in the weight-space trajectory rather than gradual construction. The pre-transition state is not necessarily distributed (it may simply be the absence of the mechanism); the stratum-change interpretation requires evidence that the pre-transition model has a different positive mechanism rather than the absence of one. AGOP trajectories are the natural evidence source for distinguishing these.

**Formation criterion.** Olsson et al. detect the transition as a bump in the training loss, with prefix-matching scores rising abruptly in the same window. Whether a weight-space criterion converges earlier than that behavioral one is open.

## Current evidence state

Two readings of the same evidence base separate here.

- **Narrow reading** (the heads copy a token that followed the same context earlier): **view-invariant**. Support crosses three families — ablation attributing in-context learning to those heads (identity), the copying and prefix-matching terms read off the OV and QK circuits (mathematical), and the coincidence of head formation with the in-context learning jump (process).
- **Broad reading** (the heads are the mechanistic source of general in-context learning): **contested**. The same three families support it, so family breadth does not separate the two. What separates them is the later literature: the causal ablation was never run above 42M parameters; at 70–72B the heads carrying abstract in-context reasoning form a disjoint set from induction heads (Webb et al., 2025); suppressing induction-head formation leaves abstract in-context learning intact on 13 of 21 tasks (Sahin et al., 2025); and once function-vector heads are preserved, ablating induction heads above 1B is comparable to ablating random heads (Yin et al., 2025).

## What would cross a second family boundary

**[Subspace view](/mechanistic-views/views/subspace/), Tier 1 → 2** (single-domain causal evidence):
- [DAS](/mechanistic-views/views/subspace/#evidence) recovery of the induction variable subspace with IIA reported
- [Grassmannian](/mechanistic-views/formalism/grassmannian/) distance measurement between the $W^{OV}$ SVD subspace and the DAS-recovered subspace

**[Process view](/mechanistic-views/views/process/), Tier 2 → 3** (two-domain + cross-model consistency):
- AGOP trajectory analysis showing subspace convergence precedes behavioral transition across seeds
- Quantitative account of transition timing from weight-decay schedule parameters

**[Structural view](/mechanistic-views/views/structural/), Tier 1 → 2** (single-domain evidence):
- Cosheaf construction for the induction circuit with $H^\bullet$ computed
- Comparison of composition-score-based and patching-based circuit proposals for coverage equivalence

## Further reading

Olsson, C., Elhage, N., Nanda, N. et al. "In-context Learning and Induction Heads." arXiv:2209.11895, 2022.
