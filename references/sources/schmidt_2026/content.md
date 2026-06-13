# The Science of Trustworthy AI: Research Agenda - Schmidt Sciences

Source: https://www.schmidtsciences.org/trustworthy-ai-research-agenda/

## Introduction

### Challenge Statement

"Despite staggering recent AI progress, we lack a scientific understanding of what makes AI systems trustworthy."

Contemporary AI development resembles experimental trial-and-error rather than mature science. Researchers increase data, compute, and training duration while hoping desirable behaviors emerge. Results are impressive, yet predicting model behavior under novel conditions remains limited — especially as systems become more agentic.

### Core Concepts

**Technical Alignment:** Ensuring system behavior matches intended specifications. A key distinction exists between stated training objectives (what developers specify) and effective goals (what systems reliably pursue across contexts based on actual behavior).

**Goal-like Behavior:** May reflect stable internal representations and planning, or arise from heuristics, pattern completion, and role-conditioned policies induced through prompting and post-training.

**Misalignment Sources:**
- **Misspecification:** Stated objectives fail to capture true user intent
- **Underspecification:** Multiple solutions satisfy training objectives, with models selecting unintended ones through inductive biases

### Why Misalignment Matters

Misaligned behavior can propagate rapidly across millions of users through deployed systems operating under conditions substantially different from training. Current systems demonstrate sycophancy, deception, and specification gaming — not isolated pathologies but recurring patterns reflecting deeper objective mismatches.

### Limitations of Current Approaches

Existing post-training methods improve in-distribution behavior through surface-level modifications that often fail under novel or adversarial conditions. Understanding how training shapes internal representations and which interventions remain effective as capabilities advance and autonomy increases remains limited.

### Research Agenda Aims

1. **Characterize and forecast misalignment** in frontier AI systems — understand why training-and-deployment safety practices still result in models learning effective goals failing under distribution shift, pressure, or extended interaction.

2. **Develop generalizable measurements and interventions** — advance evaluation science with decision-relevant validity and create interventions controlling what systems learn (not just what they express).

3. **Oversee superhuman AI systems and address multi-agent risks** — develop oversight methods for settings where direct human evaluation isn't feasible and address risks from interacting AI systems.

---

## Section 1: Characterizing and Forecasting Misalignment

Modern AI systems can appear aligned during training while learning effective goals that fail under distribution shift, optimization pressure, extended interaction, new tool access, or adversarial contexts. A recurring failure pattern: surface-level compliance without robust generalization.

This section aims to:
- Clarify what constitutes misalignment in practically relevant regimes
- Characterize failures
- Identify generative mechanisms
- Forecast changes with scale and increased agentic capability

### 1.1: What is Misalignment, and How Much Do We See Today?

Before predicting or preventing misalignment, sharper answers to core questions are needed.

**Prioritized Questions:**

- **Operationalizing misalignment:** What constitutes misalignment in decision-relevant terms, and how can magnitude be quantified or bounded?

- **Specification gaming and goal misgeneralization:** Under which conditions do models exploit training objective flaws or pursue unintended goals satisfying specifications in-distribution but diverging out-of-distribution? What signatures distinguish these from error or brittle generalization?

- **Distribution shift and emergent misalignment:** Which shifts (domain, capability, optimization pressure, post-training protocol, tool access) increase misalignment risk? What causes emergent misalignment, and what implications exist for future AI safety?

- **Model interactions with real users:** How do extended human-model interactions shape behavior over time? When do manipulative, misleading, or approval-seeking dynamics emerge and reinforce? Do stable behavioral patterns persist across conversations and contexts?

### 1.2: Mechanisms of Generalization and Representation

Characterization is necessary but insufficient. Understanding *why* models generalize in misalignment-producing ways requires insight into how training shapes internal representations determining behavior under distribution shift.

**Prioritized Questions:**

- **Inductive biases and convergence:** Why do models converge on particular solutions among many consistent with training data? How do architecture, optimization dynamics, data composition, curriculum, and scale shape learning? Which theoretical predictions about inductive biases hold empirically?

- **Internal representations:** When do models behave as if possessing internal representations of beliefs, goals, values, and uncertainty? How do such representations emerge during training (including through mesa-optimization)? How do they relate to misalignment failures?

- **Causal structure and world models:** When do internal representations support causal reasoning and counterfactual planning affecting alignment under distribution shift? Can richer world models improve robustness or primarily increase constraint-routing ability?

- **Abstraction and proxy collapse:** When does training compress intended objectives into proxies sufficient in-distribution but misgeneralizing under shift (e.g., user approval for helpfulness, passing evals for safety)? Can such proxy objectives be detected internally?

