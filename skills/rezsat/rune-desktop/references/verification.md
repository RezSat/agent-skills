# Rune verification protocol

This is an **execution guide**, not a claim that this skill's repository contains a buildable Rune app. Commands below reflect [Anomaly's Rune core documentation](https://github.com/anomalyco/rune/blob/dev/crates/rune/README.md) and [`examples/hello`](https://github.com/anomalyco/rune/tree/dev/examples/hello), reviewed 2026-11-22. Check command and API compatibility at the chosen pinned SHA.

## Set the target first

Discover the app's actual Cargo package and runnable binary. In the commands below replace `<app>` with that package and `artifacts/rune` with a disposable output directory. Create the directory before saving files; don't commit generated captures unless the project intentionally versions visual fixtures.

A Rune **debug** binary accepts headless flags. A release binary needs the `rune` dependency's `tooling` feature enabled. On a release build missing that feature, headless flags intentionally fail. Keep a separate verification build/profile rather than shipping tooling without a reason.

## Minimum reproducible evidence

```sh
cargo fmt --all -- --check
cargo check --workspace --all-targets
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
mkdir -p artifacts/rune

# Run the app's actual binary with Rune's flags:
cargo run -p <app> -- --list-scenes
cargo run -p <app> -- --snap artifacts/rune/default.png --size 800x600 --scale 2 --theme dark
cargo run -p <app> -- --tree artifacts/rune/default.json
```

Use an app-defined `--scene NAME` if it has registered scenes (don't assume "default" exists). Repeat snapshots at the relevant narrow/wide sizes, light/dark themes, and scale factors. Compare against the approved design or baseline, not an AI-generated imagined design.

Record for each tested state:

| Dimension | Required observation |
| --- | --- |
| Visual | PNG inspected: correct spacing, typography, contrast, clipping, overlay and scrolling |
| Semantics | Tree inspected: unique/scoped keys, roles, labels, control values, focus, enabled/disabled |
| Interaction | User action reaches the intended element and produces the expected state/side effect |
| Failure | Invalid input, unavailable resource, cancel/retry, denied permission handled meaningfully |
| Native | Tested OS, DPI, IME, keyboard, dialogs, file paths, window lifecycle and distribution as applicable |

## Scripted input is not an assertion

Rune scripts use timestamped events. For a view with an actual `switch` key, a minimal example is:

```json
{"events":[{"t":0.1,"type":"tap","key":"switch"}]}
```

For the app's own registered key and fixture, replay and inspect the result:

```sh
cargo run -p <app> -- --script tests/ui/toggle.json --snap artifacts/rune/after-toggle.png
cargo run -p <app> -- --script tests/ui/toggle.json --tree artifacts/rune/after-toggle.json
```

Tests and fixtures must exist in the **destination app**. Never report this example as executed until you create those fixtures and run the commands. Use a `Runtime` test to assert state, geometry, keyboard or event outcomes rather than treating an image export as a behavioral pass. The upstream hello example uses `Runtime::new`, `frame`, `find` and pointer events; inspect its current source before adapting that test.

Where the application needs multi-step verification, use headless `--script` with keyed input and deterministic time; inspect traces when animation behavior matters. Screenshots and semantic trees complement each other but do not replace native integration testing.

## Explicit release/OS gates

- **Windows:** test MSVC build prerequisites, keyboard/IME, scaling, notifications and file dialogs used by the app. Rune documents additional binutils prerequisites for GNU targets.
- **macOS:** test app activation/close/reopen behavior, keyboard shortcuts, IME, signing/notarization where distribution requires them.
- **Linux:** test the intended Wayland/X11 environments and desktop portal integrations; screenshots alone do not establish portal or clipboard support.
- **Every shipping OS:** check first launch, permission denial, no-network/failure mode, persistence/restart, high-DPI resizing, and a packaged artifact if distributing an installer.

If a platform or check is unavailable, report **not tested**, not pass. Distinguish an upstream framework limitation from a defect in the app and record a reproducible issue or workaround.
