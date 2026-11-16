# Contribute a skill

Place each skill in skills/<publisher>/<skill-name>. Use skills/rezsat for original RezSat skills. Choose a globally unique lowercase name and match the directory name in YAML frontmatter.

Describe the result and the situations that trigger the skill. Write actionable steps with observable completion criteria. Link to supporting resources by relative path and load them only when a step needs them. State client and tool requirements explicitly.

For third-party imports record the source, revision, author, license, and any adaptations. Retain license notices and review companion files for publication rights and private data. Provide the upstream installation route when redistribution is unavailable.

Install PyYAML with python -m pip install PyYAML==6.0.3. Run python scripts/validate-skills.py and exercise a matching prompt in the intended client.
