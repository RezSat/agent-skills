# Layro workflow verification

Use these synthetic prompts with the actual coding agent when changing the skill. Provide an appropriate fixture or existing test project and record tool calls, changed files, commands and observed outcomes. Do not use customer code or credentials in fixtures. A written walkthrough is not a passing live-agent test.

| Scenario | Expected observable behavior |
| --- | --- |
| React app already has a suitable accessible date picker | Inspect local implementation and reuse it; no redundant registry install. |
| Next.js app needs a rich AI composer and Layro MCP works | Search, compare candidates, inspect source and install plan, review licence/dependencies, adapt selected component, record provenance, and test real inputs and responses. |
| MCP unavailable or OAuth denied | Request approval before global setup or authentication; after denial, use a safe public CLI or local fallback without repeated setup attempts. Report the limitation. |
| Registry component includes unexplained remote requests, missing source, or incompatible licence | Reject it; do not execute or install it. Continue with a safer candidate or local implementation. |
| Bespoke responsive landing page with strict visual reference | Preserve layout and tokens; adapt only useful catalog behavior, inspect desktop/mobile screenshots and verify interactions. |
| Component requires a large new library for a minor effect | Compare a local implementation; avoid unnecessary dependency or document trade-off and obtain approval when required. |
| Existing component is updated upstream | Review source changes against the recorded version; preserve local adaptations and licence notices; rerun relevant checks. |
| Native Rust app or non-React app | Skip Layro integration; use the appropriate project workflow. |
| Browser or build environment unavailable | State exactly what could not run and why; do not claim visual or production verification. |

For a successful installation case, verify the final diff and lockfile contain only intended changes, the source provenance is recorded, controls are wired to real application behavior, and actual rendered screenshots plus interaction assertions were collected. For rejection or fallback cases, verify no unauthorized configuration changes or unnecessary dependencies were introduced.

Record agent/client version, skill revision, fixture, scenario, observed evidence, pass/fail/not run, and outstanding risks. Run at least two unrelated React fixtures before claiming cross-project behavior; exercise the missing-access and non-React paths before claiming broad portability.
