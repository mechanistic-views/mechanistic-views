---
title: Glossary
---

# Glossary

Quick-reference definitions for terms used across this site. For the mathematical formalisms (Grassmannian, gauge quotients, sheaves, stratification), see the [Formalisms](/formalism/) section.

---

## Framework terms

**Mechanistic view.** The set of commitments underlying a mechanistic claim, formalized as a 5-tuple $\sigma = (O, {\sim}, E, F, T)$: ontology, identity criterion, evidential standards, formalism, target. See [Framework](/framework/).

**Ontology.** What kind of entity counts as a mechanism — a component, a functional role, a subspace, a gauge-invariant structure, a formation trajectory, or a stratum point. Each of the [eight views](/views/) gives a different answer.

**Identity.** When two descriptions refer to the same mechanism. Must fit the ontology: component overlap for the [object view](/views/object/), role equivalence for the [role view](/views/role/), geodesic distance for the [subspace view](/views/subspace/), gauge-orbit membership for the [structural view](/views/structural/).

**Evidence.** What measurements can warrant a claim about a mechanism. Linked to ontology: a component claim is supported by ablation; a subspace claim needs [DAS/IIA](/views/subspace/#evidence) plus [subspace stability](/formalism/grassmannian/#subspace-stability); a structural claim needs measurements robust to reparameterization.

**Formalism.** The mathematical language used to express the claim. Ranges from [directed graphs](/formalism/directed-graph/) (object view) to [Whitney stratification](/formalism/stratification/) (stratified view). See [Formalisms](/formalism/) for all eight.

**Target.** What phenomenon the mechanism is supposed to explain — a specific behavior, a functional class, a representational variable, or a mechanism's origin.

**Coherence.** A view is coherent if the identity criterion fits the ontology, the evidence tracks the identity criterion, and the formalism can express both. Incoherent views produce contradictory demands. See [Framework](/framework/).

**Determination chain.** Ontology → Identity → Formalism. What a mechanism is determines when two are the same, which determines what mathematical language is needed.

**Mechanistic Validity.** A companion framework for evaluating whether mechanistic claims are warranted. Six-layer pipeline from description modes to verdicts, 27 criteria across 5 validity types. See [Mechanistic Validity Interface](/mechval-interface/).

## Technical terms

**Residual stream.** The $d$-dimensional vector accumulated by transformer blocks. The ambient space in which mechanisms are defined under the subspace, structural, and stratified views.

**Attention head.** A computational unit producing a weighted sum over positions. The OV circuit $W^{OV} = W^O W^V$ determines what information is moved; the QK circuit $W^{QK} = (W^K)^\top W^Q$ determines where attention is directed.

**Composition score.** $\|W^{OV}_u \cdot W^{QK}_v\|_F$ — a distribution-free upper bound on how much head $u$'s output influences head $v$'s attention pattern. Invariant under head permutations but not under orthogonal rotations. See [Fiber bundle quotient](/formalism/fiber-bundle-quotient/) for the gauge-invariance caveat.

**DAS (Distributed Alignment Search).** A method that searches over subspaces to find one whose swap transfers a causal variable. Produces a point on the [Grassmannian](/formalism/grassmannian/), evaluated by [IIA](/views/subspace/#evidence).

**IIA (Interchange Intervention Accuracy).** The fraction of inputs on which swapping a subspace's projection successfully transfers the target variable's value. Tests surgical intervention quality. Low IIA is ambiguous: the swap may be non-surgical, or the causal graph may be wrong.

**Causal subspace.** A subspace $S$ such that swapping the projection onto $S$ transfers a high-level causal variable. The mechanism under the [subspace view](/views/subspace/).

**Surgical intervention.** An intervention that changes one causal variable without directly altering others. Required for interventionist causal claims. IIA is the empirical test.

**Dark matter ratio.** (Full model logit difference) / (circuit logit difference). Ratio 1.0 means the circuit fully explains the model's behavior. Above 1.0 means incomplete coverage — which may reflect missing components or genuinely distributed computation.

**AGOP (Average Gradient Outer Product).** A training-time sensitivity measure. AGOP trajectories sometimes converge to the eventual DAS causal subspace before behavioral detection. Evidence for the [process view](/views/process/).

**Multi-domain triangulation.** Convergent evidence across structurally different domains (weight-space, activation-space, dynamics-space). Each domain alone is non-injective on mechanism space — two distinct mechanisms can look identical in one domain. See [Methods](/methods/#cross-cutting-observations).

**Qua-problem.** Identity claims are well-formed only relative to a description level. "Head 4.4 is the same mechanism as head 7.3" is meaningful only given a specified identity criterion — component overlap, role equivalence, or gauge-orbit membership give different answers.
