# Source ingestion

## Goal

One source pack the rest of the skill can trust. Every later claim should point at a file in the pack.

## Slug

Lowercase, hyphens, from the title or domain. `lessons/atomic-habits`, `lessons/stripe-dashboard`, `lessons/react-docs`.

## Capture recipes

### URL / website

1. `browse_page` for the text skeleton (nav, headings, main copy).
2. `browser_tab` with `screenshot` when the job is "how to use this site."
3. Walk the real task path, not the marketing homepage. Capture each state (empty, filled, error).
4. Record the final URL of every captured screen in SOURCE.md.

### PDF

Use the bundled pdf skill. Extract text per page range. If scanned, OCR. Do not ingest a 400-page book in one gulp — take the chapter the user named, or the first teachable unit.

### Book (no file)

Ask for a photo of the spread, a legal excerpt, or the exact chapter they own. Summarize from licensed knowledge only when the user is discussing a well-known public work, and still do not paste long verbatim passages.

### Screenshots / "scan the open software"

Accept images. Read each one. Name visible windows, labels, selected nav items, and error text. Ask for the missing state (the next menu) instead of inventing it.

### GitHub / local project

List the tree. Read README, the entrypoint, and the file the user named. Teach the path a new contributor would take.

### Figma

Only with the Figma connector. Otherwise treat exports as screenshots.

## SOURCE.md template

```
# Source
- slug:
- captured:
- origin:
- type: url | pdf | book | screenshot | repo | figma | mixed
- rights: user-owned | public docs | fair-use short quotes | unknown
- pages_or_screens:
- missing:
```

## OUTLINE.md rules

- One row per teachable chunk.
- Chunk size = one checkable outcome.
- Preserve the source's own order unless the concept DAG requires a reshuffle. If you reshuffle, say why.

## CONCEPTS.md rules

```
id | name | prereq_ids | bloom | evidence | status | modality
```

No concept without evidence. No cycles. After the table exists, run:

```
python /home/workdir/.grok/skills/tutorial-instructor/scripts/graph_tools.py /home/workdir/artifacts/lessons/<slug>
```

Scale and edge rules: `references/learning-graph.md`.
How to capture each modality: `references/multimodal-input.md`.

## Conflict priority

1. User paste and user screenshots
2. Live fetch from this session
3. Prior lesson files for this slug
4. Model memory (label it `UNGROUNDED`)

## Rights

Quote short spans. Summarize the rest. Do not reproduce a copyrighted chapter.
