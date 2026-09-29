---
name: full-song-generator
description: Generate complete songs with structured lyrics, style tags, vocal-ready blueprints, and export packs for YuE2, ACE-Step 1.5, Tencent SongGeneration LeVo, DiffRhythm, HeartMuLa, and Suno-class tools. Use when the user asks for a song, full track, lyrics plus music, lyrics2song, cover song, vocal stem, or AI music like Suno or YuE.
metadata:
  type: workflow
  version: "1.1"
  sources: YuE2 ACE-Step-1.5 SongGeneration-LeVo DiffRhythm HeartMuse SongComposer
settings:
  awareness: earned-awareness
  self_grade: forbidden
---

# Full Song Generator

## Global instrument layer (always first)

Every lyric and prompt file starts with this four-line header. It locks instrument palette, timing profile, and performance style before any verse text. Do not omit it. Do not let the renderer infer it.

```
[Style: Delta Blues, slide guitar, distorted harmonica, raw male vocals]
[Tempo: 74 BPM, 12-bar shuffle, heavy syncopation]
[Key: A Major]
[Atmosphere: Smoky, vinyl crackle, live performance]
```

Swap the values, keep the keys:

- Electronic / club — `[Style: Deep House, 4x4 kick, sidechained pads]` and `[Tempo: 124 BPM, steady pulse]`
- Orchestral / world — `[Style: Cinematic Celtic Folk, uilleann pipes, tin whistle]` and `[Tempo: 68 BPM, 3/4 waltz time]`
- Retro electronic — `[Style: Synthwave, 1980s analog synthesizers, driving retro bassline, clean female vocals]` and `[Tempo: 110 BPM, straight 4/4 time]`

Then tag every functional segment. Never leave chorus/verse boundaries implicit.

- `[Intro]` / `[Outro]` — beds only, no lead vocal
- `[Verse 1]` / `[Verse 2]` — lower energy, clear diction
- `[Pre-Chorus]` — tension
- `[Chorus]` — more layers, harmony, intensity
- `[Bridge]` — contrast before the last chorus
- `[Instrumental Break]` / `[Guitar Solo]` / `[Drop]` — vocals out of the buffer
- Inline `(Spoken)` / `(Whispered)` on the affected line

Full schema, templates, and genre dicts: `references/production-tag-layer.md`.
Export field contracts: `references/lyric-and-tag-contracts.md`.
Auto-tag raw lyric files with `scripts/parse_lyrics.py`.

## Overview

Produce a complete song package, not just a verse. Every request yields structured lyrics, production tags, a section map, and model-ready prompt files. This sandbox cannot run 12–24 GB music foundation models. Write production-grade source files the user can render locally or on a hosted API, plus a spoken vocal scratch via the Voice connector when asked.

Read references/model-catalog.md for model choice.

## Collect before writing

Ask only for missing items. Infer reasonable defaults.

- Title and theme
- Language
- Genre, subgenre, era — maps to `[Style]`
- Mood and narrative POV — maps to `[Atmosphere]`
- Vocal identity (gender, age band, grit vs clean)
- BPM, meter, groove — maps to `[Tempo]`
- Key / mode — maps to `[Key]`
- Target length (short 1.5–2.5 min, radio 3–3.5 min, long 4–6 min)
- Explicitness
- Target renderer (YuE2, ACE-Step, LeVo, DiffRhythm, HeartMuLa, Suno, unknown)

## Output package (always)

Write under /home/workdir/artifacts/songs/<slug>/

1. BRIEF.md — creative brief plus the four global header fields
2. LYRICS.txt — global header then section-tagged lyrics (universal)
3. TAGS.txt — comma tags for ACE-Step / HeartMuLa / Suno
4. YUE_STYLE.txt — one-line YuE2 style sentence (must agree with `[Style]`)
5. LEVO.json — LeVo / SongGeneration payload
6. STRUCTURE.md — form, BPM, key, time signature, arrangement notes
7. SUNO_PROMPT.txt — header + lyrics block
8. When the user hands raw untagged lyrics, run `python scripts/parse_lyrics.py raw.txt -o LYRICS.txt -g <preset>` and then hand-edit section tags so the chorus is correct. Presets: delta-blues, deep-house, cinematic-celtic, synthwave, heavy-metal.

