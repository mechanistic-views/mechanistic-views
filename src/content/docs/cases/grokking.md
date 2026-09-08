---
title: Case Study — Grokking
---

# Case Study — Grokking

**The phenomenon.** Models trained on modular arithmetic memorize training data before transitioning to near-perfect generalization — sometimes thousands of steps after near-perfect training accuracy (Power et al., 2022). The generalization mechanism uses Fourier features.

## Why this case is important

Grokking is a natural case for the [process view](/mechanistic-views/views/process/). The static views describe the final Fourier mechanism but cannot describe why the transition occurs when it does.

## The final-state mechanism (Fourier)

The generalized model represents inputs as combinations of Fourier basis functions in the residual stream. The relevant variable traces a circle $S^1$ embedded in a flat 2-dimensional subspace spanned by sine and cosine components — it does live inside $\mathcal{M}_2$ as a [Grassmannian](/mechanistic-views/formalism/grassmannian/) stratum. However, the variable is not *linearly* encoded in the sense required by [DAS](/mechanistic-views/views/subspace/#evidence): the causal variable (the remainder class modulo $p$) is a nonlinear function of the projection onto that 2D subspace. A flat subspace swap will not transfer the correct remainder class unless the swap is structured to respect the circular geometry. Under the [subspace view](/mechanistic-views/views/subspace/) with DAS, this means the [Grassmannian](/mechanistic-views/formalism/grassmannian/) identity criterion is necessary but not sufficient — the full description requires the additional structure of the circular embedding within $\mathcal{M}_2$, which belongs to the nonlinear manifold stratum.

## The memorization mechanism

Before grokking, the model outputs correct training labels without compositional structure. Both mechanisms coexist before the transition; grokking is the point where Fourier dominates. Under the [process view](/mechanistic-views/views/process/), this corresponds to a [stratum](/mechanistic-views/formalism/stratification/) change: the Fourier mechanism is in $\mathcal{M}_2$ with nonlinear (circular) encoding. The stratum of the memorization mechanism is not established — it could be high-$k$ (a large-dimensional lookup table), genuinely distributed ($\mathcal{M}_\infty$), or even low-dimensional with a different structure. Treating the transition as a stratum change from high-$k$/distributed to $\mathcal{M}_2$ is a working hypothesis, not an established characterization of the memorization mechanism.

## [Process view](/mechanistic-views/views/process/) account

Nanda et al. (2023) report that the generalizing circuit is amplified gradually and is formed well before test loss drops, and that grokking is the later removal of the memorizing components rather than a sudden switch between circuits. The mechanism is the trajectory — the sequence of weight-space changes and the checkpoint-by-checkpoint emergence of the algorithmic solution. No static description of the final circuit explains why generalization occurred, when it occurred, or what determined the transition point.

A complete process-view account should derive the transition timing from the dynamical system structure (e.g., from the relative decay rates of memorization and generalization components under the specific weight-decay schedule), not just describe it empirically.

## Current evidence state

Tiers below are the [Mechanistic Validity](/mechanistic-views/mechval-interface/) ladder, not this framework's verdict vocabulary. The framework's own verdicts are view-invariant, contested and candidate.

- **Tier 3** for the final-state Fourier mechanism under the [subspace view](/mechanistic-views/views/subspace/)
- **Tier 2** for the phase transition dynamics under the [process view](/mechanistic-views/views/process/): well-documented, but full dynamical account preliminary
- **Tier 1** under the [structural view](/mechanistic-views/views/structural/): no gauge-invariant characterization of either circuit has been published

## Further reading

Power, A., Burda, Y., Edwards, H., Babuschkin, I., Misra, V. "Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets." [arXiv:2201.02177](https://arxiv.org/abs/2201.02177), 2022.

Nanda, N., Chan, L., Lieberum, T., Smith, J., Steinhardt, J. "Progress measures for grokking via mechanistic interpretability." [ICLR 2023. arXiv:2301.05217](https://arxiv.org/abs/2301.05217), 2023.
