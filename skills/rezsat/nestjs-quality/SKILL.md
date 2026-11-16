---
name: nestjs-quality
description: "Implement or review NestJS HTTP APIs, modules, services, providers, guards, validation, persistence, and tests with clear boundaries and production-safe defaults."
---

# NestJS engineering quality

Use for NestJS services and APIs. Apply `typescript-quality` for type design; this skill supplies Nest-specific architecture, request lifecycle, and runtime checks.

## Discover the application

1. Inspect installed Nest and Node versions, HTTP adapter (Express or Fastify), module graph, configured global pipes/guards/filters, DI providers, ORM, transport, and existing test conventions.
2. Confirm the changed endpoint or message's request schema, response shape, authentication, authorization, side effects, and backwards-compatibility requirements.
3. Follow established feature/module boundaries. Don't create extra modules, generic base services, or repositories for a single endpoint without a real boundary.

## Correct Nest patterns

- Controllers handle routing, request mapping, and response contracts. Providers/services own application behavior; persistence and external transport belong behind explicit, testable adapters.
- Register dependencies through Nest DI and modules; avoid manually constructing providers that Nest manages. Keep provider scope singleton by default; use request/transient scopes only where lifecycle requirements justify overhead.
- Use DTOs with a configured `ValidationPipe` (or an equivalent validated transport schema). Confirm the runtime transformation semantics and intentionally choose `whitelist` / `forbidNonWhitelisted` as appropriate. TypeScript DTO annotations alone do not validate incoming bytes.
- Put authentication in the appropriate strategy/guard; make authorization checks on **each resource/action**, not only a login token. Never rely solely on frontend access rules.
- Use guards for admission, pipes for parsing/validation, interceptors for cross-cutting behavior, and filters for error presentation. Do not hide business failures in an unconditional 200 response or swallow exceptions.
- Centralize validated configuration and fail fast on missing critical environment values. Never log secrets, session tokens, passwords, or full sensitive request bodies.
- Keep DB interactions deterministic: parameterized queries, explicit transaction boundaries for multi-write invariants, sensible pagination, unique constraints, and deliberate retries/idempotency for external effects.
- Make background jobs and event handlers observable and recoverable; define timeouts, retry ceilings, duplicate-event policy, and shutdown cleanup.

## Performance without folklore

- Inspect query count/N+1, serialization cost, external request time, pool saturation, and per-request work before changing the HTTP adapter or caching strategy.
- Avoid request-scoped dependency trees and synchronous CPU-heavy work on the event loop unless explicitly necessary. Compare representative latency and memory baselines before claiming gains.

## Verification gate

- Run repository scripts for lint, typecheck, tests, and build using the detected package manager.
- Exercise services with Nest's testing utilities, and changed public endpoints with integration/e2e tests (validation rejection, unauthorized/forbidden, normal success, persistence/error behavior).
- If security, configuration, or error mapping changed, verify the real HTTP status and response body rather than only mocking service calls.
- Report the test commands/results, adapter and module assumptions, contract differences, and any unverified deployment-specific behavior.

## Primary references

- [Nest validation](https://docs.nestjs.com/techniques/validation)
- [Nest testing](https://docs.nestjs.com/fundamentals/testing)
- [Nest authentication](https://docs.nestjs.com/security/authentication)
- [Nest providers](https://docs.nestjs.com/providers)
