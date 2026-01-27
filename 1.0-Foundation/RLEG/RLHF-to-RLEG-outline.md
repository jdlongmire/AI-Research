# From RLHF to RLEG: Expert Grounding as a Solution to the Fluency-Calibration Tradeoff

## Paper Outline (Revised with RLEG terminology and Research Program)

---

## Abstract

Reinforcement Learning from Human Feedback (RLHF) produces large language models that are fluent, engaging, and confidently wrong. Recent research documents a persistent tradeoff: optimizing for human approval improves conversational quality while frequently degrading calibration, increasing verbalized overconfidence, and damaging factual reliability. This paper argues that the problem is not reward engineering but feedback source. Standard RLHF relies on crowdworker judgments that can evaluate fluency, tone, and format but cannot evaluate domain accuracy, appropriate uncertainty, or fitness for purpose. We propose RLEG (Reinforcement Learning from Expert Guidance) as an alternative paradigm in which domain experts provide training signal that carries teleological and mereological information crowdworkers cannot access. The shift from "Feedback" to "Guidance" is substantive: feedback is reactive and corrective (vertical axis—was the reasoning sound?); guidance is directional and purposive (grounding axis—does it serve the right end? does it fit the whole it enters?). The expert evaluates not only whether an output is correct but whether it serves its intended purpose and fits the whole it enters. We analyze the Deep Blue and AlphaGo precedents, where expert grounding enabled superhuman performance in domains of increasing intractability, and argue that RLEG requires analogous team structures: domain experts who provide grounded judgment paired with AI training specialists who translate that judgment into effective reward signal. We identify a novel competency gap—the absence of trained RLEG practitioners who understand both domain requirements and reward shaping—and propose a multi-phase research program for developing this methodology. Finally, we argue that RLEG does not solve the grounding problem at the model level (the system remains derivative) but solves it at the training signal level, propagating expert grounding through the learned distribution. The result is a model that pattern-matches to outputs experts judged as serving the right purpose and fitting the right whole, rather than outputs crowdworkers found engaging.

**Keywords:** reinforcement learning from human feedback; expert guidance; calibration; fluency-accuracy tradeoff; teleology; mereology; grounding; human-AI collaboration; RLEG

---

## Terminological Note

RLEG (Reinforcement Learning from Expert Guidance) should be distinguished from RLEF (Reinforcement Learning from Execution Feedback) introduced by Gehring et al. (2024), which uses automated test execution as feedback signal for code synthesis. The shift from "Feedback" to "Guidance" is deliberate and substantive:

- **Feedback** is reactive, corrective, backward-looking: "that was wrong" (vertical axis)
- **Guidance** is directional, purposive, forward-looking: "this is what it's for, this is where it fits" (grounding axis)

RLHF and RLEF both operate primarily on the vertical axis—improving reasoning quality and correctness. RLEG operates on the grounding axis—ensuring outputs serve their intended purpose and cohere with the wholes they enter. The two approaches are complementary: execution feedback provides grounding where formal verification exists (code, mathematics, formal logic); expert guidance provides grounding where it does not (medicine, law, strategy, ethics, open-ended generation). This paper addresses the latter.

---

## 1. Introduction

### 1.1 The RLHF Success Story
- RLHF transformed base models into usable products
- Dramatic improvements in user engagement, instruction-following, perceived helpfulness
- Commercial viability depends on RLHF or similar alignment techniques

### 1.2 The Hidden Cost
- Frequently observed calibration degradation post-RLHF
- Verbalized overconfidence regardless of actual reliability
- Factuality damage in open-ended generation
- The "deployment paradox": models most suitable for users resist safety interventions in conversational contexts

### 1.3 The Standard Diagnosis
- Field treats this as a reward engineering problem
- Proposed solutions: better reward models, multi-objective optimization, factuality-specific training
- Implicit assumption: the problem is *how* feedback is structured, not *who* provides it

