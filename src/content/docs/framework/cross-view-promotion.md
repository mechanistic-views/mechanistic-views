---
title: Cross-View Promotion
---

# Cross-View Promotion

A common question: under what conditions can a result at one view be promoted to a higher-commitment view? Each promotion requires new evidence of the kind specified by the target view. Evidence from the source view does not accumulate toward the target view's standard — it answers a different question.

## Promotion conditions

**[Object](/mechanistic-views/views/object/) → [Role](/mechanistic-views/views/role/).** The component must be tested with an independently operationalized role specification on held-out constructions. If the role predicts behavior beyond the original discovery distribution, the result can be stated as a role claim.

**[Role](/mechanistic-views/views/role/) → [Subspace](/mechanistic-views/views/subspace/).** The functional role must be shown to be mediated by a specific low-dimensional subspace (e.g., via linear DAS with alignment constraints), and this subspace must be stable across prompt distributions with small geodesic distance on Gr(k,d).

**[Subspace](/mechanistic-views/views/subspace/) → [Structural](/mechanistic-views/views/structural/).** The subspace must survive computation-preserving symmetries of the weight space. If the subspace recovered by DAS changes under a reparameterization that does not change the model's computation, the subspace claim is not structural. Holonomy measurements provide a gauge-invariant fingerprint.

**Any → [Process](/mechanistic-views/views/process/).** The static claim must be supplemented with training-dynamics evidence: checkpoint analysis showing when and how the mechanism formed, formation knockouts, or loss-curve structure. No amount of final-checkpoint evidence can substitute.

The chain is not sequential: promotion can skip levels when the evidence supports it. For example, an Object-level result can promote directly to Subspace if linear DAS identifies a causal subspace spanning the relevant components, without requiring an intermediate Role specification. The subspace evidence subsumes the object evidence (the components are where the subspace has support) but does not require role-level mediation.

## Connections to neighboring fields

The five-axis framework has natural translations into several disciplines whose concepts it draws on.

**Philosophy of science.** The ontology axis corresponds to the central question of the [new mechanist](/mechanistic-views/glossary/#mechanisms-in-science) literature: what counts as a mechanism? The identity axis operationalizes Lewis's account of functional identification: when do a role description and a component description pick out the same thing? The evidence axis inherits the eliminativist structure of Earman's [Bayesian epistemology](/mechanistic-views/glossary/#bayesian-epistemology): independent evidence types eliminate distinct confounders.

**Physics.** The [structural view's](/mechanistic-views/views/structural/) gauge-invariance requirement is the direct analogue of gauge symmetry in field theory: two weight configurations related by a computation-preserving transformation are the same mechanism, just as two vector potentials related by a gauge transformation describe the same electromagnetic field. The [stratified view](/mechanistic-views/views/stratified/) borrows the renormalization group's central insight: effective descriptions change with measurement scale, and the interesting objects are the fixed points and relevant operators.

**Mathematics.** Grassmannian geometry makes subspace proximity a metric statement; fiber bundles make gauge invariance a theorem rather than a heuristic check; Whitney stratification gives a rigorous account of how mechanism identity changes across strata boundaries. Each formalism carries proof obligations that the corresponding informal claim does not.

**Cognitive science and neuroscience.** The localization–distribution spectrum (object view through stratified view) mirrors the debate between localizationism and distributed coding in systems neuroscience. The double dissociation methodology in neuropsychology is the nearest analogue to the necessity and sufficiency tests used in the object view.
