# Multimodal input

Normalize every input to a source pack file plus a modality tag on the concept it produced. Do not flatten a screenshot into "some text" and throw the layout away.

## Router (this harness)

| Input | Tool | What you write into the pack |
| pasted text | as-is | `captures/text.md` |
| URL / live site | `browse_page` then `browser_tab` with screenshot | `captures/pages.md` + `captures/screens/*.png` |
| PDF (text layer) | bundled pdf skill — pdfplumber / pdftotext | `captures/pdf.txt` per page range |
| scanned PDF / photo of page | `pdftoppm` then `tesseract` (pytesseract is installed) | page images + `captures/ocr.txt` |
| screenshot of software | `read_file` / vision on the image | `captures/screens/NN-label.png` plus a UI inventory |
| image (diagram, chart) | `read_file` or `view_image` | keep the image; write `captures/visual-notes.md` |
| local video file | ffmpeg — keyframes + audio extract | `captures/frames/` + `captures/audio.wav` |
| X / Twitter video | `view_x_video` | timestamped notes |
| Figma file | Figma connector, if connected | node tree + exports |
| Google Drive file | Drive connector | copied into artifacts, then route by type |
| GitHub repo | GitHub connector or clone | tree + chosen files |
| spoken request | Voice connector is TTS only | ask for text or a transcript file |
| "the app that is open" | no desktop observer | demand screenshot, recording, or URL |

Connected tools that are **output**, not intake: Voice TTS, HyperFrames render, Canva/Figma generate, image generation.

## Recipe — screenshot / UI

1. Save under `captures/screens/`.
2. Inventory: window title, selected nav, primary CTA, visible errors, unread badges.
3. Each labeled control that the lesson will use becomes a concept of kind `ui`.
4. Ask for the next state if a menu is closed. Do not invent items behind the fold.

## Recipe — PDF

1. Bound the page range. Default: the chapter they named, else first 15 pages.
2. If `pdftotext` returns almost nothing, treat as scan → render pages → OCR.
3. Keep figures as images (`pdftoppm` or `pdfimages`). Charts are concepts, not captions only.

## Recipe — video

1. `ffprobe` for duration.
2. Extract 1 frame every N seconds (N = duration/12, min 2s) plus scene-change frames if cheap.
3. Extract audio wav. There is **no speech-to-text connector** in this session. If the user needs a transcript, ask them to paste one or supply a `.txt`. Do not pretend a Whisper run happened.
4. Teach from visible UI + supplied transcript. Timestamp every claim.

## Recipe — mixed pack

A lesson may have a URL plus three screenshots plus a PDF chapter. Merge into one graph. When they disagree, user capture wins (see source-ingestion conflict priority). Tag the losing claim `superseded`.

## What multimodal is for

- Grounding — the graph cites a page, a frame, or a control
- Walkthrough video — screens become passports for movie-producer
- Diagnosis — "point at the button" only works if we have the button

It is not a substitute for a source pack. An unexplained screenshot is not a course.
