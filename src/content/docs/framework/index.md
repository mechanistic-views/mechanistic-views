---
title: Framework
---

# Framework

Every mechanistic interpretability result assumes a view of what mechanisms are. The claim "head 4.4 is a name-mover" assumes mechanisms can be identified with heads. The claim "a causal subspace at layer 8 stores the indirect object" assumes mechanisms can be subspaces. The claim "the grokking circuit forms by epoch 30K" assumes mechanisms are processes with formation timelines.

These assumptions are usually tacit. This site makes them explicit.

## The five axes

A mechanistic view must answer five questions. The questions fall into distinct categories, which matter for how the answers relate to each other.

**Metaphysical axes** — what the mechanism is and when two are the same:

**Ontology.** What kind of thing is a mechanism? Options include: a concrete component (head, neuron, feature), a functional role that can be multiply realized, a causal subspace in residual stream geometry, an invariant relational structure, a temporally extended process, or a combination of these at multiple strata.

**Identity.** When are two mechanism descriptions referring to the same mechanism? This matters for cross-model comparison, for deciding when two competing circuit papers are contradicting each other versus measuring different things, and for tracking a mechanism across training checkpoints. The identity criterion must fit the ontology: the right criterion for a role (functional equivalence) differs from the right criterion for a subspace (geodesic distance on a Grassmannian).

**Epistemological axis** — what justifies the claim:

**Evidence.** What measurements would warrant a mechanism claim of this type? Different ontologies license different evidence. A component claim is most directly supported by ablation and patching. A subspace claim needs subspace recovery and causal tests that jointly converge. A structural claim needs measurements robust to reparameterization. Evidence and ontology are linked: an evidence type that does not track the claimed kind of object cannot confirm the claim.

Three models of evidence are in play in the literature, corresponding to different epistemological traditions:

- **Hypothetico-deductive (HD)**: a mechanistic hypothesis is supported when its predictions are confirmed. Activation patching is used HD-style when a researcher predicts "ablating head 4.4 should reduce accuracy on IOI" and observes the reduction.
- **Bayesian**: evidence updates the probability of a mechanism hypothesis. This is the implicit model behind most "evidence accumulation" discourse: multiple independent tests move credence up. The triangulation requirement reflects the Bayesian insight that *independent* evidence is worth more than correlated evidence.
- **Eliminative/triangulation**: evidence from structurally different domains eliminates distinct alternative hypotheses. A weight-space result rules out one class of confounders; an activation-space result rules out a different class; convergence establishes what survives both eliminations.

The tier system in this site is most naturally read as tracking eliminative strength: Tier 1 is how-possibly (HD confirmation only), Tier 3–4 is how-actually (eliminative convergence across domains).

**Representational axis** — how the claim is expressed:

**Formalism.** What mathematical language is used to represent the mechanism? A circuit diagram, a point on a Grassmannian, and a cosheaf cohomology class are different representational choices. The choice of formalism determines what can be stated precisely and what can be proved. Formalism is not itself a stance on what exists — two researchers can hold the same ontological view and express it in different formalisms — but the formalism constrains what the ontological view can commit to.

**Scope axis** — what the claim is about:

**Target.** What phenomenon is the mechanism supposed to explain? A mechanism of indirect object identification, of in-context learning, of grokking, and of factual recall carry different target-level commitments. The target determines the level of description at which the explanation must be pitched (corresponding to what Craver calls "constitutive relevance" in the philosophical literature on mechanistic explanation), and therefore which evidence types are relevant and what counts as explanatory success.

## A note on "mechanism"

The word "mechanism" is used here in the sense established in the interpretability literature: a computational structure inside a neural network responsible for a specific behavior.

