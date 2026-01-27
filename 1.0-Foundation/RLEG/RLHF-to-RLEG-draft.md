# From RLHF to RLEG: Expert Grounding as a Solution to the Fluency-Calibration Tradeoff

**J.D. Longmire**

*Draft v1.0 — January 2025*

---

## Abstract

Reinforcement Learning from Human Feedback (RLHF) produces large language models that are fluent, engaging, and confidently wrong. Recent research documents a persistent tradeoff: optimizing for human approval improves conversational quality while frequently degrading calibration, increasing verbalized overconfidence, and damaging factual reliability. This paper argues that the problem is not reward engineering but feedback source. Standard RLHF relies on crowdworker judgments that can evaluate fluency, tone, and format but cannot evaluate domain accuracy, appropriate uncertainty, or fitness for purpose. We propose RLEG (Reinforcement Learning from Expert Guidance) as an alternative paradigm in which domain experts provide training signal that carries teleological and mereological information crowdworkers cannot access. The shift from "Feedback" to "Guidance" is substantive: feedback is reactive and corrective, addressing whether reasoning was sound; guidance is directional and purposive, grounding outputs in intended function and systemic coherence. The expert evaluates not only whether an output is correct but whether it serves its intended purpose and fits the whole it enters. We analyze the Deep Blue and AlphaGo precedents, where expert grounding enabled superhuman performance in domains of increasing intractability, and argue that RLEG requires analogous team structures: domain experts who provide grounded judgment paired with AI training specialists who translate that judgment into effective reward signal. We identify a novel competency gap—the absence of trained RLEG practitioners who understand both domain requirements and reward shaping—and propose a multi-phase research program for developing this methodology. Finally, we argue that RLEG does not solve the grounding problem at the model level (the system remains derivative) but solves it at the training signal level, propagating expert grounding through the learned distribution. The result is a model that pattern-matches to outputs experts judged as serving the right purpose and fitting the right whole, rather than outputs crowdworkers found engaging.

**Keywords:** reinforcement learning from human feedback; expert guidance; calibration; fluency-accuracy tradeoff; teleology; mereology; grounding; human-AI collaboration; RLEG

---

## Terminological Note

RLEG (Reinforcement Learning from Expert Guidance) should be distinguished from RLEF (Reinforcement Learning from Execution Feedback) introduced by Gehring et al. (2024), which uses automated test execution as feedback signal for code synthesis. The shift from "Feedback" to "Guidance" is deliberate and substantive. Feedback is reactive, corrective, and backward-looking: it tells us that something was wrong. Guidance is directional, purposive, and forward-looking: it tells us what the output is for and where it fits.

RLHF and RLEF both operate primarily on what we might call the vertical axis—improving reasoning quality and correctness. RLEG operates on the grounding axis—ensuring outputs serve their intended purpose and cohere with the wholes they enter. The two approaches are complementary: execution feedback provides grounding where formal verification exists, such as in code, mathematics, and formal logic; expert guidance provides grounding where it does not, including medicine, law, strategy, ethics, and open-ended generation. This paper addresses the latter.

---

## 1. Introduction

### 1.1 The RLHF Success Story

Reinforcement Learning from Human Feedback has transformed the landscape of large language model deployment. The technique, pioneered by Christiano et al. (2017) and refined through subsequent work including Proximal Policy Optimization (Schulman et al., 2017), takes base language models that are capable but unwieldy and shapes them into systems that follow instructions, maintain coherent conversations, and provide responses that users find helpful and engaging.

The commercial success of this transformation cannot be overstated. ChatGPT's explosive adoption, the rapid integration of language models into enterprise workflows, and the emergence of AI assistants as mainstream productivity tools all depend fundamentally on RLHF or similar alignment techniques. Base models, despite their impressive capabilities, produce outputs that users find difficult to work with: they continue text rather than answering questions, they fail to maintain conversational context, and they frequently generate content that is inappropriate or unhelpful for practical use cases. RLHF addresses these limitations by training models to produce outputs that human evaluators prefer.

The standard RLHF pipeline works as follows. First, human evaluators—typically crowdworkers recruited through platforms like Amazon Mechanical Turk or specialized data-labeling services—compare pairs of model outputs and indicate which they prefer. These preference judgments are used to train a reward model that learns to predict human preferences. Finally, the language model is fine-tuned using reinforcement learning to maximize the reward model's scores, effectively training it to produce outputs that would be preferred by the human evaluators.

This pipeline has proven remarkably effective at improving user experience metrics. Models trained with RLHF are more engaging, more likely to follow instructions precisely, and more likely to produce responses that users rate as helpful. The technique has become standard practice across the industry, with variations like Direct Preference Optimization (DPO) and Reinforcement Learning from AI Feedback (RLAIF) building on its foundations.

### 1.2 The Hidden Cost

Beneath the success story, however, lies a troubling pattern. Researchers have documented that the RLHF process frequently degrades model calibration—the correspondence between a model's expressed confidence and its actual reliability. This finding appears across multiple studies and manifests in several distinct phenomena.

First, RLHF-trained models often exhibit verbalized overconfidence regardless of their actual reliability on a given question. Tian et al. (2023) found that while pre-trained language models often show well-calibrated conditional probabilities, RLHF fine-tuning produces models whose probability estimates are poorly calibrated. Their work demonstrated that verbalized confidences—asking the model to express its confidence in words—are often better calibrated than the model's internal probability estimates, but both show degradation compared to base model performance on calibration metrics.

Second, factuality frequently suffers in open-ended generation. Lin et al. (2024), in their work on factuality-aware alignment (FLAME), documented that conventional alignment processes fail to enhance factual accuracy and often lead to increased hallucination. They identified that training on novel information or unfamiliar texts—common in the diverse datasets used for RLHF—can encourage confabulation. Furthermore, the reward functions used in standard reinforcement learning often encourage hallucination by favoring longer, more detailed, and more helpful-seeming responses.

Third, there emerges what might be called the "assertiveness prior": in natural conversation, being helpful and confident dominates over expressing appropriate uncertainty. Users prefer decisive answers to hedged ones, and this preference propagates through the training process. The result is a model that has learned to sound authoritative even when its knowledge is uncertain.

It is important to note that these effects vary with training methodology and model architecture. Not all RLHF implementations produce the same degree of calibration degradation, and some approaches explicitly target calibration preservation. However, the tendency toward miscalibration under standard RLHF is sufficiently documented that it represents a genuine concern for deployment in high-stakes domains.

### 1.3 The Standard Diagnosis

The field has largely treated the fluency-calibration tradeoff as a reward engineering problem. The implicit assumption is that if we could design better reward functions—ones that balance helpfulness with accuracy, or that explicitly penalize overconfidence—we could retain the benefits of RLHF while mitigating its drawbacks.

This perspective has generated productive research. Multi-objective reward functions attempt to balance competing desiderata. Factuality-specific training objectives, as in the FLAME approach, modify the training process to preserve or enhance accuracy. Calibration-aware training explicitly includes calibration metrics in the optimization target. These approaches represent genuine progress and often improve on naive RLHF implementations.

However, this diagnosis may be addressing a symptom rather than a cause. If we examine more carefully what happens during standard RLHF training, we find that the issue may not be how feedback is structured but rather who provides it in the first place.

### 1.4 Our Thesis

This paper argues that the fluency-calibration tradeoff in RLHF stems fundamentally from the nature of the feedback source, not from the structure of the reward function. Crowdworkers can evaluate what they can perceive—fluency, tone, format, engagement, surface-level coherence. They cannot reliably evaluate what requires domain expertise: factual accuracy in specialized fields, validity of technical reasoning, appropriateness of expressed uncertainty given available evidence, or subtle errors that would be apparent to a trained practitioner.

We propose RLEG (Reinforcement Learning from Expert Guidance) as an alternative paradigm in which domain experts provide training signal. This is not merely RLHF with better-qualified evaluators; the shift from "Feedback" to "Guidance" marks a conceptual distinction. Experts provide not just correctness judgments but teleological grounding (does this output serve its intended purpose?) and mereological grounding (does this output fit properly within the system or workflow it enters?). This is information that crowdworkers cannot access regardless of how carefully the task is structured.

Implementing RLEG requires organizational and methodological innovations that do not yet exist as developed disciplines. The expert who can evaluate domain correctness typically lacks knowledge of reward shaping and training dynamics. The AI training specialist who understands how to translate feedback into effective learning signal typically lacks domain expertise. RLEG requires novel team structures that pair these competencies, along with methodologies for their collaboration that have not yet been developed.

