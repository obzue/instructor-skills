#!/usr/bin/env python3
"""Reject a trail row that is missing a field or graded only by the agent."""

import sys
from pathlib import Path

ALLOWED = {"pass", "fail", "blocked"}
SELF_GRADE = ("i think", "looks good", "i believe", "seems fine", "i'm confident", "i am confident")


def check(text: str) -> list[str]:
    errors: list[str] = []
    rows = [line.strip() for line in text.splitlines() if line.strip() and not line.startswith("#")]
    if not rows:
        return ["trail is empty"]
    for index, row in enumerate(rows, start=1):
        parts = [part.strip() for part in row.split("|")]
        if len(parts) != 4:
            errors.append(f"row {index} needs intent | limit | evidence | result")
            continue
        intent, limit, evidence, result = parts
        if not intent or not limit or not evidence:
            errors.append(f"row {index} has an empty field")
        if result not in ALLOWED:
            errors.append(f"row {index} result must be pass, fail, or blocked")
        if any(phrase in evidence.lower() for phrase in SELF_GRADE):
            errors.append(f"row {index} evidence is a self-grade")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_trail.py trail.txt", file=sys.stderr)
        return 2
    errors = check(Path(sys.argv[1]).read_text())
    if errors:
        print("\n".join(errors))
        return 1
    print("trail ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
