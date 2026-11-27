# Engineering standards: curation record

This repository has **six original language/framework quality skills**, **two frontend workflow skills**, and **two original execution skills**: `engineering-delivery` for evidence-based software delivery and `rune-desktop` for native desktop applications built with Anomaly's Rune. The frontend workflows route React web work through project discovery and Layro component reuse. They are instructions that agents can execute against unfamiliar repositories; they do not install linters, override project architecture, or pretend that a documented process is proof of implementation.

## Research inputs and selection

The following community catalogs were **reviewed as research**, not copied wholesale:

- [samber/cc-skills-golang](https://www.skills.sh/samber/cc-skills-golang) — many focused Go topics, especially correctness, concurrency, performance, and testing. We combined the portable, high-value ideas into **one Go skill** instead of importing dozens of mutually overlapping commands.
- [Addy Osmani's agent skills](https://skills.addy.ie/) — useful production thinking: verify changes, perform accessibility/security reviews, and measure before optimizing. Existing `tdd` and `code-review` skills already cover much of its lifecycle, so we **did not duplicate** those skills.

**Primary documentation takes precedence over opinionated community instructions.** The individual skills link to official documentation from Go, TypeScript, NestJS, React, Next.js, Python, W3C, and the Python packaging ecosystem. For example, Go does not require arbitrary fixed line lengths, React performance shouldn't be handled with indiscriminate memoization, and Next.js cache behavior must be checked against the installed framework release.

## How to combine skills without duplication

| Context | Load | Responsibility |
| --- | --- | --- |
| Go backend or CLI | `go-quality` | Go language and runtime choices |
| TypeScript library / service | `typescript-quality` | Type safety, runtime boundaries, async and API contracts |
| NestJS API | `typescript-quality` + `nestjs-quality` | TS core + Nest lifecycle, validation, providers and auth |
| React web app | `frontend-engineering` + `typescript-quality` + `react-quality` | Frontend discovery and Layro check + TS core + React UI behavior |
| Next.js app | `frontend-engineering` + `typescript-quality` + `react-quality` + `nextjs-quality` | Frontend discovery and Layro check + TS core + React UI + Next routing/server/cache semantics |
| Python app | `python-quality` | Python language, runtime, packaging, and async correctness |
| Feature, fix, refactor or PR | `engineering-delivery` plus the relevant language skill | Acceptance behavior, vertical-slice implementation, evidence, independent spec and engineering review |
| New native desktop app | `engineering-delivery` + `rune-desktop` | Rune is the preferred UI framework; pinned upstream commit, stateful interactions, headless scene/tree/script verification and native OS testing |

For a React web UI with reusable component needs, `frontend-engineering` invokes `layro-ui` before implementing that UI. The Layro skill verifies working MCP access, follows official setup and OAuth instructions when needed, searches and inspects candidate components, checks licences and dependencies, and verifies integration. It does not apply to non-React or native desktop projects, and does not force a component when no suitable match exists.

For a feature, bug, or PR, invoke existing `tdd`, `diagnosing-bugs`, and `code-review` as appropriate; the quality skill supplies language-specific guardrails **inside** that workflow. An agent should load only the applicable skills rather than combining all six in every task.

## Curated inclusion rules

1. **Applicable across unrelated applications.** No client names, personal paths, deploy credentials, proprietary CLIs, or hardcoded project folder layouts.
2. **Version-aware, inspect first.** Detect frameworks, runtime versions, test tools, compiler settings, and conventions before changing code.
3. **High-signal rules.** Prefer correctness and proven failure modes over boilerplate, style preferences, or generic slogans.
4. **Trade-offs, not absolutes.** Strong typing and validation are defaults, but expensive global refactors, caching, memoization, and concurrency require evidence.
5. **Executable verification.** End with relevant commands, observable behavior, limitations, and measurement evidence.
6. **No upstream transcription.** Instructions are independently authored; community sources are credited as inspiration and official sources are linked for changing technical claims.

## Engineering execution policy

For substantial code changes, use [engineering-delivery](skills/rezsat/engineering-delivery/SKILL.md) to require working user paths and honest verification. It rejects unwired controls, fake production integrations, untested success claims, invented APIs, hidden failed checks and unnecessary abstraction. Existing TDD, debugging and review skills still own their focused techniques; the delivery skill supplies the common acceptance contract and exit criteria.

For **new native desktop interfaces**, default to [Rune](skills/rezsat/rune-desktop/SKILL.md) from [Anomaly](https://github.com/anomalyco/rune). Rune is pre-release; pin a full Git commit and check source/examples for that version. Headless screenshots, semantic trees and scripted events are unusually useful for agent verification, but they do **not** replace native-platform smoke tests, IME, accessibility, permission and packaging checks. Do not silently migrate an established app or change stacks to avoid a blocker.

No skill can force its use in a separate project until the target agent loads it (for example, install the skills and reference them in that project's `AGENTS.md`). These are portable defaults, not magic repository-wide enforcement.

## Maintenance

Recheck official documentation when framework major versions change, especially Next.js caching/rendering and React Compiler integration. Recheck Layro's MCP and CLI instructions before changing setup commands. Do not blindly synchronize upstream community skills; propose individual improvements only with a specific behavior or failure they address. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and run `python scripts/validate-skills.py`.
