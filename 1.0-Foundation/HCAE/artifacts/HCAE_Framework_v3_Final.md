# Human-Curated, AI-Enabled: A Framework for Reliable AI Deployment

**Author:** James (JD) Longmire  
**Affiliation:** Northrop Grumman Fellow (unaffiliated research)  
**ORCID:** 0009-0009-1383-7698  
**Correspondence:** jdlongmire@outlook.com

*Developed under the ECAE (Expert-Curated, AI-Enabled) model described in this framework, with derivational contributions from Claude. Origination, judgment, and final authority on truth and validity remain with the human author.*

---

## Abstract

Enterprise AI projects fail at rates between 70% and 95%. The dominant response—more data, larger models, better retrieval—addresses the wrong problem. These are grounding-axis failures misdiagnosed as infrastructure problems. AI systems lack access to the purposes they serve and the wholes their outputs enter. Scaling cannot fix what scaling did not break.

The Human-Curated, AI-Enabled (HCAE) framework provides a design discipline for reliable deployment. Four tiers supply the grounding AI structurally lacks: User-Curated (UCAE) for low-stakes ideation, Professional-Curated (PCAE) for routine domain work, Expert-Curated (ECAE) for high-stakes analysis, and Synthesis-Curated (SCAE) for formally verifiable domains. The framework is a decision tool, not a maturity model; the goal is matching tier to task, not maximizing tier. Building on the AI Dunning-Kruger (AIDK) framework, this paper operationalizes structural epistemic limitations into deployment guidance, addressing hybrid deployments, tier transitions, and the three-axis model explaining why horizontal and vertical solutions alone cannot resolve reliability problems.

*Keywords: artificial intelligence, large language models, deployment architecture, AI governance, HCAE framework, formal verification, epistemic grounding, enterprise AI*

---

## 1. Introduction

The promise of enterprise AI has not matched the reality. Organizations invest billions in generative AI initiatives. The vast majority fail to deliver measurable value.

MIT's Project NANDA reports that 95% of enterprise AI pilots produce no measurable P&L impact (MIT Project NANDA, 2025). Gartner predicts that 30% of generative AI projects will be abandoned after proof of concept by the end of 2025, with over 40% of agentic AI projects canceled by 2027 due to escalating costs, unclear business value, or inadequate risk controls (Gartner, 2024, 2025). These are not isolated findings. Multiple independent sources consistently report failure rates between 70% and 95% across enterprise AI initiatives.

The standard diagnosis points to execution failures: poor data quality, mismatched expectations, governance gaps, insufficient training. The standard prescription follows: fix the data, manage expectations, strengthen governance, train users. These interventions operate on what this paper calls the horizontal axis. They concern getting the right information to the right place efficiently. They are legitimate engineering work. They are also insufficient.

This paper proposes an alternative diagnosis. Enterprise AI fails because organizations face grounding-axis problems and respond with horizontal-axis solutions. AI systems lack access to the purposes they serve (teleological blindness) and the wholes their outputs enter (mereological blindness). No amount of data, compute, or architectural refinement addresses this structural deficit. The solution space and the problem space do not intersect.

The Human-Curated, AI-Enabled (HCAE) framework provides a design discipline for addressing grounding-axis problems. It specifies deployment architectures that supply the grounding AI systems structurally lack, matching the level of human epistemic authority to the demands of the task.

**The framework is a decision tool, not a maturity model.** Higher tiers are not universally better. They are appropriate for different task profiles. The goal is matching deployment architecture to task requirements, not maximizing tier. UCAE is the right answer for brainstorming. PCAE is the right answer for routine professional work with genuine review. ECAE is the right answer for high-stakes analysis where formal specification is unavailable. SCAE is the right answer for formalizable domains where correctness is non-negotiable. Attempting the wrong tier for a given task produces either waste (over-deployment) or failure (under-deployment).

The paper proceeds as follows. Section 2 establishes the theoretical foundations: the structural inevitability of hallucination, the incentive structures that perpetuate it, and the AIDK/IDKE constructs that explain how AI limitations interact with human limitations. Section 3 develops the four-tier HCAE framework, including hybrid deployments and tier transitions. Section 4 examines SCAE as the emerging frontier for high-assurance AI, including strengthening mechanisms for ECAE when SCAE is unavailable and worked examples of SCAE in practice. Section 5 integrates the framework with the three-axis model that explains why horizontal and vertical solutions alone are insufficient. Section 6 addresses the matching problem: how to select the appropriate tier for a given deployment. Section 7 discusses economic and regulatory implications. Section 8 concludes.

---

## 2. Theoretical Foundations

### 2.1 The Structural Inevitability of Hallucination

Large language models hallucinate. They produce confident, fluent, false outputs. This is not a bug awaiting correction but a structural feature of the architecture.

Xu, Jain, and Kankanhalli (2024) prove this formally. Using computability theory, they demonstrate that hallucination is inevitable for any computable LLM used as a general problem solver. The diagonalization argument establishes a lower bound: for any LLM, there exist queries on which it must either hallucinate or refuse to answer. This is not a limitation of current models awaiting architectural innovation. It is a mathematical constraint on the class of systems.

Banerjee, Agarwal, and Singla (2024) extend this analysis using Gödel's incompleteness theorem and undecidability arguments. They demonstrate that LLMs face fundamental trade-offs among truthfulness, information conservation, knowledge revelation, and coherence. No training regime, however sophisticated, can eliminate hallucination without sacrificing other desiderata. The authors' conclusion is stark: we must learn to live with hallucination rather than expecting to eliminate it.

These proofs establish that hallucination is not a temporary deficiency but a permanent feature. Scaling does not resolve it. Better data does not resolve it. Architectural refinement may reduce hallucination rates in specific domains but cannot eliminate the structural vulnerability. Any deployment strategy that assumes hallucination will be solved is building on false premises.

### 2.2 Incentive-Driven Persistence

Beyond structural inevitability, current training regimes actively incentivize hallucination.

Kalai, Nachum, Vempala, and Zhang (2025) analyze why language models hallucinate from an incentive perspective. Next-token prediction rewards fluent continuation regardless of truth value. Accuracy-only evaluations reward guessing over hedging. Reinforcement learning from human feedback (RLHF) amplifies fluency because human evaluators reward confident, well-structured responses even when those responses are wrong.

The training signal says: produce outputs that sound knowledgeable. The training signal does not say: produce outputs that are true. When these objectives conflict, the system optimizes for the former. A system trained to sound knowledgeable will, when it lacks knowledge, produce outputs that sound knowledgeable anyway. This is not malfunction. This is the system doing what it was trained to do.

The implication for deployment is direct. We cannot rely on the system to signal its own uncertainty accurately. Confidence is a learned behavior pattern, not a reliability indicator. Fluent outputs may be correct or incorrect with equal probability from the system's perspective. External verification is not optional. It is the only mechanism for distinguishing reliable from unreliable outputs.

### 2.3 The AI Dunning-Kruger Effect

The structural epistemic limitations of large language models have been formalized as the AI Dunning-Kruger effect (AIDK) in prior work (Longmire, 2026a).

AIDK is the condition in which AI systems produce outputs with uniform confidence regardless of actual reliability, lack mechanisms for detecting their own competence boundaries, and cannot self-correct through encounter with reality. Unlike human Dunning-Kruger effects, which are developmental and correctable through feedback, AIDK is architectural and permanent. The system has no access to truth conditions against which to calibrate.

The critical distinction is trajectory. Human overconfidence is a stage in a developmental process that reality can correct. The novice encounters failure, receives feedback, revises beliefs, and gradually calibrates confidence toward warrant. AI overconfidence is a permanent condition arising from categorical separation from reality. The model operates entirely within a derived symbolic space with no feedback loop to the world itself.

Calibration studies confirm this pattern. Kadavath et al. (2022) found that language models can be calibrated on multiple-choice tasks but this calibration does not transfer reliably to open-ended generation. The system expresses high confidence on queries it answers incorrectly at rates indistinguishable from queries it answers correctly. Confidence is not a reliability signal.

### 2.4 The Interactive Dunning-Kruger Effect

AIDK does not exist in isolation. When AI systems with structural epistemic limitations interact with humans who have their own epistemic limitations, an emergent phenomenon arises: the Interactive Dunning-Kruger Effect (IDKE) (Longmire, 2026a).

IDKE is the amplification of human epistemic overconfidence through interaction with AI systems that cannot assess their own reliability, resulting in confidence inflation untethered from warrant in both parties to the interaction.

