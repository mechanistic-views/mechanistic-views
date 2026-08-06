# Literature search findings — IOI audit correction and promotion target

## 1. The IOI audit was wrong (correction required)

The CrossView draft scores IOI at δ ≈ 1–1.5 and recommends a structural-view analysis
as the path to higher depth. Both the score and the recommendation are stale.

**Structural view — already occupied.**
- Elhage et al. 2021, *A Mathematical Framework for Transformer Circuits* — origin of the
  composition score as a weight-only quantity.
- **Merullo et al. 2024 (NeurIPS), *Understanding Inter-layer Communication in Transformer
  Language Models*** — weight-based composition scores computed specifically for
  name-mover head 9.9, without activation data. The direct hit.
- **arXiv 2601.10266 (2026)** — full OQ/OK/OV composition analysis on GPT-2 Small,
  reproducing the IOI cast (S-inhibition L8H10, name-movers L10H7/L11H3) purely in weight
  space; identifies L4H7 as a structural hub.

**Process view — partial.**
- **Tigges et al., *LLM Circuit Analyses Are Consistent Across Training and Scale***
  (arXiv 2407.10827) — ~154 Pythia checkpoints, 300B tokens; role persistence despite
  component churn. This is persistence, not formation.
- No paper does IOI-specific formation timing. The closest template is *When Do Attention
  Circuits Form?* (arXiv 2606.02378), on induction/BOS-attractor formation.

**Consequence.** Recomputed, IOI spans object + role + subspace + structural + partial
process across four families, so δ ≈ 4 — **above induction heads (3.5)**. This inverts the
draft's narrative: IOI is among the better-corroborated claims, not a low-depth cautionary
tale. What survives of the original criticism is only the internal inconsistency (fixed
circuit, Wang et al., vs prompt-specific, Franco et al.), which the maximal-consistent-subset
rule still penalises. The genuine open gap is IOI formation timing.

## 2. SAE features — confirmed promotion target, with a published rescue hypothesis

- **Weight-space:** nothing exists. No one has run composition scores on SAE decoder
  vectors. *Dense SAE Latents Are Features, Not Bugs* analyses latent geometry, but that is
  activation geometry, not weight-space structure. Gap confirmed.
- **Cross-seed stability (the negative-result cluster):**
  - **arXiv 2606.12138, *Unstable Features, Reproducible Subspaces*** — individual SAE
    features are not reproducible across seeds, but they cluster into reproducible low-rank
    **subspaces**. This is precisely "the object view fails, the subspace view may rescue
    it," and it makes the promotion experiment concrete and immediately testable.
  - **arXiv 2606.02061, *Ablating Archetypes*** — claimed stability gains were an artifact
    of shared initialisation.
- **Process arm:** arXiv 2412.17626, *Tracking the Feature Dynamics in LLM Training* —
  checkpoint-level feature formation.
- **Contrastive-baseline robustness:** no dedicated study. Open gap.

## 3. Other single-view candidates

- **Refusal direction** (Arditi et al. 2024) — activation steering and ablation only; no
  weight-space or checkpoint analysis of the direction itself. Live and unclaimed.
- **J-space** — activation/Jacobian evidence only; zero weight-space or training-dynamics work.

## 4. J-space — rejected as the calibration target

Code is public (`github.com/anthropics/jacobian-lens`, Apache-2.0) and Nanda replicated the
five core properties on open-weight Qwen 3.6 27B with ~25 prompts, so it is cheap to run.
But it is weeks old, has no ground truth, and no baseline claim has stabilised — the first
structural analysis of it would have no comparison point. Interesting for a later paper,
wrong for calibration now.

## Citations to add to the bib

Merullo et al. 2024 (NeurIPS) · arXiv 2601.10266 · Tigges et al. arXiv 2407.10827 ·
arXiv 2606.12138 · arXiv 2606.02061 · arXiv 2412.17626 ·
Lawlor, Tilling & Davey Smith 2016, *Int J Epidemiol* 45(6):1866–1886.
