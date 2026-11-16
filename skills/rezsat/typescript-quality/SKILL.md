---
name: typescript-quality
description: "Write and review robust TypeScript with precise types, runtime boundary validation, safe async flows, clean modules, and maintainable APIs. Use in TypeScript libraries, apps, services, and TSX projects."
---

# TypeScript engineering quality

Use for any TypeScript project; combine with `react-quality`, `nextjs-quality`, or `nestjs-quality` when the corresponding framework is present. TypeScript's type system is **not** runtime input validation.

## Establish the repository contract

1. Inspect `package.json`, lockfile, `tsconfig*.json`, installed TypeScript version, lint/format config, tests, import aliases, module format, and public API conventions.
2. Use the existing package manager and scripts. Follow the current ESM/CJS and build setup; do not rewrite module resolution, reorganize folders, or add a validation library without a reason.
3. Prefer `strict` type checking for new projects. For existing projects, propose incremental enablement; don't flip a setting that makes hundreds of unrelated files fail in the middle of a focused change.

## Type and API design

- Model valid states explicitly with discriminated unions and narrow interfaces. Avoid primitive boolean combinations that admit impossible states.
- Prefer inference for local obvious values and explicit types at exported APIs, external boundaries, and nontrivial callbacks. Use `satisfies` where it checks object shape while preserving inference.
- Avoid `any`, non-null assertions (`!`), double casts, and broad `as` assertions. For genuinely unknown data, accept `unknown` and narrow it via runtime checks, a schema, or an explicit trust boundary.
- Validate untrusted HTTP bodies, files, environment values, DB/queue messages, and third-party responses at runtime before using them. Treat serialization and error paths as external boundaries too.
- Handle `null`, `undefined`, empty collections, rejected promises, aborts, and timeout behavior explicitly. Never leave detached async work unobserved.
- Keep dependencies pointed in one direction. Design small stable module entry points and hide implementation detail; avoid circular dependencies, barrels that expose internals, and unnecessary abstraction.
- Prefer immutable data transformations where they clarify ownership. Don't copy large datasets unnecessarily merely to satisfy a stylistic preference.
- Maintain compatibility of exported contracts. Avoid silently changing validation, optional fields, or JSON shape when refactoring.

## Security and performance

- Never treat a TypeScript cast as authorization or sanitization. Enforce access checks where trusted data is accessed; parameterize queries and escape output in the relevant rendering context.
- Avoid adding heavyweight dependencies for trivial operations. Measure startup, bundle size, allocation, and network/query cost before optimizing.
- Consider `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` for stronger new-project contracts; enable only after checking compatibility and budget.

## Verification gate

- Run the repository's formatter/linter, type-check script, tests, and production build where applicable. If scripts are absent, run the TypeScript compiler against the appropriate project config when feasible.
- Test valid/invalid boundary inputs, discriminated cases, async rejections, and the public behavior changed. A green type-check is not evidence that JSON or environment input is valid.
- Summarize contracts changed, validation performed, commands and results, and deferred or unavailable checks.

## Primary references

- [TypeScript TSConfig reference](https://www.typescriptlang.org/tsconfig/)
- [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
- [TypeScript module reference](https://www.typescriptlang.org/docs/handbook/modules/reference.html)