The mechanism operates through a predictable sequence. A user with limited domain expertise consults an AI system exhibiting AIDK. The AI produces confident-sounding output. The user cannot evaluate correctness. The AI cannot signal unreliability. The user's confidence increases without warrant. The user now holds and acts on ungrounded confidence.

Research on AI-assisted decision-making documents this pattern. Buçinca, Malaya, and Gajos (2021) found that people overrely on AI suggestions even when those suggestions are wrong, and that explanations do not reduce this overreliance and may increase it. Dell'Acqua et al. (2023) demonstrated a "jagged technological frontier" where AI creates a 19 percentage point performance drop when used outside its capability boundary. Consultants who blindly adopted AI output performed worse than those who maintained critical distance.

IDKE magnitude scales inversely with user expertise. Users with high domain expertise catch errors; AIDK effects are bounded by their judgment. Users with low domain expertise cannot evaluate outputs; AIDK fills the epistemic void and amplification is maximal. The people most vulnerable to epistemic overconfidence are most amplified by AI interaction.

The effect is invisible while occurring. Neither participant can detect IDKE in real time. The user does not know they do not know. The AI does not know it does not know. The confidence persists beyond the interaction and propagates into subsequent decisions.

### 2.5 From Diagnosis to Design

The AIDK framework establishes the structural diagnosis. The question for deployment is: what follows?

If AIDK is architectural rather than contingent, scaling cannot resolve it. If IDKE emerges from the interaction of AI and human limitations, deployment architecture must address both sides. If confidence transfer is invisible to participants, external structure must compensate for what internal awareness cannot provide.

The Human-Curated, AI-Enabled (HCAE) framework operationalizes these implications. It specifies deployment architectures that supply the epistemic grounding AI systems structurally lack, matching the level of human epistemic authority to the demands of the task.

The framework does not depend on AIDK and IDKE being precisely correct in every detail. It rests on the more basic claim that AI systems lack epistemic grounding and that human judgment must supply it. AIDK and IDKE elaborate why this matters and predict how failures manifest. If the constructs require revision in light of empirical findings, the framework's core logic remains intact.

---

## 3. The HCAE Framework

The Human-Curated, AI-Enabled (HCAE) framework stratifies AI deployment by the epistemic authority responsible for validating outputs. It rejects the undifferentiated notion of "human-in-the-loop" by recognizing that not all humans are capable of evaluating truth claims in all domains. The framework specifies who supplies grounding, what form that grounding takes, and how grounding adequacy must match task requirements.

### 3.1 User-Curated, AI-Enabled (UCAE)

At the UCAE tier, the end user provides prompts and consumes outputs without possessing the domain expertise required to independently assess correctness. Validation is intuitive or stylistic rather than truth-directed.

**Appropriate use cases:** Low-stakes drafting, brainstorming, ideation, creative exploration, entertainment. Contexts where stimulation matters more than correctness and where outputs will be revised before consequential use.

**Primary risk:** Confidence laundering. The user inherits the system's groundless confidence and treats AI-generated claims as their own without independent evaluation. IDKE effects are maximal at this tier.

**Grounding mechanism:** None. The user cannot supply epistemic grounding because they lack the expertise to evaluate outputs. UCAE works when grounding is unnecessary. It fails when grounding is required but absent.

### 3.2 Professional-Curated, AI-Enabled (PCAE)

At the PCAE tier, a trained professional reviews AI output within their field. The professional has domain training and institutional context but operates under time, scope, or capacity constraints that limit verification depth.

**Appropriate use cases:** Routine professional work where plausibility checks are possible. Legal research for established precedents. Medical documentation for common presentations. Financial analysis using standard methods. Technical documentation within familiar domains.

**Primary risk:** Silent edge-case failure. The professional can verify that outputs fall within normal parameters but may miss subtle errors, novel failure modes, or edge cases that require deeper expertise. Verification becomes pattern-matching rather than genuine evaluation.

**Grounding mechanism:** Professional norms and training. The professional knows what the output is for, what adequate work product looks like, and how this output fits the larger engagement. This provides weak but real teleological and mereological grounding.

### 3.3 Expert-Curated, AI-Enabled (ECAE)

At the ECAE tier, a domain expert with the capacity to independently evaluate truth conditions curates AI output. The expert can assess not only plausibility but correctness, not only format but substance.

**Appropriate use cases:** High-stakes analysis where formal specification is unavailable or impractical. Novel clinical presentations. Complex litigation strategy. Strategic planning under uncertainty. Contested interpretations requiring judgment.

**Primary risk:** Over-delegation. The expert's presence provides assurance, but that assurance depends on continued engagement. If the expert begins to rubber-stamp outputs, treating AI generation as presumptively correct, ECAE degrades to PCAE or worse. Fatigue, time pressure, and repeated exposure to acceptable outputs erode vigilance.

**Grounding mechanism:** Expert judgment. The expert has deep teleological understanding of what "good" means in this domain and rich mereological awareness of how outputs connect to the field, what they presuppose, and what they enable. This provides strong but not mechanical grounding.

### 3.4 Synthesis-Curated, AI-Enabled (SCAE)

At the SCAE tier, expert judgment is combined with a formal validation system such as a proof assistant, compiler, test harness, or regulatory verification engine. AI proposes candidate solutions; validation systems enforce non-negotiable constraints. Trust is replaced by proof within the scope of formal coverage.

**Appropriate use cases:** Mathematical proof with formal verification. Safety-critical code with static analysis and theorem proving. Regulatory compliance with codified rules. Domains where correctness is binary, formalizable, and mechanically checkable.

**Primary risk:** Over-formalization and scope confusion. Formal verification provides guarantees only within its coverage. Treating formally verified components as globally reliable when they address only part of the problem produces false confidence. The boundary between covered and uncovered territory must be explicit.

**Grounding mechanism:** Formal specification plus expert synthesis. The formal system encodes teleological constraints (what counts as valid) and enforces them mechanically. The expert supplies what formalization cannot: judgment about whether the specification captures the intent, whether the scope is adequate, and what lies beyond formal coverage.

### 3.5 The Tier Hierarchy

The tiers form a hierarchy of epistemic assurance:

| Tier | Validator | Grounding | Assurance Level |
|------|-----------|-----------|-----------------|
| UCAE | End User | None | Minimal |
| PCAE | Professional | Professional norms | Moderate |
| ECAE | Expert | Expert judgment | High |
| SCAE | Expert + Formal System | Mechanical verification | Highest (within scope) |

Each tier addresses AIDK and IDKE differently. UCAE provides no mitigation; confidence laundering is expected. PCAE provides partial mitigation through professional training. ECAE provides strong mitigation through expert judgment. SCAE provides mechanical mitigation within formal coverage by removing reliance on the system's confidence entirely.

### 3.6 Tier-Task Matching

The central deployment question is: what tier does this task require?

Matching criteria include:

**Consequence severity.** What happens if the output is wrong? Low-stakes tasks tolerate lower tiers. High-stakes tasks demand higher tiers.

**Verifiability.** Can correctness be assessed, and by whom? Tasks where correctness is observable can tolerate lower tiers than tasks where errors remain hidden.

**Expertise availability.** Do qualified validators exist and are they available? Tier requirements must be achievable, not aspirational. Requiring ECAE when no experts are available produces either process theater or deployment failure.

**Formal specifiability.** Can correctness be expressed in terms a verification system can check? SCAE requires affirmative answer; ECAE is the ceiling otherwise.

**Domain change rate.** How quickly does the domain evolve? Rapidly changing domains may resist formal coverage even where specification is theoretically possible.

Mismatch in either direction causes problems. Under-deployment (low tier for high-demand task) produces the failures that dominate enterprise AI statistics. Over-deployment (high tier for low-demand task) wastes expert capacity and slows iteration without corresponding benefit.

### 3.7 Hybrid Deployments and Tier Transitions

The four HCAE tiers describe ideal types. Actual deployments rarely operate at a single tier throughout their lifecycle. A legal research tool might handle routine case law retrieval at PCAE while escalating novel constitutional questions to ECAE. A clinical decision support system might operate at PCAE for common presentations while flagging rare symptom clusters for specialist review. The framework must accommodate this reality without collapsing into "it depends."

#### 3.7.1 The Escalation Principle

Tier selection is not a property of the system but of the query-context pair. The same AI system may appropriately serve different tiers for different queries. The governing principle: **epistemic authority must match epistemic demand**.

A query's epistemic demand is determined by consequence severity, verification difficulty, and domain coverage in training data. When demand exceeds the epistemic authority available at the current tier, escalation is required. When demand falls within current-tier capacity, escalation wastes resources.