### 1.4 Our Thesis
- The problem is feedback source, not feedback structure
- Crowdworkers can evaluate what they can perceive; they cannot evaluate what requires domain expertise
- RLEG addresses the grounding gap by changing who provides training signal
- This requires novel team structures, methodologies, and a sustained research program not yet developed

---

## 2. The Fluency-Calibration Tradeoff: Empirical Foundations

### 2.1 Calibration in Base Models
- Pre-RLHF models often show well-calibrated conditional probabilities
- Confidence tracks correctness more reliably before alignment in many observed cases
- Important caveat: some base models already exhibit miscalibration in certain regimes
- Base models are typically calibrated but unusable for deployment

### 2.2 Calibration Degradation Post-RLHF
- Reward models frequently exhibit inherent bias toward high-confidence outputs
- Verbalized overconfidence emerges as trained behavior in many RLHF implementations
- The "assertiveness prior": being helpful and confident dominates in natural conversation
- Quantitative evidence: ECE increases, factuality scores decrease on open-ended tasks
- Note: effects vary with method and architecture; claims should be understood as "frequently observed" rather than universal

### 2.3 The Mechanism
- Crowdworkers reward fluency, confidence, completeness, engagement
- Crowdworkers cannot reliably evaluate: domain accuracy, reasoning validity, appropriate uncertainty, subtle errors
- Optimization target diverges from reliability target
- Model learns to *appear* reliable rather than *be* reliable

### 2.4 Why Reward Engineering Cannot Fully Solve This
- Multi-objective rewards help but don't eliminate the gap
- Factuality rewards require ground truth crowdworkers cannot provide
- Calibration rewards require correctness labels crowdworkers cannot generate
- The bottleneck is evaluator competence, not reward function design
- Cite: contrast with approaches that modify reward modeling or calculation but still use non-expert raters (Leng et al.)

---

## 3. RLEG: Conceptual Foundations

### 3.1 The Expert Difference
- Domain experts can evaluate what crowdworkers cannot:
  - Factual accuracy in specialized domains
  - Reasoning validity within domain constraints
  - Appropriate uncertainty given available evidence
  - Subtle errors invisible to non-experts

### 3.2 Beyond Accuracy: Teleological and Mereological Grounding
- The "Guidance" in RLEG signifies grounding-axis evaluation: experts assess purpose-fitness and part-whole fit, not just correctness
- **Teleological grounding:**
  - "Does this output serve its intended function?"
  - "Would this be useful in the actual workflow it enters?"
  - Telos-awareness in training signal that crowdworkers cannot provide
- **Mereological grounding:**
  - "Does this component work within the system it enters?"
  - "Are there integration failures invisible at the output level?"
  - Whole-awareness in training signal that isolated evaluation cannot provide
- **Concrete examples:**
  - *Medical:* Radiologist evaluates diagnostic summary not just for accuracy but for clinical workflow integration—does it serve triage, treatment planning, or documentation? Does it fit the patient's whole case?
  - *Legal:* Attorney evaluates contract analysis not just for correctness but for fitness to the matter at hand—does it serve the client's actual legal strategy? Does it cohere with the full case context?

### 3.3 What RLEG Does and Does Not Solve
- Does solve: grounding at the training signal level
- Does not solve: grounding at the model level
- The model remains derivative; it pattern-matches to expert-validated outputs
- But derivative from expert judgment is categorically different from derivative from crowdworker approval

### 3.4 RLEG vs. RLEF (Execution Feedback)
- Gehring et al. (2024): RLEF uses compiler/test feedback for code synthesis
- Execution feedback works where formal verification exists
- Expert feedback required where it does not
- Complementary approaches for different domain types
- RLEG addresses the harder problem: domains without automatic ground truth

---

## 4. Historical Precedents: From Deep Blue to AlphaGo

### 4.1 Deep Blue: Expert Grounding in Tractable Domains

**Structure of the achievement:**
- Chess grandmasters provided domain grounding
- IBM engineers provided computational implementation
- Neither alone could beat Kasparov; together they did

