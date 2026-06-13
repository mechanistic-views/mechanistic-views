---
title: "Barez et al.: MI Needs Philosophy"
---

# Barez et al.: "Mechanistic Interpretability Needs Philosophy"

[Williams, Oldenburg, Dhar et al. (2026)](https://arxiv.org/abs/2506.18852) argue that MI needs philosophy as an ongoing partner — for clarifying concepts, refining methods, and navigating epistemic complexity. They illustrate this through three open problems from the MI literature, each of which maps onto view-level confusions in our framework.

## Problem 1: How should we decompose networks? (§2.1)

The paper challenges what they call the assumption of "the One True Decomposition" — that there is a privileged way to carve a neural network into interpretable parts. Drawing on philosophy of science, they argue for **explanatory pluralism**: different decompositions serve different explanatory goals, and no single decomposition has a unique claim to being "the real one."

This is exactly the [Decomposition Identity](/mechanistic-views/open-problems/decomposition-identity/) problem. Their philosophical framing maps onto our view analysis:

| Their concept | Our view | The connection |
|---|---|---|
| No single correct decomposition | [Subspace](/mechanistic-views/views/subspace/) vs [Object](/mechanistic-views/views/object/) | Object view assumes a unique decomposition; Subspace view says the subspace is real, the basis is a choice |
| Explanatory pluralism | [Perspectival](/mechanistic-views/views/perspectival/) | Different methods project different decompositions — this is expected, not a failure |
| Evaluate by causal understanding, not "true structure" | [Role](/mechanistic-views/views/role/) | Decompositions should be judged by functional utility, not correspondence to some Platonic structure |

## Problem 2: What "features" do AI systems discover? (§2.2)

The paper introduces the philosophical distinction between **vehicles** and **content** of representations. The *vehicle* is the physical carrier (a neuron, a direction in activation space). The *content* is what it represents (the concept "dog," the property "is plural").

This maps onto our Object/Role split applied to features:

| Their concept | Our view | The connection |
|---|---|---|
| Vehicle (the direction/neuron) | [Object](/mechanistic-views/views/object/) | The feature *is* the component |
| Content (what it represents) | [Role](/mechanistic-views/views/role/) | The feature *is* the functional role it plays |
| What grounds representational content? | [Subspace](/mechanistic-views/views/subspace/) | Causal subspace (DAS/IIA) provides grounding — interventions establish that the representation actually drives behavior |

They also note that "feature" is used inconsistently in MI — sometimes meaning the vehicle, sometimes the content. This ambiguity is a source of confusion in debates about [SAE "true" features](/mechanistic-views/open-problems/sae-true-features/) and [probe features](/mechanistic-views/open-problems/probe-features/).

## Problem 3: How can we detect deceptive behaviour? (§2.3)

The paper argues that deception detection requires philosophical clarity on what deception *is*. In philosophy, deception requires intentions and beliefs on the part of the deceiver — criteria that are controversial to attribute to language models. They also make a key distinction: not all information-concealing circuits are ethically equivalent. A circuit that hides dangerous capabilities, one that protects user privacy, and one that redirects to emergency care all "conceal information" but require completely different interventions.

This connects to our [Deceptive Alignment](/mechanistic-views/open-problems/deceptive-alignment/) analysis:

| Their concept | Our view | The connection |
|---|---|---|
| Deception requires intentions/beliefs | [Structural](/mechanistic-views/views/structural/) | You need gauge-invariant evidence of a computation that implements strategic reasoning, not just a "deception direction" |
| Behavioral detection is insufficient | [Instrumental](/mechanistic-views/views/instrumental/) ceiling | Competent deception evades behavioral detection by definition |
| Different "deceptive" circuits need different responses | [Role](/mechanistic-views/views/role/) | The functional role matters — same Object-level structure, different Role-level meaning |

## Convergence

This paper arrives at many of the same conclusions as our framework but from philosophy of science rather than measurement theory. Where we say "different views define mechanisms differently," they say "explanatory pluralism." Where we say "Object view vs Subspace view," they say "vehicle vs content." Where we say "Instrumental evidence is structurally insufficient for deception detection," they say "behavioral approaches cannot establish deception without philosophical clarity on what deception requires."

The convergence from independent starting points strengthens both analyses.

## See also

- [Decomposition Identity](/mechanistic-views/open-problems/decomposition-identity/) — their Problem 1
- [SAE "True" Features](/mechanistic-views/open-problems/sae-true-features/) — their Problem 2
- [Deceptive Alignment](/mechanistic-views/open-problems/deceptive-alignment/) — their Problem 3
- [Probe Features](/mechanistic-views/open-problems/probe-features/) — vehicle/content ambiguity applies here too
