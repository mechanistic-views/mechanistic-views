# A List of 45+ Mech Interp Project Ideas from Apollo Research's Interpretability Team

Source: https://www.alignmentforum.org/posts/KfkpgXdgRheSRWDy8

## Overview

Apollo Research's interpretability team compiled a comprehensive list of mechanistic interpretability (mech interp) project ideas after completing several projects. The authors note that while previous lists like Neel's "200 Concrete Open Problems" were valuable, "many project ideas in that list aren't an up-to-date reflection" of current research frontiers.

**Key disclaimers:**
- Projects vary in specificity and scope
- Not all team members endorse every project with equal priority
- Multiple team members typically support each listed idea
- Projects span multiple categories

## Foundational Work on Sparse Dictionary Learning

### Transcoder-Related Projects

**Training and releasing high-quality transcoders** involves developing top-k transcoders, with GPT-2 as a primary candidate and exploration of smaller models.

**Tooling for transcoders** includes creating programming APIs for attribution analysis and potentially developing web interfaces with Neuronpedia.

**Circuit analysis using transcoders** entails examining random input sequences and summarizing pathway findings and error term attribution.

**Cross-layer superposition** investigation would identify specific examples by searching for features with similar decoder vectors.

**Improving transcoder architectures** proposes adding linear bypass terms and coordinating sparsity penalties across multiple layers.

### Other Foundational Projects

**Logit lens improvements for SAE features** suggest training high-quality SAEs at the residual stream pre-unembed layer and interpreting features through logit effects.

**Toy models of feature splitting** would explore two hypotheses: higher-dimensional manifolds chunked discretely, or discrete but highly-related features.

**Opposing feature directions** investigates whether SAEs learn opposite-facing direction pairs when representing subspace-like features.

**Activation shuffling analysis** examines the impact of not shuffling activations during SAE training, particularly for end-to-end approaches.

**SAE/Transcoder initialization** studies various initialization strategies and their effects on training efficiency.

**Public benchmarks for SAEs and transcoders** would create centralized evaluation infrastructure, potentially hosted by Neuronpedia.

**Mixture of Expert SAEs** could leverage hierarchical feature structure and accelerate both encoder and decoder inference.

**Canonical features identification** explores whether consistent features emerge across different model sizes, architectures, and datasets, similar to edge detectors in vision.

**SAE generalization studies** assess how models generalize across different data distributions and contexts.

**Layer norm effects on features** investigate how normalization transforms feature representations before and after application.

**Connecting SAE features to polytopes** would explore compositional relationships between sparse features and polytope-based representations.

**Feature verification based on model weights** would demonstrate that features are model properties rather than dataset artifacts.

**Feature splitting structure** examines whether splitting patterns reveal underlying compositional principles.

**SAE geometry analysis** includes PCA on SAE activations, studying number embeddings, subset relationships, and subspace organization.

**Better sparsity penalties** would derive improved penalties by analyzing expected feature activation distributions.

**Interaction basis preprocessing** suggests rotating activations before SAE training to emphasize output-relevant dimensions.

**Attribution sparsity penalties** proposes refining end-to-end SAE training with improved attribution-based penalties.

## Applied Interpretability

**Vision network analysis** proposes applying SAEs/transcoders to convolutional networks like AlexNet to complete detailed understanding of seminal architectures. The project would develop convolutional sparse autoencoders with specific weight shapes and training procedures.

**Multimodal interpretability interfaces** seeks methods for visualizing and understanding audio, video, and other modalities, building on approaches like "Interpreting OpenAI's Whisper."

**Continuing Whisper interpretation** extends existing audio model analysis.

**Backdoor detection** investigates whether mechanical interpretability methods can detect backdoors without access to backdooring distributions.

**Mamba/SSM interpretation** applies sparse dictionary learning to state-space models.

**Low-level vision geometry** characterizes structural properties of early-layer vision features through Fourier analysis and other quantitative methods.

**First sequence index understanding** attempts to mechanistically reverse-engineer how transformers process the first non-BOS token, as a stepping stone to more complex sequences.

**Complete toy model understanding** measures how well we can explain small language models like TinyStories through identified mechanisms.

**Complete layer-by-layer model understanding** seeks to map connections between transcoder features across adjacent layers in small models.

## Intrinsic Interpretability

**Bilinear transformer analysis** would train bilinear transformers and use sparse dictionary learning to understand features in terms of closed-form solutions.

**Interpretable inference** explores converting trained models into more interpretable forms through techniques like 1-bit weights, mixture of experts, bilinear layers, Mamba models, or sparse attention patterns.

**Mathematical framework for linear attention** extends existing transformer circuit formalization to linear attention mechanisms, potentially yielding analytical expressions.

## Understanding Features (Non-SDL)

**Auto-interpretability scoring** proposes finding features by directly optimizing for human interpretability through iterative LLM-based labeling.

## Theoretical Foundations

### Singular Learning Theory (SLT)

**SLT at finite data/precision** seeks to extend singular learning theory from infinite-data limits to practical finite-data scenarios.

**Bounding local learning coefficients** proposes using Hessian null space rank to obtain lower bounds on learning coefficients, with implications for model degeneracy.

**LLC and behavioral LLC relationships** would clarify connections between training-loss-based learning coefficients and output-based measures.

### Other Theoretical Work

**Superposition theory extensions** proposes generalizing computation-in-superposition frameworks from boolean to floating-point variables.

**Bounding representation sparsity** seeks theoretical arguments for feature activation sparsity without assuming SAE correctness.

**Loss landscape and superposition** explores relationships between circuit complexity and learning coefficient geometry.

## Meta-Research and Philosophy

**Comparative analysis across disciplines** proposes reviewing connections between computational neuroscience, mech interp, and philosophy of science regarding representational geometry, topology, dynamics, and explanations.

**"What is a feature?" analysis** examines fundamental definitional questions and their implications.

**Natural latents expectation** investigates whether network features align with natural latent variables.

## Engineering

**TinyStories dataset and model improvements** proposes creating a higher-quality dataset addressing existing formulaic structure and unicode issues, with accompanying model suite for full reverse-engineering attempts. Noa Nabeshima has initiated related work with cleaned datasets and small models.

---

## Comments Highlights

Neel Nanda confirmed the older problems list is outdated. Leo Gao provided empirical findings on opposing features, activation shuffling, and encoder-decoder initialization. Discussion included questions about linear transformations in MLPs, sparsity penalty priors, and feature splitting toy models.
