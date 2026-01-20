# Reddit Post: r/LLMPhysics

---

Title: Your LLM physics theory is probably wrong, and here's why

---

Post:

I've been lurking here for a while and I want to offer a framework for why most of the theories posted here are almost certainly wrong, even when they sound compelling.

The problem isn't that LLMs are dumb. The problem is they have no way to know when they're wrong.

When you ask an LLM to generate a physics theory, it produces output with the same confident fluency whether it's reproducing established physics, making plausible-sounding interpolations, or generating complete nonsense dressed in technical language. There's no internal signal distinguishing these cases. The model learned what physics text looks like, not what makes physics true.

I call this the AI Dunning-Kruger Effect. Human overconfidence is correctable because we bump into reality. We run experiments, get results that don't match predictions, and update our understanding. LLMs can't do this. They operate entirely in a symbolic space derived from text about reality with no actual contact with reality itself.

So when your LLM generates a theory about quantum gravity or unified fields or whatever, it's pattern-matching to what such theories look like in its training data. It has no idea if the math works out, if the predictions are testable, if it contradicts established results, or if it's just word salad that sounds sophisticated.

Here's the uncomfortable part. If you're not a physicist, you can't tell either. And the LLM can't signal its own uncertainty because it doesn't have any. The confidence is a learned behavior, not a reliability indicator.

The result is what I call the Interactive Dunning-Kruger Effect. You ask about something outside your expertise, the LLM responds with fluent confidence, you can't evaluate it, and your confidence increases without any actual warrant. You end up defending a theory that was never grounded in anything except statistical patterns over physics text.

This doesn't mean LLMs are useless for physics exploration. But it does mean that without someone who actually understands physics evaluating the output, you have no way to distinguish an interesting insight from sophisticated-sounding garbage. The fluency is identical.

Full framework: https://doi.org/10.5281/zenodo.18316059

Shorter version: https://airesearchandphilosophy.substack.com/p/the-ai-dunning-kruger-effect-why

Not trying to kill the fun here. Just offering a framework for why we should be skeptical of LLM-generated theories by default.