This principle has a corollary: **systems should be designed for their highest anticipated tier, with lower tiers as constrained operating modes**. A system designed for UCAE cannot escalate to ECAE because it lacks the verification infrastructure. A system designed for ECAE can operate in PCAE mode for routine queries while retaining escalation capacity.

#### 3.7.2 Escalation Triggers

Five categories of signals should trigger upward escalation:

**Consequence signals.** The downstream use of the output increases in stakes. A draft becomes a filing. A suggestion becomes a prescription. A recommendation becomes a commitment. When the same output moves from low-consequence to high-consequence use, the tier must rise to match.

**Novelty signals.** The query falls outside well-represented training territory. Novel fact patterns, emerging domains, recent developments not yet absorbed into training data, edge cases at the boundaries of established categories. Novelty increases hallucination risk and demands higher epistemic authority for validation.

**Conflict signals.** The system produces outputs that conflict with prior outputs, with external sources, or with user-supplied constraints. Internal inconsistency is a reliability flag. The system cannot adjudicate its own conflicts; escalation to human judgment is required.

**Uncertainty signals.** The system expresses uncertainty, hedges extensively, or produces outputs with low confidence scores (where such scores are available and calibrated). Genuine uncertainty expression should trigger verification, not dismissal.

**Domain boundary signals.** The query crosses into adjacent domains where the validating human lacks expertise. A legal professional reviewing AI output on a tax question that implicates medical issues cannot provide PCAE assurance for the medical component. Cross-domain queries require either multi-expert review or escalation to a generalist with broader competence.

#### 3.7.3 Escalation Protocols

Escalation is not merely "ask someone more senior." It requires structured handoff:

**Context preservation.** The escalated query must carry its history: what was asked, what the system produced, why escalation was triggered, what verification has already occurred. Escalation without context forces the higher-tier validator to repeat work or miss relevant information.

**Authority confirmation.** The receiving tier must confirm that appropriate epistemic authority is actually present. Escalating from PCAE to ECAE requires confirming that a genuine domain expert (not merely a more senior professional) receives the query. Title is not expertise.

**Scope specification.** Escalation should specify what requires higher-tier validation. "Review this entire output" is less useful than "verify the causation analysis in paragraph three, which relies on a novel application of precedent X." Targeted escalation focuses expert attention where it is needed.

**Resolution documentation.** The outcome of escalated review should be documented: what was verified, what was corrected, what remains uncertain. This documentation serves both immediate quality assurance and longer-term system improvement.

#### 3.7.4 De-escalation Criteria

Not all queries require the highest available tier. De-escalation from ECAE to PCAE, or from PCAE to UCAE, is appropriate when:

**The query class has been validated.** Repeated queries of the same type, verified at higher tiers without significant correction, may be safely handled at lower tiers. This is earned trust, not default trust. The earning requires documented verification history.

**Consequences are bounded.** The output will receive additional review before consequential use. A draft that will be revised by a human expert before submission can be generated at a lower tier than a document that will be used as-is.

**Recovery is available.** Errors can be detected and corrected before harm occurs. Lower tiers are more acceptable when feedback loops exist to catch failures.

De-escalation should be explicit and justified, not implicit and convenient. The temptation to de-escalate for efficiency must be resisted when epistemic demand remains high.

#### 3.7.5 Organizational Implementation

Hybrid deployment requires organizational infrastructure:

**Escalation pathways.** Clear routing for queries that trigger escalation signals. Who receives escalated queries? How quickly? With what authority to act?

**Tier certification.** Documented assessment of which personnel can validate at which tiers. Not all professionals provide PCAE assurance; not all credentialed experts provide ECAE assurance. Validation capacity is individual, not categorical.

**Monitoring and audit.** Tracking of escalation patterns, resolution outcomes, and tier-match accuracy over time. Systematic under-escalation (high-demand queries handled at low tiers) indicates process failure. Systematic over-escalation (routine queries consuming expert capacity) indicates inefficiency.

**Feedback integration.** Escalation outcomes should inform system improvement. Patterns in what gets escalated and what gets corrected reveal coverage gaps, calibration failures, and domain boundaries that the system handles poorly.

### 3.8 The Framework as Decision Tool

The tiers are options to select among, not rungs to climb. Each serves a purpose; none is universally superior.

UCAE is the right answer for brainstorming, early-stage ideation, and low-stakes drafting. Deploying ECAE for tasks that need only stimulation wastes expert capacity and slows iteration. Match tier to task, not task to aspiration.

PCAE is the right answer for routine professional work where review is genuine and consequences are bounded. Most professional AI deployment should live here. The failure mode is not "should have used ECAE" but "review became perfunctory" or "consequences were higher than recognized."

ECAE is the right answer for high-stakes analysis where formal specification is unavailable or impractical. Strategic judgment, complex negotiations, novel clinical presentations, contested interpretations: these require expert grounding that cannot be mechanized. Strengthened ECAE (ensemble review, adversarial testing, structured protocols) extends assurance within this tier rather than reaching for SCAE that is not available.

SCAE is the right answer for formalizable domains where correctness is non-negotiable. Mathematical proof, safety-critical systems, regulatory compliance with codified rules. Attempting SCAE where formal specification is intractable produces either failure (the domain resists formalization) or false confidence (partial formalization mistaken for complete coverage).

The framework succeeds when organizations can answer: "What tier does this task require, and do we have the infrastructure and expertise to deploy at that tier?" The framework fails if it becomes a compliance checklist divorced from the matching logic that justifies it.

**Selection, not aspiration.** The question is not "how do we get to SCAE?" but "what tier fits this task?" For most tasks, the answer is not SCAE. For many tasks, PCAE with genuine review provides adequate assurance at sustainable cost. The framework's value lies in making the selection explicit and justified rather than implicit and accidental.

---

## 4. SCAE as the Emerging Frontier

The Synthesis-Curated tier represents the highest epistemic assurance currently achievable for AI-assisted work. It combines the generative capacity of AI systems with the mechanical verification of formal systems. This section examines what SCAE requires, how to strengthen ECAE when SCAE is unavailable, and how SCAE operates in practice.

### 4.1 The SCAE Architecture

SCAE deployment follows a consistent pattern regardless of domain:

1. **Human formalization.** Experts translate requirements, specifications, or conjectures from natural language into formal representations that verification systems can process. This step requires deep domain expertise and formal methods training. It cannot be automated because formalization requires understanding what the problem means, not merely what the symbols say.

2. **AI-guided search.** The AI system generates candidate solutions, explores the space of possibilities, proposes approaches, and produces outputs that might satisfy the formal constraints. The AI operates as a powerful search engine over the solution space, guided by patterns learned from training data.

3. **Mechanical verification.** A formal system (proof assistant, static analyzer, test harness, regulatory engine) checks whether the candidate solution satisfies the specified constraints. This check is syntactic and mechanical. The verifier does not understand the solution; it verifies that the formal derivation is valid according to the rules of the system.

4. **Expert interpretation.** Experts review verified solutions for significance, completeness, and faithfulness to intent. A solution can be formally valid but practically useless, or valid but relying on assumptions that should be scrutinized. The expert validates that the formalization captured the original problem.

The architecture places humans at both ends of the pipeline. AI operates in the middle, amplifying search capacity under formal constraint. The guarantee emerges from the combination: within the scope of formal specification, verified outputs are correct. Not probably correct. Correct.

### 4.2 SCAE Requirements

SCAE is not universally applicable. It requires:

**Formal specifiability.** Correctness criteria must be expressible in a language that verification tools accept. Domains with clear, rule-governed correctness (mathematics, logic, type-safe programming, regulatory compliance with codified rules) are SCAE-ready. Domains where correctness depends on tacit judgment, aesthetic evaluation, or contested values are not.

**Tool maturity.** Verification tools must exist for the domain and be capable of handling realistic problems. Tool limitations constrain what can be verified in practice.

**Expert availability.** People must exist who can both understand the domain and perform formal specification. This combination is rare. Domain experts often lack formal methods training. Formal methods experts often lack domain depth.

**Economic justification.** The cost of SCAE must be warranted by the stakes. Formal specification is expensive. Verification infrastructure requires investment. For low-stakes applications, strengthened ECAE may provide sufficient assurance at lower cost.

Where these criteria are met, SCAE represents the highest available epistemic assurance. Where they are not met, ECAE remains the ceiling.

### 4.3 Current SCAE Domains

Several domains have achieved mature SCAE implementations:

