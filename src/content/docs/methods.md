---
title: Methods
---

# Methods

Common interpretability methods are not view-neutral. Each carries implicit axis commitments.

## Five-axis classification

Each method carries implicit commitments across all five axes. Method links provided from [learnmechinterp.com](https://learnmechinterp.com).

| Method | Ontology | Identity (${\sim}$) | Evidence | Formalism | Target |
|---|---|---|---|---|---|
| [Activation patching](https://learnmechinterp.com/topics/activation-patching/) | [Object](/views/object/) | Component overlap | Activations | [Directed graph](/formalism/directed-graph/) | Task circuit |
| [Path patching](https://learnmechinterp.com/topics/activation-patching/#path-patching) | [Object](/views/object/) | Component overlap | Activations | [Directed graph](/formalism/directed-graph/) | Task circuit |
| [ACDC](https://learnmechinterp.com/topics/attribution-patching/) | [Object](/views/object/) | Component overlap | Activations | [Directed graph](/formalism/directed-graph/) | Task circuit |
| [EAP](https://learnmechinterp.com/topics/attribution-patching/) | [Object](/views/object/) | Component overlap | Activations + Weights | [Directed graph](/formalism/directed-graph/) | Task circuit |
| [Ablation](https://learnmechinterp.com/topics/activation-patching/) | [Object](/views/object/) | Component overlap | Activations | [Directed graph](/formalism/directed-graph/) | Importance |
| [DAS / IIA](https://learnmechinterp.com/topics/causal-abstraction/) | [Role](/views/role/) | Role equivalence | Activations | [Causal graph](/formalism/causal-graph/) | Concept |
| [Causal scrubbing](https://learnmechinterp.com/topics/causal-abstraction/) | [Role](/views/role/) | Role equivalence | Activations | [Causal graph](/formalism/causal-graph/) | Alignment |
| [Linear probing](https://learnmechinterp.com/topics/probing-classifiers/) | [Role](/views/role/) | Role equivalence | Activations | [Linear classifier](/formalism/linear-classifier/) | Detection |
| [SAE features](https://learnmechinterp.com/topics/sparse-autoencoders/) | [Object](/views/object/) | Component overlap | Activations | [Dictionary](/formalism/dictionary/) | Feature catalog |
| [Logit / tuned lens](https://learnmechinterp.com/topics/logit-lens-and-tuned-lens/) | [Object](/views/object/) | Component overlap | Activations | [Linear projection](/formalism/linear-projection/) | Layer readout |
| [SVD of weights](https://learnmechinterp.com/topics/qk-ov-circuits/) | [Subspace](/views/subspace/) | Subspace proximity | Weights | [Grassmannian $\mathrm{Gr}(k,d)$](/formalism/grassmannian/) | Decomposition |
| [Composition scores](https://learnmechinterp.com/topics/composition-and-virtual-heads/) | [Structural](/views/structural/) | Gauge orbit | Weights | [Fiber bundle quotient](/formalism/fiber-bundle-quotient/) | Info-flow bound |
| [AGOP](https://arxiv.org/abs/2110.04005) | [Process](/views/process/) | Basin membership | Dynamics | [Dynamical system](/formalism/dynamical-system/) | Trajectory |

<!-- TODO: add back once published
| Factorization | [Subspace](/views/subspace/) | Subspace proximity | Weights | [Grassmannian](/formalism/grassmannian/) | Decomposition |
| Factor EAP | [Subspace](/views/subspace/) | Subspace proximity | Weights + Activations | [Grassmannian](/formalism/grassmannian/) + graph | Task circuit |
-->

![Methods organized by evidence domain and type](/mechanistic-views/figures/methods-evidence-grid.svg)

**Key patterns:**
- Most methods are Object view + activation evidence. The field's default ontology is components (heads, neurons, features).
- DAS uses Subspace *parameterization* but Role *identity* — it validates by interchange intervention success (IIA), not Grassmannian distance. The subspace is the search space, not the ontology.
- The instrumental and perspectival views describe philosophical positions rather than method families. The structural, process, and stratified views are proposed as novel research programs — individual methods touch their territory (composition scores for structural, AGOP for process) but no method fully adopts their ontology.

## Limitations and axis tensions

Each method has practical limitations and, in several cases, internal tensions between the axes — the ontology implies one thing, the formalism or evidence assumes another.

| Method | Evidence domain | Limitation | Axis tension |
|---|---|---|---|
| [Activation patching](https://learnmechinterp.com/topics/activation-patching/) | Activations, interventional | Fails for distributed mechanisms; confounded by backups | — |
| [Path patching](https://learnmechinterp.com/topics/activation-patching/#path-patching) | Activations, interventional | Attribution may be non-unique | — |
| [Ablation](https://learnmechinterp.com/topics/activation-patching/) | Activations, interventional | Overestimates role when backups exist | — |
| [EAP](https://learnmechinterp.com/topics/attribution-patching/) | Activations + Weights, interventional | Gradient approximation; may miss nonlinear effects | — |
| [DAS / IIA](https://learnmechinterp.com/topics/causal-abstraction/) | Activations, interventional | Linearity assumption; IIA tests surgical intervention quality | Searches over subspaces ([Grassmannian](/formalism/grassmannian/)) but evaluates with IIA ([causal graph](/formalism/causal-graph/) criterion) — the search formalism and the evaluation formalism operate at different levels |
| [Causal scrubbing](https://learnmechinterp.com/topics/causal-abstraction/) | Activations, interventional | Result depends on the pre-specified causal graph | — |
| [Linear probing](https://learnmechinterp.com/topics/probing-classifiers/) | Activations, observational | Non-causal; high accuracy does not establish causal role | Formalism ([linear classifier](/formalism/linear-classifier/)) tests linear accessibility, but conclusions are stated as role claims — accessibility does not establish use |
| [SAE features](https://learnmechinterp.com/topics/sparse-autoencoders/) | Activations, observational | Sparse reconstruction criterion is not a causal criterion; feature splitting complicates identity | [Dictionary](/formalism/dictionary/) optimizes reconstruction, but features are interpreted as components ([object view](/views/object/)) — bridged only by independent causal validation |
| [Logit / tuned lens](https://learnmechinterp.com/topics/logit-lens-and-tuned-lens/) | Activations, observational | Observational only | [Linear projection](/formalism/linear-projection/) shows what is decodable at each layer, but conclusions are stated about specific layers ([object-level](/views/object/)) — presence does not establish causal role |
| [SVD of weights](https://learnmechinterp.com/topics/qk-ov-circuits/) | Weights, observational | SVD subspace is not necessarily the causal subspace | — |
| [Composition scores](https://learnmechinterp.com/topics/composition-and-virtual-heads/) | Weights, observational | Upper bound only; does not confirm edge is causally active | Presented as [structural-view](/views/structural/) evidence, but invariant only under head permutations, not the full gauge group — partial invariance, not full |
| [AGOP](https://arxiv.org/abs/2110.04005) | Dynamics, observational | Tracks task sensitivity; convergence to causal subspace is conjecture | — |

## Cross-cutting observations

**No single method suffices.** Each evidence domain is individually non-injective on mechanism space: two distinct mechanisms can look identical in any one domain.

**Activation-space methods are jointly limited.** Activation patching, path patching, ablation, DAS, and EAP all belong to the activation-space domain. They have correlated failure modes. Treating two activation-space methods as independent triangulation is weaker than using activation-space plus weight-space.

**Weight-space methods are more portable.** SVD, composition scores, and invariant subspace analysis operate on weights, which exist before any prompt. Weight-domain evidence is invariant to prompt distribution and more directly comparable across architectures.

**IIA bears on both intervention quality and causal graph validity.** Low IIA has two distinct interpretations: (A) the subspace swap is non-surgical and disturbs other variables, or (B) the proposed causal graph is wrong and changing this variable *should* change downstream behavior. These require different responses. See the [Subspace View](/views/subspace/) page.

Note: for per-view triangulation method requirements, see [Mechanistic Validity Interface](/mechval-interface/#minimal-triangulation-for-tier-3).

## Statistical caveats

The evidence standards described on this site are qualitative. The following formal statistical problems are currently underdeveloped in the mechanistic interpretability literature and should be kept in mind when evaluating claims.

**Effect sizes and thresholds.** IIA of 0.8 vs 0.9, a composition score of 0.12 vs 0.08, a Fréchet variance of 0.04 vs 0.07 — the field lacks agreed null distributions and agreed thresholds for what constitutes meaningful evidence. Current practice is to eyeball these numbers and compare within a study. Cross-study comparison is unreliable.

**Multiple comparisons.** Circuit-finding procedures search over large spaces of candidate components and edges. Without correction for the number of tests performed, false positives are expected. Studies that identify 26 heads in 7 classes from an initial sweep of all heads in GPT-2 Small should be interpreted with this in mind; the reported circuit is a hypothesis, not a validated causal structure.

**Power analysis.** Activation patching and ablation results are sensitive to the prompt distribution used. Whether the observed effect would replicate on a different distribution of the same task, a paraphrase, or a cross-lingual version is usually not reported. Tier 3–4 claims require cross-distribution robustness; Tier 1–2 claims may not.

**Convergence vs consistency.** "Convergent evidence from three methods" is stronger than one method, but only if the methods are genuinely independent — which they may not be if they share the same prompt distribution, the same model forward pass, or the same implicit linearity assumption. The triangulation requirement is a principle; whether any specific combination of methods satisfies it in practice requires case-by-case examination.

These are not objections to the field; they are known open problems. Interpretability is in an early phase where establishing the existence of phenomena matters more than formal power analysis. As the field matures, the quantitative standards will need to tighten.
