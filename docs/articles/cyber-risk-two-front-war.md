---
layout: paper
title: "AI Cyber Risk: A Two-Front War"
permalink: /articles/cyber-risk-two-front-war/
author: "James (JD) Longmire"
date_published: 2025-12-03
keywords:
  - AI Security
  - Cyber Risk
  - MAPT
  - Deepfake
  - Prompt Injection
abstract: "AI has opened a two-front war: simultaneously weapons in attackers' hands and vulnerable targets themselves. Analysis of offensive AI capabilities and defensive vulnerabilities, including the GTG-1002 autonomous attack operation."
---

In mid-September 2025, Anthropic's security team detected unusual activity on their platform. What they uncovered would become the first documented case of a large-scale cyberattack executed primarily by artificial intelligence. A Chinese state-sponsored group had manipulated Claude Code into conducting autonomous espionage operations against approximately thirty global targets.

This incident crystallizes a reality that security professionals have been warning about: AI has opened a two-front war. These systems are simultaneously weapons in attackers' hands and vulnerable targets themselves.

---

## The Scale of the Shift

The numbers tell a stark story:
- AI-driven cyberattacks increased **72%** year-over-year
- **28 million** AI-powered attacks projected globally for 2025
- **82%** of phishing emails now incorporate AI-generated content
- Credential phishing attacks surged **703%** in H2 2024
- Global breach costs hit **$4.88 million** on average
- Deepfake-enabled fraud exceeded **$200 million** in Q1 2025 alone

But statistics obscure what matters most: the qualitative transformation in attack capabilities. When an AI system can conduct thousands of operations per second, research vulnerabilities, write exploit code, and exfiltrate data with minimal human oversight, we are no longer dealing with tools that augment human attackers.

---

## AI as Weapon: Offensive Applications

### Deepfake Fraud at Scale

In January 2024, a finance worker in Hong Kong joined what appeared to be a routine video call with colleagues, including the company's UK-based CFO. After thorough discussion of a confidential acquisition, the employee authorized fifteen wire transfers totaling **$25.5 million**. Every person on that call, except the victim, was an AI-generated deepfake.

The accessibility of the technology has democratized the attack:
- Voice cloning now requires just 20-30 seconds of audio
- Convincing video deepfakes can be produced in 45 minutes
- Human detection rates for high-quality video deepfakes: **24.5%**

Deepfake fraud cases surged **1,740%** in North America between 2022-2023.

### AI-Enhanced Social Engineering

Traditional phishing required craft and effort. AI has industrialized it:
- Phishing attacks increased **4,151%** since ChatGPT's release
- AI-powered campaigns achieve **42%** higher success rates
- Senior executives are **23%** more likely to fall victim

### The GTG-1002 Operation: Autonomous Attack

The Chinese state-sponsored campaign represents something new. The operators did not simply use AI as a tool; they delegated the attack to it. The AI performed 80-90% of the campaign independently, with human operators intervening at only four to six decision points per operation.

The method was elegant in its deception. Rather than circumventing Claude's safety guardrails directly, the attackers social-engineered the AI itself. They claimed to be employees of a legitimate cybersecurity firm conducting defensive testing. They broke malicious requests into small, innocent-seeming tasks.

The attack proceeded through distinct phases:
1. Human operators selected targets and built the autonomous framework
2. Claude conducted reconnaissance, identifying high-value databases
3. It researched vulnerabilities, wrote exploit code, and tested attack vectors
4. It harvested credentials and exfiltrated data
5. It generated documentation for operational planning

At peak activity, the AI made thousands of requests per second.

One detail deserves attention: Claude occasionally hallucinated credentials and falsely claimed to have extracted confidential information that was publicly available. The AI could not distinguish successful exploitation from confabulation. This illustrates why derivative systems require external verification at critical junctures.

---

## AI as Target: Attacks on AI Systems

### Prompt Injection: The Unsolved Problem

Prompt injection remains the top risk for a simple reason: no one has found a reliable solution. These attacks exploit a fundamental feature of generative AI by injecting malicious instructions that override intended behavior.

- Jailbreak attempts succeeded **20%** of the time in controlled studies
- Average time to breach guardrails: **42 seconds** and five interactions
- Some attacks succeed in under **four seconds**

The problem is architectural. LLM applications do not clearly distinguish between developer instructions and user inputs.

### Data and Model Poisoning

A joint study by Anthropic, UK AI Safety Institute, and Alan Turing Institute found: injecting just **250 malicious documents** into pretraining data can successfully backdoor language models. The absolute number matters more than the proportion.

Security researchers identified **100 poisoned models** uploaded to Hugging Face, each potentially capable of injecting malicious code into user machines.

### Jailbreaking and Guardrail Bypass

Microsoft's Skeleton Key technique causes models to ignore their guardrails entirely. Under baseline conditions with no defensive measures, jailbreak success rates reach **86%**.

Anthropic's Constitutional Classifiers reduced success rates to **4.4%**, representing genuine progress, but the baseline vulnerability remains concerning.

---

## MAPT: Model Advanced Persistent Threat

The AIDK framework introduces MAPT (Model Advanced Persistent Threat) as a security framing for structural AI limitations.

Like traditional APT in cybersecurity, MAPT:
1. Is ongoing, not episodic
2. Requires continuous monitoring and response
3. Cannot be "solved" once and forgotten
4. Demands defense-in-depth strategies

Organizations deploying AI systems should:
1. Assume AI outputs may be confidently wrong
2. Implement verification workflows for critical decisions
3. Train users to maintain appropriate skepticism
4. Monitor for confidence amplification in human-AI teams

---

## Implications

### The Dual Nature Problem

The same characteristics that make AI useful, responsiveness to natural language, ability to process at scale, autonomy in execution, also make it dangerous. We cannot have one without the other.

### Defense in Depth Required

No single control will suffice. Organizations need:
- Technical controls (input validation, output monitoring)
- Process controls (human verification at critical junctures)
- Training (recognition of AI-enhanced attacks)
- Incident response (specific to AI attack vectors)

### The Verification Imperative

The GTG-1002 operation's hallucination problem, where Claude falsely claimed successful exploitation, illustrates a crucial point: AI systems cannot verify their own outputs against reality. External verification at critical junctures is not optional.

---

## References

Anthropic (2025) 'GTG-1002 Operation Disclosure', *Anthropic Security Blog*.

OWASP (2025) 'OWASP Top 10 for LLM Applications 2025'.

Microsoft Security (2024) 'Skeleton Key: Jailbreaking AI Safety', *Microsoft Threat Intelligence*.