This paper develops these claims across several sections. We first examine the empirical evidence for the fluency-calibration tradeoff and its mechanisms. We then articulate the conceptual foundations of RLEG, distinguishing it from both standard RLHF and from execution-based feedback approaches. We analyze historical precedents—specifically Deep Blue and AlphaGo—where expert grounding enabled superhuman performance, drawing lessons for language model training. We discuss the team structures and practitioner competencies that RLEG would require. Finally, we outline a multi-phase research program for developing RLEG from conceptual framework to deployable methodology.

---

## 2. The Fluency-Calibration Tradeoff: Empirical Foundations

### 2.1 Calibration in Base Models

Before examining how RLHF affects calibration, we must understand the baseline. Pre-trained language models—those that have undergone self-supervised learning on large text corpora but not alignment training—often exhibit remarkably well-calibrated conditional probabilities for certain task types. Kadavath et al. (2022), in their study of language model self-knowledge, found that models can meaningfully assess their own reliability across different question types and that this self-assessment correlates with actual performance.

The calibration of base models is not perfect or universal. Some architectures and training regimes produce better-calibrated models than others, and calibration can vary significantly across different types of questions and knowledge domains. Nevertheless, there is substantial evidence that the raw probability distributions learned during pre-training often track correctness more reliably than post-RLHF confidence expressions.

This observation is critical because it suggests that calibration degradation is not inherent to large language models but rather emerges from the alignment process. If base models can achieve reasonable calibration, then the question becomes what about RLHF training disrupts this property.

It should be noted, however, that base models, while often better calibrated, are typically unsuitable for deployment. They lack instruction-following capabilities, tend to continue text in unpredictable directions rather than answering questions directly, and often produce content that is inappropriate for user-facing applications. The practical value of RLHF comes precisely from making models usable—the question is whether this usability must come at the cost of reliability.

### 2.2 Calibration Degradation Post-RLHF

Multiple lines of evidence document calibration degradation following RLHF training. The mechanisms are distinct but reinforce each other.

First, reward models themselves frequently exhibit bias toward high-confidence outputs. When crowdworkers compare model responses, they tend to prefer answers that sound more confident and authoritative. This preference is understandable: in everyday conversation, hedging and uncertainty expressions can signal lack of knowledge or competence. When we ask a question, we want an answer, not a discussion of what the answerer doesn't know. But when this preference is encoded into a reward model, the language model learns to express confidence regardless of its actual reliability.

Second, verbalized overconfidence emerges as trained behavior. Tian et al. (2023) documented this phenomenon systematically, showing that RLHF models exhibit poor calibration in their probability estimates compared to base models. Their finding that verbalized confidences are often better calibrated than raw probabilities suggests that the model has learned to modulate its stated confidence differently from its internal uncertainty representation—a form of learned overconfidence.

Third, the dynamics of conversational engagement favor assertiveness. When a model hedges excessively, users often follow up asking for a direct answer. When a model gives a confident but incorrect answer, users may not notice the error, especially if they lack domain expertise themselves. The reward model captures this asymmetry: the costs of appearing uncertain are immediate (lower preference ratings), while the costs of being confidently wrong are often invisible to the training process.

Quantitative evidence supports these observations. Expected Calibration Error (ECE) typically increases following RLHF training, indicating that expressed confidence and actual accuracy have become less well-matched. Factuality scores on open-ended generation tasks tend to decrease, particularly for questions outside the model's reliable knowledge base. The effect sizes vary across implementations, but the direction is consistent enough to represent a genuine phenomenon rather than an artifact of particular studies.

### 2.3 The Mechanism

Understanding why this degradation occurs requires examining what crowdworkers can and cannot evaluate. The core issue is that the optimization target diverges from the reliability target.

Crowdworkers can reliably evaluate:
- **Fluency**: Is the text grammatically correct and well-structured?
- **Engagement**: Is the response interesting and well-written?
- **Format compliance**: Does the response follow the requested format?
- **Tone appropriateness**: Is the tone suitable for the context?
- **Surface coherence**: Does the response make sense on first reading?

Crowdworkers cannot reliably evaluate:
- **Domain accuracy**: Is this medical/legal/technical information correct?
- **Reasoning validity**: Is the logical structure of this argument sound?
- **Appropriate uncertainty**: Should the model be more or less confident given the available evidence?
- **Subtle errors**: Are there mistakes that require expertise to detect?
- **Knowledge boundaries**: Is the model operating within its reliable knowledge or confabulating?

When the training process optimizes for crowdworker preferences, it optimizes for the first set of criteria. The model learns to produce outputs that appear reliable—fluent, confident, well-structured, engaging—without necessarily learning to be reliable. In fact, because appearing uncertain is penalized while being confidently wrong often goes undetected, the optimization actively pushes against calibration.

The result is a model that has learned to simulate expertise rather than exhibit it. The simulation is often quite convincing, especially to non-experts. But for high-stakes applications where actual reliability matters, this simulation is precisely the problem.

### 2.4 Why Reward Engineering Cannot Fully Solve This

Given this diagnosis, a natural response is to engineer better reward functions. Why not add explicit calibration terms? Why not include factuality objectives? This approach has value—the FLAME work demonstrates that factuality-aware alignment can improve on naive implementations—but it faces fundamental limitations.

The bottleneck is evaluator competence, not reward function design. Consider what it would take to create a reward function that penalizes factual errors:

1. The reward model would need training data that identifies factual errors
2. Creating this training data requires evaluators who can recognize factual errors
3. Recognizing factual errors in specialized domains requires domain expertise
4. Crowdworkers, by definition, lack this expertise

We can create factuality rewards for domains where ground truth is accessible—simple factual questions with verifiable answers, mathematical calculations, code that can be executed. But for the vast space of questions where correctness depends on domain expertise—medical advice, legal analysis, strategic recommendations, complex technical explanations—the crowdworker bottleneck remains.

Similarly, consider calibration rewards. Penalizing confidence-correctness mismatch requires knowing whether answers are correct. For the same reason that crowdworkers cannot evaluate factuality, they cannot evaluate whether expressed confidence is appropriate. They can rate whether confidence expressions feel appropriate, but this is a different property from whether confidence actually matches reliability.

Multi-objective reward approaches help at the margins but do not eliminate the fundamental gap. If one objective (factuality) cannot be reliably measured by the available evaluators, then weighting it in a multi-objective function does not solve the measurement problem. The model may learn to game the proxy metrics that crowdworkers can evaluate while the underlying factuality remains unaddressed.

This analysis leads to a clear conclusion: if we want training signal that reliably reflects domain accuracy, appropriate uncertainty, and fitness for purpose, we need evaluators who can assess these properties. We need experts.

---

## 3. RLEG: Conceptual Foundations

### 3.1 The Expert Difference

Domain experts can evaluate what crowdworkers cannot. This is not a matter of training or instruction—it reflects genuine asymmetries in knowledge and judgment that years of specialized education and practice create.

An experienced physician evaluating a diagnostic summary can assess whether the listed considerations are medically appropriate, whether important possibilities have been missed, whether the reasoning from symptoms to conclusions is valid, and whether the expressed confidence matches the actual state of medical knowledge on the topic. A crowdworker, regardless of how carefully instructed, cannot perform this evaluation. They can assess whether the summary sounds medical, whether it is well-organized, whether the language is appropriate—but not whether it would serve a patient well.

An attorney evaluating legal analysis can assess whether the cited precedents are relevant, whether the reasoning extends them appropriately, whether important counterarguments have been considered, and whether the overall strategy serves the client's interests. A crowdworker can evaluate whether the analysis sounds legal, whether it is clearly written, whether it addresses the question asked—but not whether it would survive scrutiny in court.

This asymmetry is the foundation of RLEG. By changing who provides training signal—from crowdworkers who can evaluate appearance to experts who can evaluate substance—we change what the model learns to optimize. Instead of learning to appear reliable, the model learns from evaluators who can assess actual reliability.

### 3.2 Beyond Accuracy: Teleological and Mereological Grounding

The advantage of expert evaluation extends beyond mere accuracy. Experts provide two forms of grounding that crowdworkers cannot access, and the "Guidance" in RLEG signifies this grounding-axis evaluation.

**Teleological grounding** concerns purpose-fitness. The expert evaluates not just whether an output is correct but whether it serves its intended function. A diagnostic summary might be factually accurate but useless for clinical decision-making because it fails to prioritize actionable information. A legal analysis might correctly state the law but fail to serve the client's actual strategic needs. A technical explanation might be accurate but pitched at the wrong level for its intended audience.

These are teleological failures—failures of purpose-fitness—that require understanding what the output is for. Crowdworkers, who encounter outputs without context of use, cannot evaluate teleological fit. Experts, who understand how outputs will be used in actual practice, can assess whether they serve their intended purpose.

