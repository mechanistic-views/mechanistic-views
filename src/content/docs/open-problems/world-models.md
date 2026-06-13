---
title: "World Models"
---

# Do Language Models Build Internal World Models?

**The question.** When a language model plays Othello, predicts physical interactions, or reasons about spatial relationships, does it build an internal representation of the world that mirrors the world's causal structure? Or does it learn statistical shortcuts that approximate world-model-like behavior without representing the world as such?

This question matters for safety (a model with a world model could reason about evasion) and for capabilities (world models would enable systematic generalization). We show that the disagreement turns on what "world model" means — and different views define it differently.

## What each view says

### [Instrumental view](/mechanistic-views/views/instrumental/) — the model predicts well, that's the finding

A model that predicts legal Othello moves, solves physics problems, or generates spatially coherent descriptions is exhibiting world-model-like *behavior*. The Instrumental view says: the model's predictions are consistent with having a world model. Whether it "really" has one is a question the Instrumental view doesn't ask.

**The limit.** Predictive success is consistent with both a world model and a bag of statistical heuristics. GPT-2 predicts "the ball rolled under the table" without anyone claiming it understands physics. High accuracy on world-model-requiring tasks is necessary but not sufficient evidence for an internal world model.

### [Subspace view](/mechanistic-views/views/subspace/) — linear encodings of state variables

[Li et al. (2023)](https://arxiv.org/abs/2210.13382) showed that a model trained on Othello move sequences develops linear representations of board state — you can decode which squares are occupied using a linear probe. This is Subspace evidence: there exist causal subspaces encoding state predicates.

**What this establishes.** The model encodes board state in a way that is linearly accessible and causally relevant (intervening on the representation changes downstream predictions). This is real and interesting — but it is not a world model. A world model would require these state representations to be organized into a causal graph that mirrors the world's causal structure. Linear encodings of individual state variables are *components* of a world model, not the model itself.

**The gap.** Linear probes for individual predicates (is this square occupied?) don't tell you whether the model represents the *relationships* between predicates (if this square is occupied, these moves become illegal). That requires Structural evidence.

### [Structural view](/mechanistic-views/views/structural/) — causal structure matching world structure

A world model, in the Structural view, is a [gauge-invariant](/mechanistic-views/views/structural/) computational structure inside the model whose causal graph is isomorphic (or approximately so) to the causal graph of the world being modeled. The board state representations aren't just encoded — they're connected by computations that mirror the game's rules.

**What this would require.** Showing that the model's internal causal graph (not just its activations) mirrors the world's causal graph. This means: manipulating one state variable and showing that downstream state variables update as the world's causal structure predicts — not just that the model's *output* changes, but that its *internal representations* of other state variables change accordingly.

**The evidence gap.** Mechanistic Validity [E4 Counterfactual validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/counterfactual-validity/) is the relevant criterion: does intervening on the model's world-state representation produce the same downstream effects as intervening on the actual world state? No published work has demonstrated this at the Structural level for a full world model (as opposed to individual state predicates).

### [Process view](/mechanistic-views/views/process/) — when and how does it form?

If the model develops a world model, the Process view asks: does it form all at once or incrementally? Do spatial predicates form before causal relationships? Is there a phase transition where the model shifts from statistical shortcuts to genuine world modeling?

[Nanda et al. (2023)](https://arxiv.org/abs/2301.05217) showed that grokking involves a sudden phase transition from memorization to algorithmic computation. If world models form via similar transitions, there may be a training checkpoint where the model shifts from "predicting well using heuristics" to "predicting well using a world model." Process evidence would identify that transition.

## The resolution

"Does the model have a world model?" is not one question:

| View | What "world model" means | Evidence required | Current status |
|---|---|---|---|
| [Instrumental](/mechanistic-views/views/instrumental/) | Predicts world-model-requiring tasks | Task accuracy | Established for many tasks |
| [Subspace](/mechanistic-views/views/subspace/) | Encodes state predicates in causal subspaces | Linear probes + DAS/IIA | Demonstrated for Othello, some spatial tasks |
| [Structural](/mechanistic-views/views/structural/) | Internal causal graph mirrors world causal graph | Holonomy, causal graph isomorphism | Not demonstrated |
| [Process](/mechanistic-views/views/process/) | World model forms during training | Checkpoint analysis, phase transition detection | Preliminary (grokking analogues) |

The field has strong Subspace evidence (linear encodings of state variables) and treats this as evidence for world models. But Subspace evidence establishes that the model *encodes* world state, not that it *models* the world's causal structure. The latter requires Structural evidence that no one has produced.

**The practical implication:**
1. "The model encodes board state" — Subspace claim. Established. Real and interesting.
2. "The model has a world model" — Structural claim. Not established. Requires causal graph comparison.
3. "The model learned a world model during training" — Process claim. Requires training dynamics evidence.

Most papers making "world model" claims have Subspace evidence. The framework makes the gap between evidence and claim explicit.

## Resolution status: **Reframed**

The framework clarifies that "world model" means different things at different views and that current evidence (Subspace) is weaker than the claims being made (Structural). The empirical question — does any model actually have a Structural-level world model? — remains open. The framework doesn't answer it, but it tells you exactly what evidence would.

## Mechanistic validity criteria

| Criterion | Status | What it tells you |
|---|---|---|
| [E4 Counterfactual validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/counterfactual-validity/) | Critical | Does intervening on the model's world representation produce world-consistent downstream effects? |
| [I1 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency/) | Central | Does the world model subspace causally drive behavior? |
| [C1 Operationalization](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/operationalization/) | Central | What does "world model" mean operationally? |
| [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion/) | Critical | Could statistical shortcuts explain the same behavior? |

## See also

- [Probe Features](/mechanistic-views/open-problems/probe-features/) — the broader question of whether probes find features the model uses
- [Linear Assumption](/mechanistic-views/open-problems/linear-assumption/) — linear encodings may not capture non-linear world structure
- [Subspace view](/mechanistic-views/views/subspace/) — the view that establishes state encoding
- [Structural view](/mechanistic-views/views/structural/) — the view required for genuine world model claims
