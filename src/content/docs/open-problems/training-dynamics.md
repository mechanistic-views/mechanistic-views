---
title: "Training Dynamics"
---

# Do mechanisms survive training?

Most mechanistic interpretability analyzes a snapshot: a fully trained model frozen in time. But mechanisms form during training, change during fine-tuning, and can be destroyed by adversarial optimization. The static snapshot tells you what mechanisms exist *now* but nothing about whether they're stable, how they got there, or whether they'll survive the next round of training.

**Fine-tuning changes circuits without replacing them.** Prakash et al. (2024) find that fine-tuning enhances rather than replaces existing mechanisms, and preference optimization bypasses rather than removes them. The ICML 2026 actionability paper (Orgad, Barez et al.) tracks which circuit heads degrade after fine-tuning on unrelated data. Either way, a safety monitor keyed to a circuit identified in the base model can be silently invalidated by continued training, and the process view is what supplies the evidence to tell enhancement from relocation.

**Whether adversarial training relocates mechanisms is open.** Sharkey's Sparsify agenda includes "robust-to-training" experiments: fine-tune a model to reduce circuit localization, then check whether the circuit is still detectable and whether it moved. No published result settles it. This is especially concerning for safety: a model optimized to evade interpretability-based monitoring could relocate its mechanisms.

**Phase transitions create mechanisms suddenly.** Grokking (Power et al. 2022; Nanda et al. 2023) shows that models can train for thousands of steps with no change in circuit structure, then undergo a sudden phase transition where a new mechanism crystallizes. Induction heads (Olsson et al. 2022) show a similar pattern: they form abruptly during training, in a window that coincides with a jump in in-context learning. The narrow reading — the heads copy a token that followed the same context earlier — is well supported. The broad reading, that the heads are the mechanistic source of general in-context learning, is contested: at 70–72B the heads carrying abstract in-context reasoning are disjoint from induction heads (Webb et al. 2025), suppressing induction-head formation leaves abstract in-context learning intact on 13 of 21 tasks (Sahin et al. 2025), and above 1B, once function-vector heads are preserved, ablating induction heads is comparable to ablating random heads (Yin et al. 2025). Understanding *when* and *why* mechanisms form is orthogonal to understanding what they are.

## The view territory

These problems belong naturally to the [Process view](/mechanistic-views/views/process/), which defines mechanisms by their formation trajectories. The Process view asks: how did this mechanism get here? Is the formation robust across random seeds? Does the mechanism survive perturbation of the training process?

Most current MI operates at the Object, Role, or Subspace level — all static views. Adding Process-view evidence doesn't replace static analysis; it supplements it. A mechanism described at the Subspace level (a stable causal subspace) with Process-level evidence (it forms reliably, survives fine-tuning, and emerges at a specific phase transition) has substantially stronger validity than either analysis alone.

The Process view is unique in that it provides evidence for criteria that no static view can address: [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability/) (cross-seed), [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) (pre/post fine-tuning), and formation order (which mechanisms are developmental prerequisites for others).

## Mechanistic validity impact

| Criterion | Static views | With Process view |
|---|---|---|
| [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability/) | Possible (re-run method) | **Covered** (cross-seed comparison is built-in) |
| [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | Not testable | **Covered** (stability across training checkpoints) |
| [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness) | Testable but static | **Strengthened** (mechanism that survives fine-tuning on new distribution is more robust) |
| [E5 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response) | Static dose-response | **Strengthened** (formation trajectory shows gradual development, not just static graded effect) |

## Resolution status: **Scoped**

Most mechanistic interpretability work analyzes static snapshots, but mechanisms form and change during training. Tigges et al. (2024) track components across checkpoints and find head identities turning over while the algorithm persists; Olsson et al. (2022) locate induction-head formation in a phase change. These belong to the Process view, which uniquely provides evidence for cross-seed reliability and robustness to continued training.

## Sources

- **Sharkey "Sparsify" (2024)**: Robust-to-training experiments ([Sparsify agenda](https://www.alignmentforum.org/posts/64MizJXzyvrYpeKqm))
- **ICML 2026 (Orgad, Barez et al.)**: Catastrophic forgetting circuits ([arXiv:2605.11161](https://arxiv.org/abs/2605.11161))
- **Nanda (2022)** §5: Training dynamics ([200 Open Problems](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability))
- **Power et al. (2022)**: Grokking — generalization beyond overfitting on small algorithmic datasets
- **Nanda et al. (2023)**: Progress measures for grokking via mechanistic interpretability
- **Olsson et al. (2022)**: In-context learning and induction heads
