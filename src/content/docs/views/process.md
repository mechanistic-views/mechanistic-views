---
title: Process View
---

# Process View

All the other views look at a trained model and ask "what mechanisms are in here?" The process view asks a different question: "how did these mechanisms get here?" It treats the training trajectory as part of the mechanism's description — when it formed, what had to form first, whether it appeared gradually or as a sudden phase transition.

This matters because the same final circuit can arise from different formation processes, and the formation process tells you things the final state does not.

## Thesis

A mechanism is a process that forms over training, individuated in part by its formation history: when it forms, what it depends on, what must precede it.

## What it explains

**Grokking.** The generalization mechanism exists in the weights long before it appears in behavior. The phase transition from memorization to generalization is a formation event — one that static views looking only at the final checkpoint cannot see. The process view makes the delayed generalization into a core part of what the mechanism IS, not just a historical curiosity about how it was found (Nanda et al., 2023).

**Induction head emergence.** Induction heads appear suddenly at a specific training step, not gradually. This suggests a phase transition rather than gradual construction. The formation has a prerequisite: previous-token heads must form first. These developmental dependencies — mechanism B cannot form until mechanism A exists — are invisible from any static view (Olsson et al., 2022).

**Why the same final circuit can be different mechanisms.** Two models might converge to the same circuit (same subspace, same gauge orbit) by different training paths. The process view says these are different mechanisms because they formed differently. This is a genuine empirical disagreement with the static views, not a terminological one.

## What this view says

The mechanism at time $t$ is the state of the process at $t$, not the static object it converges to. What "exists" under this view includes checkpoint trajectories, formation events, and developmental prerequisites.

Two mechanisms are the same if they share the same formation process: same formation event type, same developmental prerequisites, same formation criterion timing. Cross-seed identity requires that the formation event occurs at the same relative training step, in the same order relative to other events, with the same prerequisites.

The process view is naturally paired with a static view (usually [subspace](/mechanistic-views/views/subspace/) or [structural](/mechanistic-views/views/structural/)) — the static view says what the mechanism is at any given checkpoint, and the process view says how it changes across checkpoints. It is not a replacement for static views but an additional dimension of description.

## When it works and when it doesn't

The process view is needed when the phenomenon is inherently dynamic: phase transitions, developmental prerequisites, formation order, delayed generalization. For these cases, no static view can express the relevant claims.

**Computationally expensive.** Requires checkpoint analysis across many training runs with many saved checkpoints. This is impractical for large models where each checkpoint is tens of gigabytes.

**Formation criterion ambiguity.** Different criteria — behavioral threshold, AGOP (average gradient outer product — a matrix summarizing the gradient structure of the learned function) convergence, weight-space structure — can give different formation times for the same mechanism. The formation criterion must be stated explicitly, and the choice changes the claim.

**Overreach.** Not every mechanism needs a developmental explanation. Describing the training trajectory is informative when the phenomenon is dynamic, but adding "it formed at step 5000" to a mechanism description does not always add explanatory power. The process view is needed when the phenomenon is inherently dynamic, not by default.

---

## Technical details

### Evidence

- **Checkpoint analysis**: subspace estimates ([DAS](https://learnmechinterp.com/topics/causal-abstraction/) or AGOP) measured across training steps
- **AGOP trajectories**: convergence to eventual causal subspace — empirically observed to precede behavioral detection in some cases (Nanda et al., grokking), but whether this generalizes to arbitrary mechanisms is not established
- **Phase transitions**: sudden changes in IIA, [composition score](https://learnmechinterp.com/topics/composition-and-virtual-heads/), or behavior
- **Knockout retraining**: train a model with a proposed prerequisite component permanently ablated (a *training-time* intervention, not inference-time ablation) — if the target mechanism then fails to form, the prerequisite is established; if it forms anyway via a different route, the prerequisite claim is falsified

### What it lets you prove

- **Formation order**: mechanism A forms before mechanism B across seeds
- **Developmental prerequisite**: ablating component X during training prevents mechanism Y from forming
- **Lead time**: AGOP convergence precedes behavioral detection by $\Delta t$ steps

### Formalism

[Dynamical systems](/mechanistic-views/formalism/dynamical-system/) on weight space, AGOP, training-time subspace estimation. The formation event corresponds to a trajectory crossing a boundary in mechanism space $\mathcal{M}$.

### Relationship to Mechanistic Validity

The process view adds temporal evidence that no static view can address. It inherits the static coverage of whichever view it combines with.

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability), [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility) | [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | — | 2/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency) | [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity), [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control) | — | 2/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture) | — | 2/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability), [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | — | 2/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence) | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | — | 2/5 |

**Why reliability (M1) is covered.** The process view naturally runs multiple training seeds — cross-seed consistency of formation timing and order is reliability by construction.

**No impossible criteria.** When paired with the subspace or structural view, the process view has access to all their criteria plus temporal evidence. Limitations are computational cost, not ontological impossibility.

### Further reading

- Nanda et al., "Progress measures for grokking via mechanistic interpretability" (2023) — progress measures track mechanism formation before behavioral detection
- Olsson et al., "In-context Learning and Induction Heads" (2022) — induction head formation as a developmental event with prerequisites
- For related views: [Object view](/mechanistic-views/views/object/) and [Subspace view](/mechanistic-views/views/subspace/) describe the static end-state; the process view describes how it got there
