---
name: portfolio-design-system
description: Refine the existing PortfolioV Django sidebar, templates and pages into a unified premium dark developer-portfolio design without changing routing or backend data.
---

# PortfolioV premium visual system

Prerequisite: read DESIGN_BRIEF.md and BASELINE_AUDIT.md; establish what currently works.

1. Establish CSS design tokens for background/surface, accessible text, indigo/teal accents, borders, radii, typography, spacing, elevation and breakpoints; write docs/portfolio-redesign/DESIGN_SYSTEM.md.
2. Do not create a competing separate UI framework. The source has substantial inline styles in base.html and five includes; improve progressively and consolidate safely when beneficial.
3. Preserve existing layout relationship and visual identity: avatar + social/profile sidebar, main content, right page navigation, mobile dock, five pages.
4. Home: purposeful hero + 2 actions. About: strong, evidence-based expertise cards. Resume: clean experience timeline, propose changes to subjective skill percentages for owner approval. Portfolio: filterable real project grid, readable controls, visible links. Contact: accessible labels/feedback while keeping Django POST/CSRF.
5. Reuse genuine images and existing Django context data from core/views.py; do not invent screenshots or verified claims.
6. Validate full-page and SPA partial rendering. Avoid injecting styles that vanish or duplicate on SPA navigation.
7. Prefer vanilla CSS and minimal JS, semantic HTML, readable line widths, keyboard focus, aria-current and mobile safe areas.
8. No production or backend config changes; document before/after comparisons and any owner approvals needed.
