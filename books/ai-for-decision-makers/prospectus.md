# Book Prospectus

## AI for Decision-Makers
### How It Works, Where It Fails, When to Trust It

---

## Author

James (JD) Longmire
Northrop Grumman Fellow, Chief Architect – Digital Ecosystems
MS Applied AI (in progress)
ORCID: 0009-0009-1383-7698

---

## Overview

Every professional now encounters artificial intelligence. Lawyers use it for research. Doctors see it in diagnostic tools. Managers evaluate vendor pitches. Writers wonder if it will replace them. Executives make adoption decisions with millions on the line.

Most of these professionals are flying blind.

The typical AI education available to non-engineers falls into two categories: hype that oversells capabilities, or fear that undersells them. Neither equips decision-makers to evaluate claims, structure oversight, or calibrate trust appropriately. The result is a landscape of bad decisions: over-reliance on systems that fail silently, under-utilization of systems that could help, and vendor relationships built on demonstrations rather than understanding.

*AI for Decision-Makers* fixes this. It explains how AI actually works—from basic computation through neural networks to the large language models powering ChatGPT and its competitors—using a two-register approach: accessible narrative for intuition, technical detail for those who want depth. The goal is not to turn professionals into engineers but to make them literate enough to ask the right questions.

But understanding mechanism is only the beginning. The book's core contribution is a framework for understanding *why* AI systems fail the way they do and *how* to structure human oversight accordingly.

**AI Dunning-Kruger (AIDK)** names the structural condition: AI systems produce outputs with uniform confidence regardless of actual reliability. They cannot detect their own competence boundaries. They cannot self-correct through encounter with reality. This isn't a bug awaiting a fix—it's an architectural feature that persists across scaling and fine-tuning.

**The Interactive Dunning-Kruger Effect (IDKE)** describes what happens when AIDK meets human limitations. Users who can't evaluate outputs interact with systems that can't signal unreliability. Confidence transfers from machine to human, untethered from warrant. The people most vulnerable to overconfidence are most amplified by AI interaction.

**Human-Curated, AI-Enabled (HCAE)** provides the response: a deployment framework that stratifies AI use by the epistemic authority of the human responsible for validation. Four tiers—User, Professional, Expert, Synthesis—with appropriate safeguards for each. Safety scales with human authority, not model capability.

The result is a book that leaves professionals genuinely informed about AI's capabilities, diagnostically equipped to understand its failures, and practically armed with frameworks for deployment decisions.

---

## Target Audience

**Primary:** Professionals who use, manage, purchase, or make policy about AI systems without engineering backgrounds. This includes:
- Executives and managers evaluating AI adoption
- Lawyers, doctors, consultants, and other professionals using AI tools
- Product managers working with AI features
- Procurement officers assessing vendor claims
- Policy makers and regulators needing technical grounding
- Educators incorporating AI into teaching

**Secondary:** Engineers and data scientists who want accessible explanations for communicating with non-technical stakeholders. The book provides vocabulary and frameworks for cross-functional conversations.

**Tertiary:** Informed general readers who want rigorous understanding without requiring a technical background.

---

## Comparative Titles

**Ethan Mollick, *Co-Intelligence: Living and Working with AI* (Portfolio, 2024)**
Mollick offers practical advice for AI adoption but focuses on use cases rather than mechanism. *AI for Decision-Makers* provides the technical foundation that makes Mollick's practical advice evaluable.

**Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans* (Farrar, Straus and Giroux, 2019)**
Mitchell writes accessibly about AI for general audiences but without the decision-maker focus or deployment frameworks. *AI for Decision-Makers* is more practically oriented and includes AIDK/HCAE as actionable tools.

**Ajay Agrawal, Joshua Gans, and Avi Goldfarb, *Prediction Machines* (Harvard Business Review Press, 2018)**
An economics-focused treatment of AI as prediction technology. Strong on business implications, lighter on mechanism. *AI for Decision-Makers* goes deeper on how the technology works and why it fails.

**Meredith Broussard, *Artificial Unintelligence* (MIT Press, 2018)**
A critical take on AI hype with good skeptical framing, but predates the large language model revolution. *AI for Decision-Makers* covers current technology with similar epistemic caution.

**Kai-Fu Lee, *AI Superpowers* (Houghton Mifflin Harcourt, 2018)**
Focused on geopolitics and industry dynamics rather than mechanism or deployment frameworks. Different angle, complementary rather than competitive.

*AI for Decision-Makers* occupies a unique position: technically grounded, failure-aware, and practically oriented toward deployment decisions.

---

## Chapter Outline

### Part I: How It Works

