---
title: Mechanistic Views
subtitle: A reference for the implicit commitments in mechanistic interpretability claims
---

# Mechanistic Views

Mechanistic interpretability produces circuits, features, subspaces, and algorithms. Each of these results rests on implicit assumptions: about what kind of object a mechanism is, what evidence supports the claim, and when two descriptions refer to the same thing. This site makes those assumptions explicit.

The basic unit is a **mechanistic view**: a background account of what mechanisms are, how they are identified, when two mechanisms are the same, and what evidence can justify claims about them. Most interpretability papers assume a view without stating it. Making the view explicit does not settle empirical questions, but it makes the right questions easier to find.

## What this site covers

- **Framework.** What the five axes are, how they differ, and what a view is.
- **Views.** Eight named views, each with full axis assignments, evidence standards, proof consequences, and failure modes.
- **Formalisms.** Mathematical objects referenced by the views: Grassmannians, gauge quotients, sheaves, holonomy, stratification.
- **Decisions.** Five specific forks where the choice of view changes what experiments are appropriate and what can be proved.
- **Cases.** Worked examples on IOI, induction heads, grokking, hallucination, and self-knowledge.
- **Methods.** How common interpretability methods map to view commitments.
- **MechVal interface.** How this site connects to MechVal (Mechanistic Validity) — a companion framework of 27 criteria for evaluating whether mechanistic claims are warranted by evidence.
- **Glossary.** Shared vocabulary.

## The five axes

A mechanistic stance is a bundled answer to five questions. The questions fall into distinct categories:

| Axis | Category | Question |
|---|---|---|
| Ontology | Metaphysical | What kind of thing is a mechanism? |
| Identity | Metaphysical | When are two mechanisms the same? |
| Evidence | Epistemological | What warrants the claim? |
| Formalism | Representational | What math expresses it? |
| Target | Scope | What phenomenon is it a mechanism of? |

## Reading path

Read **framework** first, then one or two view pages. The **cases** section shows the views applied to real examples. The **formalisms** section assumes different backgrounds for different pages. Grassmannian geometry requires linear algebra and basic differential geometry. Gauge quotients and holonomy require familiarity with Lie groups and fiber bundles. Sheaf cohomology requires some algebraic topology. Stratification requires point-set topology. The Grassmannian page is accessible with linear algebra alone; the others benefit from graduate-level background. All pages aim to be self-contained enough to be readable without that background, but some arguments will be opaque without it.

## Relationship to companion work

This site is a companion to two working papers:

- *Mechanistic Validity* introduces 27 criteria for evaluating whether a mechanistic claim is warranted by evidence.
- *The Geometry of Mechanisms* develops the Grassmannian SCM, the No-Free-Lunch Triangulation Theorem, and geometric invariants for mechanism identity.

This site addresses a different question: what background assumptions make a mechanism claim well-defined?

## How this relates to existing literature

**Mechanistic interpretability.** The immediate context is the interpretability literature: Elhage et al. (2021) on transformer circuits, Olsson et al. (2022) on induction heads, Wang et al. (2023) on IOI, and the broader program of circuit-level analysis. This site provides the conceptual scaffolding for evaluating and comparing the claims made in that literature.

**Philosophy of science.** The questions asked here about mechanism identity, evidence warrant, and explanatory levels correspond directly to debates in the philosophy of mechanistic explanation (Machamer-Darden-Craver, Craver, Woodward), perspectivalism (Massimi), and the epistemology of scientific models. The site uses that literature without requiring familiarity with it. Key terms are defined when they first appear.

**Mathematics and physics.** The formalisms section draws on differential geometry (Grassmannians, fiber bundles), algebraic topology (sheaf/cosheaf cohomology), and the geometry of stratified spaces (Whitney conditions, Thom-Mather theory). The physics section of the gauge page describes connections between transformer gauge symmetry and gauge field theory. These tools are used because they are the right tools for the objects being studied, not as illustration.

**Measurement theory.** The evidence and validation standards used here have connections to psychometric validity theory (construct validity, criterion validity, external validity) as applied to the specific case of mechanistic claims about trained neural networks.

**Cognitive science and neuroscience.** The localized-vs-distributed debate in this site mirrors a long-standing debate in cognitive science and systems neuroscience: localizationism (specific functions are implemented by specific brain regions or circuits) versus holism or distributed coding (functions emerge from patterns of activity across large populations). The double dissociation methodology in neuropsychology — showing that two functions can be selectively impaired or preserved independently — is the nearest analogue to the necessity and sufficiency tests used here. The causal Bayesian network tradition (Cheng, Waldmann, Pearl) provides the formal framework for the interventionist semantics used in the subspace view. Readers from these fields will find the conceptual problems familiar; the main novelty here is that the mechanisms are inside a trained neural network whose architecture is precisely known, which makes some questions more tractable and others (like the absence of spatial structure) more difficult.

## Working assumption

The views are presented neutrally at the atlas level. The current working hypothesis is that **stratified structural realism** handles the widest range of cases and supports the strongest theorems. That argument is built through the formalisms and case studies, not assumed from the start.
