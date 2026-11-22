# Maintain the portable skill collection

- Follow CONTRIBUTING.md and start original skills from templates/SKILL.md.
- Publish only cross-project workflows; language/tool specialization is fine, but client-specific commands, business logic, machine paths, and private data are not.
- Generalize useful project-local procedures by discovering repo conventions and making integration prerequisites explicit. Otherwise leave them in the original project's skills folder.
- Preserve upstream licenses and record provenance/adaptations when importing.
- Keep INVENTORY.md consistent with skill folders actually published, not local plugin caches or user-machine inventories.
- Verify companion files and run `python scripts/validate-skills.py` before committing.
- For implementation work, apply `skills/rezsat/engineering-delivery/SKILL.md`: real acceptance paths, executable evidence, bounded diffs and truthful status, not decorative scaffolding or fabricated results.
- For a **new native desktop application's UI**, default to Anomaly Rune using `skills/rezsat/rune-desktop/SKILL.md`. Pin the upstream Git commit, inspect the versioned source/examples, and require visual, semantic, interaction and OS-level verification. An existing app is not automatically a migration project.
- For coding sessions in this repository under a supported Codex environment, use `skills/rezsat/capsule-workflow/SKILL.md`: check Capsule first, install from its official source if missing, preserve compression and safety hooks, and use the tested `CAPSULE_ADVISOR=0` advisor opt-out before launching a fresh Codex process.
