---
name: react-quality
description: "Develop or review accessible, predictable, testable React components and hooks with appropriate state, effects, composition, and evidence-based rendering performance."
---

# React engineering quality

Use for React components, hooks, state logic, and UI reviews. Pair with `typescript-quality` for TSX and `nextjs-quality` for Next.js-specific server/client boundaries.

## Inspect first

1. Check React version, compiler configuration, framework, routing, state libraries, design system, accessibility requirements, lint rules, and existing component tests.
2. Identify which state is local, shared, server-derived, or URL-derived. Honor current conventions instead of introducing a global state library or UI kit by default.
3. Understand the interaction, loading, error, empty, and keyboard states before changing the render tree.

## Components and hooks

- Keep rendering pure and deterministic. Never mutate props/state, trigger network calls in render, or use effects to compensate for impure rendering.
- Store **minimal** state. Compute derived values during render when cheap; don't mirror props in state or use `useEffect` to synchronize values that could be calculated directly.
- Use effects for synchronization with external systems and clean them up. Keep dependencies accurate; prevent stale closures and request races with cancellation or stale-result protection.
- Prefer composition, small cohesive components, explicit props, and stable identity. Use semantic list keys from data, not array positions when items can reorder.
- Keep transient interaction state near where it is used. Use context or an external store only when sharing requirements warrant it; avoid passing unstable objects through large trees without need.
- Handle pending, error, empty, and success states deliberately. Use error boundaries and Suspense where supported by the actual framework; don't invent Suspense behavior for arbitrary promises.
- Use semantic HTML, labels, focus management, keyboard interaction, and sensible screen reader announcements. Do not replace buttons/links with clickable divs. Check contrast and reduced-motion expectations.

## Performance decisions

- Fix network waterfalls, needless global state updates, oversized lists, and heavyweight client dependencies before blanket memoization.
- Follow React's Rules of React and the installed compiler configuration. Do not mechanically sprinkle `useMemo`, `useCallback`, or `memo`; profile a real slow interaction first and use them where evidence warrants.
- Virtualize genuinely large lists when useful; split heavy code at route or interaction boundaries only after considering UX and loading overhead.

## Verification gate

- Run the repo's lint/typecheck/tests/build. Exercise components with user-visible behavior and accessible queries, not implementation details.
- Test relevant mouse, keyboard, focus, async, error, and empty states. Where available, run accessibility checks and manually inspect critical interactions.
- For performance work, capture profiler, bundle, or Web Vitals measurements before/after and state the environment. Never claim faster renders without data.
- Report meaningful test results, remaining accessibility risks, and any intentionally retained trade-offs.

## Primary references

- [Rules of React](https://react.dev/reference/rules)
- [React memoization guidance](https://react.dev/reference/react/useMemo)
- [React Compiler introduction](https://react.dev/learn/react-compiler/introduction)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
