---
title: "Case Study — Do Probes Find Features the Model Uses?"
---

# Do Probes Find Features the Model Actually Uses?

**The question.** A linear probe trained on a model's activations achieves high accuracy at predicting some property — part of speech, sentiment, truthfulness, spatial position. Does this mean the model *represents* that property? Does the model *use* it in its computation? Or is the probe just a powerful classifier extracting signal the model never relies on?

This question drove the "probing wars" of 2019-2022 and remains unresolved. We show that the disagreement is a view confusion: "represents," "uses," and "is there" mean different things under different views.

## What each view says

### [Instrumental view](/mechanistic-views/views/instrumental/) — the probe predicts, that's the finding

A probe that achieves high accuracy has demonstrated that the property is linearly decodable from the model's activations. Full stop. Whether the model "uses" it is a separate question the probe cannot answer — and the Instrumental view does not ask it.

**The limit.** High probe accuracy is consistent with the model encoding the property *and* with the property being an artifact of the activation geometry that the model never relies on. [Hewitt and Liang (2019)](https://arxiv.org/abs/1909.03368) introduced selectivity — the gap between probe accuracy on a real model vs. a control — precisely to address this. But selectivity is itself an Instrumental measure: it tells you the model's activations are *different from random*, not that the model *uses* the property.

### [Subspace view](/mechanistic-views/views/subspace/) — "uses" means causally active

The probe identifies a direction (or subspace) in activation space. The question becomes: is that direction causally active? [Distributed Alignment Search (DAS)](https://arxiv.org/abs/2303.02536) and [Interchange Intervention Accuracy (IIA)](https://arxiv.org/abs/2303.02536) test this directly: swap the component of one input's activation along the probe's direction with another input's, and check whether the model's behavior changes as predicted.

If IIA is high, the model is using the subspace the probe found. If IIA is low, the probe found a correlation in the activations that isn't causally relevant — the model can produce the same behavior without it.

**The resolution.** The probe identifies a candidate subspace. DAS/IIA tests whether that subspace is causally active. This is the standard the Subspace view provides: a feature the model "uses" is one that lives in a causal subspace, measured as a point on the [Grassmannian](/mechanistic-views/formalism/grassmannian/) $\mathrm{Gr}(k, d)$.

### [Perspectival view](/mechanistic-views/views/perspectival/) — probes impose structure

A sufficiently expressive probe can find "features" in any high-dimensional space, including random activations. The Perspectival view treats the probe as a method that projects structure onto the model. The critical question is [discriminant validity](/mechanistic-views/views/perspectival/#evidence): does the probe find qualitatively more structure in a trained model than in a control?

[Zhang and Bowman (2018)](https://arxiv.org/abs/1802.04302) showed that probes can achieve high accuracy on linguistic properties even in models that should not encode them. [Belinkov (2022)](https://arxiv.org/abs/2102.12452) surveyed the probing literature and concluded that high accuracy alone is not evidence of representation — you need controls.

**The implication.** Before claiming the model "represents X," you need:
1. Probe accuracy on the trained model
2. Probe accuracy on a control (random model, shuffled activations, different architecture)
3. A meaningful gap between the two

Without the control, you cannot distinguish "the model represents X" from "linear classifiers are powerful."

### [Role view](/mechanistic-views/views/role/) — "uses" means functionally necessary

The model uses a feature if that feature plays a functional role: removing it degrades performance on tasks that require it, and it generalizes across inputs that require the same function. This is stronger than the Subspace view's causal activity — it requires that the feature is not just causally active but functionally necessary for a class of behaviors.

**The test.** Ablate or suppress the probe's direction and measure degradation on role-relevant tasks. If removing the "sentiment direction" degrades sentiment-dependent behavior but not other behavior, sentiment is a functional role the model uses.

## The resolution

"Does the model use this feature?" is not one question:

| View | What "uses" means | Evidence required | Probe alone sufficient? |
|---|---|---|---|
| [Instrumental](/mechanistic-views/views/instrumental/) | Decodable from activations | Probe accuracy | Yes — but this is a weak claim |
| [Perspectival](/mechanistic-views/views/perspectival/) | More than method artifact | Discriminant validity vs. control | No — need control comparison |
| [Subspace](/mechanistic-views/views/subspace/) | Causally active direction | DAS / IIA | No — need causal intervention |
| [Role](/mechanistic-views/views/role/) | Functionally necessary | Ablation + role transfer | No — need knockout experiments |

The probe wars happened because researchers made claims at one view using evidence from another. A linear probe gives you **Instrumental** evidence: the property is decodable. Concluding that the model "represents" or "uses" the property is a **Subspace** or **Role** claim. The evidence doesn't match the claim.

**The practical fix:** match the evidence to the claim.
1. "This property is linearly decodable" — Instrumental. Probe accuracy suffices.
2. "This property is encoded differently in trained vs. random models" — Perspectival. Need discriminant validity ([V3](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/discriminant-validity/)).
3. "This property is causally active in the model's computation" — Subspace. Need DAS/IIA ([I1 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency/)).
4. "This property is functionally necessary for the model's behavior" — Role. Need ablation + specificity ([I2 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity/), [E3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/specificity/)).

Each is a valid claim. They are not the same claim.

## Mechanistic validity criteria

| Criterion | Status | What it tells you |
|---|---|---|
| [V3 Discriminant validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/discriminant-validity/) | Critical | Can you distinguish real encoding from probe artifact? |
| [I1 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency/) | Central | Does intervening on the subspace produce the expected behavior? |
| [I2 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity/) | Central | Does removing the subspace degrade the expected behavior? |
| [I4 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control/) | Critical | Is probe accuracy confounded by activation geometry? |
| [E3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/specificity/) | Relevant | Does the feature affect only the relevant behavior? |

## Resolution status: **Dissolved**

The framework dissolves the debate. The probe wars were caused by evidence-claim mismatch: Instrumental evidence (probe accuracy) used to support Subspace or Role claims (the model "uses" or "represents" the feature). Name the view, match the evidence to the claim, and the disagreement disappears. What remains is empirical work — actually running the causal interventions — not conceptual confusion.

## See also

- [Linear Assumption](/mechanistic-views/open-problems/linear-assumption/) — the broader question of whether linear structure is real
- [Subspace view](/mechanistic-views/views/subspace/) — the view that provides the causal test
- [Perspectival view](/mechanistic-views/views/perspectival/) — the view that predicts probe artifacts
- [Safety Evidence Gaps](/mechanistic-views/open-problems/safety-evidence-gaps/) — where Instrumental evidence is used for stronger claims