In the philosophy of science, "mechanism" carries more structure. The influential Machamer-Darden-Craver (MDC) account defines mechanisms as entities and activities organized to produce a phenomenon: they have a specific start condition, end condition, spatial and organizational layout, and temporal order (Machamer, Darden, and Craver, *Thinking About Mechanisms*, Philosophy of Science 67(1), 2000). Craver further distinguishes *how-possibly* models (a mechanism that could produce the phenomenon) from *how-actually* models (a mechanism that does produce it), with evidence requirements increasing accordingly. This distinction maps onto the tier system used in this site: Tier 1 claims are how-possibly; Tier 3–4 claims are how-actually.

The interpretability sense diverges from MDC in two ways. First, it makes no commitment to spatial structure — neural network mechanisms are not organized in physical space. Second, the emphasis on interventionism (see [Subspace view](views/subspace/)) aligns more with Woodward's manipulationist account of causation (*Making Things Happen*, Oxford, 2003): a causal variable is identified by what happens when it is surgically manipulated, not by its role in an organized spatial structure.

A further concept from philosophy of science that appears in this site is *constitutive relevance* (Craver, *Explaining the Brain*, Oxford, 2007): a component is constitutively relevant to a phenomenon if it is part of the mechanism producing it, as established by mutual manipulability — intervening on the component affects the phenomenon and vice versa. This is the criterion measured by activation patching and ablation, which is why those methods appear under the object and role views. When this distinction between MDC mechanisms and interpretability mechanisms matters, the text says so explicitly.

## What a view is

A view is a bundle of answers to the five axes. Formally, a mechanistic stance is a 5-tuple:

$$\sigma = (O, I, E, F, T)$$

where $O$ is the ontological type, $I$ is an identity criterion defined on objects of type $O$, $E$ is the evidence type, $F$ is the formalism, and $T$ is the target phenomenon.

**Well-formedness conditions.** A stance $\sigma$ is *coherent* if and only if:
1. $I$ is well-defined on objects of type $O$ — the identity criterion can be applied to the claimed ontological entities.
2. $E$ produces measurements that track $I$ — the evidence type is sensitive to the property that $I$ uses to distinguish mechanisms.
3. $F$ can express claims of type $(O, I)$ — the formalism has the expressive power to represent the object and state the identity criterion.

Incoherence arises when these conditions fail. Example: claiming $O =$ component but $I =$ geodesic distance on $\mathrm{Gr}(k,d)$ violates condition (1), because geodesic distance requires subspace objects, not component objects. Example: citing activation patching as $E$ for a gauge-orbit identity claim $I$ violates condition (2), because activation patching is head-index-dependent and therefore not sensitive to gauge-orbit membership. The bundle should be *coherent*: the identity criterion should be appropriate for the ontology, the evidence should be sufficient to establish the identity, the formalism should be able to express the claim, and the target should determine which aspects of the other axes are relevant.

**What incoherence looks like.** A view is incoherent when its axes make incompatible demands. Example: claiming the object view ontology (mechanism = specific component) but using subspace identity (geodesic distance on $\mathrm{Gr}(k,d)$) — the identity criterion requires a subspace, but the ontology has no subspace to measure distance between. Another example: using the structural view identity criterion (same gauge orbit) while citing only activation patching as evidence — activation patching is gauge-covariant (head index-dependent), so it cannot establish gauge-orbit identity. A coherent view has evidence that tracks the identity criterion that tracks the ontology.

Write a stance as:

$$\sigma = (O, I, E, F, T)$$

For example, the subspace view bundles:
- $O$: mechanism as causal subspace
- $I$: geodesic distance on $\mathrm{Gr}(k, d)$
- $E$: convergence of DAS-recovered and SVD-weight subspaces across seeds and architectures
- $F$: Grassmannian geometry, transport maps, G-SCM
- $T$: causal variables (e.g., the indirect object token in IOI)

## Axes versus views

The axes are questions. The views are answers.

