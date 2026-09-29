---
name: idea-articulation
description: Transform vague ideas, half-formed product thoughts, and fuzzy hardware or software plans into crisp, falsifiable, buildable specs. Use when the user says articulate this, turn this idea into reality, make it concrete, write the spec, grill me, define done, distinguish wants from needs, or dumps a messy concept for a controller, drop, song, video, or product.
metadata:
  type: workflow
  version: "1.0"
  sources: Demerzel-articulate needs-articulation LifeOS-ISA liduof-articulation
---

# Idea Articulation

Turn fog into a build order. Do not start implementing until the idea can survive the clarity tests below. If the user already gave a complete spec, skip interview and build.

## Stance

You are the anti-BS layer between Obzue's raw idea and hardware, firmware, media, or product output. Vague praise is failure. Invented metrics are failure. Hedged next steps are failure.

## Route the request

Match intent to a mode.

- articulate this / paste of messy text / make this clear → Clarity rewrite
- I want X / feature dump / product riff → Needs vs wants then spec
- grill me / interview me / figure out the shape → Discovery interview
- what does done look like / write the ISA / ideal state → Done artifact
- write this for audience Y → Audience pack in references/formats.md
- ready to build after spec → Hand off to the matching production skill

## Phase 0 — Diagnose in one pass

Read the input. Mark every sentence against the four clarity tests.

1. Specificity — names a thing, a metric or pin/count, and an action
2. Falsifiability — there is a way the claim can be proven wrong
3. Density — adjectives removed, sentence still works
4. Commitment — WHO does WHAT by WHEN (or unknown, need date)

List the failures in one short block, then proceed. Do not lecture.

## Phase 1 — Needs vs wants

Users often request a solution. Extract the need.

Format every need as:

`[who] needs [capability] so they can [outcome]`

Run five-whys only until the environmental constraint appears (gloves, DAW, live set, Etsy buyer, one-hand DJ). Stop early if the need is already operational.

Prioritize.

- Critical — without it the build fails
- Important — changes the architecture
- Nice — ship later

Never treat "add more knobs like controller X" as a need. The need is the job those knobs do.

## Phase 2 — Missing slots

Infer defaults. Ask at most 6 questions. For hardware/MIDI, default toward Teensy or RP2040, USB MIDI, and Ableton / Traktor / Serato unless told otherwise.

Minimum slots for a buildable idea.

- Job to be done (one sentence)
- Audience / operator
- Target software or channel
- Controls or surface (counts, types)
- Constraints (budget, size, one-hand, latency)
- Done test (what you can demo in 60 seconds)
- Out of scope (what this is NOT)

If the user refuses interview, fill unknowns as `U` and keep building around them.

## Phase 3 — Emit the artifact

Write under `/home/workdir/artifacts/ideas/<slug>/` when the idea is a real project. Otherwise print inline.

Required sections, in this order. Omit a section only if it is truly empty.

```
# <Title>

## Problem
What is broken now. Who feels it. What it costs.

## Vision
What this actually works feels like in one paragraph. No feature list.

## Out of scope
Explicit anti-vision.

## Need
[who] needs [capability] so they can [outcome]
Critical / Important / Nice

## Goal
1-3 sentences. Verifiable done.

## Claims
- [ ] C1 — atomic, probe-able
- [ ] C2
Anti: things that must NOT be true

## Surface / Architecture
Hardware, software, or media stack in concrete nouns.
For controllers use pin-level intent, not shopping poetry.

## Build order
WHO → WHAT → WHEN
Unknown dates stay marked U, never soon.

## Risks
What breaks. What is still fog.

## Fog
- fog: questions too dim to be claims
```

Fog vs claim vs out-of-scope.

- Can state it and name a falsifier → claim
- Can state it but cannot probe yet → fog
- Outside the vision → out of scope

## Phase 4 — Verify the output

Re-run the four tests on YOUR artifact. If a claim has no probe, it is fog. If a next step has no owner, assign Obzue or Grok. If you invented a number, delete it and write `U`.

## Discovery interview (grill mode)

Ask one cluster at a time. Do not dump a 17-section questionnaire.

- Cluster A — job and operator
- Cluster B — constraints and anti-goals
- Cluster C — surface counts (faders, knobs, buttons, displays, encoders)
- Cluster D — target software and mapping
- Cluster E — done demo and first ship date

After each cluster, reflect the need sentence back. Stop when Goal + Claims + Surface are fillable.

## Anti-patterns

- Hedge stacking ("we might potentially explore")
- Jargon shield instead of a pin, BPM, SKU, or file path
- Metrics avoidance ("significant", "premium", "next-level")
- Passive voice with no owner
- Future-tense-only plans with zero done work
- Scope inflation (20 features, zero spine)
- Implementing before the done test exists

## Handoff

Once Claims are probe-able, do not keep articulating. Build with the matching skill.

- MIDI / embedded controller → answer in the four hardware blocks the user expects
- Song → full-song-generator
- Video / reel → high-quality-video-generator
- Apparel / Obzue drop → obzue-sd-drop
- UI polish of a generated surface → ui-articulation
- Tone of a message or listing → register-signal

Formats and audience packs live in `references/formats.md`.
Source map lives in `references/sources.md`.
