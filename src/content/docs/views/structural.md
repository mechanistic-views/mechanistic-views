---
title: Structural View
---

# Structural View

The structural view treats mechanisms as invariant relational structures. What persists under admissible transformations — basis changes, head permutations, symmetries preserving function — is the mechanism proper. What does not persist is parameterization artifact.

## Thesis

A mechanism is an equivalence class: the gauge orbit of all weight configurations that implement the same input-output function. The phrase 'same way' does not add content here — gauge equivalence captures functional identity, not procedural similarity.

## The qua-problem and the justification for gauge orbits

The structural view must answer why the gauge orbit is the right identity criterion rather than, say, component overlap, behavioral equivalence, or cohomology class. This is a version of the *qua-problem*: head-4.4 is the same *qua* gauge orbit as head-7.2 in another model, but different *qua* component index. Any identity claim is implicitly relative to a description level.

The argument for gauge orbits is functional: gauge transformations preserve the input-output function exactly. Two configurations in the same orbit compute the same thing. Any property distinguishing them is a property of the parameterization, not of the computation. If the goal is to characterize computational structure, the gauge orbit is the minimal equivalence class eliminating purely representational variation.

This presupposes that the goal is characterizing computation rather than parameterization-level structure. For safety applications concerned with actual model weights (e.g., detecting when a fine-tuned model has the same dangerous mechanism as a reference), the gauge orbit may be the right level. For applications concerned with computational function (e.g., cross-architecture replication claims), it is the appropriate choice.

Behavioral equivalence is coarser: two mechanisms can compute differently but have the same output distribution. Cohomology class is also coarser: different gauge orbits can have isomorphic cohomology. The gauge orbit is finer than both and is therefore the appropriate choice when the claim is specifically about computational identity.

## What exists

Invariants, transport maps, and equivalence classes:
- **Gauge orbits**: sets of weight configurations related by function-preserving transformations
- **Holonomy fingerprints**: accumulated rotations from parallel-transporting a subspace around a closed loop (connection-dependent; see [Gauge and Holonomy](/formalism/deep-dives/gauge-holonomy/))
- **Cosheaf cohomology classes**: topological invariants tracking localizability (linearization-dependent; see [Sheaf Cohomology](/formalism/deep-dives/sheaves/))
- **Coverage equivalence classes**: circuit hypotheses with isomorphic cosheaf cohomology

## Identity

Two mechanisms are the same when they lie in the same gauge orbit. Isomorphic holonomy groups are a necessary condition (established) but not a sufficient one (open). Same cohomological equivalence class is a coarser criterion than same gauge orbit.

## Evidence

- **Gauge-invariant measurements**: singular values of [OV circuits](https://learnmechinterp.com/topics/qk-ov-circuits/) $W^{OV}$, principal angles, effective rank — invariant under both head permutations and (approximate) orthogonal rotations. [Composition scores](https://learnmechinterp.com/topics/composition-and-virtual-heads/) $\|W^{OV}_u \cdot W^{KQ}_v\|_F$ are invariant under head permutations but not under the orthogonal rotation symmetry (a residual-stream rotation $U$ transforms $W^{KQ} \to U W^{KQ}$, changing the score); they are gauge-invariant only with respect to the permutation subgroup
- **Holonomy**: estimates of the holonomy group (connection must be specified); isomorphic holonomy is necessary for identity
- **Cohomological tests**: $H^0$ and $H^1$ of the circuit cosheaf (relative to base sections and choice of cosheaf structure)

## Formalism

[Fiber bundle quotient](/formalism/fiber-bundle-quotient/) $\mathcal{W}/\mathcal{G}$, principal fiber bundles (at generic points), parallel transport, holonomy (connection-dependent), cellular cosheaf cohomology (base-section-dependent). See the [Gauge and Holonomy](/formalism/deep-dives/gauge-holonomy/) and [Sheaf Cohomology](/formalism/deep-dives/sheaves/) deep dives for the technical conditions under which these constructions are well-defined.

## What it explains

Portability. When the same mechanism appears across seeds or architectures, what is preserved is the structural invariants. Also explains apparent circuit disagreements: coverage-equivalent proposals (same cosheaf cohomology) have the same localizability structure and may not be contradicting each other — though coverage equivalence is a necessary, not sufficient, condition for non-contradiction (see [Sheaf Cohomology](/formalism/deep-dives/sheaves/)).

## What it lets you prove

- **Gauge-invariant identity**: same gauge orbit implies same mechanism (the substance is the argument that gauge orbits are the right level)
- **Holonomy as necessary condition**: same mechanism implies isomorphic holonomy groups
- **Cohomological localizability**: relative to the cosheaf construction and base sections

## Failure modes

**Computability.** Holonomy and cosheaf cohomology are difficult to compute at scale.

**Over-abstraction.** Too coarse an invariant conflates distinct mechanisms.

**Wrong symmetry group.** LayerNorm breaks the full $O(d)$ rotation symmetry; using the wrong $\mathcal{G}$ produces incorrect identity judgments.

**Gauge group non-freeness.** At non-generic points (identical heads), the bundle structure breaks down and holonomy is undefined.

**Connection dependence.** Different connections give different holonomy groups. Claims must specify the connection.

## Relationship to Mechanistic Validity

Strengthens external validity (generalization as invariance under symmetries) and interpretive validity (Marr-level correspondence as structural claim). The caveats about gauge freeness and connection choice must be stated alongside any Mechanistic Validity assessment using structural-view criteria.

## Further reading

- Elhage et al., "A Mathematical Framework for Transformer Circuits" (2021) — composition scores and QK/OV decomposition as weight-space invariants
- Ainsworth et al., "Git Re-Basin: Merging Models modulo Permutation Symmetries" (2023) — permutation gauge symmetry in neural networks
- For related views: [Object view](/views/object/) (uses the same weight matrices but identifies mechanisms with components, not invariants), [Subspace view](/views/subspace/) (identifies mechanisms with Grassmannian points, a related but distinct geometric object)
