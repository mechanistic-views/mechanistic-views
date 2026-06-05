---
title: Glossary
---

# Glossary

Key terms used across this site, in order of dependency.

---

**Residual stream.** The $d$-dimensional vector accumulated by transformer blocks. The ambient space for mechanism geometry.

**Attention head.** A computational unit producing a weighted sum over positions projected through output and value weights. The OV circuit: $W^{OV} = W^O W^V$.

**Grassmannian $\mathrm{Gr}(k, d)$.** The set of all $k$-dimensional linear subspaces of $\mathbb{R}^d$. A smooth compact manifold of dimension $k(d-k)$.

**Principal angles.** The canonical angles $0 \leq \theta_1 \leq \cdots \leq \theta_k \leq \pi/2$ between two specific $k$-dimensional subspaces $S_1$ and $S_2$, computed via $\cos\theta_i = \sigma_i(P_1 P_2)$. A property of the *pair*, not of either subspace alone. Geodesic distance: $d(S_1, S_2) = (\sum_i \theta_i^2)^{1/2}$.

**Causal subspace.** A subspace $S \in \mathrm{Gr}(k,d)$ such that swapping the projection onto $S$ transfers a high-level causal variable. The IIA condition tests whether this intervention is surgical.

**Surgical intervention.** An intervention changing a causal variable's value without directly altering others in the causal graph. Required for interventionist causal claims (Woodward, 2003). IIA is the empirical test of surgical intervention quality.

**Transport map.** $\tau_W(S) = \overline{\mathrm{span}(WS)}$ for $W \in \mathbb{R}^{d_\text{out} \times d_\text{in}}$. For nonlinear modules: defined via expected Jacobian.

**G-SCM.** Grassmannian SCM: Pearl SCM with subspaces as nodes and transport maps as edges. Requires transport-respecting alignments, which in principle addresses the Sutter et al. (2025) vacuity result. Not yet empirically validated on natural transformer circuits.

**Sutter et al. (2025) (Denis Sutter, Julian Minder, Thomas Hofmann, Tiago Pimentel. "The Non-Linear Representation Dilemma: Is Causal Abstraction Enough for Mechanistic Interpretability?" NeurIPS 2025) vacuity result.** Unrestricted nonlinear alignment functions can achieve high IIA without genuine causal structure.

**Gauge transformation.** A symmetry of transformer weights preserving function. Exact: head permutations, $W^Q/W^K$ rescaling. Approximate (broken by LayerNorm): orthogonal rotation of residual stream.

**Gauge orbit.** All weight configurations related by gauge transformations.

**Gauge group $\mathcal{G}$.** The group of gauge transformations. The fiber bundle structure requires $\mathcal{G}$ to act freely — holds only at generic points where no two heads at the same layer have identical weights.

**Holonomy.** The rotation accumulated from parallel-transporting a subspace around a closed loop in $\mathcal{W}/\mathcal{G}$. Gauge-invariant. Depends on the connection. Isomorphic holonomy groups: necessary but not proven sufficient for same-mechanism identity under the structural view.

**Connection (on the weight bundle).** The choice of horizontal subspace in the principal bundle $\mathcal{W} \to \mathcal{W}/\mathcal{G}$. Natural options: Euclidean metric and Fisher information metric. These give different parallel transports and different holonomy groups. Claims about holonomy should specify the connection.

**Base section.** The reference subspace at each site in the layer graph, relative to which the cellular cosheaf is linearized. Cosheaf cohomology depends on this choice and should be stated explicitly in empirical applications.

**Cellular cosheaf.** A cosheaf on a directed graph: vector spaces at nodes, forward coboundary maps on edges. For a graph with no 2-cells, the cochain complex is $0 \to C^0 \xrightarrow{\delta^0} C^1 \to 0$, and $H^1 = C^1/\mathrm{im}(\delta^0)$.

**Dark matter ratio.** $r = $ (full model logit difference) / (circuit logit difference). Ratio 1.0: circuit fully explains model. Ratio above 1.0: circuit explains less. Convention varies by paper — some use (circuit) / (full model), giving $r < 1$ for incomplete coverage. When circuit logit difference is near zero or negative, the ratio is undefined; report raw logit differences. High ratio may reflect incomplete recovery (hypothesis A) or genuine distribution with $H^1 \neq 0$ (hypothesis B).

**AGOP.** Average Gradient Outer Product. Training-time sensitivity measure. AGOP trajectories often converge to the eventual DAS causal subspace before behavioral detection.

**$W^{KQ}$.** The key-query product matrix for an attention head: $W^{KQ} = (W^K)^\top W^Q \in \mathbb{R}^{d \times d}$, where $W^K$ and $W^Q$ are the key and query weight matrices. The attention logit from position $i$ to $j$ is $x_i^\top W^{KQ} x_j$ (up to scaling). Convention follows Elhage et al. (2021).

**Composition score.** The Q-composition score for heads $u$ (writer) and $v$ (reader): $\|W^{OV}_u \cdot W^{KQ}_v\|_F$. Measures how much $u$'s output influences which positions $v$ attends to. The K-composition score ($\|W^{OV}_u \cdot W^{KQ\top}_v\|_F$) and V-composition score ($\|W^{OV}_u\|_F \cdot \|W^{OV}_v W^{KQ}_u\|_F / \ldots$) measure different information-flow paths. When the site refers to "composition score" without qualification, it means the Q-composition score. All variants are distribution-free upper bounds on causal information flow.

**Multi-domain triangulation.** Each evidence domain (weight-space, activation-space, dynamics-space) is individually non-injective on mechanism space: two distinct mechanisms can look identical in one domain. Convergent evidence across domains is required for unambiguous identification. The joint map across all three domains is injective for mechanisms that differ in at least one domain — a condition that is plausible for natural mechanisms but not formally verified.

**Qua-problem.** Identity claims are only well-formed relative to a description level. The structural view's choice of gauge orbit as the identity criterion is a response: gauge orbits are the minimal equivalence class eliminating purely representational variation, given the goal of characterizing computation.

**MechVal.** Mechanistic Validity: 27 criteria across 5 validity lenses, 5-tier evidence taxonomy. Tier assignments are view-relative.

**Mechanistic stance.** $\sigma = (O, I, E, F, T)$. Axes: metaphysical (O, I), epistemological (E), representational (F), scope (T).

**Five-axis taxonomy.** The categories are distinct: ontology and identity are metaphysical (what exists and when it is the same); evidence is epistemological (how we know); formalism is representational (how we express it); target is scope (what phenomenon the claim is about). Axes in different categories can be varied independently.

**Stratified structural realism.** Working hypothesis: mechanisms occupy strata in $\mathcal{M}$, with stratum-appropriate identity criteria and three-domain triangulation. Whitney stratification established for finite Grassmannian strata at generic points; $\mathcal{M}_\infty$ stratum is a working hypothesis.
