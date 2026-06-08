---
title: Subspace View
---

# Subspace View

The subspace view treats mechanisms as causal subspaces of the residual stream. A mechanism's variable is located in a low-dimensional subspace — a geometric object independent of any particular coordinate system.

## Thesis

A mechanism is a subspace $S \in \mathrm{Gr}(k, d)$ such that intervening on the projection of the residual stream onto $S$ causes the model to behave as if the corresponding high-level variable had changed.

## Interventionism and the surgical intervention condition

The definition is interventionist in the sense of Woodward (2003): a causal variable is identified with the subspace $S$ such that a surgical intervention on $S$ changes the model's output in the predicted way while leaving everything else unchanged.

For this to be a genuine causal claim rather than a correlation, the intervention must be **surgical**: changing $S$ must not directly alter the values of other variables in the causal graph. In the DAS/IIA setting, the relevant test is the **IIA condition**: base-pass behavior is preserved on all variables other than the one being intervened on.

IIA is therefore not merely a measurement reliability condition. It is an empirical test bearing on the validity of the causal claim. However, low IIA has two distinct interpretations that must be distinguished:

**(A) Non-surgical intervention.** The subspace swap disturbs variables other than the claimed one — the intervention leaks into other parts of the causal graph. The intervention is not isolating the proposed variable.

**(B) Wrong causal graph.** The intervention may be perfectly surgical on the proposed variable, but the causal graph assumed by the test is incorrect — the variable being swapped is causally upstream of what is being measured, so changing it *should* change base-pass behavior of downstream variables. In this case low IIA is evidence of incorrect causal graph specification, not a non-surgical intervention.

These two interpretations produce the same IIA signal but require different responses: (A) calls for a better subspace candidate; (B) calls for revising the causal graph. IIA should be reported as a diagnostic for intervention quality and graph validity, not just as a scalar accuracy metric.

## What exists

A point on $\mathrm{Gr}(k, d)$. DAS identifies a projector $QQ^\top$ invariant under $Q \mapsto QR$ for any $R \in O(k)$ — a subspace, not a specific matrix. A mechanism also has transport structure: weight matrices induce maps between subspaces at different layers.

## Identity

Geodesic distance on $\mathrm{Gr}(k, d)$:

$$d(S_1, S_2) = \left(\sum_{i=1}^k \theta_i^2\right)^{1/2}$$

where $\theta_1, \ldots, \theta_k$ are the principal angles between $S_1$ and $S_2$, computed as $\cos\theta_i = \sigma_i(P_1 P_2)$.

## Evidence

Three independently non-injective sources:

- **Activation-space interventional**: DAS/IIA (with IIA as surgical-intervention test)
- **Weight-space structural**: SVD of $W^{OV} = W^O W^V$, invariant subspace decomposition
- **Dynamics-space**: AGOP convergence toward the eventual DAS subspace during training

Each domain is individually non-injective on mechanism space, but the joint map is conjectured to be injective under a **general position condition** — the requirement that no pair of distinct mechanisms looks identical across all three domains simultaneously. This has not been formally verified for natural transformer mechanisms. See the [Single-Method vs. Triangulated Evidence](/decisions/single-vs-triangulated/) page for discussion.

## Formalism

Grassmannian geometry. The **Grassmannian SCM (G-SCM)** extends Pearl's SCM with subspaces as nodes and weight-induced transport maps as edges. In principle, requiring alignment maps to respect transport structure addresses the Sutter et al. (2025) vacuity result, though the G-SCM has not yet been empirically validated on natural transformer circuits. See [Grassmannian Geometry](/formalism/grassmannian/).

## What it explains

How a high-level causal variable can be distributed across many neurons while remaining localized in a low-dimensional direction.

