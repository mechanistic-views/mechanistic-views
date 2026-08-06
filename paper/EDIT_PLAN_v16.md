# MechViews — editing plan for v16

Self-contained spec. Source: `mechviews_v15.tex` (~3,127 lines) plus the realism material from `cross_view_invariance_v3_1/v4`. Target: **~20–25pp main body**, appendix unbounded.

---

## 1. The thesis change (most important)

**v15 thesis:** "Here is an atlas of nine mechanistic views."
**v16 thesis:** **"Mechanistic claims are made under views whose artifacts are invisible from inside the view, so a claim supported across views with independent failure modes is the only kind we are entitled to call real — here is the atlas, the criterion, and an experiment testing it."**

Everything below follows from that. The atlas becomes the *apparatus*; the realism criterion becomes the *reason the apparatus exists*. The reader must know by paragraph two why they should care.

A taxonomy can't fail at anything, which is why v15 reads as a reference document. v16 makes a prediction that can come out false.

---

## 2. Global cuts (do these first)

| Cut | Why |
|---|---|
| **Coverage metric, the ~5% number, composition operator, Szymkiewicz–Simpson coefficient** | Different thesis ("how much does the field explain?" ≠ "when may we believe a mechanism is real?"). It is field commentary, not a result; the number chains three arbitrary choices (harmonic weights, δmax=5, denominator=144 heads) and is the most attackable thing in the cluster. Cutting it also drops the MechKnow self-citation. |
| **Grassmannians, fiber bundles, holonomy** | Attached to the three views nobody has run. Removing them changes **no conclusion in the paper**. That is the test: if deleting a formalism changes no claim, it is decoration. |
| **Multi-context-systems appendix, Levi-contraction entrenchment conjecture** | Explicitly conjectural ("formal proof is future work"); drops the MechRef self-citation. |
| **17-open-problems survey** | Compress to 4–5 that follow from the experiment. |

**Keep δ.** Three lines, does real work, defensible at a whiteboard: *methods have different blind spots; count how many independent blind spots a claim survives.*

**Citation target: MechVal only.** After these cuts, no other in-preparation self-citation should remain.

---

## 3. Section-by-section disposition

| v15 material | Disposition | Notes |
|---|---|---|
| "One head, seven readings" walkthrough | **KEEP — make it the opening** | Best on-ramp in the cluster. Earns the framework in two pages and makes "view" concrete before any abstraction. Upgrade from narrative to quantitative (see §5). |
| Five-axis definition of a view | **KEEP, compressed** | Needed to make "view" precise. ~1pp. |
| Nine-view atlas, full per-view breakdowns (ontology/identity/evidence/formalism/failure-modes/discriminating-experiment) | **APPENDIX** | Body keeps a single summary table. |
| **Occupancy table (ontology × identity, occupied/empty/incoherent)** | **KEEP — and elevate** | This is the answer to "why nine?" It reframes an arbitrary list as the coherent cells of a principled cross-product. Currently buried; it should be a headline figure. |
| Five families + failure modes table | **KEEP — load-bearing** | This is what δ actually needs (δmax = number of families, not views). |
| Determination chain | **APPENDIX** | Good, not story. |
| Methods→views mapping | **APPENDIX**, keep a 3-sentence summary in body | |
| Worked example #1 | **KEEP** | |
| Worked examples #2–3 | **APPENDIX or cut** | |
| Philosophy grounding | **COMPRESS to ~1pp + table**, detail to appendix | Same treatment applied to MechVal's Foundations section. |

---

## 4. Material folded in from Cross-View Invariance

Take **contributions 1 and 2 only** (invariance depth; the realism argument). Contribution 3 (coverage) is cut per §2 — which is what makes the fold clean, with no residue.

Fold in, as the paper's payoff sections:

1. **The artifact problem** — Sutter (unconstrained DAS hits 100% IIA on random models), Leask (SAE features are seed-dependent, not canonical), Franco (patched circuits are prompt-specific). Three results, each undermining one view, none undermining claims that cross views. **This belongs early — it is the motivation for the whole paper.**
2. **Invariance depth δ** — definition, harmonic discounting within families, the consistency constraint. Keep short.
3. **The three-level realism argument** — coherentist confirmation (how much to believe) → structural realism (what the belief is about) → the warrant (convergence is constitutive of the *warrant*, not of the *thing*). Preserve the "constitutive of the warrant, not the thing" distinction verbatim; it is what stops the position being circular.
4. **The audit examples** — induction heads pass (δ≈3.5, three families); a single SAE feature does not (δ=1). Keep both.
5. **Thresholds table** — δ=1 candidate / ≥2 distinct families / ≥3 realism licensed.

---

## 5. New material to write

### 5a. Add a **Feature view** to the atlas
SAE features are currently scored as object-view claims, which is charitable but wrong: they then inherit the object view's failure mode (*role inflation*) when their actual demonstrated failure mode is **decomposition-dependence** (different seeds → different dictionaries; large-dictionary latents decompose into finer ones). By the atlas's own criterion for individuating views — distinct ontology, identity criterion, and characteristic failure mode — a Feature view qualifies.

