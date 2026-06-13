---
title: "Cross-Model Identity"
---

# Are features universal?

Multiple groups have claimed to find "the same features" across different models. Convergent results across model scales, random seeds, and even architectures are cited as evidence that neural networks learn universal representations — that there are fundamental computational primitives the same way that chemistry has elements. If true, this would be one of the most important findings in the field. But "the same" is doing a lot of work in these claims, and the identity criterion is almost never stated.

When two models trained from different random seeds both have a feature that activates on Python code, are they "the same feature"? It depends on what you mean:

- **Same top-activating examples** (Instrumental): The features predict the same inputs. But many different features could predict "Python code" — this is a very weak identity criterion.
- **Same ablation effect** (Object): Ablating both features degrades the same behavior by the same amount. Stronger, but component identity is architecture-dependent — a 12-layer model and a 24-layer model have different components.
- **Same subspace** (Subspace): The features span the same geometric region of representation space, measured by Grassmannian distance. This is architecture-independent — subspaces can be compared across models via CKA, RSA, or Procrustes alignment.
- **Same gauge orbit** (Structural): The features occupy the same position in the space of computations modulo symmetry. The strongest criterion, and the hardest to test.

Most current universality claims operate at the Instrumental level (same top-activating examples) while drawing conclusions at the Structural level ("networks learn the same computation"). The evidence and conclusion are separated by three view levels.

## The view ceiling

Cross-model identity is structurally **impossible** under the [Object view](/mechanistic-views/views/object/). Object identity is defined by component overlap — the same attention heads, the same neurons. But different architectures have different components, so there is no basis for comparison. This is not a limitation of current methods; it's a logical consequence of defining mechanisms as concrete parts.

The [Role view](/mechanistic-views/views/role/) makes cross-model identity **possible** — two components in different models can fill the same functional role (both are "name movers" or "induction heads"). The [Subspace view](/mechanistic-views/views/subspace/) makes it **measurable** — subspace distance is defined for any pair of models with the same input space, regardless of architecture.

This is the [E6 Cross-architecture generalization](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture/) criterion: can your mechanistic description transfer across architectures? It's impossible at Object, possible at Role, measurable at Subspace, and natural at Structural. The current universality literature mostly operates at Object while claiming Structural results.

## Mechanistic validity impact

| Criterion | Object view | Role view | Subspace view |
|---|---|---|---|
| [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture/) | **Impossible** | Possible (same role) | Covered (Grassmannian distance) |
| [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance/) | **Impossible** (basis-dependent) | Possible (role is basis-independent) | Covered (subspace is basis-independent) |
| [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/) | Fails across methods | Possible if roles converge | Testable via cross-method subspace overlap |
| [E4 Model scale](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/model-scale/) | Components change with scale | Roles may persist | Subspaces may persist (testable) |

## Sources

- **Nanda (2022)** §5.32, §5.34, §9.53, §9.54: Feature universality across seeds and architectures ([200 Open Problems](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability))
- **Sharkey et al. (2026)** §3.6: Cross-architecture MI ([arXiv:2501.16496](https://arxiv.org/abs/2501.16496))
- **Li et al. (2015)**: Convergent learning — do different neural networks learn the same representations?
- **Morcos et al. (2018)**: Insights on representational similarity in neural networks with canonical correlation
- **Bansal et al. (2021)**: Revisiting model stitching to compare neural representations
