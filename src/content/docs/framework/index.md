---
title: Framework
---

# Framework

Every mechanistic interpretability result assumes a view of what mechanisms are. The claim "head 4.4 is a name-mover" assumes mechanisms can be identified with heads. The claim "a causal subspace at layer 8 stores the indirect object" assumes mechanisms can be subspaces. The claim "the grokking circuit forms by epoch 30K" assumes mechanisms are processes with formation timelines.

These assumptions are usually tacit; this site makes them explicit.

## The five axes

![Five axes of a mechanistic view](/mechanistic-views/figures/five-axes-pipeline-clean.svg)

A mechanistic view must answer five questions. The questions fall into distinct categories, which matter for how the answers relate to each other.

**Definitional axes** — what the mechanism is and when two are the same:

1. **Ontology.** What kind of thing is a mechanism? Options include: a concrete component (head, neuron, feature), a functional role that can be multiply realized ([Putnam 1967](https://doi.org/10.1017/CBO9780511625268.023)), a causal subspace in residual stream geometry, an invariant relational structure, a temporally extended process, or a combination of these at multiple strata. The concept of mechanism ontology in science follows [Machamer, Darden & Craver (2000)](https://doi.org/10.1086/392759).

2. **Identity.** When are two mechanism descriptions referring to the same mechanism? This is a form of the classical identity problem in ontology ([Quine 1948](https://doi.org/10.2307/2181613)): no entity without identity criteria. This matters for cross-model comparison, for deciding when two competing circuit papers are contradicting each other versus measuring different things, and for tracking a mechanism across training checkpoints. The identity criterion must fit the ontology: the right criterion for a role (functional equivalence) differs from the right criterion for a subspace (geodesic distance on a Grassmannian). When two weight configurations compute the same function, the identity question becomes one of gauge equivalence ([Earman 2004](https://doi.org/10.1016/j.shpsb.2003.02.001)).

**Evidential axis** — what justifies the claim:

3. **Evidence.** What measurements would warrant a mechanism claim of this type? Different ontologies license different evidence. A component claim is most directly supported by ablation and patching. A subspace claim needs subspace recovery and causal tests that jointly converge. A structural claim needs measurements robust to reparameterization. Evidence and ontology are linked: an evidence type that does not track the claimed kind of object cannot confirm the claim.

   Three models of evidence are in play in the literature, corresponding to different epistemological traditions:

   - **Hypothetico-deductive (HD)**: a mechanistic hypothesis is supported when its predictions are confirmed ([Popper 1959](https://doi.org/10.4324/9780203994627); Hempel 1966). Activation patching is used HD-style when a researcher predicts "ablating head 4.4 should reduce accuracy on IOI" and observes the reduction.
   - **Bayesian**: evidence updates the probability of a mechanism hypothesis (Howson & Urbach 2006). This is the implicit model behind most "evidence accumulation" discourse: multiple independent tests move credence up. The triangulation requirement reflects the Bayesian insight that *independent* evidence is worth more than correlated evidence.
   - **Eliminative/triangulation**: evidence from structurally different domains eliminates distinct alternative hypotheses ([Campbell & Fiske 1959](https://doi.org/10.1037/h0046016); [Woodward 2003](https://doi.org/10.1093/0195155270.001.0001)). A weight-space result rules out one class of confounders; an activation-space result rules out a different class; convergence establishes what survives both eliminations.

   The tier system in this site is most naturally read as tracking eliminative strength: Tier 1 is how-possibly (HD confirmation only), Tier 3–4 is how-actually (eliminative convergence across domains).

**Representational axis** — how the claim is expressed:

4. **Formalism.** What mathematical language is used to represent the mechanism? A circuit diagram, a point on a Grassmannian, and a cosheaf cohomology class are different representational choices. The choice of formalism determines what can be stated precisely and what can be proved. Formalism is not itself a stance on what exists — two researchers can hold the same ontological view and express it in different formalisms — but the formalism constrains what the ontological view can commit to.

**Scope axis** — what the claim is about:

5. **Target.** What phenomenon is the mechanism supposed to explain? A mechanism of indirect object identification, of in-context learning, of grokking, and of factual recall carry different target-level commitments. The target determines the level of description at which the explanation must be pitched (corresponding to what Craver calls "constitutive relevance" in the philosophical literature on mechanistic explanation), and therefore which evidence types are relevant and what counts as explanatory success.

## The determination chain

The five answers are not independent. What a mechanism is determines when two are the same, which determines what formalism is needed:

$$\text{Ontology} \;\longrightarrow\; \text{Identity} \;\longrightarrow\; \text{Formalism}$$

Under the object view, mechanisms are specific components, identity is component overlap, and the formalism is a directed graph. Under the role view, mechanisms are functional roles, identity is role equivalence, and the formalism is a role graph. Possible mismatches arise between these three axes: using subspace math while holding a component-overlap notion of identity, or using patching evidence (object-level) to support a structural-level claim. These mismatches are a common source of incoherence in practice.

## What a view is

A view is a bundle of answers to the five axes. Formally, a mechanistic view is a 5-tuple:

$$\sigma = (O, {\sim}, E, F, T)$$

where $O$ is the ontological type (the set of entities that count as mechanisms), ${\sim} \subseteq O \times O$ is an equivalence relation (the identity criterion: $x \sim y$ means descriptions $x$ and $y$ refer to the same mechanism), $E$ is a set of evidential standards, $F$ is the formalism, and $T$ is the target phenomenon.

**Coherence conditions.** A view $\sigma$ is *coherent* if and only if:
1. **Identity is grounded**: ${\sim}$ is definable using only the objects in $O$ and the language of $F$. A view whose identity criterion involves objects not in its own ontology is incoherent.
2. **Evidence tracks identity**: for every measurement type $m \in E$, the claims $m$ can support are expressible in terms of ${\sim}$-classes, not finer-grained distinctions. Evidence that distinguishes objects within a ${\sim}$-class is picking up on a different ontology than the one declared.
3. **Formalism is expressive**: every element of $O$ has a representation in $F$, and ${\sim}$ is computable in $F$.

**Incoherent views produce contradictory demands.** If a view violates condition (2) — there exists a measurement $m \in E$ and objects $x, y \in O$ with $x \sim y$ but $m(x) \neq m(y)$ — then the view simultaneously asserts that $x$ and $y$ are the same mechanism (by ${\sim}$) and that they are different (by $m$). No experiment can satisfy both demands. This is immediate from the definitions.

A stronger consequence: incoherent views produce *systematic underdetermination*. Each new measurement either agrees with the identity criterion (offering no information about the discrepancy) or disagrees (introducing its own underdetermination). This is why debates between activation-patching advocates and DAS advocates cannot be settled by more of the same evidence when the participants hold different implicit views.

**Examples.** Claiming $O =$ component but ${\sim} =$ geodesic distance on $\mathrm{Gr}(k,d)$ violates condition (1): geodesic distance requires subspace objects, not component objects. Citing activation patching as $E$ for a gauge-orbit identity claim violates condition (2): activation patching is head-index-dependent and therefore not sensitive to gauge-orbit membership.

The subspace view bundles:
- $O$: mechanism as causal subspace
- ${\sim}$: same projector, or geodesic distance on $\mathrm{Gr}(k, d)$ below threshold
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

## Why this matters

Disagreements in mechanistic interpretability are often view-level disagreements. Two researchers looking at the same activation-patching result may disagree about what it shows, not because of different data, but because they hold different background views about what mechanism the data is evidence for.

Making the view explicit does not automatically resolve the disagreement. But it locates the disagreement precisely, which makes it possible to design experiments that distinguish between views.

A persistent problem is **underdetermination**: multiple distinct mechanism hypotheses can be consistent with the same evidence. An activation-patching result that shows head 4.4 is necessary is consistent with (a) head 4.4 being the mechanism, (b) head 4.4 being one realizer of a role-level mechanism, (c) head 4.4 participating in a distributed mechanism whose activity happens to be concentrated there, and (d) head 4.4 being a measurement artifact of the patching protocol. These are not equivalent claims under different descriptions; they support different predictions and require different interventions.

The triangulation requirement in this site — requiring convergent evidence across weight-space, activation-space, and dynamics-space domains — is a response to underdetermination. The single-domain evidence produces an underdetermined verdict; multi-domain convergence narrows the hypothesis space. This is a pragmatic application of the principle that *independent* evidence is stronger than repeated evidence from the same source.

**Cross-model comparison.** The claim that two models implement "the same" mechanism requires a notion of identity that works across models. Component indices (head 9.9 in model A, head 7.3 in model B) are trivially not cross-model. Functional roles may be comparable, if independently specified. Geometric structure may be, if a canonical mapping is defined. Which notion is assumed determines whether "the same mechanism" is meaningful across architectures.

**Generalization.** Finding a circuit invites a natural question: does its presence guarantee specific behavior on inputs the model has never seen? Under an object view, circuit presence is about specific components on a specific distribution — it says nothing about novel inputs. Under a subspace or higher view, the circuit is defined by structure that is increasingly robust: a subspace is stable under perturbation, a gauge-invariant structure survives reparameterization. The stronger the view, the stronger the generalization claim.

**Post-hoc explanation.** In circuit discovery, components are identified first and functional roles assigned afterward — labels like "name mover" describe observed behavior, not independent predictions. Any observed behavior can be given a plausible role label, making the functional story difficult to falsify. The backup name movers in the IOI circuit ([Wang et al. 2022](https://arxiv.org/abs/2211.00593)) illustrate this: knock out the "name movers" and other heads take on the same role. A role claim becomes falsifiable when the role is predicted from independent evidence — structure, training dynamics, or cross-model transfer — rather than read off the same activations that identified the component.

## Relationship to Marr's levels

Marr's tri-level account — computational, algorithmic, implementational — organizes *explanatory targets*: what a system does, how it does it, what substrate realizes the process. The five axes here organize *ontological commitments*: what kind of object the mechanism is, when two are the same, what evidence can support the claim. These are orthogonal. Two researchers can agree that IOI is an algorithmic-level finding — a procedure involving duplicate token heads, S-inhibition heads, and name movers — and still disagree about two things: what a circuit is as a formal object, and what underlying mechanism the circuit describes.

Is it just a useful predictive model? A projection of the method used to find it? A set of specific components? A role structure that any components could fill? A subspace? A gauge-invariant pattern in the weights? A trajectory that formed during training? A multi-resolution object that changes depending on the scale at which you look?

These are eight different claims about what exists inside the network, each corresponding to a mechanistic view.

## Deeper commitments

**Two senses of "mechanism."** The word "mechanism" is used here in the sense established in the interpretability literature: a computational structure inside a neural network responsible for a specific behavior. In the philosophy of science, "mechanism" carries more structure. The influential Machamer-Darden-Craver (MDC) account defines mechanisms as entities and activities organized to produce a phenomenon, with specific start conditions, end conditions, and temporal order ([Machamer, Darden & Craver 2000](https://doi.org/10.1086/392759)). Craver further distinguishes *how-possibly* models from *how-actually* models, with evidence requirements increasing accordingly — a distinction that maps onto this site's tier system (Tier 1 = how-possibly, Tier 3–4 = how-actually). The interpretability sense diverges from MDC in two ways: no commitment to spatial structure, and an emphasis on Woodward's manipulationist causation ([Woodward 2003](https://doi.org/10.1093/0195155270.001.0001)) over organized spatial layout. A related concept is *constitutive relevance* ([Craver 2007](https://doi.org/10.1093/acprof:oso/9780199299317.001.0001)): a component is constitutively relevant to a phenomenon if mutual manipulability holds — intervening on the component affects the phenomenon and vice versa. This is what activation patching and ablation measure.

**The realism spectrum.** The eight views span a realism-to-instrumentalism spectrum. The structural view is the most strongly realist: a mechanism is the gauge orbit of weight configurations computing the same function, which exists independent of any measurement procedure. Perspectival views hold that mechanism descriptions are always relative to a measurement procedure — what exists is the procedure and its outputs (cf. [Massimi 2022](https://doi.org/10.1093/oso/9780197555620.001.0001)). Instrumentalist views hold that "mechanism" is useful shorthand for a predictive model. The subspace, role, process, and object views sit between full realism and perspectivalism. Choosing a view is implicitly a commitment about how realist one's conclusions are entitled to be.

**The qua-problem.** The *qua-problem* arises whenever an entity can be described under multiple predicates: head 4.4 is "the same mechanism" as head 7.2 in another model *qua what?* Under the component description they are different; under the role description they may be the same; under the gauge-orbit description they may be the same if the orbits are isomorphic. Every mechanistic identity claim is implicitly a *qua*-claim. The five axes force that implicit claim to be stated explicitly: identity *qua* gauge orbit (structural view), *qua* role (role view), *qua* geodesic proximity (subspace view), *qua* formation process (process view). There is no view-independent answer to "are these the same mechanism?" — only answers relative to a specified identity criterion.
