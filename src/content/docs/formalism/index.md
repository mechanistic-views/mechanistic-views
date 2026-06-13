---
title: Formalisms
---

# Formalisms

Each of the eight mechanistic views uses a different mathematical language to express its claims. These pages introduce each formalism: what it is, how the view uses it, and where to learn more.

## How formalisms relate

Formalisms build on each other. Colors match the view each formalism serves; gray cards are method-level tools not tied to a single view. Dashed borders mark cross-cutting frameworks drawn on by multiple views.

![Formalism network](/mechanistic-views/figures/formalism-network.svg)

## Pages

One per view, ordered by increasing ontological commitment:

- [Model Theory](model-theory/) — the instrumental view's formalism
- [Measurement Algebra](measurement-algebra/) — the perspectival view's formalism
- [Directed Graph](directed-graph/) — the object view's formalism
- [Role Graph](role-graph/) — the role view's formalism
- [Grassmannian](grassmannian/) — the subspace view's formalism
- [Fiber Bundle Quotient](fiber-bundle-quotient/) — the structural view's formalism
- [Dynamical System](dynamical-system/) — the process view's formalism
- [Whitney Stratification](stratification/) — the stratified view's formalism

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
- [Sheaf Cohomology](deep-dives/sheaves/) — cosheaves on directed graphs, $H^0$ and $H^1$, localizability
- [Stratification](deep-dives/stratification/) — Whitney conditions, Thom-Mather theory, the $\mathcal{M}_\infty$ stratum

These assume graduate-level mathematics. The overview pages are accessible with linear algebra alone.