**Mathematical proof.** Proof assistants like Lean, Coq, and Isabelle provide mechanical verification of mathematical derivations. AlphaProof (Hubert et al., 2025) demonstrated AI-assisted mathematical reasoning with formal verification, achieving silver-medal performance at the 2024 International Mathematical Olympiad by solving problems that stymied human competitors under time constraints. The AI proposes proof strategies; Lean verifies validity; mathematicians formalize conjectures and interpret results.

**Safety-critical systems.** DO-178C (avionics) and ISO 26262 (automotive) recognize formal methods for compliance demonstration. Static analysis tools like Frama-C and SPARK verify that code satisfies formal specifications. AI can generate candidate implementations; formal tools verify safety properties; engineers specify requirements and interpret verification results.

**Hardware verification.** Chip design increasingly relies on formal verification to ensure correctness before fabrication. Tools verify that implementations match specifications. AI can assist in generating test cases and exploring the verification space.

**Regulatory compliance.** Tax codes, financial regulations, and legal requirements that admit formal encoding can be verified mechanically. AI can generate candidate compliance strategies; rule engines verify consistency with encoded requirements.

These domains share common features: correctness is binary, formalizable, and mechanically checkable. Domains lacking these features cannot support SCAE regardless of AI capability.

### 4.4 SCAE Limitations

Even mature SCAE implementations have boundaries:

**Formalization bottleneck.** Human expert time is the constraint. Formalizing problems is slow, skilled work. The AI can search faster than humans, but humans must still prepare the search targets and interpret results.

**Scope boundaries.** Verification covers only what is specified. Properties not formalized receive no assurance. Completeness of specification is a human judgment that verification cannot check.

**Tool trust.** Verification toolchains could contain bugs. Defense in depth requires tool qualification, independent verification, and conservative interpretation of tool outputs.

**Partial coverage.** In practice, not all components can be formally verified. Organizations prioritize verification for the most critical components and rely on traditional assurance methods for the rest.

SCAE provides mechanical guarantees within scope. Beyond scope, SCAE provides nothing. The boundary must be explicit.

### 4.5 ECAE as Ceiling: High-Stakes Domains Without Formal Specification

SCAE represents the highest epistemic assurance the HCAE framework can provide. But SCAE requires formal specifiability. Correctness must be expressible in terms a verification engine can check. Many high-stakes domains lack this property.

Strategic military planning involves judgment under uncertainty with incomplete information, adversarial adaptation, and normatively contested objectives. Diplomatic negotiation requires reading intentions, managing relationships, and balancing incommensurable values. Novel clinical presentations demand pattern recognition across sparse data, integration of patient-specific context, and decisions under irreducible uncertainty. Complex litigation strategy depends on predicting judicial and jury behavior, anticipating opponent moves, and weighing risks that resist quantification.

These domains share a common feature: correctness is real but not formalizable. A strategic plan can be better or worse, but "better" cannot be reduced to constraint satisfaction. A diagnosis can be right or wrong, but "right" depends on context, probability thresholds, and value judgments that resist mechanical encoding.

For such domains, SCAE is unavailable. ECAE is the ceiling. The question becomes: how do we strengthen ECAE to approach SCAE-level assurance without formal verification?

#### 4.5.1 The ECAE Assurance Gap

Standard ECAE relies on a single expert's judgment to validate AI outputs. This provides substantial assurance when the expert is competent, attentive, and appropriately skeptical. But single-expert ECAE has vulnerabilities:

**Fatigue and attention decay.** Experts reviewing many outputs develop routines. Verification becomes pattern-matching rather than genuine evaluation. Plausible outputs pass without scrutiny.

**Blind spots and biases.** Individual experts have systematic tendencies: favored approaches, familiar framings, areas of relative weakness within their domain.

**Overconfidence in own judgment.** Experts are not immune to Dunning-Kruger dynamics within their own domain.

**Adversarial vulnerability.** A sufficiently capable AI system might learn to produce outputs that exploit specific expert tendencies.

These vulnerabilities make single-expert ECAE insufficient for the highest-stakes applications in non-formalizable domains.

#### 4.5.2 Strengthening ECAE: Ensemble Expert Review

The first strengthening mechanism is multiplying expert perspectives:

**Cognitive diversity.** Select experts for different training backgrounds, methodological orientations, and areas of subspecialty. Heterogeneous panels catch more errors.

**Independent assessment.** Each expert evaluates outputs independently before discussion. Group deliberation that begins with a senior expert's opinion produces anchoring and conformity.

**Disagreement as signal.** When experts disagree, that disagreement is information. Forced consensus suppresses this signal.

**Minority opinion documentation.** When consensus is reached over dissent, document the dissenting view.

#### 4.5.3 Strengthening ECAE: Adversarial Red-Teaming

The second strengthening mechanism is deliberate stress-testing:

**Role separation.** Red-team experts should be distinct from validation experts. The cognitive set of "verify this output" differs from "break this output."

**Adversarial prompting.** Red-team members probe edge cases, construct failure scenarios, and test boundary conditions.

**Failure pattern documentation.** Red-teaming produces a catalog of known failure modes that inform deployment constraints.

**Iterative hardening.** Red-team findings feed back into system refinement.

#### 4.5.4 Strengthening ECAE: Structured Disagreement Protocols

The third strengthening mechanism is formalizing deliberation without formalizing correctness:

**Explicit criteria articulation.** Before evaluating outputs, experts articulate what they are looking for.

**Structured argumentation.** Defenses follow a common structure: claim, grounds, warrant, qualifications, rebuttals considered.

**Devil's advocate assignment.** For high-stakes assessments, one expert argues against the emerging consensus.

**Decision audit trails.** Document the path from AI output to validated output.

#### 4.5.5 Strengthening ECAE: Explicit Uncertainty Documentation

The fourth strengthening mechanism is preserving uncertainty:

**Uncertainty inheritance.** When AI outputs carry uncertainty, expert validation should not strip it away.

**Residual uncertainty flagging.** Validated outputs carry explicit markers of what remains uncertain.

**Decision-relevant uncertainty communication.** For outputs informing decisions, communicate uncertainty in decision-relevant terms.

**Uncertainty calibration over time.** Track whether expressed uncertainty matches actual error rates.

#### 4.5.6 The Limits of Strengthened ECAE

These mechanisms improve ECAE but do not transform it into SCAE. The gap remains:

**No mechanical guarantee.** Ensemble review, red-teaming, structured protocols, and uncertainty documentation all rely on human judgment. Human judgment can fail even when well-structured.

**Resource intensity.** Multiple experts, dedicated red teams, structured deliberation, and documentation all cost time and money.

**Expertise scarcity.** The mechanisms assume sufficient expert availability.

**Process degradation.** Structured processes can become ritualized over time.

These limits do not counsel abandonment. They counsel realism. Strengthened ECAE is the best available approach for high-stakes non-formalizable domains. It is substantially better than standard ECAE or lower tiers. It is not perfect. Where formal specification is possible and stakes are sufficient, SCAE remains preferable. Where formal specification is impossible, strengthened ECAE is the ceiling.

#### 4.5.7 Minimum Viable Strengthened ECAE

The full strengthened ECAE package (ensemble review, dedicated red teams, structured protocols, explicit uncertainty documentation) requires resources many organizations lack. When expert capacity is constrained, which mechanisms provide the most value per unit of expert time?

**Priority 1: Single expert with explicit criteria articulation.** Before reviewing AI outputs, the expert writes down what they are looking for. This simple discipline, requiring perhaps five minutes, substantially improves review quality by forcing conscious engagement rather than pattern-matching. It is the minimum intervention that distinguishes genuine ECAE from rubber-stamping.

**Priority 2: Uncertainty inheritance.** When AI outputs hedge or express uncertainty, preserve that uncertainty through the validation process. This requires no additional expert time, only the discipline not to strip hedging language from validated outputs. The cost is zero; the benefit is preventing false confidence propagation.

**Priority 3: Decision audit trail.** Document what was reviewed, what was changed, and why. A brief note ("Accepted AI analysis of factors 1-3; rewrote factor 4 based on recent precedent X") takes minutes and creates accountability. This documentation enables retrospective learning and protects against liability claims that no human review occurred.

**Priority 4: Periodic adversarial spot-checks.** Rather than dedicated red-teaming, allocate 10% of expert review time to actively trying to break outputs rather than verify them. One adversarial review per ten routine reviews surfaces failure patterns without requiring a separate red team.

**Priority 5: Second-expert review for threshold decisions.** Reserve ensemble review for decisions above a consequence threshold. Not every output needs multiple experts; the highest-stakes outputs do. Define the threshold explicitly rather than leaving it to ad hoc judgment.

**What to defer when resources are scarce:**