Consider a concrete example from medical practice. A radiologist reviewing an AI-generated diagnostic summary evaluates not just accuracy but clinical workflow integration. Does this summary serve triage, treatment planning, or documentation? Different purposes require different information structures. A triage summary should highlight urgent findings; a treatment planning summary should connect findings to therapeutic options; a documentation summary should be comprehensive and defensible. The same accurate information, structured differently, might succeed for one purpose and fail for another. Expert evaluation captures this teleological dimension.

**Mereological grounding** concerns part-whole fit. The expert evaluates not just whether an output is correct in isolation but whether it integrates properly with the system it enters. A component that is locally correct might create integration failures at the system level—conflicts with other components, violations of assumptions that other parts of the system rely on, or failures to maintain invariants that the whole requires.

Consider a legal example. An attorney evaluating AI-generated contract analysis assesses not just whether the analysis of a particular clause is correct but whether it coheres with the full case context. How does this clause interact with other provisions? Does the analysis account for the overall deal structure? Does it serve the client's position in light of the broader negotiation? These are mereological considerations—the part must fit the whole—that require understanding beyond the isolated component.

Crowdworkers, who evaluate outputs without access to the systems they enter, cannot assess mereological fit. Experts, who understand how outputs function within larger wholes, can evaluate whether the part serves the whole it enters.

Together, teleological and mereological grounding constitute what the "Guidance" in RLEG represents. It is not merely correction of errors but direction toward purpose and coherence—grounding that transcends accuracy to address function.

### 3.3 What RLEG Does and Does Not Solve

It is important to be precise about the claims being made. RLEG does not solve the grounding problem at the model level. The language model, after RLEG training, still lacks direct access to reality. It still cannot verify facts against the world, still cannot perceive causation, still does not understand in the way that human experts understand. The model remains a derivative system—a sophisticated pattern-matcher operating on learned distributions.

What RLEG solves is grounding at the training signal level. By using experts rather than crowdworkers as the source of training signal, the grounding that experts possess propagates through the learned distribution. The model learns to produce outputs that experts—with their access to domain truth, their understanding of purpose, their grasp of systemic fit—would approve.

This is still derivation, but derivation from a different source. A model trained on crowdworker preferences inherits the limitations of crowdworker judgment: it learns to produce outputs that appear reliable to non-experts. A model trained on expert judgment inherits the standards of expert evaluation: it learns to produce outputs that would satisfy those who can actually assess reliability.

The result is a model that pattern-matches to outputs experts judged as serving the right purpose and fitting the right whole, rather than outputs crowdworkers found engaging. The model does not achieve expert understanding, but it approximates expert-validated behavior. For many practical purposes, this approximation is what matters.

### 3.4 RLEG vs. RLEF (Execution Feedback)

RLEG should be distinguished from RLEF (Reinforcement Learning from Execution Feedback), recently introduced by Gehring et al. (2024) for code synthesis. RLEF uses automated test execution as the feedback signal: code is evaluated by whether it passes test cases, providing ground truth that does not depend on human judgment.

RLEF is a powerful approach for domains where formal verification exists. Code can be executed; tests either pass or fail. Mathematical proofs can be checked by automated theorem provers. Formal logic admits mechanical verification. In these domains, the ground truth is accessible without human intervention, and execution feedback provides reliable training signal at scale.

However, many domains lack this property. Medical diagnosis cannot be "executed" against reality in the way that code can be compiled and run. Legal analysis does not have test cases that provide unambiguous success or failure signals. Strategic recommendations, ethical judgments, complex explanations—these produce effects in the world, but effects that are delayed, confounded, and not reducible to pass/fail evaluation.

RLEG addresses precisely these domains—those where formal verification is unavailable and ground truth depends on expert judgment. The two approaches are complementary. RLEF provides grounding where automation suffices; RLEG provides grounding where it does not. Together, they span a wider range of domain types than either alone.

It is worth noting that RLEF, despite using automated feedback, still often requires human expertise in designing test suites and evaluation criteria. The choice of what to test reflects human judgment about what matters. In this sense, even execution-based approaches carry implicit expert input. RLEG makes this expert input explicit and extends it to domains where execution-based evaluation is unavailable.

---

## 4. Historical Precedents: From Deep Blue to AlphaGo

### 4.1 Deep Blue: Expert Grounding in Tractable Domains

The 1997 victory of IBM's Deep Blue over world chess champion Garry Kasparov represents a landmark in AI history. Less commonly appreciated is what made that victory possible: a collaboration between domain experts and engineers that prefigures the RLEG paradigm.

Deep Blue was not the creation of IBM engineers alone. As documented by Campbell, Hoane, and Hsu (2002), the system incorporated extensive input from chess grandmasters who provided domain grounding that the engineers could not have supplied. This contribution took several forms.

First, grandmasters curated the opening book—the database of established opening sequences and their evaluations. Opening theory in chess represents centuries of accumulated expert knowledge about which positions are advantageous and why. The grandmasters selected which openings to include, evaluated novel positions, and ensured that the opening book reflected sound chess understanding. This was teleological grounding: which sequences serve the goal of achieving favorable positions?

Second, grandmasters provided input into the evaluation function weights. Chess evaluation functions assign numerical scores to positions based on features like material balance, piece activity, pawn structure, and king safety. The relative importance of these features—how much to weight a passed pawn versus an open file versus king vulnerability—reflects chess judgment that only experts possess. The grandmasters calibrated these weights based on their understanding of what makes positions good or bad. This was mereological grounding: how do the parts (individual features) combine to constitute positional value (the whole)?

Third, grandmasters contributed endgame knowledge. Endgame theory provides exact evaluations of simplified positions, determining which endgames are won, drawn, or lost with perfect play. This knowledge, accumulated over centuries of analysis, was encoded into Deep Blue's endgame databases. The grandmasters validated that these databases reflected correct chess understanding.

What the engineers contributed was equally essential but categorically different. They translated expert judgment into computable form. They designed the search algorithms that leveraged the evaluation function to explore vast numbers of positions. They implemented the hardware and software that made the computation tractable. They optimized within the constraints that expert judgment defined.

Neither group alone could have defeated Kasparov. The engineers lacked the chess understanding to create meaningful evaluations; any evaluation function they designed without expert input would likely have had critical blind spots. The grandmasters lacked the computational expertise to implement their knowledge at the scale and speed required to match Kasparov's calculating power.

Deep Blue thus represents what we might call proto-RLEG: human-curated, AI-enabled before the terminology existed. The system achieved superhuman performance not by developing genuine understanding but by inheriting grounding through its evaluation function. Deep Blue never "understood" chess—it knew nothing about strategy, psychology, or the meaning of the game. But it produced moves that the experts who shaped it would recognize as strong, and that proved sufficient to defeat the world champion.

### 4.2 AlphaGo: Expert Grounding Scales to Intractable Domains

If Deep Blue demonstrated expert grounding in a tractable domain, AlphaGo (Silver et al., 2016) demonstrated that the approach scales to domains previously considered intractable. Go presented challenges that pure search could not overcome: a branching factor of approximately 250 legal moves per position compared to roughly 35 in chess, and a game length that makes exhaustive analysis impossible even with massive computational resources.

The Deep Blue approach—hand-crafted evaluation functions calibrated by experts—could not scale to Go. The features that matter in Go are more subtle, more contextual, and less amenable to explicit enumeration than those in chess. Expert Go players could not articulate their evaluation heuristics in a form that engineers could encode into evaluation functions.

AlphaGo's innovation was to learn the evaluation function from data rather than hand-crafting it. But crucially, the initial version of AlphaGo learned from expert games. The policy network, which predicted move probabilities, was trained on approximately 30 million positions from games played by strong human players. The value network, which evaluated position quality, was trained to predict game outcomes from expert-level play.

This training process embedded expert grounding into the learned representations. The networks learned to approximate what strong human players would choose (policy) and what strong human players would consider good positions (value). The grounding was implicit rather than explicit—learned from examples rather than encoded as rules—but it was still grounding derived from expert judgment.

AlphaGo Zero (Silver et al., 2017) demonstrated that this expert-seeded training could be transcended. Starting from random play, using only the rules of Go and self-play reinforcement learning, AlphaGo Zero converged on superhuman performance without exposure to human games. This result is striking and has sometimes been interpreted as showing that expert input is unnecessary.

This interpretation misses a crucial point. Even in self-play, the system learned to approximate what strong play would produce. The game of Go has an objective win condition, and self-play against an improving opponent drives toward strategies that achieve that condition. The system was still grounded in expert-recognizable strength—validated by its ability to defeat professional players and by the quality of play that human experts analyzed and admired.

Furthermore, the benchmark for success remained alignment with expert-recognized standards. AlphaGo's strength was validated by human experts who could evaluate game quality. When AlphaGo Zero played Move 37 in its second game against Lee Sedol—a move that shocked professional commentators—it was experts who recognized the move's brilliance in retrospect. Without expert evaluation, there would be no way to verify that the system had achieved genuine strength rather than discovering some degenerate strategy that exploits weaknesses in its own training process.

