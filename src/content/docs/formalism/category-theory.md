---
title: Category Theory
---

# Category Theory

A cross-cutting formalism primarily used by the [role view](/mechanistic-views/views/role/), with connections to the [structural view](/mechanistic-views/views/structural/).

## What it is

Category theory studies structure-preserving maps between mathematical objects. A category consists of objects and morphisms (arrows) between them, with composition and identity. A functor $F: \mathcal{C} \to \mathcal{D}$ maps one category to another while preserving composition. A natural transformation $\eta: F \Rightarrow G$ is a coherent family of morphisms between two functors: a systematic way to transform one structure-preserving map into another.

The key idea for interpretability: if two circuits are related by a natural transformation, they implement the same abstract computation in different substrates. The transformation respects all the compositional structure, not just input-output behavior.

See [Category theory](https://en.wikipedia.org/wiki/Category_theory) on Wikipedia.

## How it is used in interpretability

Category theory formalizes what the role view means by "same functional role across models." Two components play the same role if there exists a functor between their computational contexts that maps one to the other. This is strictly stronger than matching input-output behavior: it requires that the entire compositional structure is preserved, not just the endpoint.

Causal abstraction can be viewed categorically: an alignment between a high-level causal model and a low-level neural network is a functor that preserves interventional behavior. When the functor exists, the high-level model is a faithful abstraction of the low-level one.

The limitation: category theory provides a language for stating when two things are the same, but does not say how to *find* such equivalences in practice. Constructing functors between neural network circuits requires specifying the categorical structure of both circuits first, which is itself a substantial interpretability challenge.

## Relationship to other formalisms

The [role graph](/mechanistic-views/formalism/role-graph/) is a specific instance of categorical structure: a category whose objects are functional roles and whose morphisms are information-flow dependencies. Category theory generalizes this by asking when two role graphs are equivalent in a structure-preserving sense.

The [fiber bundle quotient](/mechanistic-views/formalism/fiber-bundle-quotient/) has a natural categorical interpretation: gauge transformations form a groupoid (a category where every morphism is invertible), and gauge-invariant quantities are the objects of the quotient category.

[Representation theory](/mechanistic-views/formalism/representation-theory/) is the study of functors from a group (viewed as a single-object category) to vector spaces. The equivariant structure that the structural view looks for is precisely the data of such a functor.

## Further reading

- Geiger et al., "Causal Abstraction for Faithful Model Interpretation" (2021) -- causal abstraction as a functorial relationship
- Fong and Spivak, "An Invitation to Applied Category Theory" (2019) -- accessible introduction to categorical thinking in applied settings
- Gavranovic et al., "Category Theory for Autonomous and Networked Dynamical Systems" (2022) -- categorical frameworks for compositional systems