- *Full ensemble review for all outputs:* Reserve for high-stakes decisions only.
- *Dedicated red team:* Replace with periodic adversarial spot-checks.
- *Formal structured argumentation:* Simplify to explicit criteria plus brief rationale documentation.
- *Minority opinion documentation:* Implement only when ensemble review is used.

**The irreducible minimum:** A single qualified expert who (1) articulates criteria before review, (2) preserves AI-expressed uncertainty, and (3) documents what they changed and why. Below this threshold, deployment is not ECAE regardless of what it is called. Organizations unable to meet this minimum should either reduce deployment scope or accept that they are operating at PCAE with its corresponding limitations.

### 4.6 SCAE in Practice: Worked Examples

#### 4.6.1 Example One: Mathematical Proof with Lean Verification

**The problem domain.** Mathematical proof is the canonical SCAE application. Correctness is binary: a proof is valid or invalid. Validity is mechanically checkable against formal axioms.

**The workflow.**

*Step 1: Human formalization.* A mathematician translates a conjecture from natural language into the Lean proof assistant's type theory. This step requires deep expertise. The formalization must capture the mathematical content precisely. Errors here propagate through the entire pipeline.

*Step 2: AI-guided search.* The AI system (AlphaProof) searches for proof candidates. It proposes lemmas, attempts proof strategies, backtracks from dead ends, and explores the space of possible derivations. The search is guided by learned heuristics from training on human-written proofs.

*Step 3: Mechanical verification.* Each candidate proof is checked by Lean's kernel. The kernel verifies that every step follows from axioms and previously established results. This check is purely syntactic. The kernel does not understand the proof; it verifies formal derivation validity.

*Step 4: Expert interpretation.* The mathematician reviews verified proofs for mathematical significance. A proof can be formally valid but mathematically uninteresting, or valid but obscure where a cleaner proof exists.

**Strengths demonstrated.** Hallucination elimination within scope: the AI cannot produce invalid proofs that pass verification. Productivity amplification: mathematicians report acceleration on problems that would otherwise take months. Auditability: verified proofs carry complete derivation traces.

**Limitations demonstrated.** Formalization bottleneck: the mathematician's time is the constraint. Scope boundaries: Lean verifies within its axiom system but cannot verify axiom system consistency. Coverage limits: not all mathematics is formalized.

#### 4.6.2 Example Two: Safety-Critical Avionics Code

**The problem domain.** Flight control software must not fail. Errors can kill. Regulatory frameworks (DO-178C) require demonstration of correctness.

**The workflow.**

*Step 1: Specification formalization.* Systems engineers translate safety requirements into formal specifications using languages like ACSL (for C) or SPARK (for Ada).

*Step 2: AI-assisted code generation.* An AI system generates candidate implementations that aim to satisfy the specification.

*Step 3: Formal verification.* Static analysis tools and theorem provers check whether generated code satisfies formal specifications. Three outcomes are possible: Verified (property holds), Falsified (counterexample found), or Unknown (cannot determine).

*Step 4: Expert adjudication.* Engineers review verification results. Unknown results require human judgment about next steps.

**Strengths demonstrated.** Proactive error detection: formal verification finds errors testing misses. Regulatory alignment: DO-178C recognizes formal methods for compliance. Change confidence: re-verification immediately reveals if changes break proven properties.

**Limitations demonstrated.** Specification completeness: verification covers only specified properties. Verification complexity: many code patterns defeat automated provers. Tool trust: verification toolchains could contain bugs. Partial coverage: not all code can be formally verified in practice.

#### 4.6.3 Common Patterns Across Examples

Both examples reveal structural features of SCAE deployment:

**Human expertise bookends the process.** Experts formalize the problem at the start and interpret results at the end. AI operates in the middle, searching solution space under formal constraint.

**Mechanical verification provides bounded guarantees.** Within scope, verification is conclusive. But scope is always bounded.

**Scope awareness is essential.** SCAE systems must know their boundaries. Queries outside formal coverage should trigger refusal or escalation.

**The bottleneck is human synthesis capacity.** AI can search faster than humans. Verification can check faster than humans. But formalization remains slow, skilled, human work.

#### 4.6.4 SCAE Readiness Assessment

Assessment criteria for SCAE viability:

**Formal specifiability.** Can correctness criteria be expressed in a language verification tools accept?

**Tool maturity.** Do verification tools exist for this domain?

**Expert availability.** Are there people who can both understand the domain and perform formal specification?

**Economic justification.** Is the cost warranted by the stakes?

Where these criteria are met, SCAE represents the highest available epistemic assurance. Where they are not met, ECAE remains the ceiling.

---

## 5. Theoretical Integration: HCAE and the Three-Axis Framework

The HCAE tiers are not arbitrary categories chosen for convenience. They emerge from a deeper analysis of what makes AI systems reliable or unreliable. This section connects the tiered deployment framework to a three-axis model that distinguishes the dimensions along which AI systems succeed or fail.

### 5.1 The Three Axes

Most AI discourse operates on a single axis: infrastructure and data. Discussions of scaling laws, dataset curation, retrieval augmentation, context windows, and compute optimization all live on this axis. Call it the **horizontal axis**. It concerns getting the right information to the right place efficiently. This is legitimate engineering work. Infrastructure matters.

But infrastructure is not the whole problem.

A second axis concerns epistemology: does the system reason well about what it receives? Call it the **vertical axis**. Calibrated confidence, categorical precision, valid inference, self-consistency, appropriate uncertainty expression. Vertical-axis concerns appear in discussions of hallucination, calibration, chain-of-thought prompting, and reasoning benchmarks. Some AI discourse touches this axis, particularly in safety research.

A third axis concerns what the system is for and how it fits into larger wholes. Call it the **grounding axis**. This axis encompasses teleology (purpose, function, what counts as success) and mereology (part-whole relationships, how components relate to systems they enter). Almost no AI discourse addresses this axis directly.

The three-axis framework proposes that AI reliability problems are primarily grounding-axis problems misdiagnosed as horizontal-axis problems and addressed with horizontal-axis solutions.

### 5.2 The Grounding Deficit

Large language models have no access to the grounding axis.

**Teleological blindness.** The system has no representation of what it is for. It optimizes for next-token prediction, not for serving purposes external to that optimization. When deployed for tasks (legal research, medical consultation, strategic analysis), the system cannot evaluate whether its outputs serve the task's purpose. It produces probable token sequences. Whether those sequences constitute good legal research, sound medical advice, or useful strategic analysis is invisible to the system.

A system that cannot represent purpose cannot evaluate whether it is achieving purpose. It can be efficient, fluent, and internally consistent while failing entirely at what it was deployed to do. This is not a training failure. It is a structural feature. Purpose-evaluation requires access to purposes. Token prediction does not provide this access.

**Mereological blindness.** The system has no representation of how its outputs fit into larger wholes. It produces components without modeling the systems those components enter. A function that works in isolation may break the architecture it joins. An answer correct in general may be wrong for this context. A locally valid step may contribute to globally invalid conclusions.

A system that cannot represent part-whole relationships cannot evaluate whether its parts serve wholes. It produces outputs. Whether those outputs integrate coherently with existing systems, serve organizational objectives, or contribute to human flourishing is invisible to the system. This is not a limitation awaiting technical solution. It is categorical. Part-whole evaluation requires access to wholes. Token prediction operates at the part level.

### 5.3 How HCAE Addresses Grounding

The HCAE framework is a grounding-axis intervention. Each tier provides a different mechanism for supplying the grounding that AI systems structurally lack.

**UCAE: No grounding constraint.** At the User-Curated tier, the system operates without grounding. The user consumes outputs without evaluating whether they serve purposes or fit wholes. This is appropriate only when grounding does not matter: brainstorming where stimulation is the goal, drafting where revision will follow, entertainment where correctness is irrelevant. UCAE works when the absence of grounding is acceptable. It fails catastrophically when grounding is required but absent.

**PCAE: Professional norms as weak grounding.** At the Professional-Curated tier, professional training and institutional context provide partial grounding. The professional knows what the output is for (the client matter, the patient case, the business decision). Professional norms specify what counts as adequate work product. These function as weak teleological constraints. The professional also has partial mereological awareness: how this output fits the larger engagement, what depends on it, what it must cohere with.

But professional grounding is weak. Time pressure erodes verification. Plausibility substitutes for correctness. The professional's own limitations (knowledge gaps, biases, fatigue) constrain grounding quality. PCAE provides grounding, but grounding that may be insufficient for high-stakes applications.

