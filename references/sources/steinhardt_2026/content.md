# The Case for Evaluating Model Behaviors

Source: https://www.lesswrong.com/posts/J5KkwYnnaeNX7hL2s/the-case-for-evaluating-model-behaviors

Author: jsteinhardt
Date: 20th May 2026
Read time: 4 min

---

Most evaluations of AI systems focus on their capabilities: how good they are at coding tasks, how effectively they can answer complex scientific questions, and so on.

From a safety perspective, capability evaluations have a place: by understanding how close we are to different capabilities, and the rate of progress on them, we can forecast when different risks are likely to occur, as well as the broad shape of AI development. These capability evaluations were very useful to me when writing GPT-2030, and more recently I've found the METR time horizon graph useful for extrapolating the likely degree of autonomy of future agents.

However, these evaluations also have pretty significant externalities: accurate capability measurements speed up capability research, and the work needed to fully elicit model capabilities involves developing agent scaffolds and other artifacts that directly advance model capabilities. This also means that AI labs are already highly incentivized to produce such evaluations, making the counterfactual impact lower.

There is a different class of evaluations that I think is significantly more valuable and underinvested in, and that doesn't have these issues. These are **behavior evaluations**: evaluations that measure a model's tendencies (sometimes also called **propensity evals**).

Here are the sorts of questions a behavior eval might answer:

* How often does a model agree with a user in cases where the user is factually wrong?
* How frequently do models explicitly verbalize awareness that they are being evaluated, and what factors lead to this?
* How often do different models reward hack an environment (e.g. hard-coding unit tests) and in what situations does this tend to occur?
* How frequently do models report having internal desires or subjective experience?

To turn these questions into concrete numbers, we will typically define a judge of the behavior (often a language model with a rubric) as well as a distribution over environments that the model is placed in, and compute the average value of the judge across these environments. This gives us an automated procedure that lets us compare across different models as well as across time.

## Why behavior evals are high-impact

It is basically a given that model capabilities will increase over time: there are strong incentives to do so, and the rate of increase follows robust trend lines. Model behaviors, in contrast, are far more up for grabs: whether sycophancy increases or decreases is a complex function of the incentives of model trainers that push in multiple directions.

One of the best ways to incentivize changes in a model behavior is to measure it: if it is public knowledge how sycophantic each model is, and the sycophancy metric is clearly connected to adverse outcomes, no developer wants to be at the top of the sycophancy leaderboard. The disadvantages of capability evals now become advantages:

* Quantifying a behavior makes it much easier to iterate on it.
* The research needed to quantify a behavior is likely to produce useful tools that accelerate the general science of model behaviors.

## Why this impact is likely counterfactual

In contrast to capability evals, constructing behavior evals can be **at odds with** the incentives of AI developers, especially if they reveal a mismatch between the developer's goals and user's goals (e.g. engagement vs. well-being). Making this information public makes the overall market more efficient by letting users make more informed choices, which in aggregate creates a transfer of surplus from developers to users.

Beyond cases of direct conflict, many behaviors that are important to tail risks (e.g. tendencies to seek power) are only very indirectly tied to developers' bottom lines. It is likely possible to build evaluations of these behaviors that are significantly more comprehensive than AI developers would build by default.

## Model behaviors are likely core to alignment

My model of AI is that high-level outcomes arise from the cumulative effect of reinforcing a large number of low-level tendencies. A model that becomes incorrigibly power-seeking does so because there are many cases during training where seeking power is rewarded. A model becomes extremely manipulative by first learning to be manipulative in many smaller ways. Models will lean on the patterns that have worked well for them in the past, so the more that we can measure and incentivize good behavior over bad, the more models will have a good "character" and continue to behave well as they become more capable.

To make this more concrete, I basically agree with Ryan Greenblatt that current models seem pretty misaligned to me. If the patterns of behavior that Ryan identifies continue as models become more capable, I think we will be in a good deal of trouble once we hit the point where we can no longer tell if they are behaving in line with our goals -- both because of the direct effect of those patterns, and because they are likely to generalize to other types of malign behavior. If we could replace these with consistently good patterns of behavior, we would be in a much better position for AI alignment.

## Summary

I think safety researchers, especially those working outside of AI labs, should put significantly more focus on creating high-quality behavior evaluations for AI, especially for behaviors where there is misalignment between AI developers and consumers, and for behaviors related to catastrophic misalignment and other tail risks. These evaluations would better align incentives between AI developers and the public, are unlikely to be created otherwise, and could drive us towards significantly more aligned AI systems.

---

### Footnotes

1. Though still non-zero because the evaluations might not be public by default, or optimized for enabling accurate forecasts.

2. Some behaviors are clearly good or bad (e.g. sycophancy or reward hacking), others are neutral but informative (e.g. subjective experience).

3. Perez, E., et al. (2022). Discovering Language Model Behaviors with Model-Written Evaluations. arXiv:2212.09251.

   Wei, J., Huang, D., Lu, Y., Zhou, D., and Le, Q. V. (2023). Simple synthetic data reduces sycophancy in large language models. arXiv:2308.03958.

   Cheng, M., Yu, S., Lee, C., Khadpe, P., Ibrahim, L., and Jurafsky, D. (2025). Social Sycophancy: A Broader Understanding of LLM Sycophancy. arXiv:2505.13995.

4. Goldowsky-Dill, N., et al. (2025). Claude Sonnet 3.7 (often) knows when it's in alignment evaluations. Apollo Research blog.

   Goodfire (2026). Verbalized Eval Awareness Inflates Measured Safety. Goodfire research note.

5. Gabor, J., Lynch, J., and Rosenfeld, J. (2025). EvilGenie: A Reward Hacking Benchmark. arXiv:2511.21654.

6. Anthropic (2025a). Claude Opus 4 & Claude Sonnet 4 System Card.

   Anthropic (2025b). Claude Sonnet 4.5 System Card.