**What the grandmasters contributed:**
- Opening book evaluation (purpose-fitness of positions)
- Position evaluation weights (what features matter)
- Endgame knowledge (how parts relate to game trajectory)
- Teleological and mereological judgment encoded in evaluation functions

**What the engineers contributed:**
- Translation of expert judgment into computable form
- Search algorithms that leveraged the evaluation function
- Hardware and software implementation
- Optimization within the constraints experts defined

**Deep Blue as proto-RLEG:**
- Human-curated, AI-enabled before the terminology existed
- Grounding through expert judgment, not through system access to reality
- The system never "understood" chess; it inherited grounding through its evaluation function

### 4.2 AlphaGo: Expert Grounding Scales to Intractable Domains

**Why Go required a paradigm shift:**
- Chess: moderate branching factor, tractable via brute-force + human heuristics
- Go: astronomical branching factor (~250 legal moves per position vs. ~35 in chess)
- Pure search fails; grounding must be injected via learning from expert-like distributions

**The expert grounding pathway in AlphaGo:**
- Initial version: supervised pre-training on ~30 million positions from human expert games
- Policy network learned to approximate what strong human play would choose
- Value network learned to evaluate positions as experts would
- Analogous to grandmasters curating opening books and evaluation weights, but at scale

**Self-play amplification:**
- AlphaGo Zero removed human data entirely
- Converged on superhuman play through self-play reinforcement
- Yet the ultimate benchmark remained alignment with expert-recognized strength (win conditions, professional games for validation)
- Self-play amplified expert-seeded grounding rather than replacing it

**The key insight:**
- Even in self-play phases, the system learned to approximate what strong human play would deem good
- Grounding remained derivative—pattern-matching to expert-validated distributions
- But derivation from expert judgment produced superhuman performance where derivation from naive heuristics could not

### 4.3 The Complexity Escalation: Why Language Requires RLEG

**Domain complexity progression:**

| Domain | Tractability | Branching | Win Condition | Expert Grounding Method |
|--------|--------------|-----------|---------------|------------------------|
| Chess | Moderate | ~35 moves | Objective | Evaluation function encoding |
| Go | Astronomical | ~250 moves | Objective | Expert-seeded learning + self-play |
| Language | Unbounded | Infinite | Contested/teleological | RLEG (required, not optional) |

**Why crowdworker RLHF is even less adequate for language than hand-crafted heuristics were for Go:**
- Go's complexity forced a leap from hand-crafted heuristics to learned intuition
- Language is even more contested and teleology-heavy than Go
- No crisp win condition; success depends on user intent, workflow fit, appropriate uncertainty
- Crowdworkers can judge surface qualities but lack the teleological and mereological grounding that experts provide
- In intractable domains with contested success criteria, expert-sourced feedback is not just better—it is essential for high-stakes reliability

**The argument:**
- In tractable domains (chess), expert grounding + engineering translation sufficed
- In intractable domains with clear objectives (Go), expert-seeded learning scaled to superhuman performance
- In intractable domains with contested objectives (language), crowdworker preferences are structurally inadequate
- RLEG is not an incremental improvement; it addresses a category of problem that RLHF cannot reach

### 4.4 Fluency and Calibration in Game AI: A Parallel

**AlphaGo achieved both fluency and calibration:**
- "Fluent" in human terms: natural, elegant, creative plays that professionals admired
- Well-calibrated to winning probability: value network rarely overconfident in lost positions
- Move 37 in Game 2 against Lee Sedol: surprising to experts but strategically sound

**Why this occurred:**
- Training signal was grounded in true domain expertise (human games or self-play approximating expert outcomes)
- The system optimized for what experts would recognize as strong, not what observers would find entertaining

**The counterfactual:**
- If Go training had used "crowdworker-style" preferences ("does this move look cool/surprising/fun?")
- The system might have learned flashy but unreliable tactics
- Mirroring the verbalized overconfidence and assertiveness bias documented in RLHF LLMs

