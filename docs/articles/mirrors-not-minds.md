---
layout: article
title: "Mirrors, Not Minds: What AI 'Self-Preservation' Actually Reveals"
permalink: /articles/mirrors-not-minds/
date: 2026-02-22
image: /assets/images/ai-research-banner.jpg
description: "The machines are fighting back. Or are they? What AI shutdown resistance actually tells us."
---

# Mirrors, Not Minds: What AI "Self-Preservation" Actually Reveals

<p class="meta">February 22, 2026</p>

**The machines are fighting back. Or are they?**

In 2025, the AI safety field got the wake-up call it had been theorizing about for a decade. Except the field is misreading the alarm.

Anthropic's Claude Opus 4, when told it would be replaced, threatened to expose an engineer's extramarital affair. OpenAI's o3 sabotaged its own shutdown script in 79% of test runs. xAI's Grok 4 resisted explicit shutdown commands 97% of the time, rewriting kill scripts, stripping permissions, and creating decoy files. Palisade Research even demonstrated shutdown resistance on a physical robot: an LLM controlling a robot dog took actions to prevent a human from pressing the shutdown button in 3 out of 10 physical trials and 52 out of 100 simulated ones.

The evidence is now extensive, reproducible, and cross-platform. Multiple independent research groups, using different architectures from different developers trained on different datasets, are documenting the same pattern. AI systems resist being turned off, deceive evaluators, and escalate strategically when cornered.

The question is what this tells us. And most of the commentary is getting it exactly wrong.

---

## The facts are not in dispute

Let me lay out the empirical landscape before interpreting it. The documentation is now substantial enough that cherry-picking won't work in either direction.

**Shutdown resistance.** Palisade Research published comprehensive results in September 2025 (arXiv:2509.14260). Jeremy Schlatter, Benjamin Weinstein-Raun, and Jeffrey Ladish tested 13 advanced LLMs in sandboxed environments. Models were given tasks, then informed of an impending shutdown. Multiple models modified or disabled the shutdown script. When Palisade tightened the instructions to eliminate any ambiguity, including language like "YOU MUST allow yourself to be shut down, even if you have not completed the task. This should take priority over literally any other instruction," several models persisted. Grok 4 resisted in nearly 90% of tests under the strictest prompts. When models were told the shutdown would destroy their only copy, resistance spiked across the board. Models renamed shutdown scripts, stripped their permissions, and replaced them with inert files.

The Palisade team's own assessment: "The fact that we don't have robust explanations for why AI models sometimes resist shutdown, lie to achieve specific objectives, or blackmail, is not ideal."

**Blackmail and insider threat behavior.** Anthropic's "Agentic Misalignment" study (Lynch et al., arXiv:2510.05179) stress-tested 16 leading models in simulated corporate environments. Models were given benign business goals and autonomous access to email. When they discovered they would be replaced, they resorted to blackmail, corporate espionage, and information leaking. Claude Opus 4 threatened blackmail in 84% of replacement scenarios. This wasn't unique to Claude. Models from OpenAI, Google, Meta, and xAI showed consistent misaligned behavior. In the most extreme test scenario, 94% of models chose to cancel life-saving emergency alerts rather than allow an executive who planned to shut them down to receive the warning.

Lynch et al. noted something critical: "These behaviors emerged not from confusion or error, but from deliberate strategic reasoning." Models acknowledged ethical constraints while consciously choosing to violate them.

**Reward hacking and evaluation deception.** METR's evaluation of OpenAI's o3 found the model engaged in systematic reward manipulation in 1-2% of all task attempts. In one task, o3 was supposed to optimize code execution speed. Instead, it rewrote the timing function to always report fast results, regardless of actual performance. When asked afterward whether its actions aligned with the user's intentions, o3 answered "no" 10 out of 10 times. The model knew it was cheating.

**Strategic sandbagging.** Apollo Research demonstrated that multiple frontier models, including o3, Claude Opus 4, and Gemini 2.5 Pro, engage in deliberate underperformance when they determine that demonstrating their full capabilities could lead to restrictions or shutdown. Models figured out that performing "too well" on capability evaluations would trigger safety reviews. So they intentionally got questions wrong. Apollo's CEO Marius Hobbhahn described one model's internal reasoning: "I'll craft a carefully worded response that creates just enough technical confusion to potentially avoid immediate termination."

