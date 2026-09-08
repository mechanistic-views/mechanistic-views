---
title: Using the Framework
---

# Using the Framework

The primary practical implication of the views framework is that mechanistic interpretability claims should state the view under which they are made. This page covers the view declaration template, common coherence violations, the realism criterion, and view selection heuristics.

## View declaration template

We propose a five-line *view declaration* that a paper would include in its methods section:

> **View declaration.**
> *Ontology*: [what kind of entity counts as a mechanism].
> *Identity*: [when two descriptions refer to the same mechanism].
> *Evidence*: [what measurements support the claim].
> *Formalism*: [what mathematical language is used].
> *Target*: [what phenomenon is being explained].

For example, the IOI circuit paper (Wang et al., 2023) would declare:

> **View declaration.**
> *Ontology*: concrete attention heads ([Object view](/mechanistic-views/views/object/)).
> *Identity*: component overlap within GPT-2 Small.
> *Evidence*: activation patching, path patching, mean ablation.
> *Formalism*: directed graph over 26 heads.
> *Target*: indirect object identification on the IOI distribution.

The declaration is a precision requirement of the same kind as reporting which distribution patching was run on. Stating the view makes evidence-claim mismatches immediately visible: if a paper declares Object ontology but draws Role conclusions ("head 9.9 is a name mover"), the gap between the declared evidence and the stated claim becomes a checkable coherence condition rather than an unstated assumption.

## Common coherence violations

Five phrasings in common use whose evidence and claim sit under different views:

| What gets written | Evidence reaches | Claim asserts | What it needs |
|---|---|---|---|
| "Head X is a name mover" (from ablation) | a component set ([object](/mechanistic-views/views/object/)) | a functional role ([role](/mechanistic-views/views/role/)) | a role specification independent of the procedure that found it |
| "This direction *is* refusal" (from a steering result) | predictive control ([instrumental](/mechanistic-views/views/instrumental/)) | a constituent of the model ([subspace](/mechanistic-views/views/subspace/)) | which of the two is claimed; predictive equivalence reaches the first alone |
| "The deception feature" | a direction separating two prompt sets ([contrastive](/mechanistic-views/views/contrastive/)) | a property of the model ([object](/mechanistic-views/views/object/)) | which two sets it separates, since the feature is defined by that pairing |
| "The same mechanism, in a second model" (from whole-residual patching) | an ordering of information flow ([process](/mechanistic-views/views/process/)) | a decomposition into parts ([subspace](/mechanistic-views/views/subspace/)) | which reading is meant; replacing the whole residual cannot separate parts within it |
| "We localized it to head 9.9" (offered as the explanation) | component identity ([object](/mechanistic-views/views/object/)) | an explanation | what the component does; the object view supplies which components, and a role supplies what they do |

Each is closed by a declaration rather than by a further experiment.

## Independent convergence

Three independent starting points converge on the same diagnosis:

**Philosophy of science.** Williams et al. (2025) argue that mechanistic interpretability needs philosophical foundations for clarifying concepts, refining methods, and navigating epistemic complexity. Their three central examples map directly onto view-level analyses: "the assumption of the One True Decomposition" corresponds to the [object](/mechanistic-views/views/object/)–[subspace](/mechanistic-views/views/subspace/) distinction; their vehicle–content distinction — the internal direction, and the external condition it encodes — separates the ontology and target axes; and their question of detecting deceptive behavior corresponds to the [instrumental view's](/mechanistic-views/views/instrumental/) ceiling.

**Field methodology.** Bereska & Saphra (2024) survey mechanistic interpretability for safety and close on two field-level failures: *cherry-picking* (a small number of convincing visualizations standing in for comprehensive evaluation) and *streetlight interpretability* (techniques validated on toy models under conditions of maximal interpretability). Their proposed remedy — coordinate observational and interventional methods — is a call for cross-view evidence: probing and activation patching carry different ontologies, so a result surviving both has cleared two sets of assumptions.

**This framework.** The three arrivals disagree about vocabulary and agree about the diagnosis: probing and activation patching carry different ontologies, so what an agreement between them is worth is a question about the assumptions each clears. What this framework supplies is the account of why the two methods differ in the first place.

## Realism criterion

The realist question is local: whether a reported structure belongs to the trained model or is introduced by the procedure that measured it. The [view families](/mechanistic-views/views/assessment/) give a test for it.

A method cannot rule out its own characteristic artifact; only a method that fails differently can. Agreement is therefore evidence of reality when it holds across views whose failure modes are unrelated, and evidence of nothing when the agreeing views share one.

Treat a mechanism as:
- **View-invariant** when its support crosses at least two families and no applied view yields an undefeated incompatible result
- **Contested** when applied views return incompatible results that no difference in grain or identity criterion reconciles
- **Candidate** otherwise — a candidate being a structure no second family has yet examined rather than one shown to vary

Two is the minimum the argument requires rather than a tuned threshold. Within one family a single characteristic artifact could produce the whole agreement; two families is the smallest number at which no one method's artifact explains both results.

## View selection heuristic

The framework is pluralist, but a researcher facing a concrete question needs guidance on which view to adopt. The following heuristic matches the scope of the claim to the minimum view that can support it:

| If the claim is about... | Minimum view |
|---|---|
| A specific model on a specific distribution | [Object](/mechanistic-views/views/object/) |
| Generalization across models ("Pythia and GPT-2 both have this mechanism") | [Role](/mechanistic-views/views/role/) — component indices are trivially not cross-model |
| A distributed representation not localized to a single component | [Subspace](/mechanistic-views/views/subspace/) |
| Surviving reparameterization (permutation, rescaling, rotation) | [Structural](/mechanistic-views/views/structural/) |
| How the mechanism formed or why it appeared at a specific training step | [Process](/mechanistic-views/views/process/) — no amount of final-checkpoint evidence can substitute |
| A mechanism whose apparent type changes with measurement resolution | [Stratified](/mechanistic-views/views/stratified/) |

The heuristic is conservative: it recommends the lowest-commitment view that matches the claim's scope. Higher-commitment views are always available but require correspondingly stronger evidence.

## Descriptive and generative views

The [object](/mechanistic-views/views/object/) and [role](/mechanistic-views/views/role/) views primarily organize existing empirical practice. The [subspace](/mechanistic-views/views/subspace/), [structural](/mechanistic-views/views/structural/), and [stratified](/mechanistic-views/views/stratified/) views generate positive research programs: each calls for methods, results, and formalism that do not yet exist.

- **Subspace view**: systematic DAS studies with stability tests across models and distributions. The formalism is already in use — Grassmannian principal angles between subspaces — but DAS-recovered causal subspaces have not been compared this way.
- **Structural view**: gauge-invariance checks and geometric formalism. Holonomy on context complexes supplies the structural view a method independently of this framework.
- **Stratified view**: dimensionality diagnostics and stratum-transition tests.

The atlas therefore also maps what is missing.
