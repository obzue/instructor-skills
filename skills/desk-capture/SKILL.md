---
name: desk-capture
description: Record a lesson desk — a virtual browser or a file the learner opened — as a beat log plus a short film. Use when the user says screen record, film this page, capture the walkthrough, record the tutorial, or save what we just did on the site.
metadata:
  type: workflow
  version: "1.0"
  sources: microsoft/skill-recorder github/awesome-copilot/screen-recording jodonnell24/screenstage
settings:
  awareness: earned-awareness
  self_grade: forbidden
---

# Desk capture

Belongs to ObzueAI Professor. The company name is ObzueAI.

Film the lesson surface, not the learner's computer. Distilled from three public approaches and rewritten: a local timeline of intent and steps, a cropped paced demo, and a browser capture that can be either live or replayed on its own clock.

Do not copy those repositories. Do not install their apps. This skill is the procedure.

Sister skills: `tutorial-instructor` owns what is taught. `movie-producer` owns a finished tutorial film when the take needs shots, narration, and edit. This skill only captures the desk.

Read `references/capture-contract.md` before writing a beat log or calling the film finished.

## What to record

Record one of these, and name which one in the take:

1. The virtual desk — address, title, readable text, and the links the learner followed
2. A file the learner picked — PDF or text. Never the rest of the disk
3. A tab the learner explicitly shared. If they decline, say so and keep the desk film

Do not record a phone, a lock screen, or another app that was not put on the desk.

## Two clocks

- Live — the learner drives. Log each open, back, forward, file, and note with a timestamp. Thinking pauses stay in the live take
- Replay — after the log exists, play the beats on their own clock so model delay is not in the film. Pause after an action, then add one annotation. Do not annotate during the action

## Beat log

Write `beats.json`:

```json
{
  "intent": "Show how spaced repetition schedules a card",
  "beats": [
    { "t": 0.0, "kind": "open", "url": "https://example.com/page", "label": "Opened the article" }
  ]
}
```

Kinds: `open`, `back`, `forward`, `file`, `note`, `film-start`, `film-stop`.

Run `scripts/validate_beats.py beats.json` before treating the log as a lesson.

## From a take to a procedure

Only after the learner has seen the log:

1. One intent sentence
2. Ordered steps a person can follow without the video
3. Drop passwords, tokens, cookies, and anything that looks like a secret
4. Hand the steps to `tutorial-instructor` as `WALKTHROUGH.md` if they want a full class
5. Hand the film to `movie-producer` only if they want a cut, not a raw desk take

## Picture

- Crop to the desk. Do not film a desktop you do not have
- Readable desk film is WebM drawn from the title, address, and text the desk actually fetched
- A shared-tab recording is the only pixel capture of a live frame, and only after a browser prompt
- Silent proof can stay a short film. Add voice later. Do not invent a voice track
- 8 frames a second is enough for reading. Do not chase a cinematic frame rate on a text desk

## Do not

- Claim the film shows a site that refused to load
- Claim you recorded their screen if they only got the readable desk film
- Store a secret because it was visible in an address or a form
- Turn a raw take into a skill file until the learner reviews the steps
