---
name: engineering-delivery
description: "Execute coding tasks like a responsible software engineer: discover the real system, define acceptance contracts, implement complete vertical slices, test actual behavior, review the diff, and report verifiable evidence. Use for features, fixes, refactors, integrations, and PR delivery in any stack."
---

# Evidence-driven engineering delivery

Use for **non-trivial implementation and review tasks**, independently of language or agent harness. The project's instructions, security constraints, approved architecture and user requirements take precedence. This skill orchestrates work; it does not replace `tdd`, `diagnosing-bugs`, `code-review`, or a language/framework skill.

**Definition of done: requested behavior works through the real application boundary, relevant regressions are checked, and claims match recorded evidence.** Code volume, impressive screenshots, and a green formatter are not acceptance criteria.

## 1. Locate the real task and boundaries

- Inspect `AGENTS.md`, product/spec/issue and comments, architecture/ADRs, current branch and dirty tree, neighboring implementation, tests, dependencies, and CI. Prefer reading code over guessing APIs.
- Record a short **acceptance contract**: starting condition; input/action; expected observable result; failure/cancellation behavior; what remains unchanged; and evidence to collect. For a bug, first reproduce it or capture a credible failing test/trace. For ambiguous behavior, surface the decision and a reversible assumption rather than inventing product requirements.
- Identify affected boundaries: data ownership and persistence, API/auth, files, UI and accessibility, external services, deployment. Define non-goals and risks. Make a plan proportional to the task; don't turn a two-line bug into a ceremony.
- Check current tests and toolchain before changing them. Confirm breaking changes and data migrations explicitly; never overwrite unrelated work or silently switch framework.

## 2. Design to solve the requirement, not to look sophisticated

- Choose the smallest cohesive change that spans the **actual** user path. Preserve established interfaces and conventions; write an ADR only for consequential, hard-to-reverse decisions.
- Separate domain rules from UI/transport and external I/O where this reduces coupling. Make ownership, invariants, validation, error mapping, cancellation, and retry/idempotency explicit where the problem needs them.
- Verify unfamiliar APIs in **official source/docs at the installed version**. A plausible method name is not evidence it exists.
- Reject speculative interfaces, generic factory layers, ornamental design systems, unnecessary dependencies, sprawling refactors, and cut-and-paste logic. Abstractions must pay for themselves with a current use case.

## 3. Implement a complete vertical slice

1. Add or update an executable test that expresses the acceptance contract; for bugs, ensure the regression test fails for the original defect when feasible.
2. Implement the smallest production path: input → validation → domain behavior → real state/side effect → truthful user-visible result. Verify it end to end before multiplying components.
3. Handle empty/loading/error/cancel/denied/timeout states that actually apply. Keep UI controls connected to working behavior. A mocked adapter is fine in a clearly labeled **prototype** or an isolated test, never silently substituted for production integration.
4. Inspect each incremental diff, run relevant checks, and revise. Do not declare success because a unit test passes while the integration is unimplemented.
5. Do not replace errors with empty catches, use `unwrap`/`expect` on expected external failures, disable static checks, leak secrets to logs, or hide incomplete behavior behind a success screen. A deliberate exception needs a specific justification.

## 4. Verification matrix — evidence over theatre

Choose checks based on the change's risk, then **run** what the environment permits:

| Surface touched | Minimum meaningful proof |
| --- | --- |
| Business logic | Edge cases, invalid inputs, invariants and regression assertions |
| API/integration | Request/response contract, auth/authorization, timeouts, retries and real or contract-test transport |
| Persistence | Migration/rollback strategy, restart consistency, corrupt/missing data where relevant |
| UI | Screenshot/visual comparison **plus** scripted user journey, interaction assertions, keyboard and accessibility |
| Concurrency/background work | Cancellation, ownership, bounded work, race/reentrancy and shutdown |
| Security-sensitive work | Threat boundaries, least privilege, secrets/PII handling, dependency exposure |
| Performance claim | Representative baseline, controlled after-measurement and trade-off |
| Release | Target-platform build/smoke, configuration, deployment/package checks when in scope |

Run formatter, type/compile checks, lint and the relevant test suite. Use the repo's commands, not fictitious generic ones. Check that new tests actually execute in CI. For desktop Rune tasks, load [rune-desktop](../rune-desktop/SKILL.md) and follow its headless **and** native verification contract.

If a check cannot run, state **not run: reason** and the resulting risk. Never invent an execution log, CI result, benchmark, screenshot inspection or reviewer approval.

## 5. Independent review before delivery

Inspect `git diff` against the agreed base (and `git status`). Review separately:

- **Spec axis:** every required action/state/error case implemented? Any hardcoded demo response, missing wiring, scope creep, broken contract or accidental behavior change?
- **Engineering axis:** correctness, readability, invariants, API fit, security, accessibility, test coverage, cleanup, operational impact, rollback, and unnecessary complexity.

Fix high-severity findings; prefer a focused PR on a feature branch. Never merge or deploy without the repo's authorization. Include a concise PR body describing behavior, risks, changed contracts, tests and manual verification. Handoffs must include exact branch/ref, changed files, evidence and unresolved work—not a narrative that assumes the next agent remembers the chat.

## Anti-slop rejection gate

Stop and revise if the deliverable contains dead controls, fake production data, unhandled foreseeable errors, unjustified stubs/TODOs on accepted functionality, invented APIs, absent behavioral tests for a behavior change, hidden failed checks, or a broad unrelated rewrite. Don't add boilerplate files only to satisfy a list; every file must have a concrete responsibility.

For explicitly requested prototypes or exploratory spikes, lighter verification is acceptable **when clearly labeled**. The output still must be honest about what is simulated and what works.

## Delivery format

Report (1) implemented behavior versus acceptance criteria, (2) files/architecture changed and why, (3) exact commands and observed pass/fail results, (4) end-to-end/manual checks and environment, (5) known limitations and unverified surfaces, and (6) branch/PR or artifacts. Separate **implemented**, **verified**, and **not yet verified**. No vague "fully tested" or "production ready" assertion without the required evidence.
