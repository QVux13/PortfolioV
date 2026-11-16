# Acceptance checklist — portfolio redesign

This checklist is for the **future implementation PR**. The present documentation-only PR does not claim these tests have passed.

## Routes and rendering
- [ ] All five full-page URLs serve complete HTML with correct active navigation.
- [ ] Each URL responds to X-SPA-Request: 1 with appropriate partial content.
- [ ] /download-cv/ returns the existing PDF or documented error.
- [ ] Images and styles render correctly after direct refresh and after SPA navigation.
- [ ] Document title reflects the current page.

## SPA and interactions
- [ ] Main/right/mobile navigation works; Back and Forward restore correct content and active state.
- [ ] Rapid navigation or fetch error does not strand page in a loading/hidden state.
- [ ] Repeated Home -> Portfolio -> Resume -> Portfolio visits do **not** duplicate event handlers, filter actions or animations.
- [ ] All category buttons filter projects correctly; changing categories after returning to the page still works.
- [ ] Working and placeholder external links are inventoried; no fabricated replacement links.
- [ ] Contact form fields have labels, validation and usable feedback.
- [ ] Contact POST includes CSRF and is tested using mocked email/backend; no unapproved real delivery.

## Layout and responsiveness
- [ ] BEFORE/AFTER screenshots at identical 1440x900 and 390x844 for each page, or documented browser limitation.
- [ ] Visual check at 360, 390, 768, 1024 and 1440px widths.
- [ ] Profile/sidebar identity and desktop page layout remain recognizable.
- [ ] Bottom navigation works with touch and safe-area insets; no horizontal overflow.
- [ ] Portfolio images preserve usable crop and aspect ratio; no broken images.
- [ ] Readable contrast, consistent spacing and clear heading hierarchy.

## Accessibility and performance
- [ ] Keyboard navigation has visible focus and no arrow-key interference with expected scrolling.
- [ ] Active page state exposed accessibly; after SPA navigation focus and announcements are sensible.
- [ ] No essential action only appears on hover.
- [ ] Reduced-motion preference suppresses nonessential animation without hiding content.
- [ ] No duplicate autoplay/perpetual heavy effects; animation favors opacity/transform.
- [ ] Run automated accessibility and performance checks if tooling is available; record measured scores only.

## Engineering
- [ ] Django check and existing tests run; exact command/results recorded.
- [ ] No unapproved edits to views' factual data, credentials, URLs, media routing or deployment workflow.
- [ ] No production deployment from the feature branch; compare diff and review PR.
- [ ] Document remaining limitations and content items requiring owner verification.
