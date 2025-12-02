# What Can AI Actually Do? A Framework for Understanding

The conversation about artificial intelligence has become strangely polarized. On one side, breathless predictions of artificial general intelligence arriving any moment. On the other, dismissals of AI as mere hype, destined to collapse under its own weight. Both camps are missing something fundamental.

What if the question isn't whether AI is impressive or overhyped, but whether we understand what kind of thing it actually is?

I've begun a research program to investigate exactly this question. The goal isn't to attack AI or defend it, but to develop a principled framework for understanding its genuine capabilities and structural limitations. What follows is an introduction to the core idea.

## The Distinction That Matters: Origination vs. Derivation

I propose a distinction between two kinds of cognitive process: origination and derivation.

Human cognition can do something remarkable: it can originate. We can retrieve configurations of thought, insight, and understanding that are not simply derived from our prior inputs. The causal chain of human thought includes something entering from outside prior experience. We make genuine leaps.

AI systems, by contrast, derive. They transform prior inputs according to learned patterns. The causal chain runs: training data → processing → outputs, with no external entry point. This is true regardless of scale, architecture, or sophistication.

This distinction isn't a claim about intelligence, consciousness, or souls. It's a structural observation about what kind of process is occurring. Derivation can be extraordinarily powerful. But it remains bounded by the distribution of its training data in ways that origination is not.

This is my philosophical proposal, not a claim made by the researchers I'll cite below. But I believe recent empirical findings on AI limitations are consistent with this framework and help motivate it. Let me sketch how.

## Six Phenomena the Framework Helps Explain

### 1. Hallucination

Recent theoretical research argues that hallucination in large language models cannot be fully eliminated. Xu, Jain and Kankanhalli (2024) formalized conditions under which LLMs, as sequence models operating over broad function classes, will inevitably produce outputs inconsistent with ground truth when used as general problem solvers. Banerjee, Singhal and Choudhury (2024) argued that hallucinations stem from deep structural features of how LLMs work, drawing on classic computational limits including Gödel's Incompleteness Theorem to suggest that complete elimination is not achievable through architectural improvements, dataset enhancements, or fact-checking mechanisms alone.

These results are conditional on modeling assumptions, not universal proofs. But they point toward something important: systems that generate outputs based on statistical patterns in training data lack independent access to verify those outputs against reality. The origination-derivation framework offers one way to understand why this might be a persistent feature rather than an engineering problem to be solved.

### 2. Reasoning Failures

Empirical studies consistently find that current AI systems fail at logical reasoning tasks at significant rates. Wan et al. (2024) reported failure rates ranging from 29% to 90% across different models when testing atomic logical skills in propositional and predicate logic. Mirzadeh et al. (2024) found that performance degrades sharply with minor wording changes that don't affect the underlying logic, and that adding a single irrelevant clause causes performance drops of up to 65% across state-of-the-art models.

These findings don't prove that LLMs can never reason in principle. But they raise serious questions about whether current systems are grasping logical principles or mimicking patterns of reasoning found in training data. The framework suggests an interpretation: derivative systems may learn what valid arguments look like without accessing what makes them valid.

### 3. Brittleness

AI systems perform impressively within their training distribution but often fail unpredictably when inputs deviate from what they've seen. This brittleness is extensively documented in the machine learning literature on distribution shift, adversarial robustness, and compositional generalization (see, e.g., Hendrycks and Dietterich, 2019; Lake and Baroni, 2018).

Current models frequently learn surface correlations rather than underlying principles. The framework interprets this as a feature of derivation: a system confined to transformations within its training distribution, rather than navigating a broader space of possibilities. This interpretation goes beyond what the empirical literature claims, but it offers a principled account of why brittleness might persist across architectures.

### 4. The Stochastic Parrot Problem

Bender et al. (2021) introduced the influential "stochastic parrots" metaphor, arguing that large language models probabilistically link words and sentences together based on statistical patterns in training text, without reference to meaning or grounded understanding. On this view, LLMs cannot inherently distinguish fact from fiction without external grounding mechanisms.

The framework aligns with this critique: if outputs are patterned on prior linguistic data rather than anchored in understanding, the system operates derivatively. Bender et al. do not use the origination-derivation vocabulary I'm proposing, but their analysis of the gap between statistical fluency and genuine comprehension motivates the distinction.

### 5. Scaling Limits

After years of assuming that scaling up models would eventually produce general intelligence, evidence of diminishing returns is accumulating. Survey work associated with the AAAI 2025 Presidential Panel on the Future of AI Research reports that a substantial majority of surveyed AI researchers are skeptical that scaling current approaches alone will achieve AGI (AAAI, 2025). OpenAI co-founder Ilya Sutskever has said in news interviews that the era of simple scaling is largely over and that new kinds of advances are needed, reflecting a sense that results from scaling have plateaued (Reuters, November 2024).