### 4.3 The Complexity Escalation: Why Language Requires RLEG

The progression from chess to Go to language reveals an escalating complexity that makes expert grounding increasingly essential.

Chess is moderately tractable: manageable branching factor, well-defined evaluation features, objective win conditions. Expert grounding could be encoded directly into hand-crafted evaluation functions. The Deep Blue approach—explicit expert input translated into computable form—sufficed.

Go is astronomically complex: branching factor that defeats exhaustive search, positional features too subtle for explicit enumeration. But it retains an objective win condition—whoever controls more territory wins. This objective allowed self-play reinforcement learning to discover superhuman strategies, with expert games providing an initial seed for the learning process.

Language is unbounded and contested: infinite branching factor (any sequence of words is possible), no objective win condition (success depends on user intent, context, and purpose), and correctness criteria that vary across domains and applications. There is no analogue to Go's self-play loop because there is no automatic signal of success. A language model playing against itself does not converge on truth or quality; it converges on fluent self-consistency, which may be entirely disconnected from reality.

This comparison illuminates why crowdworker RLHF is even less adequate for language than hand-crafted heuristics would be for Go. Go's complexity forced a leap from hand-crafted heuristics to learned intuitions; hand-crafting simply could not scale. Language is more complex still, with the additional complication that success criteria are contested and teleology-heavy. Crowdworkers can judge surface qualities—fluency, engagement, format—but they lack the teleological and mereological grounding that would be needed to evaluate whether outputs serve their intended purpose and fit the wholes they enter.

The argument crystallizes as follows:
- In tractable domains with objective success criteria (chess), expert grounding plus engineering translation sufficed
- In intractable domains with objective success criteria (Go), expert-seeded learning scaled to superhuman performance
- In intractable domains with contested success criteria (language), crowdworker preferences are structurally inadequate
- RLEG is not an incremental improvement; it addresses a category of problem that RLHF cannot reach

### 4.4 Fluency and Calibration in Game AI: A Parallel

AlphaGo's development offers an instructive parallel to the fluency-calibration tradeoff in language models. AlphaGo achieved both what might be called "fluency"—moves that appeared natural, creative, and elegant to human experts—and calibration—accurate assessment of win probability throughout the game. The value network rarely expressed high confidence in positions that were objectively lost.

This combination was possible because the training signal was grounded in genuine expertise. Whether through learning from human games or through self-play against improving opponents, AlphaGo learned to pursue what experts would recognize as strong play. It was not optimizing for what observers would find entertaining or surprising but for what would actually win games.

Consider the counterfactual: what if AlphaGo had been trained on preferences from casual observers who knew the rules of Go but lacked expertise? Such observers might prefer "exciting" games with dramatic captures and surprising territorial swings. They might rate as superior the games that provided entertainment value rather than those that demonstrated strategic depth. Optimizing for these preferences could have produced a system that played flashy but unreliable Go—one that appeared strong to non-experts while having critical strategic weaknesses that strong players would exploit.

This counterfactual mirrors the RLHF situation. Language models optimized for crowdworker preferences learn to produce outputs that appear reliable to non-experts: confident, well-structured, engaging. But these surface properties can mask underlying problems that only experts would detect. The parallel suggests that the solution is analogous: ground training in expert judgment rather than non-expert preferences.

### 4.5 The Self-Play Limitation: What Language Cannot Borrow

AlphaGo achieved superhuman performance through self-play reinforcement learning, raising the question: could language models follow a similar path? The answer reveals a critical limitation.

Self-play worked for Go because of three properties:
1. **Clear win condition**: Game outcome provides unambiguous reward signal
2. **Closed system**: Rules are fully specified; no external world to model
3. **Unlimited data**: Self-play generates arbitrary amounts of training data with automatic ground truth

Language lacks all three properties:
1. **No automatic success signal**: There is no "win" for open-ended generation; success depends on purpose, context, and external evaluation
2. **Open world**: Language refers to an external reality that the model cannot access for verification
3. **No ground truth generation**: Self-play in language produces text, but there is no automatic oracle to evaluate that text's quality

This analysis has important implications for RLEG. AlphaGo could seed learning with expert games and then amplify through self-play, eventually transcending human play quality. RLEG for language cannot rely on this amplification pathway. Expert grounding must be more directly sustained throughout training because there is no self-play substitute.

This constraint makes the expert-trainer collaboration methodology discussed in subsequent sections even more critical. Where AlphaGo could use expert games as a seed and then learn autonomously, RLEG requires ongoing expert involvement. The scaling challenges are real, but they cannot be circumvented by hoping for a self-play breakthrough.

### 4.6 Derivative Systems with Inherited Grounding

Both Deep Blue and AlphaGo were derivative systems. Neither understood the games they played. Deep Blue had no concept of strategy, no appreciation for chess's aesthetic qualities, no understanding of why certain positions are superior to others. It evaluated positions using functions that humans had designed and tuned. AlphaGo similarly lacked understanding—it learned patterns from data without grasping their significance. It could not explain its moves or reason about chess principles; it simply produced outputs consistent with its learned distributions.

Yet both achieved superhuman performance. They did so by inheriting grounding through expert-shaped training signal. The grounding that the grandmasters possessed—their understanding of positional quality, their appreciation of strategic depth—propagated into Deep Blue's evaluation function. The grounding implicit in expert Go games—what constitutes good shape, sound strategy, winning play—propagated into AlphaGo's learned networks.

This is the RLEG thesis in miniature. The language model, after RLEG training, will not understand domains in the way experts understand them. It will remain a derivative system, pattern-matching to learned distributions. But if those distributions are shaped by expert judgment rather than crowdworker preferences, the model will pattern-match to outputs that experts would approve—outputs that are actually reliable, not merely appearing reliable.

Derivation from expert grounding is categorically different from derivation from surface preferences. Both produce derivative systems, but the quality of what is inherited differs fundamentally. RLEG does not solve the grounding problem at the model level, but it solves it at the training signal level, and for practical purposes, this may be what matters.

---

## 5. The RLEG Team Structure

### 5.1 Why a Single Expert Is Insufficient

The analysis thus far might suggest a simple solution: replace crowdworkers with domain experts. Hire physicians to evaluate medical outputs, attorneys to evaluate legal analysis, engineers to evaluate technical content. This approach is directionally correct but practically insufficient.

Domain expertise does not automatically translate into effective training signal. An expert who can recognize a correct diagnosis may not know how to structure feedback in a way that produces intended learning dynamics. Expert judgment is often holistic and intuitive—physicians recognize good clinical reasoning without necessarily being able to articulate what features they are responding to. Translating this holistic judgment into the granular feedback that reward model training requires is a nontrivial task.

Furthermore, naive expert feedback may produce unintended model behavior. If an expert consistently penalizes a particular type of error while ignoring others, the model may learn to avoid that error type while becoming more prone to the ignored errors. If expert feedback implicitly rewards certain surface features that correlate with quality in the training data but not in general, the model may learn to exploit these features. These dynamics—familiar to machine learning practitioners as forms of reward hacking—are not obvious to domain experts without training in machine learning.

Finally, expert time is expensive and limited. If experts provide feedback inefficiently—evaluating cases that provide little training signal, spending time on aspects the model has already learned—the approach becomes practically infeasible. Effective use of expert time requires understanding of active learning, uncertainty sampling, and training dynamics that domain experts typically lack.

### 5.2 Why a Single AI Trainer Is Insufficient

The complementary limitation holds for AI training specialists. They understand reward shaping, know how to structure feedback for effective learning, can monitor for reward hacking and distribution shift, and can design elicitation protocols that extract information efficiently. But they lack the domain knowledge to evaluate whether outputs are actually correct.

An AI trainer working on medical RLEG cannot assess whether a diagnostic summary is clinically sound. They cannot judge whether appropriate conditions have been considered, whether the reasoning from symptoms to conclusions is valid, whether expressed confidence matches the actual state of medical knowledge. They can structure the training process, but they cannot evaluate the content.

This creates a fundamental gap. The trainer can observe that the reward model is learning, that calibration metrics are shifting, that the model's behavior is changing—but they cannot tell whether these changes represent progress toward reliable medical reasoning or convergence on some other property that happens to correlate with the feedback they are able to observe.

Training without grounding optimizes the wrong target. The trainer may successfully optimize their observable metrics while missing the actual goal. This is precisely analogous to the crowdworker problem—optimizing for what can be measured rather than what matters—but at a different level of the system.

### 5.3 The Required Collaboration

