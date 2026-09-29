#!/usr/bin/env python3
"""Create craft specs under /home/workdir/artifacts/songs/<slug>/."""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path("/home/workdir/artifacts/songs")

FILES = {
    "LYR-SPEC.md": "# LYR-SPEC\ntitle:\npromise:\nlanguage:\ntitle_line:\nimages:\nrhyme:\nsyllables:\nchorus_stress:\nexplicit:\nnotes:\n",
    "ARR-SPEC.md": "# ARR-SPEC\nform:\nbars:\nkey:\ntempo:\nmeter:\ngroove:\nchords:\nentries:\nenergy:\nvocal:\nmix:\npicture_spots:\n",
}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("slug")
    args = p.parse_args()
    slug = args.slug.strip().lower().replace(" ", "-")
    dest = ROOT / slug
    dest.mkdir(parents=True, exist_ok=True)
    for name, tmpl in FILES.items():
        path = dest / name
        if not path.exists():
            path.write_text(tmpl, encoding="utf-8")
    print(dest)


if __name__ == "__main__":
    main()
