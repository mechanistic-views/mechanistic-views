---
title: Process View
---

# Process View

All the other views look at a trained model and ask "what mechanisms are in here?" The process view asks a different question: "how did these mechanisms get here?" It treats the training trajectory as part of the mechanism's description — when it formed, what had to form first, whether it appeared gradually or as a sudden phase transition.

This matters because the same final circuit can arise from different formation processes, and the formation process tells you things the final state does not. Induction heads appear suddenly at a specific training step, suggesting a phase transition rather than gradual construction. Grokking shows mechanisms that exist in the weights long before they appear in behavior. These are process-view claims: you cannot express them by looking only at the final checkpoint.

The process view is naturally paired with a static view (usually subspace or structural) — the static view says what the mechanism is at any given checkpoint, and the process view says how it changes across checkpoints. Its main limitation is cost: you need many training runs with many saved checkpoints. Its main conceptual risk is overreach — not every mechanism needs a developmental explanation, and describing the training trajectory is not always part of explaining the final behavior.

## Thesis

A mechanism is a process that forms over training and is individuated in part by its formation history: when it forms, what it depends on, what must precede it.

## What exists

Checkpoint trajectories, formation events, developmental prerequisites. The mechanism at time $t$ is the state of the process at $t$, not the static object it converges to.

## Identity

Two mechanisms are the same if they have the same formation process — specifically, if they share the same formation event type, developmental prerequisites, and formation criterion timing. This must be cashed out concretely: "same formation process" is not defined by loss trajectory similarity alone (many distinct mechanisms can share a loss curve shape) but by convergence of the process-view evidence: same AGOP subspace trajectory, same formation criterion timing across seeds, same developmental dependency structure.

Cross-seed identity under the process view requires: the formation event (phase transition, AGOP convergence, weight-space asymptote) occurs at the same relative training step, in the same order relative to other events, with the same prerequisites. Two mechanisms that form by different routes to the same final static structure are distinct under the process view but identical under the static views — this is a genuine empirical disagreement between views, not just a terminological one.

## Evidence

- **Checkpoint analysis**: subspace estimates ([DAS](https://learnmechinterp.com/topics/causal-abstraction/) or [AGOP](https://arxiv.org/abs/2110.04005)) measured across training steps
- **AGOP trajectories**: convergence to eventual causal subspace — empirically observed to precede behavioral detection in some cases (Nanda et al., grokking), but whether this generalises to arbitrary mechanisms is not established
- **Phase transitions**: sudden changes in IIA, [composition score](https://learnmechinterp.com/topics/composition-and-virtual-heads/), or behavior
- **Knockout retraining**: train a model with a proposed prerequisite component permanently ablated (a *training-time* intervention, not inference-time ablation) — if the target mechanism then fails to form, the prerequisite is established; if it forms anyway via a different route, the prerequisite claim is falsified

The **formation criterion** must be stated explicitly, because different criteria (behavioral threshold, AGOP convergence, weight-space structure) can disagree in timing. The process view should specify which criterion is used.

## Formalism

[Dynamical systems](/mechanistic-views/formalism/dynamical-system/) on weight space, [AGOP](https://arxiv.org/abs/2110.04005), training-time subspace estimation. The formation event corresponds to a trajectory crossing a boundary in mechanism space $\mathcal{M}$.

## What it explains

[Grokking](/mechanistic-views/cases/grokking/): the phase transition is the formation event of the Fourier generalization mechanism, preceded by a memorization phase. [Induction head](/mechanistic-views/cases/induction/) emergence: the sudden formation corresponds to a developmental event with a prerequisite (previous-token head formation). These phenomena are not visible from static views.

## What it lets you prove

- **Formation order**: mechanism A forms before mechanism B across seeds
- **Developmental prerequisite**: ablating component X prevents mechanism Y from forming
- **Lead time**: AGOP convergence precedes behavioral detection by $\Delta t$ steps

## Failure modes

**Computationally expensive.** Requires checkpoint analysis across many training runs.

**Formation criterion ambiguity.** Different criteria give different formation times; the choice changes the claim.

**Overreach.** Describing the training trajectory is not always part of explaining the final mechanism. The process view is needed when the phenomenon is inherently dynamic, not by default.

## Relationship to Mechanistic Validity

The process view adds a temporal dimension that no static view can address — formation order, developmental prerequisites, phase transitions. It inherits the static coverage of whichever view it combines with (typically subspace or structural) but adds its own criteria around dynamics. Its unique limitation: it requires many training runs, making most criteria expensive rather than impossible.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility) | [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | — | 2/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency) | [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity), [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 2/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | — | 2/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability), [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | — | 2/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | — | 2/5 |

**Covered** = the view's standard methods directly produce this evidence. **Possible** = testable under this view, but not standard practice. **Impossible** = the view's ontology structurally cannot satisfy this criterion.

**Why reliability (M1) is covered.** The process view naturally runs multiple training seeds — cross-seed consistency of formation timing and order is a core part of the evidence. This is reliability by construction.

**No impossible criteria.** The process view inherits whatever static view it combines with. When paired with the subspace or structural view, it has access to all their validity criteria plus temporal evidence. Its limitations are computational cost (many training runs) and formation criterion ambiguity (different progress measures give different formation times), not ontological impossibility.

## Further reading

- Nanda et al., "Progress measures for grokking via mechanistic interpretability" (2023) — AGOP-like progress measures track mechanism formation before behavioral detection, see [Grokking case study](/mechanistic-views/cases/grokking/)
- Olsson et al., "In-context Learning and Induction Heads" (2022) — induction head formation as a developmental event with prerequisites, see [Induction case study](/mechanistic-views/cases/induction/)
- For related views: [Object view](/mechanistic-views/views/object/) and [Subspace view](/mechanistic-views/views/subspace/) describe the static end-state; the process view describes how it got there. [Stratified view](/mechanistic-views/views/stratified/) also tracks mechanism dimensionality but at a fixed time point, not across training