If the user wants audio in-session, generate a spoken scratch with voice_generate_speech (list voices first). Label it as lyric recitation, not a finished mix.

## Lyric craft (non-negotiable)

- Write the four-line global header before any section.
- Use section tags on their own lines. [Intro], [Verse 1], [Pre-Chorus], [Chorus], [Verse 2], [Bridge], [Final Chorus], [Outro]. Add [Instrumental] / [Instrumental Break] / [Guitar Solo] / [Drop] only when no lead vocal.
- Apply (Spoken) or (Whispered) on the line, not as a section tag.
- Chorus is the hook. Repeatable, shorter lines, higher vowel openness, title landing on a stressed beat.
- Verses advance story or image. Do not restate the chorus.
- Pre-chorus raises harmonic or rhythmic tension. Bridge contrasts key, POV, or density.
- Singability. Prefer 6–11 syllables per line for pop/rock; rap can stack internal rhyme.
- Avoid stacked near-identical chorus copies unless the brief is radio-pop. Vary last chorus with an extra couplet or stacked harmony note.
- Match language of the requested market. Do not mix languages unless asked.

## Style / tag craft

Write tags as a flat comma list, most important first.

Order: genre, subgenre, era, mood, vocal type, lead instruments, drums feel, tempo word, production era, mix adjectives.

Example:

pop soul, 1990s r&b, late-night, female alto, warm lead vocal, rhodes, muted guitar, tight dry drums, 86 bpm, analog mix, wide backing vocals

YuE2 style is one natural-language sentence, not a tag salad.

English, 90s pop-soul, warm female alto, Rhodes and muted guitar, dry tight drums, late-night radio mix

Never invent BPM that fights the lyric density. Ballad 68–84, mid 92–112, dance 118–128, DnB 160–174, trap 130–150 with half-time feel.

## Model routing

- Best open lyrics-to-full-song with editable score — YuE2 (m-a-p/YuE2-3B, repo multimodal-art-projection/YuE). Needs about 24 GB VRAM. Modes cot=full (new song), cot=melody (cover), cot=off (direct).
- Best local consumer GPU / Mac / AMD — ACE-Step 1.5 (ace-step/ACE-Step-1.5). Tags plus lyrics. 10 s to 10 min. MIT.
- Best Tencent research stack — SongGeneration / LeVo (tencent-ailab/songgeneration). Lyrics plus description, full songs to about 4m30s.
- Fast latent diffusion lyrics2song — DiffRhythm.
- Local HeartMuLa plus LLM lyrics UI — HeartMuse (strnad/HeartMuse).
- Symbolic lyric plus melody LLM — SongComposer.

If the user has no GPU, ship the prompt pack and point them at ACE-Step UI or a hosted Space. Do not pretend a foundation-model mix was rendered here.

## Cover and edit workflow (YuE2)

1. Transcribe source melody to ABC (SheetSage2 in the YuE repo).
2. Write new lyrics that fit the phrase lengths of that ABC.
3. Style sentence describes the NEW arrangement, not the original recording.
4. Generate with cot=melody.

## Quality gate before delivery

- LYRICS.txt opens with [Style], [Tempo], [Key], [Atmosphere]
- Chorus title appears in the chorus, not only the filename
- Every section has an explicit tag. Chorus is never inferred by position alone
- Section order is a real song form
- No trademarked artist-name cloning as a vocal identity
- Tags, [Style] sentence, and lyrics language agree
- Duration estimate matches section count (verse plus chorus cycles)

## Do not

- Claim the WAV/FLAC was synthesized by YuE or ACE-Step unless the user ran those weights
- Dump raw model cards into chat
- Write placeholder chorus lines like "yeah yeah oh"
- Copy copyrighted lyrics