1. The same axis can take different values in different views.
2. A view changes multiple axes at once in a coherent way. Switching from the object view to the subspace view is not just changing the ontology; it changes the identity criterion, the evidence standard, and the appropriate formalism together.
3. Axes can be used as an audit tool. For any paper making a mechanistic claim, you can ask: which axis values is this paper assuming? Are those assumptions consistent? Are they stated?

## Mixing axes

The eight named views represent coherent combinations of axis values. But there is no requirement to adopt a named view wholesale — you can take the subspace ontology with the structural identity criterion, or the object ontology with process-view evidence standards. Such combinations are valid as long as they remain coherent.

The coherence check: does the identity criterion fit the ontology? Does the evidence track the identity criterion? If you use a subspace ontology but need to compare mechanisms across models, you need an identity criterion that works for subspaces — geodesic distance or gauge-orbit membership, not component overlap. Mixing is fine; incoherence is not.

In practice, most interpretability papers mix axes implicitly. The axis framework makes the mixing explicit so it can be evaluated.

## Why this helps

Disagreements in mechanistic interpretability are often view-level disagreements. Two researchers looking at the same activation-patching result may disagree about what it shows, not because of different data, but because they hold different background views about what mechanism the data is evidence for.

Making the view explicit does not automatically resolve the disagreement. But it locates the disagreement precisely, which makes it possible to design experiments that distinguish between views.

## Underdetermination and the need for triangulation

A persistent epistemological problem in mechanistic interpretability is **underdetermination**: multiple distinct mechanism hypotheses can be consistent with the same evidence. An activation-patching result that shows head 4.4 is necessary is consistent with (a) head 4.4 being the mechanism, (b) head 4.4 being one realizer of a role-level mechanism, (c) head 4.4 participating in a distributed mechanism whose activity happens to be concentrated there, and (d) head 4.4 being a measurement artifact of the patching protocol. These are not equivalent claims under different descriptions; they support different predictions and require different interventions.

The triangulation requirement in this site — requiring convergent evidence across weight-space, activation-space, and dynamics-space domains — is a response to underdetermination. The single-domain evidence produces an underdetermined verdict; multi-domain convergence narrows the hypothesis space. This is a pragmatic application of the epistemological principle that *independent* evidence is stronger than repeated evidence from the same source. See [Single-method vs triangulated](decisions/single-vs-triangulated/).

## The realism spectrum

The eight views span a realism-to-instrumentalism spectrum. Understanding where each view falls matters for how strongly its conclusions can be stated.

**Realist views** hold that mechanisms are real objects independent of how we measure them. The structural view is the most strongly realist: a mechanism is the gauge orbit of weight configurations computing the same function, which exists independent of any particular measurement procedure.

**Perspectival views** hold that mechanism descriptions are always relative to a measurement procedure. What exists is the procedure and its outputs; whether there is a view-independent mechanism is bracketed. This position has precedent in the philosophy of science literature on perspectivalism (cf. Massimi, *Perspectival Realism*, Oxford, 2022), which holds that scientific representations are perspectival without being merely subjective.

**Instrumentalist views** hold that "mechanism" is useful shorthand for a predictive/interventional model. The instrumental view here is the limiting case of this position.

The subspace, role, process, and object views sit between full realism and perspectivalism. Choosing a view is implicitly a commitment about how realist one's conclusions are entitled to be.

## The qua-problem

The *qua-problem* (originally in philosophy of mathematics) arises whenever an entity can be described under multiple predicates: head 4.4 is "the same mechanism" as head 7.2 in another model *qua what?* Under the component description they are different; under the role description they may be the same; under the gauge-orbit description they may be the same if the orbits are isomorphic.

Every mechanistic identity claim is implicitly a *qua*-claim. The five axes force that implicit claim to be stated explicitly: identity *qua* gauge orbit (structural view), *qua* role (role view), *qua* geodesic proximity (subspace view), *qua* formation process (process view). There is no view-independent answer to "are these the same mechanism?" — only answers relative to a specified identity criterion.
