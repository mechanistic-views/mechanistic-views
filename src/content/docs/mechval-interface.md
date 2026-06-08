---
title: Mechanistic Validity Interface
---

# Mechanistic Validity Interface

Mechanistic Views and [Mechanistic Validity](https://mechanistic-validity.github.io/mechanistic-validity/) are companion frameworks with different scopes.

**[Mechanistic Validity](https://mechanistic-validity.github.io/mechanistic-validity/)** asks: is a mechanistic claim warranted by the evidence provided? It supplies 27 operational criteria across 5 validity lenses and a 5-tier evidence taxonomy.

**Mechanistic Views** asks: what background view makes the claim meaningful in the first place?

The questions are distinct but dependent. A Mechanistic Validity audit assumes the claim's concepts — mechanism, identity, evidence — are well-defined. Mechanistic Views supplies those definitions, making the Mechanistic Validity criteria applicable.

## How the validity lenses map to view commitments

| Mechanistic Validity lens | What it validates | View-level commitment it presupposes |
|---|---|---|
| Construct validity | The mechanism concept is well-specified | Ontology and identity axes |
| Measurement validity | The measurement procedure is stable | Evidence axis — what is being measured must be identified first |
| Internal validity | The causal claim is supported | Evidence axis — intervention type must match mechanism type; IIA tests surgical intervention quality |
| External validity | The claim generalizes | Identity axis — generalization requires a criterion for when two descriptions refer to the same mechanism |
| Interpretive validity | The claim is at the right explanatory level | Formalism and target axes — Marr-level correspondence is a structural claim |

## Target axis and Marr levels

The target axis determines what explanatory level is required. Marr's three levels: (1) computational theory — *what* the system computes and why; (2) algorithm and representation — *how* it carries out the computation (the circuit structure, roles, data structures); (3) physical implementation — the specific weights, neurons, or hardware realizing the algorithm.

A Marr-level-1 claim (the model computes function $f$) is satisfied by behavioral evidence. A Marr-level-2 claim (it does so via circuit or role structure $C$) requires component- or subspace-level mechanistic evidence. A Marr-level-3 claim (it does so using these specific weight values) requires weight-space evidence. This dependence on the target axis is not automatic in Mechanistic Validity and must be stated by the researcher.

## The five-tier taxonomy

Mechanistic Validity uses five evidence tiers, assigned relative to a stated view:

| Tier | Label | Description |
|---|---|---|
| 1 | Existence claim | Behavioral observation only; no mechanistic evidence |
| 2 | Preliminary | Single-domain mechanistic evidence; failure modes not ruled out |
| 3 | Established | Two-domain convergent evidence; cross-seed or cross-prompt consistency shown |
| 4 | Well-characterized | Three-domain triangulation; cross-architecture or cross-task generalization established |
| 5 | Canonical | Multiple independent replications; mechanism used as reference for further work |

Tier assignments are view-relative: the same evidence can warrant Tier 3 under the object view and only Tier 2 under the subspace view, because the subspace view requires cross-domain triangulation where the object view does not.

## Minimal triangulation for Tier 3

Each view requires convergent evidence from at least two independent domains. Two of any three domains alone leaves an identifiability gap.

**Object view:**

1. **Activation-space interventional**: activation patching or ablation showing the component is necessary
2. **Weight-space structural**: composition scores or SVD showing the component participates in a weight-space circuit
3. **At least one of**: cross-prompt robustness (same component is necessary on held-out distributions), cross-seed consistency, or path patching confirming the causal pathway

**Role view:**

1. **Activation-space interventional**: role-specific causal test (DAS/IIA for the role, or causal scrubbing against a role-level causal graph)
2. **Independence from specific components**: the role survives component knockouts (backup behavior), or is realized by different components in different models
3. **At least one of**: cross-architecture transfer (same role found in a different model family), cross-task generalization (role serves the same function on related tasks), or weight-space evidence that the role structure is latent

**Subspace view:**

1. **Activation-space interventional**: DAS/IIA with IIA reported and interpreted as surgical-intervention quality
2. **Weight-space structural**: SVD or composition score analysis showing the subspace is latent in weights
3. **At least one of**: dynamics-space evidence (AGOP convergence), cross-seed consistency, or cross-architecture transfer

**Structural view:**

1. **Weight-space invariant**: composition scores, holonomy, or other gauge-invariant quantities showing the structure exists in weights independent of basis choice
2. **Activation-space confirmation**: patching or ablation results that are consistent across reparameterizations of the model (not just one basis)
3. **At least one of**: cross-architecture transfer (same invariant structure in a different model family), or formal verification that the claimed invariance holds under the full gauge group (not just a subgroup)

## The geometric realization of the validity chain

The Mechanistic Validity validity chain can in principle be realized as Grassmannian convergence conditions. These realizations are not yet empirically validated:

- **Construct validity**: weight-space, activation-space, and dynamics-space subspace estimates lie within geodesic $\epsilon_C$ of each other on $\mathrm{Gr}(k, d)$
- **Measurement validity**: Fréchet variance of subspace estimates across seeds and prompts below $\epsilon_M$
- **Internal validity**: IIA tests surgical intervention quality (activation-space domain); composition score $\|W^{OV}_u \cdot W^{KQ}_v\|_F$ provides a distribution-free *upper bound* on causal information flow (weight-space domain) — it is a necessary condition for significant flow, not a direct causal test, and is invariant under head permutations but not full orthogonal rotation
- **External validity**: cross-architecture generalization corresponds to isomorphic holonomy groups (necessary condition, connection-dependent)
- **Interpretive validity**: the claim's Marr level determines the required evidence type (level 1 behavioral; level 2 component/subspace mechanistic; level 3 weight-space)

## Caveats for structural-view criteria

When using structural-view identity criteria in a Mechanistic Validity audit:
- State whether the model is at a generic point (free gauge action)
- Specify the connection used for holonomy estimates
- Specify the base sections used for cosheaf construction
These are not formalities; different choices give different verdicts.