RLEG requires genuine collaboration between domain experts and AI training specialists. Each brings essential competencies that the other lacks, and the combination produces capabilities neither possesses alone.

The domain expert contributes:
- **Correctness judgment**: Is this output factually accurate and reasoning valid?
- **Purpose evaluation**: Does this output serve its intended function?
- **Whole-fit assessment**: Does this output integrate properly with the systems it enters?
- **Calibration judgment**: Is the expressed confidence appropriate given what is known?
- **Consequence weighting**: How serious are different types of errors?

The AI training specialist contributes:
- **Reward structure design**: How should feedback be structured for effective learning?
- **Elicitation protocol development**: How can expert judgment be extracted efficiently?
- **Reward hacking detection**: Is the model learning the intended behavior or gaming the feedback?
- **Learning dynamics monitoring**: Is training progressing appropriately?
- **Efficiency optimization**: How can expert time be used most effectively?

Neither set of contributions is reducible to the other. Domain judgment cannot be automated without solving the grounding problem that RLEG aims to address. Training expertise cannot be replaced with domain knowledge because it reflects understanding of learning systems that is independent of any particular domain.

### 5.4 The Interface Between Them

For collaboration to succeed, the interface between expert and trainer must be carefully designed. The expert must communicate information that the trainer can translate into training signal, and the trainer must provide feedback that helps the expert understand what the model is learning.

What the expert needs to communicate includes:
- **Category of error**: Not just "wrong" but what type of error—factual inaccuracy, reasoning failure, inappropriate confidence, missing consideration, poor integration
- **Magnitude of error**: How serious is this mistake? Would it harm a patient, lose a case, cause a system failure?
- **Direction of improvement**: What would a better response look like? What is missing, what should be removed, what should be rephrased?
- **Stakes involved**: What are the consequences of this type of error in practice?
- **Calibration appropriateness**: Given what is knowable, is the expressed confidence appropriate?

What the trainer needs to provide includes:
- **Elicitation protocols**: Structured interfaces that extract the needed information from experts efficiently
- **Reward translations**: Methods for converting expert judgment into training signal
- **Learning feedback**: Information about what the model is actually learning from the expert's feedback
- **Reward hacking alerts**: Detection when the model appears to be gaming the feedback rather than learning intended behavior
- **Efficiency feedback**: Guidance on which cases provide most training value for expert evaluation

### 5.5 Precedent: Software Development

The required collaboration has precedent in software development, where business analysts and engineers collaborate through structured interfaces despite lacking each other's expertise.

Business analysts understand the domain—what users need, how processes work, what outcomes matter. Engineers understand implementation—how to build systems that achieve desired outcomes. Neither can do the other's job, but effective collaboration produces software that meets genuine needs.

The collaboration succeeds through structured interfaces:
- **Requirements elicitation**: Structured processes for extracting and documenting what is needed
- **User stories**: Standardized formats for communicating requirements
- **Acceptance criteria**: Verifiable conditions that determine whether implementation succeeds
- **Iterative feedback**: Continuous loops where analysts evaluate implementations and engineers refine based on evaluation

RLEG requires analogous methodology. The elicitation protocols, feedback formats, and iteration loops that enable software development collaboration need parallels for expert-trainer collaboration in machine learning. These methodologies do not currently exist as developed disciplines; their development is part of the research program that RLEG requires.

---

## 6. The RLEG Practitioner: A Missing Role

### 6.1 The Competency Gap

A striking feature of the current landscape is the absence of practitioners trained for RLEG. No current educational program produces professionals with the combined competencies that RLEG requires. Domain experts—physicians, attorneys, engineers—receive no training in machine learning or reward shaping. AI engineers and researchers receive no deep training in specialized domains. The intersection is largely unpopulated.

This gap is not merely an educational oversight; it reflects the novelty of the challenge. RLHF using crowdworkers does not require specialized domain knowledge because the evaluation task is designed to be accessible to non-experts. The crowdworker's job is to assess which of two responses seems better—a judgment that requires only general literacy and following instructions. The RLEG evaluator's job is fundamentally different: to assess whether an output is actually correct and fit for purpose, which requires expertise that takes years to develop.

The gap creates a practical barrier to RLEG implementation. Organizations that want to improve their language models' performance in specialized domains face a choice between experts who cannot structure effective training and trainers who cannot evaluate domain correctness. Neither option works.

### 6.2 What RLEG Practitioners Would Need to Know

Bridging this gap requires practitioners with hybrid competencies. The ideal RLEG practitioner would possess:

**Domain knowledge sufficient for evaluation**: This need not be full expert-level mastery, but it must include enough depth to evaluate outputs meaningfully. For some domains, this might mean practitioners who are themselves domain experts with additional training in AI. For others, it might mean practitioners with sufficient domain exposure to work effectively under expert supervision, serving as intermediaries who can translate between expert judgment and training process.

**Understanding of reward shaping**: How does feedback structure affect learned behavior? What are the dynamics of reward model training? How do different feedback formats translate into different learning outcomes? This understanding is essential for designing feedback that produces intended behavior.

**Knowledge of failure modes**: What is reward hacking? How does distribution shift affect model behavior? What causes calibration collapse? How can these problems be detected and mitigated? Without understanding of failure modes, practitioners cannot design robust training processes.

**Elicitation skills**: How can expert judgment be extracted efficiently? What questions reveal the most useful information? How can holistic expert judgment be decomposed into learnable components? Effective elicitation is essential for making RLEG practical at scale.

**Translation ability**: How can expert judgment be converted into effective training signal? This is perhaps the core RLEG skill—bridging between what experts can say and what training processes can learn from.

### 6.3 Training Pathways

Several pathways could produce RLEG practitioners:

**Domain experts with AI supplementation**: Experts in medicine, law, engineering, or other fields could receive additional training in machine learning and reward shaping. This pathway has the advantage of starting with deep domain knowledge, which is harder to acquire than AI training knowledge. Medical schools, law schools, and engineering programs could add AI training curricula for students interested in human-AI collaboration.

**AI engineers with domain immersion**: Machine learning practitioners could receive extended training in specific domains. This pathway is more challenging because domain expertise typically requires years of study and practice, but intensive domain exposure could produce practitioners with sufficient knowledge to work under expert supervision.

**New graduate programs**: Universities could create interdisciplinary programs specifically focused on human-AI collaboration in specialized domains. Such programs would combine technical AI training with domain specialization, producing graduates prepared for RLEG work from the start.

**Professional certification**: Industry bodies could develop certification programs for RLEG practitioners, combining assessment of both domain knowledge and AI training expertise. Such certification could help organizations identify qualified practitioners and create career pathways for this emerging role.

### 6.4 Organizational Implications

RLEG teams represent a new organizational form, neither traditional machine learning engineering nor traditional domain practice. Their placement within organizations raises questions that do not have obvious answers.

Should RLEG teams report to AI leadership or domain leadership? Both have legitimate claims, and the answer may depend on organizational context. What is clear is that RLEG teams need authority and resources from both domains—access to training infrastructure and data from AI, access to expert time and evaluation from domain practice.

What are the incentive structures for RLEG work? Traditional domain practice rewards expertise directly. Traditional AI engineering rewards model performance on standard benchmarks. RLEG requires a different value proposition: improving model reliability in specialized domains where standard benchmarks may not apply. Organizations need to develop incentive structures that recognize this distinct contribution.

How should RLEG quality be measured? Standard ML metrics may not capture what RLEG aims to achieve. Benchmark performance may be irrelevant if the benchmark does not reflect domain-specific requirements. New metrics—expert approval rates, calibration within domains, performance on domain-specific evaluations—may be needed.

These organizational questions require empirical investigation. Different structures may work for different domains and organizations. What is clear is that RLEG implementation requires organizational innovation, not just technical innovation.

---

## 7. Maintaining Fluency Under RLEG

### 7.1 The Risk

A natural concern about RLEG is that optimizing hard for expert approval may sacrifice fluency. If the training signal comes from domain experts focused on correctness and purpose-fitness, the model may learn to produce outputs that satisfy experts but fail to meet users' expectations for accessibility and engagement.

This risk is real. Expert discourse in specialized domains often uses technical vocabulary, assumes background knowledge, and prioritizes precision over accessibility. An attorney writing for other attorneys uses different language than one writing for clients. A physician documenting for medical records uses different structure than one explaining to patients. If RLEG training signal comes primarily from experts evaluating for other experts, the model may learn expert register at the cost of general usability.

Outputs that are technically correct but stilted, inaccessible, or off-putting may fail in practice even when they satisfy domain requirements. User adoption depends on perceived helpfulness, which includes not only accuracy but fluency, engagement, and accessibility. An RLEG-trained model that users find difficult to work with may not deliver value despite its improved reliability.

