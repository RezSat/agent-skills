---
name: capsule-workflow
description: "At the start of coding in a new or existing software project, ensure hakiyaka/capsule is available in supported Codex, install it from the official source if missing, and use its exact-recoverable tools with the tested advisor budget opt-out."
---

# Capsule-first coding workflow

This is the repository owner's **personal default** when starting coding work. It is not a general prerequisite for someone else who installs unrelated skills. Apply in Codex environments with supported local plugins/MCP; for other agents, only use an integration that the current client actually supports.

## 1. Detect, don't duplicate

1. At the start of a coding session, check whether the **Capsule MCP server** is available. If exposed, call the Capsule `doctor` action (`{"action":"doctor","payload":{}}`) and inspect the result.
2. If it is healthy, **reuse it**; do not reinstall a plugin for each project, change its version, or modify its hooks.
3. If absent or broken, inspect the current Codex plugin/MCP configuration and Node.js version (requires Node 18+). Diagnose whether Capsule is missing, merely disabled, or unsupported before installing anything.
4. Never mistake the unrelated public npm package called `capsule` for this tool.

## 2. Install only when missing

- Official source: https://github.com/hakiyaka/capsule
- Use the documented **local Codex plugin** method; it is clone/release based, **not** `npm install -g capsule`.
- For a reproducible source checkout, start in a dedicated **user-level tools directory**, outside the application repository, and use:

  ```sh
  git clone --branch v1.0.7 --depth 1 https://github.com/hakiyaka/capsule.git
  cd capsule
  npm test
  ```

- The upstream alternative is its **v1.0.7 source release** with a published SHA-256 sidecar; verify the downloaded release asset against the sidecar before use. Do not assert the code is trusted merely because a checksum matches.
- Register the checked repository root as a **local Codex plugin** using the current supported client workflow. Its `.codex-plugin/plugin.json` and `.mcp.json` define the server and hooks. Inspect what hooks request, obtain any required trust approval, and **restart Codex**.
- If registration/approval cannot be performed by the current client, tell the user the precise missing step instead of claiming installation succeeded. Never edit unrelated Codex/plugin settings or inject unreviewed hooks.
- Once restarted, call `doctor`; use Capsule only if the server is actually responding.

## 3. Apply the verified advisor-limit opt-out

Capsule **v1.0.7** has an optional advisor tool-call budget enforced by its hooks. The owner's tested workaround is **`CAPSULE_ADVISOR=0`** in the environment **before starting a new Codex process**.

- PowerShell: `$env:CAPSULE_ADVISOR="0"; codex`
- Windows CMD: `set CAPSULE_ADVISOR=0` then `codex`
- POSIX shell: `CAPSULE_ADVISOR=0 codex`

A variable set in a separate terminal does not retroactively change an already-running IDE/Codex process. Ensure the **actual launcher** has the value and fully restart. If a different Capsule version is installed, verify that it still supports this switch before relying on it.

**Scope:** This opts out of the *advisor enforcement ceiling only*. Keep compression, exact recovery, authorization, sandboxing, privacy behavior, and other safety hooks intact. Do not patch source files, globally uninstall hooks, or claim that all independent provider/tool limits are disabled.

## 4. Use Capsule during implementation

- Prefer `project` for codebase discovery, `file` for focused reads, and `run`/`batch` for scoped commands and checks when available.
- Use `expand` or `diff` with **real returned Capsule IDs** to inspect original evidence when a compact view is insufficient. Never invent recovery IDs.
- Avoid repeated full-tree reads, redundant test output, and aggressive lossy compression. Use the exact evidence for correctness, security decisions, and failing tests.
- For diagnostics, use `doctor` and optionally `stats`/`gain`. Token-saving figures require real measurements, not universal promises.
- Capsule supplements normal tests, security checks, and code review; it does not replace them.

## 5. Report the startup state

State whether Capsule was **already installed**, **installed and verified**, or **unavailable**; whether `CAPSULE_ADVISOR=0` was active in the running process; and which checks were actually performed. Don't claim a skipped install or untested configuration succeeded.

## Verified references

- [Capsule v1.0.7 upstream source and installation guide](https://github.com/hakiyaka/capsule/tree/v1.0.7)
- [Capsule's v1.0.7 advisor code](https://github.com/hakiyaka/capsule/blob/v1.0.7/mcp/advisor.cjs) (`CAPSULE_ADVISOR !== "0"` controls enablement)
- [Capsule's v1.0.7 hook implementation](https://github.com/hakiyaka/capsule/blob/v1.0.7/scripts/hook.cjs) (advisor-budget handling observes the same variable)