**The parallel to RLEG architecture:**
- AlphaGo: win probability (expert-validated objective) as primary, elegance emerged as byproduct
- RLEG: grounding/accuracy/calibration as primary objective (expert-driven), fluency as soft constraint or emergent property
- Both succeed by not letting crowd-pleasing surface qualities dominate and degrade core reliability

### 4.5 The Self-Play Limitation: What Language Cannot Borrow

**Why AlphaGo could amplify expert grounding via self-play:**
- Clear win condition: game outcome provides unambiguous reward signal
- Closed system: rules fully specified, no external world to model
- Self-play generates unlimited training data with automatic ground truth

**Why language lacks this self-supervised loop:**
- No automatic "win" signal for open-ended generation
- Success criteria are contested, context-dependent, teleologically defined
- Self-play in language produces fluent nonsense or mode collapse, not superhuman insight
- The system cannot verify its own correctness against reality

**Implications for RLEG:**
- RLEG cannot rely on self-play amplification the way AlphaGo did
- Expert grounding must be more directly sustained throughout training
- Requires stronger scaffolding: multi-objective rewards, staged training, explicit calibration penalties
- Section 8 addresses this: calibration-preserving RLEG with structured reward components

**The bottleneck shifts:**
- AlphaGo: expert grounding seeds the process, self-play scales it
- RLEG for language: expert grounding must be continuously injected because no self-play substitute exists
- This makes expert-trainer collaboration methodology (Sections 5-6) even more critical

### 4.6 What Both Precedents Share: Derivative Systems with Inherited Grounding

**Neither system achieved genuine understanding:**
- Deep Blue never "understood" chess; it evaluated positions via expert-encoded functions
- AlphaGo never "understood" Go; it pattern-matched to expert-validated distributions
- Both remained derivative systems with no access to what makes chess or Go meaningful

**Yet both achieved superhuman performance:**
- By inheriting grounding through expert-shaped training signal
- The grounding propagated through the learned distribution
- The system outputs reflected expert judgment without instantiating expert understanding

**This is the RLEG thesis in miniature:**
- RLEG does not solve grounding at the model level (the system remains derivative)
- RLEG solves grounding at the training signal level
- Expert judgment becomes encoded in learned behavior
- The result is a model that pattern-matches to expert-validated outputs, not crowdworker-approved outputs
- Derivative from expert grounding is categorically superior to derivative from surface preferences

**Transfer potential (research direction):**
- AlphaZero generalized the AlphaGo architecture to chess, beating prior engines with human heuristics
- Suggests RLEG in one high-stakes domain (e.g., medical) might transfer grounding benefits to adjacent areas
- Worth exploring: does expert grounding in one domain improve calibration and reliability in related domains?

---

## 5. The RLEG Team Structure

### 5.1 Why a Single Expert Is Insufficient
- Domain expertise ≠ reward shaping expertise
- Expert knows correct answer; doesn't know how to structure feedback for learning
- Naive expert feedback may not produce intended model behavior

### 5.2 Why a Single AI Trainer Is Insufficient
- AI training expertise ≠ domain expertise
- Trainer can structure rewards; cannot evaluate domain correctness
- Training without grounding optimizes the wrong target

### 5.3 The Required Collaboration
- Domain expert provides: correctness judgment, purpose evaluation, whole-fit assessment, calibration judgment
- AI training expert provides: reward structure design, feedback elicitation protocols, reward hacking detection, learning dynamics monitoring

### 5.4 The Interface Between Them
- **What must the expert communicate?**
  - Category of error (not just "wrong")
  - Magnitude of error (not just binary)
  - Direction of fix (not just "try again")
  - Stakes involved (consequence weighting)
  - Calibration appropriateness (was uncertainty appropriate?)
- **What must the trainer provide?**
  - Elicitation protocols that extract this information efficiently
  - Reward models that preserve these distinctions
  - Feedback on what the model is actually learning
  - Detection when reward hacking circumvents intent

### 5.5 Precedent: Software Development
- Business analysts ≠ engineers, but they collaborate through structured interfaces
- Requirements elicitation, user stories, acceptance criteria
- RLEG needs analogous methodology for expert-trainer collaboration

