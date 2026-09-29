---
name: high-quality-video-generator
description: Produce high-quality videos with an OpenMontage-style pipeline, Hypit-style word-locked captions, HyperFrames compose/render, image storyboards, Voice narration, and ffmpeg assembly. Use when the user asks for a video, reel, short, trailer, explainer, music video, cinematic clip, talking-head, or agent video skill.
metadata:
  type: workflow
  version: "1.1"
  sources: OpenMontage hypit llm-video-maker ai-film-skills CogVideo LTX-Video Wan html-video
settings:
  awareness: earned-awareness
  self_grade: forbidden
---

# High Quality Video Generator

## Global instrument / timing layer (music video and scored films)

When the job is a music video, lyric visualizer, or any cut that rides a song, inherit the song skill header before any shot list. Do not invent a conflicting BPM, key, or section map.

```
[Style: Delta Blues, slide guitar, distorted harmonica, raw male vocals]
[Tempo: 74 BPM, 12-bar shuffle, heavy syncopation]
[Key: A Major]
[Atmosphere: Smoky, vinyl crackle, live performance]
```

Genre swaps (same keys, new values):

- Club / electronic — `[Style: Deep House, 4x4 kick, sidechained pads]` + `[Tempo: 124 BPM, steady pulse]`
- Orchestral / world — `[Style: Cinematic Celtic Folk, uilleann pipes, tin whistle]` + `[Tempo: 68 BPM, 3/4 waltz time]`
- Retro electronic — `[Style: Synthwave, 1980s analog synthesizers, driving retro bassline, clean female vocals]` + `[Tempo: 110 BPM, straight 4/4 time]`

Map song section tags onto video scenes. One section = one scene block unless the user wants coverage variants.

| Song tag | Video behavior |
| [Intro] / [Outro] | No lyric captions. Establish palette, location, instrument close-ups. Fade on [Outro]. |
| [Verse 1] / [Verse 2] | Lower energy picture. Word-locked captions. Clear face or object story. |
| [Chorus] | Coverage change, more layers, wider or harder cuts, title card allowed. |
| [Bridge] | Contrast lens, grade, or location. |
| [Instrumental Break] / [Guitar Solo] / [Drop] | Mute lyric captions. Cut on downbeats. Feature the named instrument or drop. |
| (Spoken) / (Whispered) | Caption style change (plain / smaller / desaturated). Do not treat as sung. |

Beat lock: parse BPM from `[Tempo]`. At 74 BPM a quarter = 811 ms; at 124 BPM a quarter = 484 ms. Land hard cuts and caption in-points on downbeats when a song file or STRUCTURE.md exists.

If lyrics arrive raw, run the song skill parser first (`full-song-generator/scripts/parse_lyrics.py`) and edit the chorus tags before boarding.

Write the four header lines at the top of `BRIEF.md` and `SHOTS.md` for scored jobs. Non-music jobs may skip the header.

## Overview

Treat video as a production pipeline, not a single prompt. Distilled from OpenMontage (agentic studio, 12 pipelines), Hypit (SVML / word-locked clone-and-variant), llm-video-maker, ai-film-skills, and open models CogVideoX, LTX-Video, Wan, HunyuanVideo, Open-Sora.

This agent does not host 24–80 GB text-to-video weights. Default path in-session is HyperFrames compose plus image/audio/ffmpeg. Also emit a portable shot list the user can feed to Veo, Seedance, Kling, Wan, or LTX.

Read references/pipelines-and-models.md before choosing a path. For scored / music-video jobs also read references/music-video-tag-map.md.

## Collect before shooting

- Goal (ad, song visualizer, explainer, trailer, talking head, clone-variant)
- Aspect (9:16 short, 16:9 youtube, 1:1)
- Duration (if scored, derive from song form + BPM, do not fight `[Tempo]`)
- Voice / on-camera vs B-roll only
- Brand palette and type vibe
- Must-use footage or song (pull `[Style] [Tempo] [Key] [Atmosphere]` and section tags)
- Platform

## Pipeline (OpenMontage order)

Run every stage. Skip only if the user already supplied that artifact.

1. Research — facts, references, banned claims
2. Proposal — logline, audience, runtime, style refs
3. Script — spoken words first. Time the VO at about 140–160 wpm
4. Scene plan — shot list with duration, start-word, visual, motion, on-screen text
5. Assets — stills via generate_image / search_images; speech via Voice; music from the song skill or user file
6. Edit — HyperFrames compose for designed motion plus captions, or ffmpeg slideshow/ken-burns for local MP4
7. Review gate — captions readable, audio peaks, jump cuts, dead frames
8. Deliver — MP4 plus shot list plus caption file

## Path A — HyperFrames (preferred in this session)

Connected tools

- hyperframes_by_heygen___compose — create or edit. Omit projectId on first call.
- hyperframes_by_heygen___get_project_status — poll when the user asks if it is done
- hyperframes_by_heygen___get_project — preview
- hyperframes_by_heygen___render_video — explicit downloadable MP4
- hyperframes_by_heygen___get_render_status — when they want the URL

Compose prompt must include aspect ratio, duration, scene-by-scene action, on-screen copy, voiceover text, music mood, and a designSource when the register is clear (blockframe, claude, mat, monochrome, signal).

Do not call render while compose is still processing. Do not invent project IDs.

## Path B — Local ffmpeg assembly

Use the bundled ffmpeg skill.

Typical stack

1. Voice voice_list_voices then voice_generate_speech with with_timestamps=true if captions are needed
2. One still per scene via generate_image (consistent character sheet first)
3. Ken Burns / crossfade / hard cut per scene duration
4. Mix VO plus bed, cap loudness, burn captions if requested

Write working files under /home/workdir/artifacts/videos/<slug>/

## Path C — External T2V / I2V (user GPU or API)

Emit SHOTS.md with one block per shot

SHOT 04
duration: 4s
start_word: when the circuit closes
camera: slow push in, 35mm, shallow fog
action: close-up of copper traces lighting up
first_frame: path/to/04_start.png
last_frame: path/to/04_end.png
model_hint: LTX-Video or Wan 2.2 I2V
negative: morphing hands, extra fingers, watermark, text

Model hints

- Open-Sora 2.0 — most-starred open T2V project
- CogVideoX — Diffusers-friendly, about 16 GB
- LTX-Video — fast
- Wan 2.2 — 1.3B on 8 GB, 14B on 24 GB
- HunyuanVideo — high quality, 60–80 GB class
- Paid cinematic — Veo, Seedance, Kling, Sora (user account)

## Hypit-style word locking

Anchor cuts and captions to transcript words, not wall-clock guesses.

If Voice timestamps exist, cut on sentence boundaries from timestamps.json. Keep burned captions at most 42 characters per line, 1–2 lines, high contrast.

For clone-and-variant jobs, separate locked structure (pacing, caption rhythm, B-roll slots) from swap layer (face, product, language, hook line). Do not claim a Hypit render ran unless the user installed that CLI.

## Quality gate

- First 2 seconds state the hook
- No stretched stills that jitter
- VO does not collide with lyric or SFX peaks
- Aspect matches platform
- No unreadable tiny type
- Music video cuts land on downbeats when a song is provided
- Scored jobs copy the four-line global header into BRIEF.md and SHOTS.md
- Chorus / verse / drop boundaries in the edit match the song section tags
- (Spoken) lines are captioned as speech, not sung karaoke

## Do not

- Promise photoreal 4K T2V from this sandbox
- Download random copyrighted film clips as B-roll
- Ignore the ffmpeg skill when assembling local media
