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

**Composition score.** $\|W^{OV}_u \cdot W^{QK}_v\|_F$ — a distribution-free upper bound on how much head $u$'s output influences head $v$'s attention pattern. Invariant under head permutations but not under orthogonal rotations. See [composition and virtual heads on learnmechinterp](https://learnmechinterp.com/topics/composition-and-virtual-heads/) and the [fiber bundle quotient](/formalism/fiber-bundle-quotient/) for the gauge-invariance caveat.

**DAS (Distributed Alignment Search).** A method that searches over subspaces to find one whose swap transfers a causal variable. Produces a point on the [Grassmannian](/formalism/grassmannian/), evaluated by [IIA](/views/subspace/#evidence). See [causal abstraction on learnmechinterp](https://learnmechinterp.com/topics/causal-abstraction/).

**IIA (Interchange Intervention Accuracy).** The fraction of inputs on which swapping a subspace's projection successfully transfers the target variable's value. Tests surgical intervention quality. Low IIA is ambiguous: the swap may be non-surgical, or the causal graph may be wrong.

**Causal subspace.** A subspace $S$ such that swapping the projection onto $S$ transfers a high-level causal variable. The mechanism under the [subspace view](/views/subspace/).

**Surgical intervention.** An intervention that changes one causal variable without directly altering others. Required for interventionist causal claims. IIA is the empirical test.

**Dark matter ratio.** (Full model logit difference) / (circuit logit difference). Ratio 1.0 means the circuit fully explains the model's behavior. Above 1.0 means incomplete coverage — which may reflect missing components or genuinely distributed computation.

**AGOP (Average Gradient Outer Product).** A training-time sensitivity measure ([Radhakrishnan et al. 2022](https://arxiv.org/abs/2110.04005)). AGOP trajectories sometimes converge to the eventual DAS causal subspace before behavioral detection. Evidence for the [process view](/views/process/).

**Multi-domain triangulation.** Convergent evidence across structurally different domains (weight-space, activation-space, dynamics-space). Each domain alone is non-injective on mechanism space — two distinct mechanisms can look identical in one domain. See [Methods](/methods/#cross-cutting-observations).

**Qua-problem.** Identity claims are well-formed only relative to a description level. "Head 4.4 is the same mechanism as head 7.3" is meaningful only given a specified identity criterion — component overlap, role equivalence, or gauge-orbit membership give different answers.

## Methods

**Activation patching.** Replacing a component's activations from one forward pass into another to test causal relevance. See [activation patching on learnmechinterp](https://learnmechinterp.com/topics/activation-patching/) and the [object view](/views/object/).

**Path patching.** Variant of activation patching that tests specific information-flow paths. See [activation patching on learnmechinterp](https://learnmechinterp.com/topics/activation-patching/#path-patching).

**SAE (Sparse Autoencoder).** Learns an overcomplete [dictionary](/formalism/dictionary/) of feature directions from a model's activations. Each feature is a candidate $\mathrm{Gr}(1, d)$ mechanism. The sparsity criterion is reconstruction-based, not causal — causal validation (steering, ablation) is needed to establish that a feature is a mechanism. See [sparse autoencoders on learnmechinterp](https://learnmechinterp.com/topics/sparse-autoencoders/) and the [SAE features discussion](/views/subspace/#sae-features-and-the-subspace-view) on the subspace view page.

**Linear probing.** Trains a [linear classifier](/formalism/linear-classifier/) on intermediate activations to test whether a concept is linearly represented. Observational, not causal. See [probing classifiers on learnmechinterp](https://learnmechinterp.com/topics/probing-classifiers/).

**Logit lens / tuned lens.** Applies the unembedding matrix (or a learned affine transform) at intermediate layers to read off vocabulary-level predictions. Observational layer-by-layer readout. See [logit lens on learnmechinterp](https://learnmechinterp.com/topics/logit-lens-and-tuned-lens/) and the [linear projection formalism](/formalism/linear-projection/).

## Additional terms

**Formation criterion.** The threshold or condition used to declare that a mechanism has "formed" during training. Different criteria (behavioral threshold, AGOP convergence, weight-space structure) can disagree in timing. Process-view claims must specify which criterion is used. See [Process view](/views/process/).

**G-SCM (Grassmannian Structural Causal Model).** Extension of Pearl's SCM with subspaces as nodes and weight-induced transport maps as edges. Requiring alignment maps to respect transport structure is expected to address vacuity concerns (Sutter et al. 2025). See the [Grassmannian formalism](/formalism/grassmannian/).

**Gauge-invariant.** A property that depends only on the gauge orbit $[\theta] \in \mathcal{W}/\mathcal{G}$, not on any particular weight configuration within it. Examples: singular values of $W^{OV}$, principal angles, effective rank. See the [structural view](/views/structural/) and [fiber bundle quotient](/formalism/fiber-bundle-quotient/).

**Principal angles.** The angles $\theta_1, \ldots, \theta_k$ between two subspaces $S_1, S_2 \in \mathrm{Gr}(k, d)$, computed as $\cos\theta_i = \sigma_i(Q_1^\top Q_2)$. Used to define geodesic distance on the Grassmannian. See the [Grassmannian deep dive](/formalism/deep-dives/grassmannian/).

**Fréchet variance.** $\sigma^2_F = \frac{1}{n}\sum_i d(\bar{S}, S_i)^2$ — measures how stable a recovered subspace is across seeds or prompt distributions. Low Fréchet variance means the subspace is a reliable measurement; high variance means it may be an artifact. See [Grassmannian formalism](/formalism/grassmannian/#subspace-stability).
