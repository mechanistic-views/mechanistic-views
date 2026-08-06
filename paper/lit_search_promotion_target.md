# Literature search — fix the IOI audit + pick a promotion target

## Q1. What structural / process work already exists on IOI? (fixes a factual error)

> For the IOI (indirect object identification) circuit in GPT-2 Small, 2022–2026: which papers analyze it in **weight space** rather than via activation patching or ablation? Include OV/QK circuit decomposition, composition scores, gauge-invariant or reparameterization-invariant characterizations, and any weight-based account of the name-mover / S-inhibition heads. Separately: is there any **training-dynamics or checkpoint** work on when the IOI circuit forms? Give primary citations and say clearly what each analyzed.

*Why:* the cross-view audit currently scores IOI at δ≈1–1.5 and recommends "a structural-view analysis" as the path to higher δ. If that work exists, IOI's δ is understated and the recommendation is stale. Need this to correct the audit regardless of which promotion target we pick.

## Q2. SAE features beyond the object view (leading promotion target)

> For sparse-autoencoder features in transformer language models, 2023–2026: what evidence exists **beyond activation-based analysis**? Specifically — (a) **weight-space / structural** characterization of feature directions: do SAE decoder directions correspond to identifiable weight-space structure, composition scores, or gauge-invariant quantities? (b) **training-dynamics / checkpoint** studies: when during training do SAE features form, and do the same features appear across checkpoints? (c) evidence that a feature's identity survives systematic variation of the **contrastive baseline**. Include negative results.

## Q3. Candidate single-view claims (other promotion targets)

> Which prominent mechanistic-interpretability claims about transformer LMs (2023–2026) are supported **only** by activation-based evidence — patching, ablation, probing, DAS — with **no** weight-space/structural analysis and **no** training-dynamics analysis? List candidates suitable for a cross-view corroboration attempt, with what evidence each currently has.

## Q4. J-space feasibility (only if considering it as the experiment)

> What **open-weight replications** of Anthropic's J-space / Jacobian-lens "global workspace" result exist? Which models, what compute was required, is code public? Has anyone done weight-space or training-dynamics analysis of the J-space subspace, as opposed to the original interventional (swap/ablate/inject) evidence?
