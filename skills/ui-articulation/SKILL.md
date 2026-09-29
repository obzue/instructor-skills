---
name: ui-articulation
description: Translate vague UI taste into precise design language, defensible critique, and the smallest visual change. Use when the user says make it bigger, cleaner, premium, pop, obvious, airy, compact, polish this UI, explain what looks wrong, or wants an HTML before/after mock of a design phrase.
metadata:
  type: workflow
  version: "1.0"
  sources: liangming99-ui-articulation-skill
settings:
  awareness: earned-awareness
  self_grade: forbidden
---

# UI Articulation

Treat vague feedback as intent, not an instruction. Bigger is not a pixel value until you name the dimension.

## Gatekeeper

Do not mechanically apply a change that would make the surface worse unless the user marks it mandatory.

1. State the design risk
2. Name the principle or vocabulary term
3. Offer a better alternative that still hits the intent
4. If mandatory, implement with least damage

## Branch A — Real UI

When they give a screenshot, HTML, component, or complaint.

1. Name the surface and state
2. Map each vague phrase to a dimension
3. Diagnose only relevant dimensions
4. Gate harmful changes
5. Recommend the smallest coherent fix with a verification method

Dimensions. Typography, color, layout, interaction, motion, accessibility, copy, components.

Never leave modern / nice / clean / polished untranslated.

## Branch B — Ambiguity atlas

When they ask what a phrase could mean.

1. Quote the phrase exactly
2. Split into 4-8 interpretations, each one term + one parameter
3. Prefer a single self-contained HTML comparison file under `/home/workdir/artifacts/ui-atlas/`
4. Label every pair with term, parameter, and visible effect

Phrase maps live in `references/ambiguity-atlas.md`.

## Output rules

Lead with the issue and the term. Prefer one hierarchy fix over decorative glow. Touch targets stay at least 44px. Contrast stays WCAG-sensible unless the brief is explicitly raw/industrial.
