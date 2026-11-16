# Published skill inventory

This inventory describes **files actually shipped under `skills/`**, not every skill installed on a particular machine. It intentionally excludes user home directories, project workspaces, plugin caches, and private paths.

**44 published skills**: 37 retained upstream skills in `skills/matt-pocock/<skill-name>/` and seven original RezSat skills in `skills/rezsat/<skill-name>/`. The categories below help discover a workflow; category membership does not change its invocation name or prerequisites.

## Curated language and framework quality (RezSat originals)

- `go-quality` — idiomatic Go, errors, concurrency, testing, profiling
- `typescript-quality` — typed contracts, runtime validation, async safety, modules
- `nestjs-quality` — DI, DTO validation, auth, module boundaries, e2e tests
- `react-quality` — pure rendering, state/effects, accessibility, profiler-based optimization
- `nextjs-quality` — server/client split, router/version awareness, cache isolation, mutations
- `python-quality` — typing, packaging, resource safety, async, testing, profiling

These are **original distilled instructions**, not republished community skills. Each links to primary documentation and adapts to the target repository's version and tools. See [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md).

## Personal coding workflow (RezSat original)

- `capsule-workflow` — when coding starts, detect Capsule; install its official Codex plugin if missing; disable only the tested optional advisor ceiling with `CAPSULE_ADVISOR=0`; verify and use exact-recoverable context tools. See [its skill](skills/rezsat/capsule-workflow/SKILL.md).

## Planning, product discovery, and architecture

- `ask-matt`
- `codebase-design`
- `domain-modeling`
- `grill-with-docs`
- `grilling`
- `improve-codebase-architecture`
- `loop-me`
- `prototype`
- `research`
- `software-factory`
- `to-questionnaire`
- `to-spec`
- `to-tickets`
- `wayfinder`

## Implementation, review, and maintenance

- `code-review`
- `diagnosing-bugs`
- `implement`
- `implement-spec`
- `pr`
- `retro`
- `tdd`
- `triage`

## Reusable developer tooling

- `claude-handoff`
- `git-guardrails-claude-code`
- `handoff`
- `migrate-to-shoehorn`
- `setup-matt-pocock-skills`
- `setup-pre-commit`
- `setup-ts-deep-modules`
- `wizard`

## Agent operations, learning, and technical writing

- `chief-of-staff`
- `teach`
- `wait-what`
- `writing-beats`
- `writing-for-agents`
- `writing-fragments`
- `writing-shape`

## Portability decisions

| Decision | Reason |
| --- | --- |
| **Retain** the 37 skills listed above | They are reusable workflows or explicitly conditional on a common tool, language, or environment; they are not tied to a particular client application. |
| **Retain** TypeScript-specific `setup-ts-deep-modules` and `migrate-to-shoehorn` | Language and library specialization is acceptable when the dependency is stated and the skill works in different repositories. |
| **Retain** Claude Code and Husky workflows | These require named developer tools, not a particular customer or application. Use only where those tools are installed. |
| **Exclude** `scaffold-exercises` | It hardcodes one course's `exercises/XX-section/XX.YY-exercise` structure and `pnpm ai-hero-cli internal lint`; there is no general application-engineering use case that justifies publishing those assumptions. |
| **Exclude** project-local skills, user-installed plugin caches, and machine inventories | They are not shared application-building skills; redistribution rights and references to local workspaces also need independent review. |

## Review standard for future imports

Only add a skill if it can run in at least two unrelated codebases without edits to its instructions. If a valuable workflow has project-specific commands or paths, first replace them with repository discovery, configuration, or a clearly labeled optional adapter. If the core task is a single project's business process, leave it in that project's skill directory instead.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the submission checklist. For upstream details and original credit, see [Matt Pocock's source revision](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa).