**Chapter 1: A Brief History of Mechanical Minds**
The dream is old. The disappointment is recurring. The pattern is structural. From Leibniz's calculus of reason to Babbage and Lovelace (who noted the machine "has no pretensions to originate anything"), through Turing's universal machine, the AI summers and winters, expert systems, neural networks, deep learning, and now large language models. Each generation crosses a capability threshold; each expects the threshold to be the gap; each discovers the gap remains. The architecture never changed—it's still symbol manipulation. The professional thread: the pattern of overpromise and underdelivery is structural, not incidental. Knowing the history calibrates expectations and inoculates against hype.

**Chapter 2: What Is Computation?**
The foundation: computers manipulate symbols according to rules. The difference between syntax (symbol manipulation) and semantics (meaning). Why this distinction matters for evaluating AI claims. The gap that persists regardless of scale.

**Chapter 3: Learning from Data**
The core insight of machine learning: instead of programming rules, let the system discover patterns from examples. Training vs. inference. The problem of generalization. What "learning" means—and doesn't mean—when applied to machines.

**Chapter 4: Neural Networks in Plain English**
Layers of simple computations composed into complex functions. How networks are trained: loss functions, gradient descent, backpropagation. The "chef tasting soup" metaphor grounded in intuition. What neural networks can represent and why they work.

**Chapter 5: How Computers Learned Language**
The problem of turning words into numbers. Tokenization and the geometry of meaning. Embedding spaces where similar words cluster. The shift from symbols to vectors.

**Chapter 6: The Architecture of Language Models**
Embedding, transforming, and unembedding: the three acts of every language model. Attention mechanisms and how models learn context. The transformer architecture that powers ChatGPT, Claude, and competitors. What happens between your prompt and the response.

**Chapter 7: Training at Scale**
Next-token prediction as the training objective. Massive datasets, massive compute, emergent capabilities. RLHF: how models are fine-tuned for helpfulness. What training shapes—and what it can't shape.

### Part II: Where It Fails

**Chapter 8: The Confidence Problem**
AI systems produce outputs with uniform fluency regardless of reliability. They sound equally confident when right and when wrong. No internal signal distinguishes knowledge from confabulation. Introduction of the pattern this chapter will explain.

**Chapter 9: AI Dunning-Kruger (AIDK)**
Formal introduction of AIDK: the structural condition where systems cannot detect their own competence boundaries and cannot self-correct through encounter with reality. Unlike human overconfidence, AIDK is architectural—permanent, not developmental. Why scaling doesn't fix it. Why fine-tuning doesn't fix it. Why it's a feature, not a bug.

**Chapter 10: Hallucination as Architecture**
Why AI systems confabulate. The inevitability results: mathematical proofs that hallucination cannot be eliminated from systems trained on finite data. Hallucination isn't failure to learn enough—it's a consequence of how learning works. Implications for deployment.

**Chapter 11: The Interaction Risk (IDKE)**
What happens when AIDK meets human epistemic limitations. Users who can't evaluate outputs interact with systems that can't signal unreliability. Confidence laundering: how ungrounded machine confidence becomes defended human belief. The people most vulnerable to overconfidence are most amplified. Case studies in IDKE-driven failure.

**Chapter 12: Enterprise AI Failure Patterns**
The documented 70-95% failure rate of enterprise AI projects. Applying AIDK as diagnostic: why projects fail confidently, why demos don't predict deployment, why "human in the loop" often doesn't help. Patterns that repeat across industries.

### Part III: When to Trust It

**Chapter 13: The HCAE Framework**
Introduction of Human-Curated, AI-Enabled deployment. The core insight: safety scales with human epistemic authority, not model capability. Four tiers:
- **User-Curated (UCAE):** No domain expertise to evaluate. Appropriate for low-stakes drafting and brainstorming only.
- **Professional-Curated (PCAE):** Trained professional reviews within constraints. Plausibility checking possible; edge-case failure still likely.
- **Expert-Curated (ECAE):** Domain expert with independent truth-evaluation capacity. Confidence flows from human to system.
- **Synthesis-Curated (SCAE):** Expert judgment combined with formal validation (compilers, test suites, proof assistants). Trust replaced by proof.

**Chapter 14: Matching Tiers to Tasks**
How to assess which tier a given application requires. Factors: stakes, expertise availability, verification infrastructure, error recoverability. Decision trees and heuristics for common use cases. When to upgrade tier requirements. When to reject deployment entirely.

**Chapter 15: Designing Human Oversight**
Why "human in the loop" fails when the wrong human is in the loop. Selecting validators by epistemic authority, not availability. Structuring review processes that actually catch errors. Avoiding IDKE in oversight design. The difference between checkbox compliance and genuine validation.