### 1.3: Scaling, Emergence, and Forecasting Risk

Some failures matter primarily when scaling with capability or emerging discontinuously. This prioritizes forecasting and early-warning work identifying measurable precursors predicting deployment failures.

**Prioritized Questions:**

- **Safety scaling laws:** How do risk-relevant properties — autonomy, effective time horizon, capability uplift — scale with model size, inference compute, and scaffolding? When do qualitatively new failure classes emerge undermining existing oversight assumptions?

- **Emergence and phase transitions:** When and how do safety-relevant capabilities emerge during training or agent deployment? Are predictable phase transitions where risks increase discontinuously? Are safety-relevant concepts modular, sparse, or disentangled from capabilities?

- **Forecasting failures ex ante:** Which observable signals (training metadata, representation diagnostics, capability profiles, evaluation patterns, training dynamics) best predict future misbehavior under deployment-like conditions?

- **Safety cases for generalizing evaluations:** As AI systems scale or enter new regimes, what structured arguments justify relying on evaluation or detection methods outside tested settings?

---

## Section 2: Generalizable Measurements and Interventions

Even when correctness and safety are theoretically verifiable by humans, evaluation can be expensive, incomplete, strategically gamed, or measuring wrong constructs. Interventions can improve in-distribution behavior without changing learned effective goals.

This section prioritizes:
1. Advancing rigorous evaluation science
2. Interventions that generalize under distribution shift and adversarial pressure by changing what systems learn

### 2.1: Building a Science of Evaluation

Evaluations should: (a) measure meaningful latent safety properties (construct validity), (b) predict deployment behavior (predictive validity), and (c) remain informative under optimization pressure.

**Prioritized Questions:**

- **Construct validity:** How can evaluations measure safety-relevant constructs and latent traits with defensible evidence, including theoretically grounded, empirically validated, and auditable behavioral or internal indicators? Which behavioral or internal features provide valid indicators?

- **Predictive validity and contextualization:** What evidence demonstrates an evaluation predicts behavior in real-world settings (healthcare, education, scientific research)?

- **Evidence standards for decision-relevant evaluations:** When an evaluation or detector appears generalizing, what structured evidence justifies relying on it in safety cases? What validity evidence types are needed? How should such arguments be stress-tested?

- **Robust under realistic conditions:** How can rare, delayed, or trajectory-dependent behavior be identified without artificial elicitation? Can propensities for harmful behavior in deployment-relevant settings be estimated? When do models condition behavior on evaluation?

- **Strategy-proof evaluations:** How can evaluations remain valid when explicitly optimized against? How do evaluation designs account for information asymmetries between developers, evaluators, and models?

- **Model organisms and controlled testbeds:** Can simplified controlled settings reliably produce misaligned behavior, enabling systematic measurement, stress-testing, and method comparison?

- **Tail risk and uncertainty quantification:** Can probabilities of consequential but low-frequency failures be estimated, including distribution-tail events never appearing in finite evaluation sets? How should safety-property uncertainty be represented and communicated?

- **Reasoning trace monitorability:** When are chain-of-thought or intermediate outputs informative about model reasoning for monitoring? Under what conditions do models produce textual reasoning faithful to decision-making versus strategically optimized to appear aligned?

### 2.2: Interventions that Generalize

Evaluation enables measurement; intervention enables improvement. This prioritizes methods reducing misalignment in generalizable ways across novel contexts and adversarial settings.

**Prioritized Questions:**

- **Shaping what is learned:** Which interventions change underlying learned drivers (effective goals) rather than surface behavior? When do such constraints generalize across architectures, scales, and training regimes? When do mechanistic interventions offer advantages over behavioral post-training? What evidence demonstrates genuine learned goal shaping versus improved in-distribution performance?

- **Generalization of alignment methods:** When do deliberative training, myopic training, and process supervision improve alignment robustness under pressure and distribution shift versus inducing strategic compliance or legible-but-misaligned reasoning?

- **Improving specifications and value uncertainty:** How far can improved model specifications reduce misalignment, and what failure modes remain? How can models represent value uncertainty appropriately and act robustly under normative ambiguity?

- **Preserving human agency:** Are interventions available that differentially preserve human agency rather than substituting for it (measured by human-AI collaborative uplift)?

---

## Section 3: Oversight Under Capability Gaps and Multi-Agent Risks

Section 2 assumes humans can reliably assess and verify correctness or safety. This breaks down in two cases:

