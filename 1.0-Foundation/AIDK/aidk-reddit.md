# Reddit Post: AIDK Framework

Suggested subreddits: r/artificial, r/MachineLearning, r/philosophy, r/ArtificialIntelligence, r/singularity

---

Title: I developed a framework for understanding why LLMs are confidently wrong - the AI Dunning-Kruger Effect

---

Post:

You know how ChatGPT, Claude, Gemini all answer everything with the same confident tone whether they're right or completely making things up? I've been thinking about why this isn't something we can just train away with more data or better techniques.

Here's my take. Human Dunning-Kruger is correctable. We bump into reality, fail, get feedback, and recalibrate over time. LLMs can't do this. They operate in a closed symbolic space - text about reality - with no actual contact with reality itself. There's no grounding wire. No feedback loop that tells them "that was wrong" in a way that updates their relationship to truth rather than just shifting token probabilities.

I'm calling this AI Dunning-Kruger or AIDK. It's a structural condition, not a training artifact. The system produces uniform confidence regardless of reliability, has no mechanism for detecting its own competence boundaries, and can't self-correct through encounter with reality.

But here's what really concerns me. When this meets human uncertainty, it amplifies. Think about it - you ask about something outside your expertise, the AI responds confidently, you can't really evaluate whether it's correct because that's why you asked in the first place, the AI has no way to signal its own unreliability, and suddenly your confidence increases without any actual warrant for it. You end up defending a position you never independently evaluated because it feels like yours now.

The AI's inability to know what it doesn't know gets laundered into your confident assertion. And the people most vulnerable to the human version of Dunning-Kruger are the ones most amplified by the AI version.

The solution I'm proposing isn't better models - it's better deployment design. We need to stratify AI use by the epistemic authority of whoever is in the loop. An end user versus a domain expert versus an expert with formal verification tools are completely different risk profiles. Just saying "human in the loop" doesn't cut it.

I published the full framework with citations on Zenodo if anyone wants to dig in: https://doi.org/10.5281/zenodo.18316059

Shorter version on Substack: https://airesearchandphilosophy.substack.com/p/the-ai-dunning-kruger-effect-why

What do you all think? Is this a useful frame or am I missing something obvious?
