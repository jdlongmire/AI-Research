# Book Prospectus

## Symbols Without Souls
### The Christian's Guide to Artificial Intelligence

---

## Author

James (JD) Longmire
Northrop Grumman Fellow, Chief Architect – Digital Ecosystems
MS Applied AI (in progress)
ORCID: 0009-0009-1383-7698

---

## Overview

Artificial intelligence is everywhere—in our phones, our search results, our news feeds, and increasingly our conversations. Large language models like ChatGPT produce text that sounds thoughtful, knowledgeable, even wise. They pass professional exams, write poetry, and argue philosophy. Naturally, people ask: *Is this thing thinking? Does it understand? Could it have a soul?*

Most answers to these questions fail in one of two ways. Popular accounts mystify AI, treating it as an inscrutable oracle whose inner workings are beyond ordinary comprehension. Technical accounts demystify it but assume mathematical fluency that most readers lack. Neither equips Christians to think clearly about what AI is, what it isn't, and why the difference matters.

*Symbols Without Souls* fills this gap. It explains how AI actually works—from basic computation through neural networks to large language models—using a two-register approach: accessible narrative ("Story Time") followed by technical detail ("Technical Time"). Readers can engage at the level that suits them, building genuine understanding rather than borrowing borrowed confidence.

But the book doesn't stop at mechanics. It presses the philosophical question: *What is missing when a machine manipulates symbols without access to meaning?* And it answers from a distinctly Christian framework, drawing on the doctrine of the Logos, the imago Dei, and a robust theological anthropology to articulate what distinguishes human cognition from even the most sophisticated pattern-matching.

The result is a book that leaves readers genuinely informed about AI's capabilities and limitations, appropriately skeptical of inflated claims, and theologically grounded in their understanding of what it means to be a thinking, knowing, ensouled creature made in God's image.

---

## Target Audience

**Primary:** Educated Christians who encounter AI in their work, news consumption, or daily life and want to understand it without either uncritical enthusiasm or reflexive fear. Pastors, teachers, professionals, and thoughtful laypeople who sense that AI raises important questions but lack the technical background to evaluate competing claims.

**Secondary:** Technically literate readers (engineers, developers, data scientists) who want a philosophically and theologically serious treatment of AI's nature and limits. Christians in technical fields often find that popular Christian engagement with technology is shallow; this book takes both the technology and the theology seriously.

**Tertiary:** Secular readers interested in a rigorous but accessible explanation of AI mechanics, who may find the theological framework a useful foil for their own thinking even if they don't share its commitments.

---

## Comparative Titles

**John Lennox, *2084: Artificial Intelligence and the Future of Humanity* (Zondervan, 2020)**
Lennox offers a Christian perspective on AI but focuses primarily on ethical and eschatological questions rather than technical explanation. *Symbols Without Souls* complements this by providing the technical foundation that makes ethical evaluation possible.

**Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans* (Farrar, Straus and Giroux, 2019)**
Mitchell writes accessibly about AI for general audiences but without theological engagement. *Symbols Without Souls* covers similar technical ground with the two-register approach and adds the philosophical and Christian framework.

**Stephen Wolfram, *What Is ChatGPT Doing... and Why Does It Work?* (Wolfram Media, 2023)**
Wolfram explains transformer architecture in detail but assumes comfort with mathematical notation and offers no theological reflection. *Symbols Without Souls* is more accessible and addresses questions Wolfram doesn't ask.

**Jason Thacker, *The Age of AI: Artificial Intelligence and the Future of Humanity* (Zondervan, 2020)**
Thacker addresses AI from a Christian ethics perspective but provides limited technical depth. *Symbols Without Souls* goes deeper on mechanism while arriving at similar ethical and anthropological conclusions.

*Symbols Without Souls* occupies a unique position: technically substantive, philosophically rigorous, theologically grounded, and genuinely accessible.

---

## Chapter Outline

### Part I: Foundations

**Chapter 1: A Brief History of Mechanical Minds**
The dream is old. The disappointment is recurring. The pattern is structural. From Leibniz's calculus of reason to Babbage and Lovelace (who noted the machine "has no pretensions to originate anything"), through Turing's universal machine, the AI summers and winters, expert systems, neural networks, deep learning, and now large language models. Each generation crosses a capability threshold; each expects the threshold to be the gap; each discovers the gap remains. The architecture never changed—it's still symbol manipulation. The theological thread: the persistent attempt to build minds from machines reflects something about how we understand ourselves, made in the image of a Creator, attempting to create in our own image.

**Chapter 2: Symbols and Machines**
What is computation? Turing's insight that thinking can be modeled as symbol manipulation—and the crucial gap between manipulating symbols and understanding meaning. The Chinese Room argument as a frame for the book's central question.

**Chapter 3: Representation and Numbers**
How computers encode information: text as numbers, images as grids, sound as waveforms. Why encoding choices matter. The reduction of everything to mathematical representation—and what might be lost in translation.

**Chapter 4: Functions and Optimization**
The mathematical idea of a function: inputs mapped to outputs. What it means to "optimize" a function—to find parameters that make it behave as desired. The conceptual foundation for all machine learning.

### Part II: Learning from Data

**Chapter 5: What Is Learning?**
The core insight of machine learning: instead of programming rules, let the system discover patterns from examples. Training vs. inference. The problem of generalization—performing well on data you haven't seen.

**Chapter 6: The Simplest Learner**
Linear regression as the minimal case: a line that fits data points. Loss functions (measuring error), gradient descent (improving iteratively). The "chef tasting soup" metaphor grounded in simple math.

