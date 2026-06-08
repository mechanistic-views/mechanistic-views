---
title: Object vs. Role
---

# Object vs. Role

**The fork.** When identifying a mechanism, are you identifying the component or the functional role it plays?

## Option A: [Object](/views/object/)

The mechanism *is* the component. Commits you to identity by component overlap. Cross-model claims are component-level.

**When it goes wrong.** If the same role is realized by different heads across seeds, the object view implies each seed has a different mechanism — technically defensible but often missing the scientific point.

## Option B: [Role](/views/role/)

The mechanism is the role. Commits you to functional equivalence under a specified transformation class. The role must be defined precisely enough to predict which component will play it in a new model.

**When it goes wrong.** Vague role definitions explain nothing. "Roughly moves names" is satisfied by any head that weakly affects naming tasks.

## Distinguishing experiments

**Seed comparison.** Do different components play the same role across seeds? If so, only the role view can express cross-seed identity.

**Component transplant.** Replace $h_1$ from $M_1$ with $h_2$ from $M_2$. Preserved behavior implies both realize the same role.

**Role-partitioned circuit search.** Does restricting edge search to role-respecting edges achieve comparable precision and recall? If yes, the role structure is real.

## Recommended default

[Role view](/views/role/) for cross-model claims and multi-seed analyses. [Object view](/views/object/) for precise single-model circuit recovery at early investigation stages. See the [IOI case study](/cases/ioi/) for a concrete example where both views apply to the same circuit.