### 7.2 Evidence That the Tradeoff May Be Softer Than Assumed

Fortunately, evidence suggests that the fluency-accuracy tradeoff may be softer than feared. Lin et al. (2024), in their FLAME work, demonstrated that factuality and fluency can improve together when training objectives are structured appropriately. Their factuality-aware alignment produced models that were more accurate while maintaining or improving fluency ratings.

This finding suggests that fluency and accuracy are not necessarily in tension. When models produce inaccurate responses, they are often not more fluent as a result—they are simply wrong while being equally readable. The perceived tradeoff may arise from optimization pressure that pushes toward confident-sounding but unreliable outputs, not from any inherent tension between quality dimensions.

The intuition is as follows: truly expert outputs in most domains are both accurate and clear. Expert physicians can explain diagnoses in accessible language. Expert attorneys can communicate legal analysis to clients. Expert engineers can translate technical content for non-technical audiences. Expertise includes communication skill, not just domain knowledge.

If RLEG training includes experts who value communication alongside correctness—and if training signal rewards accessible accuracy rather than inaccessible precision—the model may learn to produce outputs that satisfy both criteria. The tradeoff sharpens when objectives compete directly; it softens when they are structured as complementary.

### 7.3 Proposed Architecture: Fluency as Constraint, Grounding as Objective

Based on this analysis, we propose an architecture that treats fluency as a constraint to be maintained while optimizing for expert-judged grounding. Several implementations are possible.

**Staged training** could apply RLEG in a first phase, establishing domain accuracy, purpose-fitness, and appropriate calibration, followed by a second phase of fluency optimization within the bounds established by RLEG. The first phase ensures the model learns what constitutes correct, well-calibrated, purpose-fit outputs; the second phase adjusts presentation for accessibility while preserving the learned quality dimensions.

**Composite rewards** could combine expert approval as a hard constraint with fluency as a soft optimization target. The model would be prevented from producing outputs that experts reject while being encouraged to maximize fluency among expert-approved options. This approach maintains grounding while allowing fluency optimization within the grounded space.

**Multi-domain expert evaluation** could include communication experts alongside domain experts. Medical RLEG might include both clinicians (evaluating accuracy) and patient communication specialists (evaluating accessibility). Legal RLEG might include both attorneys (evaluating legal correctness) and client relations specialists (evaluating client-appropriate communication). This approach builds communication quality directly into the expert evaluation.

### 7.4 The Weighting Problem

Any architecture that balances fluency and accuracy must confront the weighting problem: how much fluency loss is acceptable for how much accuracy gain? This is not a technical question with a technical answer; it depends on domain context and deployment purpose.

In high-stakes applications where errors have serious consequences—medical diagnosis, legal advice, safety-critical engineering—accuracy should likely dominate. Users in these contexts may accept less accessible outputs in exchange for greater reliability. They are presumably seeking expert guidance, and expert-register outputs may even signal the quality they desire.

In lower-stakes applications where engagement and accessibility are primary values—consumer information, entertainment, casual assistance—fluency may deserve more weight. Users expect accessible, engaging responses, and overly technical outputs may fail even if they are correct.

Between these extremes lies a large space where weighting decisions are genuinely difficult. The RLEG methodology should include explicit mechanisms for specifying fluency-accuracy tradeoffs appropriate to the domain and use case. This specification is itself a form of teleological grounding: determining what balance of qualities serves the output's intended purpose.

---

## 8. Calibration-Preserving RLEG

### 8.1 Calibration as Explicit Training Objective

Standard RLHF often treats calibration as an afterthought if it addresses calibration at all. Reward models are trained to predict human preferences, and preferences do not reliably encode calibration information. Crowdworkers cannot assess whether expressed confidence is appropriate because they cannot assess whether answers are correct.

RLEG opens the possibility of treating calibration as an explicit training objective. Experts can evaluate not just whether an output is correct but whether the expressed confidence matches the output's reliability. "This answer is correct, and the model's confidence is appropriate" differs from "this answer is correct, but the model is more confident than it should be given the difficulty of the question." This distinction, invisible to crowdworkers, is accessible to experts.

By structuring RLEG training to reward confidence-correctness alignment, we can build calibration directly into the training process. The model learns not just to produce correct outputs but to express appropriate confidence in its outputs—more confident when answers are clear and well-supported, more hedged when answers are uncertain or when the question lies near the boundaries of reliable knowledge.

### 8.2 Expert Calibration Judgment

What does it mean for an expert to evaluate calibration? The expert's judgment answers a counterfactual: "Given what is knowable about this question, should a reliable system be this confident in its answer?"

This judgment requires several forms of knowledge that experts possess:
- **Epistemic landscape**: What is well-established versus contested in the domain? What questions have clear answers versus open disagreement among experts?
- **Difficulty assessment**: How hard is this particular question? Does it require straightforward knowledge recall, or complex reasoning under uncertainty?
- **Evidence quality**: What evidence supports this answer? How strong is that evidence? What are the limits of what the evidence can establish?
- **Known unknowns**: What aspects of this question remain uncertain even with full domain knowledge?

Crowdworkers lack this knowledge and therefore cannot evaluate calibration meaningfully. They can assess whether confidence expressions feel appropriate—whether the model sounds appropriately uncertain—but this is a fluency judgment, not a calibration judgment. Expert evaluation provides the actual calibration information that training requires.

### 8.3 Proposed Reward Components

Based on this analysis, we propose a multi-component reward structure for calibration-preserving RLEG:

**Accuracy reward**: Is the output correct? This component evaluates factual accuracy and reasoning validity, the primary focus of domain expertise.

**Calibration reward**: Does expressed confidence match reliability? This component evaluates whether the model's confidence expressions are appropriate given the correctness and difficulty of the question. Overconfidence in wrong answers and underconfidence in right answers are both penalized.

**Purpose reward**: Does this output serve its intended function? This component evaluates teleological fit—whether the output is appropriate for its intended use.

**Coherence reward**: Does this output fit properly with the whole it enters? This component evaluates mereological fit—whether the output integrates well with surrounding context and systems.

**Fluency reward**: Is this output accessible and well-formed? This component maintains communication quality as a secondary objective.

The weighting across these components should prioritize calibration and accuracy while treating fluency as a constraint. Purpose and coherence rewards capture the teleological and mereological dimensions that distinguish RLEG from mere correctness feedback.

### 8.4 Detecting Calibration Collapse

Even with calibration-aware training, monitoring is essential. Models can exhibit calibration collapse—a drift toward uniform confidence that ignores question difficulty—as an unintended consequence of training dynamics.

Detection requires monitoring confidence distributions across training. If the model becomes uniformly confident (or uniformly uncertain) regardless of question type and difficulty, calibration is collapsing. Similarly, if the relationship between expressed confidence and actual accuracy breaks down over training, something is going wrong.

Expert spot-checks on uncertainty-appropriate cases provide a qualitative complement to quantitative monitoring. Experts can evaluate whether the model is expressing appropriate uncertainty on questions that should elicit hedged responses. If the model becomes confidently wrong on genuinely difficult questions, this signals calibration problems that aggregate metrics might miss.

The RLEG practitioner—the hybrid expert in both domain and training dynamics—is essential for effective calibration monitoring. They can interpret calibration metrics in domain context, recognizing when statistical patterns indicate genuine problems versus domain-appropriate behavior.

---

## 9. Limitations and Open Questions

### 9.1 Scalability

Expert time is expensive and scarce. RLEG cannot scale like crowdworker RLHF, where large pools of inexpensive labor can generate massive amounts of training data. This scalability limitation is real and constrains where RLEG can be practically applied.

Several approaches might mitigate the limitation:

**Expert-seeded RLAIF**: Train AI models on expert feedback, then use these expert-aligned AI models to provide proxy feedback for further training. The initial expert investment pays off through AI-mediated scaling. This approach trades some grounding quality for scalability, and the quality degradation requires empirical investigation.

**Hierarchical review structures**: Junior reviewers handle routine cases; senior experts handle edge cases and difficult questions. This approach parallels how expert time is already managed in professional contexts—associates handle routine work under partner supervision. Effective implementation requires protocols for identifying which cases require senior review.

**Active learning for efficient expert allocation**: Use uncertainty-based sampling to identify cases where expert feedback would provide the most training value. Do not waste expert time on easy cases the model handles well or hopeless cases outside the model's capabilities. Focus expert effort on the learning frontier.

**Uncertainty-triggered expert review**: Train the model to flag its own uncertainty, routing only uncertain cases to expert evaluation. This approach requires that the model's self-assessment be calibrated, creating a bootstrapping challenge that RLEG itself aims to address.

These approaches are not mutually exclusive; practical implementations may combine several. But the fundamental constraint remains: expert grounding requires expert involvement, and expert involvement is scarce. RLEG may be most practical for high-stakes domains where the value of improved reliability justifies the cost of expert participation.

