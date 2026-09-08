---
title: View Mappings
---

# View Mappings

How the nine views relate to each other, and how other positions in the interpretability literature map onto them.

## Ontological commitment ordering

![Views ordered by ontological commitment](/mechanistic-views/figures/views-pyramid.svg)

## View families

The nine views group into five families, where membership is fixed by *primary failure mode*: two views belong to the same family when one methodological error corrupts both. The **Identity family** (Object, Role; failure: role inflation), the **Mathematical family** (Subspace, Structural; failure: alignment vacuousness), the **Process family** (Process; failure: training-detail overfitting), the **Pragmatic family** (Instrumental; failure: safety-relevant overreach), and the **Analyst-choice family** (Contrastive, Perspectival, Stratified; failure: analyst-choice dependence — each individuates mechanisms relative to a parameter the analyst sets).

![Views organized by family](/mechanistic-views/figures/nine-views-families.svg)

## Ontology determines identity determines formalism

Each view's ontological commitment implies a specific identity criterion, which in turn implies a specific ambient formalism. The chain is mostly one-to-one: if mechanisms are causal subspaces, identity is geodesic proximity on $\mathrm{Gr}(k,d)$ and the formalism must include Grassmannian geometry; if they are gauge-invariant structures, identity is orbit membership and the formalism must include fiber bundles. The one loose case is loose for a reason: a role is a universal that different components realize, so a formalism naming a particular realizer would contradict the ontology it expresses. Evidence and target are constrained but not determined, so the chain has two free parameters once the ontology is fixed.

![Three-column chain: Ontology → Identity → Formalism](/mechanistic-views/figures/ontology-identity-formalism-v2.svg)

The diagrams encode a philosophical gradient. The three lowest-commitment views — Instrumental, Contrastive, and Perspectival — make no claim that circuits or features are real objects in the model: the Instrumental view treats them as useful fictions, the Perspectival view as method-relative projections, and the Contrastive view as patterns relative to an analyst-chosen foil. The six higher-commitment views make progressively stronger realist claims, culminating in the Stratified view's assertion that mechanisms have resolution-dependent structure that exists independent of any particular measurement. The ontology-determines-identity chain shows why this matters: each view's ontological stance locks in what counts as evidence, what counts as the same mechanism, and what mathematical language is natural. Mixing commitments from different views without recognizing the mismatch is a common source of confusion in the interpretability literature.

In practice, these diagrams can be used as a lookup table: find the view that matches your method, and the chain tells you what identity criterion and formalism follow. If your method targets architectural components, you are in the Object view; if it targets learned subspaces, you are in the Subspace view. Making this explicit avoids the common failure of collecting evidence at one level while drawing conclusions at another.

## Other positions in the literature

:::note
This content is not included in the paper.
:::

Several coherent positions appear in the interpretability literature that are not listed as separate views here. In each case, we argue the position maps onto one of the nine views, adds a constraint to an existing view, or lacks practical methods for trained models.

**Algorithmic** (RASP, Tracr). Treats mechanisms as formal programs the network implements. A coherent philosophical position, but the only cases where "this network implements algorithm X" can be verified are toy models or very simple circuits where the algorithm is already obvious. For real models, the computation is too distributed and approximate to extract a clean program. Algorithmic claims about trained models reduce to detailed role descriptions in practice.

**Information-theoretic** (mutual information bottlenecks, probing-as-compression). Defines mechanisms as information channels between input and output variables. This collapses into the **[Perspectival view](/mechanistic-views/views/perspectival/)**: what you find depends on your choice of MI estimator, partitioning scheme, and layer — the "mechanism" is relative to the measurement procedure. Information theory is listed as a cross-cutting formalism rather than a view for this reason.

**Distributed / superposition** (Elhage et al. "Toy Models of Superposition"). Claims that mechanisms are overcomplete codes spread across many dimensions simultaneously. This is not a separate view but a negative result within the **[Object view](/mechanistic-views/views/object/)**: it shows that clean component-level decomposition fails in certain regimes. The positive version — "the mechanism is the interference structure itself" — is a **[Subspace view](/mechanistic-views/views/subspace/)** claim about the geometry of overcomplete representations.

**Representational similarity** (CKA, RSA, SVCCA). Identifies mechanisms with representational geometries: two layers or models have the "same mechanism" when their representations have high CKA or RSA similarity. This is the **[Subspace view](/mechanistic-views/views/subspace/)** with a different metric. CKA compares subspaces; RSA compares geometry within subspaces. The ontological commitment is the same — mechanisms are geometric properties of representation spaces.

**Compression / MDL** (minimum description length, pruning-as-compression). Defines the mechanism as whatever survives optimal compression. This makes no claim about what the mechanism *is*, only that it is predictively necessary — exactly the **[Instrumental view](/mechanistic-views/views/instrumental/)**.

**Concept bottleneck** (TCAV, Network Dissection, concept bottleneck models). Treats mechanisms as human-interpretable concepts used as intermediate variables. This is the **[Role view](/mechanistic-views/views/role/)** with an additional constraint: the role must be human-legible. It does not require a new ontology — a concept is a functional role that happens to align with a human category. It can also appear as the **[Subspace view](/mechanistic-views/views/subspace/)** plus interpretability (the concept is a direction in activation space that aligns with a human-meaningful axis).

**Phase transition / modularity** (grokking, induction head formation). Claims that mechanisms emerge at specific training loss thresholds as discrete phase transitions. This is the **[Process view](/mechanistic-views/views/process/)**: a phase transition is a feature of the formation trajectory — the point where a qualitative change occurs along the training dynamics. The dynamical systems formalism already covers bifurcations and critical transitions.
