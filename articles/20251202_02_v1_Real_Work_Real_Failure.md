# Real Work, Real Failure: What the Freelancer Test Reveals About AI

![AI Limitations](figures/what-can-ai-do.png)

A new study puts numbers to something many suspected: the gap between AI benchmark performance and real-world competence isn't a gap. It's a canyon.

## The Study

The **Remote Labor Index (RLI)**, developed by the Center for AI Safety and Scale AI, is the first benchmark designed to measure how well AI agents can perform paid, real-world work (Mazeika et al., 2025).

Researchers collected 240 freelance projects sourced directly from experienced professionals on Upwork. This is work that humans actually got paid for. Architecture design, video editing, game development, 3D modeling, data dashboards. Projects ranging from $9 to $22,500, totaling $143,991 in professional work. Mean human completion time: 28.9 hours per project.

They deployed six state-of-the-art AI agents: Manus, Grok 4, Claude Sonnet 4.5, GPT-5, ChatGPT Agent, and Gemini 2.5 Pro.

The results:

| Agent | Success Rate | Earnings |
|-------|--------------|----------|
| Manus | 2.5% | $1,720 |
| Grok 4 | 2.1% | - |
| Claude Sonnet 4.5 | 2.1% | $1,280 |
| GPT-5 | 1.7% | $1,180 |
| ChatGPT Agent | 1.3% | - |
| Gemini 2.5 Pro | 0.8% | - |

The best agent failed **97.5% of the time.**

## The Failure Patterns

The study's failure analysis reveals systematic issues:

- **45.6%** had quality issues: work simply not at professional standard
- **35.7%** submitted incomplete or malformed deliverables (truncated videos, missing files, empty directories)
- **17.6%** produced corrupt, unusable, or empty files
- **14.8%** failed to maintain visual or logical consistency across project files

As the researchers note: "Agents excel at creating from scratch from a simple prompt, but fail at complex editing or following a precise, multi-step brief. Their generative skill is high, but their ability to act as a reliable, detail-oriented professional is low."

Dan Hendrycks, director of the Center for AI Safety, identified core limitations: "They don't have long-term memory storage and can't do continual learning from experiences. They can't pick up skills on the job like humans."

## What the Framework Explains

This study illustrates a core claim of the origination-derivation framework: **benchmark performance does not predict real-world competence.**

Why? Because benchmarks test pattern-matching within known distributions. Real work requires something different.

Consider what a freelance project actually demands:

1. **Understanding unstated requirements** - Clients rarely specify everything. Human freelancers fill gaps with judgment about what the client actually needs.

2. **Navigating ambiguity** - Real projects involve contradictory constraints, unclear priorities, and evolving requirements.

3. **Quality judgment** - Knowing when something is "good enough" versus "unprofessional" requires understanding the purpose, not just matching patterns.

4. **Coherent integration** - A 3D building that looks different from every angle reveals a failure to maintain coherent representation across perspectives.

These tasks require more than deriving outputs from training patterns. They require origination: accessing understanding that isn't simply a transformation of prior inputs.

## Benchmarks vs. Reality

The systems tested had crushed every benchmark. Bar exams. Medical licensing. Standardized tests.

But these benchmarks share a common feature: they have defined correct answers within established frameworks. They test whether a system can match the pattern of "what a correct answer looks like" within a closed domain.

As the RLI researchers explain: "Current AI progress on research benchmarks, which often test isolated skills, provides limited insight into the trajectory of actual automation."

This benchmark-reality gap appears across domains:
- **Software development** (clear goals, verifiable output): 30.4% task completion
- **Financial analysis**: 8.3% success
- **Administrative work**: 0% success
- **Lab to production**: 37% performance degradation (AWS research)

Real work is open-ended. The "correct answer" for a freelance project isn't pre-defined. It emerges from understanding what the client needs, what counts as professional in that context, and how to navigate the inevitable gaps in specification.

The framework predicts exactly this pattern: derivative systems excel at bounded tasks with clear success criteria, and struggle with open-ended work requiring judgment that can't be reduced to pattern-matching.

## The Honest Interpretation

This study doesn't prove AI is useless. It proves that current AI systems are tools, not autonomous workers.

The 2.5% success rate likely represents projects where:
- Requirements were unusually explicit
- The task closely matched training examples
- Minimal judgment was required

For such tasks, AI delivers value. For everything else, which is most professional work, the canyon remains.

## Implications

If derivative systems fundamentally cannot access what makes work "professional" or "appropriate" without explicit specification, then:

1. **Autonomous AI workers remain distant** - Not because of insufficient scale, but because the task requires origination.

2. **Human-AI collaboration is the path** - AI as tool, human as originator. Derivation augmenting origination, not replacing it.

3. **Benchmark skepticism is warranted** - Impressive test scores reveal pattern-matching capability, not general competence.

The $144,000 freelancer test didn't reveal a temporary limitation. It revealed a structural boundary.

---

**Research Repository:** https://github.com/jdlongmire/AI-Research

## References

Mazeika, M. et al. (2025) 'Remote Labor Index: Measuring AI Automation of Remote Work', *arXiv preprint arXiv:2510.26787*. Available at: https://arxiv.org/abs/2510.26787

Scale AI (2025) 'Remote Labor Index'. Available at: https://scale.com/leaderboard/rli

Center for AI Safety and Scale AI (2025) 'The Remote Labor Index: Measuring the Automation of Work'. Available at: https://scale.com/blog/rli

Source video: https://www.youtube.com/shorts/hE56XjBUl1g

---

**James (JD) Longmire**

ORCID: [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)

Northrop Grumman Fellow

*Human-curated, AI-enabled.*

*This work is entirely my own independent research. It does not reflect endorsement from, or the views of, Northrop Grumman Corporation or any of its affiliates.*