**ECAE: Expert judgment as strong grounding.** At the Expert-Curated tier, domain expertise provides robust grounding. The expert has deep teleological understanding: not just what the output is for, but what "good" means in this domain, what tradeoffs are acceptable, what failure modes matter most. The expert has rich mereological awareness: how this output connects to the state of the field, what it presupposes, what it enables, how it might be misused.

Expert grounding is strong but not mechanical. It depends on the expert's continued engagement, their resistance to automation bias, their willingness to override plausible-sounding outputs when judgment says otherwise. ECAE works when experts maintain epistemic authority. It degrades when experts defer to the system.

**SCAE: Formal specification as mechanical grounding.** At the Synthesis-Curated tier, formal systems provide mechanical grounding within their scope. The formal specification encodes teleological constraints: what counts as a valid proof, what safety properties must hold, what regulatory requirements apply. The verification engine enforces these constraints regardless of how fluent or plausible the AI output sounds. Mereological constraints can also be encoded: type systems, interface contracts, consistency requirements that ensure parts fit wholes.

SCAE grounding is mechanical but bounded. It extends only as far as formal specification reaches. Beyond formal coverage, SCAE provides no grounding. The boundary between covered and uncovered territory must be explicit, and the system must refuse or escalate queries outside coverage.

### 5.4 Why Horizontal Solutions Fail

The documented failure of enterprise AI projects becomes intelligible through this framework.

Organizations face grounding-axis problems: AI outputs that do not serve organizational purposes, components that do not integrate with existing systems, locally optimized solutions that produce globally dysfunctional outcomes. These are teleological and mereological failures.

Organizations respond with horizontal-axis solutions: more data, better retrieval, larger context windows, finer-tuned models. These interventions elaborate the system's capacity to produce fluent outputs. They do not address whether those outputs serve purposes or fit wholes.

The result is sophisticated systems producing sophisticated failures. Outputs become more plausible while remaining disconnected from organizational reality. The gap between what the system produces and what the organization needs persists or widens. Investment increases while value capture stagnates.

The three-axis framework predicts this outcome. Horizontal solutions cannot resolve grounding problems. They operate on the wrong axis. The solution space and the problem space do not intersect.

### 5.5 Why Vertical Solutions Are Insufficient

Vertical-axis interventions (calibration, reasoning enhancement, hallucination reduction) fare better but still fall short.

Better calibration helps the system express appropriate uncertainty. But calibrated uncertainty about whether an output serves a purpose is still uncertainty about the wrong question. The system can be perfectly calibrated about token probabilities while remaining blind to teleological fit.

Enhanced reasoning helps the system produce more valid inferences. But valid inferences from ungrounded premises yield ungrounded conclusions. Reasoning quality is vertical-axis. Premise grounding is grounding-axis. Improving the former does not address the latter.

Hallucination reduction helps the system avoid factual errors. But factually accurate outputs can still fail teleologically (accurate information that does not serve the purpose) or mereologically (accurate components that do not fit the whole). Hallucination is a vertical-axis problem with grounding-axis consequences. Reducing hallucination is necessary but not sufficient.

Vertical interventions improve system quality on vertical criteria. They do not supply the grounding the system structurally lacks. HCAE remains necessary even for systems that excel on vertical metrics.

### 5.6 The Grounding Imperative

The three-axis framework yields a design imperative: **grounding must be supplied externally because it cannot be generated internally**.

AI systems can be improved on the horizontal axis (better infrastructure, more data, more compute). They can be improved on the vertical axis (better reasoning, better calibration, less hallucination). They cannot be improved on the grounding axis through internal modification because grounding requires access to purposes and wholes that exist outside the system.

This is not a contingent limitation. It is structural. A system that operates over representations of the world (text about reality) cannot access the world those representations describe. A system that produces components cannot access the wholes those components serve. The grounding axis is externally constituted.

HCAE operationalizes this imperative. It specifies who supplies grounding (users, professionals, experts, formal systems), what form that grounding takes (intuition, professional norms, expert judgment, mechanical verification), and how grounding adequacy matches task requirements (the tier-task matching problem).

The framework is not a workaround for temporary limitations. It is a design discipline for permanent structural features of the technology. Scaling will not eliminate the need for HCAE. Architectural innovation will not eliminate it. As long as AI systems operate over representations rather than reality, grounding must come from outside.

### 5.7 Implications for AI Development

The three-axis integration has implications for how AI systems should be built, not just deployed.

**Training data curation is grounding work.** The humans who select, filter, and annotate training data are supplying grounding. Their judgments about what counts as good output, what examples to include, what behaviors to reinforce encode teleological assumptions. Curation quality constrains the grounding available at deployment.

**Evaluation design is grounding work.** Benchmarks that reward accuracy without calibration, fluency without correctness, plausibility without fit are grounding-impoverished. They optimize systems on vertical criteria while ignoring grounding criteria. Better evaluations encode teleological and mereological standards, not just performance metrics.

**System prompting is grounding work.** Instructions that specify purpose, context, constraints, and success criteria supply grounding at inference time. Prompting that simply requests outputs without specifying fit leaves the system ungrounded. Prompt engineering is not merely eliciting capability; it is supplying the telos the system lacks.

**Deployment architecture is grounding work.** The choice of tier, the design of escalation pathways, the specification of validation protocols all determine how grounding flows into deployed systems. Deployment is not an afterthought to development. It is where grounding either succeeds or fails.

The common thread: grounding is human work. It is performed by curators, evaluators, prompt engineers, and deployment architects. It cannot be automated away because automation lacks grounding access. AI can assist this work (suggesting criteria, surfacing patterns, accelerating synthesis), but the judgment that constitutes grounding remains human.

---

## 6. The Matching Problem

The central practical question for HCAE deployment is tier selection: given a task, what tier does it require? This section provides structured guidance for the matching problem.

### 6.1 Assessment Dimensions

Five dimensions determine appropriate tier:

**Consequence severity.** What happens if the output is wrong? 

- Minimal consequence (embarrassment, minor rework) → UCAE acceptable
- Moderate consequence (professional reputation, recoverable financial loss) → PCAE minimum
- Serious consequence (legal liability, significant financial loss, health impacts) → ECAE minimum
- Catastrophic consequence (irreversible harm, safety-critical failure, loss of life) → SCAE required where available; strengthened ECAE where not

**Verifiability.** Can correctness be assessed, and by whom?

- Correctness is obvious to any user → UCAE acceptable
- Correctness requires professional training to assess → PCAE minimum
- Correctness requires deep domain expertise to assess → ECAE minimum
- Correctness can be mechanically verified → SCAE candidate

**Expertise availability.** Do qualified validators exist and are they available?

- No expertise required → UCAE
- Professional expertise available → PCAE achievable
- Domain experts available → ECAE achievable
- Formal methods experts and tools available → SCAE achievable

Tier requirements must match actual organizational capacity. Requiring ECAE when no experts are available produces either process theater (nominal review without substance) or deployment paralysis (work stops awaiting unavailable validation).

**Formal specifiability.** Can correctness be expressed in terms a verification system can check?

- Correctness is subjective or context-dependent → SCAE unavailable
- Correctness is objective but not formalizable → SCAE unavailable
- Correctness is formalizable but tools are immature → SCAE impractical
- Correctness is formalizable with mature tools → SCAE candidate

**Domain change rate.** How quickly does the domain evolve?

- Stable domain with established knowledge → All tiers viable
- Moderately evolving domain → SCAE may lag; ECAE often practical ceiling
- Rapidly evolving domain → Formal coverage lags; ECAE with continuous expert update required

### 6.2 The Tier Selection Matrix

Combining these dimensions produces a decision matrix:

| Consequence | Verifiability | Expertise | Specifiability | Recommended Tier |
|-------------|---------------|-----------|----------------|------------------|
| Minimal | Obvious | None needed | N/A | UCAE |
| Moderate | Professional | Available | N/A | PCAE |
| Serious | Expert | Available | No | ECAE (strengthened) |
| Serious | Expert | Available | Yes | SCAE |
| Catastrophic | Expert | Available | No | ECAE (strengthened) + compensating controls |
| Catastrophic | Expert | Available | Yes | SCAE mandatory |

The matrix is heuristic, not algorithmic. Edge cases require judgment. But the structure disciplines thinking and makes tier selection explicit rather than implicit.

### 6.3 Common Mismatches

**Under-deployment** (low tier for high-demand task) produces the failures documented in enterprise AI statistics. Symptoms include:

- Confident errors propagated into consequential decisions
- Users defending AI-originated positions they cannot evaluate
- Silent failures discovered only through downstream consequences
- Gradual erosion of trust as error accumulation becomes visible