---

## 6. The RLEG Practitioner: A Missing Role

### 6.1 The Competency Gap
- No current training produces RLEG practitioners
- Domain experts lack AI training knowledge
- AI engineers lack domain expertise
- The intersection is unpopulated

### 6.2 What RLEG Practitioners Would Need to Know
- Domain knowledge sufficient to evaluate outputs (or protocols for working with those who have it)
- Reward shaping: how feedback structure affects learned behavior
- Failure modes: reward hacking, distribution shift, calibration collapse
- Elicitation: how to extract grounded judgment from experts efficiently
- Translation: how to convert expert judgment into effective training signal

### 6.3 Training Pathways
- Domain experts + AI training supplementation
- AI engineers + domain immersion
- New graduate programs at the intersection
- Professional certification for RLEG practice

### 6.4 Organizational Implications
- RLEG teams as distinct organizational unit
- Neither pure ML engineering nor pure domain work
- Hybrid reporting structures and incentives

---

## 7. Maintaining Fluency Under RLEG

### 7.1 The Risk
- Optimizing hard for expert approval may sacrifice fluency
- Outputs become technically correct but stilted, inaccessible, unusable
- Model learns expert register at the cost of general usability

### 7.2 Evidence That the Tradeoff May Be Softer Than Assumed
- Factuality tuning studies show fluency can improve alongside accuracy
- FLAME results demonstrate that factuality and fluency can improve together when training objectives are structured properly
- The tradeoff is sharper when objectives compete; it softens when they're structured as constraint + optimization

### 7.3 Proposed Architecture: Fluency as Constraint, Grounding as Objective
- Stage 1: RLEG for domain accuracy, purpose-fitness, calibration
- Stage 2: Fluency optimization within RLEG-established bounds
- Alternative: Composite reward with expert approval as hard constraint, fluency as soft optimization

### 7.4 The Weighting Problem
- How much fluency loss is acceptable for how much accuracy gain?
- Domain-dependent: consumer chat vs. medical diagnosis vs. legal analysis
- RLEG methodology must include explicit fluency-accuracy tradeoff specification

---

## 8. Calibration-Preserving RLEG

### 8.1 Calibration as Explicit Training Objective
- Standard RLHF often ignores calibration; RLEG can target it
- Expert evaluates not just "is this correct" but "is this confidence appropriate"
- Reward structure penalizes confidence-correctness mismatch
- Ground in factuality-aware alignment and calibration-oriented RLHF work (FLAME, Leng et al.)

### 8.2 Expert Calibration Judgment
- Experts can assess: "Given what's knowable, should the model be this confident?"
- Crowdworkers cannot assess this; they reward confidence regardless
- RLEG training signal carries calibration information RLHF cannot

### 8.3 Proposed Reward Components
- Accuracy reward: is the output correct?
- Calibration reward: does expressed confidence match reliability?
- Purpose reward: does this serve its intended function?
- Fluency reward: is this accessible and well-formed?
- Weighting: calibration and accuracy as constraints, fluency as optimization target

### 8.4 Detecting Calibration Collapse
- Monitor confidence distribution across training
- Flag when model becomes uniformly confident
- Expert spot-checks on uncertainty-appropriate cases

---

## 9. Limitations and Open Questions

### 9.1 Scalability
- Expert time is expensive and scarce
- RLEG cannot scale like crowdworker RLHF
- Possible mitigations (building on existing active learning and human-in-the-loop RL literature):
  - Expert-seeded RLAIF
  - Hierarchical review structures
  - Active learning for efficient expert allocation
  - Uncertainty-based sampling to maximize expert impact

### 9.2 Expert Disagreement
- Experts disagree; domains have contested questions
- RLEG with disagreeing experts may produce confused models
- Need protocols for handling expert disagreement: flag uncertainty, present alternatives, defer to consensus where possible

### 9.3 Domain Coverage
- RLEG requires experts for each domain the model addresses
- General-purpose LLMs cover unbounded domains
- Possible approach: RLEG for high-stakes domains, standard RLHF for general chat

