---
layout: default
title: "AI Research & Philosophy"
image: /assets/images/ai-research-banner.jpg
---

<div class="hero-banner-wrapper">
  <div class="hero-banner">
    <img src="{{ site.baseurl }}/assets/images/ai-research-banner.jpg" alt="AI Research & Philosophy - Understanding AI Through the AIDK Framework" />
  </div>
</div>

<div class="topic-header">
  <h1>AI Research & Philosophy</h1>
  <p>Understanding AI Capabilities and Limitations Through the AIDK Framework</p>
  <p><a href="{{ site.baseurl }}/articles/">Jump to Articles →</a></p>
</div>

## The Core Thesis

**AI Dunning-Kruger (AIDK)** describes the structural epistemic limitations of Large Language Models. This is not a correctable bug but an architectural condition: AI systems produce uniform confidence regardless of reliability, lack mechanisms for detecting competence boundaries, and cannot self-correct through encounter with reality.

The framework distinguishes:

- **Origination**: Retrieving configurations from Infinite Information Space not derived from prior inputs
- **Derivation**: Transformation of prior inputs according to learned patterns

Human cognition has access to two coexistent primitives - Infinite Information Space ($I_\infty$) and the three fundamental laws of logic ($L_3$). AI systems are categorically derivative, operating downstream of human-generated data and unable to access these primitives directly.

> *More derivation does not become origination.*

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **AIDK** | AI Dunning-Kruger: structural epistemic limitation (architectural, not correctable) |
| **IDKE** | Interactive Dunning-Kruger Effect: amplification when AI limitations meet human limitations |
| **HCAE** | Human-Curated, AI-Enabled: deployment framework stratified by epistemic authority |
| **MAPT** | Model Advanced Persistent Threat: security framing for AIDK |

---

## Framework Papers

<div class="paper-grid">
  <div class="paper-card">
    <h3><a href="{{ site.baseurl }}/framework/aidk/">AIDK Framework</a></h3>
    <p>The complete theoretical framework establishing structural epistemic limitations in AI systems. Published on Zenodo with DOI.</p>
    <div class="meta">January 2026 | Foundation Paper</div>
    <a href="{{ site.baseurl }}/framework/aidk/" class="card-link">Read Framework</a>
  </div>

  <div class="paper-card">
    <h3><a href="{{ site.baseurl }}/framework/hcae/">HCAE Deployment Model</a></h3>
    <p>Human-Curated, AI-Enabled: A tiered approach to AI deployment based on epistemic authority requirements.</p>
    <div class="meta">January 2026 | Deployment Framework</div>
    <a href="{{ site.baseurl }}/framework/hcae/" class="card-link">Read Framework</a>
  </div>

  <div class="paper-card">
    <h3><a href="{{ site.baseurl }}/framework/research-program/">Research Program</a></h3>
    <p>The full theoretical program investigating AI through the origination-derivation lens.</p>
    <div class="meta">December 2025 | Research Agenda</div>
    <a href="{{ site.baseurl }}/framework/research-program/" class="card-link">Read Program</a>
  </div>
</div>

---

## Recent Articles

<div class="paper-grid">
{% assign articles = site.pages | where_exp: "page", "page.path contains 'articles/'" | where_exp: "page", "page.layout == 'article'" | sort: "date" | reverse %}
{% for article in articles limit: 6 %}
  <div class="paper-card">
    <h3><a href="{{ article.url | relative_url }}">{{ article.title }}</a></h3>
    <p>{{ article.description | default: "An article from AI Research & Philosophy." }}</p>
    <div class="meta">{{ article.date | date: "%B %Y" }}</div>
    <a href="{{ article.url | relative_url }}" class="card-link">Read Article</a>
  </div>
{% endfor %}
</div>

<p style="text-align: center; margin-top: 1rem;"><a href="{{ site.baseurl }}/articles/">View All Articles →</a></p>

---

## Author

**James (JD) Longmire**

- ORCID: [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)
- Email: jdlongmire@outlook.com
- GitHub: [jdlongmire](https://github.com/jdlongmire)
- Substack: [AI Research & Philosophy](https://airesearchandphilosophy.substack.com/)

**AI Assistance Disclosure**: This work was developed with assistance from AI language models including Claude (Anthropic), ChatGPT (OpenAI), Gemini (Google), Grok (xAI), and Perplexity. All substantive claims, arguments, and errors remain the author's responsibility. **Human-Curated, AI-Enabled (HCAE)**.

---

## Archives

- [Zenodo Community](https://zenodo.org/communities/ai-research-philosophy) - Persistent DOI-minted archives
- [AIDK Framework (DOI: 10.5281/zenodo.18316059)](https://zenodo.org/records/18316059) - Published framework
- [GitHub Repository](https://github.com/jdlongmire/AI-Research) - Source code and development history
