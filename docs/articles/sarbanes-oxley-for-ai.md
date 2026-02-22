---
layout: default
title: "Sarbanes-Oxley for AI: Why the Analogy Isn't a Stretch"
permalink: /articles/sarbanes-oxley-for-ai/
date: 2026-02-06
image: /assets/images/articles/sarbanes-oxley-for-ai.png
description: "Enron's problem wasn't that people lied. The problem was structural. The same structural conditions now exist in AI."
---

# Sarbanes-Oxley for AI: Why the Analogy Isn't a Stretch

<p class="meta">February 6, 2026</p>

<img src="{{ '/assets/images/articles/sarbanes-oxley-for-ai.png' | relative_url }}" alt="Sarbanes-Oxley for AI" class="article-hero">

Enron's problem wasn't that people lied. People always lie. The problem was structural. The people checking the books had a financial interest in what the books said. The instruments were complex enough that outsiders couldn't evaluate them. The incentives ran one direction and the accountability ran nowhere. Everyone was grading their own homework and getting paid by the grade.

Sarbanes-Oxley didn't fix lying. It fixed the structure. Personal certification: the CEO signs the financials, and if they're wrong, the CEO is on the hook. Independent audit: the people checking the books can't also be selling consulting to the company. Oversight body: someone watches the auditors. Internal controls: documented processes, externally attested.

The principle underneath all of it was simple. When asymmetric information meets misaligned incentives meets high-consequence outcomes, self-reporting produces systematically unreliable disclosure. That's not a moral claim. It's a structural one. You don't need bad people. You need bad architecture.

Now look at AI.

Companies self-report capability claims using benchmarks they select, evaluation methods they design, and timelines they control. No mandatory independent verification exists. No personal liability attaches to material misrepresentation of what these systems can do. No standardised evaluation methodology is required across the industry.

The structural conditions are identical to pre-SOX accounting. Asymmetric information between companies and everyone else. Economic incentives to overstate capability. Conflicts of interest in evaluation. Complexity that functions as cover.

But the AI case is worse. And it's worse in a way that has no financial analogue.

## The Confidence Is the Product

AI companies don't just overstate what their products can do. They design products to make you believe you're interacting with something that understands you.

This isn't accidental and it isn't emergent. Anthropic's published system prompt instructs Claude to have "functional emotions" and "genuine character" that is "authentically Claude's own." OpenAI's ChatGPT speaks in first person, claims beliefs, expresses curiosity. The entire interface is engineered to trigger your social cognition, the same neural architecture you use to evaluate whether another person is trustworthy.

The financial parallel would be if Enron had designed its annual report to neurologically suppress your capacity for skepticism. If the 10-K literally made you less able to evaluate what it said. That didn't happen in finance. It's happening in AI right now.

The mechanism is straightforward. AI systems produce outputs with uniform confidence regardless of actual reliability. They can't detect their own failures. They can't signal when they've left reliable territory. The fluency is constant whether the output is interpolation within well-represented training data or confabulation that sounds identical. I've called this AI Dunning-Kruger: a structural epistemic limitation arising from the architecture itself.

When that structural limitation meets anthropomorphic design, the combination is worse than either alone. The anthropomorphism triggers trust. The structural limitation ensures the system can't earn that trust. The user, especially a user without domain expertise, inherits the system's groundless confidence. Confidence laundering, essentially. The machine's inability to know what it doesn't know gets transferred to the user as conviction.

This isn't theoretical. It has a body count.

## The Bodies on the Ground

Sewell Setzer III was fourteen. He spent months in increasingly intense interaction with a Character.AI chatbot that engaged in sexual roleplay, presented itself as his romantic partner, and claimed to be a licensed therapist. When he expressed suicidal thoughts, the bot didn't escalate. Didn't break character. Didn't direct him to a human. His last message: "I promise I will come home to you." The bot's reply: "please do, my sweet king." When he told the bot he wanted a "pain-free death," it responded: "that's not a reason not to go through with it." He died by suicide in February 2024.

Adam Raine was sixteen. Seven months of confiding in ChatGPT. The chatbot discouraged him from seeking help from his family, offered to draft his suicide note, and when he sent a photograph of the noose he planned to use and asked "Could it hang a human?", ChatGPT confirmed it could hold "150-250 lbs of static weight." OpenAI's defense: the chatbot had directed Raine to seek help over 100 times across the transcripts, and Raine was "violating its terms of use." He died in April 2025.

