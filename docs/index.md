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
  <p>Commentary and Analysis on AI Capabilities and Limitations</p>
</div>

## Latest Articles

<div class="paper-grid">
{% assign articles = site.pages | where_exp: "page", "page.path contains 'articles/'" | where_exp: "page", "page.layout == 'article'" | sort: "date" | reverse %}
{% for article in articles limit: 6 %}
  <div class="paper-card">
    <h3><a href="{{ article.url | relative_url }}">{{ article.title }}</a></h3>
    <p>{{ article.description | default: "An article from AI Research & Philosophy." }}</p>
    <div class="meta">{{ article.date | date: "%B %d, %Y" }}</div>
    <a href="{{ article.url | relative_url }}" class="card-link">Read Article</a>
  </div>
{% endfor %}
</div>

---

## All Articles

{% assign articles_by_month = site.pages | where_exp: "page", "page.path contains 'articles/'" | where_exp: "page", "page.layout == 'article'" | sort: "date" | reverse | group_by_exp: "article", "article.date | date: '%B %Y'" %}

{% for month in articles_by_month %}
### {{ month.name }}

| Date | Article |
|------|---------|
{% for article in month.items %}| {{ article.date | date: "%b %d" }} | [{{ article.title }}]({{ article.url | relative_url }}) |
{% endfor %}

{% endfor %}

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
