---
title: Linear Projection
---

# Linear Projection

A method-level formalism used by the logit lens and tuned lens.

## What it is

A linear projection maps a vector from one space to another via a matrix multiplication: $y = Wx + b$. In the context of transformers, the key projection is the unembedding matrix $W_U$, which maps residual stream vectors to logits over the vocabulary.

See [Projection (linear algebra)](https://en.wikipedia.org/wiki/Projection_(linear_algebra)) on Wikipedia.

## How it is used in interpretability

The **logit lens** applies the model's unembedding matrix $W_U$ to intermediate residual stream states — at each layer, it projects the current residual stream into vocabulary space to see what the model "would predict" at that point. The **tuned lens** learns an affine transformation per layer to improve this projection, accounting for the fact that intermediate representations may not be in the same basis as the final residual stream.

Both methods provide a layer-by-layer readout of how the model's prediction evolves through the network. They are observational — they read off information without intervening — and they assume that the unembedding direction (or a learned affine transformation of it) is a meaningful frame for interpreting intermediate representations.

The limitation: observational only. A logit lens reading shows what information is linearly accessible at each layer, not what the model actually uses. Two layers can show the same logit lens output while playing different causal roles in the computation.