This *strengthens* the SAE argument: it upgrades "δ=1, no corroboration" (a counting claim) to "this view's characteristic failure mode has been empirically realized" (a mechanism-of-failure claim). Cost: δmax goes 5 → 6 if it forms a new family. Write the entry in the atlas's standard format.

### 5b. **Correct the IOI audit** ⚠ factual error
The CrossView audit scores IOI at δ≈1–1.5 and says "the recommended path to higher δ is a structural-view analysis." **Weight-space/composition-score work on IOI already exists.** So IOI's δ is understated and the recommendation is stale. Verify what structural work exists, recompute IOI's δ, and drop or rewrite the recommendation. A reviewer who knows the IOI literature catches this immediately.

### 5c. **Results section** — the preregistered experiment
See `PREREG_cross_view_predictive_validity.md`. Central claim: *cross-view support predicts mechanistic correctness beyond the best single-view result, method count, and ordinary faithfulness.* Report the scoped Tracr + modular-arithmetic study; the full study is future work.

### 5c-bis. **New section: researcher degrees of freedom across views** (required)
δ is only meaningful if the view-support set was specified *before* looking. Otherwise it measures "how many views I could find that agreed" — a garden-of-forking-paths statistic, and precisely the "flexible scope" / "circuit redefinition" failure modes the framework itself catalogues, turned on the framework. Write a short section covering:

- **The problem stated honestly**, in the paper's own vocabulary.
- **The fix**: a *preregistered* view-support set is severe; a *discovered* one is not. This is the confirmation/corroboration distinction (already in the MechVal severity rule) applied to views rather than criteria — cite MechVal, and note the two papers share one principle.
- **Reporting rule**: report the **specification curve across views** — every view's result for a claim — rather than max δ or the supporting subset. Import from multiverse / specification-curve analysis; note its use in ML to prevent fairness hacking (*One Model Many Scores*, FAccT 2024).
- **Null baselines**: promotion/support rates for random directions and scrambled claims, so "how often does this fire by chance across N views" is measured, not assumed.

### 5c-ter. **Cite the epidemiology precedent** ⚠ currently missing
**Lawlor, Tilling & Davey Smith (2016), "Triangulation in aetiological epidemiology," *Int. J. Epidemiol.* 45(6):1866–1886** — triangulation across approaches whose **key sources of bias are unrelated to each other**. This is the direct precedent for cross-view invariance and its absence is a real gap; a causal-inference reviewer will catch it. Position the contribution as *formalizing triangulation for MI with catalogued failure modes and a measure*, not as inventing it.

Also adopt their **stronger criterion**: triangulation is most convincing when the biases of different approaches would push results in *opposite directions* if those biases were driving the finding. "Failure modes differ" is weaker than "failure modes predict opposite errors." Consider refining family orthogonality accordingly.

### 5d. Make "seven readings" quantitative
Compute each reading on the same head — ablation (object), independent functional test (role), constrained DAS/IIA (subspace), composition score (structural), effect across varied foils (contrastive), training trajectory (process). Report where they agree and diverge, in one figure. Turns the paper's best explanatory device into its central demonstration.

---

## 6. Target structure for v16

1. **Introduction** — the artifact problem (Sutter/Leask/Franco), then the thesis. Reader knows by ¶2 why views matter.
2. **One head, seven readings** — the on-ramp, now with numbers.
3. **What a view is** — five axes, compressed.
4. **The atlas** — summary table + the elevated occupancy table + the five families with failure modes. Full per-view detail → appendix.
5. **Invariance depth and the realism criterion** — δ, the three-level argument, thresholds.
6. **Audit** — induction heads pass; SAE features do not; the corrected IOI case.
7. **Experiment** — preregistered cross-view predictive validity; results; what it revised.
8. **Discussion** — what a researcher does differently on Monday: declare your view, report your view-support set, treat δ=1 as a candidate, don't deploy single-view claims as safety monitors.
9. **Limitations, conclusion.**
10. **Appendices** — nine per-view breakdowns, determination chain, methods mapping, philosophy detail, extra worked examples.

---

## 7. Writing constraints

- **Nothing stays that the author cannot explain at a whiteboard.** Borrowed machinery is a question you are promising to answer.
- No negation-contrast ("not X, but Y") — rephrase positively.
- One idea per sentence; split anything stitched with "while"/semicolons.
- Close every paragraph — no trailing bare citations or "which we detail below."
- Interpret every figure and table; captions self-sufficient.
- Assertive for facts, hedged for mechanisms.

---

## 8. Acceptance check

v16 is done when a reader can answer, without re-reading: *what is the claim, what would falsify it, and what do I do differently on Monday?* If the honest answer to the third is "think more clearly," the edit is not finished.