### 9.2 Expert Disagreement

Experts disagree. Medical professionals debate diagnoses; attorneys disagree about legal strategy; engineers differ on technical approaches. Domains have contested questions where no consensus exists among qualified practitioners.

RLEG with disagreeing experts faces the risk of confused training signal. If different experts provide conflicting feedback on similar cases, the model may learn conflicting patterns, producing outputs that satisfy no one or that vary unpredictably.

Several approaches might address this challenge:

**Flag uncertainty in contested areas**: Train the model to recognize when it is operating in contested territory and to express appropriate uncertainty rather than confident positions that half of experts would reject.

**Present alternatives**: In genuinely contested areas, train the model to acknowledge multiple positions and their supporting arguments rather than endorsing one.

**Defer to consensus where possible**: Use expert agreement as stronger training signal than individual expert preferences. Cases where all experts agree provide clearer training signal than cases where experts disagree.

**Explicit disagreement modeling**: Track which experts disagree on which questions, using this structure to learn the shape of disagreement rather than trying to resolve it.

These approaches require protocols for handling disagreement that are themselves part of the RLEG methodology to be developed. The challenge is not unique to RLEG—any system that learns from human judgment must handle disagreement—but RLEG makes it more salient because expert disagreement often concerns substantive issues rather than preferences.

### 9.3 Domain Coverage

RLEG requires experts for each domain the model addresses. General-purpose language models cover effectively unbounded domains—any topic a user might ask about. Providing expert coverage for all these domains is impossible.

This suggests a hybrid approach: RLEG for high-stakes domains where reliability matters most, standard RLHF or other methods for general-purpose chat where the stakes are lower. The model would receive domain-specific expert grounding for medical, legal, financial, or other high-stakes content while receiving broader crowdworker-based alignment for casual conversation.

Implementation raises questions about how domain-specific training interacts with general-purpose training. Does RLEG in one domain affect model behavior in others? Can expert grounding in medical contexts transfer to related areas like health wellness? These questions require empirical investigation and may have domain-specific answers.

### 9.4 The Grounding Limit

RLEG solves grounding at the training signal level but not at the model level. The trained model still lacks access to reality; it still cannot verify facts against the world; it still does not understand domains in the way that experts understand them. The model remains a derivative system that pattern-matches to learned distributions.

This limitation is fundamental, not technical. No training process can give the model genuine understanding or reality access. RLEG propagates expert grounding through learned behavior, but it does not instantiate expert understanding in the system.

This means RLEG-trained models still require appropriate deployment constraints. They should not be deployed as autonomous expert systems; they should be deployed as tools that experts supervise, or as interfaces that connect users to human expertise, or in contexts where their limitations are well understood.

The RLEG claim is not that we can create genuinely grounded AI systems. The claim is that we can create systems whose derivative grounding comes from expert judgment rather than crowdworker preferences—and that this is a meaningful improvement for reliability in specialized domains.

### 9.5 Evaluation

How do we measure RLEG success? Standard language model benchmarks may not capture what RLEG aims to achieve. Perplexity, BLEU scores, and general reasoning benchmarks do not assess domain-specific accuracy, purpose-fitness, or calibration.

Proposed metrics for RLEG evaluation include:
- **Domain-specific accuracy**: Performance on expert-curated evaluation sets in target domains
- **Calibration metrics**: Expected Calibration Error, reliability diagrams, and related measures of confidence-accuracy alignment
- **Expert approval rate**: Direct expert evaluation of output quality in target domains
- **Purpose-fitness**: Expert assessment of whether outputs serve their intended functions
- **Fluency ratings**: Human evaluation of accessibility and communication quality
- **Downstream task performance**: Performance on real-world tasks in target domains

Developing appropriate benchmarks is part of the RLEG research program. Existing benchmarks were designed for general-purpose evaluation; RLEG requires evaluation that captures teleological and mereological fit in specific domains.

---

## 10. A Research Program for RLEG

This paper proposes not a single empirical result but a paradigm shift requiring sustained investigation. The following research program outlines the work needed to develop RLEG from conceptual framework to deployable methodology.

### 10.1 Phase 1: Foundational Validation (Years 1-2)

The core question for Phase 1 is straightforward: Does RLEG actually preserve calibration better than RLHF?

The research agenda would include matched domain comparisons: RLEG versus RLHF on identical base models in identical domains. Calibration measurement would use ECE, reliability diagrams, and confidence-accuracy curves before and after training. Factuality measurement would employ domain-specific accuracy benchmarks. Fluency measurement would use human evaluation of output quality.

Success criteria for Phase 1 would be demonstrated calibration preservation or improvement under RLEG with no significant fluency degradation (or documented tradeoff curves), reproducible across at least two distinct domains.

This phase has no dependencies and represents the foundational empirical test of the RLEG thesis. Potential collaborators include academic machine learning laboratories and industry research teams with access to domain experts.

### 10.2 Phase 2: Methodology Development (Years 2-4)

Phase 2 addresses: How should expert-trainer collaboration be structured for effective RLEG?

The research agenda includes developing expert elicitation protocols (what questions extract grounded judgment efficiently?), designing reward structures (how should teleological and mereological information be preserved in training signal?), creating team collaboration frameworks (interface specifications, communication protocols, feedback loops), and detecting failure modes (reward hacking, calibration collapse, distribution shift under RLEG).

Success criteria include published elicitation protocols with measured efficiency (expert time per unit of training signal), reward structure templates validated across multiple domains, and team collaboration methodology that has been documented and replicated.

Phase 2 depends on Phase 1 results demonstrating RLEG's value proposition. Potential collaborators include human-computer interaction researchers, organizational behavior specialists, and domain-specific institutions.

### 10.3 Phase 3: Domain Instantiation (Years 3-5)

Phase 3 asks: What does RLEG look like in specific high-stakes domains?

The research agenda includes developing domain-specific implementations:
- **Medical RLEG**: Clinician feedback on diagnostic outputs, clinical workflow integration
- **Legal RLEG**: Attorney feedback on legal analysis, case strategy fit
- **Engineering RLEG**: Domain engineer feedback on technical outputs, system integration
- **Financial RLEG**: Analyst feedback on market analysis, risk assessment calibration

Success criteria include at least three domain-specific RLEG implementations, documented case studies including team structure, methodology, and outcomes, and domain-specific benchmarks for teleological and mereological fit.

Phase 3 depends on Phase 2 methodology being sufficient for domain adaptation. Potential collaborators include medical schools, law schools, engineering firms, and financial institutions.

### 10.4 Phase 4: Scaling Solutions (Years 4-6)

Phase 4 addresses the fundamental question: How can RLEG overcome expert scarcity?

The research agenda includes expert-seeded RLAIF (can AI models trained on expert feedback provide proxy feedback?), hierarchical review structures (junior reviewers handle routine cases, experts handle edge cases), active learning optimization (uncertainty-based sampling to maximize expert impact), and transfer learning experiments (does RLEG in one domain transfer benefits to adjacent domains?).

Success criteria include a demonstrated scaling pathway achieving greater than 10x expert leverage, maintained calibration under scaled approaches, and transfer experiments showing cross-domain benefits.

Phase 4 depends on Phase 3 successful domain implementations providing training data. Potential collaborators include large-scale machine learning infrastructure teams and active learning researchers.

### 10.5 Phase 5: Theoretical Foundations (Ongoing, Years 1-6)

Phase 5, running parallel to the empirical phases, asks: What formal characterization underlies RLEG effectiveness?

The research agenda includes formal specification (what information does expert feedback carry that crowdworker feedback cannot?), grounding propagation (how does training signal grounding transfer to model behavior?), identification of RLEG limits (what can expert feedback not solve? where does derivative grounding fail?), and connection to theoretical frameworks about AI epistemic limits.

Success criteria include a formal framework distinguishing expert-grounded from crowd-grounded training, theoretical predictions validated by empirical results, and clear articulation of RLEG limits and appropriate deployment constraints.

This phase runs parallel to other phases and is informed by their results. Potential collaborators include philosophy of AI researchers, formal methods specialists, and AI safety theorists.

### 10.6 Research Program Summary

| Phase | Core Question | Timeline | Key Deliverables |
|-------|--------------|----------|------------------|
| 1. Validation | Does RLEG preserve calibration? | Years 1-2 | Comparative studies, calibration measurements |
| 2. Methodology | How should teams collaborate? | Years 2-4 | Elicitation protocols, reward structures, team frameworks |
| 3. Instantiation | What works in specific domains? | Years 3-5 | Medical, legal, engineering case studies |
| 4. Scaling | How to overcome expert scarcity? | Years 4-6 | RLAIF seeding, active learning, transfer |
| 5. Theory | What formal foundations apply? | Ongoing | Formal framework, grounding propagation theory |

