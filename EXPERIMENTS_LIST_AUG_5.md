# MechViews — experiments and v19 plan

Written after a session that ran three hostile reviews over proposed v19 additions.
Headline: **v18 survived all three.** Every problem found was in LLM-generated material
about the paper, not in the paper. v19 is small.

## How to read the evidence claims in this file

- **[V]** — I grepped the string in a locally held PDF. Path and line given.
- **[S]** — secondary: a source that page-cites the original, or a subagent that read the
  PDF and reported line numbers. Reliable enough to plan on, not to quote.
- **[U]** — unverified. Relayed from an LLM summary. Do not print.

## Two claims in this file were wrong earlier and are now corrected

1. I said Cao & Yamins have a worked over-resolution case. **They do not.** Their L5PC
   7-layer MLP fails 3M++ "because it does not satisfy a model-to-mechanism mapping…
   the components of the MLP do not map to real-world components"
   (`reference/philsci/cao_yamins_part1.txt:1243-1246`) **[V]**. That is
   non-correspondence, a different failure. **There is still no worked over-resolution
   case in any source, including ours.**
2. I said Kuorikoski & Marchionni support the per-view commensurability restriction.
   **They pose the problem and answer it the opposite way** — comparability is
   case-by-case empirical, needing "only (preferably controlled) covariation," and their
   account is "silent" on hypothesis-to-hypothesis comparison (p. 243) **[S]**. Cite for
   the problem, never the solution.

If a reviewer finds a third error of this kind, treat the whole file as needing re-check.

---

## Part 1 — v19 scope. Four items, two already done.

| # | Item | Status | Cost |
|---|---|---|---|
| 1 | Stratified rewritten: philosophy + three measurements, Whitney demoted to a footnote | **DONE** in `paper/mechviews_v19.tex` | — |
| 2 | Franco 2026 corrected in both places (components are *reused*, signals differ) | **DONE** | — |
| 3 | Promote the position statement | todo | half a day |
| 4 | Add Woodward | todo | an afternoon |

