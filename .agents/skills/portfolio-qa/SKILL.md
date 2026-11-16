---
name: portfolio-qa
description: Check Django PortfolioV's full and SPA route behavior, responsive rendering, project filters, CV, contact form, accessibility and motion after redesign.
---

# PortfolioV QA gate

1. Use docs/portfolio-redesign/ACCEPTANCE_CHECKLIST.md. Run python manage.py check and existing tests, recording real outputs, not assumed success.
2. Validate all five routes as direct HTML documents and as X-SPA-Request: 1 partial responses. Confirm /download-cv/ downloads PDF.
3. Test SPA navigation, active nav state, document title, browser Back/Forward, rapid navigation, failure fallback and repeated page visits.
4. Specifically detect duplicated Portfolio filter click handlers and Resume IntersectionObserver / spa:page-ready initialization after multiple navigations.
5. Test form required inputs, CSRF and success/error UI. Mock SMTP / use console mail locally; do not send email to real contacts.
6. Test mobile 360/390, tablet 768/1024, desktop 1440 widths; no overflow, broken image/crop, bottom dock overlap or inaccessible CTA.
7. Test keyboard focus, aria-current, screen reader feedback on route changes, reduced motion, non-hover access to project links. Inspect JS console/network errors.
8. Capture AFTER screenshots using identical BEFORE viewport dimensions and routes. Run Lighthouse/a11y checks if available; only report measured scores.
9. Output docs/portfolio-redesign/QA_REPORT.md with test matrix, commands, screenshots, results, remaining defects and owner approval items. Do not deploy.
