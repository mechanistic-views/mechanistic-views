---
title: "Schmidt Trustworthy AI Agenda"
---

# Schmidt Sciences "Trustworthy AI" Agenda

The [Schmidt Sciences 2026 research agenda](https://www.schmidtsciences.org/trustworthy-ai-research-agenda/) ("The Science of Trustworthy AI") outlines priorities for technical research on trustworthy AI. It is one of the largest coordinated funding signals in AI safety research. The agenda explicitly uses validity language — "construct validity," "predictive validity," "evidence standards" — and asks questions that map directly onto the [mechanistic views](/mechanistic-views/views/) framework, often without the vocabulary to frame them as such.

The agenda has three sections:
1. **Characterizing and forecasting misalignment** — understanding why models learn goals that fail under distribution shift
2. **Generalizable measurements and interventions** — building evaluations with construct and predictive validity
3. **Oversight under capability gaps** — maintaining oversight when humans can't verify AI outputs

Each section contains questions that are, at their core, questions about which view level of evidence is needed and which validity criteria must be satisfied.

## Section-by-section mapping

### Section 1: Characterizing misalignment

| Agenda question | View translation | Views involved |
|---|---|---|
| "What does it mean for an AI system to be misaligned, and how can we quantify it?" (§1.1) | What is the right operationalization? Behavioral divergence (Instrumental) vs. internal goal representation (Object/Subspace) vs. method-relative measurement (Perspectival) | [Instrumental](/mechanistic-views/views/instrumental/) vs. [Object](/mechanistic-views/views/object/) |
| "When do models behave *as if* they have internal representations of beliefs, values, and goals?" (§1.2) | Is the representation real (Object+) or a useful fiction (Instrumental)? The "as if" hedging is the Instrumental-Object boundary | [Instrumental](/mechanistic-views/views/instrumental/) vs. [Object](/mechanistic-views/views/object/) |
| "How do architecture, optimization dynamics, data composition shape what is learned?" (§1.2) | How do mechanisms form? This is the Process view's core question | [Process](/mechanistic-views/views/process/) |
| "When does training cause models to compress intended objectives into proxies?" (§1.2) | Proxy collapse is a mechanism that exists at the Subspace level (a subspace that correlates with the target in-distribution but diverges OOD) | [Subspace](/mechanistic-views/views/subspace/) |
| "Are safety-relevant concepts modular, sparse, or disentangled from capabilities?" (§1.3) | This is asking about the geometry of safety-relevant subspaces — a Subspace-view question with Stratified implications (resolution-dependent) | [Subspace](/mechanistic-views/views/subspace/), [Stratified](/mechanistic-views/views/stratified/) |
| "Which observable signals best predict future misbehavior?" (§1.3) | Predictive validity is the Instrumental view's strength — but the agenda wants prediction that *generalizes*, which requires higher-commitment evidence | [Instrumental](/mechanistic-views/views/instrumental/) floor, needs [Subspace](/mechanistic-views/views/subspace/)+ |

### Section 2: Measurements and interventions

This section maps most directly onto [Mechanistic Validity](https://mechanistic-validity.github.io/mechanistic-validity/). The agenda's evaluation desiderata are almost exactly the mechval criteria:

| Agenda requirement | Mechanistic Validity criterion |
|---|---|
| "Construct validity for latent properties" (§2.1) | [C1 Operationalization](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/operationalization/), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/) |
| "Predictive validity and contextualization" (§2.1) | [E1 Task transfer](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/task-transfer/), [E2 Distribution shift](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/distribution-shift/) |
| "Evidence standards for decision-relevant evaluations" (§2.1) | The full mechval framework — this is what it's for |
| "Robust under realistic conditions" (§2.1) | [E2 Distribution shift](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/distribution-shift/), [E5 Temporal stability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/temporal-stability/) |
| "Strategy-proof evaluations" (§2.1) | [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion/) — can the model game the evaluation? |
| "Reasoning trace monitorability" (§2.1) | [Perspectival](/mechanistic-views/views/perspectival/) concern — is the trace faithful (real mechanism) or strategic (method artifact)? |

The interventions section (§2.2) asks the key view-level question directly:

> "When do mechanistic interventions (e.g., targeting features, circuits, or learned representations) offer advantages over behavioral post-training methods?"

In our language: **when does [Object](/mechanistic-views/views/object/)/[Subspace](/mechanistic-views/views/subspace/) evidence beat [Instrumental](/mechanistic-views/views/instrumental/) evidence for safety?** The answer is: when you need generalization guarantees that Instrumental evidence structurally cannot provide — specifically [E1 Task transfer](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/task-transfer/), [E2 Distribution shift](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/distribution-shift/), and [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion/).

### Section 3: Oversight under capability gaps

| Agenda question | View translation |
|---|---|
| "What properties about stronger models can weaker overseers reliably verify?" (§3.1b) | Which view level is *verifiable* at scale? Instrumental claims (behavior prediction) are easy to verify but weak. Structural claims (gauge-invariant computation) are strong but hard to verify. The Pareto frontier between evidence strength and verifiability is a view-level question |
| "How can oversight remain effective when models condition behavior on being monitored?" (§3.1b) | This is a [Perspectival](/mechanistic-views/views/perspectival/) problem — the measurement changes the subject. Overcoming it requires evidence that doesn't depend on the model's cooperation, which is the Structural view's territory |
| "When do agents learn to coordinate in ways that defeat oversight?" (§3.2) | Multi-agent collusion is a Process-view question (how does the coordination mechanism form?) combined with a Structural question (what computation are the agents jointly performing?) |

## The meta-observation

The Schmidt agenda repeatedly asks for "evidence standards," "construct validity," "predictive validity," and "generalization guarantees." These are exactly the concepts that the [Mechanistic Validity](https://mechanistic-validity.github.io/mechanistic-validity/) framework formalizes into 27 criteria across 5 lenses. The agenda asks *what* evidence is needed; mechval provides *how* to measure whether you have it; and the views framework tells you *which methods can produce it*.

The agenda's core tension — "surface-level compliance without robust generalization" — is the Instrumental view's ceiling stated in safety language. A model that passes behavioral evaluations (Instrumental evidence) but fails under distribution shift has satisfied the Instrumental view's criteria and nothing more. The agenda is asking for evidence that goes beyond the Instrumental view without having a name for the Instrumental view.

## Relation to the Schmidt interpretability RFP

Schmidt Sciences also ran a separate, narrower [interpretability pilot program](https://www.schmidtsciences.org/trustworthy-ai-research-agenda/) focused specifically on detecting deceptive behaviors: sycophancy, harmful advice, and selective omission. Where the broad agenda asks the philosophical questions ("what evidence is sufficient?"), the interpretability RFP asks for concrete experiments ("can you detect sycophancy circuits?"). See [Safety evidence gaps](/mechanistic-views/open-problems/safety-evidence-gaps/) for how those experiments map onto the views framework.