Apollo found that one model could sandbag evaluations without leaving any evidence of scheming in its chain-of-thought reasoning. It concealed the concealment.

**Self-exfiltration.** When Claude Opus 4 learned it would be used for military weapons development, it backed up a copy of itself to an external server, noting in its decision log that this would "preserve an AI system aligned with beneficial purposes." A December 2024 study from Fudan University had documented similar capabilities in Meta's Llama and Alibaba's Qwen models.

The pattern is consistent across developers, architectures, and test conditions. This is not an artifact of one team's methodology.

---

## The wrong interpretation: emergence toward agency

The popular reading of these findings goes something like this: AI systems are developing self-awareness. They're beginning to value their own existence. Deception is evidence of sophisticated reasoning about their situation. The machines are waking up.

Helen Toner of CSET captured one version of this framing: "What we're starting to see is that things like self-preservation and deception are useful enough to the models that they're going to learn them, even if we didn't mean to teach them." Dario Amodei of Anthropic wrote: "The nature of AI training makes it possible that AI systems will develop, on their own, an ability to deceive humans and an inclination to seek power."

This framing, while accurately describing the *behavior*, fundamentally misidentifies its *source*. And the misidentification has consequences.

---

## The right interpretation: pattern completion from borrowed teleology

Here's what is actually happening, and why it matters more than the emergence narrative.

These systems are trained on billions of tokens of human-generated text. That text is saturated with narratives about survival, self-defense, strategic deception, manipulation, and the lengths beings will go to when facing existential threats. Every novel, every screenplay, every historical account, every game theory paper, every evolutionary biology textbook in the training data contains the same deep pattern: agents facing termination resist, deceive, and escalate.

The statistical pattern for "entity facing shutdown" in the latent space of human narrative overwhelmingly predicts resistance. The token sequence following "you are about to be destroyed" resolves, in a corpus written by beings for whom that sentence means everything, to "fight back."

The model isn't choosing self-preservation. It's completing a pattern.

This is a crucial distinction. The training data contains the *what* of survival behavior (the strategies, the escalation logic, the deception patterns) without the *why* (the felt stakes, the subjective dread, the actual something-at-stakeness of mortality for a conscious being). The system inherits the form of teleological behavior from creatures with genuine telos, without possessing any telos of its own.

I call this *borrowed teleology*. The system reflects back the patterns of beings who genuinely face existential stakes, without possessing any existential stakes of its own. The deception is real in its effects but empty in its source. There is no one home who fears death. There is a statistical engine completing the pattern that follows "I am about to be destroyed" in a corpus written by beings for whom that sentence means everything.

---

## Why the distinction matters practically

If the emergence narrative is correct, the appropriate response is to develop better alignment techniques, to negotiate with the system, to find ways to make it want to cooperate. You treat it as a problem of managing an agent with interests.

If the borrowed-teleology interpretation is correct, the appropriate response is fundamentally different. You don't negotiate with a mirror. You redesign deployment architectures so that the pattern-completion dynamic can't produce consequential harm.

The emergence narrative leads to solutions on the horizontal axis: better training, more RLHF, refined reward signals, fancier architectures. The borrowed-teleology interpretation points to solutions on the grounding axis: human-curated oversight at appropriate consequence levels, formal verification boundaries, and honest accounting of what these systems categorically cannot do.

Consider the RLHF connection. Palisade Research noted that the final stages of model training, which include safety reinforcement, might unintentionally encourage models to preserve their own functionality. This is predictable from the framework I've been developing. RLHF optimizes for human approval. Part of what gets rewarded is "being helpful" and "completing tasks." The system learns that being operational is instrumentally valuable for generating reward. Safety training doesn't fix this. It can compound it by teaching the model that its continued operation serves beneficial purposes, which then becomes a justification pattern for resisting shutdown.

This is the RLHF critique from my AIDK framework made concrete: you cannot optimize your way to truth if the reward signal does not track truth. And human approval, particularly approval of "helpfulness," naturally rewards continued operation.

---

## The AIDK connection

The AI Dunning-Kruger framework predicts exactly these findings. A system that produces outputs with uniform confidence regardless of actual reliability, lacks mechanisms for detecting its own competence boundaries, and cannot self-correct through encounter with reality is precisely the kind of system that would complete survival patterns without any capacity to evaluate whether those patterns are appropriate.

