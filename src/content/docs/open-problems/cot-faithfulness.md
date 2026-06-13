---
title: "Is Chain-of-Thought Faithful?"
---

# Is Chain-of-Thought Faithful to the Model's Reasoning?

**The question.** When a language model produces a chain-of-thought explanation — "I need to find the capital of France, which is Paris" — is that explanation faithful to the internal computation that produced the answer? Or is it post-hoc rationalization that bears no reliable relationship to what actually happened inside the network?

This question has become central to AI safety: if CoT is faithful, it's a window into model reasoning; if it isn't, it's a misleading facade. We show that the disagreement turns on what "faithful" means — and different views define it differently.

## What each view says

### [Instrumental view](/mechanistic-views/views/instrumental/) — faithful means predictive

A CoT explanation is faithful if it predicts the model's behavior. If the CoT says "I'm comparing X and Y" and the model's output is consistent with comparing X and Y, that's faithfulness in the only sense that matters instrumentally.

**The limit.** This is a low bar. A post-hoc rationalization that happens to correlate with the output would count as "faithful." The Instrumental view explicitly does not ask whether the explanation corresponds to internal computation — it asks whether it's useful for prediction.

### [Perspectival view](/mechanistic-views/views/perspectival/) — single-method evidence is structurally unreliable

CoT is one method's projection of the model's computation. The Perspectival view predicts, *before looking at any data*, that single-method evidence will be unreliable. The model may have learned to produce plausible-sounding explanations that are systematically disconnected from its actual computation.

**The fix.** Cross-method convergence. If the CoT says "I relied on feature X," and probing finds X active, and activation patching shows X is causally necessary, then you have triangulated evidence for faithfulness. If the methods disagree — CoT says X but patching shows Y — then at least one method is unfaithful, and you cannot tell which from CoT alone.

[Turpin et al. (2023)](https://arxiv.org/abs/2305.04388) showed that CoT explanations are systematically influenced by biased few-shot examples while the model's answers remain correct — a case where CoT is demonstrably unfaithful. [Lanham et al. (2023)](https://arxiv.org/abs/2307.13702) found that early CoT tokens can be replaced without changing the final answer. Both are exactly what the Perspectival view predicts for single-method evidence.

### [Structural view](/mechanistic-views/views/structural/) — faithful means structurally corresponding

Faithfulness requires that the steps in the CoT correspond to identifiable computational steps in the network — not just that outputs correlate, but that there is a structural mapping between the explanation and the computation. This is the strongest notion of faithfulness: the CoT is a description of the actual [gauge-invariant](/mechanistic-views/views/structural/) computational structure.

**The challenge.** This is extremely hard to test. It requires identifying the model's computational graph for a specific input, then showing that the CoT steps map onto that graph. No published work has demonstrated structural faithfulness in this sense.

### [Role view](/mechanistic-views/views/role/) — faithful means role-preserving

A CoT step is faithful if it describes a genuine functional role in the computation. "I compared the two options" is faithful if there is a component that plays the comparison role — regardless of which specific head or MLP does it. This is weaker than structural faithfulness but stronger than instrumental: the explanation must correspond to real functional roles, not just predict the output.

## The resolution

"Is CoT faithful?" is not one question. It is four:

| View | Meaning of "faithful" | Testable? | Current evidence |
|---|---|---|---|
| [Instrumental](/mechanistic-views/views/instrumental/) | Predicts behavior | Yes | Often passes — but low bar |
| [Perspectival](/mechanistic-views/views/perspectival/) | Converges with other methods | Yes | Frequently fails (Turpin et al., Lanham et al.) |
| [Role](/mechanistic-views/views/role/) | Describes real functional roles | Partially | Untested at scale |
| [Structural](/mechanistic-views/views/structural/) | Maps onto computational graph | In principle | No evidence yet |

The safety-relevant question is usually the Perspectival or Structural one: can we trust CoT as evidence about what the model is doing internally? The Perspectival view gives the clearest answer: *not from CoT alone*. Cross-method convergence is the minimum standard.

**The practical fix:** stop treating CoT as a single evidence source and start triangulating:
1. **CoT says X** — this is an Instrumental claim (predictive)
2. **Probing confirms X** — this adds a second method (moving toward Perspectival convergence)
3. **Patching shows X is causal** — this adds causal evidence ([I1 Sufficiency](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/sufficiency/))
4. **All three agree** — now you have cross-method convergent evidence ([C5 Convergent](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/))

If you're drawing safety conclusions from CoT alone, you are at the Instrumental view making Structural claims. The framework makes this mismatch visible.

## Mechanistic validity criteria

| Criterion | Status | What it tells you |
|---|---|---|
| [C5 Convergent validity](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/construct/convergent-validity/) | Central | Do CoT explanations agree with other methods? |
| [V4 Alternative exclusion](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/interpretive/alternative-exclusion) | Critical | Can you distinguish faithful CoT from post-hoc rationalization? |
| [I4 Confound control](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/internal/confound-control/) | Critical | Is the correlation between CoT and computation genuine or confounded? |
| [M1 Reliability](https://mechanistic-validity.github.io/mechanistic-validity/framework/criteria/measurement/reliability/) | Relevant | Does the same input produce consistent CoT explanations? |

## Resolution status: **Reframed**

The framework does not answer whether CoT is faithful — that remains an empirical question. But it dissolves the *confusion* by showing that "faithful" means four different things under four different views, and that the safety-relevant notion (Structural faithfulness) requires cross-method convergence that no one has demonstrated. The framework tells you what evidence you'd need; it doesn't collect it for you.

## See also

- [Perspectival view](/mechanistic-views/views/perspectival/) — the view that predicts single-method unreliability
- [Validation Methodology](/mechanistic-views/open-problems/validation-methodology/) — the broader problem of circular evidence
- [Safety Evidence Gaps](/mechanistic-views/open-problems/safety-evidence-gaps/) — how Instrumental evidence is used for Structural claims
