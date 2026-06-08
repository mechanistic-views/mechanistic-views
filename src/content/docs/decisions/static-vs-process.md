---
title: Static vs. Process Descriptions
---

# Static vs. Process Descriptions

**The fork.** Should a mechanism be described as a static object or as a process with a characteristic formation history?

## Option A: Static

The mechanism is the final circuit, subspace, or structural invariant. Training is how mechanisms are produced; the mechanisms themselves are the object of study.

**Appropriate when.** The target is behavioral (how does the model produce output $y$?), cross-snapshot comparison is not needed, and the phenomenon of interest is the final computation.

**Rules out.** Explaining why this mechanism formed rather than another; addressing phase transitions; developmental prerequisites.

## Option B: [Process](/views/process/)

The mechanism includes its formation history. Formation order and developmental prerequisites are part of the description.

**Required when.** The phenomenon is inherently dynamic ([grokking](/cases/grokking/), emergence); the claim involves formation timing; the target is intervention on training.

**Commits you to.** Checkpoint data; a **stated formation criterion**; dynamics-domain evidence.

## The formation criterion problem

Different criteria can give different formation times:
- **Behavioral threshold**: IIA exceeds a threshold
- **Subspace convergence**: AGOP subspace is within $\epsilon$ of the eventual DAS subspace
- **Weight-space structure**: composition score reaches asymptotic value

AGOP convergence often precedes behavioral detection by thousands of steps. A process-view claim must state which criterion is used.

## Distinguishing experiments

**Lead-time test.** Measure when AGOP subspace converges, when DAS IIA first exceeds threshold, and when composition score reaches asymptote. Coincidence supports the static description. Divergence reveals formation structure invisible to static views.

**Formation knockout.** Retrain with a proposed prerequisite absent. If the target mechanism fails to form, the prerequisite is established — a process-view claim that static descriptions cannot express.

## Recommended default

Static for well-studied final-state mechanisms. [Process view](/views/process/) by default for any temporally defined phenomenon: [grokking](/cases/grokking/), emergence, fine-tuning effects. Do not use static-only descriptions to make causal claims about training (e.g., "this mechanism forms *because of* weight decay") — those are process claims requiring process-view evidence. See the [dynamical system formalism](/formalism/dynamical-system/) for the mathematical framework.
