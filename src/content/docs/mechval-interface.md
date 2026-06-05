---
title: MechVal Interface
---

# MechVal Interface

Mechanistic Views and Mechanistic Validity (MechVal) are companion frameworks with different scopes.

**MechVal** asks: is a mechanistic claim warranted by the evidence provided? It supplies 27 operational criteria across 5 validity lenses and a 5-tier evidence taxonomy.

**Mechanistic Views** asks: what background view makes the claim meaningful in the first place?

The questions are distinct but dependent. A MechVal audit assumes the claim's concepts — mechanism, identity, evidence — are well-defined. Mechanistic Views provides those definitions.

## How the validity lenses map to view commitments

| MechVal lens | What it validates | View-level commitment it presupposes |
|---|---|---|
| Construct validity | The mechanism concept is well-specified | Ontology and identity axes |
| Measurement validity | The measurement procedure is stable | Evidence axis — what is being measured must be identified first |
| Internal validity | The causal claim is supported | Evidence axis — intervention type must match mechanism type; IIA tests surgical intervention quality |
| External validity | The claim generalizes | Identity axis — generalization requires a criterion for when two descriptions refer to the same mechanism |
| Interpretive validity | The claim is at the right explanatory level | Formalism and target axes — Marr-level correspondence is a structural claim |

## Target axis and Marr levels

The target axis determines what explanatory level is required. Marr's three levels: (1) computational theory — *what* the system computes and why; (2) algorithm and representation — *how* it carries out the computation (the circuit structure, roles, data structures); (3) physical implementation — the specific weights, neurons, or hardware realizing the algorithm.

A Marr-level-1 claim (the model computes function $f$) is satisfied by behavioral evidence. A Marr-level-2 claim (it does so via circuit or role structure $C$) requires component- or subspace-level mechanistic evidence. A Marr-level-3 claim (it does so using these specific weight values) requires weight-space evidence. This dependence on the target axis is not automatic in MechVal and must be stated by the researcher.

## The five-tier taxonomy

MechVal uses five evidence tiers, assigned relative to a stated view:

| Tier | Label | Description |
|---|---|---|
| 1 | Existence claim | Behavioral observation only; no mechanistic evidence |
| 2 | Preliminary | Single-domain mechanistic evidence; failure modes not ruled out |
| 3 | Established | Two-domain convergent evidence; cross-seed or cross-prompt consistency shown |
| 4 | Well-characterized | Three-domain triangulation; cross-architecture or cross-task generalization established |
| 5 | Canonical | Multiple independent replications; mechanism used as reference for further work |

Tier assignments are view-relative: the same evidence can warrant Tier 3 under the object view and only Tier 2 under the subspace view, because the subspace view requires cross-domain triangulation where the object view does not.

## The geometric realization of the validity chain

The companion geometry paper shows the MechVal validity chain can be realized as Grassmannian convergence conditions:

- **Construct validity**: weight-space, activation-space, and dynamics-space subspace estimates lie within geodesic $\epsilon_C$ of each other on $\mathrm{Gr}(k, d)$
- **Measurement validity**: Fréchet variance of subspace estimates across seeds and prompts below $\epsilon_M$
- **Internal validity**: IIA tests surgical intervention quality (activation-space domain); composition score $\|W^{OV}_u \cdot W^{KQ}_v\|_F$ provides a distribution-free *upper bound* on causal information flow (weight-space domain) — it is a necessary condition for significant flow, not a direct causal test, and is invariant under head permutations but not full orthogonal rotation
- **External validity**: cross-architecture generalization corresponds to isomorphic holonomy groups (necessary condition, connection-dependent)
- **Interpretive validity**: the claim's Marr level determines the required evidence type (level 1 behavioral; level 2 component/subspace mechanistic; level 3 weight-space)

## Safety applications

Safety-relevant interpretability makes claims of a different type than standard circuit descriptions. The relevant claims include: "this model has a deceptive internal goal," "this model's capability representation generalizes to out-of-distribution inputs," "fine-tuning changed this mechanism." These claims require more than the object view can provide.

**Object view limitations for safety.** Object-view claims are model- and seed-specific: "head 4.4 in this checkpoint implements name-moving." They cannot establish whether a dangerous capability is present in a different model, has generalized across training, or has been removed by fine-tuning. Safety claims require cross-model identity, which requires at minimum the role or structural view.

**Minimum view for safety claims:**

| Safety claim type | Minimum required view | Why object view fails |
|---|---|---|
| "This model has the same dangerous capability as a reference model" | Structural (gauge-orbit identity) | Object view has no cross-model identity criterion |
| "This capability generalizes to new inputs" | Role or subspace | Object view is input-distribution dependent |
| "Fine-tuning removed this mechanism" | Process or structural | Object view cannot track mechanism identity across training |
| "This model is pursuing goal G" | Role (functional specification) | Object view describes components, not goals |
| "This representation encodes deceptive intent" | Subspace or structural | Object view cannot represent distributed representations |

The instrumental view is explicitly insufficient for safety: saying "this predictive shorthand is useful" cannot distinguish a model that has learned a dangerous goal from one that produces dangerous-looking outputs by a different mechanism, and these may come apart under deployment conditions.

## Caveats for structural-view criteria

When using structural-view identity criteria in a MechVal audit:
- State whether the model is at a generic point (free gauge action)
- Specify the connection used for holonomy estimates
- Specify the base sections used for cosheaf construction
These are not formalities; different choices give different verdicts.
