---
title: Behavioral vs. Mechanistic
---

# Behavioral vs. Mechanistic

**The fork.** Is a finding about a model's *behavioral propensity* (how it tends to behave on a distribution) or about a *mechanism* (an internal structure that produces behavior)?

This decision point matters most for safety, where the gap between instrumental evidence and mechanistic conclusions is the central evidence deficit.

## When you face this decision

Suppose you find a steering vector that reliably suppresses refusal behavior on a test distribution. You can add the vector and induce refusal on harmless instructions, or subtract it and remove refusal on harmful ones. The intervention works.

Is this a mechanistic finding — you have identified the refusal mechanism — or a behavioral finding — you have found a lever that controls refusal behavior? Your answer determines what safety conclusions you can draw.

## Option A: Behavioral (instrumental)

The finding is about a model's propensity: does it typically do X, and under what conditions? Under the [instrumental view](/mechanistic-views/views/instrumental/), a behavioral finding — the model reliably outputs Y given X — is sufficient. The propensity is the object of interest and the mechanism is irrelevant.

**What it buys you.** Practical control. If the steering vector reliably suppresses refusal across your test distribution, you have a useful tool regardless of whether it targets "the" refusal mechanism.

**What goes wrong.** A behavioral finding establishes a lever, not a mechanism. Whether that vector *is* the refusal mechanism, or merely interferes with it, requires further evidence. The lever may not generalize beyond the test distribution. For safety applications, the gap between "controls behavior" and "we understand why it behaves this way" is where the risk lives.

## Option B: Mechanistic

The finding is about an internal structure that produces behavior. Under the [object view](/mechanistic-views/views/object/), a behavioral finding is a starting point: the question becomes which components produce that behavior, and whether they are necessary.

**What it buys you.** Understanding. If you have identified the mechanism, you can predict behavior in novel situations, detect when the mechanism is being circumvented, and verify that a safety intervention targets the right internal structure rather than a surface correlation.

**What goes wrong.** Mechanistic claims require mechanistic evidence — ablation of specific components, stability of intervention directions across distributions, subspace analysis. A capability finding (the model *can* do X) is weaker than a propensity finding (the model *typically does* X), because a capability finding requires only that the mechanism exists, while a propensity finding requires that it be routinely recruited.

## The safety-critical distinction

A steering vector that suppresses refusal establishes an instrumental capability. Mechanistic understanding of refusal is a further claim. Whether the vector *is* the refusal mechanism requires at least [object-view](/mechanistic-views/views/object/) evidence (ablation of specific components) and ideally [subspace-view](/mechanistic-views/views/subspace/) evidence (stability of the intervention direction across distributions).

The gap between instrumental evidence and the safety conclusions drawn from it is the central evidence deficit identified by the [open problems analysis](/mechanistic-views/open-problems/safety-evidence-gaps/).

## Distinguishing experiments

**Distribution shift.** Apply the steering vector on a distribution substantially different from the one used to estimate it. If refusal suppression holds, the lever may reflect something closer to the mechanism. If it fails, the finding was distribution-specific — behavioral, not mechanistic.

**Rank analysis.** Test whether refusal is organized along one dimension (rank-1 intervention) or requires higher-rank subspace interventions. If a single direction suffices across distributions, the subspace claim is stronger. If not, the steering result may be an artifact of the estimation procedure.

**Component ablation.** Identify the components whose activations project most strongly onto the steering direction. Ablate them individually. If ablation of those components reproduces the steering effect, you have converging object-level and subspace-level evidence.

## Recommended default

Start with **behavioral evidence** — it is faster to collect and establishes the practical baseline. But be explicit about what it does and does not show. A steering vector is an instrumental lever until you have independent evidence that it targets a mechanism.

For **safety claims**, behavioral evidence alone is structurally insufficient. The standard for "we understand refusal" is higher than the standard for "we can control refusal," and the difference is the mechanistic evidence.
