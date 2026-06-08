---
title: Views
---

# Views

Each page presents one answer to the five axes — a coherent bundle of ontological, identity, epistemological, representational, and scope commitments.

| View | Ontology | Identity | Evidence | Formalism | Target |
|---|---|---|---|---|---|
| [Instrumental](/views/instrumental/) | Predictive model | Predictive equivalence | [Forecast, intervention utility](/views/instrumental/#evidence) | [Model theory](/formalism/model-theory/) | Behavioral prediction |
| [Perspectival](/views/perspectival/) | Method projection | Cross-method coherence | [Multi-method robustness](/views/perspectival/#evidence) | [Measurement algebra](/formalism/measurement-algebra/) | Method-relative |
| [Object](/views/object/) | Concrete part | Component overlap | [Ablation, patching](/views/object/#evidence) | [Directed graph](/formalism/directed-graph/) | Specific behavior |
| [Role](/views/role/) | Functional role | Role equivalence | [Role-specific causal tests](/views/role/#evidence) | [Role graph](/formalism/role-graph/) | Functional class |
| [Subspace](/views/subspace/) | Causal subspace | Same projector; $d_{\mathrm{Gr}} < \theta$ | [DAS/IIA (linear)](/views/subspace/#evidence), [subspace stability](/formalism/grassmannian/#subspace-stability) | [Grassmannian $\mathrm{Gr}(k,d)$](/formalism/grassmannian/) | Representational variable |
| [Structural](/views/structural/) | Gauge-invariant structure | Gauge-orbit membership | [Holonomy, composition scores](/views/structural/#evidence) | [Fiber bundle quotient](/formalism/fiber-bundle-quotient/) | Computation class |
| [Process](/views/process/) | Formation trajectory | Same trajectory type | [Checkpoints, formation knockouts](/views/process/#evidence) | [Dynamical system](/formalism/dynamical-system/) | Mechanism origin |
| [Stratified](/views/stratified/) | Stratum point | Stratum + local equivalence | [Dimensionality, localization](/views/stratified/#evidence) | [Whitney stratification](/formalism/stratification/) | Resolution-relative |

The views are not mutually exclusive: a single paper may use several, and convergence across views constitutes stronger evidence than any single view. The point is to distinguish them so that each view's commitments and limitations can be assessed independently.

## View families

The eight views group into three families of two (Identity, Mathematical, Process) plus two singletons (Methodological, Pragmatic), ordered by increasing ontological commitment.

![Eight views organized by family](/mechanistic-views/figures/eight-views-families.svg)

## Ontology determines identity determines formalism

Each view's ontological commitment implies a specific identity criterion, which in turn implies a natural formalism. The chain is mostly 1-to-1: choosing what a mechanism *is* determines when two are *the same* determines what *math* you use.

![Three-column chain: Ontology → Identity → Formalism](/mechanistic-views/figures/ontology-identity-formalism-v2.svg)

## Ontological commitment ordering

The views can be ordered by increasing ontological commitment — how much they claim about the existence and nature of the mechanism independent of any measurement procedure:

$$\text{Instrumental} < \text{Perspectival} < \text{Object} < \text{Role} < \text{Subspace} < \text{Structural} < \text{Process} < \text{Stratified}$$

Higher-commitment views make stronger claims but require more evidence. The instrumental view requires only predictive utility; the stratified view requires evidence across multiple strata and measurement resolutions. Most published interpretability work operates at the Object or Role level.

## Reading path

Start with [Object](object/) and [Subspace](subspace/) for the two most common background assumptions in the current literature. Then read [Structural](structural/) for the gauge-invariance argument. Read [Stratified](stratified/) last: it synthesizes the others as special cases.

## How the views relate

The views are not mutually exclusive at the level of phenomena. A given model may contain mechanisms best described by different views at different strata. The goal is to identify which commitments different descriptions carry, not to select a single correct view.
