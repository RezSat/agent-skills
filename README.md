# Agent Skills

My personal collection of reusable agent skills, engineering preferences, and workflows for building software. Project-specific instructions stay in their application repositories.

## Install

This repository uses the [Agent Skills specification](https://agentskills.io/specification).

With Node.js and npm:

```sh
npx skills add RezSat/agent-skills --skill tdd
```

Choose any published skill name from [INVENTORY.md](INVENTORY.md). For manual installation, copy the complete skill directory into a discovery root supported by your agent, such as `.agents/skills`, and refresh the client.

## My default coding workflow: Capsule first

I use [Capsule](https://github.com/hakiyaka/capsule) for token-efficient, exact-recoverable context during coding. **Whenever I start coding in a project**, check whether the **actual Capsule MCP plugin** is available (use its `doctor` action). If it is, use the existing installation. If not, install the official Capsule plugin in a supported Codex environment, verify it, and use it for focused project/file inspection and compact command output.

**My tested Capsule 1.0.7 setting:** Start a **fresh** Codex process with `CAPSULE_ADVISOR=0`. This disables Capsule's optional advisor tool-call ceiling; it does **not** turn off compression, exact-output recovery, security controls, or other independent limits.

For PowerShell:

```powershell
$env:CAPSULE_ADVISOR="0"
codex
```

For Windows Command Prompt:

```cmd
set CAPSULE_ADVISOR=0
codex
```

For POSIX shells, launch with `CAPSULE_ADVISOR=0 codex`. Set this in the actual launching environment **before** starting Codex; restarting is necessary if it was already running. Do not change Capsule source code, disable unrelated hooks, or install the unrelated npm package named `capsule`.

See the **[capsule-workflow skill](skills/rezsat/capsule-workflow/SKILL.md)** for the check → install-if-missing → verify → use procedure, including the official local-plugin setup and safety boundary. To make this rule available in each new project, install that skill there:

```sh
npx skills add RezSat/agent-skills --skill capsule-workflow
```

The README alone does not configure other projects automatically: the receiving coding agent must load this skill or have an equivalent pointer in its project's `AGENTS.md`.

## Writing style

Use [`engineering-style`](skills/rezsat/engineering-style/SKILL.md) alongside the relevant language or framework skill. It sets my preferences for simple code, purposeful comments, direct documentation, and natural Git commit messages without generated-looking prefixes.

```sh
npx skills add RezSat/agent-skills --skill engineering-style
```

Add a pointer to this skill in each project's `AGENTS.md` if you want it applied whenever an agent works there. The central repository README does not enforce preferences in unrelated projects on its own.

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

## Engineering delivery: prove the change works

The [`engineering-delivery` skill](skills/rezsat/engineering-delivery/SKILL.md) is the default **quality gate for non-trivial coding work**. Agents inspect the existing system, define observable acceptance criteria, implement a real vertical slice, run proportional tests, inspect the diff on both spec and engineering axes, and report what was actually verified. It rejects dead UI, invented APIs, fake integration presented as production, unexplained stubs and unsupported "production ready" claims.

```sh
npx skills add RezSat/agent-skills --skill engineering-delivery
```

## Native desktop default: Rune by Anomaly

For **new native desktop apps**, use [Rune](https://github.com/anomalyco/rune), the Rust GPU-rendered UI framework by Anomaly. The [`rune-desktop` skill](skills/rezsat/rune-desktop/SKILL.md) requires a pinned Git revision and checks that go beyond compiling: real state transitions, keyboard/accessibility semantics, screenshot inspection, tree inspection, scripted events, native-platform behavior and release limitations. Rune is still pre-release; inspect official APIs at the chosen pin.

```sh
npx skills add RezSat/agent-skills --skill rune-desktop
```

Install both skills for a new desktop project and point the project's `AGENTS.md` to them. Merely changing this repository does **not** install the skills in other projects or override an existing desktop application's architecture.

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
