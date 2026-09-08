---
title: Contrastive View
---

# Contrastive View

The contrastive view treats mechanisms as defined relative to a foil: a mechanism is what a component or subspace does in condition A *compared to* condition B. This is how most interpretability experiments actually work in practice — the IOI circuit is studied by contrasting indirect-object completion with subject completion, not by characterizing what heads do in absolute terms — but the contrastive structure is rarely made explicit as an ontological commitment.

The contrastive view draws on a well-developed tradition in philosophy of science. Van Fraassen's pragmatic theory of explanation holds that explanations are always contrastive: we explain why P rather than Q, not why P simpliciter. Lipton gives the contrastive structure a causal reading: to explain why P rather than Q is to cite a cause of P absent from the history of Q, so different foils yield different — and jointly correct — causal explanations.

## Thesis

A mechanism is a contrastive pattern: a difference in internal behavior between a target condition and a foil condition. The foil is part of the mechanism's definition, not a methodological convenience.

## What it explains

**Why foil choice matters.** A head identified as "important for IOI" by contrasting IO tokens with subject tokens may not be identified as important when the foil is random tokens. The contrastive view makes this explicit: different foils define different mechanisms, and both results are correct under their respective contrasts.

**Why the same experiment can yield different circuits.** Two research groups running activation patching on "the same task" with different counterfactual distributions will find different circuits. Under the contrastive view, they are studying different contrastive mechanisms — not disagreeing about one mechanism.

**Why steering vectors are foil-dependent.** A "refusal direction" estimated as the axis separating harmful and harmless prompts is a contrastive object: it is defined by the pairing of those two prompt sets. A different pairing yields a different direction.

## What this view says

Two mechanism descriptions refer to the same mechanism iff they produce the same contrastive pattern across the same foil set. A "name mover" mechanism identified by contrasting IO with S tokens is a different contrastive mechanism from one identified by contrasting IO tokens with random tokens, even if both identify the same head — because the foil determines what aspect of the head's behavior is being explained.

## Evidence

Contrastive evidence requires specifying both the target condition and the foil:

- **Activation patching with a specific counterfactual** is inherently contrastive (the counterfactual is the foil)
- **Mean ablation** is less contrastive (the foil is an average, not a specific alternative)
- **Systematic foil variation**: if the mechanism's effect is stable across foils within a class but changes across foil classes, the contrastive boundary reveals the mechanism's scope

The strongest contrastive evidence comes from systematic variation of the foil set.

## Failure modes

**Foil dependence without acknowledgment.** Reporting a mechanism claim without specifying the foil, then treating it as an absolute characterization. Most circuit discovery papers do this — the counterfactual distribution is buried in the methods and the claim is stated as if absolute.

**Foil cherry-picking.** Choosing the foil that produces the cleanest result without testing alternatives. If only one foil yields a clean circuit, the mechanism may be an artifact of that particular contrast rather than a robust property of the model.

## Discriminating experiment

Take a published mechanism claim and vary the foil systematically. If the circuit identified for IOI changes when the foil is changed from "repeat the subject" to "output a random name" to "output nothing," the mechanism is foil-relative and should be stated as such.

## Formalism

The contrastive view is naturally expressed through [causal graphs](/mechanistic-views/formalism/causal-graph/) where edges are defined by interventional contrasts. It connects to the [instrumental view](/mechanistic-views/views/instrumental/) (both care about interventional effects) but differs in that the contrastive view takes the foil as constitutive of the mechanism's identity, not just a methodological choice.

## Relationship to other views

The contrastive view is orthogonal to the [object](/mechanistic-views/views/object/)–[role](/mechanistic-views/views/role/) distinction. A contrastive mechanism can be stated at the object level ("head 9.9 behaves differently under foil A vs B") or the role level ("the name-mover function is foil-relative"). What distinguishes the contrastive view is that the foil is part of the mechanism's definition — not a parameter of the experiment.

The [perspectival view](/mechanistic-views/views/perspectival/) diagnoses a related but distinct concern: that the analyst's choices shape what is found. The contrastive view makes one specific analyst choice — the foil — into a first-class part of the ontology rather than treating it as a bias to be eliminated.

---

## Technical details

### Identity criterion

Two mechanism descriptions refer to the same mechanism iff they produce the same contrastive pattern across the same foil set. Same foil set + same pattern = same mechanism.

### Relationship to Mechanistic Validity

The contrastive view's foil-dependence limits most validity criteria — the mechanism changes when the foil changes, so cross-foil generalization, invariance, and convergence are structurally impossible. Its strength is falsifiability: a claimed contrastive pattern can be tested by varying the foil systematically.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability) | [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity) | [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | 1/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | — | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency) | [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity), [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | 0/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | — | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | 0/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | — | [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability), [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | 0/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration) | [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | 1/5 |

**Why convergent validity (C5) is impossible.** Convergence requires a foil-independent mechanism to converge on. The contrastive view denies that such an object exists — the mechanism is constitutively foil-relative.

**Why measurement invariance (M2) is impossible.** Changing the foil changes the mechanism. This is not measurement error; it is the view's core claim.

### Further reading

- Van Fraassen, *The Scientific Image* (1980) — pragmatic theory of contrastive explanation
- Lipton, "Contrastive Explanation" (1990) — causal contrastive explanation
- For related views: [Instrumental view](/mechanistic-views/views/instrumental/) (shares interventional focus), [Perspectival view](/mechanistic-views/views/perspectival/) (diagnoses analyst-dependence more broadly)