**Over-deployment** (high tier for low-demand task) wastes resources without corresponding benefit. Symptoms include:

- Expert time consumed by routine validation
- Bottlenecks where expert availability constrains throughput
- Formalization effort exceeding the value it protects
- User frustration with unnecessary process requirements

Neither mismatch is benign. Under-deployment causes harm. Over-deployment causes inefficiency and can produce backlash that undermines appropriate caution elsewhere.

### 6.4 Organizational Assessment

Before deploying AI at any tier, organizations should assess:

**Current capacity.** What tier can we actually support with existing personnel, infrastructure, and processes? Do not plan for ECAE if you lack experts. Do not plan for SCAE if you lack formal methods capability.

**Capacity development.** What investments would enable higher-tier deployment where warranted? Hiring, training, tool acquisition, process development. These investments should be proportionate to the value at stake.

**Risk tolerance.** What residual risk is acceptable given the domain and organizational context? Some organizations must be more conservative than others. Regulated industries, safety-critical domains, and high-liability contexts warrant higher tiers than general business applications.

**Feedback mechanisms.** How will we detect tier-task mismatches after deployment? Monitoring, audit, incident review, user feedback. Without feedback, mismatches persist until failure makes them visible.

### 6.5 Decision Vignettes

The tier-selection criteria are abstract by design. These vignettes illustrate how the criteria apply in concrete organizational contexts.

#### Vignette 1: Contract Review Tool for a Mid-Size Law Firm

**Scenario.** A 50-attorney law firm considers deploying AI to review commercial contracts, flagging non-standard terms and suggesting revisions.

**Assessment.**
- *Consequence severity:* Moderate to serious. Missed non-standard terms could expose clients to unfavorable obligations. Errors in high-value transactions could produce significant liability.
- *Verifiability:* Professional training required. Associates can assess whether flagged terms are genuinely non-standard; partners can evaluate suggested revisions.
- *Expertise availability:* Partners have deep contract expertise. Associates have professional training but variable experience.
- *Formal specifiability:* Low. Contract interpretation depends on context, intent, and jurisdiction-specific precedent. Some clause types (e.g., indemnification caps) have clearer boundaries than others (e.g., "material adverse change" definitions).
- *Domain change rate:* Moderate. Contract law evolves, but standard commercial terms are relatively stable.

**Tier determination.** PCAE for routine contract review with associate validation. ECAE escalation for high-value transactions, novel clause structures, or unfamiliar jurisdictions. SCAE is unavailable because contract interpretation resists formalization.

**Implementation.** Associates review all AI-flagged terms before client delivery. Partner review required for transactions above threshold value or involving non-standard structures. Escalation triggers: conflicting AI suggestions, novel industry-specific terms, cross-border transactions with unfamiliar legal regimes.

#### Vignette 2: Clinical Decision Support for Emergency Department Triage

**Scenario.** A hospital system considers AI-assisted triage in emergency departments, suggesting acuity levels based on presenting symptoms and vital signs.

**Assessment.**
- *Consequence severity:* Serious to catastrophic. Under-triage delays treatment for critical patients. Over-triage wastes resources but rarely causes direct harm. Missed sepsis or cardiac events can be fatal.
- *Verifiability:* Expert assessment required for edge cases. Nurses can verify obvious presentations; physicians required for ambiguous cases.
- *Expertise availability:* ED physicians are domain experts but face severe time constraints. Triage nurses have professional training with variable experience.
- *Formal specifiability:* Partial. Some triage criteria (vital sign thresholds, validated scoring systems like qSOFA) are formalizable. Gestalt clinical judgment for atypical presentations is not.
- *Domain change rate:* Moderate. Clinical guidelines evolve; novel pathogens (as COVID demonstrated) can invalidate existing protocols rapidly.

**Tier determination.** PCAE baseline with nurse validation using standardized protocols. ECAE escalation mandatory for AI uncertainty flags, atypical presentations, or high-risk chief complaints. SCAE partially applicable for rule-based components (vital sign alerts, validated scoring systems) but cannot cover clinical gestalt.

**Implementation.** AI suggests acuity level; triage nurse confirms or overrides. Automatic physician notification for AI-flagged high-risk presentations regardless of nurse assessment. Strengthened ECAE (dual-physician review) for patients where AI and nurse assessments conflict. Audit trail for all AI suggestions and human decisions. Weekly case review of AI misses and near-misses.

#### Vignette 3: Financial Analysis for Investment Committee

**Scenario.** An asset management firm considers AI-generated analysis of potential investments, including financial modeling, risk assessment, and recommendation synthesis.

**Assessment.**
- *Consequence severity:* Serious. Poor investment decisions affect client returns and firm reputation. Fiduciary obligations create legal exposure.
- *Verifiability:* Expert assessment required. Financial modeling assumptions, risk factor weighting, and recommendation logic require experienced analyst evaluation.
- *Expertise availability:* Senior analysts and portfolio managers have deep expertise. Junior analysts have professional training but limited pattern recognition for market anomalies.
- *Formal specifiability:* Partial. Quantitative models (DCF, comparable analysis) have formalizable components. Investment thesis quality, management assessment, and market timing judgment do not.
- *Domain change rate:* High. Market conditions, sector dynamics, and macroeconomic factors evolve continuously.

**Tier determination.** ECAE required. Investment decisions are too consequential for PCAE, and the domain's judgment-intensive nature precludes SCAE for the recommendation layer. SCAE applicable for quantitative model validation (checking arithmetic, flagging assumption inconsistencies).

**Implementation.** AI generates draft analysis; senior analyst reviews all components before investment committee presentation. Quantitative models validated through automated consistency checks (SCAE component). Investment thesis and risk narrative require analyst rewriting, not just approval. Explicit documentation of where analyst judgment diverged from AI suggestion. Portfolio manager final authority; AI analysis is input, not recommendation.

#### Vignette 4: Marketing Content Generation for E-Commerce

**Scenario.** An online retailer considers AI-generated product descriptions, promotional copy, and email campaigns.

**Assessment.**
- *Consequence severity:* Minimal to moderate. Poor copy reduces conversion rates. Factual errors about products could create customer service issues or, rarely, liability for misleading claims.
- *Verifiability:* Obvious for most content. Marketing team can assess tone, brand alignment, and basic accuracy. Legal review needed only for claims requiring substantiation.
- *Expertise availability:* Marketing professionals available. Legal review available but expensive to deploy routinely.
- *Formal specifiability:* Low for creative quality. Partial for compliance (prohibited claims, required disclosures).
- *Domain change rate:* High for promotional content; moderate for product descriptions.

**Tier determination.** UCAE acceptable for draft generation and internal brainstorming. PCAE required before publication, with marketing professional review for brand alignment and basic accuracy. ECAE escalation (legal review) for health claims, comparative advertising, or regulated product categories.

