---
layout: paper
title: "What Can AI Actually Do? A Framework for Understanding"
author: "James (JD) Longmire"
date_published: 2025-12-02
keywords:
  - AI Limitations
  - Origination
  - Derivation
  - LLM
  - Philosophy of AI
abstract: "The conversation about artificial intelligence has become strangely polarized. This article introduces the origination-derivation framework for understanding AI's genuine capabilities and structural limitations, examining six phenomena the framework helps explain."
---

The conversation about artificial intelligence has become strangely polarized. On one side, breathless predictions of artificial general intelligence arriving any moment. On the other, dismissals of AI as mere hype, destined to collapse under its own weight. Both camps are missing something fundamental.

What if the question isn't whether AI is impressive or overhyped, but whether we understand what kind of thing it actually is?

---

## The Distinction That Matters: Origination vs. Derivation

I propose a distinction between two kinds of cognitive process: origination and derivation.

**Human cognition can originate.** We can retrieve configurations of thought, insight, and understanding that are not simply derived from our prior inputs. The causal chain of human thought includes something entering from outside prior experience. We make genuine leaps.

**AI systems derive.** They transform prior inputs according to learned patterns. The causal chain runs: training data → processing → outputs, with no external entry point. This is true regardless of scale, architecture, or sophistication.

This distinction isn't a claim about intelligence, consciousness, or souls. It's a structural observation about what kind of process is occurring. Derivation can be extraordinarily powerful. But it remains bounded by the distribution of its training data in ways that origination is not.

---

## Six Phenomena the Framework Helps Explain

### 1. Hallucination

Recent theoretical research argues that hallucination in large language models cannot be fully eliminated. Xu et al. (2024) formalized conditions under which LLMs will inevitably produce outputs inconsistent with ground truth. Banerjee et al. (2024) argued that hallucinations stem from deep structural features, drawing on Gödel's Incompleteness Theorem to suggest complete elimination is not achievable.

**Framework mapping:** Systems that generate outputs based on statistical patterns in training data lack independent access to verify those outputs against reality.

### 2. Reasoning Failures

Empirical studies consistently find significant failure rates on logical reasoning tasks. Wan et al. (2024) reported 29-90% failure rates across models. Mirzadeh et al. (2024) found performance degrades sharply with minor wording changes.

**Framework mapping:** Derivative systems may learn what valid arguments look like without accessing what makes them valid.

### 3. Brittleness

AI systems perform impressively within their training distribution but often fail unpredictably when inputs deviate. Current models frequently learn surface correlations rather than underlying principles.

**Framework mapping:** A system confined to transformations within its training distribution, rather than navigating a broader space of possibilities.

### 4. The Stochastic Parrot Problem

Bender et al. (2021) argued that LLMs probabilistically link words together based on statistical patterns, without reference to meaning or grounded understanding.

**Framework mapping:** If outputs are patterned on prior linguistic data rather than anchored in understanding, the system operates derivatively.

### 5. Scaling Limits

Evidence of diminishing returns is accumulating. A majority of surveyed AI researchers are skeptical that scaling current approaches alone will achieve AGI.

**Framework mapping:** More derivation does not become origination. Quantity may not transform into a different kind of process.

### 6. Creativity Ceilings

Cropley (2025) derived an illustrative upper bound of around 0.25 on a creativity scale, roughly corresponding to amateur-professional boundary. The core insight: for effective responses, models must select high-probability tokens, but high-probability tokens are low in novelty.

**Framework mapping:** Derivative systems can recombine what they have seen, but cannot retrieve from a space of possibilities beyond their training distribution.

---

## What AI Does Well

This framework is not a case against AI. Derivation is genuinely valuable.

AI systems excel at:
- Pattern recognition at scale
- Synthesizing and summarizing existing information
- Consistency checking within defined parameters
- Executing well-specified tasks with speed and accuracy
- Augmenting human origination through drafting and iteration

The key is understanding which tasks require origination and which can be accomplished through derivation.

---

## The Research Ahead

Planned work includes:
- Scholarly analysis of whether AI limitations are categorical rather than merely computational
- Examination of ethical implications for AI deployment
- Commentary on current AI research through the framework's lens
- Exploration of human-AI collaboration models

---

## References

AAAI (2025) *AAAI 2025 Presidential Panel on the Future of AI Research*.

Banerjee, S., Singhal, A. and Choudhury, S. (2024) 'LLMs Will Always Hallucinate, and We Need to Live With This', *arXiv preprint arXiv:2409.05746*.

Bender, E.M. et al. (2021) 'On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?', *FAccT '21*.

Cropley, A. (2025) 'A New Look at the Creativity of LLMs: The Creativity Ceiling', *Creativity Research Journal*.

Mirzadeh, S.I. et al. (2024) 'GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models', *Apple Machine Learning Research*.

Wan, Z. et al. (2024) 'LogicAsker: Evaluating and Improving the Logical Reasoning Ability of Large Language Models', *arXiv preprint*.

Xu, Z., Jain, S. and Kankanhalli, M. (2024) 'Hallucination is Inevitable: An Innate Limitation of Large Language Models', *arXiv preprint arXiv:2401.11817*.
