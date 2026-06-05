---
title: Single-Method vs. Triangulated Evidence
---

# Decision: Single-Method vs. Triangulated Evidence

**The fork.** When is one strong source sufficient, and when is convergent evidence from independent domains required?

## Why single-domain evidence is insufficient

The epistemological problem here is **underdetermination**: multiple distinct mechanism hypotheses are consistent with evidence from any single domain.

- Weight-space evidence alone is consistent with any mechanism that produces the same weight structures (which can include mechanisms with identical weights but different causal roles).
- Activation-space evidence alone is consistent with mechanisms that produce the same activation patterns on the observed prompt distribution (different mechanisms may produce identical activations within-distribution while diverging out-of-distribution).
- Dynamics-space evidence alone is consistent with mechanisms that have the same training trajectory (different final mechanisms can form via the same dynamics if the trajectory is underspecified).

The triangulation requirement does not eliminate underdetermination — no finite body of evidence can do that — but it *reduces* the hypothesis space by requiring consistency across domains with structurally different failure modes. A hypothesis that explains all three domains is not trivially underdetermined.

The joint map across all three domains is injective for any pair of mechanisms that are not identical in all three domains simultaneously — a condition that is plausible but has not been formally verified for natural transformer mechanisms. This is a standing open question; the claim here is only that convergent evidence across domains is stronger than any single domain, which is uncontroversial.

## Option A: Single strong source

Sufficient when the claim is scoped narrowly enough that the domain's known failure modes do not apply, and the method distinguishes the proposed mechanism from all plausible alternatives within that scope.

**Commits you to.** Tier 2 (Preliminary). Specifying which failure modes would overturn the claim and what cross-domain tests would confirm it.

## Option B: Triangulation required

Required for: mechanism identity claims, cross-model generalization, mechanism formation, safety-relevant interventions.

**Commits you to.** Evidence from at least two of the three independent domains with genuinely different failure modes.

## The non-independence trap

Activation patching and DAS are both activation-space methods. They share failure modes: both fail for distributed mechanisms, both depend on prompt distribution, both are confounded by backup circuits. They are not independent triangulation.

The three genuinely independent domains and their distinct failure modes:
- **Weight-space**: invariant to prompt distribution; fails for low-rank causally active structures that composition score analysis misses
- **Activation-space**: sensitive to prompt distribution; fails when the mechanism is not activated by the specific prompts used
- **Dynamics-space**: captures formation; fails when different training trajectories converge to the same final mechanism

## Recommended default

Single-method: acceptable at Tier 2 for single-model, single-task claims.

Two domains: required for cross-seed or cross-model identity claims.

All three domains: required for safety-relevant or intervention-design claims.
