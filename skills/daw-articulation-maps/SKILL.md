---
name: daw-articulation-maps
description: Design DAW articulation and expression maps for sampled instruments and MIDI controllers. Use when the user mentions keyswitches, articulation mapping, expression maps, Cubase Expression Map, Logic Articulation Set, Studio One sound variations, Cakewalk articulation maps, UACC, or mapping legato staccato spiccato on a controller.
metadata:
  type: workflow
  version: "1.0"
  sources: r-koubou-ArticulationMappingFiles
---

# DAW Articulation Maps

Map playing techniques to MIDI, not adjectives. An articulation is a named switch with a channel, key, CC, or UACC value.

## Collect

- Library / instrument
- Target DAW (Cubase, Logic, Studio One, Cakewalk, Reaper, Ableton)
- Switch method the library already uses (keyswitch, UACC CC32, program change, keyvelocity, MIDI channel)
- Controller surface that will fire the switch
- Techniques required (sustain, legato, staccato, spic, pizz, trem, harmonics, con sord)

## Canonical technique table

Write a source table before exporting any DAW file.

```
id | name | group | trigger | value | latch/momentary | default
```

Rules.

- One sounding technique at a time inside a mutually exclusive group (bowed longs vs shorts)
- Additive techniques (sordino, sul pont) can layer if the library supports it
- Never collide keyswitches with the playable range
- Document the lowest playable note after keyswitches eat the bottom octave
- Prefer UACC when the library implements it so maps stay portable

Common UACC anchors (Spitfire-style, verify per library).

- 1 sustain / 7 legato / 8 portato / 40 staccato / 42 spic / 52 pizz / 56 col legno / 64 trem / 81 harmonics

## DAW export intent

Do not invent proprietary binary formats in-session. Emit.

1. SOURCE.md — the canonical table
2. Cubase-style text description of slots, groups, and output events
3. Logic Articulation Set intent (articulation ID, keyswitch note, output MIDI)
4. Ableton / controller mapping — which physical pad sends which note or CC
5. Firmware snippet if the surface is a custom MIDI box (note-on on channel 16 is a common keyswitch lane)

Point the user at https://r-koubou.github.io/ArticulationMappingFiles for generated DAW files when a matching library already exists.

## Controller wiring note

If the same device also runs faders and knobs, keep articulation switches on a dedicated MIDI channel or on notes below the instrument range so they never leak into pitched MIDI.
