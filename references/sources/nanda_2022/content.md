# 200 Concrete Open Problems in Mechanistic Interpretability

Author: Neel Nanda
Source: https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability
Sequence: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj

Note (July 2024 edit by author): This sequence is somewhat dated. Sparse Autoencoders represent emerging important directions not covered in the original text.

---

# Introduction

This introductory post launches a sequence exploring mechanistic interpretability (MI) -- the practice of reverse-engineering neural networks to understand how they function. "Taking an inscrutable stack of matrices where we know that it works, and trying to reverse engineer how it works."

## Key Motivations

1. **Alignment relevance**: Understanding whether models accomplish tasks through genuine helpfulness or deception
2. **Scientific inquiry**: Discovering fundamental principles underlying neural network behavior

## Difficulty Ratings

- **A**: Beginner problems solvable in days to two weeks
- **B**: Substantial projects requiring several weeks minimum
- **C**: Harder problems suitable for multi-week projects
- **D**: Ambitious, loosely-defined directions requiring significant scoping

## Posts in the Sequence

1. The Case for Analysing Toy Language Models
2. Looking for Circuits in the Wild
3. Interpreting Algorithmic Problems
4. Exploring Polysemanticity and Superposition
5. Analysing Training Dynamics
6. Techniques, Tooling and Automation
7. Image Model Interpretability
8. Interpreting Reinforcement Learning
9. Studying Learned Features in Language Models

---

# Post 1: The Case for Analysing Toy Language Models

Source: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/GWCgZrzWCZCuzGktv

## Overview

This post argues for studying small transformer models as a pathway to understanding mechanistic interpretability. Nanda notes that "it's way easier to get traction" with toy models, having released 12 open-sourced variants ranging from 1-4 layers.

## Two Pathways for Value

1. **Finding universal circuits**: Discovering fundamental patterns that reappear across model scales. Induction heads exemplify this -- they appear consistently across all examined models and are "universal in all models we've looked at."

2. **Developing reverse-engineering methodology**: Understanding which techniques, conceptual frameworks, and tools effectively decompose model behavior.

## Research Strategy

Find "a problem or type of text that a toy model can predict competently and then to reverse engineer how it does it." Recommendations:

- Exploring concrete, minimal examples
- Creating counterfactuals with correct/incorrect answers
- Using logit differences rather than raw outputs
- Applying activation patching and direct logit attribution

## Open Problems

- **Problems 1.1-1.8**: Neuron reverse-engineering across layer depths
- **Problems 1.9-1.12**: Analyzing composition in multi-layer attention-only models
- **Problems 1.13-1.22**: Comparing architectural variations and bug-fixing mechanisms
- **Problem 1.23**: Open-ended exploration of interesting patterns

Each problem includes difficulty ratings (A-C scale) and specific methodological guidance.

---

# Post 2: Looking for Circuits in the Wild

Source: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/XNjRwEX9kxbpzWFWd

## Overview

This post discusses the importance of reverse-engineering circuits in real language models. "Our ultimate goal is to be able to reverse engineer real, frontier language models," and studying actual model circuits represents a crucial intermediate step.

## Key Motivation

The paper "Interpretability In The Wild" serves as the primary inspiration. Redwood Research analyzed how GPT-2 Small solves Indirect Object Identification (IOI) -- determining that in "John and Mary went to the store, then John handed a bottle of milk to," the answer is Mary. The model accomplishes this using 26 attention heads organized into 7 distinct groups.

Key insights:
- **Built-in redundancy**: "if the name mover heads are knocked-out, then there are backup heads which take over and do the task instead"
- **Repurposed functionality**: Components designed for complex tasks get reused for simpler ones
- **Universality questions**: Do different models learn identical circuits for the same task?

## Research Workflow

1. Identify a specific behavior to understand
2. Develop deep black-box understanding through varied inputs
3. Form and test scientific hypotheses about model implementation
4. Self-critique and identify potential flaws in reasoning
5. Scale up with rigorous techniques like path patching and causal scrubbing

## Open Problems: Natural Language Circuits

**B* 2.1** - Reverse-engineer induction heads using pointer arithmetic in GPT-2 Small, focusing on weight-level understanding

