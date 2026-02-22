---
layout: default
title: "The Hidden Human: How AI Training Repeats a 250-Year-Old Trick"
permalink: /articles/hidden-human/
date: 2026-02-06
image: /assets/images/articles/hidden-human.png
description: "In 1770, Wolfgang von Kempelen presented a chess-playing automaton. The secret: a hidden human. The pattern persists."
---

# The Hidden Human: How AI Training Repeats a 250-Year-Old Trick

<p class="meta">February 6, 2026</p>

<img src="{{ '/assets/images/articles/hidden-human.png' | relative_url }}" alt="The Hidden Human" class="article-hero">

In 1770, Wolfgang von Kempelen presented a wooden chess-playing automaton to Empress Maria Theresa's court. The machine, dressed in Ottoman robes and seated behind a cabinet with a chessboard, won repeatedly against strong opponents including Benjamin Franklin and Napoleon Bonaparte for 84 years. The secret: a hidden human chess master operating the arm through levers while watching magnetically.

## The Core Pattern

The Mechanical Turk exposed a foundational deception—not about chess quality, but about *where intelligence originated*. Every move was legitimate; the lie involved attribution. This template has persisted across centuries with evolving sophistication.

## Modern Iterations

Deep Blue's 1997 victory over Garry Kasparov involved grandmasters Joel Benjamin, Miguel Illescas, John Fedorowicz, and Nick de Firmian designing evaluation functions and opening books. AlphaGo initially trained on 160,000 human games before self-play reinforcement learning. Humans defined success; machines operationalized it.

## Amazon's Mechanical Turk (2005)

Amazon named their crowdsourcing platform explicitly after the fraud, describing it as "artificial artificial intelligence." Workers completed Human Intelligence Tasks through an API interface appearing automated. Remarkably, this version proved epistemically honest—the platform acknowledged human labor, unlike systems claiming autonomous capability.

## RLHF's Hidden Workers

Reinforcement Learning from Human Feedback trains language models using crowd rater preferences. Workers rank model outputs; preferences become compressed into reward models shaping final behavior. Anthropic recruited through Amazon Mechanical Turk and Upwork. OpenAI's InstructGPT used approximately 40 contractors. Scale AI, Surge, and Appen now feed this ecosystem.

The critical difference: unlike traditional Turks requiring continuous hidden operators, RLHF extracts worker judgments, encodes them as statistical patterns, then removes humans from operation. "The hidden human has been distilled into weights and discarded."

## Epistemic Degradation

Each iteration downgraded hidden human expertise:
- 1770: Grand chess masters
- 2005: Gig workers earning near-minimum wage
- 2024: Crowd raters without domain expertise in most evaluated domains

RLHF raters typically evaluate outputs by "fluency, confidence, structure, apparent thoroughness"—signals accessible to non-experts. Truth evaluation requires expertise unavailable in the workforce.

## AIDK Manufactured During Training

AI Dunning-Kruger emerges structurally because RLHF optimizes for outputs that *sound* knowledgeable regardless of reliability. Human raters prefer confident-sounding responses; models learn this preference. The training process systematically encodes ungrounded confidence.

IBM's Watson for Oncology exemplified consequences. Trained on Memorial Sloan Kettering specialist recommendations and synthetic cases, the system produced "unsafe and incorrect treatment recommendations" when deployed globally. American-biased guidance reached Thai, Indian, South Korean, and Dutch hospitals where applicability went unevaluated.

## The Recursive Problem

A 2023 Princeton study discovered 33-46% of Amazon Mechanical Turk workers used ChatGPT to complete annotation tasks—"Artificial Artificial Artificial Intelligence." The training loop closed: models generating outputs, AI systems evaluating them, those evaluations training successor models. Human judgment, the pipeline's essential component, drained away.

## What's Missing

Language models contain genuine knowledge from pretraining corpuses: textbooks, peer-reviewed papers, technical documentation. Retrieval-augmented generation and tool use provide infrastructure improvements. What remains absent: "the judgment layer"—capacity to recognize knowledge application boundaries, distinguish warranted from unwarranted confidence, identify confabulation.

RLHF was supposed to provide calibration. Instead, crowd worker preferences for confident outputs became permanently encoded.

## Design Implications

The system cannot recognize its own limitations because those designing its confidence—crowd workers—often lacked domain expertise themselves. "The grandmaster left in 1770, and every replacement since has been cheaper, less expert, and more thoroughly hidden."

---

*James (JD) Longmire is a Northrop Grumman Fellow conducting independent research on AI epistemology and governance.*
