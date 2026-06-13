# MIB: A Mechanistic Interpretability Benchmark

Source: https://openreview.net/forum?id=sSrOwve6vb

## Publication Details
- **Published:** 01 May 2025
- **Last Modified:** 16 Aug 2025
- **Venue:** ICML 2025 Conference (Poster)
- **License:** CC BY 4.0
- **Submission Number:** 13210

## Authors
Aaron Mueller, Atticus Geiger, Sarah Wiegreffe, Dana Arad, Ivan Arcuschin, Adam Belfki, Yik Siu Chan, Jaden Fried Fiotto-Kaufman, Tal Haklay, Michael Hanna, Jing Huang, Rohan Gupta, Yaniv Nikankin, Hadas Orgad, Nikhil Prakash, Anja Reusch, Aruna Sankaranarayanan, Shun Shao, Alessandro Stolfo, Martin Tutek, and 3 additional authors

## TL;DR
"We propose a benchmark to establish lasting standards for comparing causal localization methods."

## Abstract
The paper introduces MIB, a mechanistic interpretability benchmark with two evaluation tracks spanning four tasks and five language models. The research examines methods for identifying model components crucial to task performance and aligning discovered features to task-relevant causal variables.

Key findings indicate that attribution and mask optimization methods excel at circuit localization, while supervised DAS outperforms sparse autoencoders for causal variable identification. Notably, SAE features showed no advantage over basic neurons in this context.

## Lay Summary
The research addresses the need for standardized evaluation in mechanistic interpretability. Previous work lacked consistent comparison methods across different interpretation approaches. MIB provides this standardization, enabling researchers to assess whether methods effectively locate important model components and identify where concepts are computed within language models.

## Primary Research Area
Social Aspects: Accountability, Transparency, and Interpretability

## Keywords
interpretability, causality, localization, benchmarking, circuits

## Code Repository
https://github.com/aaronmueller/MIB