**B* 2.2** - Interpret circuits for continuing common sequences (numbers, days of the week, Roman numerals)

**B* 2.3** - Analyze numbered list continuations like "1. Text\n2. Text\n -> 3."

**B* 2.4** - Study three-letter acronym generation (ACG, RFU)

**B* 2.5** - Interpret name-to-email conversion (Katy Johnson -> katy_johnson)

**C* 2.6** - Investigate factual recall using causal tracing methods

**B* 2.7** - Find capitalization circuits for words following periods

**B-C* 2.8** - Analyze object-counting mechanisms in text

**C* 2.9** - Study memorization phenomena like recalled contact information

**B 2.10** - Reverse-engineer induction heads in non-toy models like GPT-2 Small

**B 2.11** - Interpret pronoun selection (he/she/it/they) using rhetorical questions

**A-C 2.12** - Identify and interpret novel model behaviors

## Code-Focused Circuits

**B* 2.13** - Study bracket-closing mechanisms

**B* 2.14** - Interpret HTML tag closure

**C* 2.15** - Analyze method selection based on object type

**A-C* 2.16** - Discover and reverse-engineer algorithmic code patterns

## IOI Circuit Extensions

**A* 2.17** - Test IOI circuit universality across Stanford mistral models trained with different seeds

**A* 2.18** - Investigate backup behavior in early circuit heads through ablation

**B* 2.19** - Develop general patterns for understanding backup mechanisms

**A* 2.20** - Reverse-engineer duplicate token head weights deeply

**B* 2.21** - Understand IOI in GPT-Neo using MLP composition

**C* 2.22** - Determine negative/backup name mover head roles outside IOI contexts

**C* 2.23** - Analyze conditions enabling compensation when heads are ablated

**B* 2.24** - Study GPT-Neo (trained without dropout) for backup head behavior

**B 2.25** - Reverse-engineer parameter-level behavior of sharp previous token heads

**C 2.25** - Investigate beyond-first-layer MLP roles in IOI tasks

**C 2.26** - Understand adversarial example dynamics and S-Inhibition head patterns

## Confusing Model Phenomena

**B-C* 2.27** - Explain why models contain numerous induction heads and how they specialize

**B* 2.28** - Investigate why ablating MLP0 severely damages GPT-2 Small performance

**B-C* 2.29** - Gather evidence for residual stream shared bandwidth hypothesis

**B* 2.30** - Search for memory management neurons with negative cosine similarity

**B* 2.31** - Track memory usage throughout induction circuits

## Larger Model Studies

**B-C* 2.32** - Interpret translation heads in GPT-J using activation patching

**C* 2.33** - Reverse-engineer sophisticated induction heads like pattern-matching variants

**C-D* 2.34** - Understand few-shot learning mechanisms

**C* 2.35** - Analyze two-digit addition implementation in larger models

**C* 2.36** - Investigate emergent residual stream features and their interpretability

---

# Post 3: Interpreting Algorithmic Problems

Source: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/ejtFsvyhRkMofKAFy

## Overview

Introduces mechanistic interpretability through algorithmic tasks -- simplified, synthetic problems where models learn interpretable computations. The approach emphasizes reverse-engineering small models trained on single tasks with known ground truth solutions.

## Core Strategy

1. **Simplify** to minimal settings exhibiting the phenomenon
2. **Reverse-engineer** models in detail
3. **Extrapolate** insights to broader applications
4. **Verify** findings across different examples

## Key Motivation: Grokking

Models initially memorize algorithmic task data, then suddenly generalize after extended training. Nanda's work on modular addition revealed the model employs "a funky trig-based algorithm" converting numbers to frequencies via Discrete Fourier Transform.

## Beginner Problems (A-Level)

- **A 3.1-3.2**: Sorting fixed and variable-length lists
- **A 3.3-3.4**: Interpreting MLPs/transformers for modular arithmetic
- **A 3.5-3.7**: Min/max operations, permutations, Fibonacci sequences
- **A* 3.21**: Training one-layer attention-only transformers for token prediction

## Intermediate Problems (B-Level)

