# MechViews — turning the taxonomy into results (parked plan)

Goal: the atlas currently can't fail at anything. Each study below makes a prediction that could come out false.

## Study 1 — Test failure-mode orthogonality (highest intellectual value)
δ depends on "views have orthogonal failure modes," which is asserted and is your own open problem #2.
**Run:** manufacture claims you *know* are artifacts (e.g. a circuit found by patching on a deliberately narrow prompt distribution, Franco-style), then check whether the artifact also gets support under structural / subspace / process views.
**Outcomes, both publishable:** artifacts don't propagate → orthogonality validated, δ's foundation goes from asserted to tested. Artifacts do propagate between some pairs → those views are correlated, δ overcounts, weights need revising (the more interesting result).

## Study 2 — View promotion on a real claim ⚠ NEEDS A NEW EXAMPLE
Original idea: do the structural-view analysis of IOI that CrossView *recommends* rather than recommending it.
**PROBLEM (Elliot, correct):** IOI has already had composition-score / weight-space work done on it. So this is not a fresh promotion.
**Two consequences:**
1. Pick a different target claim — one that genuinely sits at δ=1 with no structural/process evidence yet. (Perplexity search pending.)
2. **Fix CrossView itself:** if IOI already has structural-view support, its δ in the audit (1–1.5) is *understated*, and the "recommended path to higher δ is a structural-view analysis" line is stale. This is a factual error in the paper independent of which example we choose.

## Study 3 — Occupancy survey (cheapest; do first, no GPU)
**Run:** classify ~100–150 MI papers by view using the atlas criteria; report the distribution + inter-rater agreement with a second rater.
**Buys:** a quotable field-level number ("the field occupies N of 9 views"), converts "why these nine?" from philosophical objection to empirical claim, evidences the ontology × identity occupancy table, and the IRR checks whether view assignment is operational at all.

## Study 4 — "One head, seven readings" quantified
**Run:** compute all seven readings on the same head — ablation (object), independent functional test (role), DAS/IIA (subspace), composition score (structural), effect across baselines (contrastive), training trajectory (process).
**Buys:** turns the best on-ramp into the central demonstration — "the same head is load-bearing under four readings and negligible under two, here is which measurement disagrees with which," in one figure.

## Recommended package
Study 3 (field result) + Study 4 (centerpiece) + one of Study 1 or 2 (the experiment).
Thesis shifts from "here is an atlas" to "MI occupies N of 9 views, single-view claims are indistinguishable from artifacts, and here's what happened when we promoted one."

## Parked question — make the 5% coverage number defensible
Currently chains three soft choices: harmonic weight heuristic, δmax = 5, denominator |M| = 144 heads. Options to harden it:
- Report a **sensitivity analysis**: coverage under several weight schemes and denominators; show the qualitative conclusion (single-digit %) is invariant even if the point estimate isn't.
- Replace the chosen 0.5 containment threshold with a swept curve.
- Ground δmax empirically from Study 1 (measured failure-mode correlation) instead of "number of families."
- Or state it as an explicit **order-of-magnitude bound**, not a measurement.
Fallback if the composition formalism gets stripped: keep only the qualitative claim — "fifty IOI papers do not produce fifty units of understanding, because they overlap" — which survives any weighting.
