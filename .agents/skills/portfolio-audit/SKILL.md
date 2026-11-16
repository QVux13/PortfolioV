---
name: portfolio-audit
description: Audit the current Django PortfolioV source and actual browser behavior, including its existing custom SPA and animation, before proposing any redesign.
---

# PortfolioV audit: observe before editing

1. Read AGENTS.md and docs/portfolio-redesign/REPO_AUDIT.md. Do not treat those documents as proof of runtime behavior.
2. Inspect my_portfolio/urls.py, core/views.py, core/templates/core/base.html, five page includes and partials, media assets, Django settings and deployment workflow.
3. Preserve the desktop profile sidebar / center content / right nav and mobile bottom dock. Inventory current CSS variables, glows, avatar ring, transitions, spotlight and responsiveness instead of rebuilding them.
4. Launch locally when possible; visit /, /about/, /resume/, /portfolio/, /contact/. Record URL, viewport, content, interactions and issues. Capture BEFORE screenshots at 1440x900 and 390x844 if browser available.
5. Test direct navigation and SPA header behavior. Check Fetch/History, back/forward, page title, loading fallback, partial script re-execution and both spa:ready/spa:page-ready event paths.
6. Revisit Portfolio and Resume repeatedly to detect duplicate document-level handlers. Inventory filters, dynamic project images, IntersectionObserver progress bars, contact CSRF and CV link.
7. Do NOT submit live email, deploy, change secrets or falsify content or screenshots.
8. Write docs/portfolio-redesign/BASELINE_AUDIT.md with verified findings, screenshot paths, preserved invariants, prioritized problems, and a phased implementation plan. Label unverified items clearly.
