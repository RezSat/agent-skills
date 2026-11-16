---
name: go-quality
description: "Write, refactor, or review production Go code for idiomatic APIs, predictable errors, safe concurrency, testability, security, and measured performance. Use for Go packages, services, CLIs, and libraries."
---

# Go engineering quality

Apply to Go code changes; work with the repository's existing architecture instead of imposing a universal directory tree. This is a **language-specific quality layer**, not a replacement for feature planning, TDD, or code review.

## Inspect before changing code

1. Read `go.mod`, the Go version, adjacent packages and tests, README, CI, and any project conventions. Check whether generated code, database layers, or a framework own the touched files.
2. Identify the public behavior and failure modes the change must preserve. Prefer a focused diff over a broad cleanup.
3. Use standard-library capabilities before adding a dependency. Do not introduce a framework or `pkg/` / `internal/` structure just to satisfy a template.

## Write idiomatic Go

- Run `gofmt`. Use concise, descriptive package names; exported identifiers deserve useful doc comments. Avoid Java/C#-style getters and redundant names (for example, a package's name need not appear in every exported type).
- Favor small, cohesive packages and simple functions. Define interfaces at the **consumer** boundary when multiple implementations or testing justify them; do not manufacture interfaces for every struct.
- Return errors instead of panicking for expected failures. Check errors, wrap with meaningful operation context using `%w` when callers need the cause, and test behavior with `errors.Is` or `errors.As`. Never leak credentials or sensitive payloads into error messages.
- Accept `context.Context` as the first argument of request-scoped operations; propagate cancellation and deadlines through network/DB calls. Do not store request contexts on long-lived structs.
- Make ownership of mutable state and resources explicit: close files, response bodies, and SQL rows; check `rows.Err()`; respect connection timeouts; use parameterized database queries.
- Prefer straightforward synchronous code. For each goroutine document how it terminates, handles cancellation and errors, and whether concurrency is bounded. Synchronize access to shared state; channels do not automatically prevent races.
- Keep exported APIs small, consistent, and backwards-compatible unless the task explicitly calls for breaking changes.

## Optimize only from evidence

- Choose a representative benchmark or production metric first. Diagnose algorithmic complexity, IO, DB queries, allocations, lock contention, and goroutine leaks **before** micro-optimizing.
- Use `go test -bench . -benchmem` for appropriate benchmark packages and pprof when sampling real hotspots. Record baseline and after values on comparable inputs. Do not claim a speedup without measurements.
- Reject clever pooling, concurrency, or premature caching when it complicates correctness more than it improves a measured bottleneck.

## Required evidence

- Format changed Go files; if practical check `gofmt -l` for zero results.
- Run `go test ./...` and `go vet ./...`, scoped appropriately in large monorepos. Run `go test -race ./...` when concurrency is involved and the platform supports it.
- Include tests for happy path, boundary inputs, errors, cancellation/timeouts, and concurrent access where relevant. Preserve failing regression tests for bugs.
- Run `govulncheck ./...` if installed or required by CI; never assert a security scan ran if it did not.
- Report changed behavior, commands executed, outcomes, and any skipped checks with reasons.

## Primary references

- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)
- [Effective Go](https://go.dev/doc/effective_go)
- [Go Test Comments](https://go.dev/wiki/TestComments)
- [Go diagnostics](https://go.dev/doc/diagnostics)