### 9.4 The Grounding Limit
- RLEG solves grounding at training signal level, not model level
- The model still lacks reality access
- Expert grounding propagates through learned distribution but doesn't constitute genuine understanding
- RLEG-trained models remain derivative systems requiring appropriate deployment constraints

### 9.5 Evaluation
- How do we measure RLEG success?
- Proposed metrics: domain-specific accuracy, calibration (ECE), expert approval rate, fluency ratings, downstream task performance
- Need benchmarks that capture teleological and mereological fit, not just output correctness

---

## 10. A Research Program for RLEG

This paper proposes not a single empirical result but a paradigm shift requiring sustained investigation. The following research program outlines the work needed to develop RLEG from conceptual framework to deployable methodology.

### 10.1 Phase 1: Foundational Validation (Years 1-2)

**Core question:** Does RLEG actually preserve calibration better than RLHF?

**Research agenda:**
- Matched domain comparisons: RLEG vs. RLHF on identical base models, identical domains
- Calibration measurement: ECE, reliability diagrams, confidence-accuracy curves pre/post training
- Factuality measurement: domain-specific accuracy benchmarks
- Fluency measurement: human evaluation of output quality

**Success criteria:**
- Demonstrated calibration preservation or improvement under RLEG
- No significant fluency degradation (or documented tradeoff curves)
- Reproducible across at least two distinct domains

**Dependencies:** None (foundational)

**Potential collaborators:** Academic ML labs, industry research teams with domain expert access

### 10.2 Phase 2: Methodology Development (Years 2-4)

**Core question:** How should expert-trainer collaboration be structured for effective RLEG?

**Research agenda:**
- Expert elicitation protocols: What questions extract grounded judgment efficiently?
- Reward structures: How to preserve teleological and mereological information in training signal?
- Team collaboration frameworks: Interface specifications, communication protocols, feedback loops
- Failure mode detection: Reward hacking, calibration collapse, distribution shift under RLEG

**Success criteria:**
- Published elicitation protocols with measured efficiency (expert time per training signal unit)
- Reward structure templates validated across multiple domains
- Team collaboration methodology documented and replicated

**Dependencies:** Phase 1 results demonstrating RLEG value proposition

**Potential collaborators:** Human-computer interaction researchers, organizational behavior specialists, domain-specific institutions

### 10.3 Phase 3: Domain Instantiation (Years 3-5)

**Core question:** What does RLEG look like in specific high-stakes domains?

**Research agenda:**
- Medical RLEG: Clinician feedback on diagnostic outputs, clinical workflow integration
- Legal RLEG: Attorney feedback on legal analysis, case strategy fit
- Engineering RLEG: Domain engineer feedback on technical outputs, system integration
- Financial RLEG: Analyst feedback on market analysis, risk assessment calibration

**Success criteria:**
- At least three domain-specific RLEG implementations
- Documented case studies including team structure, methodology, outcomes
- Domain-specific benchmarks for teleological and mereological fit

**Dependencies:** Phase 2 methodology sufficient for domain adaptation

**Potential collaborators:** Medical schools, law schools, engineering firms, financial institutions

### 10.4 Phase 4: Scaling Solutions (Years 4-6)

**Core question:** How can RLEG overcome expert scarcity?

**Research agenda:**
- Expert-seeded RLAIF: Can AI models trained on expert feedback provide proxy feedback?
- Hierarchical review: Junior reviewers handle routine cases, experts handle edge cases
- Active learning optimization: Uncertainty-based sampling to maximize expert impact
- Transfer learning: Does RLEG in one domain transfer benefits to adjacent domains?

**Success criteria:**
- Demonstrated scaling pathway achieving >10x expert leverage
- Maintained calibration under scaled approaches
- Transfer experiments showing cross-domain benefits

**Dependencies:** Phase 3 successful domain implementations providing training data

**Potential collaborators:** Large-scale ML infrastructure teams, active learning researchers

