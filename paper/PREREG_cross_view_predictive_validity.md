# Preregistration — Cross-View Predictive Validity

**Status:** DRAFT — freeze before running. Commit this file, record the SHA here and in the paper, then run.
**Freeze SHA:** `________` (fill on commit)

---

## 0. Why this study exists

MechViews currently makes two assumptions it does not measure: that views have **orthogonal failure modes**, and that the **harmonic weighting** of within-family redundancy is right. Both are load-bearing for invariance depth δ. This study measures them, and tests whether the framework buys anything a simpler account does not.

The framework can lose here. That is the point.

---

## 1. Central hypothesis

> **Cross-view support predicts mechanistic correctness beyond the best single-view evidence, the number of methods used, and ordinary circuit faithfulness.**

This is deliberately distinct from MIB, which compares *which methods best localize circuits*. We test whether **structured triangulation across ontologically different claims** improves epistemic reliability.

---

## 2. Preregistered hypotheses and decision rules

All evaluation uses **program-level grouped cross-validation** (entire programs held out; see §7).

| ID | Hypothesis | Decision rule | If it fails |
|---|---|---|---|
| **H1** | Cross-family view support has incremental predictive value over (best single-view evidence + method count). | ΔAUROC > 0.05, bootstrap 95% CI excludes 0. | The realism argument loses its empirical backing. Report it. |
| **H2** | **View-family count outperforms raw method count.** | Family-count model beats method-count model on held-out log loss; ΔAUROC CI excludes 0. | *"Views add vocabulary, not measurement."* The most important possible negative result — publish it. |
| **H3** | Failure modes are not uniformly shared: the artifact-acceptance matrix \(A_{vf}\) is not rank-1. | ≥1 artifact class accepted by some views and rejected by others, with the accept/reject pattern differing across ≥2 artifact classes. | Orthogonality premise is false; δ is overcounting throughout. |
| **H4** | Two views from *different* families add more incremental predictive value than two from the *same* family. | ΔAUROC(cross-family pair) > ΔAUROC(same-family pair), CI excludes 0. | Harmonic discounting is unjustified; families are not the right partition. |
| **H5** | δ re-weighted from measured error covariance outperforms heuristic harmonic δ. | Held-out AUROC(empirical δ) > AUROC(harmonic δ). | Keep the heuristic, but say it is unimproved rather than justified. |
| **H6** | A scoring rule frozen on Tracr retains above-chance discrimination on *learned* models. | Held-out AUROC > 0.60 on modular-arithmetic models. | Tracr does not transfer — a major limitation on the whole framework, and a finding in itself. |

**Pre-specified:** H2 and H6 are the two that can most damage the framework. Both are reported regardless of outcome.

---

## 3. Unit of analysis

The unit is a **mechanistic claim**, not a method output and not a paper:

> *"Causal variable Z is implemented by carrier U, which performs role R in computing output Y."*

Each view evaluates a distinct projection of the **same** preregistered claim.

Three outcome labels are kept distinct and never collapsed: **supported**, **tested but failed**, **inapplicable/untested**.

---

## 4. Views tested — must span ≥3 families

The MVP's view selection is chosen to **span families**, because δ rests on cross-*family* orthogonality. (An earlier draft used object/role/subspace/structural, which spans only two families and therefore could not test the core claim.)

| View | Family | Operationalization | MVP |
|---|---|---|---|
| Object (method A) | Identity | Activation patching | ✅ |
| Object (method B) | Identity | Attribution/EAP | ✅ — **the method-count control** |
| Structural | Mathematical | Weight composition scores; invariance under reparameterization | ✅ |
| Contrastive | Contrastive | Same claim under systematically varied foils/baselines | ✅ (cheap) |
| Process | Process | Emergence across training checkpoints | ✅ (learned models only) |
| Subspace | Mathematical | Constrained DAS/IIA, projector recovery | ❌ MVP — deferred |

**Why subspace is deferred in the MVP:** it shares the mathematical family with structural, so it adds nothing to family-spanning, and DAS requires an optimization per claim — by far the largest compute cost. It enters in the full study to test H4 (within-family redundancy).

---

## 5. Claim bank — true claims and hard negatives

Evaluating only recovered mechanisms creates selection bias. Every program gets claims of each type:

1. **Ground truth** (correct carrier, correct role).
2. **Near miss** — one component wrong.
3. **Right carrier, wrong role.**
4. **Right role, wrong carrier.**
5. **Superset** — true mechanism plus distractors.
6. **Alternative sufficient but non-necessary path.**
7. **Rotated subspace** — partly outside the true causal subspace.
8. **Narrow-distribution discovery** — found on a deliberately restricted prompt set.
9. **Permissive-alignment claim** — generated with intentionally unconstrained alignment.
10. **Seed-varying feature claim** — decomposition-dependent (SAE-style), where applicable.

Types 7–10 are the **hard negatives**: they encode exactly the failure modes MechViews claims different views should catch. Without them the benchmark is trivially easy and any positive result is uninformative.

---

## 6. Recorded per claim

Ground-truth correctness · best single-view evidence score · method count · view count · **view-family count** · pairwise cross-view consistency · heuristic δ · standard faithfulness/completeness · claim size (|U|) · program id · claim type.

---

## 7. Analysis plan

**Primary analysis — incremental validity.** Nested model comparison predicting Pr(correct):

- M0: claim size only (null)
- M1: best single-view evidence
- M2: M1 + method count
- M3: M2 + **view-family count** ← H1/H2 test
- M4: M2 + heuristic δ
- M5: M2 + empirically-weighted δ ← H5

