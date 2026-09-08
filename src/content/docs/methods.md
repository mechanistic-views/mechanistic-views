---
title: Methods
---

# Methods

Common interpretability methods are not view-neutral. Each carries implicit axis commitments.

## Five-axis classification

Each method carries implicit commitments across all five axes. Method links provided from [learnmechinterp.com](https://learnmechinterp.com).

| Method | Ontology | Identity (${\sim}$) | Evidence | Formalism | Target |
|---|---|---|---|---|---|
| [Activation patching](/mechanistic-views/glossary/#activation-patching) | [Object](/mechanistic-views/views/object/) | Component overlap | Activations | [Directed graph](/mechanistic-views/formalism/directed-graph/) | Task circuit |
| [Path patching](/mechanistic-views/glossary/#path-patching) | [Object](/mechanistic-views/views/object/) | Component overlap | Activations | [Directed graph](/mechanistic-views/formalism/directed-graph/) | Task circuit |
| [ACDC](/mechanistic-views/glossary/#attribution-patching) | [Object](/mechanistic-views/views/object/) | Component overlap | Activations | [Directed graph](/mechanistic-views/formalism/directed-graph/) | Task circuit |
| [EAP](/mechanistic-views/glossary/#attribution-patching) | [Object](/mechanistic-views/views/object/) | Component overlap | Activations + Weights | [Directed graph](/mechanistic-views/formalism/directed-graph/) | Task circuit |
| [Ablation](/mechanistic-views/glossary/#activation-patching) | [Object](/mechanistic-views/views/object/) | Component overlap | Activations | [Directed graph](/mechanistic-views/formalism/directed-graph/) | Importance |
| [DAS / IIA](/mechanistic-views/glossary/#causal-abstraction) | [Role](/mechanistic-views/views/role/)<sup>†</sup> | Role equivalence | Activations | [Grassmannian $\mathrm{Gr}(k,d)$](/mechanistic-views/formalism/grassmannian/) (borrowed) | Concept |
| [Causal scrubbing](/mechanistic-views/glossary/#causal-abstraction) | [Role](/mechanistic-views/views/role/) | Role equivalence | Activations | [Causal graph](/mechanistic-views/formalism/causal-graph/) | Alignment |
| [Linear probing](/mechanistic-views/glossary/#linear-probing) | [Role](/mechanistic-views/views/role/) | Role equivalence | Activations | [Linear classifier](/mechanistic-views/formalism/linear-classifier/) | Detection |
| [SAE features](/mechanistic-views/glossary/#sae) | [Object](/mechanistic-views/views/object/) | Component overlap | Activations | [Dictionary](/mechanistic-views/formalism/dictionary/) | Feature catalog |
| [Logit / tuned lens](/mechanistic-views/glossary/#logit-lens) | [Object](/mechanistic-views/views/object/) | Component overlap | Activations | [Linear projection](/mechanistic-views/formalism/linear-projection/) | Layer readout |
| [SVD of weights](/mechanistic-views/glossary/#qk-ov-circuits) | [Subspace](/mechanistic-views/views/subspace/) | Subspace proximity | Weights | [Grassmannian $\mathrm{Gr}(k,d)$](/mechanistic-views/formalism/grassmannian/) | Decomposition |
| [Composition scores](/mechanistic-views/glossary/#composition-score) | [Structural](/mechanistic-views/views/structural/) | Gauge orbit | Weights | [Fiber bundle quotient](/mechanistic-views/formalism/fiber-bundle-quotient/) | Info-flow bound |
| AGOP (Radhakrishnan et al.) | [Process](/mechanistic-views/views/process/) | Basin membership | Dynamics | [Dynamical system](/mechanistic-views/formalism/dynamical-system/) | Trajectory |

<!-- TODO: add back once published
| Factorization | [Subspace](/mechanistic-views/views/subspace/) | Subspace proximity | Weights | [Grassmannian](/mechanistic-views/formalism/grassmannian/) | Decomposition |
| Factor EAP | [Subspace](/mechanistic-views/views/subspace/) | Subspace proximity | Weights + Activations | [Grassmannian](/mechanistic-views/formalism/grassmannian/) + graph | Task circuit |
-->

![Methods organized by evidence domain and type](/mechanistic-views/figures/methods-evidence-grid.svg)

**Key patterns:**
- Most methods are Object view + activation evidence. The field's default ontology is components (heads, neurons, features).
- DAS uses Subspace *parameterization* but Role *identity* — it validates by interchange intervention success (IIA), not Grassmannian distance. The subspace is the search space, not the ontology.
- Six views are descriptive — object, role, subspace, process, instrumental, contrastive — characterizing commitments already operative in published work. Three are programmatic — structural, stratified, perspectival — articulating views implicit in emerging directions without widely adopted methods. No widely used method operates in the stratified or perspectival views; composition scores reach structural territory and AGOP reaches process territory.

## Limitations and axis tensions

Each method has practical limitations and, in several cases, internal tensions between the axes — the ontology implies one thing, the formalism or evidence assumes another.

| Method | Evidence domain | Limitation | Axis tension |
|---|---|---|---|
| [Activation patching](/mechanistic-views/glossary/#activation-patching) | Activations, interventional | Fails for distributed mechanisms; confounded by backups | — |
| [Path patching](/mechanistic-views/glossary/#path-patching) | Activations, interventional | Attribution may be non-unique | — |
| [Ablation](/mechanistic-views/glossary/#activation-patching) | Activations, interventional | Overestimates role when backups exist | — |
| [EAP](/mechanistic-views/glossary/#attribution-patching) | Activations + Weights, interventional | Gradient approximation; may miss nonlinear effects | — |
| [DAS / IIA](/mechanistic-views/glossary/#causal-abstraction) | Activations, interventional | Linearity assumption; IIA tests surgical intervention quality | Searches over subspaces ([Grassmannian](/mechanistic-views/formalism/grassmannian/)) but evaluates with IIA ([causal graph](/mechanistic-views/formalism/causal-graph/) criterion) — the search formalism and the evaluation formalism operate at different levels |
| [Causal scrubbing](/mechanistic-views/glossary/#causal-abstraction) | Activations, interventional | Result depends on the pre-specified causal graph | — |
| [Linear probing](/mechanistic-views/glossary/#linear-probing) | Activations, observational | Non-causal; high accuracy does not establish causal role | Formalism ([linear classifier](/mechanistic-views/formalism/linear-classifier/)) tests linear accessibility, but conclusions are stated as role claims — accessibility does not establish use |
| [SAE features](/mechanistic-views/glossary/#sae) | Activations, observational | Sparse reconstruction criterion is not a causal criterion; feature splitting complicates identity | [Dictionary](/mechanistic-views/formalism/dictionary/) optimizes reconstruction, but features are interpreted as components ([object view](/mechanistic-views/views/object/)) — bridged only by independent causal validation |
| [Logit / tuned lens](/mechanistic-views/glossary/#logit-lens) | Activations, observational | Observational only | [Linear projection](/mechanistic-views/formalism/linear-projection/) shows what is decodable at each layer, but conclusions are stated about specific layers ([object-level](/mechanistic-views/views/object/)) — presence does not establish causal role |
| [SVD of weights](/mechanistic-views/glossary/#qk-ov-circuits) | Weights, observational | SVD subspace is not necessarily the causal subspace | — |
| [Composition scores](/mechanistic-views/glossary/#composition-score) | Weights, observational | Upper bound only; does not confirm edge is causally active | Presented as [structural-view](/mechanistic-views/views/structural/) evidence, but invariant only under head permutations, not the full gauge group — partial invariance, not full |
| AGOP (Radhakrishnan et al.) | Dynamics, observational | Tracks task sensitivity; convergence to causal subspace is conjecture | — |

## Cross-cutting observations

**No single method suffices.** Each evidence domain is individually non-injective on mechanism space: two distinct mechanisms can look identical in any one domain.

**Activation-space methods are jointly limited.** Activation patching, path patching, ablation, DAS, and EAP all belong to the activation-space domain. They have correlated failure modes. Treating two activation-space methods as independent triangulation is weaker than using activation-space plus weight-space.

**Weight-space methods are more portable.** SVD, composition scores, and invariant subspace analysis operate on weights, which exist before any prompt. Weight-domain evidence is invariant to prompt distribution and more directly comparable across architectures.

**IIA bears on both intervention quality and causal graph validity.** Low IIA has two distinct interpretations: (A) the subspace swap is non-surgical and disturbs other variables, or (B) the proposed causal graph is wrong and changing this variable *should* change downstream behavior. These require different responses. See the [Subspace View](/mechanistic-views/views/subspace/) page.

Note: for per-view triangulation method requirements, see [Mechanistic Validity Interface](/mechanistic-views/mechval-interface/#minimal-triangulation-for-tier-3).

## Statistical caveats

The evidence standards described on this site are qualitative. The following formal statistical problems are currently underdeveloped in the mechanistic interpretability literature and should be kept in mind when evaluating claims.

**Effect sizes and thresholds.** IIA of 0.8 vs 0.9, a composition score of 0.12 vs 0.08, a Fréchet variance of 0.04 vs 0.07 — the field lacks agreed null distributions and agreed thresholds for what constitutes meaningful evidence. Current practice is to eyeball these numbers and compare within a study. Cross-study comparison is unreliable.

**Multiple comparisons.** Circuit-finding procedures search over large spaces of candidate components and edges. Without correction for the number of tests performed, false positives are expected. Studies that identify 26 heads in 7 classes from an initial sweep of all heads in GPT-2 Small should be interpreted with this in mind; the reported circuit is a hypothesis, not a validated causal structure.

**Power analysis.** Activation patching and ablation results are sensitive to the prompt distribution used. Whether the observed effect would replicate on a different distribution of the same task, a paraphrase, or a cross-lingual version is usually not reported. Tier 3–4 claims require cross-distribution robustness; Tier 1–2 claims may not.

**Convergence vs consistency.** "Convergent evidence from three methods" is stronger than one method, but only if the methods are genuinely independent — which they may not be if they share the same prompt distribution, the same model forward pass, or the same implicit linearity assumption. The triangulation requirement is a principle; whether any specific combination of methods satisfies it in practice requires case-by-case examination.

These are not objections to the field; they are known open problems. Interpretability is in an early phase where establishing the existence of phenomena matters more than formal power analysis. As the field matures, the quantitative standards will need to tighten.