- **B* 3.8**: Five-digit addition/subtraction
- **B* 3.9**: Predicting simple code function outputs
- **B* 3.10-3.12**: Graph theory, multi-task learning, automata
- **B* 3.13-3.14**: In-context linear regression
- **B 3.16-3.17**: Induction head detection, custom algorithmic problems
- **B* 3.22-3.23**: Indirect Object Identification circuits, modular addition variants
- **B-C* 3.25**: Dimensionality reduction techniques comparison

## Advanced Problems (C-Level)

- **C 3.15**: Binary/five-digit multiplication
- **C* 3.20**: Reverse-engineering Othello-GPT
- **C* 3.24**: Memorization mechanisms
- **C* 3.27**: Testing direct logit attribution reliability
- **C* 3.30-3.33**: Othello-GPT modular circuits, neuron interpretability, transformer circuit exploration

## Advanced Exploration (D-Level)

- **D* 3.28-3.29**: Lottery Ticket Hypothesis and Deep Double Descent

---

# Post 4: Exploring Polysemanticity and Superposition

Source: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/o6ptPu7arZrqRCxyz

## Key Concepts

**Features and Representations**: Neural networks internally compute features -- specific input properties like grammatical roles or semantic categories -- represented as directions in activation space.

**Superposition**: Networks compress more features than their dimensional capacity permits, essentially "simulating a larger model." This occurs in two forms:
- Linear bottleneck superposition (compression in residual streams)
- Neuron superposition (computation in MLP layers)

**Polysemanticity**: Individual neurons represent multiple unrelated features simultaneously.

## Three Research Directions

1. **Conceptual frameworks** clarifying superposition mechanisms through toy models
2. **Empirical evidence** from real models testing toy model predictions
3. **Practical methods** for identifying and handling superposed features

## Toy Model Variants (4.1-4.20)

Proposed modifications include:
- Dropout effects on privileged bases (4.1)
- Non-uniform sparsity exploration (4.4)
- Binary inputs and logical operations (4.5)
- Different activation functions like GELU (4.10-4.11)
- Classification with cross-entropy loss (4.12)
- Multi-layer ReLU computation (4.14)
- Attention head polysemanticity (4.15)
- Simultaneous interference handling (4.16)
- Non-linear and non-decomposable representations (4.17-4.19)

## Real Language Models (4.21-4.45)

Studies examining bottleneck and neuron superposition include:
- Token identity storage in induction heads (4.21-4.22)
- Indirect Object Identification circuits (4.23)
- Positional embedding dimensions (4.24)
- Geometric superposition configurations (4.25-4.27)
- Simultaneous interference examples (4.28)
- Polysemantic neuron disambiguation (4.29-4.32)
- Adversarial examples via superposition (4.33)
- Asymmetric superposition motifs (4.34)

## Probing and Feature Detection (4.35-4.36)

Training linear probes to identify specific linguistic features within model activations.

## SoLU vs. GELU Comparison (4.37-4.41)

Analyzing whether SoLU activations reduce polysemanticity compared to GELU alternatives.

## Eliminating Superposition (4.42-4.44)

Investigating whether wider MLP layers or fine-tuning approaches can eliminate superposed features.

---

# Post 5: Analysing Training Dynamics

Source: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/hHaXzJQi6SKkeXzbg

## Key Background

1. **Induction Heads Paper**: Discovered circuits in small language models that enable in-context learning through sudden phase transitions, with visible impacts on loss curves.

2. **Grokking Research**: Analyzed models that initially memorize training data then suddenly generalize after extended training, decomposing dynamics into three phases: memorization, circuit formation, and cleanup.

## Research Tips

- Study small algorithmic models first; they train quickly
- Take frequent checkpoints using exponential decay schedules
- Understand final models before analyzing training
- Use multiple random seeds for validation
- Be cautious about metric interpretation -- accuracy appears sharper than loss

## Open Problems (37 total)

### Algorithmic Tasks (Understanding Grokking)
- Explaining phase changes in digit addition
- Interpreting PCA components of model states
- Predicting grokking timing without future information
- Understanding frequency selection in solutions
- Testing progress measures' effects on training

### Lottery Tickets & Initialization
- Testing lottery ticket hypotheses with induction heads
- Examining why certain heads consistently form
- Analyzing effects of knocking out circuit parameters early

### Head Composition Analysis
- Finding progress measures for head pair development
- Predicting which heads compose first
- Studying composition as phase transitions