**Chapter 16: Evaluating Vendor Claims**
What to ask vendors that they don't want you to ask. Red flags in demos. How to probe for AIDK vulnerability. Contractual protections. Pilot design that reveals deployment reality rather than demo conditions. Building organizational capacity to evaluate.

**Chapter 17: Organizational AI Literacy**
Building teams that can work with AI effectively. Training programs that calibrate trust rather than inflate it. Creating feedback loops that surface failures. Institutional memory for AI incidents. Culture that rewards appropriate skepticism.

### Part IV: What's Next

**Chapter 18: Current Trajectory**
Where the technology is heading based on disclosed research directions. Scaling laws and their limits. Multimodal models. Agents and tool use. What would have to change for current limitations to be overcome—and why those changes are harder than they appear.

**Chapter 19: Decisions Under Uncertainty**
Living with technology whose trajectory is unclear. Avoiding both over-commitment and under-utilization. Building organizational flexibility. The professional's posture: informed skepticism, continuous calibration, willingness to update.

---

## Format and Features

**Length:** Approximately 70,000–80,000 words (19 chapters averaging 3,500–4,000 words each, plus front and back matter)

**Two-Register Structure:** Each chapter uses "Story Time" (accessible narrative with concrete metaphors) as the primary mode, with "Technical Time" sections for readers who want mechanism. Technical sections can be skipped without losing the thread.

**AIDK/HCAE Framework:** The book's core intellectual contribution, introduced in Parts II and III and applied throughout. Provides vocabulary and decision tools readers can use immediately.

**Figures:** Each chapter includes 2–4 explanatory figures: architecture diagrams, decision trees, risk matrices, case study illustrations. Designed to be reproducible in presentations and internal documents.

**Case Studies:** Real-world examples of AI deployment success and failure, analyzed through the AIDK/HCAE lens. Drawn from healthcare, legal, financial, and enterprise contexts.

**Decision Tools:** Checklists, decision trees, and assessment frameworks designed for practical use. Available as downloadable resources.

**Chapter Summaries:** Each chapter ends with key takeaways formatted for quick reference and organizational sharing.

---

## Author Platform

**Professional Credibility:** 30+ years in systems architecture across commercial and aerospace-defense sectors. Current role as Chief Architect for Digital Ecosystems at Northrop Grumman provides direct engagement with enterprise AI implementation at scale. Pursuing MS in Applied AI ensures current technical knowledge.

**Framework Development:** AIDK and HCAE frameworks developed through independent research, with academic papers in development for peer-reviewed publication. Frameworks have been tested in enterprise architecture contexts.

**Speaking and Training:** Experience communicating complex technical concepts to non-technical audiences in corporate and educational settings.

**Writing Sample:** Two completed chapters ("How a Computer Learns Words" and "The Three Acts of a Language Model") are available demonstrating the two-register approach and intended accessibility.

**Audience Access:** Professional network spans enterprise technology leadership, AI practitioners, and business decision-makers. LinkedIn platform provides launch channel for professional audience.

---

## Market Opportunity

The AI literacy gap is a recognized problem. Organizations are adopting AI tools faster than their personnel can evaluate them. The market for accessible AI education is growing, but most offerings are either too superficial (blog posts, webinars) or too technical (textbooks, courses).

*AI for Decision-Makers* fills a specific gap: serious enough to ground real decisions, accessible enough for professionals without engineering backgrounds, and practically oriented toward deployment rather than abstract understanding.

The AIDK/HCAE framework is a differentiator. No comparable book offers a diagnostic framework for AI failure (AIDK) combined with a deployment framework calibrated to human epistemic authority (HCAE). This gives the book both conceptual novelty and practical utility.

Corporate training and bulk sales represent a significant secondary market. The book's structure—clear frameworks, decision tools, chapter summaries—makes it suitable for organizational learning programs.

---

## Related Title

*Symbols Without Souls: The Christian's Guide to Artificial Intelligence* covers the same technical foundation with theological framing and philosophical depth for Christian readers. The two books share significant material in early chapters but diverge in application: *Symbols Without Souls* toward theological anthropology, *AI for Decision-Makers* toward deployment frameworks. Cross-references between books extend reach without requiring both.

---

## Timeline

- **Proposal submission:** [Date]
- **Sample chapters completed:** Available now
- **Full manuscript delivery:** 12 months from contract
- **Preferred publication:** 18 months from contract

---

## Contact

James (JD) Longmire
jdlongmire@outlook.com
ORCID: 0009-0009-1383-7698