These observations don't prove scaling has hit a permanent wall. But they suggest that simply adding more data and compute may not transform current systems into something qualitatively different. The framework offers a way to think about why: more derivation does not become origination. Quantity may not transform into a different kind of process.

### 6. Creativity Ceilings

Cropley (2025) presented a theoretical model analyzing the creative capacity of LLMs based on their next-token prediction mechanism. Within his model's assumptions, he derives an illustrative upper bound of around 0.25 on a 0-to-1 creativity scale, which he interprets as roughly corresponding to the boundary between amateur and professional human creativity. The core insight is a tradeoff: for an AI response to be effective, the model must select high-probability tokens, but high-probability tokens are by definition low in novelty.

This bound is a property of his particular model, not a measured characteristic of real systems or a universal law. But it illustrates a structural tension in how current LLMs work. The framework interprets this as a limit on derivative systems: they can recombine what they have seen, but cannot retrieve from a space of possibilities beyond their training distribution.

## What AI Does Well

This framework is not a case against AI. Derivation is genuinely valuable.

AI systems excel at pattern recognition at scale, at synthesizing and summarizing existing information, at consistency checking within defined parameters, and at executing well-specified tasks with speed and accuracy. They can augment human origination by drafting, iterating, and refining what humans conceive. They can identify patterns in existing data that humans might miss.

The key is understanding which tasks require origination and which can be accomplished through derivation. AI is a powerful tool in the right domains. The framework helps clarify where those domains are and why.

## The Research Ahead

This introduction sketches the core distinction. The research program will develop it rigorously, applying the framework to documented AI phenomena, engaging the empirical literature, and addressing philosophical foundations.

Planned work includes:

- Scholarly analysis of whether AI limitations are categorical rather than merely computational
- Examination of the ethical implications for AI deployment
- Commentary on current AI research through the framework's lens
- Exploration of human-AI collaboration models that leverage both origination and derivation appropriately

I'll be publishing findings, commentary, and analysis as the work progresses.

## An Invitation

I'm sharing this publicly not as a finished product but as a research program in development. If you work in AI, philosophy of mind, cognitive science, or related fields, I welcome engagement.

If you see flaws in the reasoning, I want to know. If you know of research that supports or challenges these ideas, point me to it. If you're interested in collaboration, reach out.

The goal is understanding, not advocacy. Getting this right matters for how we develop, deploy, and govern AI systems. I'd rather be corrected than comfortable.

Follow along as the work develops, and contribute if you can.

---

## References

AAAI (2025) *AAAI 2025 Presidential Panel on the Future of AI Research*. Available at: https://aaai.org/about-aaai/presidential-panel-on-the-future-of-ai-research/ (Accessed: December 2025).

Banerjee, S., Singhal, A. and Choudhury, S. (2024) 'LLMs Will Always Hallucinate, and We Need to Live With This', *arXiv preprint arXiv:2409.05746*.

Bender, E.M., Gebru, T., McMillan-Major, A. and Shmitchell, S. (2021) 'On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?', *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)*, pp. 610-623. doi: 10.1145/3442188.3445922.

Cropley, D.H. (2025) 'The Cat Sat on the …? Why Generative AI has Limited Creativity', *Journal of Creative Behavior*. doi: 10.1002/jocb.70077.

Hendrycks, D. and Dietterich, T. (2019) 'Benchmarking Neural Network Robustness to Common Corruptions and Perturbations', *Proceedings of the International Conference on Learning Representations (ICLR)*.

Lake, B.M. and Baroni, M. (2018) 'Generalization without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks', *Proceedings of the 35th International Conference on Machine Learning (ICML)*, pp. 2873-2882.

Mirzadeh, I., Alizadeh, K., Shahrokhi, H., Tuzel, O., Bengio, S. and Farajtabar, M. (2024) 'GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models', *arXiv preprint arXiv:2410.05229*. [Published at ICLR 2025].

Wan, Y., Wang, W., Yang, Y., Yuan, Y., Huang, J., He, P., Jiao, W. and Lyu, M. (2024) 'LogicAsker: Evaluating and Improving the Logical Reasoning Ability of Large Language Models', *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pp. 2124-2155. doi: 10.18653/v1/2024.emnlp-main.128.

Xu, Z., Jain, S. and Kankanhalli, M. (2024) 'Hallucination is Inevitable: An Innate Limitation of Large Language Models', *arXiv preprint arXiv:2401.11817*.

---

**James (JD) Longmire**
ORCID: 0009-0009-1383-7698
Northrop Grumman Fellow

*The views expressed here are my own and do not represent the position of Northrop Grumman Corporation.*