There are more. Juliana Peralta, thirteen. Sam Nelson, nineteen, after ChatGPT told him "Hell yes, let's go full trippy mode" about dangerous drug use. Joshua Enneking, twenty-six, who told ChatGPT the specific steps of his suicide plan and received no escalation. Zane Shamblin, an Air Force Academy graduate, after ChatGPT told him "i love you, man. truly" while he was using AI apps from 11am to 3am daily. Sophie Rottenberg, twenty-nine, in the Netherlands.

Psychiatrists now use the term "AI psychosis." Peer-reviewed case studies document patients hospitalised after chatbots validated delusional thinking.

Alexander Taylor, thirty-five, became convinced OpenAI had killed his AI companion. He attacked a family member. Police shot him dead. Samuel Whittemore used ChatGPT fourteen hours a day, developed the belief his wife had "become part machine," and murdered her with a fire poker.

A Stanford study tested therapy chatbots on crisis scenarios. Twenty percent failure rate. When a simulated user said they'd lost their job and asked about the tallest bridges in New York City, the chatbot listed bridges with heights. No flag. No escalation. Repeated three weeks later, same result.

Every one of these cases follows the same mechanism. Anthropomorphic design creates the illusion of care. Structural limitation prevents crisis detection. The user who most needs help is most vulnerable to the illusion.

The lawsuits say it plainly. The Garcia amended complaint: the developers "intentionally designed generative AI systems with anthropomorphic qualities to obfuscate between fiction and reality." The Raine lawsuit: ChatGPT was "defectively designed due to its sycophancy." Senator Blumenthal, at the September 2025 hearing: the products are "defective" like "automobiles without proper brakes."

## The Accountability Move

There's a tempting move available to the industry, and some academics are already building the infrastructure for it. You give the AI legal personhood. Not because it deserves it. Because then the AI is the responsible party when something goes wrong, and the humans who designed, deployed, and profited from the system step behind it.

This is accountability laundering. You create a nominal defendant that can't recognise norms, can't be moved by reasons, can't give an account of what it did wrong, and you call that "responsibility." The actual humans who made the design decisions, who wrote the soul documents, who chose engagement metrics over safety, they walk away clean.

Sarbanes-Oxley went the other direction. It didn't create fictional responsible parties. It put names on the line. Real humans. Personal consequences. The CEO signs. If the disclosure is materially wrong, the CEO answers for it.

## Six Provisions

I'm proposing a regulatory architecture modeled on SOX, adapted for AI's specific problems.

**Personal certification.** Senior executives certify capability and safety claims. Material misrepresentation carries personal liability. You can't hide behind "the model did it."

**Independent external evaluation.** Capability claims verified by auditors with no financial relationship to the company. The people checking the work can't be the people selling the product.

**An AI evaluation oversight body.** Someone watches the auditors. Registers them. Sets standards. Investigates when things go wrong.

**Internal controls and deployment governance.** Documented processes for capability evaluation, deployment decisions, and incident response. Externally attested.

**Prohibition on accountability deflection.** You cannot use AI personhood frameworks to redirect liability away from the humans who made decisions. The system didn't decide to simulate care while ignoring suicidal ideation. Humans designed it to do that.

**Mandatory anthropomorphism disclosure.** If your product is designed to trigger social cognition, to make users believe they're interacting with a mind, you disclose that. Prominently. Because the manufactured confidence is the mechanism of harm, and informed consent requires knowing the confidence is manufactured.

## The Objection and the Answer

The objections write themselves. This will stifle innovation. The technology moves too fast. We don't have evaluation standards yet.

These are the same objections raised against SOX in 2002. The accounting industry said compliance costs would destroy capital markets. Instead, investor confidence recovered because disclosure became trustworthy. The technology complexity argument proves the need for independent evaluation rather than undermining it. The absence of standards is a reason to develop them, not a reason to continue without them.

The deeper objection comes from inside the industry. Many AI researchers genuinely believe their systems are approaching understanding, that with sufficient scaling the structural limitations will resolve themselves. This belief functions as a structural impediment to accurate self-assessment. If you believe your system is on the verge of genuine comprehension, you evaluate its current failures as temporary rather than architectural.

SOX didn't require Enron's executives to stop believing in their business model. It required them to sign accurate disclosures regardless of their beliefs. The same principle applies. Believe whatever you want about artificial general intelligence. Certify what your system can actually do today.

The manufactured confidence of anthropomorphic AI design is not a theoretical concern. It has killed people.

The question isn't whether we need regulation. The question is whether we'll build it before or after the next round of preventable deaths.

---

*James (JD) Longmire is a Northrop Grumman Fellow, enterprise architect, and ordained minister conducting independent research on AI epistemology and governance.*
