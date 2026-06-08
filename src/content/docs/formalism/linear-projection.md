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

The limitation: observational only. A [logit lens or tuned lens](https://learnmechinterp.com/topics/logit-lens-and-tuned-lens/) reading shows what information is linearly accessible at each layer, not what the model actually uses. Two layers can show the same logit lens output while playing different causal roles in the computation.

## Relationship to other formalisms

The unembedding projection $W_U$ defines a preferred frame for reading off vocabulary-level predictions. The [Grassmannian](/formalism/grassmannian/) formalism generalizes this: instead of projecting onto the unembedding basis, it considers arbitrary subspaces of the residual stream. The [linear classifier](/formalism/linear-classifier/) is another observational formalism, but tests for binary concept presence rather than vocabulary-level readout. See the [methods page](/methods/) for how [logit/tuned lens](https://learnmechinterp.com/topics/logit-lens-and-tuned-lens/) fits into the evidence landscape.
