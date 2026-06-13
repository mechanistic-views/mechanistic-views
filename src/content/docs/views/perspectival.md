---
title: Perspectival View
---

# Perspectival View

Run activation patching and you get one circuit. Run DAS (distributed alignment search) and you get a different description. Run ACDC (Automatic Circuit DisCovery) and you get a third. The perspectival view says: none of these is "the real mechanism." Each is a valid description relative to the method that produced it. There is no method-independent ground truth to recover.

This is a skeptical position, but not a nihilistic one. It takes measurement seriously — more seriously than the realist views, which treat method disagreement as noise to be averaged out. The perspectival view says method disagreement is informative: it tells you that the "mechanism" looks different depending on how you look at it, which is itself a fact about the model.

## Thesis

A mechanism description is always relative to a measurement procedure. Different methods produce different mechanism descriptions that are equally valid relative to their respective methods.

## What it explains

**Why methods disagree.** Under the perspectival view, disagreement between activation patching, DAS, and SAE decomposition is not a problem to solve — it is evidence that the "mechanism" looks different from different measurement standpoints. The divergence is informative, not noise.

**Why convergence is so valuable.** Cross-method coherence (when methods *do* agree) is the strongest evidence you can get under this view. If methods with non-overlapping assumptions produce the same description, something view-independent is being tracked — which pushes toward a stronger realist view.

**Why "which method found the real mechanism?" may be the wrong question.** If the mechanism genuinely looks different from different measurement standpoints, asking which method found the "real" mechanism may presuppose that a unique answer exists.

## What this view says

The perspectival view denies that there is a method-independent answer to questions like "what is the mechanism for indirect object identification?" There are answers relative to activation patching, to DAS, to SAE decomposition, and to weight-space analysis. These may partially overlap, but they do not all uniquely pick out the same object.

Importantly, this does not deny that the measurements are real. Activation patching and DAS produce real, reproducible results. The perspectival view denies that these results all converge on a unique underlying object called "the mechanism."

The cost is that you cannot make claims about mechanisms independent of methods. You cannot say "the model has an induction head mechanism" — only "activation patching identifies an induction-like circuit" and "DAS identifies an induction-like subspace." For many practical purposes this is fine. For safety-critical applications where you need to know what the model is actually doing independent of your measurement, the perspectival view may be too weak.

This position is consistent with Michela Massimi's *perspectival realism* (Oxford, 2022): scientific representations are perspectival — produced from a standpoint, using a particular instrument or framework — without being merely subjective or arbitrary. The perspectival view differs from relativism: it does not say that any description is as good as any other. Descriptions are evaluated within their measurement context, and convergence across contexts is stronger evidence than any single-context result.

## When it works and when it doesn't

The perspectival view is most useful when methods persistently diverge. If DAS, SAEs, and activation patching all identify different "mechanisms" for the same behavior with no convergence, the perspectival view is the appropriate diagnostic framing: the divergence is real evidence that the methods are picking up different things, and the question "which method found the real mechanism?" may be ill-posed.

It motivates the triangulation and convergence requirements in the stronger views. If distinct methods converge on the same description — same subspace, same cohomology class (a topological invariant measuring global consistency of local descriptions) — that convergence is evidence against the purely perspectival position and pushes toward the [subspace](/mechanistic-views/views/subspace/) or [structural](/mechanistic-views/views/structural/) view.

Its main limitation: you cannot prove theorems about mechanisms. The perspectival view has no formal object to make claims about. It can characterize what measurements show and when they diverge, but cannot make positive claims about what the model is doing independent of measurement.

---

## Technical details

### Evidence

Under the perspectival view, evidence is always relative to a measurement procedure. A claim is warranted if it is robust within its method: reproducible across runs, stable across prompt distributions, and internally consistent. Cross-method convergence is not required for a perspectival claim, but when it occurs, it is evidence that something view-independent is being tracked.

### Formalism

The perspectival view does not commit to a single formalism — that is precisely its point. Different measurement procedures come with their own formalisms: causal graphs for patching, Grassmannian geometry for DAS, cosheaf cohomology for circuit analysis. The perspectival view treats each as a valid language for describing measurement outcomes, not as a description of the mechanism itself.

The [measurement algebra](/mechanistic-views/formalism/measurement-algebra/) formalism captures the perspectival view's emphasis on measurement operations as the primary objects.

### Relationship to Mechanistic Validity

The perspectival view treats all validity as method-relative — there is no mechanism to validate independent of a measurement procedure. This makes construct validity structurally impossible (there is no object to validate the construct of) and collapses most other criteria to "relative to method X."

| Lens | Covered | Possible | Impossible | Score |
|---|---|---|---|---|
| [Construct](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/construct) | — | [C1 Falsifiability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/falsifiability) | [C2 Structural plausibility](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/structural-plausibility), [C3 Task specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/task-specificity), [C4 Minimality](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/minimality), [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity) | 0/5 |
| [Internal](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/internal) | — | [I1 Necessity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/necessity), [I2 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency) | [I3 Specificity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/specificity), [I5 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control), [I4 Consistency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/consistency) | 0/5 |
| [External](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/external) | — | [E4 Effect magnitude](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/effect-magnitude) | [E5 Robustness](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/robustness), [E6 Cross-architecture](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/cross-architecture), [E1 Reach](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/intervention-reach), [E2 Graded response](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/graded-response), [E3 Selectivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/external/selectivity) | 0/6 |
| [Measurement](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/measurement) | [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability) | [M3 Baseline separation](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/baseline-separation), [M4 Sensitivity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/sensitivity) | [M2 Invariance](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/invariance), [M5 Calibration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/calibration), [M6 Coverage](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/construct-coverage) | 1/6 |
| [Interpretive](https://mechanistic-validity.github.io/mechanistic-validity/framework/validity-types_v4/interpretive) | [V1 Level declaration](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-declaration), [V5 Scope honesty](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/scope-honesty) | — | [V2 Level-evidence match](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/level-evidence-match), [V3 Narrative coherence](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/narrative-coherence), [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | 2/5 |

**Why most criteria are impossible.** The perspectival view does not commit to a mechanism existing independent of measurement. Without a mechanism to validate, criteria that ask "is this the right mechanism?" (construct), "does this mechanism generalize?" (external), or "is this mechanism invariant?" (measurement) have no well-defined answer. The view can confirm that a measurement procedure is reliable (M1) and honestly scoped (V5), but cannot confirm that what it measures is real.

### Further reading

- Massimi, *Perspectival Realism* (Oxford, 2022) — the philosophical framework underlying the perspectival view
- For comparison: the [instrumental view](/mechanistic-views/views/instrumental/) is anti-realist about mechanisms entirely, while the perspectival view accepts them as real but method-relative. The [subspace](/mechanistic-views/views/subspace/) and [structural](/mechanistic-views/views/structural/) views are realist — they commit to specific objects that exist independently of any measurement procedure
