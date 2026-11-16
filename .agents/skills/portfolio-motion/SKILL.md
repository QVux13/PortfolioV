---
name: portfolio-motion
description: Optimize PortfolioV's existing dark-neon animation, custom SPA transitions, scroll reveals and hover interaction for accessibility and performance.
---

# PortfolioV motion quality, not quantity

The code already has a glowing avatar ring, background blobs, project card animations, page transitions, a cursor spotlight, IntersectionObserver bars, and a custom SPA fetch engine. Audit and rationalize these **before** adding effects.

Suggested ranges:
- Hero reveal: 450–650ms with 12–18px motion, short stagger.
- Navigation hover/focus: 160–220ms.
- Project card feedback: 180–260ms and lift no greater than 3–4px.
- Scroll reveals: 400–600ms, default-visible fallback.
- Route transition: use existing progressive enhancement and fast failure fallback.

Technical safeguards:
1. Respect prefers-reduced-motion. Disable nonessential perpetual animations, ensure content remains visible.
2. Prefer transform and opacity, avoid layout thrash, repeated blur and expensive full-page filters.
3. Page scripts are re-executed on each SPA replacement and dispatch spa:page-ready. Make listeners idempotent, scoped or cleaned up; inspect existing Portfolio/Resume initialization carefully.
4. Keep standard anchors, deep-link refresh, History API, page title, tab focus and backend form submission functional.
5. Never hide clickable content behind hover-only overlays, never hijack scroll, and avoid app-wide arrow key handling that breaks normal reading.
6. Verify on touch, keyboard, reduced motion and mobile. Record trigger/duration/fallback in docs/portfolio-redesign/MOTION_SPEC.md.
