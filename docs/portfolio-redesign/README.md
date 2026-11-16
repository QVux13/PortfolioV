# Portfolio redesign — Antigravity handoff

**Goal:** turn the existing portfolio into a premium, modern, professional software-engineering site with beautiful but purposeful motion, **without changing its recognizable layout**.

**Source snapshot:** QVux13/PortfolioV, main at 19fae54a94f8b0ab57c06a03523b0b8c2e025bb5 (17 September 2026).
**Public URL:** https://quangvudev.io.vn/

## Start here
- REPO_AUDIT.md — facts established from the repository, and unverified runtime behavior.
- DESIGN_BRIEF.md — style direction, design tokens and page-by-page priorities.
- ANTIGRAVITY_PROMPT.md — ready-to-paste implementation prompt for Antigravity.
- ACCEPTANCE_CHECKLIST.md — functional, mobile, accessibility and performance gates.
- ../../AGENTS.md — cross-cutting agent constraints.
- ../../.agents/skills/ — four task-specific skills (audit, design system, motion, QA).

## Recommended sequence
1. Open the repository in Antigravity; use a fresh feature branch.
2. Paste the full contents of ANTIGRAVITY_PROMPT.md.
3. Agent performs a local source/runtime audit and captures BEFORE screenshots at fixed viewport sizes (if browser available).
4. Agent implements a cohesive visual refresh page by page while preserving Django and existing SPA.
5. Agent runs tests, verifies interactions, captures AFTER screenshots, and presents diff plus QA report.
6. Review changes before a PR is merged or deployed.

## Scope boundary
These documents are **guidance only**. Their addition does not change the appearance or behavior of the deployed portfolio. No application code, credentials, workflow, or runtime configuration is changed by this documentation commit.

If production cannot be accessed or the app cannot run locally, record limitations rather than inventing observations or Lighthouse results.
