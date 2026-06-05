---
title: Formalisms
---

# Formalisms

The views in this atlas reference several mathematical structures not standard in machine learning. These pages introduce each one in enough depth to follow the arguments on the view pages and in companion papers.

The natural dependency order is: **Grassmannian → Gauge and Holonomy → Sheaf Cohomology → Stratification**. Each page is self-contained, but reading in order helps. Undergraduate linear algebra is assumed throughout.

## Pages

- [Grassmannian Geometry](grassmannian/) — subspace geometry, principal angles, $\mathrm{Gr}(k,d)$ as mechanism space
- [Gauge Quotients and Holonomy](gauge-holonomy/) — transformer symmetries, fiber bundles, mechanism fingerprints, and the gauge-physics analogy and its limits
- [Sheaf Cohomology](sheaves/) — circuit cosheaves on directed graphs, cochain complex structure, $H^0$ and $H^1$, base sections
- [Stratification](stratification/) — stratified spaces, Whitney conditions A and B, mechanism space strata, what is established vs. conjectured

## Why these formalisms

**Grassmannian geometry** is needed because DAS identifies a subspace, not a vector. The natural space of subspaces is the Grassmannian.

**Gauge quotients** are needed because transformer parameter space has symmetries preserving function. Mechanism claims should be invariant to these symmetries. The holonomy construction requires care about (i) when the gauge group acts freely (generic position) and (ii) which connection is chosen.

**Sheaf cohomology** — specifically, cellular cosheaf cohomology on the transformer layer graph — is needed because "is this mechanism localizable?" is a question about whether local descriptions can be consistently assembled globally. $H^0$ and $H^1$ measure this. The construction requires linearization around base sections; cohomology depends on this choice.

**Stratification** is needed because mechanism space is not a manifold. Different mechanism types occupy qualitatively different strata with different identity criteria. The Whitney stratification is established for the finite Grassmannian strata; the $\mathcal{M}_\infty$ stratum is a working hypothesis pending further mathematical development.
