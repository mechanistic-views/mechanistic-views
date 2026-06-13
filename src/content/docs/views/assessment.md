---
title: View Assessment
---

# View Assessment

The [validity coverage tables](/mechanistic-views/views/#validity-coverage-comparison) on each view page answer one question: **within this view, which mechanistic validity criteria can you satisfy?** That is a coverage question — it tells you the ceiling of what your methods can validate if you adopt a given view.

This page asks a different question: **how justified is each view itself, as a claim about what neural network mechanisms are?**

These are different questions. The object view has modest validity coverage (6/27) but strong empirical support — we know circuits exist and ablation works. The stratified view has broad coverage (16/27) but limited empirical support — most of its theoretical apparatus has not been tested. Coverage is about what you *could* prove; justification is about what *has been* shown.

## The distinction

| | Coverage (existing tables) | Justification (this page) |
|---|---|---|
| Question | What can you validate if you adopt this view? | What evidence supports adopting this view? |
| Subject | Mechanistic claims made within the view | The view's own claims about neural networks |
| Example | "Within the object view, necessity and sufficiency are testable" | "The object view's assumption that mechanisms are localized components is supported by circuit discovery results but challenged by dark matter" |

## Assessment by view

### Instrumental

**Claim:** Mechanisms are useful predictive models, nothing more.

**Evidence for:**
- Undeniably works — logit lens, probing, and behavioral prediction all succeed without ontological commitment
- Immune to replication failures that afflict stronger views (if the prediction works, the prediction works)

**Evidence against:**
- Cannot explain *why* a prediction works, which limits its usefulness for intervention design
- No evidence *against* this view is possible — it is unfalsifiable by construction, which is a philosophical weakness

**Assessment:** Safe but limited. The instrumental view is justified as a floor — everything the field does is at least instrumentally useful — but its unfalsifiability means it cannot be wrong, which means it cannot be informative.

---

### Perspectival

**Claim:** Mechanisms are method-relative projections. There is no method-independent ground truth about "the mechanism."

**Evidence for:**
- Methods genuinely disagree: activation patching, DAS, and SAE decomposition often identify different components as "the mechanism" for the same task
- Probing accuracy varies dramatically with probe architecture, suggesting what you find depends on how you look

**Evidence against:**
- When independent methods *do* converge (as in grokking, where weight decomposition and activation probing both identify Fourier structure), that convergence is hard to explain under pure perspectivalism
- The view predicts that method disagreement is the baseline — but some mechanisms show robust cross-method agreement

**Assessment:** Genuinely useful as a corrective — it prevents premature reification of method-specific findings. Less convincing as a complete position, because convergence phenomena exist and demand explanation.

---

### Object

**Claim:** Mechanisms are specific model components (heads, neurons, channels). Identity is component overlap.

**Evidence for:**
- The strongest empirical base of any view. Circuit discovery (IOI, induction heads, greater-than) has repeatedly identified specific components with causal roles
- Ablation and activation patching directly test necessity and sufficiency of components
- Most published interpretability work implicitly adopts this view and produces useful results

**Evidence against:**
- Dark matter: circuits rarely account for 100% of model behavior. The gap could be measurement error or genuinely distributed computation
- Coordinate dependence: "head 9.1 is the name mover" is basis-dependent. Rotate the residual stream and the same computation lives in different components
- Backup circuits: knock out the "name movers" and other heads take over the role, suggesting the role matters more than the components
- Cross-model identity is undefined — "head 9.1" in GPT-2 has no counterpart in Llama

**Assessment:** Well-supported for single-model circuit discovery. Breaks down for cross-model claims, distributed mechanisms, and identity questions. The view's limitations are well-documented but do not invalidate its core use case.

---

### Role

**Claim:** Mechanisms are functional roles (name-mover, S-inhibition head). Identity is role equivalence.

**Evidence for:**
- Induction heads appear across diverse model families — a role-level regularity that the object view cannot express
- IOI backup circuits show that the role persists even when specific components are ablated
- Cross-model comparison becomes possible when roles are independently specified

**Evidence against:**
- Post-hoc role assignment: labels like "name mover" are read off the same activations used to identify the component. Any behavior can be given a plausible role label
- Vague role definitions are unfalsifiable — "roughly moves names" is satisfied by too many components
- No established method for predicting which components will fill a role in a new model

**Assessment:** Conceptually important, especially for cross-model work. The main vulnerability is that role claims are easy to make and hard to falsify. The view becomes genuinely useful only when roles are precisely specified and independently testable.

---

### Subspace

**Claim:** Mechanisms are causal subspaces — points on the Grassmannian $\mathrm{Gr}(k,d)$. Identity is proximity in Grassmannian distance.

**Evidence for:**
- DAS successfully recovers causal subspaces with high IIA on multiple tasks
- Subspaces are coordinate-invariant, resolving the object view's basis-dependence problem
- Weight-space SVD and activation-space DAS sometimes converge on the same Grassmannian point, providing cross-domain evidence

**Evidence against:**
- The Sutter vacuity problem: with unrestricted nonlinear alignment maps, any model can achieve 100% IIA on any task. The subspace view's restriction to linear maps avoids this but is an assumption, not a theorem
- DAS finds subspaces in random models too — the method's ability to find *something* does not establish that what it finds is real
- Linearity assumption: some mechanisms may live on curved manifolds where Grassmannian geometry is the wrong framework

**Assessment:** The strongest mid-commitment position. Addresses the object view's coordinate-dependence problems while remaining computationally tractable. The vacuity concern is serious but has a clear resolution path (restricting alignment maps — what we propose as G-SCM). The linearity assumption is a known limitation, not a fatal flaw.

---

### Structural

**Claim:** Mechanisms are gauge-invariant structures — equivalence classes of weight configurations under function-preserving transformations. Identity is gauge-orbit membership.

**Evidence for:**
- Gauge symmetries in transformers are mathematically established (head permutations, scaling symmetries)
- Composition scores and singular value spectra are gauge-invariant quantities that do distinguish mechanisms
- The framework resolves cross-architecture identity in principle

**Evidence against:**
- Computability: holonomy, cosheaf cohomology, and gauge-orbit comparison have not been computed for any real transformer at scale
- Wrong symmetry group: LayerNorm breaks the full rotation symmetry, and the correct gauge group for transformers with LayerNorm is not established
- The view's objects (gauge orbits, holonomy groups) are currently more theoretical constructs than empirical tools

**Assessment:** Theoretically compelling — it correctly identifies that basis-dependent claims are not real claims about computation. Practically limited by the gap between what the theory demands and what the toolkit can deliver. The value today is more as a theoretical ceiling (what the right answer looks like) than as a working methodology.

---

### Process

**Claim:** Mechanisms include their formation trajectories. Identity is trajectory type (same sequence of qualitative phases).

**Evidence for:**
- Grokking is a clear process-level phenomenon: the mechanism's formation involves a sharp phase transition that static analysis misses
- Induction head formation follows a characteristic developmental sequence across models
- AGOP subspace convergence sometimes precedes behavioral detection, suggesting formation structure is real

**Evidence against:**
- The formation criterion problem: behavioral threshold, subspace convergence, and weight-space structure can give different formation times. Which is "real"?
- Checkpoint analysis is expensive and model-specific
- Few process-level claims have been replicated across model families

**Assessment:** The process view is not a standalone view — it is a temporal modifier that pairs with a static view. Its unique contribution (formation order, developmental prerequisites) is well-supported for specific phenomena (grokking, induction heads) but has not been shown to be generally necessary. Most mechanisms can be adequately described statically.

---

### Stratified

**Claim:** Mechanism space is a stratified space with distinct geometric strata ($\mathcal{M}_1$ directions, $\mathcal{M}_k$ subspaces, $\mathcal{M}_\Sigma$ manifolds, etc.). Identity is same-stratum same-point.

**Evidence for:**
- Different methods do seem to operate on different geometric types — SAEs find directions, DAS finds subspaces, manifold steering finds curves
- The "methods as charts" framing explains method disagreement without declaring any method wrong
- Grokking's circular representation is a concrete example of a non-linear stratum

**Evidence against:**
- Stratum assignment has no canonical procedure — no algorithm tells you which stratum a mechanism occupies
- The Duhem-Quine problem: if an experiment fails to show stratum-specific patterns, you can always claim the wrong stratum was assigned
- Most of the theoretical apparatus (cosheaf cohomology, stratum-preserving maps, pullback metrics) has not been computed for any real model
- The strata may not be discrete categories — $\mathcal{M}_1$ and $\mathcal{M}_k$ might just be low-curvature limits of $\mathcal{M}_\Sigma$, making the stratification illusory

**Assessment:** The most ambitious view, with the broadest explanatory scope and the least empirical support. Its core insight — that method disagreement often reflects geometric mismatch rather than empirical contradiction — is valuable regardless of whether the full stratification machinery is correct. The main risk is that the mathematical sophistication creates an illusion of rigor for claims that have not been tested.

## Summary

| View | Empirical support | Theoretical coherence | Main vulnerability |
|---|---|---|---|
| Instrumental | Strong (trivially) | Complete | Unfalsifiable; cannot explain *why* |
| Perspectival | Moderate | Complete | Cannot explain convergence |
| Object | Strong | Moderate | Coordinate-dependent; no cross-model identity |
| Role | Moderate | Moderate | Post-hoc labeling; vague specifications |
| Subspace | Moderate-strong | Strong | Vacuity; linearity assumption |
| Structural | Weak | Strong | Computationally intractable |
| Process | Moderate (for specific phenomena) | Moderate | Not standalone; formation criterion ambiguity |
| Stratified | Weak | Ambitious | Stratum assignment unsolved; Duhem-Quine |

The pattern: empirical support and theoretical ambition are roughly inversely correlated. The views with the most evidence (object, instrumental) make the weakest claims. The views with the broadest explanatory scope (structural, stratified) have the least empirical grounding. This is expected — stronger claims require more evidence, and the field has not yet produced that evidence for the higher-commitment views.
