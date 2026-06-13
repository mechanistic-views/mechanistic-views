---
title: Localized vs. Distributed
---

# Localized vs. Distributed

**The fork.** Can the mechanism be assigned to a compact circuit, or is it genuinely distributed across the network?

This is the decision that determines whether circuit discovery -- the workhorse of mechanistic interpretability -- can even work for your phenomenon. If the mechanism is localized, circuit discovery will find it. If it is genuinely distributed, circuit discovery will either miss it or return a circuit that covers most of the model, which is not a useful explanation.

## When you face this decision

You are studying how GPT-2 Small handles IOI (indirect object identification). You run ACDC and recover a circuit of about 26 heads and their edges. You measure how well this circuit accounts for the full model's behavior using the **dark matter ratio**:

$$r = \frac{\text{full model logit difference}}{\text{circuit logit difference}}$$

A ratio of 1.0 means the circuit fully explains the model's behavior on this task. (Note: some papers define this ratio inverted, as circuit/full, giving values below 1.0 for incomplete coverage. Always check which convention a paper uses.)

For IOI, the ratio is close to 1.0 -- the circuit accounts for most of the behavior. But suppose you try the same approach on a different task and get $r = 2.5$. Your circuit explains less than half the model's performance. Now what?

**Degenerate cases.** If the circuit logit difference is near zero or negative -- which happens when circuit components interfere destructively -- the ratio is undefined or flips sign. In these cases, report the raw logit differences directly rather than the ratio.

## The two interpretations of high $r$

When the dark matter ratio is persistently high, there are two very different explanations:

**(A) Incomplete recovery.** A localized mechanism exists, but your circuit proposal missed part of it. The "dark matter" is a measurement artifact. The fix is more circuit recovery work -- find the missing components.

**(B) Genuine distribution.** No compact circuit captures the mechanism. The computation is spread across the network in a way that resists localization. The fix is not more circuit recovery but a fundamentally different analysis approach.

These are not equivalent, and conflating them leads to wasted effort. Interpretation (A) calls for better circuit discovery. Interpretation (B) calls for distributed analysis methods (subspace interventions, representation-level characterization). If the mechanism is genuinely distributed and you keep searching for the missing circuit components, you will spend a long time finding nothing.

## Distinguishing experiments

No single experiment cleanly separates these interpretations. Use them in combination.

**Iterative circuit expansion.** Repeatedly add the next most important component to your circuit and re-measure $r$. If the ratio converges to 1.0 while the circuit remains a small fraction of the model, the mechanism is localized and your initial circuit was just incomplete. If the circuit grows to cover most of the model before $r$ approaches 1.0, localization is failing.

**Cross-method convergence.** Run multiple independent methods -- activation patching, DAS (Distributed Alignment Search, which finds subspaces where swapping activations between inputs changes model behavior as if a causal variable changed), and SAE channel analysis. If they all recover different components and none substantially reduces $r$, this is convergent evidence for distribution. If they converge on the same components, the mechanism is likely localized and your initial method just missed some of them.

**Cohomological test.** For researchers with the relevant mathematical background: build the circuit cosheaf (a formal structure that tracks how local circuit descriptions glue together across the network) and estimate $H^1$. Non-zero $H^1$ indicates a topological obstruction to localization in that particular cosheaf proposal. However, this only establishes that *this specific description* cannot be localized -- it does not rule out the existence of some other description that can.

## Recommended default

Default to **localization** for well-studied tasks where circuit discovery methods have a track record (IOI, induction, greater-than). These tasks have compact circuits, and the dark matter ratio is typically close to 1.0.

Treat **distribution** as the working hypothesis when $r$ is persistently high despite multiple recovery attempts with independent methods. But be cautious about strong claims of irreducible distribution -- a non-zero $H^1$ for one cosheaf proposal does not prove that no localized description exists, only that a particular one failed.
