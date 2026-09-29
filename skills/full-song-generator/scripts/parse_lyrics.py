#!/usr/bin/env python3
"""Parse raw lyrics into a tagged AI-music prompt.

Injects the global instrument / timing / atmosphere header, section tags,
and micro-timing modifiers. Self-contained — stdlib only.
"""

from __future__ import annotations

import argparse
import os
import sys


DEFAULT_GENRE = {
    "style": "Pop, clean vocals",
    "tempo": "120 BPM, 4/4 time",
    "key": "C Major",
    "atmosphere": "Studio recording",
}

GENRE_PRESETS = {
    "delta-blues": {
        "style": "Delta Blues, slide guitar, distorted harmonica, raw male vocals",
        "tempo": "74 BPM, 12-bar shuffle, heavy syncopation",
        "key": "A Major",
        "atmosphere": "Smoky, vinyl crackle, live performance",
    },
    "deep-house": {
        "style": "Deep House, 4x4 kick, sidechained pads",
        "tempo": "124 BPM, steady pulse",
        "key": "A Minor",
        "atmosphere": "Warehouse night, dark club, analog warmth",
    },
    "cinematic-celtic": {
        "style": "Cinematic Celtic Folk, uilleann pipes, tin whistle",
        "tempo": "68 BPM, 3/4 waltz time",
        "key": "D Major",
        "atmosphere": "Mist, hall reverb, live session",
    },
    "synthwave": {
        "style": "Synthwave, 1980s analog synthesizers, driving retro bassline, clean female vocals",
        "tempo": "112 BPM, straight 4/4 time",
        "key": "E Minor",
        "atmosphere": "Neon glare, dense reverb snare, cyberpunk cinematic",
    },
    "heavy-metal": {
        "style": "Heavy Metal, dual distorted guitars, aggressive male vocals",
        "tempo": "140 BPM, driving 4/4, double-kick passages",
        "key": "E Minor",
        "atmosphere": "Arena stage, high-gain, live crowd room",
    },
}

SECTION_OVERRIDE_TOKENS = ("[VERSE", "[CHORUS", "[BRIDGE", "[INTRO", "[OUTRO", "[PRE-CHORUS")


def generate_tagged_song(raw_lyrics_path: str, output_path: str, genre_config: dict) -> str:
    """Parse a raw lyrics file and write a tagged production prompt."""
    if not os.path.exists(raw_lyrics_path):
        raise FileNotFoundError(f"The file {raw_lyrics_path} does not exist.")

    header = (
        f"[Style: {genre_config.get('style', DEFAULT_GENRE['style'])}]\n"
        f"[Tempo: {genre_config.get('tempo', DEFAULT_GENRE['tempo'])}]\n"
        f"[Key: {genre_config.get('key', DEFAULT_GENRE['key'])}]\n"
        f"[Atmosphere: {genre_config.get('atmosphere', DEFAULT_GENRE['atmosphere'])}]\n\n"
    )

    with open(raw_lyrics_path, "r", encoding="utf-8") as f:
        raw_blocks = [block.strip() for block in f.read().split("\n\n") if block.strip()]

    structured_body = []
    verse_count = 1
    total_blocks = len(raw_blocks)

    structured_body.append("[Intro]\n[Instrumental: Main theme build-up]\n")

    for index, block in enumerate(raw_blocks):
        lines = block.split("\n")
        processed_lines = []

        for line in lines:
            line_str = line.strip()
            if not line_str:
                continue
            quoted = line_str.startswith('"') and line_str.endswith('"')
            short_opener = len(line_str) < 25 and index == 0 and not line_str.startswith("[")
            if quoted or short_opener:
                line_str = f"(Spoken) {line_str.strip(chr(34))}"
            processed_lines.append(line_str)

        block_content = "\n".join(processed_lines)
        upper = block.upper()

        if any(tag in upper for tag in SECTION_OVERRIDE_TOKENS):
            structured_body.append(block)
        elif index == 0:
            structured_body.append(f"[Verse {verse_count}]\n{block_content}")
            verse_count += 1
        elif index == total_blocks - 1:
            structured_body.append(
                f"[Chorus]\n{block_content}\n\n[Vocal Harmony: High octave duplicate]"
            )
        elif total_blocks > 3 and index == total_blocks - 2:
            structured_body.append(f"[Bridge]\n[Instrumental Break]\n{block_content}")
        elif index % 2 == 1:
            structured_body.append(f"[Chorus]\n{block_content}")
        else:
            structured_body.append(f"[Verse {verse_count}]\n{block_content}")
            verse_count += 1

    structured_body.append("[Outro]\n[Fade out: Instrumentation decays into delay loops]")

    full_song = header + "\n\n".join(structured_body)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_song)

    return full_song


def _demo_lyrics() -> str:
    return (
        "Walking down this empty neon street\n"
        "Hearing nothing but my own heart beat\n\n"
        "We are running through the night\n"
        "Chasing every fading light\n\n"
        "The circuits burn, the gears shift low\n"
        "We've got nowhere left to go\n\n"
        "We are running through the night\n"
        "Holding on with all our might"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Tag raw lyrics for AI music models.")
    parser.add_argument("raw_lyrics", nargs="?", default="raw_lyrics.txt")
    parser.add_argument("-o", "--output", default="ai_ready_prompt.txt")
    parser.add_argument(
        "-g",
        "--genre",
        default="synthwave",
        choices=sorted(GENRE_PRESETS.keys()),
        help="Named genre preset",
    )
    parser.add_argument("--demo", action="store_true", help="Write sample raw_lyrics.txt first")
    args = parser.parse_args(argv)

    if args.demo and not os.path.exists(args.raw_lyrics):
        with open(args.raw_lyrics, "w", encoding="utf-8") as f:
            f.write(_demo_lyrics())

    if not os.path.exists(args.raw_lyrics):
        print(f"Error: The file {args.raw_lyrics} does not exist.", file=sys.stderr)
        return 1

    generate_tagged_song(args.raw_lyrics, args.output, GENRE_PRESETS[args.genre])
    print(f"Success! Structured framework saved to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