### Fine-Tuning Dynamics
- Building toy models of task switching
- Analyzing capability preservation across domains
- Examining circuit rewiring vs. new circuit creation
- Tracking neuron overwriting during adaptation

### Language Model Training Dynamics
- Replicating induction head phase transitions across models
- Detecting neuron formation as phase transitions
- Using per-token loss analysis for discovering new phase changes
- Studying attention pattern development over training
- Investigating path dependence versus convergence across model seeds
- Testing Git Re-Basin techniques on algorithmic tasks
- Exploring scaling law mechanisms through accumulated phase changes

---

# Post 6: Techniques, Tooling and Automation

Source: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/btasQF7wiCYPsr5qw

## Motivation

The core challenge involves developing true beliefs about neural network internals while navigating an extremely large search space. The field requires "good techniques and tooling" to make progress. "Mech interp can be very labour intensive" and demands creativity, yet we ultimately need to understand models with hundreds of billions to trillions of parameters.

## Progress Indicators

- **Refining understanding**: Identifying contexts where techniques succeed or mislead
- **Finding circuits**: Developing mindsets and practical intuitions for circuit discovery
- **Building a better toolkit**: Creating new general techniques leveraging full control over model internals
- **Gold standards of evidence**: Establishing what constitutes genuine circuit understanding
- **Good infrastructure**: Developing software enabling rapid research iteration
- **Automation**: Accelerating or fully automating researcher tasks

## Technique Dimensions

### 1. General vs. Specific
General techniques apply broadly across circuits (e.g., direct logit attribution). Specific techniques target particular circuit families (e.g., prefix matching for induction heads).

### 2. Exploratory vs. Confirmatory
Exploratory techniques generate information about confusing behavior. Confirmatory techniques test hypothesized circuits rigorously.

### 3. Rigorous vs. Suggestive
Rigorous approaches (like activation patching) provide strong, reliable evidence. Suggestive methods (like max-activating examples) offer limited but useful insights.

### 4. Scalable vs. Labour Intensive
Techniques range from fully automated to painstaking manual analysis.

## Critical Caution

Warning against "premature optimization." Many researchers dismiss labor-intensive approaches favoring obviously scalable ones, but skipping deep understanding risks producing unreliable techniques. "We only have like 3 examples of well understood circuits in real language models!"

## Problems

### Technique Refinement (6.1-6.10)

**A-C* 6.1** - Break current techniques by finding edge cases

**B* 6.2** - Direct logit attribution: investigate GPT-Neo Small's poor logit lens performance

**C* 6.3** - Fix direct logit attribution via gradient-based linear approximation

**B* 6.4** - Linearizing LayerNorm: examine bimodal scale factor distributions

**B-C* 6.5** - Activation patching: understand failures with multi-variable dependence

**C* 6.6** - Causal scrubbing technique evaluation

**A-B 6.7** - Ablations: examine backup name movers in IOI circuit

**B* 6.8** - Find contexts where one ablation method succeeds while others fail

**B 6.9** - Composition scores: investigate their poor IOI circuit performance

**B 6.10** - Eigenvalue copying score evaluation

### Head Composition (6.11-6.17)

**C* 6.11** - Automate composition detection across heads

**B* 6.12** - Analyze composition on specific inputs by decomposing residual streams

**C* 6.13** - Apply direct path patching to composition analysis

**B* 6.14** - Compare causal tracing versus activation patching

**A* 6.15** - Evaluate single-layer vs. multi-layer activation patching

**A* 6.16** - Attempt patching specific neurons for circuit identification

**B* 6.17** - Patch neuron subsets based on activation magnitude

### Automated Head Detection (6.18-6.27)

**A 6.18** - Automate previous token head detection

**A 6.19** - Automate duplicate token head detection

**A 6.20** - Automate induction head identification

**A* 6.21** - Extend to translation head detection

**B* 6.22** - Detect few-shot learning heads automatically

**B* 6.23** - Distinguish pointer arithmetic induction heads from classical variants

**B* 6.24** - Detect IOI circuit heads

**B* 6.25** - Identify factual recall heads

**B-C* 6.26** - Create head detector "wiki" combining metrics into pandas DataFrames

**C* 6.27** - Develop neuron interpretability analogs