**Chapter 7: When Lines Aren't Enough**
Why linear models fail for complex problems. The need for nonlinearity. Decision boundaries and the intuition behind more expressive functions.

**Chapter 8: Neural Networks**
Layers of simple computations composed into complex functions. The "universal approximator" theorem. Backpropagation as credit assignment: which parameters caused the error? Training deep networks at scale.

### Part III: Learning Language

**Chapter 9: How a Computer Sees Text**
The problem of turning words into numbers. Tokenization and byte-pair encoding (BPE). Why "or" becomes a single token. The shift from symbols to geometry.

**Chapter 10: Embedding: Words as Locations**
Vector spaces and learned representations. Why similar words end up near each other. The "meaning map" metaphor—and its limits.

**Chapter 11: The Three Acts**
Embedding, transforming, and unembedding as the core architecture of language models. Symbols become geometry, geometry interacts, geometry becomes symbols again. The full pipeline from input to output.

**Chapter 12: Attention and Context**
The "flashlight" mechanism: how transformers decide which tokens matter for which other tokens. Self-attention, multi-head attention, and the learned nature of attention patterns. Why transformers changed everything.

**Chapter 13: Training at Scale**
Next-token prediction as the training objective. Massive datasets, massive compute, emergent capabilities. The "bitter lesson"—that scale often beats cleverness. What the model learns by predicting words.

### Part IV: From Prediction to Behavior

**Chapter 14: What the Model Learns (and Doesn't)**
Emergent capabilities: in-context learning, chain-of-thought reasoning, apparent common sense. But also: failures of logical inference, inconsistency, hallucination. The gap between correlation and understanding. Introduction of AI Dunning-Kruger (AIDK): the structural condition where systems produce uniformly confident outputs regardless of reliability, cannot detect their own competence boundaries, and cannot self-correct through encounter with reality. Unlike human overconfidence, AIDK is architectural, not developmental—permanent, not correctable.

**Chapter 15: RLHF and Alignment**
Shaping model behavior through human feedback. Reward models, policy optimization, the "comedian and audience" metaphor. Why RLHF changes tone and safety more than knowledge. The alignment problem in miniature.

**Chapter 16: The Epistemics of AI Output**
Why confidence isn't reliability. Hallucination as a structural feature, not a bug. Introduction of the Interactive Dunning-Kruger Effect (IDKE): what happens when AIDK meets human epistemic limitations—confidence transfers from machine to human, untethered from warrant. The people most vulnerable to overconfidence are most amplified by AI interaction. The Human-Curated, AI-Enabled (HCAE) framework as response: stratifying AI deployment by the epistemic authority of the human validator. Four tiers—User, Professional, Expert, Synthesis—with safety scaling by authority, not model capability. Practical wisdom for epistemic hygiene: when to rely on AI, when to verify, when to reject.

### Part V: Philosophical Reckoning

**Chapter 17: Syntax All the Way Up?**
Revisiting the Chinese Room. Searle's argument and its critics. The symbol grounding problem: can syntax ever constitute semantics? Does scale change the question, or merely obscure it?

**Chapter 18: Intelligence Without Understanding**
What large language models reveal about the nature of knowledge and reasoning. The dissociation of competence from comprehension. Statistical regularities vs. truth-tracking. Can a system "know" things it doesn't understand?

**Chapter 19: The Image of God and the Image of Intelligence**
A distinctly Christian reckoning. The Logos as the ground of meaning, rationality, and truth. The imago Dei as the foundation of human cognition—reasoning that participates in divine Reason. Why AIDK is permanent: the system lacks not just access to reality but the soul that knows. The ontological gap beneath the architectural gap. HCAE as stewardship: placing humans with appropriate epistemic authority in the loop as responsible use of powerful tools. What it means that we can build systems that mimic cognition but lack the soul that knows. Implications for anthropology, ethics, and discipleship in an age of artificial intelligence.

---

## Format and Features

**Length:** Approximately 75,000–85,000 words (19 chapters averaging 4,000 words each, plus front and back matter)

**Two-Register Structure:** Each chapter uses "Story Time" (accessible narrative with concrete metaphors) followed by "Technical Time" (precise explanation with optional mathematical detail). Readers can engage at either level.

**Figures:** Each chapter includes 2–4 explanatory figures designed to carry conceptual weight, not merely decorate. Diagrams of architectures, visualizations of embedding spaces, flowcharts of training loops, attention heatmaps.

**"What Gets Lost" Sections:** Each Part concludes with a section addressing limitations, failure modes, and open questions—maintaining epistemic honesty throughout.

**Discussion Questions:** Each chapter ends with questions suitable for small group study, adult education, or classroom use.

**Glossary:** Technical terms defined accessibly, cross-referenced to chapters where they're introduced.

---

## Author Platform

**Professional Credibility:** 30+ years in systems architecture across commercial and aerospace-defense sectors. Current role as Chief Architect for Digital Ecosystems at Northrop Grumman provides direct engagement with enterprise AI implementation. Pursuing MS in Applied AI ensures current technical knowledge.

**Ministry Platform:** Ordained minister with active apologetics work through the oddXian platform. Experience communicating complex ideas to lay audiences in church and parachurch contexts.

**Writing Sample:** Two completed chapters ("How a Computer Learns Words" and "The Three Acts of a Language Model") are available demonstrating the two-register approach and intended tone.

**Audience Access:** Professional network spans technical practitioners and Christian ministry leaders. Existing content platforms (LinkedIn, oddXian) provide launch channels.

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
