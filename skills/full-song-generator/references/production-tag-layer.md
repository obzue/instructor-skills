# Global production tag layer

Place this block at the top of every `LYRICS.txt`, `SUNO_PROMPT.txt`, and tagged prompt file. Never let a renderer guess style, tempo, key, or section boundaries.

## 1. Global instrument / timing / performance header

Always first, in this order:

```
[Style: <genre, lead instruments, vocal identity>]
[Tempo: <BPM, meter, groove>]
[Key: <key and mode>]
[Atmosphere: <room, texture, performance feel>]
```

Genre profile examples — swap the four lines, keep the schema:

| Family | Style | Tempo | Typical key | Atmosphere |
| Delta / roots | Delta Blues, slide guitar, distorted harmonica, raw male vocals | 74 BPM, 12-bar shuffle, heavy syncopation | A Major | Smoky, vinyl crackle, live performance |
| Electronic / club | Deep House, 4x4 kick, sidechained pads | 124 BPM, steady pulse | A Minor | Warehouse night, dark club, analog warmth |
| Orchestral / world | Cinematic Celtic Folk, uilleann pipes, tin whistle | 68 BPM, 3/4 waltz time | D Major | Mist, hall reverb, live session |
| Retro electronic | Synthwave, 1980s analog synthesizers, driving retro bassline, clean female vocals | 110 BPM, straight 4/4 time | E Minor | Neon glare, gated reverb snare, cinematic |

Do not invent a BPM that fights lyric density. Ballad 68–84, mid 92–112, dance 118–128, DnB 160–174, trap 130–150 half-time.

## 2. Section segment tags

Own line. Blank line after the tag. Never bury a section start inside a lyric line.

| Tag | Engine meaning |
| [Intro] / [Outro] | Instrumentation without lead vocal. Canvas only. |
| [Verse 1] / [Verse 2] | Lower energy. Clear vocal articulation. Story advances. |
| [Pre-Chorus] | Tension rise. Optional. |
| [Chorus] | More layers, harmony, vocal intensity. Hook lives here. |
| [Bridge] | Temporary contrast — key, POV, or density — before final chorus. |
| [Final Chorus] | Last hook pass. Allowed extra couplet or stacked harmony. |
| [Instrumental] | No vocal in that block. |
| [Instrumental Break] / [Guitar Solo] / [Drop] | Push vocal out of the buffer so beds take over. |

Never let the model guess where the chorus begins. Tag it.

## 3. Micro-timing and performance modifiers

Inline, on the lyric line they affect:

- `(Spoken)` / `(Whispered)` — drop pitched singing for that line
- `[Vocal Harmony: High octave duplicate]` — stack after a chorus block
- `[Instrumental: <what plays>]` — describe the bed when vocals rest
- `[Fade out: <what decays>]` — outro decay instruction
- `[Drop]` — electronic build → raw instrumentation

Quoted short lines and first-block fragments under ~25 characters may be auto-wrapped as `(Spoken)` by `scripts/parse_lyrics.py`.

## 4. Complete production template

```
[Style: Synthwave, 1980s analog synthesizers, driving retro bassline, clean female vocals]
[Tempo: 110 BPM, straight 4/4 time]
[Key: E Minor]
[Atmosphere: Neon glare, dense reverb snare, cyberpunk cinematic]

[Intro]
[Instrumental: Neon arpeggiator build-up, slow gated reverb snare]

[Verse 1]
Midnight shadows on a concrete floor,
Running faster through the open door.
(Spoken) There's no turning back.
The neon horizon is starting to crack.

[Chorus]
We ride the lightning, we break the code!
Lost frequencies on a forgotten road!
[Vocal Harmony: High octave duplicate]
Yeah, we hold the line before the lights go cold!

[Guitar Solo]
[Instrumental: High-gain retro lead guitar, shifting pitch bend]

[Outro]
[Fade out: Bassline echoes, synthesizers decay into delay loops]
```

## 5. Genre config dictionaries

Use these keys when calling `scripts/parse_lyrics.py` or writing `STRUCTURE.md`:

```python
{
    "style": "Synthwave, 1980s analog synthesizers, driving retro bassline, clean female vocals",
    "tempo": "112 BPM, straight 4/4 time",
    "key": "E Minor",
    "atmosphere": "Neon glare, dense reverb snare, cyberpunk cinematic"
}
```

Swap the dict for Delta Blues, Deep House, Heavy Metal, Cinematic Celtic, or a user brief. Keep key names `style`, `tempo`, `key`, `atmosphere`.