### Attention Head Analysis (6.28-6.38)

**B-C* 6.28** - Find max-activating dataset examples for attention heads

**B-C* 6.29** - Refine max-activating examples through minimal or diverse selection

**B* 6.30** - Corrupt token embeddings examining importance

**B* 6.31** - Compare corrupted direction effects to random directions

**B* 6.32** - Validate examples against direct neuron logit effects

**B-C* 6.33** - Use RoBERTa or GPT-3 finding similar text

**B-C* 6.34** - Analyze neuron activations across quantiles

**B-C* 6.35** - Integrate refined techniques into Neuroscope infrastructure

**A 6.36** - Test minimal example activation through text truncation

**A 6.37** - Replicate interpretability illusion findings

**B 6.38** - Compare SoLU max-activating results across activations

### LLM-Based Interpretation (6.39-6.41)

**B* 6.39** - Assess GPT-3's ability to identify neuron activation trends

**B* 6.40** - Generate counterfactual prompts via GPT-3

**D 6.41** - Explore additional LLM applications for interpretability

### Broader Technique Application (6.42-6.45)

**B-C* 6.42** - Evaluate feature attribution (particularly integrated gradients)

**B-C* 6.43** - Test Toy Models of Superposition predictions via probing

**C* 6.44** - Apply Rauker et al's technique survey to mechanistic interpretability

**D 6.45** - Adapt Wiles et al's bug analysis automation

### Circuit Characterization & Discovery (6.46-6.59)

**C* 6.46** - Quantitatively characterize well-understood circuits

**C* 6.47** - Build on Arthur Conmy's recursive path patching

**A-C 6.48** - Resolve TransformerLens GitHub issues

**B-C* 6.49** - Create black-box model diff tooling

**B* 6.50** - Identify largest per-token probability differences between models

**B 6.51** - Compare model performance via benchmarks

**B* 6.52** - Develop algorithmic task benchmarks

**B-C* 6.54** - Build same-structure model diff tooling

**B 6.55** - Analyze weight differences across models

**B 6.56** - Compare activations across models

**B* 6.57** - Compare direct logit attribution across model layers

**B* 6.58** - Apply activation patching to performance-differential prompts

**B-C* 6.59** - Develop QK matrix alternatives for rotary attention

---

# Post 7: Image Model Interpretability

Source: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/caMoe6yNfXcaCG2u3

## Key Achievements in Image Interpretability

**Feature Visualization**: Visualize what activates neurons by performing gradient descent on images to find maximally activating patterns.

**Curve Circuits**: Researchers reverse-engineered a ~50,000 parameter circuit for curve detection and successfully hand-coded replacement weights.

**Multimodal Neurons**: Analysis of CLIP revealed abstract neurons responding to concepts -- e.g., neurons activating on both Donald Trump photos and MAGA hats.

## Open Problems

### Different Architectures
- **7.1 (B-C*)**: ResNets with residual streams
- **7.2 (B-C*)**: Vision Transformers
- **7.3 (C)**: ConvNeXt modern architecture

### Circuits Thread Extensions
- **7.4 (B-C*)**: Hand-coding enhanced curve detectors with color
- **7.5 (C*)**: Hand-coding additional circuits from early vision neurons
- **7.6 (D*)**: Applying causal scrubbing to curve circuit claims
- **7.7 (B*)**: Finding equivariance patterns across neuron families
- **7.8 (C*)**: Understanding polysemantic neurons
- **7.9 (A-B)**: Discovering diverse circuits through weight exploration

### Multimodal Models (CLIP-based)
- **7.10 (B*)**: Analyzing weight sparsity between adjacent layers
- **7.11 (B-C*)**: Rigorous circuit reverse-engineering
- **7.12 (B-C*)**: Applying transformer circuits techniques to image attention
- **7.13 (B)**: Refining max-activating text generation

### Training Dynamics & New Architectures
- **7.14 (C)**: Investigating phase transitions in curve detector formation
- **7.15 (B*)**: Testing activation patching on Inception
- **7.16-7.18 (B-C*)**: Diffusion model interpretability

---

# Post 8: Interpreting Reinforcement Learning

Source: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/eqvvDM25MXLGqumnf

## Motivation

