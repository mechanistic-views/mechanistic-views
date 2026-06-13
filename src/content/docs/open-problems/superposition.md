---
title: "Superposition"
---

# Superposition

**The question.** Neural networks represent more features than they have dimensions. [Elhage et al. (2022)](https://transformer-circuits.pub/2022/toy_model/index.html) showed in toy models that networks compress many sparse features into a lower-dimensional space by exploiting the geometry of high-dimensional spaces — features are represented as nearly-orthogonal directions that interfere slightly with each other.

Is superposition a problem to be solved? A natural property to be understood? An artifact of how we define "feature"? The answer depends on which view you're in.

## What each view says

### [Object view](/mechanistic-views/views/object/) — superposition is a problem

If features are concrete parts of the network — discrete, countable things — then superposition means those parts are entangled. You can't cleanly isolate one feature without interference from others. This is why SAEs exist: they're an attempt to "undo" superposition and recover the individual features.

**The assumption.** The Object view assumes there is a clean decomposition underneath the superposition. SAEs work if and only if this assumption holds — if the model's computation is fundamentally organized around discrete, sparse features that got compressed into superposition.

**The problem.** If the underlying representation isn't organized around discrete features — if the model uses distributed, overlapping representations that don't decompose cleanly — then SAEs are imposing a decomposition that doesn't correspond to the model's actual computational structure. "Solving superposition" becomes "projecting your preferred ontology."

### [Subspace view](/mechanistic-views/views/subspace/) — superposition is expected

Features are subspaces, not directions. Subspaces can overlap — that's not a bug, it's geometry. In a 768-dimensional space, you can have thousands of nearly-orthogonal subspaces. The model represents many concepts simultaneously because the space is high-dimensional enough to accommodate them with minimal interference.

**The reframe.** Superposition isn't a problem to solve — it's a property of the representation geometry to characterize. The questions become:
- How much do subspaces overlap? (Measure [Grassmannian distances](/mechanistic-views/formalism/grassmannian/))
- Which subspaces interfere? (Map the interference structure)
- Does interference degrade computation? (Test with [IIA](/mechanistic-views/views/subspace/#evidence))

Under the Subspace view, SAEs are one way to identify the subspaces, not the only way. [DAS](/mechanistic-views/views/subspace/#evidence) identifies causal subspaces directly without assuming discrete features.

### [Structural view](/mechanistic-views/views/structural/) — superposition is compressed computation

The model's computation has a [gauge-invariant](/mechanistic-views/views/structural/) structure. Superposition is a way of compressing that structure into the available dimensions. Different basis choices (different SAE widths, different rotation of the residual stream) are different gauges for the same underlying computation.

**The insight.** Two models with different superposition patterns may implement the same computation — the superposition is a gauge choice, not a computational fact. The structural view asks: what is the computation, independent of how it's compressed? This is a much harder question but a more fundamental one.

### [Perspectival view](/mechanistic-views/views/perspectival/) — "superposition" is theory-laden

The claim that models are "in superposition" presupposes that there are discrete features being compressed. This is the Object view's ontology. The Perspectival view asks: how do we know? What if the model's representations are inherently distributed, and "superposition" is the name we give to the gap between our preferred decomposition and the model's actual structure?

**The critique.** [Toy models of superposition](https://transformer-circuits.pub/2022/toy_model/index.html) demonstrate superposition in networks trained to reconstruct sparse inputs. But real language models weren't trained to reconstruct sparse features — they were trained to predict tokens. The mapping from "toy models show superposition" to "GPT-4 is in superposition" requires assumptions that the Perspectival view flags as unverified.

## The resolution

| View | Superposition is... | The right response is... |
|---|---|---|
| [Object](/mechanistic-views/views/object/) | A problem (features are entangled) | Decompose it (SAEs) |
| [Subspace](/mechanistic-views/views/subspace/) | Expected (subspaces overlap) | Characterize the geometry |
| [Structural](/mechanistic-views/views/structural/) | Compressed computation (gauge choice) | Find the gauge-invariant structure |
| [Perspectival](/mechanistic-views/views/perspectival/) | Theory-laden (presupposes discrete features) | Test the presupposition |

The field's current approach — train SAEs to "solve" superposition — is coherent under the Object view. But it assumes the Object view is correct. If representations are better described as subspaces (Subspace view) or compressed computations (Structural view), then SAEs are solving a problem that may not exist in the form assumed.

**The practical implications:**
1. If you're training SAEs to decompose superposition, you're making an **Object-view** commitment. State it explicitly.
2. If the subspaces SAEs find are stable across widths ([C5 Convergent](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/)), that's evidence the Object assumption is productive even if not literally true.
3. If they're not stable — if features split, merge, and absorb unpredictably — that's evidence the representation is better described at the Subspace level.
4. Discriminant validity ([V3](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/discriminant-validity/)) is critical: do SAEs find qualitatively different structure in trained models vs. random models? If not, "superposition" may be a property of high-dimensional geometry, not of learned representations.

## Resolution status: **Dissolved**

The framework dissolves the debate. "How do we solve superposition?" is an Object-view question. "How do we characterize the representation geometry?" is a Subspace-view question. "What is the gauge-invariant computation?" is a Structural-view question. They are different questions with different answers and different evidence requirements. The apparent disagreement about whether superposition is a "problem" is a view disagreement, not an empirical one.

## Mechanistic validity criteria

| Criterion | Status | What it tells you |
|---|---|---|
| [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/) | Central | Do different decomposition methods agree on the structure? |
| [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance/) | Central | Is the decomposition stable across measurement choices? |
| [V3 Discriminant validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/discriminant-validity/) | Critical | Is the structure real or a property of high-dimensional geometry? |
| [C4 Boundary specification](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/boundary-specification/) | Relevant | Where does one feature's subspace end and another's begin? |

## See also

- [SAE "True" Features](/mechanistic-views/open-problems/sae-true-features/) — the related question of whether SAE features are real
- [Decomposition Identity](/mechanistic-views/open-problems/decomposition-identity/) — which decomposition is "real"?
- [Subspace view](/mechanistic-views/views/subspace/) — the view that treats superposition as geometry
- [Structural view](/mechanistic-views/views/structural/) — the view that treats superposition as gauge choice