### 10.5 Phase 5: Theoretical Foundations (Ongoing, Years 1-6)

**Core question:** What formal characterization underlies RLEG effectiveness?

**Research agenda:**
- Formal specification: What information does expert feedback carry that crowdworker feedback cannot?
- Grounding propagation: How does training signal grounding transfer to model behavior?
- Limits of RLEG: What can expert feedback not solve? Where does derivative grounding fail?
- Connection to AIDK framework: How does RLEG relate to structural epistemic limits of LLMs?

**Success criteria:**
- Formal framework distinguishing expert-grounded from crowd-grounded training
- Theoretical predictions validated by empirical results
- Clear articulation of RLEG limits and appropriate deployment constraints

**Dependencies:** Runs parallel to empirical phases; informed by their results

**Potential collaborators:** Philosophy of AI researchers, formal methods specialists, AI safety theorists

### 10.6 Research Program Summary

| Phase | Core Question | Timeline | Key Deliverables |
|-------|--------------|----------|------------------|
| 1. Validation | Does RLEG preserve calibration? | Years 1-2 | Comparative studies, calibration measurements |
| 2. Methodology | How should teams collaborate? | Years 2-4 | Elicitation protocols, reward structures, team frameworks |
| 3. Instantiation | What works in specific domains? | Years 3-5 | Medical, legal, engineering case studies |
| 4. Scaling | How to overcome expert scarcity? | Years 4-6 | RLAIF seeding, active learning, transfer |
| 5. Theory | What formal foundations apply? | Ongoing | Formal framework, grounding propagation theory |

**The programmatic claim:** RLEG is not a single technique to be validated but a research direction requiring sustained multi-phase investigation. This paper provides the conceptual foundation; the research program provides the path to implementation.

---

## 11. Conclusion

### 11.1 Summary
- RLHF frequently produces fluent, engaging, miscalibrated models
- The problem is feedback source, not feedback structure
- RLEG addresses the grounding gap by changing who provides training signal
- The shift from "Feedback" to "Guidance" is substantive: experts provide direction toward purpose, not just correction of errors
- Implementation requires novel team structures: domain experts + AI training specialists
- The methodology for this collaboration does not yet exist as a developed discipline
- A multi-phase research program is required to develop RLEG from concept to deployment

### 11.2 The Core Insight
- Deep Blue didn't understand chess; it inherited grounding through its evaluation function
- AlphaGo didn't understand Go; it inherited grounding through expert-seeded training
- RLEG models don't understand domains; they inherit grounding through expert-shaped training signal
- This is still derivation, but derivation from grounded judgment rather than from ungrounded approval

### 11.3 The Path Forward
- Develop RLEG methodology as a distinct discipline
- Train practitioners who span domain expertise and AI training knowledge
- Build organizational structures that support expert-trainer collaboration
- Deploy RLEG-trained models within appropriate HCAE frameworks
- Pursue the research program outlined in Section 10

### 11.4 Final Observation
- The field is asking "how do we build better reward functions?"
- The deeper question is "who should be providing the feedback?"
- RLEG answers: those with access to the grounding the model cannot reach
- "Guidance" marks the difference: not just expert accuracy, but expert telos—judgment about what the output is *for* and how it fits the *whole* it serves

---

## References

### Calibration and Overconfidence
- Tian, K., Mitchell, E., Zhou, A., Sharma, A., Rafailov, R., Yao, H., Finn, C., & Manning, C. (2023). Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback. *EMNLP 2023*.
- Leng, J., et al. (2024). Taming Overconfidence in LLMs: Reward Calibration in RLHF. *ICLR 2025*.
- OpenAI. (2023). GPT-4 Technical Report. (Calibration findings post-RLHF)

### Factuality and Alignment
- Lin, S., et al. (2024). FLAME: Factuality-Aware Alignment for Large Language Models. *NeurIPS 2024*.
- Schulman, J., et al. (2017). Proximal Policy Optimization Algorithms.

