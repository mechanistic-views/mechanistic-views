---
title: Case Study — Hallucination
---

# Case Study: Hallucination

**The phenomenon.** Language models generate confident, fluent, factually incorrect outputs. Two mechanistically distinct failure modes: **knowledge absence** (the fact was never encoded) and **knowledge retrieval failure** (the fact is encoded but the wrong candidate wins). The distinction matters for what mechanism description is appropriate and what interventions would help.

## Object view

A set of components retrieves the correct fact; a competing mechanism promoting the incorrect candidate wins. Evidence: activation patching studies showing specific layers or heads produce the correct answer when patched from a correct pass.

**Limitation.** If correct and incorrect mechanisms share components, the object view cannot cleanly localize the failure.

## Role view

The mechanism is the *fact-retrieval role*: whatever promotes the correct entity as answer candidate when it is correct. Hallucination is a role-competition failure: the retrieval role and a distributional-prior role both activate, and the latter dominates.

The role view predicts that the same components may play different roles on different prompts. Role-substitution experiments distinguish this from simple ablation.

## Subspace view

The causal variable is "which entity is currently promoted as the answer candidate." This occupies a subspace at the final layers. In the hallucinating case, the wrong entity has higher projection onto the answer-readout subspace.

Evidence: DAS on minimal pairs where the correct entity is known and the prompts vary in structure, searching for the subspace whose swap changes the answer from incorrect to correct.

**Outstanding.** Systematic DAS analysis with IIA reported for factual recall hallucination has not been published.

## Structural view

Hypothesis: facts encoded with lower effective-rank weight structure hallucinate more frequently under retrieval competition. A test: measure effective rank of the fact-encoding component in $W^{OV}$ of implicated heads, correlate with hallucination frequency on ambiguous prompts.

## The distributional confound

The hallucination case has its own distributional confound: a model that reliably produces the wrong answer on certain question types may be pattern-matching the question format to a distributional prior rather than failing to retrieve a specific stored fact. The distinction matters mechanistically — distributional-prior dominance is a role-competition failure between the fact-retrieval role and the distributional-prior role; question-type pattern-matching is a different object that may not involve the fact-retrieval mechanism at all. Distinguishing them requires minimal pairs where the same fact is queried in multiple syntactic forms and the hallucination rate is measured across forms.

## Current evidence state

- **Tier 2** for the object and role views: patching studies localize factual recall to mid-to-late layers; cross-seed consistency not reported
- **Tier 1** for subspace and structural views

## What would move to Tier 3

- DAS on factual recall tasks with IIA reported and cross-prompt consistency established
- Weight-space evidence: effective rank and composition score analysis of heads identified by patching
- Mechanistic discrimination of knowledge-absence from retrieval-failure at the circuit level