**On (3).** "The paper is pluralist" appears at lines 1567 and 1722, and nowhere in the
abstract or introduction **[V]**. A reader reaches page 30 before learning the stance.
Move one sentence forward. Both existing sentences are negation-contrast ("the goal is not
to collapse … but to make"), so rewrite positively while moving.

**On (4).** The paper uses interventionist vocabulary throughout and cites Woodward zero
times **[V]**. `woodward2003` sits unused in `paper/references.bib`; Woodward 2010 is at
`reference/philsci/woodward_2010_causation_biology.pdf`. v19 uses a hand-maintained
`thebibliography` block (lines 1746–2126), so new citations are hand-written `\bibitem`s;
the `.bib` file is not wired in **[V]**.

**Not in v19, and why.** The resolution-matching section, the fat-handedness sorting, the
15-claim audit, and the expanded position statement stay staged. Full reasons with
file:line provenance are in the headers of `paper/draft_v19_positioning.tex` and
`paper/draft_v19_resolution.tex`.

Short version: **the paper already states the resolution thesis as an axiom.** Coherence
condition (ii), lines 386–390: "Evidence that discriminates within an identity class is
tracking a finer-grained ontology than the one declared" **[V]**. That is over-resolution
relative to a declared identity criterion. Nothing to add.

---

## Part 2 — the three refuted claims. Recommended paper update.

MechVal v15 lines 810–814 assembles these, with the contesting paper for each **[V]**:

| Claim | Contested by | What failed |
|---|---|---|
| "Gender bias circuit" | Vig et al. 2020 excluded the definitionally gendered items that would test it | bias never separated from gender competence |
| "Knowledge neuron" | Niu et al. 2024 | same editing machinery moves non-factual linguistic regularity |
| "SAE feature" | Heap et al. 2025 | the instrument cannot distinguish a trained transformer from a random one |

All three failed the **same** criterion — discriminant validity, C4 in MechVal.

**Views already has all three as appendix case studies**: D.1 SAE Features, D.2 Gender
Bias Circuits, D.3 Factual Recall and Knowledge Editing **[V]**. Do not write new sections.

**Write one paragraph connecting them.** The Views-specific point, which MechVal cannot
make: each named a construct and never specified its foil. Gender bias *compared to what* —
gender competence? Knowledge *compared to what* — other linguistic regularity? Feature
*compared to what* — a property of the dictionary? Under the contrastive view a mechanism
is individuated by its foil set, so a construct with an unstated foil has no identity
criterion, and there is nothing for evidence to track. The three failures are one failure:
an undeclared contrastive commitment, found later by someone who supplied the missing foil.

One hour, no new material, turns three scattered appendix entries into a result. Highest
value-per-effort item here. Home: end of §7 Using the Framework, or a fourth worked example.

---

## Part 2b — the promotion case. Second recommended paper update.

From `mechanistic-validity/docs/HANDOFF_view_promotion_to_views.md`.

**The gap.** Views Open Question 2 says cross-view promotion conditions exist but "a
systematic account of inter-view inference is missing." §Cross-View Promotion supplies
conditions with no worked case.

**The case, self-contained, does not need the ACH matrices.** An object-level result
promotes to a role-level result **for those components whose role has a specification
independent of the procedure that found them.**

- *Name moving passes.* The OV copy score is a weight-level property, so "this head copies"
  is specified without reference to the ablation that found it.
- *S-inhibition fails.* The origin paper states the attention patterns are not understood,
  so the role name carries content the evidence does not supply.

One claim, two roles, two standings — invisible in an object-level report where both are
members of a head set. Narrower than a systematic account, and more than §Promotion has.
Views already cites Wang, so no new sources.

**Do not move the ACH matrices.** (i) The scoring defect travels: a hypothesis accrues
inconsistencies only when someone runs experiments against it, so the least-examined column
wins. (ii) One claim cannot demonstrate a nine-view taxonomy — six of nine views have no
published hypothesis for IOI, so a reader concludes the views were carved to fit the three
that populate.

**Related, verified.** Wang et al. define faithfulness as |F(M)−F(C)|, lower is better, and
call the naive circuit "comparable to the full circuit C"; it separates only on the
completeness tests **[S]**. So "rival head sets reach comparable faithfulness" is citable to
the origin paper. Views does not currently make this claim — every "faithfulness" hit in
v19 is chain-of-thought **[V]** — so nothing needs fixing, but this is the source if it is
ever used.

---

## Part 3 — experiments, ranked

Every experiment in the earlier planning material was *descriptive* — apply the framework,
report what it says. None could fail. These can.

**Design problems fixed in this revision:** experiment A had no defined outcome variable
and n=6; experiment B rested on arbitrary sameness thresholds and mixed incomparable row
types; experiment C used a single principal angle where a spectrum is needed; experiment D
had a falsification condition that fires on a degenerate case. All four are addressed
below. If any still looks underpowered to you, it probably is — say so before running it.

---

### A. Contested-claims retrodiction — cross-view vs cross-level convergence

**Claim tested:** convergence across views is evidence of robustness.

**The outcome variable, pre-specified.** "Contested" means *a subsequent peer-reviewed
paper argues the original claim does not hold as stated.* Not: fewer citations, not
informal skepticism, not a replication with different numbers. Under that rule the three
in Part 2 qualify, each with a named contesting paper. The rule must be written down before
any coding, because it is the parameter that would let you fool yourself.

**Population, and the honest problem with it.** Three refuted claims against a handful of
survivors is n≈6, which cannot discriminate two axes. **Do not run it that way.** Use
MechVal's full audited set — 16 claims, already scored criterion-by-criterion — as the
population, and code every one of them on both convergence axes. n=16 is still small, and
the claim this supports is correspondingly modest.

**What it can and cannot show.** With n=16 this is a structured comparison, not a
hypothesis test. It can show a pattern worth reporting and worth someone else testing at
scale. It cannot establish that convergence predicts survival. Report it that way or a
statistician referee will do it for you.

**Design:** two axes, not one. Cross-view holds the level fixed and varies the view.
Cross-level holds the view fixed and varies the level. Score each claim on both at time of
publication — using only evidence available then, which is the part that makes it a
retrodiction rather than a rationalization.

**Falsifies if:** contested and surviving claims are indistinguishable on both axes.

**The confound to state up front:** contested claims are contested partly because someone
bothered to check them, and prominent claims get checked more. Cross-view convergence may
track prominence rather than robustness. There is no clean fix at this n; name it.

**Cost:** no compute. Reading and coding.

---

### B. Identity-criterion disagreement — as rank correlation, not thresholds

**Claim tested:** one explanandum supports several inequivalent identity criteria at once.

**Named opponent:** Fang & Zhang, *Erkenntnis*, at
`reference/philsci/fang_zhang_2024_proportionality.pdf` — "there is a **unique**
proportional cause-variable according to Definition 6 for a given effect-variable"
(`:432-434`) **[S]** — reported by a subagent that read the PDF; I have not read it myself.
Read it before writing the opposing paragraph.

**The threshold problem, and the fix.** The earlier version asked for same/different cells,
which needs a sameness threshold per criterion, and every such threshold is arbitrary.
Drop them. Two criteria are equivalent iff they induce **the same ordering** over pairs.
So: compute each criterion's continuous similarity for every pair, then take rank
correlation between criteria across pairs. Spearman ≈ 1 means the criteria are the same
criterion in different clothing. Low or negative means they are inequivalent, which is the
claim. **No thresholds, so almost nothing to pre-register.**

**Separate the row families — the earlier version mixed them and that was a real error.**
These are different kinds of sameness question and pooling them manufactures disagreement:

- *Same model, same task, different prompt distribution* — ABBA vs BABA (Franco 2026)
- *Same model, same task, different run* — two seeds (Bali, ≈0.70)
- *Same model, different task* — IOI vs Colored Objects (Merullo, 78% overlap)
- *Different model* — across scale (Tigges); within- vs across-family (Sun & Toneva,
  0.73–0.92 vs 0.13)

Run the rank correlation **within** each family. A criterion pair that agrees within
families and disagrees across them is telling you something about scope, not about identity.

**Criteria as columns:** component overlap (IoU), role equivalence (behavioral agreement
under matched intervention), subspace distance (Grassmannian), gauge-orbit membership.

**Falsifies if:** rank correlation is near 1 within every family. Then the criteria are
notational variants, Fang & Zhang are right, and you report that.

**Cost:** near zero new compute — published numbers plus existing JS / DAS / CKA results.

---

#### B-row already published: Chen et al. 2026

`mechanistic-validity/reference/chen_2026_circuits.pdf` (+ `.txt`), "All Circuits Lead to
Rome," arXiv:2605.12671. In MechVal's bib as `chen2026circuits` — surnames only, no
initials, fix before either paper ships.

Two IOI circuits both meeting "standard sheaf quality criteria, despite having only a
**4.1% IoU**" (`:304`) **[V]**. Under component-overlap identity, two mechanisms. Under
role identity, one.

**Two caveats, and the first one is mine to own.** The role-identity verdict here is **not
independent evidence** — the search *required* faithfulness, so functional equivalence is a
constraint of the method rather than a finding. What Chen establishes is that low-overlap
faithful circuits **exist**. That is enough to refute a uniqueness theorem, since
uniqueness falls to a single counterexample regardless of how it was found. It is not
enough to show that criteria disagree in the wild. Use it for the first, not the second.

Second: both circuits came from a search that explicitly penalises structural overlap, so
Chen does not show that independent methods naturally diverge. Do not use it for that.

The sharper result (`:122-126`) **[V]**: an ultra-sparse **three-edge** sheaf for IOI where
"no single component is indispensable: removing any of the three edges still allows the
discovery of high-quality sheaves," ruling out "even a weakened form" of essential
components. Object-view identity failing on its own terms — and this one is not an artifact
of the overlap penalty.

#### ⚠ The threat, which needs an answer in the paper

Chen et al. state a version of the MechViews thesis with a theorem behind it (`:107-112`)
**[V]**:

> "should no longer be interpreted as identifying **the** mechanism underlying a task.
> Rather, each discovered circuit or sheaf represents **one valid realisation among many
> within a larger space of functionally equivalent mechanisms**… a naively reductionist
> view—where task behaviour is attributed to a single sparse and indispensable
> subgraph—is insufficient"

Plus a Distributive Dense Circuit Hypothesis with "a theoretical analysis demonstrating
that non-unique, low-overlap circuit explanations arise naturally from high-dimensional
superposition under mild assumptions."

A referee will ask what MechViews adds. **The answer, which must be in the paper:** Chen
shows the multiplicity is *dense and distributed* — many mechanisms, explained by
superposition. MechViews claims it is *structured* — the alternatives are different
identity criteria, and which one is in use is a declarable commitment. "There are many
mechanisms" and "the many have a taxonomy" are different claims, and the second survives
the first being true. Write that paragraph before submission.

This also fills the empty column in the ACH work: the distributed hypothesis previously had
no paper defending it.

#### Chen is also a coherence-violation example

Zero hits for stalks, restriction maps, cohomology, sheaf Laplacian, presheaf, Hansen,
Ghrist **[V]**. "Sheaf" is inherited from DiscoGP (Yu et al. 2025) as "a subgraph that both
causally contributes to the computation and can independently sustain task performance."
No sheaf mathematics is used.

Coherence condition (iii) requires the formalism be expressive — every ontological object
has a representation and identity can be checked within it. A declared formalism doing no
work fails it. A live instance for the coherence-violations table, better than a
hypothetical. **Do not add a sheaf view to the atlas on this paper's vocabulary** — a
referee who knows sheaf theory would catch it, and Views is the worst place to be caught
borrowing formalism.

---

### C. Bias / grammar subspace separation

**Views already specifies this**, in the gender-bias case study: *"No published DAS
analysis has trained separate bias and grammar probes and measured the principal angle
between their subspaces."* **[V]**

**Design correction:** for subspaces of dimension k>1 a single principal angle is the wrong
summary — compute the **full principal-angle spectrum** and report it. The relevant
quantity is how many directions are shared, not whether the closest pair of directions is
close. A pair of 8-dimensional subspaces sharing seven directions and differing in one has
a small first principal angle and is nearly the same subspace; sharing one and differing in
seven has the same first angle and is not.

**Reads out as:** many small angles → substantially shared subspace → a linear intervention
on bias moves grammar, which is the C4 failure MechVal accuses Vig et al. of never testing.
Mostly large angles → separable, surgical intervention available.

**State the null:** two probes trained on *any* two linguistic properties over the same
representation will share some directions. Report the spectrum against a baseline pair of
unrelated properties, or the result has no scale.

**Cost:** one measurement on infrastructure that exists.

---

### D. DAS seed-pair comparison — subspace identity vs role identity

**Claim tested:** the two criteria come apart in practice.

**Design:** run DAS repeatedly on one target, varying seed, k, and hook point. For each
pair of solutions compute (i) the principal-angle spectrum between learned projectors and
(ii) IIA agreement on matched counterfactuals. Look for pairs with high IIA agreement and
large subspace distance — same role, different subspace.

**Precondition, which the earlier version missed.** If DAS converges to essentially the
same subspace every run, both measures are high and flat and the experiment is
uninformative — that is a degenerate outcome, not a falsification. **Check first that there
is variance in the subspace distances.** If there is not, report that DAS is stable and
stop; that is a publishable negative about DAS, not about identity criteria.

**Falsifies if:** given variance in subspace distance, IIA tracks it monotonically.

**Cost:** DAS infrastructure exists; a sweep plus two distance computations.

**Note:** this is a row of experiment B's *same model, same task, different run* family.
One run, two results.

---

### E. Construct a view in an empty cell

**Claim tested:** the occupancy table is generative rather than post-hoc.

**Design:** pick a cell the table marks "coherent but currently unpopulated," define a
working view there — ontology, identity criterion, evidence type, formalism, target — and
apply it to one real claim.

**Falsifies if:** you cannot, or the constructed view collapses into an existing one under
inspection. Then "coherent but unpopulated" is doing no work and the table caption should
say so.

**Cost:** a day of thinking, no compute.

**Why it matters:** the strongest available answer to "why these nine views," and the
cheapest experiment on this page.

---

### F. Two-rater reliability, minimal version

Two or three people independently code the same ten claims into views; report agreement
with a chance-corrected statistic, not raw percent. The first thing a reviewer asks of any
coding scheme. Do this rather than the community-labeling study, which needs recruitment
and weeks.

---

## Part 4 — not doing, and why

- **Prospective preregistration of predictions about future MI results** — cannot resolve
  before submission, so it ships as a promise rather than evidence. (Distinct from
  preregistering experiment A's coding rule, which should be fixed in advance.)
- **Synthetic ground-truth view-disagreement dataset** — weeks, and reads as contrived.
- **Community labeling with recruitment** — right idea, wrong timeline. See F.
- **Cross-domain audits (neuroepi, chemistry, pQTL)** — MechRef's burden, and they dilute an
  MI-scoped paper.
- **True-Jacobian / weight-space work** — belongs to the weights paper.
- **The 32-framework survey appendix** — never described, sourced, or justified in any
  planning material. Cut unless it earns its place.

---

## Part 5 — if you only do three things

1. The paragraph in Part 2. One hour, no new material, turns three appendix entries into a
   result.
2. Part 1 items 3 and 4 — position statement forward, add Woodward. A day, and v19 is
   submittable.
3. Experiment E. A day of thinking, no compute, and it answers the "why these nine"
   question that every reviewer will ask.

Experiment A is the one that could have gone against you, but it needs the 16-claim
population and the coding rule fixed first, so it is a week rather than an afternoon.
Everything else keeps.