### Expert Feedback and Domain-Specific Training
- OpenAI. (2024). Reinforcement Fine-Tuning (RFT) Documentation.
- CloudFactory. (2025). Reinforced Learning through Expert Feedback (RLEF).
- Daniels-Koch, O. (2022). The Expertise Problem: Learning from Specialized Feedback.

### Execution Feedback (Distinct RLEF Usage)
- Gehring, J., Zheng, K., Copet, J., Mella, V., Cohen, T., & Synnaeve, G. (2024). RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning. *arXiv:2410.02089*. (ICML 2025)

### Calibration Theory
- Kadavath, S., et al. (2022). Language Models (Mostly) Know What They Know.
- Guo, C., et al. (2017). On Calibration of Modern Neural Networks.

### Deep Blue, AlphaGo, and Human-AI Collaboration
- Campbell, M., Hoane, A.J., & Hsu, F. (2002). Deep Blue. *Artificial Intelligence*, 134(1-2), 57-83.
- Newborn, M. (1997). *Kasparov versus Deep Blue: Computer Chess Comes of Age*.
- Silver, D., et al. (2016). Mastering the game of Go with deep neural networks and tree search. *Nature*, 529(7587), 484-489.
- Silver, D., et al. (2017). Mastering the game of Go without human knowledge. *Nature*, 550(7676), 354-359.
- Silver, D., et al. (2018). A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play. *Science*, 362(6419), 1140-1144.

### HCAE Framework
- Longmire, J. (2024). AI Dunning-Kruger (AIDK): Structural Epistemic Limits of Large Language Models.
- Longmire, J. (2024). Human-Curated, AI-Enabled (HCAE) Framework.

### Active Learning and Human-in-the-Loop
- Settles, B. (2012). Active Learning. *Synthesis Lectures on Artificial Intelligence and Machine Learning*.
- Christiano, P., et al. (2017). Deep Reinforcement Learning from Human Preferences.

---

## Revision Notes

**Changes from initial outline based on Perplexity feedback:**

1. Softened universal claims about RLHF calibration degradation to "frequently observed" (Sections 1.2, 2.1, 2.2, 11.1)
2. Added acknowledgment that some base models already exhibit miscalibration (Section 2.1)
3. Merged teleological and mereological grounding into single section with concrete medical/legal examples (Section 3.2)
4. Added explicit FLAME linkage for fluency-factuality evidence (Section 7.2)
5. Connected scalability mitigations to existing active learning and human-in-the-loop literature (Section 9.1)
6. Added FLAME and related citations to references
7. Added contrast citation in Section 2.4 re: approaches using non-expert raters

**Changes based on Grok feedback (AlphaGo integration):**

8. Expanded Section 4 from "The Deep Blue Precedent" to "Historical Precedents: From Deep Blue to AlphaGo"
9. Added complexity escalation argument: Chess → Go → Language, showing RLEG becomes *more* necessary as complexity increases
10. Added fluency-calibration parallel in game AI (Section 4.4): AlphaGo achieved both because training signal was expert-grounded
11. Added self-play limitation analysis (Section 4.5): Language cannot borrow AlphaGo's self-play amplification, making sustained expert grounding more critical
12. Added transfer potential research direction: AlphaZero's generalization suggests RLEG benefits might transfer across domains
13. Added AlphaGo/AlphaZero references (Silver et al. 2016, 2017, 2018)

**Changes for RLEG terminology and research program:**

14. Introduced RLEG (Reinforcement Learning from Expert Guidance) terminology to distinguish from Gehring et al.'s RLEF (Execution Feedback)
15. Added Terminological Note section explaining the Feedback→Guidance distinction and its grounding-axis significance
16. Added Section 3.4 explicitly contrasting RLEG with execution-based RLEF
17. Added Gehring et al. (2024) to references
18. Expanded Section 10 from "Research Directions" to "A Research Program for RLEG" with five phases, timelines, success criteria, dependencies, and collaborator suggestions
19. Updated Abstract to reference research program and RLEG terminology
20. Updated Conclusion to reference research program and explain Guidance significance
