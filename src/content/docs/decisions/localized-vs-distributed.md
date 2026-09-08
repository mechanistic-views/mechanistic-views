---
title: Localized vs. Distributed
---

# Localized vs. Distributed

**The fork.** Can the mechanism be assigned to a compact circuit, or is it genuinely distributed across the network?

This is the decision that determines whether circuit discovery -- the workhorse of mechanistic interpretability -- can even work for your phenomenon. If the mechanism is localized, circuit discovery will find it. If it is genuinely distributed, circuit discovery will either miss it or return a circuit that covers most of the model, which is not a useful explanation.

## When you face this decision

You are studying how GPT-2 Small handles IOI (indirect object identification). Activation patching identifies a small component set as causally necessary -- the 26-head circuit. DAS, run on the same task, identifies a high-dimensional subspace spanning many more components. Which one is the mechanism?

The two results need not be contradictory. The patching identifies the components whose activation values lie in the relevant subspace; DAS characterizes the subspace. Under the object view the question is which minimal component set is causally necessary and sufficient; under the subspace view it is the dimensionality and localizability of the causal subspace; under the stratified view it is which stratum the evidence supports, which is the language in which the two results are compatible descriptions at different resolutions.

The decision bites when a circuit recovers much less of the model's behavior than the IOI circuit does. Two very different explanations are then live:

**(A) Incomplete recovery.** A localized mechanism exists, but your circuit proposal missed part of it. The "dark matter" is a measurement artifact. The fix is more circuit recovery work -- find the missing components.

**(B) Genuine distribution.** No compact circuit captures the mechanism. The computation is spread across the network in a way that resists localization. The fix is not more circuit recovery but a fundamentally different analysis approach.

These are not equivalent, and conflating them leads to wasted effort. Interpretation (A) calls for better circuit discovery. Interpretation (B) calls for distributed analysis methods (subspace interventions, representation-level characterization). If the mechanism is genuinely distributed and you keep searching for the missing circuit components, you will spend a long time finding nothing.

## Distinguishing experiments

No single experiment cleanly separates these interpretations. Use them in combination.

**Iterative circuit expansion.** Repeatedly add the next most important component to your circuit and re-measure $r$. If the ratio converges to 1.0 while the circuit remains a small fraction of the model, the mechanism is localized and your initial circuit was just incomplete. If the circuit grows to cover most of the model before $r$ approaches 1.0, localization is failing.

**Cross-method convergence.** Run multiple independent methods -- activation patching, DAS (Distributed Alignment Search, which finds subspaces where swapping activations between inputs changes model behavior as if a causal variable changed), and SAE channel analysis. If they all recover different components and none substantially reduces $r$, this is convergent evidence for distribution. If they converge on the same components, the mechanism is likely localized and your initial method just missed some of them.

**Stratum stability.** Recompute two quantities at a second measurement resolution -- a different hook granularity, or DAS under a different alignment constraint. The first is the participation ratio of the causal subspace's eigenspectrum, which reports how many directions carry the effect without requiring a variance threshold. The second is localizability: the smallest fraction of components whose ablation recovers a fixed fraction of the full causal effect. Agreement across resolutions warrants a stratum assignment; disagreement means the analysis has not identified one.

## Recommended default

Default to **localization** for well-studied tasks where circuit discovery methods have a track record (IOI, induction, greater-than). These tasks have compact circuits, though IOI still admits rival head sets of comparable faithfulness (Chen et al., 2026).

Treat **distribution** as the working hypothesis when $r$ is persistently high despite multiple recovery attempts with independent methods. But be cautious about strong claims of irreducible distribution -- a distributed result under one measurement resolution does not prove that no localized description exists, only that the resolutions tried have not found one.
