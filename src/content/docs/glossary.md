---
title: Glossary
---

# Glossary

Quick-reference definitions for terms used across this site. For the mathematical formalisms (Grassmannian, gauge quotients, sheaves, stratification), see the [Formalisms](/mechanistic-views/formalism/) section.

---

## Framework terms

<span id="mechanistic-view"></span>**Mechanistic view.** The set of commitments underlying a mechanistic claim, formalized as a 5-tuple $\sigma = (O, {\sim}, E, F, T)$: ontology, identity criterion, evidential standards, formalism, target. See [Framework](/mechanistic-views/framework/).

<span id="ontology"></span>**Ontology.** What kind of entity counts as a mechanism — a component, a functional role, a subspace, a gauge-invariant structure, a formation trajectory, or a stratum point. Each of the [nine views](/mechanistic-views/views/) gives a different answer.

<span id="identity"></span>**Identity.** When two descriptions refer to the same mechanism. Must fit the ontology: component overlap for the [object view](/mechanistic-views/views/object/), role equivalence for the [role view](/mechanistic-views/views/role/), geodesic distance for the [subspace view](/mechanistic-views/views/subspace/), gauge-orbit membership for the [structural view](/mechanistic-views/views/structural/).

<span id="evidence"></span>**Evidence.** What measurements can warrant a claim about a mechanism. Linked to ontology: a component claim is supported by ablation; a subspace claim needs [DAS/IIA](/mechanistic-views/views/subspace/#evidence) plus [subspace stability](/mechanistic-views/formalism/grassmannian/#subspace-stability); a structural claim needs measurements robust to reparameterization.

<span id="formalism"></span>**Formalism.** The mathematical language used to express the claim. Ranges from [directed graphs](/mechanistic-views/formalism/directed-graph/) (object view) to [resolution-indexed strata](/mechanistic-views/formalism/stratification/) (stratified view). See [Formalisms](/mechanistic-views/formalism/) for all nine view-associated formalisms.

<span id="target"></span>**Target.** What phenomenon the mechanism is supposed to explain — a specific behavior, a functional class, a representational variable, or a mechanism's origin.

<span id="coherence"></span>**Coherence.** A view is coherent if the identity criterion fits the ontology, the evidence tracks the identity criterion, and the formalism can express both. Incoherent views produce contradictory demands. See [Framework](/mechanistic-views/framework/).

<span id="determination-chain"></span>**Determination chain.** Ontology → Identity → Formalism. What a mechanism is determines when two are the same, which determines what mathematical language is needed.

<span id="mechanistic-validity"></span>**Mechanistic Validity.** A framework for evaluating whether mechanistic claims are warranted. Six-layer pipeline from description modes to verdicts, 36 criteria across 5 validity types. See [Mechanistic Validity Interface](/mechanistic-views/mechval-interface/).

## Technical terms

<span id="residual-stream"></span>**Residual stream.** The $d$-dimensional vector accumulated by transformer blocks. The ambient space in which mechanisms are defined under the subspace, structural, and stratified views.

<span id="attention-head"></span>**Attention head.** A computational unit producing a weighted sum over positions. The OV circuit $W^{OV} = W^O W^V$ determines what information is moved; the QK circuit $W^{QK} = (W^K)^\top W^Q$ determines where attention is directed.

<span id="composition-score"></span>**Composition score.** $\|W^{OV}_u \cdot W^{QK}_v\|_F$ — a distribution-free upper bound on how much head $u$'s output influences head $v$'s attention pattern. Invariant under head permutations but not under orthogonal rotations. See [composition and virtual heads on learnmechinterp](https://learnmechinterp.com/topics/composition-and-virtual-heads/) and the [fiber bundle quotient](/mechanistic-views/formalism/fiber-bundle-quotient/) for the gauge-invariance caveat.

<span id="qk-ov-circuits"></span>**QK/OV circuits.** The two functional circuits within each attention head. The QK circuit $W^{QK} = (W^K)^\top W^Q$ computes attention patterns (where to attend); the OV circuit $W^{OV} = W^O W^V$ determines what information is moved. SVD of these matrices reveals the head's computational structure. See [QK/OV circuits on learnmechinterp](https://learnmechinterp.com/topics/qk-ov-circuits/).

<span id="das"></span>**DAS (Distributed Alignment Search).** A method that searches over subspaces to find one whose swap transfers a causal variable. Produces a point on the [Grassmannian](/mechanistic-views/formalism/grassmannian/), evaluated by [IIA](#iia). See [causal abstraction on learnmechinterp](https://learnmechinterp.com/topics/causal-abstraction/).

<span id="iia"></span>**IIA (Interchange Intervention Accuracy).** The fraction of inputs on which swapping a subspace's projection successfully transfers the target variable's value. Tests surgical intervention quality. Low IIA is ambiguous: the swap may be non-surgical, or the causal graph may be wrong.

<span id="causal-subspace"></span>**Causal subspace.** A subspace $S$ such that swapping the projection onto $S$ transfers a high-level causal variable. The mechanism under the [subspace view](/mechanistic-views/views/subspace/).

<span id="surgical-intervention"></span>**Surgical intervention.** An intervention that changes one causal variable without directly altering others. Required for interventionist causal claims. IIA is the empirical test.

<span id="dark-matter-ratio"></span>**Dark matter ratio.** (Full model logit difference) / (circuit logit difference). Ratio 1.0 means the circuit fully explains the model's behavior. Above 1.0 means incomplete coverage — which may reflect missing components or genuinely distributed computation.

<span id="agop"></span>**AGOP (Average Gradient Outer Product).** A training-time sensitivity measure (Radhakrishnan et al., 2024). AGOP trajectories sometimes converge to the eventual DAS causal subspace before behavioral detection. Evidence for the [process view](/mechanistic-views/views/process/).

<span id="multi-domain-triangulation"></span>**Multi-domain triangulation.** Convergent evidence across structurally different domains (weight-space, activation-space, dynamics-space). Each domain alone is non-injective on mechanism space — two distinct mechanisms can look identical in one domain. See [Methods](/mechanistic-views/methods/#cross-cutting-observations).

<span id="qua-problem"></span>**Qua-problem.** Identity claims are well-formed only relative to a description level. "Head 9.9 is the same mechanism as head 7.3" is meaningful only given a specified identity criterion — component overlap, role equivalence, or gauge-orbit membership give different answers.

## Methods

<span id="activation-patching"></span>**Activation patching.** Replacing a component's activations from one forward pass into another to test causal relevance. See [activation patching on learnmechinterp](https://learnmechinterp.com/topics/activation-patching/) and the [object view](/mechanistic-views/views/object/).

<span id="path-patching"></span>**Path patching.** Variant of activation patching that tests specific information-flow paths. See [path patching on learnmechinterp](https://learnmechinterp.com/topics/activation-patching/#path-patching).

<span id="attribution-patching"></span>**Attribution patching (EAP, ACDC).** Gradient-based approximations to activation patching that scale to full circuits. Edge attribution patching (EAP) estimates each edge's causal contribution; ACDC uses iterative patching to prune a circuit graph. See [attribution patching on learnmechinterp](https://learnmechinterp.com/topics/attribution-patching/).

<span id="ablation"></span>**Ablation.** Removing or zeroing a component (head, neuron, direction) to test necessity. A component is necessary if ablation degrades performance on the target task. See [activation patching on learnmechinterp](https://learnmechinterp.com/topics/activation-patching/).

<span id="causal-abstraction"></span>**Causal abstraction.** A framework for testing whether a high-level causal model is faithfully implemented by a neural network. [DAS](#das) and [IIA](#iia) are the primary tools; [causal scrubbing](#causal-scrubbing) extends this to full computational graphs. See [causal abstraction on learnmechinterp](https://learnmechinterp.com/topics/causal-abstraction/).

<span id="causal-scrubbing"></span>**Causal scrubbing.** A method that tests whether a proposed computational graph fully accounts for a model's behavior by resampling all activations not explained by the graph. See [causal abstraction on learnmechinterp](https://learnmechinterp.com/topics/causal-abstraction/).

<span id="sae"></span>**SAE (Sparse Autoencoder).** Learns an overcomplete [dictionary](/mechanistic-views/formalism/dictionary/) of directions from a model's activations. Each direction is a candidate $\mathrm{Gr}(1, d)$ mechanism. The sparsity criterion is reconstruction-based, not causal — causal validation (steering, ablation) is needed to establish that a direction is a mechanism. See [sparse autoencoders on learnmechinterp](https://learnmechinterp.com/topics/sparse-autoencoders/) and the [SAE channels discussion](/mechanistic-views/views/subspace/#sae-channels-and-the-subspace-view) on the subspace view page.

<span id="linear-probing"></span>**Linear probing.** Trains a [linear classifier](/mechanistic-views/formalism/linear-classifier/) on intermediate activations to test whether a concept is linearly represented. Observational, not causal. See [probing classifiers on learnmechinterp](https://learnmechinterp.com/topics/probing-classifiers/).

<span id="logit-lens"></span>**Logit lens / tuned lens.** Applies the unembedding matrix (or a learned affine transform) at intermediate layers to read off vocabulary-level predictions. Observational layer-by-layer readout. See [logit lens on learnmechinterp](https://learnmechinterp.com/topics/logit-lens-and-tuned-lens/) and the [linear projection formalism](/mechanistic-views/formalism/linear-projection/).

## Worked examples

<span id="induction-heads"></span>**Induction heads.** Attention heads that implement a copy-and-complete pattern: given a repeated bigram $[A][B] \ldots [A]$, the head attends from the second $[A]$ back to $[B]$ and copies $[B]$ to the output. The strongest mechanistic claim in the current literature — the only one reaching Triangulated under Mechanistic Validity. See [induction heads on learnmechinterp](https://learnmechinterp.com/topics/induction-heads/) and the [Induction Heads case study](/mechanistic-views/cases/induction/).

<span id="ioi-circuit"></span>**IOI circuit.** The circuit for indirect object identification in GPT-2 Small, involving name mover, backup name mover, inhibition, S-inhibition, duplicate token, and previous token heads. The most-studied circuit in mechanistic interpretability. See [IOI circuit on learnmechinterp](https://learnmechinterp.com/topics/ioi-circuit/) and the [IOI case study](/mechanistic-views/cases/ioi/).

## Philosophical foundations

<span id="mechanisms-in-science"></span>**Mechanisms in science.** The philosophical literature on what constitutes a mechanism — from Machamer, Darden & Craver's "entities and activities" to the new mechanist philosophy. The nine mechanistic views in this framework draw on and extend these distinctions for the specific conditions of neural network interpretability. See the [Stanford Encyclopedia of Philosophy entry on mechanisms in science](https://plato.stanford.edu/entries/science-mechanisms/).

<span id="bayesian-epistemology"></span>**Bayesian epistemology.** The use of probability theory as a normative framework for belief revision. Relevant to [cross-view promotion](/mechanistic-views/framework/cross-view-promotion/), where convergent evidence from multiple views can be formalized as Bayesian updating over view-dependent likelihoods. See the [Stanford Encyclopedia of Philosophy entry on Bayesian epistemology](https://plato.stanford.edu/entries/epistemology-bayesian/).

## Additional terms

<span id="alignment-class-vacuity"></span>**Alignment class vacuity (Sutter et al. 2025).** Unrestricted nonlinear alignment maps achieve 100% IIA even on randomly initialized models, making DAS vacuous without structural constraints on the alignment class. Subspace-view claims therefore require either linear alignment or alignment constrained to respect the transport structure induced by the weight matrices. Without this constraint, high IIA is consistent with any causal structure. See the [Subspace view](/mechanistic-views/views/subspace/) and [Grassmannian formalism](/mechanistic-views/formalism/grassmannian/).

<span id="formation-criterion"></span>**Formation criterion.** The threshold or condition used to declare that a mechanism has "formed" during training. Different criteria (behavioral threshold, AGOP convergence, weight-space structure) can disagree in timing. Process-view claims must specify which criterion is used. See [Process view](/mechanistic-views/views/process/).

<span id="g-scm"></span>**G-SCM (Grassmannian Structural Causal Model).** A proposed extension of Pearl's SCM with subspaces as nodes and weight-induced transport maps as edges. Requiring alignment maps to respect transport structure is expected to address vacuity concerns (Sutter et al. 2025). See the [Grassmannian formalism](/mechanistic-views/formalism/grassmannian/).

<span id="gauge-invariant"></span>**Gauge-invariant.** A property that depends only on the gauge orbit $[\theta] \in \mathcal{W}/\mathcal{G}$, not on any particular weight configuration within it. Examples: singular values of $W^{OV}$, principal angles, effective rank. See the [structural view](/mechanistic-views/views/structural/) and [fiber bundle quotient](/mechanistic-views/formalism/fiber-bundle-quotient/).

<span id="principal-angles"></span>**Principal angles.** The angles $\theta_1, \ldots, \theta_k$ between two subspaces $S_1, S_2 \in \mathrm{Gr}(k, d)$, computed as $\cos\theta_i = \sigma_i(Q_1^\top Q_2)$. Used to define geodesic distance on the Grassmannian. See the [Grassmannian deep dive](/mechanistic-views/formalism/deep-dives/grassmannian/).

<span id="frechet-variance"></span>**Fréchet variance.** $\sigma^2_F = \frac{1}{n}\sum_i d(\bar{S}, S_i)^2$ — measures how stable a recovered subspace is across seeds or prompt distributions. Low Fréchet variance means the subspace is a reliable measurement; high variance means it may be an artifact. See [Grassmannian formalism](/mechanistic-views/formalism/grassmannian/#subspace-stability).
