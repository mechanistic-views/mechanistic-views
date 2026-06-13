---
title: Object vs. Role
---

# Object vs. Role

**The fork.** When you identify a mechanism, are you identifying a specific component in the network, or the functional role that component plays?

This is the most common implicit decision in interpretability research. Every time someone writes "head 9.1 is the name mover," they have already made it -- they just may not have noticed.

## When you face this decision

Suppose you have found a circuit for indirect object identification (IOI) in GPT-2 Small. You have identified specific heads -- 9.1 and 9.6 as name movers, 7.3 and 7.9 as backup name movers, and so on. Now you train GPT-2 Small again from a different random seed. You run circuit discovery on the new model and find that heads 10.2 and 10.5 are doing the name-moving work.

Are these the same mechanism or different mechanisms? Your answer depends on whether you identify the mechanism with the component (the object view) or the function (the role view).

## Option A: Object view

The mechanism *is* the component. "The IOI circuit" means a specific set of heads and edges in a specific model. Two mechanisms are the same when they share the same components.

**What it buys you.** Precision. You can point to exactly what you found, run ablation experiments on it, and make falsifiable claims about specific parts of the network. Circuit discovery methods (ACDC, activation patching, EAP) produce object-view outputs directly -- directed graphs of components.

**What goes wrong.** If the same function is realized by different heads across seeds, the object view forces you to say each seed has a *different* mechanism. This is technically defensible but often misses the point. If you are trying to understand how transformers solve IOI -- not how *this particular transformer* solves IOI -- the object view cannot express what is shared across seeds. Worse, it makes cross-architecture claims impossible: head 9.1 in GPT-2 does not exist in Llama.

## Option B: Role view

The mechanism is the functional role. "Name-moving" is the mechanism; head 9.1 is one of its realizations. Two mechanisms are the same when they play the same role, defined by a specified class of behavioral tests.

**What it buys you.** Generality. You can make claims like "both models implement name-moving" even when different heads are involved. Cross-seed and cross-architecture comparisons become expressible.

**What goes wrong.** Vague role definitions explain nothing. "Roughly moves names" is satisfied by any head that weakly affects naming tasks. For the role view to have teeth, the role must be defined precisely enough to predict which component will play it in a new model -- and that precision is hard to achieve. A role that is defined only by "does well on the IOI task" is just restating the behavioral outcome, not identifying a mechanism.

## Distinguishing experiments

**Seed comparison.** Train the same architecture from multiple random seeds and run circuit discovery on each. If different components play the same functional role across seeds, only the role view can express the cross-seed identity. If the same components always appear, both views agree and the distinction does not matter for your purposes.

**Component transplant.** Take the name-mover head from model A and splice it into model B (replacing the corresponding head). If model B's IOI performance is preserved, the two heads realize the same role -- a result the role view predicts and the object view cannot naturally express.

**Role-partitioned circuit search.** Constrain your circuit discovery to only consider edges that respect role assignments (e.g., "name mover must receive from S-inhibition head"). If this produces circuits with comparable precision and recall to unconstrained search, the role structure is capturing real computational organization, not just post-hoc labeling.

## Recommended default

Use the **object view** for precise single-model circuit recovery, especially at early investigation stages when you are still mapping out what the model does. It is the natural output of standard circuit discovery tools.

Use the **role view** for cross-model claims and multi-seed analyses, where you need to express "same mechanism, different components." The role view is also better when the goal is scientific understanding of a *class* of models rather than forensic analysis of one. But invest effort in making your role definitions precise and falsifiable -- a vague role is worse than a precise object.