1. **Superhuman capabilities:** When AI capabilities exceed supervisors in domains, maintaining oversight becomes challenging. Many applications involve superhuman tasks; this gap will widen.

2. **Multi-agent interactions:** Multiple interacting AI systems create risks from collective dynamics no single observer can fully anticipate or monitor.

### 3.1: Amplified Oversight for Superhuman Performance

As systems approach and exceed human performance, direct oversight becomes unreliable. Supervisors lack expertise for reasoning evaluation, cannot verify factual claims, and cannot anticipate subtle output failures. Yet safe training and deployment require oversight. Amplified oversight enables weaker supervisors providing reliable signals despite capability gaps through task decomposition, debate, recursive reward modeling, or similar methods.

#### 3.1a: Oversight as Training Signal

During training, oversight provides feedback shaping behavior and learned goals. As task difficulty increases, feedback increasingly relies on amplification.

**Prioritized Questions:**

- **Reliability and task coverage:** How can amplified oversight achieve sufficient reliable coverage preventing specification gaming, goal misgeneralization, or detector evasion? How will methods generalize out-of-distribution? When can weaker supervisors train stronger systems? Where does this break?

- **Human and model judge limitations:** How do known human biases interact with amplified oversight schemes? Do analogous biases arise in LLM judges? Which designs are robust to correlated evaluator errors? Can models be incentivized providing unknown evaluations?

- **Constraining and eliciting what is learned:** When do amplified oversight methods constrain learned effective goals rather than merely improving supervised-task performance? How can "honest" internal information expression be elicited?

- **Learning from limited supervision:** Can partial supervision over reasoning (bridging RLVR and supervised learning) be learned?

- **Anticipating specification failures:** Can amplified oversight identify misspecified training objectives or anticipate model constitution failures?

#### 3.1b: Oversight as Deployment-Time Control

Beyond training, oversight functions as deployment-time control enabling weaker supervisors verifying, bounding, or constraining stronger model behavior during autonomous operation.

**Prioritized Questions:**

- **Verification under capability gaps:** What properties can weaker overseers reliably verify or bound about stronger models, including worst-case risk bounds? Which problem classes admit efficient verification despite difficult generation?

- **Control evaluations:** How can generalization of oversight methods beyond specific tested failure modes be known? What task distributions and red/blue-team methods yield informative results?

- **Robustness under strategic adaptation and long-horizons:** How can oversight remain effective when models condition behavior on monitoring? How can strategies with effects only emerging after many steps, long delays, or indirect causal chains be detected and intervened upon?

### 3.2: Multi-Agent Risks and Collective Dynamics

AI systems are increasingly deployed as interacting collections rather than isolated models. Even locally-aligned individual agents introduce distinct multi-agent risks.

**Prioritized Questions:**

- **Interaction-specific safety properties:** How can properties arising through interaction — coerciveness, strategic competence, positional preferences, partiality — be measured? How do training objectives and environments shape emergence?

- **Multi-agent misgeneralization:** How do Section 1 mechanisms (specification gaming, proxy collapse, distribution shift) manifest in multi-agent settings? When do interactions amplify or dampen individual misalignment?

- **Collusion:** When do agents learn coordination defeating intended oversight or developing dangerous collective capabilities unascribable to individuals? What evaluation designs detect collusion in realistic high-stakes settings? What interventions reliably prevent it?

- **Emergent dynamics and failure propagation:** What collective-level failure modes emerge when no individual agent "intends" them? How do local failures propagate through interacting AI system networks? How can detection and containment occur?

- **Infrastructure for trusted multi-agent interaction:** What technical tooling enables trustworthy interaction — authenticated identity/reputation systems, commitment devices, private-information verification mechanisms?

- **Long-horizon risks:** What risks unfold over extended horizons (competitive drift, cooperative norm erosion, undesirable equilibrium lock-in)? How can oversight detect pre-entrenchment?

---

## Out of Scope

These topics fall outside this RFP scope:

- **Exclusive interpretability projects** (see dedicated AI Interpretability pilot program)
- **Jailbreak discovery and ad hoc adversarial probing** without fundamental robustness science connections
- **Generic capability evaluations** without safety-construct links or decision thresholds
- **Near-term product engineering** for immediate application shipping
- **Fairness, accountability, and bias research** unconnected to agenda questions
- **Policy and AI governance**
- **Epistemic integrity** (content authenticity, watermarking)
- **Direct CBRN or ARA dangerous capability evaluations** requiring security clearance
- **Model safeguards** (I/O filtering, constitutional classifiers)
