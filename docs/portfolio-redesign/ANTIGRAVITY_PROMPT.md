# Master prompt for Google Antigravity

You are working in the **existing** repository QVux13/PortfolioV, a Django-based developer portfolio. Public reference: https://quangvudev.io.vn/. Use the checked-out repository and local browser as your primary source of truth.

## Read before starting
Read AGENTS.md, docs/portfolio-redesign/README.md, REPO_AUDIT.md, DESIGN_BRIEF.md and ACCEPTANCE_CHECKLIST.md. Load the four workspace skills from .agents/skills in this order: portfolio-audit, portfolio-design-system, portfolio-motion, portfolio-qa.

## Goal
Evolve this site into a premium, credible, modern Backend / Software / AI engineer portfolio with sophisticated but restrained animation. **Maintain its familiar composition:** desktop profile/sidebar at left, central content, right-side page controls, mobile dock; preserve Home, About, Resume, Portfolio, Contact and the CV download route.

## Technical rules specific to this repository
1. Do not migrate Django to React/Next.js and do not replace the current SPA with a framework. Current frontend is HTML/CSS/vanilla JS in core/templates/core/base.html and includes/.
2. Keep routes /, /about/, /resume/, /portfolio/, /contact/ and /download-cv/ working for direct visits and SPA navigation.
3. Understand the header X-SPA-Request: 1 and partial response templates. Preserve Fetch + History API, popstate, active nav state, page title and safe full-page fallback.
4. Injected page scripts are re-executed on every SPA navigation and spa:page-ready is dispatched. Audit handlers, implement idempotent event registration or cleanup, and test repeated visits; do not introduce duplicate listeners.
5. Preserve Django template context variables, core/views.py data, media paths, project filtering, CV download, CSRF/contact POST and SMTP behavior. Test the form locally with a mocked/console email backend, not a live message.
6. Existing CSS, animated avatar ring, neon backgrounds, card effects, spotlight and transition animations already exist. Simplify and coordinate first; do not blindly add multiple overlapping animation systems.
7. Keep real content and images. Note questionable stats, dates or placeholder project links separately for my approval; do not fabricate or alter them.
8. Avoid modifying Django security configuration, GitHub Actions workflow, deployment secrets, DNS, EC2 or production. No production deploy.

## Execution
**Phase 1: Baseline** — audit source and run app locally. Capture BEFORE screenshots at 1440x900 desktop and 390x844 mobile for all five routes if browser is available. Verify navigation (full and SPA), browser history, filters, CV and form validation. Record findings in docs/portfolio-redesign/BASELINE_AUDIT.md, clearly separating verified behavior from assumptions.

**Phase 2: Design system** — derive color/type/spacing/radius/surface/motion tokens from the existing dark theme and DESIGN_BRIEF. Record in docs/portfolio-redesign/DESIGN_SYSTEM.md. Improve shared shell first; favor scoped CSS and small vanilla JS. Keep visuals coherent between direct and SPA page responses.

**Phase 3: Page improvements** — deliver a polished Home, About, Resume, Portfolio and Contact while retaining page information architecture. Improve typography, visual hierarchy, whitespace, links, project previews, card alignment, responsive sizes and accessibility.

**Phase 4: Motion** — use purposeful hero sequencing, card interaction, scroll reveals and refined route transitions. Ensure default-visible fallback, no broken content on JS failures, and prefers-reduced-motion support. Document in docs/portfolio-redesign/MOTION_SPEC.md.

**Phase 5: QA** — follow portfolio-qa and ACCEPTANCE_CHECKLIST. Test repeated SPA navigation, direct URL refresh, Back/Forward, category filtering, CV, contact form/CSRF, responsive widths 360/390/768/1024/1440, focus and reduced motion. Run python manage.py check and tests; browser console and network review; capture matching AFTER screenshots. Do not assert performance/accessibility scores without actually measuring.

## Completion format
Provide: (a) design and implementation summary; (b) modified files; (c) before/after screenshot locations and viewport sizes; (d) executed checks with pass/fail outcomes; (e) unresolved findings/content corrections for my approval; (f) any limitations. Do not deploy without permission.

Start with source + browser audit, then implement iteratively. Preserve existing content and working functionality over speculative visual features.
