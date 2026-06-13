---
title: "Training Dynamics"
---

# Do mechanisms survive training?

Most mechanistic interpretability analyzes a snapshot: a fully trained model frozen in time. But mechanisms form during training, change during fine-tuning, and can be destroyed by adversarial optimization. The static snapshot tells you what mechanisms exist *now* but nothing about whether they're stable, how they got there, or whether they'll survive the next round of training.

**Fine-tuning destroys circuits.** The ICML 2026 actionability paper (Orgad, Barez et al.) includes experiments on catastrophic forgetting circuits — tracking which circuit heads degrade after fine-tuning on unrelated data. The finding: circuits identified via ablation before fine-tuning may no longer be circuits afterward. If your safety monitor relies on a circuit identified in the base model, fine-tuning can silently invalidate it.

**Adversarial training relocates mechanisms.** Sharkey's Sparsify agenda includes "robust-to-training" experiments: fine-tune a model to reduce circuit localization, then check whether the circuit is still detectable and whether it moved. Early results suggest that targeted adversarial training can cause mechanisms to become more distributed, evading the ablation-based detection methods that found them in the first place. This is especially concerning for safety: a model optimized to evade interpretability-based monitoring could relocate its mechanisms.

**Phase transitions create mechanisms suddenly.** Grokking (Power et al. 2022; Nanda et al. 2023) shows that models can train for thousands of steps with no change in circuit structure, then undergo a sudden phase transition where a new mechanism crystallizes. Induction heads (Olsson et al. 2022) show a similar pattern: they form abruptly during training, and their formation causally enables in-context learning. Understanding *when* and *why* mechanisms form is orthogonal to understanding what they are.

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
| [I3 Dose-response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response) | Static dose-response | **Strengthened** (formation trajectory shows gradual development, not just static graded effect) |

## Sources

- **Sharkey "Sparsify" (2024)**: Robust-to-training experiments ([Sparsify agenda](https://www.alignmentforum.org/posts/64MizJXzyvrYpeKqm))
- **ICML 2026 (Orgad, Barez et al.)**: Catastrophic forgetting circuits ([arXiv:2605.11161](https://arxiv.org/abs/2605.11161))
- **Nanda (2022)** §5: Training dynamics ([200 Open Problems](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability))
- **Power et al. (2022)**: Grokking — generalization beyond overfitting on small algorithmic datasets
- **Nanda et al. (2023)**: Progress measures for grokking via mechanistic interpretability
- **Olsson et al. (2022)**: In-context learning and induction heads
