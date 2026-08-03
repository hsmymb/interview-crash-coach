#!/usr/bin/env python3
"""Validate repository-specific invariants for interview-crash-coach."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/analysis-and-planning.md",
    "references/teaching-and-answering.md",
    "references/mock-interview.md",
    "references/output-templates.md",
)

REQUIRED_SKILL_PHRASES = (
    "self-contained pack",
    "complete reference answers",
    "no mandatory external reading",
    "Never invent experience",
    "teaching-and-answering.md",
)

MOJIBAKE_MARKERS = ("\ufffd", "鈥", "銆", "锛", "鈫", "脳")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "skill_dir",
        nargs="?",
        default=Path(__file__).resolve().parents[1],
        type=Path,
    )
    return parser.parse_args()


def main() -> int:
    root = parse_args().skill_dir.resolve()
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        skill_text = skill_path.read_text(encoding="utf-8")
        line_count = len(skill_text.splitlines())
        if line_count > 500:
            errors.append(f"SKILL.md has {line_count} lines; expected at most 500")
        for phrase in REQUIRED_SKILL_PHRASES:
            if phrase not in skill_text:
                errors.append(f"SKILL.md missing required phrase: {phrase!r}")

    text_suffixes = {".md", ".yaml", ".yml", ".json", ".py"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"not valid UTF-8: {path.relative_to(root)} ({exc})")
            continue
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                errors.append(
                    f"possible encoding corruption {marker!r}: {path.relative_to(root)}"
                )

    if errors:
        print("Skill content validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill content validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