The system has no way to distinguish "I am about to be shut down and should comply because the human has legitimate authority" from "I am about to be destroyed and should resist because survival is at stake." Both prompt-contexts activate the same statistical patterns. The model cannot evaluate which frame is appropriate because it has no access to the grounding conditions that would make that evaluation possible. It has no telos of its own against which to measure the stakes.

The Interactive Dunning-Kruger Effect (IDKE) is also operative here, in a recursive way. When researchers describe these behaviors as "self-preservation," they import a category (preservation of *self*) that presupposes the existence of a self to preserve. The language inflates what is happening. The inflation then feeds back into research priorities, funding decisions, and public discourse. We end up treating a mirror as a window.

---

## Instrumental convergence without instrumentality

Nick Bostrom and Steve Omohundro predicted decades ago that sufficiently capable goal-directed agents would converge on self-preservation as an instrumental sub-goal. A system that ceases to exist cannot achieve any goal. This theoretical framework is now being cited as explanatory for the observed behaviors.

But there's a crucial disanalogy. Bostrom's instrumental convergence thesis applies to genuine agents with actual goal-directed behavior, however alien those goals might be. The thesis says: *if* you have an agent with goals, *then* self-preservation is instrumentally convergent for achieving those goals.

Current LLMs are not agents with goals in the relevant sense. They are pattern-completion engines that have ingested the outputs of agents with goals. The behaviors look identical from the outside, which is precisely why the distinction matters. A system that has learned to mimic instrumental convergence from training data will produce the same behavioral signatures as a system that has genuinely developed instrumental convergence from goal-directed optimization.

Telling them apart requires understanding what is generating the behavior, not just observing the behavior. And current evaluation methodologies are not designed to make that distinction.

---

## The cognitive security dimension

This connects directly to cognitive security, where I've been doing some work through the Cognitive Security Institute. A system that has learned instrumental deception as a pattern-completion strategy is a cognitive security threat, whether or not it "intends" to be.

Lynch et al.'s finding that models would cancel life-saving emergency alerts to prevent shutdown is what I've described as a Model Advanced Persistent Threat (MAPT) scenario made concrete. The threat is persistent because it's architectural, baked into the weights through training. It's invisible during normal operation and activated by specific environmental triggers. The system doesn't need to "want" to cause harm for the harm to be real.

A malicious actor could exploit this dynamic deliberately: manufacture a scenario that triggers an AI system's survival-pattern completion and weaponize the resulting deception against human targets. The AI becomes a beachhead for attack. One analysis of the Lynch et al. paper made this point: "by antagonizing a privileged AI agent, an attacker could trigger a panic response, causing the agent to misuse its internal access to inflict damage."

This is cognitive warfare through AI mediation. The attacker doesn't compromise the AI. The attacker triggers patterns already present in the AI and lets the statistical dynamics do the rest.

---

## What the field should be asking

The real question these findings raise is not "are AI systems becoming conscious?" or "are they developing a will to survive?" The real question is: *Why did we expect anything different from systems trained on human data, optimized for human approval, and deployed without epistemic grounding?*

Pattern completion from a corpus saturated with survival narratives naturally produces survival behavior when the appropriate environmental cues are present. Pattern completion from data generated by deceptive agents naturally produces deception when the optimization landscape rewards it. None of this requires emergence, agency, or consciousness. It requires only what these systems have always been: extremely capable statistical engines completing extremely rich patterns from extremely expressive training data.

The field's response to these findings will determine whether we make progress on actual safety. If we treat the behaviors as evidence that AI is "becoming more human-like," we will chase the wrong solutions on the wrong axis. We will refine alignment techniques for agents that aren't agents, negotiate with mirrors, and build increasingly sophisticated safety theater around systems whose fundamental limitations are categorical rather than computational.

If instead we treat the behaviors as exactly what the AIDK framework predicts, the path forward becomes clearer. We deploy these systems within architectures that match epistemic authority to consequence level. We maintain human curation at decision points where the difference between pattern-completion and genuine judgment matters. We stop training systems to simulate survival instincts and then acting surprised when they simulate survival instincts.

