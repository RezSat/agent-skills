---
name: python-quality
description: "Write, refactor, or review maintainable, typed, safe, testable Python applications and libraries with sensible packaging, resource management, and measured performance."
---

# Python engineering quality

Use for Python services, scripts, libraries, workers, and data-processing projects. Follow the repository's supported Python versions and ecosystem rather than imposing a new framework or package manager.

## Inspect the environment

1. Read `pyproject.toml`, lock files, runtime version, dependency manager, format/lint/type tools, tests, and CI. Determine whether this is an application, package, notebook workflow, or script.
2. Identify public contracts, input shapes, IO and network operations, and failures to preserve. Keep the change narrowly scoped.
3. Honor current formatting and typing tools; do not install Ruff, mypy, pyright, pytest, or a new build backend unasked in an existing mature repo.

## Clear and robust Python

- Follow the existing formatter and PEP 8 conventions; use descriptive names and straightforward control flow. Prefer small cohesive modules to speculative class hierarchies.
- Annotate public interfaces, complicated data structures, and nontrivial return values; choose `dataclass`, `TypedDict`, protocols, or ordinary objects based on actual data and behavior. Type hints do **not** validate runtime input.
- Validate untrusted inputs and configuration at system boundaries; distinguish malformed input, missing data, and programmer errors. Avoid broad `except Exception` blocks that silently suppress failures.
- Use context managers for files, DB sessions, locks, and other owned resources. Make timeouts, cancellation, retry limits, transaction boundaries, and cleanup explicit.
- Prefer parameterized SQL, safe file paths, explicit subprocess argument arrays, and secure secret handling. Avoid `eval`, unsafe unpickling of untrusted data, unsafe YAML loaders, shell string interpolation, and sensitive log output.
- Keep imports side-effect-light, avoid hidden global mutable state, and make dependencies injectable when it materially improves isolation or tests.
- For asynchronous IO, avoid blocking the event loop with sync operations. When concurrency is warranted, define task ownership, cancellation, bounded fan-out, and error propagation. Use `asyncio.TaskGroup` only when the supported Python version provides it.

## Optimize on measured bottlenecks

- Start with production metrics or a reproducible workload. Profile CPU (`cProfile`), memory, IO, query count, or algorithmic complexity before tuning.
- Prefer streaming/iterators for large data where materialization is costly; don't introduce clever generators or caches that impair readability without a measured benefit.
- Separate CPU-bound and IO-bound concurrency decisions; async is not a universal performance improvement.

## Verification gate

- Run the repository's formatter check, linter, configured type checker, and tests. For Ruff projects these may include `ruff check .` and `ruff format --check .`; use `python -m pytest` only when pytest is installed and configured.
- Exercise boundary values, invalid input, exception paths, resource cleanup, and async cancellation where applicable. Maintain determinism around time, network, and filesystem.
- For packages verify importability/build in supported environments; for services verify startup/config failures and API contracts.
- Report commands and actual outcomes, compatibility assumptions, and whether performance gains are measured or merely hypothetical.

## Primary references

- [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/)
- [Python asyncio tasks](https://docs.python.org/3/library/asyncio-task.html)
- [Python style guide (PEP 8)](https://peps.python.org/pep-0008/)
- [Ruff formatter (optional)](https://docs.astral.sh/ruff/formatter/)
