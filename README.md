# Agent Skills

Reusable agent workflows for engineering software across different applications and repositories. The library favors project-independent planning, architecture, implementation, testing, debugging, review, and developer tooling.

## Install

This repository uses the [Agent Skills specification](https://agentskills.io/specification).

With Node.js and npm:

```sh
npx skills add RezSat/agent-skills --skill tdd
```

Choose any published skill name from [INVENTORY.md](INVENTORY.md). For manual installation, copy the complete skill directory into a discovery root supported by your agent, such as `.agents/skills`, and refresh the client.

## Curated language and framework quality

Original, focused quality instructions are available for six technologies. They complement—not replace—the existing `tdd` and `code-review` workflows.

| Skill | Apply when |
| --- | --- |
| [`go-quality`](skills/rezsat/go-quality/SKILL.md) | Working with Go packages, APIs, jobs, or CLIs |
| [`typescript-quality`](skills/rezsat/typescript-quality/SKILL.md) | Working with TypeScript libraries, applications, or TSX |
| [`nestjs-quality`](skills/rezsat/nestjs-quality/SKILL.md) | Building NestJS controllers, services, or modules |
| [`react-quality`](skills/rezsat/react-quality/SKILL.md) | Building React components, hooks, or interactive UIs |
| [`nextjs-quality`](skills/rezsat/nextjs-quality/SKILL.md) | Building Next.js routes, rendering, caching, or server logic |
| [`python-quality`](skills/rezsat/python-quality/SKILL.md) | Building Python services, scripts, or libraries |

Use the base language skill with the relevant framework skill (for example, TypeScript + React + Next.js). Each skill inspects the project's versions and conventions first; none requires a fixed project structure or mandates new dependencies. For the selection rationale and source links, see [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md).

Install individually, for example: `npx skills add RezSat/agent-skills --skill go-quality`.

## What's included

- **General engineering:** discovery, architecture, domain modeling, implementation, testing, debugging, code review, and handoffs.
- **Language-specific, but reusable:** TypeScript module boundaries and Shoehorn test migrations.
- **Tool-specific, but reusable:** Claude Code Git hooks, Husky pre-commit setup, and tool-assisted workflows. These explicitly require their named tools.
- **Optional supporting workflows:** agent instruction writing, technical communication, and learning.

A skill belongs here when it works across unrelated projects after discovering the target repository's conventions. A task that assumes one app's directory layout, product terminology, internal CLI, or customer data does not belong here unmodified. See [CONTRIBUTING.md](CONTRIBUTING.md) for the generalization rules.

## Provenance

The third-party portion of this collection is a **curated subset** of [Matt Pocock's skills](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa) at revision `5863806dd4e15c63174bee4e7515a4256792ecfa`. The source is redistributed under its [MIT license](skills/matt-pocock/LICENSE); the existing YAML quoting fix is retained. The course-specific `scaffold-exercises` import was excluded because it requires a particular course layout and the `ai-hero-cli` tool. Other imported skills are left intact, including their original names and any tool requirements.

The source inventory previously included local machine paths, plugin caches, and project-only skills. Those were **not published as installable skills** and are not part of this collection. See [INVENTORY.md](INVENTORY.md) for the actual published set and exclusions. The six quality skills are original repository-authored instructions informed by official documentation and selected community workflow ideas; they are not copied imports. Repository-authored files use the [MIT license](LICENSE).

For `grill-me` (a separately distributed alias), use `npx skills add mattpocock/skills --skill grill-me`. Tool-provider skills such as Playwright CLI should be installed from their upstream providers rather than copied from a local cache.
