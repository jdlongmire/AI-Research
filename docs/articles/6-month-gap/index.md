---
layout: article
title: "The 6-Month Gap"
subtitle: "What DIB actually gives up by deploying US-origin open models instead of frontier"
date: 2026-03-23
author: JD Longmire
featured: true
featured_image: /articles/6-month-gap/featured.png
categories: [AI Governance]
tags: [defense, frontier-ai, llama, deployment, air-gap]
---

The last piece I wrote about frontier AI and the defense industrial base — [The Frontier Is Closed](https://aithinkr.net/articles/frontier-closed-defense/) — left me with a question I hadn't fully answered.

I'd argued that DIB has more access to frontier models than most people realize, but that two structural gaps remain: IP/data sovereignty and air-gapped deployment. Fair enough. But that framing assumed the gap between frontier and deployable models actually matters. What if it doesn't? What if US-origin open models are "good enough" for most defense use cases?

So I went looking.

---

The deployable US-origin landscape has one clear frontrunner: Meta's Llama 3.1 405B. 405 billion parameters, 128K context window, solid reasoning and tool use, permissively licensed, deployable on-premises without phoning home. Microsoft's Phi-4, IBM's Granite, and NVIDIA's Nemotron fill smaller niches, but Llama is the credible frontier-adjacent option.

A note on what's not on the table: Chinese-origin models like DeepSeek and Qwen are technically capable, sometimes impressively so. But NOFORN restrictions and supply chain security requirements make them non-starters for defense work. When I say "deployable," I mean US-origin, clean provenance, no foreign dependency. That narrows the field considerably.

---

So where's the gap?

It depends on what you're asking the model to do.

For reasoning depth (multi-step planning, novel problem decomposition, working through genuinely hard problems) frontier models are significantly ahead. Not incrementally. Significantly. The same is true for complex instruction following. If you need the model to handle nested, conditional instructions with multiple constraints, frontier RLHF investment shows. Claude and GPT-4 are better at this than Llama. Not because Llama is bad, but because Anthropic and OpenAI have spent more on alignment and instruction-tuning.

Agentic behavior (tool use, function calling, error recovery, maintaining state across multi-step workflows) is another gap. Frontier models have been trained explicitly for this. Open models are catching up, but they're catching up.

Context utilization is subtler. Raw context length is comparable; Llama 3.1 and Claude both handle 128K tokens. But effective use of that context (finding the relevant needle, maintaining coherence across the full window) favors frontier.

Hallucination rate matters too. Frontier models are better at knowing what they don't know.

---

The gap is smaller than I expected in several areas.

Code generation: Llama 3.1 405B is competitive with frontier on most benchmarks. Close enough that for many code assistance use cases, the difference is marginal.

Summarization and extraction: when the task is "read this document and pull out relevant information," the gap narrows for mechanical tasks.

RAG retrieval augmentation: when you ground the model in retrieved documents, base capability matters less. Open models do this reasonably well.

Domain-specific fine-tuning: this is where things get interesting. A fine-tuned Llama on your specific domain can match or exceed frontier on narrow tasks. The generalist advantage of frontier matters less when you've specialized for your problem.

---

A word on fine-tuning.

Can DIB close the gap through domain-specific work? Partially. Fine-tuning can teach a model your vocabulary, your document structures, your preferred output formats. It can make an open model much better at your specific tasks than its base weights would suggest.

But fine-tuning doesn't add capabilities the base model lacks. If Llama 3.1 struggles with multi-step planning, fine-tuning it on your planning documents won't fix that.

Fine-tuning is a bridge, not a shortcut.

---

I'd frame it as a "6-month gap." Llama 3.1 405B is roughly where frontier was six to twelve months ago. If your use case could have been solved by Claude or GPT-4 a year ago, open models can probably handle it now.

That's not nothing. But it's also not an insurmountable chasm. For a lot of defense use cases (document summarization, code assistance, structured data extraction, domain-specific Q&A with RAG) the gap is livable.

Where it hurts: anything requiring genuine novel reasoning, complex multi-step agentic workflows, or high-stakes decisions where hallucination risk matters. For those, you want frontier. And that brings us back to the original problem: how do you get frontier capability into air-gapped environments?

---

My instinct: use open models for what they're good at now, and keep pressure on the frontier access problem for use cases where the gap actually matters.

Don't pretend Llama is Claude. But don't pretend every problem needs Claude either.