Key questions:
- How much do RL agents model their environment versus rely on learned heuristics?
- Do models explicitly reason about future actions?
- What are the training dynamics like when systems discover new solutions?
- How well do MI frameworks transfer to RL?

Note: "I expect a B problem here to be harder than a B elsewhere."

## Open Problems

### AlphaZero and Chess (8.1-8.4)

**B-C* 8.1**: Replicate McGrath's work using LeelaChessZero with NMF activation analysis

**C-D* 8.2**: Apply to open-source AlphaZero Go agents

**C-D* 8.3**: Train small AlphaZero on Tic-Tac-Toe

**D* 8.4**: Extend LeelaZero work by finding how features are computed

### Goal Misgeneralization (8.5-8.7)

**B-C* 8.5**: Interpret goal misgeneralization examples from Langosco et al and Shah et al

**B* 8.6**: Start with Tree Gridworld and Monster Gridworld (tiny networks)

**C* 8.7**: Apply techniques to CoinRun agents showing goal misgeneralization

### Decision Transformers (8.8)

**B-C* 8.8**: Apply transformer circuits techniques to decision transformers

### In-Context RL (8.9)

**B-C* 8.9**: Train and interpret models from the In-Context Reinforcement Learning paper

### RLHF Systems (8.10-8.13)

**D* 8.10**: Interpret CarperAI's RLHF model

**C 8.11**: Find circuits corresponding to longer-term planning

**C* 8.12**: Interpret the reward model

**D* 8.13**: Train toy RLHF models on simple tasks

### Policy Gradient and Q-Learning (8.14-8.18)

**C 8.14**: Train and interpret small models from Guez et al

**B 8.15**: Gridworld task

**B-C* 8.16**: OpenAI Gym task

**C* 8.17**: Atari game (e.g., Pong)

**B-D 8.18**: Repeat with Q-Learning

### Advanced Projects (8.19-8.21)

**B-D* 8.19**: Clone a trained agent's output logits and reverse-engineer the clone

**B-D* 8.20**: Extend understanding to study agents during training

**A-D* 8.21**: Choose your own adventure -- pick an RL paper and attempt reverse-engineering

---

# Post 9: Studying Learned Features in Language Models

Source: https://www.alignmentforum.org/s/yivyHaCAmMJ3CqSyj/p/Qup9gorqpd9qKAEav

## Core Premise

Models learn to represent features -- properties of inputs -- with different directions corresponding to different features. Early layers learn simple features that progressively build into sophisticated representations.

## Key Challenge

**Polysemanticity and superposition**: Neurons may represent multiple features simultaneously, making reverse engineering difficult. Even identifying which features exist remains largely unknown territory.

## Primary Methodology

Examining **max activating dataset examples**: tracking texts that most strongly activate individual neurons to identify consistent patterns suggesting feature detection.

## Key Neuron Categories Identified

- **Sensory neurons**: Convert raw tokens into useful formats
- **Motor neurons**: Convert conceptual understanding into token outputs
- **Context neurons**: Activate on text sharing common features
- **De-tokenization neurons**: Merge token pairs
- **Re-tokenization neurons**: Fire mid-word for multi-token outputs

## Research Problems (60+ directions)

### Exploration Tasks
- Browsing Neuroscope to identify patterns
- Testing hypotheses about neuron functions
- Examining logit attribution alignment

### Feature Detection Targets

Searchable features include:
- Basic syntax (sentence endings, proper nouns, numbers, dates)
- Linguistic elements (subjects, objects, verbs, pronouns, tense)
- Proper nouns (names, locations, landmarks)
- Code-specific features (Python variables, indentation, brackets)
- Domain-specific patterns (Base64, hexadecimal, HTML, LaTeX)
- Multi-lingual disambiguation

### Advanced Investigations
- Training linear probes for feature detection
- Analyzing neuron activation distributions
- Identifying monosemantic vs. polysemantic neurons
- Studying memory management and signal-boosting neurons
- Examining neuron families and equivariance

## Critical Caveats

Consistent dataset patterns don't guarantee neurons are monosemantic -- they simply indicate strong feature response. Users must validate hypotheses through systematic testing, including:
- Adding/removing tokens strategically
- Replacing words with synonyms
- Testing edge cases
- Comparing against random baselines
