---
title: Views
---

# Views

We define eight mechanistic views — coherent positions on what a mechanism is, when two are the same, and what counts as evidence. They are ordered by increasing ontological commitment — how much they claim about what mechanisms are:

$$\text{Instrumental} < \text{Perspectival} < \text{Object} < \text{Role} < \text{Subspace} < \text{Structural} < \text{Process} < \text{Stratified}$$

Higher-commitment views make stronger claims but require more evidence. The instrumental view requires only predictive utility; the stratified view requires evidence across multiple strata and measurement resolutions. 

Most published interpretability work operates at the Object or Role level without stating this explicitly. This creates confusion when papers using different views disagree — the IOI circuit replication debates, the probing wars, and "how big is a circuit?" arguments are all arguably partly view-level disagreements alongside empirical ones. Making the view explicit takes one sentence and prevents a class of errors where evidence collected at one level is used to draw conclusions at another.

The views apply to both **mechanisms** (circuits, computations) and **channels** (the representations those circuits operate over). A channel is a mechanism at a different grain: the Object view says it is a specific direction or neuron, the Role view says it is whatever plays a given functional role, the Subspace view says it is a causal subspace, and so on. Whether a given channel constitutes a "real feature" is itself a view-dependent question — the Object view says yes if it is a stable direction, the Subspace view says yes if it is causally active, and the Perspectival view says there is no view-independent answer.

The views are not mutually exclusive: a single paper may use several, and convergence across views constitutes stronger evidence than any single view.

| View | Ontology | Identity | Evidence | Formalism | Target |
|---|---|---|---|---|---|
| [Instrumental](/mechanistic-views/views/instrumental/) | Predictive model | Predictive equivalence | [Forecast, intervention utility](/mechanistic-views/views/instrumental/#evidence) | [Model theory](/mechanistic-views/formalism/model-theory/) | Behavioral prediction |
| [Perspectival](/mechanistic-views/views/perspectival/) | Method projection | Cross-method coherence | [Multi-method robustness](/mechanistic-views/views/perspectival/#evidence) | [Measurement algebra](/mechanistic-views/formalism/measurement-algebra/) | Method-relative |
| [Object](/mechanistic-views/views/object/) | Concrete part | Component overlap | [Ablation, patching](/mechanistic-views/views/object/#evidence) | [Directed graph](/mechanistic-views/formalism/directed-graph/) | Specific behavior |
| [Role](/mechanistic-views/views/role/) | Functional role | Role equivalence | [Role-specific causal tests](/mechanistic-views/views/role/#evidence) | [Role graph](/mechanistic-views/formalism/role-graph/) | Functional class |
| [Subspace](/mechanistic-views/views/subspace/) | Causal subspace | Same projector; $d_{\mathrm{Gr}} < \theta$ | [DAS/IIA (linear)](/mechanistic-views/views/subspace/#evidence), [subspace stability](/mechanistic-views/formalism/grassmannian/#subspace-stability) | [Grassmannian $\mathrm{Gr}(k,d)$](/mechanistic-views/formalism/grassmannian/) | Representational variable |
| [Structural](/mechanistic-views/views/structural/) | Gauge-invariant structure | Gauge-orbit membership | [Holonomy, composition scores](/mechanistic-views/views/structural/#evidence) | [Fiber bundle quotient](/mechanistic-views/formalism/fiber-bundle-quotient/) | Computation class |
| [Process](/mechanistic-views/views/process/) | Formation trajectory | Same trajectory type | [Checkpoints, formation knockouts](/mechanistic-views/views/process/#evidence) | [Dynamical system](/mechanistic-views/formalism/dynamical-system/) | Mechanism origin |
| [Stratified](/mechanistic-views/views/stratified/) | Stratum point | Stratum + local equivalence | [Dimensionality, localization](/mechanistic-views/views/stratified/#evidence) | [Whitney stratification](/mechanistic-views/formalism/stratification/) | Resolution-relative |

## Validity coverage comparison

Each view's methods cover a different subset of the 27 [Mechanistic Validity](https://mechanistic-validity.github.io/mechanistic-validity/) criteria. Higher-commitment views cover more criteria; the two skeptical views (Instrumental, Perspectival) have the most "impossible" entries because they do not commit to a mechanism existing. See each view's page for the full breakdown.

| View | [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) (5) | [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) (5) | [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) (6) | [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) (6) | [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) (5) | Total | Impossible |
|---|---|---|---|---|---|---|---|
| [Instrumental](/mechanistic-views/views/instrumental/) | 0/5 | 0/5 | 1/6 | 0/6 | 1/5 | 2/27 | 20 |
| [Perspectival](/mechanistic-views/views/perspectival/) | 0/5 | 0/5 | 0/6 | 1/6 | 2/5 | 3/27 | 16 |
| [Object](/mechanistic-views/views/object/) | 1/5 | 2/5 | 1/6 | 1/6 | 1/5 | 6/27 | 4 |
| [Role](/mechanistic-views/views/role/) | 2/5 | 2/5 | 3/6 | 1/6 | 2/5 | 10/27 | 3 |
| [Subspace](/mechanistic-views/views/subspace/) | 3/5 | 3/5 | 2/6 | 3/6 | 2/5 | 13/27 | 0 |
| [Structural](/mechanistic-views/views/structural/) | 4/5 | 3/5 | 3/6 | 3/6 | 3/5 | 16/27 | 0 |
| [Process](/mechanistic-views/views/process/) | 2/5 | 2/5 | 2/6 | 2/6 | 2/5 | 10/27 | 0 |
| [Stratified](/mechanistic-views/views/stratified/) | 4/5 | 3/5 | 3/6 | 3/6 | 3/5 | 16/27 | 0 |

The pattern reflects the views' different commitments: the object view gives you necessity and sufficiency but cannot establish cross-architecture identity, measurement invariance, or convergent validity — these are structurally impossible given its ontology, not just untested. The subspace view addresses the coordinate-dependence problems (invariance, convergence) and has no impossible criteria. The structural and stratified views address the most criteria but are computationally expensive.

The process view scores 10/27 on its own, but this is misleading — it is not a standalone view. It is a temporal modifier that pairs with a static view: process + subspace inherits the subspace view's 13/27 coverage and adds formation evidence on top. Process + structural inherits 16/27. The process view's unique contribution — formation order, developmental prerequisites, phase transitions — is orthogonal to the static criteria in the table.

The skeptical views (Instrumental, Perspectival) score lowest because they deny that there is a mechanism to validate. Most criteria become impossible when there is no object to validate the construct of, test the invariance of, or generalize across architectures.

## How the views relate

The views are not mutually exclusive at the level of phenomena. A given model may contain mechanisms best described by different views at different strata. The goal is to identify which commitments different descriptions carry, not to select a single correct view.

See [View Mappings](mappings/) for diagrams showing how the views relate, and how other positions in the literature map onto these eight views.
