# Lyric and tag contracts

Canonical header, section, and micro-timing rules live in `production-tag-layer.md`. This file is the per-export contract.

## Universal lyric file (`LYRICS.txt`)

Header first. Then tagged sections. Blank line after every tag. No chords unless the user asked for a lead sheet.

```
[Style: genre, instruments, vocal identity]
[Tempo: BPM, meter, groove]
[Key: key and mode]
[Atmosphere: room, texture, performance]

[Intro]
[Instrumental: Main theme build-up]

[Verse 1]
line
line

[Pre-Chorus]
line
line

[Chorus]
hook line
hook line
title line
hook line

[Verse 2]
...

[Bridge]
...

[Final Chorus]
...

[Outro]
[Fade out: Instrumentation decays into delay loops]
```

Inline modifiers allowed on lyric lines: `(Spoken)`, `(Whispered)`. Block modifiers: `[Instrumental Break]`, `[Guitar Solo]`, `[Drop]`, `[Vocal Harmony: ...]`.

## ACE-Step / HeartMuLa / Suno tags (`TAGS.txt`)

Comma-separated, no trailing period.

Fields to cover when known:

- genre, subgenre
- decade / scene
- mood
- vocalist
- instrumentation
- drum feel
- tempo word or BPM
- mix / space adjectives

Do not put full lyrics in the tag field.

## YuE2 style (`YUE_STYLE.txt`)

One sentence. Include language, genre, vocal character, core instruments, mix vibe.

## LeVo JSON (`LEVO.json`)

```json
{
  "description": "English pop-soul, 86 BPM, female alto, Rhodes, muted guitar, dry drums",
  "lyrics": "[Verse 1]\n...\n[Chorus]\n...",
  "gender": "female",
  "genre": "pop soul"
}
```

## Duration vs form

- ~90–120 s: intro + V + C + V + C + outro
- ~180–210 s: add pre-chorus and a mid-8 / bridge
- ~240–270 s: double last chorus, short instrumental break
- >4 min: only if the renderer supports it (ACE-Step up to 10 min, LeVo ~4.5 min, YuE2 several minutes)
---
