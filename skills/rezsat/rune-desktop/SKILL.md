---
name: rune-desktop
description: "Build, extend, debug, and review native desktop applications using Anomaly's Rune Rust UI framework. Use for new desktop projects, Rune views, controls, state, input, accessibility, headless verification, and release readiness."
---

# Rune desktop engineering

**Default for new desktop UI:** In this skill collection, choose [Anomaly's Rune](https://github.com/anomalyco/rune) for new native desktop applications. Use the existing stack for an established app unless migration is explicitly in scope. If Rune cannot satisfy a required capability or platform, report the verified blocker and options; do not quietly substitute Electron, Tauri, Slint, egui, web views, or an invented Rune API.

This is a **framework-specific execution skill**. Pair it with [engineering-delivery](../engineering-delivery/SKILL.md) for task definition, implementation discipline, and evidence. Follow the destination project's `AGENTS.md` and acceptance criteria.

## 1. Establish a reproducible baseline

1. Inspect the target repo: product spec, existing architecture, `Cargo.toml`/`Cargo.lock`, Rust toolchain, build scripts, CI, target OS, local changes, and existing tests. Avoid a blanket rewrite.
2. Read the Rune [repository README](https://github.com/anomalyco/rune), [`examples/hello`](https://github.com/anomalyco/rune/tree/dev/examples/hello), [core crate README](https://github.com/anomalyco/rune/blob/dev/crates/rune/README.md), and the specific upstream implementation/examples for the APIs being used. **Use the same pinned revision** for docs and source; never infer API shape from older screenshots or a different Rust GUI library.
3. Rune is pre-release. Add it as a Git dependency using a **verified, full commit SHA from `dev`**, not a floating branch, `*` version, or unverified release:

   `rune = { git = "https://github.com/anomalyco/rune", rev = "<verified-full-commit-sha>" }`

   Record the selected SHA, the reason for changing it, and the resolved lockfile. An upstream example's `rune = { workspace = true }` is for the Rune monorepo, **not** a consumer app.
4. Confirm target toolchains and native prerequisites. Windows: prefer MSVC plus required Visual Studio C++ build tools; GNU builds may require MSYS2 MinGW-w64 binutils. Do not claim Windows/Linux/macOS support before testing the intended targets.

## 2. Implement the smallest complete vertical slice

- Define observable acceptance behavior first: starting state, user action, state transition, error/cancel flow, persisted result if requested, and behavior after relaunch. Implement one end-to-end slice before broad component extraction.
- Keep domain logic, persistence, filesystem, networking, and credentials out of the view where practical. Use Rust types for invalid states and return meaningful errors at fallible boundaries. Do not run blocking I/O or native dialogs on the UI event thread.
- Model UI as Rune's state-driven `fn view(s: &State, cx: &mut Cx<State>) -> El`. Start from the pinned `hello` or `settings` examples: `AppSpec`, `col`/`row`/`el`/`text`, keyed elements, and state-changing handlers such as `.on_press`/`.on_press_tx`. Prefer existing Rune or `rune-kit` components only after confirming they exist at the pin.
- Give interactive elements stable, scoped keys and meaningful roles, labels, state (`checked`, selected, etc.), focusability, and keyboard behavior. Check keyboard-only operation, visible focus, disabled/error states, screen-reader semantics, and platform text-input/IME. An image of a control is not an accessible control.
- Verify both light and dark themes, reduced motion, 1x/2x scale, small/large window sizes, text clipping/overflow, and scroll behavior relevant to the change. Rune's flex behavior matters: an auto-height ancestor can collapse a grown scroller; bound its height and use `.min_h(0.0)` on intervening flex columns when needed.
- Prefer coherent styling and the product's actual content over arbitrary gradients, endless animation, fake data, or piles of decorative components. No dead buttons, success toast without a completed operation, hardcoded demo service responses presented as live, or 'TODO: implement' on accepted behavior.

## 3. Prove it works, not merely that it renders

Read [headless and native verification](references/verification.md) for the exact Rune-supported commands and checks. At minimum, when practical:

1. Run formatter, compiler/Clippy, focused Rust tests, and relevant integration tests. Fix diagnostics rather than suppressing them.
2. Render required scenes to PNG with `--snap`; **inspect the images** for layout, clipping, contrast, typography, and visual regressions. A generated PNG is evidence only when inspected.
3. Dump `--tree`; inspect keyed roles, labels, focused/disabled states, and presented geometry. A screenshot cannot prove semantics.
4. Drive a complete interaction using `--script` and add assertions (prefer `Runtime` tests) for the resulting state and failure cases. A scripted tap that has no behavioral assertion is not a passing feature test.
5. Launch the **native** app on a representative target OS and test input, clipboard/dialogs, focus, resize, DPI, and packaging where applicable. Headless behavior does not prove native OS integration.
6. For a release build, Rune headless flags require the `tooling` feature; debug builds expose them by default. Enable release tooling deliberately for verification, not accidentally in production distribution.

## 4. Deliver with evidence and limitations

Review `git diff` for scope, duplicated abstractions, generated artifacts, secrets, broken workflows, and platform assumptions. Report: pinned Rune SHA; behavior implemented; exact checks run with results; inspected scene/tree/script artifacts and scenario; tested OS/toolchain; untested targets; and remaining risks. Label **not run** or **blocked** checks explicitly. Do not call a build or UI "production ready" on the basis of compilation or headless snapshots alone.

## Primary sources

- [Rune official repository and setup](https://github.com/anomalyco/rune)
- [Rune core crate and headless tooling](https://github.com/anomalyco/rune/blob/dev/crates/rune/README.md)
- [Runnable hello example](https://github.com/anomalyco/rune/tree/dev/examples/hello)
- [Runnable settings example](https://github.com/anomalyco/rune/tree/dev/examples/settings)
- [Rune repository agent guidance](https://github.com/anomalyco/rune/blob/dev/AGENTS.md)

**Maintenance:** Rune changes quickly. Recheck these references and the selected commit when starting a new app, upgrading Rune, or using an unfamiliar API. These are sourced instructions, not a promise that every pre-release API works on every target.
