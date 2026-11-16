"""Check the published skill manifests and the contribution template."""
from pathlib import Path
import re
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def validate_manifest(path, expected_name):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError("expected YAML frontmatter between --- delimiters")
    end = lines.index("---", 1)
    data = yaml.safe_load("\n".join(lines[1:end]))
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    name = data.get("name")
    if not isinstance(name, str) or len(name) > 64 or not NAME.fullmatch(name):
        raise ValueError("name must be 1–64 lowercase letters, digits, or single hyphens")
    if name != expected_name:
        raise ValueError(f"name must match {expected_name!r}")
    description = data.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError("description must be a nonempty string of at most 1024 characters")
    if not any(line.strip() for line in lines[end + 1:]):
        raise ValueError("skill instructions are required")


def main():
    skills = ROOT / "skills"
    expected = {p / "SKILL.md": p.name for p in skills.glob("*/*") if p.is_dir()}
    errors = []
    names = set()
    for path, name in sorted(expected.items()):
        if name in names:
            errors.append(f"{path.relative_to(ROOT)}: duplicate skill name {name}")
        names.add(name)
    for path in sorted(set(skills.rglob("SKILL.md")) - expected.keys()):
        errors.append(f"{path.relative_to(ROOT)}: unexpected manifest location")
    expected[ROOT / "templates/SKILL.md"] = "example-skill"
    for path, name in sorted(expected.items()):
        try:
            validate_manifest(path, name)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(names)} skills and the template.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