Why SAE features and DAS subspaces are not always the same object: SAE features are recovered by optimising for sparse reconstruction of activations — they are the directions that best explain activation variance with sparse codes. DAS subspaces are recovered by optimising for causal interventional consistency (IIA) — they are the directions that best predict the model's downstream behaviour under controlled swaps. A direction can explain activation variance without being causally active (e.g. a feature that is expressed but causally inert for the target task), and a direction can be causally active without being the sparsest description of the activations (e.g. a polysemantic direction). These are distinct optimisation objectives with distinct solutions in general.

## What it lets you prove

- **Convergence**: weight-space and activation-space subspaces converge on $\mathrm{Gr}(k, d)$
- **Non-vacuity** (theoretical): Sutter et al. (2025) show that for unrestricted nonlinear alignments, high IIA is achievable without genuine causal structure. Restricting to transport-respecting alignments (G-SCM) is expected to rule out these degenerate solutions, though this has not yet been empirically demonstrated on natural transformer circuits
- **Flow bounds**: $\|W^{OV}_u \cdot W^{KQ}_v\|_F$ is a distribution-free upper bound on causal information flow
- **Triangulation necessity**: each evidence domain alone is non-injective on mechanism space; convergence across domains is required for unambiguous identification

## SAE features and the subspace view

Sparse autoencoders (SAEs) have become the dominant practical method for recovering $\mathcal{M}_1$ features — single directions in the residual stream. The relationship between SAE features and subspace-view mechanisms is more subtle than it first appears.

**What SAEs recover.** An SAE trained on residual stream activations at layer $l$ learns a dictionary $D \in \mathbb{R}^{d \times n}$ ($n \gg d$) and sparse codes $a \in \mathbb{R}^n_{\geq 0}$ such that $x \approx Da$. Each column $d_i \in \mathbb{R}^d$ is a candidate feature direction — a point in $\mathrm{Gr}(1, d)$.

**The epistemological stance SAEs embed.** A feature $d_i$ is treated as real if it appears reliably in the sparse codes and has a human-interpretable activating pattern. This is a *sparse reconstruction criterion* for feature existence — a feature exists if it is needed to reconstruct the activations. This is not the same as the subspace-view *causal criterion* — a mechanism exists if intervening on the corresponding subspace changes the model's output as predicted.

**When they agree and when they don't.** A direction can be needed for sparse reconstruction without being causally active on any downstream task (a feature that is expressed but inert). A direction can be causally active without being the sparsest description of the activations (a polysemantic direction). In practice, high-IIA DAS features and SAE features often but not always identify the same directions.

**Feature splitting and polysemanticity.** As the SAE dictionary size $n$ increases, some features split into more specific ones (feature splitting). This corresponds to moving from $\mathcal{M}_k$ to $\mathcal{M}_1^n$ in the stratified view — resolving a multi-dimensional subspace into multiple one-dimensional ones. Whether the split features are genuinely distinct mechanisms or coordinate choices within the same subspace is an identity question that requires causal testing to resolve.

**Practical recommendation.** SAE features are valuable for discovering candidate $\mathcal{M}_1$ mechanisms efficiently. Treat SAE recovery as hypothesis generation. Confirm with DAS/IIA that the identified directions are causally active, not merely reconstruction-relevant. Report both the SAE-recovered direction and the IIA score; divergence between the two is informative.

## Failure modes

**Linearity.** Assumes the causal variable is linearly encoded. Nonlinear or context-switching encoding requires Riemannian geometry (as in the grokking case).

**Wrong $k$.** Too small misses the variable; too large conflates multiple variables.

**Prompt dependence.** A subspace with high IIA on one distribution may not transfer across distributions.

**Non-surgical interventions or wrong causal graph.** Low IIA has two interpretations: the intervention leaks into other variables (non-surgical), or the proposed causal graph is wrong and changing this variable should affect the measured variable (wrong graph). See the interventionism section above for how to distinguish them. High DAS accuracy does not by itself warrant the causal claim when IIA is low.

## Relationship to Mechanistic Validity

Gives concrete objects for construct validity (a point on a manifold) and measurement validity (Fréchet variance across seeds). IIA as a surgical-intervention test is a diagnostic for internal validity.
