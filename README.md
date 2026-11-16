# Agent Skills

Install reusable agent workflows using the [Agent Skills specification](https://agentskills.io/specification).

Browse [Matt Pocock's skills](skills/matt-pocock) for planning, architecture, implementation, testing, and writing. Each SKILL.md describes when to use the skill and lists any client or project dependencies.

With Node.js and npm, run:

    npx skills add RezSat/agent-skills --skill tdd

For manual installation, copy the whole skill directory into a discovery root your client supports, such as .agents/skills in a Codex project. Refresh the client and invoke the skill by name or describe a matching task.

The imports preserve installed files and match [Matt Pocock's upstream revision](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa) after line ending normalization, with one syntax fix. The software-factory description is quoted so its colon parses as YAML. Some workflows require Claude-specific tools or conventions. The [upstream MIT notice](skills/matt-pocock/LICENSE) covers the imports. Install the grill-me alias directly with npx skills add mattpocock/skills --skill grill-me.

Install excluded Playwright CLI copies from the [Microsoft project](https://github.com/microsoft/playwright-cli). For project-specific Oxitab skills, use the discovery directory in the original Oxitab workspace. For bundled skills, install the corresponding plugin through its original catalog. See the [inventory](INVENTORY.md) for migration decisions and [contribution standards](CONTRIBUTING.md) for adding skills. Repository-authored files use the [MIT license](LICENSE).
