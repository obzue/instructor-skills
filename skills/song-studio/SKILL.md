---
name: song-studio
description: Combine songwriting craft and music production into one package covering lyrics, form, harmony, arrangement, mix intent, and renderer prompts. Use when the user wants to write a song, produce a track, arrange, score a tutorial film, build lesson music, or merge songwriting with production.
metadata:
  type: workflow
  version: "1.0"
  sources: full-song-generator SJY051/music-composition jtydhr88/music-composition-skills jtydhr88/lyric-writing-skills regiellis/suno-songwriter-agent-skill NousResearch/hermes-agent-songwriting-and-ai-music
---

# Song Studio

One studio for words and sound. Distilled from composition-spec skills (ARR-SPEC), lyric-spec skills (LYR-SPEC), Suno-class prompt craft, and the existing `full-song-generator` export pack.

`full-song-generator` owns renderer contracts (YuE2, ACE-Step, LeVo, DiffRhythm, HeartMuLa, Suno files). This skill owns the craft decisions those files must agree on. When both apply, write the craft here, then emit the export pack through `full-song-generator`.

Read `references/craft.md` before writing a chorus.
Read `references/arr-spec.md` before locking form.

## Collect before writing

Ask only for missing slots.

- Title and theme
- Job — standalone song, score for a tutorial/film, bed only, parody/adaptation
- Language
- Genre / era — becomes `[Style]`
- Mood and POV — becomes `[Atmosphere]`
- Vocal identity
- BPM, meter — becomes `[Tempo]`
- Key / mode — becomes `[Key]`
- Target length
- Explicitness
- Target renderer (or unknown)
- Picture lock — if this scores a video, inherit runtime and section map from movie-producer

If the user already has `full-song-generator` files, edit those. Do not start a second song folder.

## Global header (always first)

Every lyric and prompt file starts with

```
[Style: ...]
[Tempo: ...]
[Key: ...]
[Atmosphere: ...]
```

Do not omit it. Do not let a renderer infer it. Swap values, keep keys. See `full-song-generator` for genre examples.

Tag every functional segment on its own line. `[Intro]` `[Verse 1]` `[Pre-Chorus]` `[Chorus]` `[Verse 2]` `[Bridge]` `[Instrumental Break]` `[Drop]` `[Final Chorus]` `[Outro]`. Mark `(Spoken)` / `(Whispered)` on the line.

## Two specs, one agreement

Write both under `/home/workdir/artifacts/songs/<slug>/` (or `/home/workdir/artifacts/lessons/<slug>/music/` for lesson scores).

### LYR-SPEC (`LYR-SPEC.md`)

- Promise — what the song is about in one sentence
- Title landing — which line of the chorus carries the title
- Image set — 4–8 concrete images, no abstractions stacking
- Rhyme scheme per section
- Syllable budget per line (pop/rock 6–11 as default)
- Stress map for the chorus (which words hit downbeats)
- Language layer — keep one language unless asked

### ARR-SPEC (`ARR-SPEC.md`)

- Form with bar counts
- Key, tempo, meter, groove
- Chord chart (symbols plus Roman numerals)
- Who enters / leaves per section
- Energy curve (1–10 per section)
- Vocal delivery notes
- Mix intent — dry/wet, width, lead seat, banned mud
- Picture spots if scoring a film (in-point, out-point, why music exists)

These six fields must agree across both specs: form labels, bar math, title line, language, tempo, key.

Then emit or refresh the `full-song-generator` pack (`BRIEF.md`, `LYRICS.txt`, `TAGS.txt`, `YUE_STYLE.txt`, `LEVO.json`, `STRUCTURE.md`, `SUNO_PROMPT.txt`).

## Songwriting craft

- Chorus is the hook. Shorter lines, open vowels, title on a stressed beat.
- Verses advance image or story. They do not restate the chorus.
- Pre-chorus raises tension. Bridge contrasts key, POV, or density.
- Show with objects and actions. "The kettle clicks off" beats "I feel empty."
- Options, not sermons — when the user says the chorus is weak, split the problem (range, harmonic surprise, lyric density, arrangement lift) and offer 2–4 concrete fixes with chord symbols or rewritten lines.
- Do not moralize theory. Parallel fifths are a sound, not a sin.
- No trademarked-artist vocal cloning as an identity.
- No copyrighted lyrics.

Adaptation / parody — map the source's phrase lengths first, then write new words that fit. Do not paste the original lyric into the deliverable.

## Production craft

Translate vague notes into knobs.

| Complaint | Split into |
| thin chorus | double the vocal, add a lift chord, open the filter, raise the ceiling syllable |
| verse drags | cut two lines, move the snare, start the vocal earlier |
| mix is muddy | high-pass beds at 120–180 Hz, carve 300–500 Hz, seat the vocal at 2–5 kHz |
| drop does not drop | subtract before the bar, not add after |

Arrangement default for a 3-minute pop form

- Intro — motif only
- Verse 1 — vocal plus one bed
- Pre — percussion or harmony enter
- Chorus 1 — full kit, double or stack
- Verse 2 — keep one chorus element so energy does not collapse
- Bridge — subtract or modulate
- Final chorus — one new line or one new layer
- Outro — strip back to the motif

For tutorial beds, write instrumental-only ARR-SPEC. No lead vocal in the buffer. Duck under VO. Target integrated loudness that leaves headroom for speech (bed about −18 to −21 LUFS when VO will sit on top).

## Scoring a lesson or film

When movie-producer or tutorial-instructor hands you a picture lock

1. Copy runtime and section list into ARR-SPEC
2. Spot cues — where music enters, where it must die for a spoken instruction
3. Map song sections onto video scenes (see `high-quality-video-generator` tag map)
4. Do not fight `[Tempo]` with a new BPM

## Quality gate

- Header four-pack present on LYRICS.txt
- LYR-SPEC and ARR-SPEC agree on form, key, tempo, title line
- Chorus title appears in the chorus
- Every section has an explicit tag
- No placeholder lines ("yeah yeah oh")
- Renderer files do not contradict the specs
- Lesson beds leave VO headroom

## Do not

- Claim YuE / ACE-Step / Suno rendered audio in this sandbox unless the user ran those weights
- Start a second folder when `full-song-generator` already owns the slug
- Dump a theory textbook into chat
- Copy copyrighted lyrics
