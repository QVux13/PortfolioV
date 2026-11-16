# Source audit — QVux13/PortfolioV

Audit performed from GitHub repository source on 16 November 2026. Baseline commit: 19fae54a94f8b0ab57c06a03523b0b8c2e025bb5, main. This is a **source audit**, not a completed visual, live-browser or functional test.

## Actual stack and source of truth
- Django==5.2.6, Pillow, whitenoise, gunicorn in requirements.txt.
- Server-rendered HTML templates, substantial inline CSS, vanilla JavaScript; not a React/Next.js app.
- Django configuration: my_portfolio/settings.py; routing: my_portfolio/urls.py; views/content: core/views.py.
- Shared visual shell and SPA engine: core/templates/core/base.html (~798 lines).
- Page content: core/templates/core/includes/{home,about,resume,portfolio,contact}_content.html.
- Full-page wrappers: core/templates/core/{home,about,resume,portfolio,contact}.html.
- SPA response wrappers: core/templates/core/partials/{home,about,resume,portfolio,contact}_partial.html.
- Profile and project image assets under media/profile/ and media/projects/; CV under media/resume/.
- Deployment workflow: .github/workflows/deploy.yml, Vercel production triggered by push to main, preview on PR. Other deployment infrastructure may exist outside this repo; do not assume it does not.

## URL contract
| Route | Django view | Full-page template | SPA partial |
| --- | --- | --- | --- |
| / | home | home.html | home_partial.html |
| /about/ | about | about.html | about_partial.html |
| /resume/ | resume | resume.html | resume_partial.html |
| /portfolio/ | portfolio | portfolio.html | portfolio_partial.html |
| /contact/ | contact | contact.html | contact_partial.html |
| /download-cv/ | download_cv | FileResponse for existing PDF | Not an SPA route |

## Current layout and behavior
- Desktop profile sidebar, center content, right-side page navigation, plus a bottom mobile navigation dock.
- Existing dark/neon styling, layered backgrounds, animated avatar ring, hover states, page transitions, cursor spotlight and SPA loading progress.
- The SPA engine in base.html intercepts .spa-nav and .spa-link clicks, fetches HTML with header X-SPA-Request: 1, replaces contentBox, re-executes injected script tags, updates history/title/nav state, then dispatches both spa:ready and spa:page-ready.
- Back/forward is implemented through popstate. Direct page refresh is served through the corresponding full Django template.
- Resume progress bars use IntersectionObserver and a spa:page-ready handler.
- Portfolio cards are generated from core/views.py PROJECTS; filtering uses data-filter buttons and data-categories attributes. Client-side script also attaches a spa:page-ready handler.
- Contact uses a POST form with Django CSRF token and server-side send_mail via configured SMTP. Download CV uses a FileResponse.
- Profile, experience, education, coding skills and projects are hard-coded in core/views.py (there is no project database backing those records). Django DATABASES is empty in settings.py.

## Risks and review notes
1. **SPA listener lifecycle:** injected page scripts re-register document-level spa:page-ready listeners on visits. Inspect and make initialization idempotent during redesign; test repeated navigation/filtering/skill animation.
2. **Accessibility of SPA navigation:** test focus after injected content, focus indication, screen reader announcement, back/forward, and reduced-motion support. Arrow keys are currently used for page navigation; check whether they conflict with normal page/assistive scrolling.
3. **Animation overhead:** motion already exists, so refine/remove duplicate or costly effects before adding new ones. Inspect mobile CPU and reduced-motion setting.
4. **Inline styling:** significant CSS is embedded in base.html and each include. Refactor incrementally if beneficial, while keeping partial/full-page CSS behavior consistent.
5. **Content accuracy:** some project links are placeholders (yourusername or example.com); About includes hard-coded repository/work-hour statistics. Flag for owner verification, do not silently replace them with fabricated values.
6. **Contact privacy and reliability:** contact template includes a Google Maps embed; check appropriateness and privacy before changing. Never send a live test email without permission; use mocks/console email backend locally.
7. **Security/config separate from redesign:** a Django secret key is declared directly in settings.py. Recommend a later configuration/security review and environment-based secrets; do not publish secret contents or alter deployment settings in a design-only task.
8. **Media handling:** my_portfolio/urls.py explicitly serves /media/ through django.views.static.serve. Do not change it casually; validate each deployment environment independently.

## What is NOT verified in this document
- Actual rendered appearance on production and on local desktop/mobile; no before screenshots captured here.
- Actual form submission/delivery, network behavior, accessibility scores, Lighthouse performance, JS console errors or production environment parity.
- Whether source commit exactly matches the currently served public deployment.

Before code changes, Antigravity should run the application locally, inspect each route and record screenshots and baseline behaviors. Report any discrepancy between source and live UI.
