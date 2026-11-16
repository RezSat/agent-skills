---
name: engineering-style
description: "Apply the owner's straightforward coding and writing style to source code, comments, README files, technical docs, pull requests, and Git commits across any programming language."
---

# Engineering style

Use these preferences whenever you write or revise code, comments, documentation, pull requests, or commit messages. Keep changes focused and follow the project's technical requirements.

## Code and comments

- Prefer simple, readable implementation over elaborate abstractions, layers, wrappers, or dependencies with no clear purpose.
- Keep functions and modules cohesive. Use ordinary naming and formatting that fit the language and repository.
- Write comments for **why** something exists: non-obvious behavior, invariants, constraints, hardware quirks, tricky concurrency, or deliberate trade-offs.
- Let clear code explain **what** it does. Avoid comments narrating the next line, padded/aligned comment columns, separator banners, decorative section headings, and boilerplate docstrings.
- Keep required license notices, useful public API documentation, and safety-critical warnings. Don't erase necessary context just to reduce comment count.

## Git commits

- Use a short, natural, sentence-case imperative subject that says what actually changed.
- Prefer `Set up the workspace`, `Fix invoice totals`, or `Handle expired sessions`.
- Avoid mechanically generated prefixes like `feat:`, `chore:`, `refactor:`, or `(feat):`, and vague announcements such as `initialize monorepo foundation`, `improve architecture`, or `implement functionality`.
- Group related edits into sensible commits. Don't manufacture progress commits, authorship, timestamps, or fake history.
- If the target repository **requires** Conventional Commits through an explicit enforced policy, flag the conflict rather than silently ignoring it.

## Documentation and pull requests

- Start with what the project or change does. Use precise technical words, short sentences, and concrete setup, usage, behavior, and verification details.
- State what exists today accurately. Mark unfinished or planned work as such.
- Skip slogans, self-congratulatory claims, rhetorical "This is not ..." explanations, generic boilerplate, repetitive summaries, and excessive headings.
- Write a PR description that helps someone review the actual diff. Don't invent tests or claim performance and security improvements without evidence.

Before finishing, reread the diff as a developer would: remove filler, keep necessary explanations, and check that commit and documentation wording matches the real change.
