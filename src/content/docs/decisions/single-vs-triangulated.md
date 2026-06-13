---
title: Single-Method vs. Triangulated Evidence
---

# Single-Method vs. Triangulated Evidence

**The fork.** When is one strong experiment enough to support a mechanistic claim, and when do you need converging evidence from independent domains?

This is an epistemological decision, not a methodological one. It determines how much confidence your evidence can support -- and getting it wrong means either overclaiming (treating preliminary evidence as established) or wasting effort (demanding three-domain evidence for a claim that does not need it).

## When you face this decision

You have run activation patching on GPT-2 Small's IOI circuit and found that head 9.1 is necessary for name-moving. Clean result, large effect size. Can you publish the claim "head 9.1 implements name-moving"?

With activation patching alone, several alternative explanations remain live. Head 9.1 might be necessary because it is part of a backup circuit that engages when the primary mechanism is disrupted. Its necessity might be an artifact of the specific prompt distribution you tested on. And you have no evidence about *how* the head implements name-moving -- only that removing it breaks things. The claim is supported but underdetermined: multiple distinct mechanisms are consistent with the same activation patching results.

The question is whether this level of underdetermination is acceptable for your purposes.

## Option A: Single strong source

One domain of evidence is sufficient when the claim is scoped narrowly enough that the domain's known failure modes do not apply, and the method distinguishes the proposed mechanism from all plausible alternatives within that scope.

**What it buys you.** Speed. You can make a claim and move on. For early-stage investigation, this is often the right call -- you are generating hypotheses, not establishing ground truth.

**What it commits you to.** Stating explicitly which failure modes would overturn the claim and what cross-domain tests would confirm it. A single-method claim should be framed as preliminary: "activation patching shows head 9.1 is necessary for IOI under this prompt distribution."

## Option B: Triangulation required

Evidence from at least two of three genuinely independent domains is required when the claim needs to be robust -- for mechanism identity claims, cross-model generalization, or safety-relevant conclusions.

**What it buys you.** Robustness against domain-specific failure modes. If weight-space analysis and activation-space analysis both point to the same mechanism, the chance that both are wrong in the same way is much lower than for either alone.

**What it commits you to.** Significantly more experimental work, and understanding which domains are actually independent.

## The non-independence trap

Not all methods are independent. Activation patching and DAS (Distributed Alignment Search) are both activation-space methods. They share failure modes: both fail for distributed mechanisms, both depend on prompt distribution, both are confounded by backup circuits. Using both does not constitute triangulation -- it is two views from the same vantage point.

The three genuinely independent evidence domains are:

- **Weight-space**: Analysis of the model's parameters directly (composition scores, SVD of weight matrices, weight-space circuit structure). Invariant to prompt distribution. Fails when causally active structures have low weight-space signatures.
- **Activation-space**: Analysis of what the model computes on specific inputs (activation patching, DAS/IIA, SAE channel activations). IIA (Interchange Intervention Accuracy) measures whether swapping activations in a subspace changes behavior as predicted by a causal model. Sensitive to prompt distribution. Fails when the mechanism is not activated by the specific prompts used.
- **Dynamics-space**: Analysis of how the mechanism formed during training (checkpoint trajectories, AGOP convergence, phase transitions). Captures formation order and prerequisites. Fails when different training trajectories converge to the same final mechanism.

Each domain is individually non-injective on mechanism space -- multiple distinct mechanisms can produce the same evidence within a single domain. Convergence across domains with structurally different failure modes does not eliminate underdetermination, but it substantially reduces the space of consistent hypotheses.

## Recommended default

**Single-method**: acceptable for single-model, single-task claims at the preliminary stage. Frame these claims with appropriate scope.

**Two domains**: required for cross-seed or cross-model identity claims. Weight-space plus activation-space is the most common and practical combination.

**All three domains**: required for safety-relevant claims or claims that will inform intervention design. If you are going to act on a mechanistic finding -- using it to edit a model, design a monitor, or argue that a model is safe -- the evidence bar should be high.
