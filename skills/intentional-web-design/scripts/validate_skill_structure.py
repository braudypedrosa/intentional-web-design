#!/usr/bin/env python3
"""Validate Intentional Web Design's scalable internal structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
SKILL_FILE = SKILL_ROOT / "SKILL.md"
REFERENCES_DIR = SKILL_ROOT / "references"
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ARCHETYPE_PATTERN = re.compile(
    r"^- \*\*((?:HE|H|I|S|G|D|T|C|F)\d{2})\b", re.MULTILINE
)
IMPLEMENTED_PATTERN = re.compile(r"^- Implemented:\s*(.+)$", re.MULTILINE)
ID_PATTERN = re.compile(r"^(?:HE|H|I|S|G|D|T|C|F)\d{2}$")


def local_markdown_targets(path: Path) -> set[Path]:
    targets: set[Path] = set()
    for raw_target in LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
        target = raw_target.split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        targets.add((path.parent / target).resolve())
    return targets


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    required = [SKILL_FILE, SKILL_ROOT / "agents" / "openai.yaml", REFERENCES_DIR]
    for path in required:
        if not path.exists():
            errors.append(f"Missing required path: {path.relative_to(SKILL_ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    markdown_files = [SKILL_FILE, *sorted(REFERENCES_DIR.glob("*.md"))]
    for markdown_file in markdown_files:
        for target in local_markdown_targets(markdown_file):
            if not target.exists():
                errors.append(
                    f"Broken Markdown link in {markdown_file.relative_to(SKILL_ROOT)}: "
                    f"{target}"
                )

    skill_lines = len(SKILL_FILE.read_text(encoding="utf-8").splitlines())
    if skill_lines > 500:
        errors.append(f"SKILL.md has {skill_lines} lines; the maximum is 500")

    direct_targets = local_markdown_targets(SKILL_FILE)
    for reference in sorted(REFERENCES_DIR.glob("*.md")):
        if reference.resolve() not in direct_targets:
            errors.append(
                f"Reference is not linked directly from SKILL.md: "
                f"{reference.relative_to(SKILL_ROOT)}"
            )
        line_count = len(reference.read_text(encoding="utf-8").splitlines())
        if line_count > 250:
            warnings.append(
                f"Consider splitting {reference.relative_to(SKILL_ROOT)} "
                f"({line_count} lines)"
            )

    archetype_text = (REFERENCES_DIR / "layout-archetypes.md").read_text(
        encoding="utf-8"
    )
    archetype_ids = ARCHETYPE_PATTERN.findall(archetype_text)
    duplicates = sorted({item for item in archetype_ids if archetype_ids.count(item) > 1})
    if duplicates:
        errors.append(f"Duplicate layout archetype IDs: {', '.join(duplicates)}")
    known_archetypes = set(archetype_ids)

    history_files = sorted(REFERENCES_DIR.glob("layout-history-*.md"))
    registry_targets = local_markdown_targets(REFERENCES_DIR / "layout-usage-registry.md")
    for history_file in history_files:
        if history_file.resolve() not in registry_targets:
            errors.append(
                f"Layout history is not indexed in layout-usage-registry.md: "
                f"{history_file.name}"
            )
        history_text = history_file.read_text(encoding="utf-8")
        for implemented in IMPLEMENTED_PATTERN.findall(history_text):
            ids = [item.strip() for item in implemented.split(",")]
            invalid_format = [item for item in ids if not ID_PATTERN.fullmatch(item)]
            unknown = [item for item in ids if item not in known_archetypes]
            if invalid_format:
                errors.append(
                    f"Invalid archetype ID format in {history_file.name}: "
                    f"{', '.join(invalid_format)}"
                )
            if unknown:
                errors.append(
                    f"Unknown archetype IDs in {history_file.name}: "
                    f"{', '.join(unknown)}"
                )

    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        "Structure valid: "
        f"{len(markdown_files)} Markdown files, "
        f"{len(known_archetypes)} archetypes, "
        f"{len(history_files)} industry history file(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