**Baselines reported alongside:** best single method · mean evidence across methods · method count · replication count · MIB-style localization/faithfulness · unweighted view count · harmonic δ · learned view weighting.

**Clustering is handled explicitly.** Claims are nested within programs, so the effective N is the **number of programs, not the number of claims**. All evaluation uses grouped (leave-programs-out) cross-validation, and models use program-level random effects. Reported: held-out AUROC, average precision, expected calibration error, log loss — each with bootstrap CIs resampled **at the program level**.

**Secondary analysis — failure-mode covariance.** Induce one artifact at a time and record which views accept the resulting false claim:

\[ A_{vf} = \Pr(\text{view } v \text{ supports a false claim} \mid \text{artifact } f) \]

MVP artifacts: narrow distribution · wrong foil · permissive alignment · computation-preserving basis change. From \(A_{vf}\), estimate pairwise view-error correlation and re-derive weights (H5).

---

## 7b. Researcher degrees of freedom and multiple comparisons

Testing a claim under many views is a **garden-of-forking-paths** setup: run everything, then declare whichever view fired was the intended one. This is MechVal's own "flexible scope" and "circuit redefinition" failure modes turned on our method, and it must be controlled explicitly.

**Controls, all preregistered:**

1. **Permutation / null-direction baseline (primary control).** Compute the promotion or support rate for **random directions and scrambled claims** under identical criteria. This gives the null rate empirically and sidesteps analytic corrections across views × claims entirely. If real claims are supported at rate *p* and null claims at rate ≈ *p*, there is no result. This is MechVal's M2 (baseline separation) applied reflexively to our own study.
2. **Support set declared in advance.** For each claim, the expected view-support set is written down before any view is run. δ computed from a *predicted* support set is severe; δ from a *discovered* one is not — the confirmation/corroboration distinction applied to views.
3. **Specification curve across views.** Report the **full distribution** of view-level results for every claim, not the max or the best-supported subset (multiverse / specification-curve analysis; cf. its use in ML to prevent fairness hacking). No view result is dropped.
4. **FDR control** (Benjamini–Hochberg) across claims within each view.
5. **Hold-out for pattern discovery.** Any "what predicts promotion" finding is discovered on a subset and confirmed on held-out programs/claims.
6. **Blinding.** View-scoring is blind to other views' outcomes wherever operationally possible; record where it was not.

**Related work to cite:** Lawlor, Tilling & Davey Smith (2016), *Triangulation in aetiological epidemiology* — triangulation across approaches with **unrelated key sources of bias**, the direct precedent for cross-view invariance. Note their stronger criterion: triangulation is most convincing when the biases of different approaches would push results in **opposite directions** if they were driving the finding. Consider adopting this as a refinement of family orthogonality.

## 8. Power

Pilot on 3 programs first, then a power analysis targeting H1/H2 at the **program** level. Do not fix the program count in advance of the pilot; record the pilot-derived target here before the main run:

**Pilot-derived target:** `________` programs (fill after pilot, before main run).

---

## 9. Scoped MVP (do this one)

1. **12 Tracr programs**, varying operation, circuit size, redundancy, localized vs distributed, distractor presence.
2. **~15 claims per program** (~180 claims) spanning claim types 1–8.
3. **Four views spanning three families** on Tracr: object×2 methods, structural, contrastive.
4. **Process view** added on 3–5 learned modular-arithmetic models (Clock/Pizza), which Tracr cannot supply — compiled models never *acquire* their mechanism.
5. **Four artifact interventions** → \(A_{vf}\).
6. **Grouped CV**, leaving whole programs out.
7. **Freeze the scoring rule**, then test H6 on the learned models.

That is a complete empirical paper on its own.

---

## 10. Full study (later)

Everything above, plus: 20–40 Tracr programs · the subspace view via constrained DAS (enables H4 within-family test) · claim types 9–10 · four more artifact classes (redundant-path ablation, training-hyperparameter variation, added distractors, seed instability) · external validation on 1–2 MIB tasks across Pythia checkpoints/seeds, testing **prospective intervention predictions** rather than claiming absolute ground truth.

---

## 11. Stated limitations (in the paper, not discovered by a reviewer)

- **Tracr is cleaner than reality.** Compiled models are near-one-hot, non-distributed, and structurally tidy; superposition and polysemanticity — the failure modes that dominate learned models — barely occur. An \(A_{vf}\) estimated on Tracr may not transfer. H6 tests this directly and its failure is reported as a headline result.
- **Learned-model ground truth requires a method.** Identifying Clock vs Pizza needs the Fourier diagnostic, so "ground truth" is method-mediated, if far less contested than IOI.
- **IOI is excluded on purpose.** No undisputed mechanism-level ground truth, and its object/role/weight analyses are already extensively studied.

---

## 12. Compute plan (Modal, ≤10 parallel)

- One program per job; ≤10 concurrent. `--detach`, `timeout=86400`.
- Pin every dependency with `==`. Install matplotlib even if unused (transitive-dep crash).
- `tqdm` + timestamps on every loop for pod monitoring.
- Human-readable run names (e.g. `crossview-tracr-prog07-object-patching`), never hashes.
- **Every result written to a JSON file** in the repo — never parsed from stdout/logs.
- Local smoke test on 1 program before any launch.

---

## 13. Deviation log

Any departure from this document after the freeze SHA gets logged here with date and reason.

| Date | Deviation | Reason |
|---|---|---|
| | | |
