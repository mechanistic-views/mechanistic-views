---
title: Instrumental View
---

# Instrumental View

The instrumental view treats mechanisms as useful fictions rather than real objects. A mechanism description is a representation that helps predict and control model behavior, not a description of something that genuinely exists inside the model.

## Thesis

"The induction head mechanism" is useful shorthand for a set of predictive relationships between components and outputs. Whether the mechanism "really exists" as an object inside the model is not a meaningful question; all that matters is predictive utility.

## What this gains

Removes the need to solve hard questions about mechanism identity, localization, and gauge-invariance. A mechanism description is judged solely by its predictive and interventional utility, not by metaphysical criteria.

## What this loses

The ability to make cross-model identity claims. If mechanisms are just predictive shorthand, there is no fact about whether the induction head in GPT-2 and the induction head in Llama are "the same mechanism." One can only say that similar predictive shorthands apply to both.

## The interpretability challenge

Most interpretability research implicitly makes stronger claims than the instrumental view allows. "The circuit is the mechanism" implies something about what the model is actually doing inside, not just about what predicts its behavior. Safety applications in particular depend on claims that are not purely instrumental: "this model has a deceptive goal" is not paraphrasable as "this predictive shorthand is useful."

## Evidence

Under the instrumental view, the only evidence that matters is predictive and interventional utility: does the mechanism description correctly predict the model's behavior, and do interventions guided by the description produce the expected effects? No cross-domain triangulation or structural validation is required. Forecast accuracy and intervention success are sufficient.

## When to use it

The instrumental view is appropriate as a *fallback* when stronger views produce contradictions or unresolvable disagreements. It is also appropriate at early stages of investigation when the goal is purely to find representations useful for prediction, before committing to a metaphysical stance.

## Is predictive utility itself a realist concept?

A residual tension in the instrumental view: predictive utility is defined relative to a model's behavior under intervention. But to say an intervention "worked" requires a criterion of what it means to change the model's output in the predicted way — which requires some object to predict about. The instrumental view brackets questions about what the mechanism really is, but relies on predictions that are themselves mechanistic claims at some level.

This is not a fatal objection, but it means the instrumental view is not fully anti-realist: it is committed to the reality of *behavioral regularities*, even if not to the reality of the internal structure. For safety-relevant interpretability (e.g., detecting deceptive goal representations), this may be insufficient — behavioral regularity is compatible with the mechanism operating differently under distribution shift, and there may be no behavioral signal that distinguishes the cases without making internal structural claims.

## Relationship to Mechanistic Validity

The instrumental view implies that the "existence" validity criteria in Mechanistic Validity (construct validity, cross-domain triangulation) are not required — only predictive validity is. Most interpretability researchers will find this too weak for their purposes, but it is a coherent position. The view is best understood as a floor, not a ceiling: it states the minimum that mechanistic claims must satisfy, not the maximum they should aspire to.
