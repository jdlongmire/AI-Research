# Reddit Post: r/LLMPhysics

---

Title: A framework for understanding why LLMs generate confident theories without knowing if they're valid - AI Dunning-Kruger (AIDK)

---

Post:

This subreddit is a fascinating case study in what I've been calling the AI Dunning-Kruger Effect.

Here's the issue. When an LLM generates a physics theory, it does so with the same fluent confidence whether it's reproducing established physics, interpolating plausibly between known concepts, or generating complete nonsense that sounds sophisticated. The system has no internal signal distinguishing these cases. It can't know when it's in well-represented training territory versus when it's extrapolating into unreliable pattern space.

I've been developing a framework to formalize this. The core argument is that human Dunning-Kruger is correctable - we bump into reality, run experiments, get feedback, and recalibrate. LLMs can't do this. They operate in a closed symbolic space with no grounding wire to actual physics. They've learned what physics text looks like, not what makes physics true.

This creates a structural condition I call AIDK where the system produces uniform confidence regardless of reliability, has no mechanism for detecting its own competence boundaries, and cannot self-correct through encounter with reality.

The interesting part for this community is what I call the Interactive Dunning-Kruger Effect. When someone without physics expertise asks an LLM to generate a theory, they can't evaluate whether the output is valid. The LLM can't signal its own uncertainty. The person's confidence increases without warrant, and they may end up defending a position that was never grounded in anything.

This isn't to say LLM-generated theories are worthless. They might occasionally hit on something interesting through novel combinations. But without a physicist in the loop who can actually evaluate the output against reality, there's no way to distinguish signal from noise. The fluency is identical either way.

The framework proposes stratifying AI use by who is doing the validation. An end user consuming LLM physics output is in a very different epistemic position than a physicist using an LLM as a drafting tool and then evaluating the result against their domain knowledge.

Full framework with citations: https://doi.org/10.5281/zenodo.18316059

Shorter writeup: https://airesearchandphilosophy.substack.com/p/the-ai-dunning-kruger-effect-why

Curious what this community thinks. Does this match your observations of LLM-generated theories?
