# Agent instructions — PortfolioV

This repository is an existing Django portfolio, not a blank UI project. Before editing, read:
1. docs/portfolio-redesign/README.md
2. docs/portfolio-redesign/REPO_AUDIT.md
3. docs/portfolio-redesign/DESIGN_BRIEF.md
4. docs/portfolio-redesign/ANTIGRAVITY_PROMPT.md

Use these workspace skills, in order:
- .agents/skills/portfolio-audit/SKILL.md
- .agents/skills/portfolio-design-system/SKILL.md
- .agents/skills/portfolio-motion/SKILL.md
- .agents/skills/portfolio-qa/SKILL.md

## Non-negotiable rules
- Preserve Django 5.2 project, server-side views, all five URLs, download-cv endpoint, CSRF, email submission behavior, media assets and deployment configuration.
- Maintain the recognizable desktop profile sidebar + main-content + right-hand navigation, and current compact mobile dock. Improve quality, do not replace the information architecture.
- Maintain both ordinary full-page visits and custom Fetch/History SPA navigation. On SPA fetch, Django responds with partial templates when the X-SPA-Request header is 1.
- Inspect existing styling and animation before adding more. There is already dark neon styling, glowing avatar, animated backgrounds, project filters, history navigation, and page-ready events.
- Do not introduce a React/Next.js migration or large JS framework just to redesign this portfolio.
- Do not change biography, employment dates, years of experience, stats, repository links or projects without evidence and owner review.
- Do not submit real contact messages, disclose credentials, mutate production, change DNS or deploy without explicit permission.
- Work in a feature branch, preserve user changes, and provide tested evidence, screenshots and a concise changed-files summary.

The existing workflow deploys on pushes to main and creates Vercel previews on pull requests. Treat production deployment as explicitly out of scope.
