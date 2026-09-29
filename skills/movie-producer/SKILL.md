---
name: movie-producer
description: Produce tutorial walkthroughs, explainers, shorts, and cinematic films with locked asset passports, shot cards, word-locked captions, and a review gate. Use when the user wants a movie, film, video editor, tutorial video, product walkthrough, explainer, trailer, demo, or to turn a lesson into a video.
metadata:
  type: workflow
  version: "1.0"
  sources: machina-exm/film-studio-skills hunanyanr/film-maker michaelboeding/video-producer-agent michaelboeding/walkthrough-script-agent Vincentwei1021/video-shotcraft haidrrrry/claude-remotion-skill smixs/visual-skills high-quality-video-generator
---

# Movie Producer

Run a production, not a prompt. Distilled from film-studio discipline (one asset, one passport, gates before generation), film-maker beat cards, and walkthrough-script timing. This sandbox does not host 24–80 GB video weights. Default in-session path is HyperFrames plus Voice plus ffmpeg. Always emit a portable shot list the user can feed to Veo, Kling, Wan, Seedance, or LTX.

Load `high-quality-video-generator` for assembly paths, caption locking, and model hints. This skill owns the producer layer — brief, bible, passports, gates, walkthrough timing, review.

Read `references/studio-laws.md` before scaffolding.
Read `references/shot-card.md` before writing a single shot.
For lesson videos also read `tutorial-instructor/references/walkthrough-contract.md`.

## Collect before shooting

Ask only for missing items.

- Job — tutorial walkthrough, explainer, product demo, trailer, short film, music video, talking head
- Source pack — lesson slug, URL, script, stills, footage folder
- Audience and platform
- Aspect — 16:9, 9:16, 1:1
- Duration
- On-camera / VO / silent
- Must-use assets (logo, face, product, song)
- Brand palette
- Renderer path — HyperFrames (default here), local ffmpeg, or external T2V

If `tutorial-instructor` already wrote `WALKTHROUGH.md`, treat that as locked narration plus screen action. Do not rewrite the subject matter.

## Studio tree

Scaffold under `/home/workdir/artifacts/films/<slug>/` (or reuse `/home/workdir/artifacts/lessons/<slug>/film/` when this is a lesson video).

```
BRIEF.md
BIBLE.md
ASSETS.md
WALKTHROUGH.md      # tutorials only
SHOTS.md
PASSPORTS/
SELECTS/
GENERATIONS/
FINISH/
```

Run `python scripts/scaffold_studio.py <slug>` then fill the files. Do not invent a second tree.

## Producer pipeline

Skip a stage only when its artifact already exists and is marked locked.

1. Brief — logline, audience, runtime, platform, banned claims, style refs
2. Breakdown — scene table, then one shot card per shot (see `references/shot-card.md`)
3. Passports — one descriptor per recurring character, product, UI chrome, location. Copy verbatim into every prompt. Never paraphrase a locked passport
4. Walkthrough timing (tutorials) — narration lines locked to on-screen actions with clocks
5. Reference board — approve or ban stills. Anti-references go on a ban list
6. Stress test — if a face or product must match across shots, generate cheap stills first. Do not lock a passport that fails a side-by-side
7. Assembly path — HyperFrames compose, or ffmpeg Ken Burns, or export SHOTS.md for an external model
8. Review gate — hook in 2s, captions readable, VO not colliding with music, aspect correct, no invented product UI
9. Deliver — MP4 if rendered, plus SHOTS.md, plus caption file, plus a change log

## Tutorial / walkthrough grammar

A tutorial is not a feature tour. One use case, one outcome.

Beat order

1. Hook (0–3s) — the outcome the viewer will be able to do
2. Orient — name the screen they should be looking at
3. Act — one control, one result, per beat
4. Recover — what to do if the screen does not match
5. Proof — the finished state
6. Next step — one

Narration rules

- Active voice. Name the real control.
- One idea per line.
- Match the words to the picture. If the VO says "click Export," the frame shows Export.
- Time VO at 140–160 wpm.
- First 2 seconds state the job.

Do not show a control the source pack does not contain. If the site was not captured, fetch it or mark the beat `UNVERIFIED`.

## Cinematic grammar (shorts and films)

- Identity lane — who is on screen, locked passport id
- Direction lane — action, emotion, what changes by the end of the shot
- Camera lane — size, lens, move, cut reason
- Edit lane — in-point word or downbeat, duration, incoming/outgoing cut type

One shot, one job. Coverage changes on chorus / reveal / problem-solution flip, not on boredom.

If a song is involved, inherit `full-song-generator` / `song-studio` headers (`Style`, `Tempo`, `Key`, `Atmosphere`) and cut on downbeats. Do not invent a conflicting BPM.

## Asset passport (non-negotiable)

Format in `PASSPORTS/<id>.md`

```
id: product-panel
status: draft | locked
kind: ui | person | prop | location
verbatim: <one paragraph copied into every prompt, never shortened>
states: default | hover | error
ban: watermark, extra buttons, made-up menu items
refs: path/to/still.png
```

Shot prompts paste `verbatim` as-is. If you need a wet / night / error state, fork a new id (`product-panel-error`) instead of editing the locked paragraph.

A shot that names a draft passport does not go to generation.

## Path routing

- Designed motion, captions, VO in this session — HyperFrames compose via `high-quality-video-generator` Path A
- Local MP4 from stills plus Voice — Path B (ffmpeg skill)
- User will generate elsewhere — emit SHOTS.md only, do not fake an MP4

Do not call HyperFrames render while compose is still processing. Do not invent project IDs.

## Quality gate

- BRIEF.md names job, runtime, aspect, banned claims
- Every recurring face/product/UI has a passport
- Locked passports are copied, not rewritten
- Tutorial beats cite a captured screen or are marked UNVERIFIED
- Hook lands in the first 2 seconds
- Captions ≤ 42 characters per line, high contrast
- Music videos land cuts on downbeats when a song file or STRUCTURE.md exists
- No copyrighted film clips pulled as B-roll

## Do not

- Skip the brief and jump to a single mega-prompt
- Paraphrase a locked passport to "save tokens"
- Promise photoreal 4K T2V from this sandbox
- Invent UI chrome for a product you have not seen
- Dump 40 disconnected shot ideas with no duration math
