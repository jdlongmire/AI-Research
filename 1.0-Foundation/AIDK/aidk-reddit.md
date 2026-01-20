# Reddit Post: AIDK Framework

**Suggested subreddits:** r/artificial, r/MachineLearning, r/philosophy, r/ArtificialIntelligence, r/singularity

---

**Title:** I developed a framework for understanding why LLMs are confidently wrong: the AI Dunning-Kruger Effect (AIDK)

---

**Post:**

You know how ChatGPT/Claude/Gemini answer everything with the same confident tone—whether they're right or completely hallucinating? I've been working on a framework to explain why this isn't fixable with more training or better data.

**The core argument:** Human Dunning-Kruger is correctable. We bump into reality, fail, get feedback, and recalibrate. LLMs can't do this. They operate in a closed symbolic space (text about reality) with no actual contact with reality itself. There's no grounding wire. No feedback loop that says "that was wrong" in a way that updates their relationship to truth rather than just token probabilities.

This creates what I call **AIDK (AI Dunning-Kruger)** — a *structural* condition, not a training artifact:
- Uniform confidence regardless of reliability
- No mechanism for detecting competence boundaries
- No self-correction through encounter with reality

**The scary part:** When AIDK meets human uncertainty, it amplifies. I call this **IDKE (Interactive Dunning-Kruger Effect)**:

1. You ask about something outside your expertise
2. AI responds confidently
3. You can't evaluate it (that's why you asked)
4. AI can't signal its own unreliability
5. Your confidence increases without warrant
6. You now defend a position you never evaluated

The AI's inability to know what it doesn't know gets laundered into your confident assertion. The people most vulnerable to human DK are most amplified by AI DK.

**The proposed solution:** A deployment framework (HCAE) that stratifies AI use by the epistemic authority of the human in the loop. "Human in the loop" shouldn't be undifferentiated—an end user vs. a domain expert vs. expert + formal verification are completely different risk profiles.

I've published the full framework with verified citations on Zenodo (open access): https://doi.org/10.5281/zenodo.18316059

Shorter writeup on Substack: https://airesearchandphilosophy.substack.com/p/the-ai-dunning-kruger-effect-why

Curious what this community thinks. Is AIDK a useful frame? What am I missing?

---

**TL;DR:** LLMs have a structural epistemic limitation (AIDK) that makes them confidently wrong without knowing it. This can't be trained away because it's architectural. When combined with human uncertainty, it amplifies false confidence (IDKE). The solution is deployment design, not better models.
