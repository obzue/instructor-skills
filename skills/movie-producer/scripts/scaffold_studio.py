#!/usr/bin/env python3
"""Create a film studio tree under /home/workdir/artifacts/films/<slug>/."""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path("/home/workdir/artifacts/films")

FILES = {
    "BRIEF.md": "# Brief\n- job:\n- audience:\n- runtime_s:\n- aspect:\n- platform:\n- banned:\n- renderer:\n",
    "BIBLE.md": "# Bible\n- tone:\n- palette:\n- type:\n- camera_defaults:\n- refs:\n",
    "ASSETS.md": "# Assets\n\n| id | kind | path | rights | notes |\n| --- | --- | --- | --- | --- |\n",
    "SHOTS.md": "# Shots\n",
    "WALKTHROUGH.md": "# Walkthrough\n",
}

DIRS = ("PASSPORTS", "SELECTS", "GENERATIONS", "FINISH")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("slug")
    args = p.parse_args()
    slug = args.slug.strip().lower().replace(" ", "-")
    dest = ROOT / slug
    dest.mkdir(parents=True, exist_ok=True)
    for d in DIRS:
        (dest / d).mkdir(exist_ok=True)
    for name, tmpl in FILES.items():
        path = dest / name
        if not path.exists():
            path.write_text(tmpl, encoding="utf-8")
    print(dest)


if __name__ == "__main__":
    main()
