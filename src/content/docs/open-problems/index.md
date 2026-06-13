---
title: Open Problem Map
---

# Open Problem Map


[Do SAEs recover the "true" features](/mechanistic-views/open-problems/sae-true-features/)? [Is chain-of-thought faithful to the model's reasoning](/mechanistic-views/open-problems/cot-faithfulness/)? [Do probes find features the model actually uses](/mechanistic-views/open-problems/probe-features/)? These are usually treated as empirical questions — run the experiment, get the answer. But each contains a hidden assumption: what "true" means, what "faithful" means, what "uses" means. Different [views](/mechanistic-views/views/) define these differently, and we find that disagreements in the literature often reflect unstated view commitments rather than conflicting experimental results.

We distilled 24 distinct problem types from [nine sources](#sources) spanning hundreds of individual open questions. The foundational ones — why methods disagree, what evidence can establish, when findings are the same — dissolve, reframe, or sharpen when you name the view. The methods-level ones turn out to require foundational clarity before they can be answered. Each maps onto specific [Mechanistic Validity](https://mechanistic-validity.github.io/mechanistic-validity/) criteria being violated or neglected.

Of the 24 problems: 11 are **dissolved** (the question was ill-posed — it disappears when you name the view), 2 are **reframed** (the framework clarifies what evidence would answer it), and 11 are **scoped** (the framework identifies which view owns the problem and why current methods hit a ceiling). Zero are unaddressed.

## Problem map

| Page | Problem | The confusion | Views involved | Status |
|---|---|---|---|---|
| [Decomposition identity](/mechanistic-views/open-problems/decomposition-identity/) | SAE features change with width | Which decomposition is "real"? | [Object](/mechanistic-views/views/object/) vs. [Subspace](/mechanistic-views/views/subspace/) | Dissolved |
| [Decomposition identity](/mechanistic-views/open-problems/decomposition-identity/) | SAEs find features in noise | Method artifact or real structure? | [Object](/mechanistic-views/views/object/) vs. [Perspectival](/mechanistic-views/views/perspectival/) | Dissolved |
| [SAE "true" features](/mechanistic-views/open-problems/sae-true-features/) | Do SAEs recover the "true" features? | "True" depends on the view | [Object](/mechanistic-views/views/object/) vs. [Subspace](/mechanistic-views/views/subspace/) vs. [Perspectival](/mechanistic-views/views/perspectival/) | Dissolved |
| [Superposition](/mechanistic-views/open-problems/superposition/) | How do models represent more features than dimensions? | Problem, property, or presupposition? | [Object](/mechanistic-views/views/object/) vs. [Subspace](/mechanistic-views/views/subspace/) vs. [Structural](/mechanistic-views/views/structural/) | Dissolved |
| [Circuit disagreements](/mechanistic-views/open-problems/circuit-disagreements/) | ACDC vs. EAP vs. patching disagree | Which circuit is correct? | [Object](/mechanistic-views/views/object/) vs. [Role](/mechanistic-views/views/role/) | Dissolved |
| [Circuit disagreements](/mechanistic-views/open-problems/circuit-disagreements/) | Circuit size varies by method | Sparse or dense? | [Object](/mechanistic-views/views/object/) vs. [Role](/mechanistic-views/views/role/) | Dissolved |
| [Unit of analysis](/mechanistic-views/open-problems/unit-of-analysis/) | Are attention heads the right unit? | Unit depends on the claim | [Object](/mechanistic-views/views/object/) vs. [Role](/mechanistic-views/views/role/) vs. [Subspace](/mechanistic-views/views/subspace/) | Dissolved |
| [Intervention limits](/mechanistic-views/open-problems/intervention-limits/) | Ablation triggers reconfiguration | Ablation reveals function or breaks it? | [Object](/mechanistic-views/views/object/) ceiling | Scoped |
| [Intervention limits](/mechanistic-views/open-problems/intervention-limits/) | Interventions have side effects | Targeted edit or collateral damage? | [Object](/mechanistic-views/views/object/) ceiling | Scoped |
| [Linear assumption](/mechanistic-views/open-problems/linear-assumption/) | Concepts form circles, not lines | Is linear structure real? | [Subspace](/mechanistic-views/views/subspace/) ceiling, [Perspectival](/mechanistic-views/views/perspectival/) critique | Scoped |
| [Linear assumption](/mechanistic-views/open-problems/linear-assumption/) | DAS finds subspaces in random models | Real subspace or optimization artifact? | [Subspace](/mechanistic-views/views/subspace/) vs. [Perspectival](/mechanistic-views/views/perspectival/) | Dissolved |
| [Probe features](/mechanistic-views/open-problems/probe-features/) | Do probes find features the model uses? | "Uses" means different things | [Instrumental](/mechanistic-views/views/instrumental/) vs. [Subspace](/mechanistic-views/views/subspace/) vs. [Role](/mechanistic-views/views/role/) | Dissolved |
| [Safety evidence gaps](/mechanistic-views/open-problems/safety-evidence-gaps/) | "Refusal direction" = refusal mechanism? | Lever or mechanism? | [Instrumental](/mechanistic-views/views/instrumental/) floor | Scoped |
| [Safety evidence gaps](/mechanistic-views/open-problems/safety-evidence-gaps/) | Truthfulness steering doesn't transfer | Domain-specific or general mechanism? | [Instrumental](/mechanistic-views/views/instrumental/) vs. [Subspace](/mechanistic-views/views/subspace/) | Scoped |
| [Cross-model identity](/mechanistic-views/open-problems/cross-model-identity/) | "Same features" across models | Same by what criterion? | [Object](/mechanistic-views/views/object/) impossible, [Subspace](/mechanistic-views/views/subspace/) possible | Dissolved |
| [CoT faithfulness](/mechanistic-views/open-problems/cot-faithfulness/) | Is CoT faithful to internal reasoning? | "Faithful" means four things | [Instrumental](/mechanistic-views/views/instrumental/) vs. [Perspectival](/mechanistic-views/views/perspectival/) vs. [Structural](/mechanistic-views/views/structural/) | Reframed |
| [Validation methodology](/mechanistic-views/open-problems/validation-methodology/) | Validation on discovery data | Circular evidence? | [Perspectival](/mechanistic-views/views/perspectival/) diagnosis | Scoped |
| [Validation methodology](/mechanistic-views/open-problems/validation-methodology/) | Interpretability illusions | Real feature or distribution artifact? | [Perspectival](/mechanistic-views/views/perspectival/) diagnosis | Scoped |
| [Training dynamics](/mechanistic-views/open-problems/training-dynamics/) | Fine-tuning destroys circuits | Robust mechanism or fragile artifact? | [Process](/mechanistic-views/views/process/) territory | Scoped |
| [Training dynamics](/mechanistic-views/open-problems/training-dynamics/) | Phase transitions create mechanisms | When does it form? | [Process](/mechanistic-views/views/process/) territory | Scoped |
| [Resolution & completeness](/mechanistic-views/open-problems/resolution-completeness/) | "Dark matter" — unexplained behavior | How much do we understand? | [Stratified](/mechanistic-views/views/stratified/) territory | Scoped |
| [Resolution & completeness](/mechanistic-views/open-problems/resolution-completeness/) | Behavioral propensity ≠ capability | What are we measuring? | [Instrumental](/mechanistic-views/views/instrumental/) vs. [Role](/mechanistic-views/views/role/) | Dissolved |
| [Deceptive alignment](/mechanistic-views/open-problems/deceptive-alignment/) | Can MI detect strategic deception? | Instrumental evidence is structurally insufficient | [Instrumental](/mechanistic-views/views/instrumental/) floor, [Structural](/mechanistic-views/views/structural/) + [Process](/mechanistic-views/views/process/) required | Scoped |
| [World models](/mechanistic-views/open-problems/world-models/) | Do LLMs build internal world models? | Subspace evidence used for Structural claims | [Subspace](/mechanistic-views/views/subspace/) vs. [Structural](/mechanistic-views/views/structural/) | Reframed |

## Resolution status

Each problem has a resolution status indicating how much the framework addresses it:

**Dissolved** — the question was ill-posed: it disappears when you name the view. This does not mean the underlying phenomena aren't real — it means the question as stated conflates different views and therefore has no single answer. Once you specify which view you're in, the question either has a clear answer or becomes a different (better) question. Examples: circuit disagreements, decomposition identity, superposition, the probe wars.

**Reframed** — the framework clarifies what the question actually means and what evidence would answer it, but the empirical question remains open. The conceptual confusion is resolved; the experiment hasn't been run. Example: CoT faithfulness — "faithful" means four different things, and the safety-relevant notion requires evidence no one has collected.

**Scoped** — the framework identifies which view owns the problem, what the evidence standard is, and why current methods hit a ceiling. The problem is real and structural — it requires moving up the commitment ladder or working in a view the field hasn't adopted yet. Examples: intervention limits (Object ceiling), training dynamics (Process territory).

## The pattern

Three types of problem appear:

**View confusions** — the problem dissolves when you name which view you're in. Circuit disagreements, decomposition identity, cross-model identity, superposition, SAE "true" features, the probe wars, and the unit-of-analysis debate are all cases where researchers using different views get different answers and mistake the disagreement for an empirical conflict. It isn't. Different views ask different questions and should give different answers.

**View ceilings** — the problem is real and structural, caused by the limits of the view being used. Intervention limits, the linear assumption, and safety evidence gaps all arise because a view's methods cannot produce the evidence needed for the conclusions being drawn. The fix is to move up the commitment ladder: collect evidence at a higher-commitment view where the criterion is possible rather than impossible.

**View territories** — some problems belong naturally to a specific view that the field hasn't adopted yet. Training dynamics problems belong to the [Process view](/mechanistic-views/views/process/). Resolution problems belong to the [Stratified view](/mechanistic-views/views/stratified/). These aren't confusions — they're under-explored areas of the view space.

## What the framework does and doesn't do

The views framework defines what mechanisms are, what evidence means, and when two mechanisms are the same. It is a framework *about* mechanistic interpretability — it provides evidence standards and ontological commitments. It does not itself do MI research: it doesn't find circuits, train SAEs, or detect deception.

Several prominent "open problems" in MI are methods-level problems rather than foundational problems. The framework already provides the evidence standards for evaluating solutions to them:

| Problem | Why it's not a framework gap | What the framework provides |
|---|---|---|
| **CoT faithfulness** — is chain-of-thought reasoning faithful to internal computation? | This is an empirical question about a specific method | The [Perspectival view](/mechanistic-views/views/perspectival/) already predicts that single-method evidence (including CoT) may be unfaithful. Cross-method convergence is the fix |
| **[Deceptive alignment](/mechanistic-views/open-problems/deceptive-alignment/)** — can MI detect strategic deception? | This is a target-property problem: can methods find a specific thing? | The framework says what evidence level is needed: at minimum [Structural](/mechanistic-views/views/structural/) (gauge-invariant, stable under adversarial pressure) + [Process](/mechanistic-views/views/process/) (survives retraining). [Instrumental](/mechanistic-views/views/instrumental/) evidence (steering vectors) is structurally insufficient. [Full analysis →](/mechanistic-views/open-problems/deceptive-alignment/) |
| **[World models](/mechanistic-views/open-problems/world-models/)** — do LLMs form causal world models? | This is a specific empirical finding to chase, not a framework question | Linear encodings of state predicates are [Subspace](/mechanistic-views/views/subspace/) claims. Whether they form a causal world model is a [Structural](/mechanistic-views/views/structural/) question. [Mechanistic Validity](https://mechanistic-validity.github.io/mechanistic-validity/) E4 (counterfactual validity) is the relevant criterion. [Full analysis →](/mechanistic-views/open-problems/world-models/) |
| **Automated MI at scale** — how do we scale MI to frontier models? | This is engineering, not ontology | The framework provides the evidence standards that automated systems should satisfy — especially [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability/) and [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) (does the automated system find real structure or artifacts?) |
| **Non-transformer architectures** — does MI transfer to SSMs, MoE, etc.? | The framework is architecture-agnostic by design | [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture/) is already a criterion. Whether specific methods (SAEs, DAS) transfer is a methods question |
| **Formal verification of circuits** — can mechanistic claims be deductively verified? | Deductive certainty is complementary to but separate from empirical validity | The framework assesses *empirical* validity. Formal verification provides *deductive* certainty for specific algorithmic claims. Both are useful; they answer different questions |

The one genuine scope boundary is **multi-agent mechanistic interpretability**. The views framework assumes single-model analysis — "mechanism" is defined within one model. Mechanisms that emerge from interaction between models (coordination protocols, collusion strategies) have no natural home in the current view hierarchy. This is a deliberate scope choice (single-model analysis is already hard enough), not an oversight, but it is a real boundary.

## Sources

| Source | Year | Problems | Focus |
|---|---|---|---|
| [Sharkey et al. "Open Problems in MI"](https://arxiv.org/abs/2501.16496) | 2026 | 67 | Comprehensive survey (30 authors) |
| [Nanda "200 Concrete Open Problems"](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability) | 2022 | 200 | Enumerated research questions |
| [Apollo Research project ideas](https://www.alignmentforum.org/posts/KfkpgXdgRheSRWDy8) | 2024 | 45+ | Safety-oriented MI projects |
| [Schmidt Sciences "Trustworthy AI" agenda](https://www.schmidtsciences.org/trustworthy-ai-research-agenda/) | 2026 | 35 | Evaluation validity, deception, oversight |
| [Steinhardt "The Case for Evaluating Model Behaviors"](https://www.lesswrong.com/posts/J5KkwYnnaeNX7hL2s/the-case-for-evaluating-model-behaviors) | 2026 | 37 | Behavioral propensity measurement |
| [Orgad, Barez et al. "Interpretability Can Be Actionable"](https://arxiv.org/abs/2605.11161) | ICML 2026 | 48 | Actionability and comparative advantage |
| [MIB: Mechanistic Interpretability Benchmark](https://openreview.net/forum?id=sSrOwve6vb) | 2025 | — | Standardized causal localization evaluation |
| [Barez et al. "MI Needs Philosophy"](https://arxiv.org/abs/2506.18852) | 2026 | — | Conceptual foundations and epistemic status |
| [ICML 2026 MI Workshop CFP](https://mechinterpworkshop.com/cfp/) | 2026 | — | Field-level open questions |
