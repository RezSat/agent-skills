# Contribute a skill

This is a portable engineering skill collection, **not a backup of every skill installed on a machine**.

## Eligibility

A published skill should work in at least two unrelated repositories without rewriting its instructions. Accept common **language**, **framework**, **platform**, or **tool** dependencies when they are named in the description and checked before use. Do not require a particular customer's domain, workspace, file layout, internal CLI, or credentials.

Before publishing a local skill:

1. **Discover rather than assume.** Replace fixed repository paths, package manager commands, test scripts, deployment targets, and naming conventions with steps that inspect the target project first. When something cannot be detected, instruct the agent to ask or stop.
2. **Keep conditional integrations conditional.** A TypeScript, Rust, Claude Code, or framework skill can remain specialized; explain what must be installed and how to verify it.
3. **Drop nonportable workflows.** If the workflow exists only to implement one product feature, migrate a single client's data, or operate a private service, keep it in that project's own `.agents/skills` directory.
4. **Remove personal and private data.** Check for workstation paths, account or customer identifiers, internal hosts, tokens, API keys, personal notes, and private project content. Examples must be synthetic.
5. **Preserve provenance.** When importing others' work, record the source, revision, author, license, and changes. Keep accompanying notices; do not publish source material without redistribution rights.
6. **Verify the complete folder.** Every relative link, script, reference, and template the skill uses must be present. Run its documented check in a suitable project, not only YAML validation.

## Layout and format

Place each skill in `skills/<publisher>/<skill-name>/`. Use `skills/rezsat` for original RezSat skills. Choose a globally unique lowercase, hyphenated name matching the skill's YAML `name`.

Describe the result and the situations that trigger the skill. Write actionable steps with observable completion criteria. Link to supporting resources by relative path and load them only when needed. State client, tool, and environment requirements explicitly.

Do not silently edit an imported third-party skill. Document adaptations in [INVENTORY.md](INVENTORY.md) or another provenance record.

## Validation

Install PyYAML with `python -m pip install PyYAML==6.0.3`. Run:

```sh
python scripts/validate-skills.py
```

Then review the Git diff for hardcoded project assumptions and sensitive data, and test a matching prompt in the intended agent client. The validator checks skill manifest structure, **not** whether a workflow is genuinely portable or secure.
