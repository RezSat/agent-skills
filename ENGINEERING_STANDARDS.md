# Engineering standards: curation record

This repository adds **six concise, original quality skills** for the languages and frameworks used in application development. They are instructions that an agent can execute against an unfamiliar repository; they do not install linters, overwrite configurations, or assert that every project must use the same structure.

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
| React web app | `typescript-quality` + `react-quality` (for TSX) | TS core + component state, effects, accessibility |
| Next.js app | `typescript-quality` + `react-quality` + `nextjs-quality` (for TSX) | TS core + React UI + Next routing/server/cache semantics |
| Python app | `python-quality` | Python language, runtime, packaging, and async correctness |

For a feature, bug, or PR, invoke existing `tdd`, `diagnosing-bugs`, and `code-review` as appropriate; the quality skill supplies language-specific guardrails **inside** that workflow. An agent should load only the applicable skills rather than combining all six in every task.

## Curated inclusion rules

1. **Applicable across unrelated applications.** No client names, personal paths, deploy credentials, proprietary CLIs, or hardcoded project folder layouts.
2. **Version-aware, inspect first.** Detect frameworks, runtime versions, test tools, compiler settings, and conventions before changing code.
3. **High-signal rules.** Prefer correctness and proven failure modes over boilerplate, style preferences, or generic slogans.
4. **Trade-offs, not absolutes.** Strong typing and validation are defaults, but expensive global refactors, caching, memoization, and concurrency require evidence.
5. **Executable verification.** End with relevant commands, observable behavior, limitations, and measurement evidence.
6. **No upstream transcription.** Instructions are independently authored; community sources are credited as inspiration and official sources are linked for changing technical claims.

## Maintenance

Recheck official documentation when framework major versions change, especially Next.js caching/rendering and React Compiler integration. Do not blindly synchronize upstream community skills; propose individual improvements only with a specific behavior or failure they address. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and run `python scripts/validate-skills.py`.
