---
title: Static vs. Process Descriptions
---

# Static vs. Process Descriptions

**The fork.** Should a mechanism be described as a static object -- the circuit, subspace, or structural invariant in the final model -- or as a process with a characteristic formation history?

Most interpretability work treats the trained model as a fixed object and asks "what computation does it perform?" But some phenomena are inherently temporal: grokking (delayed generalization long after memorization), emergent capabilities, and phase transitions during training. For these, the static description misses the point.

## When you face this decision

You are studying a model that exhibits grokking on modular arithmetic. The trained model has a clean circuit that performs the correct computation. But you also have checkpoints from training, and they tell a story: the model first memorizes the training set, then -- thousands of steps later -- restructures its weights into a generalizing circuit. The final circuit is the same regardless of random seed, but the *transition* from memorization to generalization happens at different times and through different intermediate states.

If you describe only the final circuit (static view), you capture *what* the model computes but not *why* it computes it that way, or *when* the mechanism formed, or *what preceded it*. If a reviewer asks "would this mechanism still form under different training conditions?", the static description cannot answer.

## Option A: Static

The mechanism is the final circuit, subspace, or structural invariant. Training is how mechanisms are produced; the mechanisms themselves are the object of study.

**What it buys you.** Simplicity. You do not need checkpoint data. Your analysis can be done on a single model snapshot. For most behavioral questions -- "how does this model produce output Y?" -- the static description is sufficient and much cheaper to obtain.

**What it rules out.** Explaining why this mechanism formed rather than another. Addressing phase transitions. Establishing developmental prerequisites (e.g., "induction heads form before IOI circuits"). Making causal claims about training (e.g., "weight decay causes this mechanism to form") -- those are inherently process claims.

## Option B: Process

The mechanism includes its formation history. Formation order, developmental prerequisites, and the dynamics of how the mechanism crystallized are part of the description.

**What it buys you.** The ability to make claims about training interventions, phase transitions, and developmental sequences. If the goal is to control what mechanisms form (steering training, preventing undesirable circuits from developing), the process view is necessary.

**What it commits you to.** Checkpoint data across training. A **stated formation criterion** -- a precise definition of when you consider the mechanism to have "formed." And dynamics-domain evidence, which is more expensive to collect than static analysis.

## The formation criterion problem

Different criteria can give different formation times for the same mechanism:

- **Behavioral threshold**: IIA (Interchange Intervention Accuracy -- a measure of how well subspace interventions reproduce expected behavior) exceeds a threshold.
- **Subspace convergence**: the AGOP (Average Gradient Outer Product) subspace is within some distance of the eventual DAS subspace.
- **Weight-space structure**: the composition score between relevant heads reaches its asymptotic value.

These can disagree substantially. AGOP convergence often precedes behavioral detection by thousands of training steps -- the weight-space structure for the mechanism is in place long before the mechanism is behaviorally detectable. This means a process-view claim must state which formation criterion it uses, because "when the mechanism forms" is not a single well-defined moment.

## Distinguishing experiments

**Lead-time test.** Measure when the AGOP subspace converges, when DAS IIA first exceeds threshold, and when the composition score reaches asymptote. If these coincide, the static description loses nothing -- the mechanism appears all at once, and formation dynamics are uninteresting. If they diverge (e.g., weight structure precedes behavioral detection by thousands of steps), the divergence reveals formation structure that static analysis cannot see.

**Formation knockout.** Retrain the model with a proposed prerequisite absent -- for example, train without the data that produces induction heads, then check whether the IOI circuit forms. If the target mechanism fails to form, the prerequisite is established. This is a process-view claim that static descriptions cannot express at all: "mechanism X requires mechanism Y to form first."

## Recommended default

Use **static descriptions** for well-studied final-state mechanisms where the research question is about what the model computes, not how it got there. This covers most circuit analysis work.

Use the **process view** by default for any temporally defined phenomenon: grokking, emergence, fine-tuning effects, phase transitions. Do not use static-only descriptions to make causal claims about training (e.g., "this mechanism forms *because of* weight decay") -- those are process claims that require process-view evidence.
