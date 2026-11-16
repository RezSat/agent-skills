---
name: nextjs-quality
description: "Build or review Next.js applications with correct App/Pages Router conventions, safe server/client boundaries, explicit caching, secure mutations, accessibility, and measured web performance."
---

# Next.js engineering quality

Use for Next.js routing, rendering, data fetching, mutations, caching, metadata, and deployment issues. Pair with `react-quality` and `typescript-quality` when relevant.

## Discover the actual version and router

1. Read `package.json`, `next.config.*`, the Next.js major version, the `app/` and/or `pages/` directories, middleware/proxy conventions, auth library, tests, and deployment adapter.
2. Identify whether touched routes use **App Router** or **Pages Router**; never mix their APIs or import a newer-version pattern into older code without verifying compatibility.
3. For each route determine public vs personalized output, SEO needs, loading behavior, and intended fresh/stale/cached semantics.

## App Router design (only where used)

- Keep components on the server by default. Add `"use client"` only to subtrees that require browser APIs, hooks, or event handlers; move interactive leaves behind narrow client boundaries.
- Fetch server-owned data in Server Components/server utilities when possible rather than calling your own Route Handler over HTTP from the server. Protect credentials and server-only modules from the client bundle.
- Use route-level `loading`, `error`, `not-found`, and Suspense patterns deliberately. Prevent avoidable sequential request waterfalls by parallelizing independent I/O.
- Validate and authorize **every mutation on the server**, including Server Actions and Route Handlers. Validate untrusted input, verify ownership/resource permissions, and return safe failure states. A UI-hidden action is not an authorization boundary.
- Treat cache behavior as **version- and API-dependent**. Inspect the installed Next.js documentation and project flags before relying on defaults. Explicitly design cache lifetime, tags/revalidation, personalized-data isolation, and invalidation after writes.
- Handle route params and search params using the signatures supported by the installed version; do not mechanically copy examples from a different release.

## All routers

- Use the framework's navigation, image, font, and metadata facilities where supported; measure rather than assume automatic optimization fixes every issue.
- Avoid accidentally importing server secrets into client code; do not put sensitive values in `NEXT_PUBLIC_*` variables.
- Guard against XSS from untrusted rich content, SSRF in server-side outbound requests, unbounded payloads, and cache mixing across users.
- Favor progressive rendering, semantic accessible markup, and efficient hydration. Inspect client JS size and Core Web Vitals before adding dependencies, memoization, or caching layers.

## Verification gate

- Run project lint/typecheck/tests plus the production Next.js build; test affected routes in the intended rendering mode.
- Verify logged-out/unauthorized behavior, bad inputs, personalized cache isolation, navigation, not-found/error responses, and post-mutation freshness where relevant.
- For performance changes measure bundle size and Web Vitals (or representative route timings) before and after, with identical conditions.
- Report router/version assumptions, cache policy, commands and results, and any deployment behaviors that still need real-environment validation.

## Primary references

- [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Next.js data fetching](https://nextjs.org/docs/app/getting-started/fetching-data)
- [Next.js App Router production checklist](https://nextjs.org/docs/app/guides/production-checklist)
- [Next.js Pages Router production checklist](https://nextjs.org/docs/pages/guides/production-checklist)