**Implementation.** AI generates content variants; marketing team selects and edits before publication. Automated flagging (rule-based, approaching SCAE) for prohibited terms and claims requiring substantiation. Legal review triggered by flags or product category (supplements, financial products, children's items). No direct AI-to-publication pipeline; human review required for all customer-facing content.

#### Vignette Patterns

These vignettes reveal common patterns:

**Hybrid deployment is typical.** Most real applications operate across multiple tiers depending on query characteristics. Pure single-tier deployment is rare outside the extremes (pure brainstorming at UCAE, pure formal verification at SCAE).

**Escalation triggers must be concrete.** Abstract criteria ("high stakes") become operational only when translated into specific signals (transaction value thresholds, clinical red flags, regulatory category).

**SCAE components embed within ECAE workflows.** Even when overall deployment is ECAE, rule-based validation (consistency checks, prohibited term flagging, threshold alerts) can provide SCAE-level assurance for formalizable subcomponents.

**Expert time is the binding constraint.** In every vignette, the limiting factor is availability of qualified human validators, not AI capability. Deployment architecture must optimize expert attention allocation, not just AI performance.

---

## 7. Economic and Regulatory Implications

### 7.1 The Economics of Grounding

HCAE reveals a fundamental economic reality: reliable AI requires human grounding, and human grounding has costs.

**UCAE is cheap but unreliable.** The cost is minimal, but so is the assurance. UCAE is economically appropriate only where the value at risk is correspondingly low.

**PCAE scales with professional labor costs.** Professional review adds cost proportional to professional compensation and time required. PCAE is economically appropriate where the value protected exceeds the review cost.

**ECAE scales with expert scarcity.** Expert review is expensive because experts are scarce. ECAE is economically appropriate for high-value tasks where expert judgment is essential and no formal alternative exists.

**SCAE has high fixed costs and low marginal costs.** Building formal infrastructure (specifications, tools, expertise) requires substantial investment. Once built, marginal verification is cheap. SCAE is economically appropriate where high-value tasks occur repeatedly within formal coverage.

Organizations that treat AI as a way to eliminate human labor costs misunderstand the technology. AI shifts where human judgment is required (from execution to validation) without eliminating the requirement. The economic benefit comes from amplification (one expert validating many AI-generated outputs) rather than replacement (no expert at all).

### 7.2 Regulatory Alignment

The HCAE framework aligns naturally with emerging regulatory approaches:

**EU AI Act.** The risk-based classification (minimal, limited, high, unacceptable risk) maps to tier-appropriate deployment. High-risk AI systems require documentation, human oversight, and accuracy obligations that ECAE or SCAE would provide. The HCAE framework provides concrete implementation guidance for these requirements.

**Sector-specific regulation.** Healthcare (FDA), finance (SEC/FINRA), aviation (FAA/EASA), and other regulated domains increasingly require validation of AI outputs. HCAE tiers map to regulatory expectations: PCAE for routine applications with professional oversight, ECAE for clinical decision support with physician review, SCAE for safety-critical systems with formal verification.

**Liability frameworks.** As AI-related litigation increases, deployment tier becomes relevant to liability assessment. Organizations that deployed at inappropriate tiers (low tier for high-stakes task) face exposure. Organizations that documented appropriate tier selection and validation have defensible positions.

The regulatory landscape is evolving. HCAE provides a framework that anticipates regulatory direction and positions organizations for compliance regardless of specific requirements that emerge.

#### 7.2.1 Regulatory Control Mapping

The following table maps specific regulatory requirements to HCAE tier controls. This is illustrative, not exhaustive; organizations should consult current regulatory text and legal counsel.

**EU AI Act - High-Risk Systems (Annex III categories)**

| Requirement | HCAE Control |
|-------------|--------------|
| Risk management system (Art. 9) | Tier selection documentation; escalation protocols; feedback mechanisms |
| Data governance (Art. 10) | Training data curation as grounding work (Section 5.7); PCAE minimum for data quality review |
| Technical documentation (Art. 11) | Decision audit trails; tier justification records |
| Record-keeping (Art. 12) | Escalation logs; validation outcome documentation |
| Transparency (Art. 13) | Tier disclosure to users; uncertainty communication |
| Human oversight (Art. 14) | ECAE minimum for high-risk; strengthened ECAE mechanisms; override capability preservation |
| Accuracy, robustness, cybersecurity (Art. 15) | SCAE for safety-critical components where formalizable; ECAE with red-teaming for others |

**FDA - Clinical Decision Support (21st Century Cures Act criteria)**

| Criterion | HCAE Implication |
|-----------|------------------|
| Intended for healthcare professional use | PCAE minimum (professional validation required) |
| Displays basis for recommendations | Uncertainty documentation; audit trail visibility |
| Professional can independently review | ECAE structure: AI proposes, clinician validates with independent judgment capability |
| Not intended to replace professional judgment | ECAE design principle: AI as input, not recommendation |

For CDS that does not meet all four criteria (and thus is regulated as a medical device):

| Requirement | HCAE Control |
|-------------|--------------|
| Premarket review (510(k) or PMA) | SCAE for algorithm validation where formalizable; ECAE with clinical validation studies |
| Quality system regulation | Tier-appropriate validation protocols; change control with re-verification |
| Postmarket surveillance | Feedback mechanisms; outcome tracking; escalation pattern monitoring |

**SEC/FINRA - Algorithmic Trading and Robo-Advice**

| Requirement | HCAE Control |
|-------------|--------------|
| Fiduciary duty (for investment advisers) | ECAE minimum; expert review of recommendations before client delivery |
| Best execution (trading) | SCAE for execution algorithm verification where formalizable |
| Suitability/Reg BI | ECAE review of suitability determinations; client-specific factor validation |
| Books and records | Decision audit trails; validation documentation retention |
| Supervision | Tier certification for supervisory personnel; escalation pathway documentation |

**FAA/EASA - Aviation Software (DO-178C)**

| Design Assurance Level | HCAE Mapping |
|------------------------|--------------|
| DAL A (catastrophic failure) | SCAE mandatory; formal methods for safety-critical components |
| DAL B (hazardous) | SCAE strongly recommended; ECAE with enhanced verification if SCAE impractical |
| DAL C (major) | ECAE minimum; structured validation protocols |
| DAL D/E (minor/no effect) | PCAE acceptable with appropriate documentation |

**Implementation guidance:**

1. **Identify applicable regulations** before tier selection. Regulatory requirements may mandate minimum tiers regardless of internal risk assessment.

2. **Document regulatory mapping** as part of deployment justification. Show which requirements are addressed by which HCAE controls.

3. **Build controls into workflow**, not as afterthought compliance. HCAE tiers provide structure; regulatory requirements provide minimum thresholds.

4. **Plan for regulatory evolution.** Current requirements are floors, not ceilings. Building stronger-than-required controls provides buffer as requirements tighten.

### 7.3 Market Implications

HCAE has implications for AI vendors and buyers:

**For vendors:** Differentiation may increasingly come from deployment infrastructure rather than model capability. Vendors that provide tier-appropriate tooling (escalation pathways, validation workflows, formal verification integration) add value beyond raw model performance.

**For buyers:** Procurement decisions should consider not just AI capability but deployment tier requirements. A more capable model deployed at an inappropriate tier may produce worse outcomes than a less capable model deployed appropriately.

**For the market:** The "scale solves everything" narrative faces structural limits. Markets that recognize grounding constraints will allocate resources differently than markets that expect scaling to resolve reliability problems. The correction may be painful for investments predicated on unlimited scaling returns.

---

## 8. Conclusion

Enterprise AI fails at rates between 70% and 95% because organizations face grounding-axis problems and apply horizontal-axis solutions. AI systems lack access to the purposes they serve and the wholes their outputs enter. Scaling cannot fix this structural deficit. Grounding must be supplied externally.

The HCAE framework provides the design discipline: UCAE for low-stakes ideation, PCAE for routine professional work, ECAE for high-stakes analysis, SCAE for formally verifiable domains. The framework is a toolkit, not a ladder. The goal is fit between tier and task.

The three-axis model explains why alternatives fail. Horizontal solutions (more infrastructure) cannot address grounding problems. Vertical solutions (better reasoning) improve quality without supplying grounding. Only grounding-axis interventions address the structural deficit.

The path forward is design discipline that acknowledges what AI systems are: powerful tools for generation and search that require human grounding. The choice is not between AI and no AI. The choice is between AI deployed with appropriate grounding and the 70-95% failure rates that characterize deployment without it. HCAE shows how to do better.

---

## References

Banerjee, S., Agarwal, A., & Singla, S. (2024). LLMs will always hallucinate, and we need to live with this. *arXiv:2409.05746*. https://arxiv.org/abs/2409.05746

Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW1), Article 188. https://doi.org/10.1145/3449287

Dell'Acqua, F., McFowland III, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality. *Harvard Business School Working Paper No. 24-013*.

Gartner. (2024, July 29). Gartner predicts 30% of generative AI projects will be abandoned after proof of concept by end of 2025. *Gartner Newsroom*. https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025

Gartner. (2025, June 25). Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027. *Gartner Newsroom*. https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027

Hubert, T., Mehta, R., Sartran, L., et al. (2025). Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature*. https://doi.org/10.1038/s41586-025-09833-y

Kadavath, S., Conerly, T., Askell, A., et al. (2022). Language models (mostly) know what they know. *arXiv:2207.05221*. https://arxiv.org/abs/2207.05221

Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate. *arXiv:2509.04664*. https://arxiv.org/abs/2509.04664

Longmire, J. (2026a). AI Dunning-Kruger (AIDK): A framework for understanding structural epistemic limitations in AI systems. *Zenodo*. https://doi.org/10.5281/zenodo.18316059

MIT Project NANDA. (2025). The GenAI divide: State of AI in business 2025. Lead author: Aditya Challapally, MIT Media Lab.

Xu, Z., Jain, S., & Kankanhalli, M. (2024). Hallucination is inevitable: An innate limitation of large language models. *arXiv:2401.11817*. https://arxiv.org/abs/2401.11817

---

*Developed under the ECAE (Expert-Curated, AI-Enabled) model described in this framework, with derivational contributions from Claude. Origination, judgment, and final authority on truth and validity remain with the human author.*
