#!/usr/bin/env python3
"""Create a lesson source pack under /home/workdir/artifacts/lessons/<slug>/."""
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

ROOT = Path("/home/workdir/artifacts/lessons")

FILES = {
    "SOURCE.md": "# Source\n- slug: {slug}\n- captured: {now}\n- origin:\n- type:\n- rights:\n- pages_or_screens:\n- missing:\n",
    "OUTLINE.md": "# Outline\n\n| order | chunk | outcome | evidence |\n| --- | --- | --- | --- |\n| 1 |  |  |  |\n",
    "CONCEPTS.md": "# Concepts\n\n| id | name | prereq_ids | bloom | evidence | status | modality |\n| --- | --- | --- | --- | --- | --- | --- |\n| c1 |  |  | understand |  | unknown | text |\n",
    "GRAPH.md": "# Graph\n\nRun graph_tools.py after CONCEPTS.md has real rows.\n",
    "GLOSSARY.md": "# Glossary\n\n| term | source words | plain |\n| --- | --- | --- |\n|  |  |  |\n",
    "LEARNER.md": "# Learner\n- level: U\n- mode: mixed\n- stakes:\n- known:\n- unknown:\n",
    "PLAN.md": "# Plan\n- job:\n- units:\n- out_of_scope:\n",
    "PROGRESS.md": "# Progress\n",
    "WALKTHROUGH.md": "# Walkthrough\njob:\naudience:\naspect: 16:9\nduration_s: 60\nsource_slug: {slug}\nvo_wpm: 150\n\n## Beats\n",
    "SUMMARY.md": "# Summary\n",
}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("slug")
    args = p.parse_args()
    slug = args.slug.strip().lower().replace(" ", "-")
    dest = ROOT / slug
    dest.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now().isoformat(timespec="seconds")
    for name, tmpl in FILES.items():
        path = dest / name
        if not path.exists():
            path.write_text(tmpl.format(slug=slug, now=now), encoding="utf-8")
    (dest / "captures" / "screens").mkdir(parents=True, exist_ok=True)
    print(dest)


if __name__ == "__main__":
    main()
