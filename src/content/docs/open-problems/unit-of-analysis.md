---
title: "Unit of Analysis"
---

# What Is the Right Unit of Analysis?

**The question.** When we say "this attention head does X" or "this neuron represents Y," we've chosen a unit of analysis — the head, the neuron, the layer, the direction. Is that the right unit? Are attention heads natural joints of the model's computation, or convenient but misleading boundaries imposed by the architecture?

This question underlies many disagreements in the field. Researchers who study individual heads reach different conclusions from researchers who study subspaces or functional roles. The views framework shows why: they've chosen different units, and different units reveal different structure.

## What each view says

### [Object view](/mechanistic-views/views/object/) — the unit is the architectural component

The mechanism is a set of components: attention heads, MLP neurons, layers. These are the natural units because they correspond to the model's architectural structure. Activation patching and ablation studies target these components directly.

**The problem.** Architectural components may not align with computational function. A single attention head can serve multiple functions depending on context. Multiple heads can collectively implement a single function (as in the IOI circuit's backup name movers). The one-head-one-function assumption is convenient but frequently violated.

[Merullo et al. (2024)](https://arxiv.org/abs/2312.10794) showed that "circuit" boundaries drawn at the head level miss distributed computations that span many heads, none of which is individually necessary. The Object view's unit creates a resolution problem: the boundaries are clear but may not carve at the joints.

### [Role view](/mechanistic-views/views/role/) — the unit is the functional role

The mechanism is a set of functional roles: "mover," "inhibitor," "detector." Which component fills the role can change — backup mechanisms, context-dependent routing, redundant implementations are all expected. The role is stable even when the component isn't.

**The advantage.** Role-level analysis explains findings that puzzle the Object view. Backup name movers in the IOI circuit are a problem for the Object view (the "circuit" has redundant components) but expected for the Role view (the role is filled; which head fills it is an implementation detail).

**The limit.** Roles are harder to define operationally than components. How do you test whether two heads play the "same role"? The Role view requires equivalence criteria that the field hasn't standardized.

### [Subspace view](/mechanistic-views/views/subspace/) — the unit is the subspace

The mechanism is a set of causal subspaces — directions or low-dimensional submanifolds in activation space. These cut across architectural boundaries: a subspace can span multiple heads, and a single head can contribute to multiple subspaces.

**The advantage.** Subspaces are architecture-independent. The same subspace might be implemented by one head in a small model and three heads in a large model. This makes cross-model comparison possible ([E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture/)) in a way that head-level comparison is not.

**The evidence.** [DAS](/mechanistic-views/views/subspace/#evidence) identifies causal subspaces without reference to architectural components. When DAS and head-level analysis disagree — the subspace spans multiple heads, or a head contributes to multiple subspaces — the Subspace view says the subspace is the more fundamental unit.

### [Stratified view](/mechanistic-views/views/stratified/) — there is no single right unit

Different phenomena live at different strata of the model's computation. Token-level features are fine-grained. Phrase-level computations are coarser. Document-level representations are coarser still. The right unit depends on the stratum you're examining.

**The implication.** Asking "are heads the right unit?" presupposes a single correct resolution. The Stratified view says the answer is resolution-dependent: heads may be the right unit at one stratum and wrong at another. A complete description requires multiple resolutions simultaneously.

## The resolution

| View | Unit of analysis | Defined by... | Cross-model comparable? |
|---|---|---|---|
| [Object](/mechanistic-views/views/object/) | Architectural component (head, neuron) | Model architecture | No — different models have different components |
| [Role](/mechanistic-views/views/role/) | Functional role | Behavioral equivalence class | Partially — if roles are well-defined |
| [Subspace](/mechanistic-views/views/subspace/) | Causal subspace | DAS / IIA | Yes — subspaces are architecture-independent |
| [Stratified](/mechanistic-views/views/stratified/) | Resolution-dependent | Stratum | Yes — at matched resolution |

The field defaults to the Object view's unit (heads, neurons) because it's easy to operationalize. But easy doesn't mean correct. When head-level circuits are fragile, non-replicable, or size-dependent, the problem may be the unit, not the method.

**The practical fix:**
1. **State your unit.** "We analyze at the attention head level" is an Object-view commitment. Say so.
2. **Test unit sensitivity.** If your finding depends on the unit (head-level analysis says X, subspace-level says Y), that's a sign you're at the wrong resolution.
3. **Match unit to claim.** If you're claiming a mechanism is universal across models ([E6](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture/)), you need an architecture-independent unit. Heads won't work.

## Resolution status: **Dissolved**

There is no single right unit. The question dissolves when you recognize that different views define different units, and the appropriate unit depends on the claim. Head-level analysis is fine for Object-view claims about specific models. Subspace-level analysis is required for cross-model claims. The apparent disagreement about "the right unit" is a view disagreement about what kind of claim you're making.

## Mechanistic validity criteria

| Criterion | Status | What it tells you |
|---|---|---|
| [C4 Boundary specification](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/boundary-specification/) | Central | Are the boundaries of the unit well-defined? |
| [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance/) | Central | Are findings stable across unit choices? |
| [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture/) | Critical | Does the unit allow cross-model comparison? |
| [C1 Operationalization](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/operationalization/) | Relevant | Can the unit be measured consistently? |

## See also

- [Circuit Disagreements](/mechanistic-views/open-problems/circuit-disagreements/) — different methods find different circuits partly because they use different units
- [Cross-Model Identity](/mechanistic-views/open-problems/cross-model-identity/) — cross-model comparison requires architecture-independent units
- [Resolution & Completeness](/mechanistic-views/open-problems/resolution-completeness/) — resolution depends on the unit
- [Role view](/mechanistic-views/views/role/) — the view that abstracts over architectural components
- [Subspace view](/mechanistic-views/views/subspace/) — the view that provides architecture-independent units
