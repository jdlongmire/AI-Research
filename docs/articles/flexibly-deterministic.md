---
layout: article
title: "Flexibly Deterministic, Structured Probabilistic: The Two Categories of AI"
permalink: /articles/flexibly-deterministic/
date: 2026-02-13
image: /assets/images/articles/flexibly-deterministic.png
description: "The split everyone uses isn't the split that matters."
---

# Flexibly Deterministic, Structured Probabilistic: The Two Categories of AI

<p class="meta">February 13, 2026</p>

<img src="{{ '/assets/images/articles/flexibly-deterministic.png' | relative_url }}" alt="Flexibly Deterministic" class="article-hero">

I propose a fundamental reorganization of how we categorize AI systems. Rather than the conventional distinctions (traditional vs. generative, narrow vs. broad), the meaningful dividing line concerns how probability functions within each system.

## Core Distinction

Traditional machine learning employs probability as an instrument serving bounded questions with measurable outcomes. A spam classifier outputs "94% chance this is junk"—a determined result expressed probabilistically. Running the same input repeatedly yields identical outputs, enabling calibration verification.

Generative AI inverts this relationship. Systems like large language models use probability as their generation mechanism itself. Multiple valid outputs exist for any prompt; "confidence" becomes meaningless since no ground truth exists. **"The structure is impressive. The probabilism renders it epistemically unaccountable."**

## Flexibly Deterministic Systems

These traditional ML approaches handle uncertainty through probabilistic reasoning while maintaining fixed input-output relationships. Credit scoring, diagnostic models, and fraud detection exemplify this category. Their limitations remain quantifiable and auditable.

## Structured Probabilistic Systems

Generative systems generate from learned probability distributions. Even at temperature zero (greedy decoding), outputs remain stochastically produced rather than determined. RLHF and retrieval-augmented generation reshape probability landscapes without introducing genuine determination.

## Hybrid Architectures

Real deployments combine both categories. Deterministic components should govern probabilistic ones—test harnesses validate code generation; databases verify facts. **"Deterministic components should govern probabilistic ones, not the reverse."**

## Governance Implications

Enterprise AI failures stem from inverting this hierarchy. Systems treating generative outputs as authoritative claims lack epistemological accountability. The distinction clarifies deployment architecture: use probabilistic layers for synthesis; reserve deterministic cores for truth claims.

Formal research establishes hallucination as structural in language models, irreducible through architectural improvements alone.

---

*James (JD) Longmire is a Northrop Grumman Fellow conducting independent research on AI epistemology and governance.*
