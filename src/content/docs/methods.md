---
title: Methods
---

# Methods

Common interpretability methods are not view-neutral. Each carries implicit axis commitments.

## Method-to-view mapping

| Method | Ontology implied | Identity implied | Evidence domain | Key limitations |
|---|---|---|---|---|
| Activation patching | Object or role | Component overlap | Activation-space, interventional | Fails for distributed mechanisms; confounded by backups |
| Path patching | Object or role | Path-level components | Activation-space, interventional | Attribution may be non-unique |
| Ablation / mean-ablation | Object | Component inclusion | Activation-space, interventional | Overestimates role when backups exist |
| DAS / IIA | Subspace | Subspace up to rotation | Activation-space, interventional | Linearity assumption; IIA tests surgical intervention quality |
| SAE features | Object (sparse) / Subspace ($\mathcal{M}_1$) | Feature overlap, cosine similarity, or IIA (if causally validated) | Activation-space, observational | Sparse reconstruction criterion ≠ causal criterion; features may not be causally active; feature splitting complicates identity |
| SVD of weight matrices | Subspace or structural | Principal angles | Weight-space, observational | SVD subspace ≠ causal subspace without further validation |
| Composition scores | Structural (permutation-invariant only) | Information-flow bound | Weight-space, observational | Upper bound only; does not confirm edge is causally active; invariant under head permutations but not under orthogonal rotations |
| Linear probing | Subspace (weak) | Feature presence | Activation-space, observational | Non-causal; high accuracy ≠ causal role |
| Causal scrubbing | Role or subspace | Causal abstraction alignment | Activation-space, interventional | Requires pre-specified causal graph; result depends on it |
| AGOP / gradient sensitivity | Process | Gradient subspace convergence | Dynamics-space, observational | Tracks task sensitivity; convergence to causal subspace is conjecture |
| Interchange interventions | Subspace | Subspace coincidence via DAS | Activation-space, interventional | Susceptible to Sutter et al. (2025) vacuity for unrestricted alignment; G-SCM (transport-respecting alignment) addresses this |
| Logit lens / tuned lens | Subspace or object | Layer-level representation | Activation-space, observational | Observational only |
| Edge attribution patching | Object or role | Edge-level components | Activation-space, interventional | Gradient approximation; may miss nonlinear effects |

## Key observations

**No single method suffices.** Each evidence domain is individually non-injective on mechanism space: two distinct mechanisms can look identical in any one domain.

**Activation-space methods are jointly limited.** Activation patching, path patching, ablation, DAS, and EAP all belong to the activation-space domain. They have correlated failure modes. Treating two activation-space methods as independent triangulation is weaker than using activation-space plus weight-space.

**Weight-space methods are more portable.** SVD, composition scores, and invariant subspace analysis operate on weights, which exist before any prompt. Weight-domain evidence is invariant to prompt distribution and more directly comparable across architectures.

**DAS/IIA requires a view commitment.** DAS identifies a subspace up to rotation — the subspace view's identity criterion. Applying DAS while implicitly holding the object view creates a mismatch.

**IIA bears on both intervention quality and causal graph validity.** Low IIA has two distinct interpretations: (A) the subspace swap is non-surgical and disturbs other variables, or (B) the proposed causal graph is wrong and changing this variable *should* change downstream behavior. These require different responses. See the [Subspace View](views/subspace/) page.

## Minimal triangulation for Tier 3 (subspace view)

1. **Activation-space interventional**: DAS/IIA with IIA reported and interpreted as surgical-intervention quality
2. **Weight-space structural**: SVD or composition score analysis showing the subspace is latent in weights
3. **At least one of**: dynamics-space evidence (AGOP convergence), cross-seed consistency, or cross-architecture transfer

Two of the three domains alone leaves an identifiability gap.

## Statistical caveats

The evidence standards described on this site are qualitative. The following formal statistical problems are currently underdeveloped in the mechanistic interpretability literature and should be kept in mind when evaluating claims.

**Effect sizes and thresholds.** IIA of 0.8 vs 0.9, a composition score of 0.12 vs 0.08, a Fréchet variance of 0.04 vs 0.07 — the field lacks agreed null distributions and agreed thresholds for what constitutes meaningful evidence. Current practice is to eyeball these numbers and compare within a study. Cross-study comparison is unreliable.

**Multiple comparisons.** Circuit-finding procedures search over large spaces of candidate components and edges. Without correction for the number of tests performed, false positives are expected. Studies that identify 26 heads in 7 classes from an initial sweep of all heads in GPT-2 Small should be interpreted with this in mind; the reported circuit is a hypothesis, not a validated causal structure.

**Power analysis.** Activation patching and ablation results are sensitive to the prompt distribution used. Whether the observed effect would replicate on a different distribution of the same task, a paraphrase, or a cross-lingual version is usually not reported. Tier 3–4 claims require cross-distribution robustness; Tier 1–2 claims may not.

**Convergence vs consistency.** "Convergent evidence from three methods" is stronger than one method, but only if the methods are genuinely independent — which they may not be if they share the same prompt distribution, the same model forward pass, or the same implicit linearity assumption. The triangulation requirement is a principle; whether any specific combination of methods satisfies it in practice requires case-by-case examination.

These are not objections to the field; they are known open problems. Interpretability is in an early phase where establishing the existence of phenomena matters more than formal power analysis. As the field matures, the quantitative standards will need to tighten.