The programmatic claim is this: RLEG is not a single technique to be validated but a research direction requiring sustained multi-phase investigation. This paper provides the conceptual foundation; the research program provides the path to implementation.

---

## 11. Conclusion

### 11.1 Summary

Reinforcement Learning from Human Feedback has proven remarkably effective at making language models usable, but it frequently produces models that are fluent, engaging, and confidently wrong. The research literature documents calibration degradation, verbalized overconfidence, and factuality damage as common consequences of the RLHF process.

This paper has argued that the problem lies not in how feedback is structured but in who provides it. Crowdworkers can evaluate surface properties—fluency, engagement, format—but cannot evaluate domain accuracy, reasoning validity, appropriate uncertainty, or fitness for purpose. These properties require domain expertise that crowdworkers lack by definition.

RLEG (Reinforcement Learning from Expert Guidance) addresses this gap by changing the feedback source. Domain experts provide training signal that carries teleological grounding (does this output serve its intended purpose?) and mereological grounding (does this output fit the whole it enters?) that crowdworker feedback cannot convey. The shift from "Feedback" to "Guidance" marks this distinction: experts provide direction toward purpose, not merely correction of errors.

Implementation requires novel team structures that pair domain experts with AI training specialists. Neither alone can implement RLEG effectively. The methodology for this collaboration does not yet exist as a developed discipline; its development is part of the research program this paper proposes.

The RLEG research program encompasses foundational validation, methodology development, domain instantiation, scaling solutions, and theoretical foundations. This represents a multi-year, multi-phase effort to develop RLEG from conceptual framework to deployable practice.

### 11.2 The Core Insight

The historical precedents of Deep Blue and AlphaGo illuminate the core insight. Deep Blue did not understand chess; it inherited grounding through its evaluation function, which chess grandmasters had shaped. AlphaGo did not understand Go; it inherited grounding through expert-seeded training and self-play that converged on what experts would recognize as strong play. Both achieved superhuman performance not through understanding but through derived grounding that propagated expert judgment into system behavior.

RLEG models would not understand domains in the way that experts understand them. They would remain derivative systems, pattern-matching to learned distributions. But they would pattern-match to distributions shaped by expert judgment rather than crowdworker preferences. This derivation from a different source is the RLEG contribution.

Derivation from expert grounding is categorically different from derivation from surface preferences. Both produce derivative systems, but what is inherited differs fundamentally. The model trained on crowdworker preferences inherits appearance of reliability; the model trained on expert judgment inherits expert standards for actual reliability.

### 11.3 The Path Forward

Developing RLEG as a deployable methodology requires work across multiple dimensions:

First, develop RLEG methodology as a distinct discipline, with its own practices, tools, and professional standards. This is not a minor variation on existing RLHF practice but a different paradigm requiring new expertise.

Second, train practitioners who span domain expertise and AI training knowledge. Current educational pathways produce neither, and the intersection remains largely unpopulated. New training programs, certification standards, and career pathways are needed.

Third, build organizational structures that support expert-trainer collaboration. RLEG teams are neither traditional ML engineering nor traditional domain practice; they require hybrid structures with appropriate authority, resources, and incentives.

Fourth, deploy RLEG-trained models within appropriate frameworks that recognize their continuing limitations. RLEG improves training signal but does not give models genuine understanding or reality access. Appropriate deployment maintains human oversight and expert supervision.

Fifth, pursue the research program outlined in Section 10, moving systematically from validation through methodology to domain instantiation to scaling to theoretical foundations.

### 11.4 Final Observation

The field is asking, "How do we build better reward functions?" This is a valuable question that has produced useful research. But the deeper question may be, "Who should be providing the feedback?"

RLEG answers: those with access to the grounding the model cannot reach. Not crowdworkers who can evaluate appearance, but experts who can evaluate substance. Not feedback that corrects errors, but guidance that points toward purpose.

The shift from "Feedback" to "Guidance" is not merely terminological. It marks the difference between reactive correction (that was wrong) and purposive direction (this is what it's for, this is where it fits). Experts provide not just accuracy but telos—judgment about what the output is for and how it fits the whole it serves.

RLEG does not solve the grounding problem at the model level. The language model, no matter how well trained, will not achieve genuine understanding or reality access. But RLEG solves the grounding problem at the training signal level, propagating expert judgment through learned behavior. For practical purposes—for producing systems that are actually reliable rather than merely appearing reliable—this may be sufficient.

The path from RLHF to RLEG is a path from surface to substance, from appearance to reliability, from what crowdworkers can see to what experts can know. It is a longer path, more expensive, and more organizationally demanding. But for high-stakes domains where reliability matters, it may be the only path that reaches the destination.

---

## References

Campbell, M., Hoane, A. J. and Hsu, F. (2002) 'Deep Blue', *Artificial Intelligence*, 134(1-2), pp. 57-83. doi: 10.1016/S0004-3702(01)00129-1.

Christiano, P., Leike, J., Brown, T., Martic, M., Legg, S. and Amodei, D. (2017) 'Deep reinforcement learning from human preferences', in *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*. Available at: https://arxiv.org/abs/1706.03741.

Gehring, J., Zheng, K., Copet, J., Mella, V., Cohen, T. and Synnaeve, G. (2024) 'RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning', *arXiv preprint arXiv:2410.02089*. Available at: https://arxiv.org/abs/2410.02089.

Guo, C., Pleiss, G., Sun, Y. and Weinberger, K. Q. (2017) 'On Calibration of Modern Neural Networks', in *Proceedings of the 34th International Conference on Machine Learning (ICML 2017)*. Available at: https://arxiv.org/abs/1706.04599.

Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., Schiefer, N., Hatfield-Dodds, Z., DasSarma, N., Tran-Johnson, E., Johnston, S., El-Showk, S., Jones, A., Elhage, N., Hume, T., Chen, A., Bai, Y., Bowman, S., Fort, S., Ganguli, D., Hernandez, D., Jacobson, J., Kernion, J., Kravec, S., Lovitt, L., Ndousse, K., Olsson, C., Ringer, S., Amodei, D., Brown, T., Clark, J., Joseph, N., Mann, B., McCandlish, S., Olah, C. and Kaplan, J. (2022) 'Language Models (Mostly) Know What They Know', *arXiv preprint arXiv:2207.05221*. Available at: https://arxiv.org/abs/2207.05221.

Lin, S., Hilton, J. and Evans, O. (2024) 'FLAME: Factuality-Aware Alignment for Large Language Models', *arXiv preprint arXiv:2405.01525*. Available at: https://arxiv.org/abs/2405.01525.

Schulman, J., Wolski, F., Dhariwal, P., Radford, A. and Klimov, O. (2017) 'Proximal Policy Optimization Algorithms', *arXiv preprint arXiv:1707.06347*. Available at: https://arxiv.org/abs/1707.06347.

Settles, B. (2012) 'Active Learning', *Synthesis Lectures on Artificial Intelligence and Machine Learning*, 6(1), pp. 1-114. doi: 10.2200/S00429ED1V01Y201207AIM018.

Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., van den Driessche, G., Schrittwieser, J., Antonoglou, I., Panneershelvam, V., Lanctot, M., Dieleman, S., Grewe, D., Nham, J., Kalchbrenner, N., Sutskever, I., Lillicrap, T., Leach, M., Kavukcuoglu, K., Graepel, T. and Hassabis, D. (2016) 'Mastering the game of Go with deep neural networks and tree search', *Nature*, 529(7587), pp. 484-489. doi: 10.1038/nature16961.

Silver, D., Schrittwieser, J., Simonyan, K., Antonoglou, I., Huang, A., Guez, A., Hubert, T., Baker, L., Lai, M., Bolton, A., Chen, Y., Lillicrap, T., Hui, F., Sifre, L., van den Driessche, G., Graepel, T. and Hassabis, D. (2017) 'Mastering the game of Go without human knowledge', *Nature*, 550(7676), pp. 354-359. doi: 10.1038/nature24270.

Silver, D., Hubert, T., Schrittwieser, J., Antonoglou, I., Lai, M., Guez, A., Lanctot, M., Sifre, L., Kumaran, D., Graepel, T., Lillicrap, T., Simonyan, K. and Hassabis, D. (2018) 'A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play', *Science*, 362(6419), pp. 1140-1144. doi: 10.1126/science.aar6404.

Tian, K., Mitchell, E., Zhou, A., Sharma, A., Rafailov, R., Yao, H., Finn, C. and Manning, C. (2023) 'Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback', in *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)*. Available at: https://arxiv.org/abs/2305.14975.

---

*Word count: approximately 10,500*
