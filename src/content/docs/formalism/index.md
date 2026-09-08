---
title: Formalisms
---

# Formalisms

Formalisms are mathematical languages for expressing mechanistic claims. They are not in a one-to-one relationship with views — a single view can be expressed through multiple competing formalisms, and a single formalism can serve multiple views. The subspace view, for example, can use Grassmannian geometry for linear subspaces or Riemannian geometry for nonlinear manifolds. Whitney stratification serves the stratified view but also describes the internal structure of the Grassmannian itself.

## How formalisms relate

Formalisms build on each other. Gray cards are method-level tools not tied to a single view. Dashed borders mark cross-cutting frameworks drawn on by multiple views.

![Formalism network](/mechanistic-views/figures/formalism-network.svg)

## View-associated formalisms

Each formalism is listed with its primary view association, but most can serve multiple views:

- [Model Theory](model-theory/) — primarily the instrumental view; predictive equivalence
- [Measurement Algebra](measurement-algebra/) — primarily the perspectival view; measurement operations as objects
- [Directed Graph](directed-graph/) — primarily the object view; circuit graphs
- [Functional Decomposition](role-graph/) — primarily the role view; roles and their dependencies, loose by necessity since a role is multiply realizable
- [Grassmannian](grassmannian/) — primarily the subspace view; also used by the structural and stratified views for linear strata
- [Fiber Bundle Quotient](fiber-bundle-quotient/) — primarily the structural view; gauge orbits, holonomy
- [Dynamical System](dynamical-system/) — primarily the process view; training dynamics
- [Resolution-Indexed Strata](stratification/) — primarily the stratified view; Whitney stratification is the mathematical antecedent, and no operational claim depends on its regularity conditions

## Method-level formalisms

These are not tied to a single view but are used by specific interpretability methods:

- [Causal Graph](causal-graph/) — used by causal scrubbing and causal abstraction
- [Linear Classifier](linear-classifier/) — used by linear probing
- [Dictionary](dictionary/) — used by sparse autoencoders (SAEs)
- [Linear Projection](linear-projection/) — used by logit lens and tuned lens

## Cross-cutting formalisms

These mathematical frameworks are drawn on by multiple views:

- [Information Theory](information-theory/) — mutual information, capacity; used by the object, role, and subspace views
- [Category Theory](category-theory/) — functors, natural transformations; used by the role and structural views
- [Representation Theory](representation-theory/) — group representations, equivariance; used by the subspace and structural views

## Deep dives

The Grassmannian, fiber bundle quotient, and Whitney stratification pages have accessible overviews above and full mathematical treatments in the [Deep Dives](deep-dives/) section:

- [Grassmannian Geometry](deep-dives/grassmannian/) — principal angles, transport maps, Fréchet statistics
- [Gauge Quotients and Holonomy](deep-dives/gauge-holonomy/) — fiber bundles, connections, holonomy computation
- [Sheaf Cohomology](deep-dives/sheaves/) — cosheaves on directed graphs, $H^0$ and $H^1$, localizability. A site elaboration: sheaves are attached to no view in the paper
- [Stratification](deep-dives/stratification/) — Whitney conditions, Thom-Mather theory, the $\mathcal{M}_\infty$ stratum

These assume graduate-level mathematics. The overview pages are accessible with linear algebra alone.
