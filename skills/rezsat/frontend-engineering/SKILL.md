---
name: frontend-engineering
description: "Plan and implement production-quality web frontends in existing React, Next.js, and TypeScript projects. Use at the start of frontend work to select the right engineering skills, check Layro component access, and establish the project's UI conventions before implementation."
---

# Frontend engineering workflow

Use this as the entry point for frontend feature work, new React web projects, UI refactors, and frontend reviews. Discover the target repository first. Do not impose a framework, component library, architecture, or dependency that the project does not need.

## 1. Discover the project

- Inspect the package manifest, lockfile, scripts, framework and React versions, routing model, styling system, design tokens, existing component library, test setup, and repository instructions.
- Identify whether this is an existing application or a new project. Preserve an established architecture unless the task requires a deliberate change.
- Confirm the actual user path, responsive requirements, data source, loading/error/empty states, and accessibility expectations before building.

## 2. Load focused engineering skills

Load only the applicable skills from this collection:

- `typescript-quality` for TypeScript and TSX contracts.
- `react-quality` for React components, hooks, state, effects, accessibility, and rendering behavior.
- `nextjs-quality` for Next.js routing, server/client boundaries, caching, and mutations.
- `layro-ui` when a React web UI could benefit from reusable catalog components.
- `engineering-delivery` for substantial features, fixes, or refactors; use `tdd` and `code-review` where their focused workflows apply.

Do not load unrelated language or platform skills. Layro is for React web UI, not a default for native desktop or non-React projects.

## 3. Check Layro before implementing reusable UI

For a React web project, decide whether the requested interface contains a meaningful reusable component candidate. If yes, invoke `layro-ui` before writing that UI.

- Verify that the active coding agent has working Layro MCP access.
- If access is missing, configure the active client using the official Layro instructions and complete OAuth when required. For Codex, use `codex mcp add layro --url https://mcp.layro.dev`, then `codex mcp login layro`, and verify with `codex mcp list` plus a real search.
- Search for relevant components, inspect source, dependencies, and licence, then install only suitable components.
- If the user must approve authentication or the environment prevents setup, ask for the required action and state the blocker. Do not claim that Layro is connected when it is not.
- If no suitable component exists, proceed with the project's existing design system and implement it locally. Do not delay unrelated backend or setup work while looking for a component.

## 4. Build the actual product UI

- Establish or follow the product's visual language: hierarchy, typography, spacing, color, surfaces, density, and interaction patterns.
- Prefer small, cohesive components and explicit state. Keep server data, URL state, shared state, and transient UI state distinct.
- Use semantic elements and accessible interactions. Include keyboard, focus, responsive, reduced-motion, and error behavior.
- Wire every visible control to real behavior. Do not ship decorative controls that appear functional but do nothing.
- Avoid speculative abstractions, unnecessary dependencies, and generic dashboard filler.

## 5. Verify the user journey

- Run the relevant lint, typecheck, unit/integration tests, and production build.
- Exercise the important user path at realistic viewport sizes, including loading, empty, error, and success states.
- Check keyboard navigation, focus, accessible names, and interaction feedback.
- Inspect the final diff and remove unused demo code, accidental configuration churn, and unnecessary dependencies.
- Report observable behavior, exact checks and results, and any remaining limitations. Never claim visual or accessibility verification that was not performed.

## Project handoff

When this skill is installed in a project, reference it from that project's `AGENTS.md` so future sessions load it. Installing this skill in the central skills repository does not automatically install it into unrelated repositories.
