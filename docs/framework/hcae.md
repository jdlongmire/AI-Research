---
layout: paper
title: "HCAE: Human-Curated, AI-Enabled Deployment Model"
permalink: /framework/hcae/
author: "James (JD) Longmire"
date_published: 2026-01-15
keywords:
  - HCAE
  - AI Deployment
  - Epistemic Authority
  - Human-AI Collaboration
abstract: "Human-Curated, AI-Enabled (HCAE) provides a tiered framework for appropriate AI deployment based on epistemic authority requirements. Rather than treating AI as either fully autonomous or fully supervised, HCAE stratifies deployment by domain criticality, verification feasibility, and human expertise availability."
---

## Overview

HCAE addresses a fundamental question: *How should AI systems be deployed given their structural epistemic limitations?*

The framework rejects both extremes:
- **Full autonomy** ignores AIDK and risks undetected errors
- **Full supervision** negates efficiency gains

HCAE provides a middle path: stratified deployment matched to actual capability and verification requirements.

---

## The Three Tiers

### Tier 1: Human Authority

**Model:** AI generates, human decides.

| Aspect | Description |
|--------|-------------|
| Human Role | Final authority on all outputs |
| AI Role | Draft generation, option surfacing, information synthesis |
| Verification | Full human review before action |
| Error Cost | High (medical, legal, safety-critical) |

**Examples:**
- Medical diagnosis assistance
- Legal document drafting
- Safety-critical system recommendations
- Executive decision support

**Key Principle:** AI output is treated as *input to* human judgment, never as *replacement for* it.

### Tier 2: Human Oversight

**Model:** AI executes within bounds, human monitors.

| Aspect | Description |
|--------|-------------|
| Human Role | Define boundaries, review samples, handle exceptions |
| AI Role | Execution within defined parameters |
| Verification | Statistical sampling, boundary monitoring |
| Error Cost | Moderate (operational, recoverable) |

**Examples:**
- Customer service automation with escalation
- Content moderation with appeal process
- Automated reporting with spot checks
- Process automation with exception handling

**Key Principle:** Trust is bounded and verified, not assumed.

### Tier 3: Monitored Autonomy

**Model:** AI operates autonomously, outputs monitored.

| Aspect | Description |
|--------|-------------|
| Human Role | System monitoring, intervention on anomaly |
| AI Role | Autonomous operation within known domain |
| Verification | Output monitoring, anomaly detection |
| Error Cost | Low (reversible, non-critical) |

**Examples:**
- Spam filtering
- Recommendation systems
- Search result ranking
- Automated categorization

**Key Principle:** Autonomy is granted only where errors are reversible and non-critical.

---

## Tier Selection Criteria

### 1. Error Reversibility

| Question | Tier Implication |
|----------|------------------|
| Can errors be easily reversed? | Lower tier possible |
| Are errors permanent or harmful? | Higher tier required |
| Is there a correction mechanism? | Enables lower tier |

### 2. Domain Criticality

| Domain | Typical Tier |
|--------|--------------|
| Safety-critical | Tier 1 only |
| Professional (legal, medical) | Tier 1-2 |
| Business operations | Tier 2-3 |
| Consumer convenience | Tier 3 possible |

### 3. Verification Feasibility

| Question | Tier Implication |
|----------|------------------|
| Can outputs be easily verified? | Enables higher tier |
| Is verification expensive/slow? | May require lower tier |
| Are verification experts available? | Required for Tier 1 |

### 4. Human Expertise Availability

| Situation | Tier Implication |
|-----------|------------------|
| Domain experts available | Enables Tier 1 |
| General oversight possible | Tier 2 appropriate |
| Monitoring-only capacity | Tier 3 necessary |

---

## Implementation Guidelines

### Tier 1 Implementation

1. **AI Output Formatting**
   - Present as suggestions, not conclusions
   - Include confidence indicators (calibrated to actual reliability)
   - Surface reasoning/sources for verification

2. **Human Review Process**
   - Structured review protocol
   - Time allocated for genuine evaluation
   - Authority to reject/modify

3. **Documentation**
   - Record AI contribution
   - Record human modifications
   - Maintain audit trail

### Tier 2 Implementation

1. **Boundary Definition**
   - Clear scope of AI authority
   - Explicit escalation triggers
   - Regular boundary review

2. **Sampling Strategy**
   - Statistical validity of sample size
   - Stratified by output type/risk
   - Trend monitoring

3. **Exception Handling**
   - Clear escalation path
   - Response time requirements
   - Learning from exceptions

### Tier 3 Implementation

1. **Monitoring Systems**
   - Output distribution monitoring
   - Anomaly detection
   - Feedback loop analysis

2. **Intervention Triggers**
   - Defined anomaly thresholds
   - User complaint patterns
   - Performance degradation

3. **Rollback Capability**
   - Quick reversion to human handling
   - Historical output review
   - Impact assessment

---

## HCAE and AIDK

HCAE is designed specifically to mitigate AIDK:

| AIDK Characteristic | HCAE Mitigation |
|---------------------|-----------------|
| Uniform confidence | Human evaluation of actual reliability |
| No competence detection | Tier boundaries define scope |
| No reality access | Human provides ground truth |
| Cannot self-correct | Human feedback corrects outputs |

The framework acknowledges that AI cannot know what it doesn't know, and structures deployment to provide the knowledge AI lacks.

---

## Anti-Patterns

### HCAE Violations

1. **Automation Bias**
   - Treating AI outputs as authoritative
   - Rubber-stamping without review
   - Deferring to AI against judgment

2. **Tier Creep**
   - Gradual expansion of AI authority
   - Reducing verification over time
   - Normalizing autonomous operation

3. **False Efficiency**
   - Removing human review to save time
   - Treating verification as overhead
   - Measuring only throughput, not quality

4. **Confidence Calibration Failure**
   - Treating AI confidence as reliability
   - Not training users on AIDK
   - Accepting IDKE as normal

---

## Organizational Implementation

### Governance Requirements

1. **Tier Classification Authority**
   - Who decides tier assignment?
   - What review process?
   - How often reassessed?

2. **Monitoring Responsibility**
   - Who monitors each tier?
   - What metrics are tracked?
   - How are anomalies escalated?

3. **Training Requirements**
   - AIDK awareness for all users
   - Tier-specific protocols
   - Regular refresher training

### Cultural Considerations

HCAE requires organizational culture that:
- Values verification over speed
- Empowers humans to override AI
- Treats AI skepticism as professional
- Rewards catching AI errors

---

## Conclusion

HCAE provides a practical framework for deploying AI systems while acknowledging their structural limitations. By stratifying deployment based on actual capability and verification requirements, organizations can capture AI value while mitigating AIDK risks.

The key insight: **AI deployment should be matched to actual capability, not hoped-for capability.**

---

## Related Work

- [AIDK Framework]({{ site.baseurl }}/framework/aidk/) - The structural limitations HCAE addresses
- [Research Program]({{ site.baseurl }}/framework/research-program/) - Broader theoretical context
