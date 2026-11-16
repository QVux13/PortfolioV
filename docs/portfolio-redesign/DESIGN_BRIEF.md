# Design brief — Premium Backend / AI Engineer Portfolio

## Design intent
Upgrade the quality of the **existing** site, rather than creating a generic new portfolio. Existing main layout is recognizable: fixed/sticky profile identity on the left, focused main page area, right-side navigation on desktop, bottom dock on mobile. Preserve that structure and all five sections.

Visual style: **Modern Dark Editorial + Subtle Motion**. Sharper hierarchy, excellent readability, controlled depth, deliberate interaction, refined photography/cropping and strong mobile polish. Existing neon teal/indigo styling is a starting point; tune it instead of layering effects indiscriminately.

Suggested token direction (confirm against screenshots):
- Background: #0B1020; elevated surface: #131B2D; card: #192238.
- Main text: #F1F5FF; muted: #A6B2C9.
- Accent: #8B9CFF (indigo); secondary: #48D9D0 (teal).
- Radius: 12–20px for cards, smaller for controls; consistent 4/8px spacing rhythm.
- Typography: large but controlled heading scale, comfortable body line length, precise alignment; prefer installed fonts and validate loading.
- Design tokens must be accessible in both static and SPA-rendered content.

## Page priorities
### Shared shell
Keep profile portrait, name, role, core links, resume CTA and five-page navigation. Refine visual balance, spacing, focus/active state and mobile behavior. Avoid bulky double navigation on narrow screens.

### Home
Strong hero name/role, a clear value proposition, concise backend/AI capability tags and two prominent CTAs. No unsupported claims or fake counters.

### About
Readable introduction and fewer, stronger service/expertise cards. Use evidence from real project work; do not invent AI implementations or testimonials.

### Resume
Readable chronological timeline and grouped skills with observable evidence. Existing numeric skill percentages are subjective: propose a content change for approval, but do not rewrite facts silently.

### Portfolio
Keep category filtering and Django-driven project list. Make images, tags, details and clickable actions clear. Show important links without hover dependence, and flag placeholder URLs for owner review.

### Contact
Keep genuine contact methods and Django POST/CSRF/send_mail logic. Improve labels, keyboard focus and success/error states; review the existing map embed for accuracy/privacy without assuming it should stay or go.

## Motion principles
Use a limited motion vocabulary:
- Enter/reveal: 450–650ms, 12–18px vertical translation, short stagger.
- Nav hover/active: 160–220ms.
- Card hover: 180–260ms, lift 3–4px at most; subtle border/image response.
- Scroll reveal: 400–600ms only when useful and observable; default visible without JS.
- Route transition: keep existing Fetch/History behavior, with unobtrusive feedback and no unnecessary wait.
- Animate transform/opacity instead of layout properties. Reduce perpetual glow/particle effects rather than adding more.
- Respect prefers-reduced-motion. Honor keyboard users, touch devices and low-end mobile performance.

## Reject designs that
- Replace the Django application with a different framework.
- Remove the profile/sidebar identity or reorder sections without good reason.
- Add heavy 3D, scrolling hijacks, opaque overlays, excessive gradients or long preloading.
- Hide vital content until JS or animation succeeds.
- Change personal facts, project history, live links or current production settings without verification.

Keep screenshot comparisons at identical 1440x900 and 390x844 viewports for all five pages, when browser access is available.
