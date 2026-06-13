---
title: Representation Theory
---

# Representation Theory

A cross-cutting formalism used by the [subspace](/mechanistic-views/views/subspace/) and [structural](/mechanistic-views/views/structural/) views.

## What it is

Representation theory studies how abstract algebraic structures (groups, algebras) act on vector spaces. A representation of a group $G$ on a vector space $V$ is a homomorphism $\rho: G \to \mathrm{GL}(V)$ assigning to each group element a linear transformation of $V$ that respects the group operation. A map $f: V \to W$ between representations is *equivariant* if $f(\rho_V(g) \cdot v) = \rho_W(g) \cdot f(v)$ for all $g \in G$ and $v \in V$: the map commutes with the group action.

The key idea for interpretability: if a model's internal computation is equivariant with respect to some symmetry group, then that symmetry constrains what the computation can be. Finding equivariant structure means finding structure that is invariant under symmetry transformations, which is exactly what the structural view looks for.

See [Representation theory](https://en.wikipedia.org/wiki/Representation_theory) on Wikipedia.

## How it is used in interpretability

The subspace view uses representation theory when asking whether a learned subspace respects symmetries of the input. If a model represents spatial position, and the position representation is equivariant under translation, then the subspace has structure beyond what its dimensionality alone captures. The representation-theoretic decomposition of the model's activation space into irreducible representations reveals what symmetries the model has learned.

The structural view uses representation theory more directly: gauge transformations act on the weight matrices, and the gauge-invariant quantities are exactly the ones that commute with this action. The [fiber bundle quotient](/mechanistic-views/formalism/fiber-bundle-quotient/) formalizes this as parallel transport along gauge orbits.

The limitation: identifying the relevant symmetry group is non-trivial. Natural symmetries (permutation of tokens, rotation of embeddings) are clear, but most interesting structure in trained models involves learned symmetries that must be discovered empirically. Representation theory tells you what follows once you know the group, but not which group to look for.

## Relationship to other formalisms

Representation theory and the [Grassmannian](/mechanistic-views/formalism/grassmannian/) interact directly: the action of $\mathrm{GL}(d)$ on $\mathrm{Gr}(k, d)$ is a representation, and equivariant subspaces are fixed points of this action. A subspace that is invariant under a symmetry group has a richer identity criterion than Grassmannian distance alone.

The connection to [category theory](/mechanistic-views/formalism/category-theory/) is formal: a representation is a functor from a group (viewed as a category with one object) to the category of vector spaces. Equivariant maps are natural transformations between such functors. This makes representation theory a special case of the categorical framework.

The [dictionary](/mechanistic-views/formalism/dictionary/) formalism finds directions in activation space; representation theory asks whether those directions transform coherently under symmetries. A dictionary feature that is part of an irreducible representation cannot be understood in isolation from the other features in that representation.

## Further reading

- Park et al., "The Linear Representation Hypothesis and the Geometry of Large Language Models" (2024) -- linear representations and their geometric structure
- Thomas et al., "Tensor Field Networks" (2018) -- equivariant neural architectures as representations
- Higgins et al., "Towards a Definition of Disentangled Representations" (2018) -- disentanglement as group-theoretic decomposition
