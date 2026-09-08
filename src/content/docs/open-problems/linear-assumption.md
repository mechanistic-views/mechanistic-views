---
title: "Linear Assumption"
---

# Is linear structure real?

Most mechanistic interpretability methods assume that concepts are encoded as linear directions in activation space. Linear probes search for hyperplanes that separate concept A from concept B. SAEs decompose activations into sparse linear combinations of feature directions. DAS (Distributed Alignment Search) finds linear subspaces that align with causal variables. Activation steering adds or subtracts a direction to control behavior. The entire toolkit assumes linearity.

Engels et al. (2024) showed this assumption can be wrong. Days of the week form a circle in activation space, not a line — Monday is close to both Sunday and Tuesday, and the representation wraps around. Months form a similar ring. Color is represented on a three-dimensional manifold. These are not exotic edge cases, but which concepts are linear and which are not remains open (Anwar et al. 2024), so the ceiling is prospective: the view may meet it, and has not yet hit it. If you apply a linear probe to a circular representation, you get a line that cuts through the circle — a flat projection of curved structure that captures some but not all of the information, and may be misleading about what information is actually there.

The problem extends beyond probes. DAS finds subspaces even in random models. Sutter et al. (2025) showed that unrestricted nonlinear alignment achieves 100% IIA on randomly initialized models, making DAS vacuous without structural constraints on the alignment class — the "subspace" is then an artifact of the optimization's degrees of freedom rather than evidence that the concept is linearly represented. Subspace-view claims therefore require either linear alignment or alignment constrained to respect the transport structure induced by the weight matrices, and the eigenvalue gap reported alongside.

## The view confusion

This is a [Subspace view](/mechanistic-views/views/subspace/) ceiling — the formalism assumes linear subspaces, and some concepts appear to be encoded otherwise — and a vindication of the [Perspectival view's](/mechanistic-views/views/perspectival/) core warning.

Linear probes find linear structure because they can only find linear structure. SAEs decompose into linear directions because that's what SAEs do. DAS finds linear subspaces because that's what it optimizes for. The Perspectival view says: what you find depends on your method, and the method's assumptions constrain the findings. When every tool in your toolkit assumes linearity, everything looks linear — even circles.

The Subspace view is not inherently linear; the Grassmannian $\mathrm{Gr}(k,d)$ is itself a curved manifold, and paths on it can track how a representation's subspace rotates across layers or training steps. But every point on the Grassmannian is a *linear* subspace of the ambient activation space, and all standard methods (DAS, linear probes, SAEs) restrict to linear structure. Extending the Subspace view to nonlinear representations — finding circles, manifolds, and curved subspaces within activation space — is an open methodological challenge, not a conceptual one.

## Mechanistic validity impact

| Criterion | Status | Why |
|---|---|---|
| [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability) | **Violated** — if "concept = direction" is wrong, the operationalization is wrong | The concept is defined as a direction, but the real representation may be a manifold |
| [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance/) | **Violated** — different linear projections of a circle give different "directions" | The direction you find depends on which part of the circle your data samples |
| [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | **Violated** — DAS in random models means the method can't discriminate real from absent structure | A method that always finds something cannot distinguish "found real structure" from "found nothing" |
| [I4 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control/) | **Violated** — optimization freedom in DAS is an uncontrolled confound | The subspace found by DAS may reflect optimization dynamics, not model structure |

The fix is methodological: nonlinear representation discovery (circles, manifolds), proper random baselines for DAS, and methods that test whether the linear assumption holds before relying on it. These are active research directions but not yet standard practice.

## Resolution status: **Scoped**

Circular and manifold representations challenge the assumption that concepts are encoded as linear directions. This is a Subspace-view ceiling: the formalism assumes linear subspaces, and some concepts appear to be encoded otherwise. Which concepts are linear and which are not remains open (Anwar et al. 2024), so the ceiling is prospective — the view may meet it, and has not yet hit it.

## Sources

- **Sharkey et al. (2025)** §2.1.2: Linear representation assumption may not hold ([arXiv:2501.16496](https://arxiv.org/abs/2501.16496))
- **Engels et al. (2024)**: Not all language model features are linear
- **Sutter et al. (2025)**: The non-linear representation dilemma — is causal abstraction enough for mechanistic interpretability? ([NeurIPS 2025](https://arxiv.org/abs/2507.08802))
- **Park et al. (2023)**: The linear representation hypothesis
- **Geiger et al. (2024)**: DAS / Boundless DAS / causal abstraction with linear subspaces
- **Nanda (2022)** §4: Superposition and polysemanticity ([200 Open Problems](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability))
