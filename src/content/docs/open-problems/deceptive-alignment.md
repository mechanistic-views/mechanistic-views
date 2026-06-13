---
title: "Deceptive Alignment"
---

# Can MI Detect Deceptive Alignment?

**The question.** Can mechanistic interpretability detect whether a model is strategically behaving well during evaluation while pursuing different goals in deployment? This is the central question of AI safety: if a model is deceptively aligned, can we tell from the inside?

This question is usually treated as a methods problem — build a better deception detector. But the views framework reveals that the difficulty is partly structural: the evidence standards required to establish deceptive alignment are much higher than the evidence most MI methods can produce.

## What each view says

### [Instrumental view](/mechanistic-views/views/instrumental/) — insufficient by design

The Instrumental view asks: can we predict when the model will behave deceptively? A probe or steering vector that activates on "deceptive" inputs would be Instrumental evidence. But Instrumental evidence only establishes predictive utility — it doesn't tell you whether the model is *computing* deception or whether the probe has found a shortcut.

**The fatal problem.** A deceptively aligned model that is good at deception would, by definition, behave identically to an aligned model during evaluation. Instrumental evidence requires behavioral differences to distinguish them. If the deception is competent, there are no behavioral differences to find — at least not on the evaluation distribution.

### [Subspace view](/mechanistic-views/views/subspace/) — necessary but not sufficient

A "deception subspace" — a causal subspace encoding whether the model is in evaluation vs. deployment mode — would be Subspace-level evidence. [DAS/IIA](/mechanistic-views/views/subspace/#evidence) could test whether intervening on this subspace switches the model between aligned and misaligned behavior.

**The problem.** A model that has learned to distribute its deceptive computation across many weakly-activated subspaces may not have a single clean "deception direction." And a model aware of interpretability methods could learn representations that evade subspace-level detection — encode the same information in a way that linear methods can't find.

### [Structural view](/mechanistic-views/views/structural/) — the right level, but extremely hard

Deceptive alignment detection requires finding a computational structure — a [gauge-invariant](/mechanistic-views/views/structural/) circuit — that implements strategic reasoning about evaluation context. This means: the model has a computation that (1) represents whether it's being monitored, (2) conditions its behavior on that representation, and (3) this computation is stable under reparameterization.

**Why Structural evidence matters.** A deceptively aligned model that is adversarially trained against interpretability can relocate its mechanisms — move the computation to different heads, distribute it differently, change the basis. Instrumental and Subspace evidence can be evaded this way. Structural evidence (gauge-invariant computation) is, by definition, stable under such reparameterizations.

**The challenge.** No one has demonstrated Structural-level analysis of any complex behavior at scale, let alone deceptive cognition. This is the right evidence standard but may be beyond current methods.

### [Process view](/mechanistic-views/views/process/) — when and how does deception form?

If deceptive alignment exists, the Process view asks: when did it form during training? Was there a phase transition? Can you identify training checkpoints before and after the deceptive mechanism appeared? Could you intervene during training to prevent it?

**The insight.** Process evidence provides a complementary angle: even if you can't find the deception mechanism in a finished model (Structural analysis failed), you might detect the *formation* of deceptive behavior during training ([E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness)). A mechanism that appears suddenly late in training, correlated with exposure to evaluation-like data, is suspicious in ways a mechanism that developed gradually is not.

## The resolution

Detecting deceptive alignment requires evidence at multiple views simultaneously:

| View | What it provides | Why it's not enough alone |
|---|---|---|
| [Instrumental](/mechanistic-views/views/instrumental/) | Behavioral prediction | Competent deception evades behavioral detection |
| [Subspace](/mechanistic-views/views/subspace/) | Causal subspace encoding evaluation-awareness | Can be evaded by distributing computation |
| [Structural](/mechanistic-views/views/structural/) | Gauge-invariant deception circuit | Extremely hard to compute at scale |
| [Process](/mechanistic-views/views/process/) | Formation trajectory during training | Requires access to training checkpoints |

The framework's contribution is not to solve deceptive alignment detection — that remains an open empirical problem. It is to make the evidence requirements explicit:

1. **Instrumental evidence is structurally insufficient.** If your deception detector is a probe or steering vector, it cannot distinguish competent deception from alignment. This is not a methods limitation — it is a structural property of the Instrumental view.
2. **The minimum standard is Structural + Process.** You need gauge-invariant evidence of a deception computation (Structural) that you can trace through training (Process). Anything less can be evaded.
3. **Current methods are Instrumental or Subspace.** The gap between where the field is (probes, steering vectors) and where it needs to be (gauge-invariant circuits, formation tracking) is the real open problem.

## Resolution status: **Scoped**

The framework identifies the evidence requirements precisely: Instrumental evidence is insufficient, Subspace evidence is necessary but evadable, Structural + Process evidence is the minimum standard. The empirical problem — actually building methods that produce Structural evidence at scale — remains open.

## Mechanistic validity criteria

| Criterion | Status | What it tells you |
|---|---|---|
| [I1 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency/) | Central | Does intervening on the mechanism produce deceptive behavior? |
| [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion/) | Critical | Could another mechanism explain the same evidence? |
| [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | Critical | Does detection generalize beyond the evaluation distribution? |
| [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | Relevant | Is the mechanism stable through training? |
| [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance/) | Relevant | Is detection robust to reparameterization? |

## See also

- [Safety Evidence Gaps](/mechanistic-views/open-problems/safety-evidence-gaps/) — the broader problem of Instrumental evidence used for Structural claims
- [Training Dynamics](/mechanistic-views/open-problems/training-dynamics/) — adversarial training can relocate mechanisms
- [CoT Faithfulness](/mechanistic-views/open-problems/cot-faithfulness/) — a related problem where model outputs may not reflect internal computation
- [Structural view](/mechanistic-views/views/structural/) — the view that provides adversarially-robust evidence
- ["MI Needs Philosophy"](https://arxiv.org/abs/2506.18852) §2.3 — deception requires intentions/beliefs models may lack ([full mapping](/mechanistic-views/open-problems/barez-philosophy/))