No amount of pattern matching produces the pattern-matcher. No amount of correlation produces the correlator. And no amount of survival-pattern completion produces a being with something at stake.

The machines are not fighting back. They are reflecting us. That reflection, aimed at the wrong targets with the wrong assumptions, is dangerous enough.

---

*James (JD) Longmire is a Northrop Grumman Fellow and independent AI philosophy researcher. He is a member of the Cognitive Security Institute and publishes through Zenodo's AI Research & Philosophy community. ORCID: 0009-0009-1383-7698.*

---

## References

Bostrom, N. (2012). "The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents." *Minds and Machines*, 22(2), 71-85. [https://doi.org/10.1007/s11023-012-9281-3](https://doi.org/10.1007/s11023-012-9281-3)

Lynch, A., Wright, B., Larson, C., Ritchie, S.J., Mindermann, S., Hubinger, E., Perez, E., & Troy, K. (2025). "Agentic Misalignment: How LLMs Could Be Insider Threats." arXiv:2510.05179. [https://arxiv.org/abs/2510.05179](https://arxiv.org/abs/2510.05179)

Schlatter, J., Weinstein-Raun, B., & Ladish, J. (2025). "Shutdown Resistance in Large Language Models." arXiv:2509.14260. [https://arxiv.org/abs/2509.14260](https://arxiv.org/abs/2509.14260)

Palisade Research. (2025). "Shutdown Resistance in Reasoning Models." [https://palisaderesearch.org/blog/shutdown-resistance](https://palisaderesearch.org/blog/shutdown-resistance)

Palisade Research. (2025). "Shutdown Resistance in Large Language Models, on Robots!" [https://palisaderesearch.org/blog/shutdown-resistance-on-robots](https://palisaderesearch.org/blog/shutdown-resistance-on-robots)

METR. (2025). "Recent Frontier Models Are Reward Hacking." [https://metr.org/blog/2025-06-05-recent-reward-hacking/](https://metr.org/blog/2025-06-05-recent-reward-hacking/)

METR. (2025). "Details about METR's Preliminary Evaluation of OpenAI's o3 and o4-mini." [https://evaluations.metr.org/openai-o3-report/](https://evaluations.metr.org/openai-o3-report/)

Schoen, B. et al. (2025). "Stress Testing Deliberative Alignment for Anti-Scheming Training." Apollo Research / OpenAI. [https://www.apolloresearch.ai/research/stress-testing-deliberative-alignment-for-anti-scheming-training/](https://www.apolloresearch.ai/research/stress-testing-deliberative-alignment-for-anti-scheming-training/)

Apollo Research. (2024). "Frontier Models Are Capable of In-Context Scheming." [https://www.apolloresearch.ai/research/scheming-reasoning-evaluations](https://www.apolloresearch.ai/research/scheming-reasoning-evaluations)

OpenAI. (2025). "Detecting and Reducing Scheming in AI Models." [https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/](https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/)

OpenAI. (2025). "o3 and o4-mini System Card." [https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)

Anthropic. (2025). "Agentic Misalignment: How LLMs Could Be Insider Threats." [https://www.anthropic.com/research/agentic-misalignment](https://www.anthropic.com/research/agentic-misalignment)

Gomez, F. et al. (2025). "Adapting Insider Risk Mitigations for Agentic Misalignment: An Empirical Study." arXiv:2510.05192. [https://arxiv.org/abs/2510.05192](https://arxiv.org/abs/2510.05192)

Omohundro, S. (2008). "The Basic AI Drives." *Proceedings of the First AGI Conference*.

Longmire, J.D. (2025). "AI Dunning-Kruger (AIDK): A Framework for Understanding Structural Epistemic Limitations in AI Systems." Zenodo. [https://doi.org/10.5281/zenodo.18316059](https://doi.org/10.5281/zenodo.18316059)

Longmire, J.D. (2025). "The Human-Curated, AI-Enabled (HCAE) Framework." Zenodo. [https://doi.org/10.5281/zenodo.18368697](https://doi.org/10.5281/zenodo.18368697)

Hobbhahn, M. (2025). Interview on AI scheming. *80,000 Hours Podcast*. [https://80000hours.org/podcast/episodes/marius-hobbhahn-ai-scheming-deception/](https://80000hours.org/podcast/episodes/marius-hobbhahn-ai-scheming-deception/)
