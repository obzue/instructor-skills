#!/usr/bin/env python3
"""Check a desk beat log. Original checker for this skill."""

import json
import sys

KINDS = {"open", "back", "forward", "file", "note", "film-start", "film-stop"}
SECRET_MARKERS = ("password=", "api_key", "bearer ", "sk-", "secret=")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_beats.py beats.json")
    with open(sys.argv[1], encoding="utf-8") as handle:
        data = json.load(handle)
    beats = data.get("beats")
    intent = data.get("intent")
    if not isinstance(intent, str) or not intent.strip():
        raise SystemExit("intent must be a sentence")
    if not isinstance(beats, list) or not beats:
        raise SystemExit("beats must be a non-empty list")
    last = -1.0
    for index, beat in enumerate(beats):
        if not isinstance(beat, dict):
            raise SystemExit(f"beat {index} is not an object")
        if beat.get("kind") not in KINDS:
            raise SystemExit(f"beat {index} has a bad kind")
        t = beat.get("t")
        if not isinstance(t, (int, float)) or t < last:
            raise SystemExit(f"beat {index} has a bad time")
        last = float(t)
        label = beat.get("label", "")
        if not isinstance(label, str) or not label.strip() or len(label) > 240:
            raise SystemExit(f"beat {index} has a bad label")
        blob = json.dumps(beat).lower()
        for marker in SECRET_MARKERS:
            if marker in blob:
                raise SystemExit(f"beat {index} looks like a secret")
    print(f"ok {len(beats)} beats")


if __name__ == "__main__":
    main()
