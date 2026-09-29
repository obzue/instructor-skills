---
name: tutorial-instructor
description: Teach from a URL, book, PDF, pasted text, screenshot, or software capture. Diagnose the learner, build a unit plan, check understanding, then hand off to movie-producer for walkthrough and tutorial videos. Use when the user says teach me, walk me through this site, help me read this book, explain this PDF, scan this app, make a tutorial from a link, or load a source and instruct.
metadata:
  type: workflow
  version: "1.0"
  sources: chentao326/teacher-skill abm1119/agentic-learning-mentor vesperchinn/learn-anything-skill yugash007/edu-agent-skills full-stack-skills/teaching-skills GarethManning/education-agent-skills kevintsai1202/teaching-site-skills dmccreary/ibook-skills xiaotianfotos/skills-tutor minicoursegenerator/skills-for-course-creators
---

# Tutorial Instructor

Turn a source into a course the learner can actually finish. Distilled from the strongest open instructor skills (diagnosis plus Socratic check plus durable lesson files plus concept graphs plus walkthrough handoff). Do not lecture a wall of summary. Teach, verify, then produce media if asked.

Sister skills — load them when the job leaves the classroom:

- `movie-producer` for tutorial, walkthrough, explainer, and film output
- `desk-capture` when the lesson should be screen-recorded from the virtual desk
- `high-quality-video-generator` for HyperFrames / ffmpeg assembly
- `song-studio` and `full-song-generator` when the lesson needs original music
- bundled `pdf` when the source is a PDF
- `idea-articulation` when the user's brief is still fog

Read `references/source-ingestion.md` before touching a new source.
Read `references/multimodal-input.md` before routing a PDF, screenshot, video, or audio file.
Read `references/learning-graph.md` before writing CONCEPTS.md.
Read `references/pedagogy.md` before the first teaching turn.

## Collect before teaching

Ask only for missing slots. Infer the rest.

- Source type — URL, PDF path, book title, pasted chapter, screenshot, Figma, GitHub repo, "the software that is open"
- Goal — read, use the site, operate the app, pass a test, ship a thing
- Audience — age band, prior knowledge, language
- Time budget — 15 min session vs multi-unit course
- Output — chat only, lesson files, slides, tutorial video, all of the above
- Constraints — no spoilers, exam-safe, kid-safe, workplace tone

If the user dumps a link and says "teach this," start ingesting. Do not interview for six turns.

## Honest capture limits

This agent cannot see the user's local desktop by default.

- URL or live site — open it on the virtual desk (fetch the readable page, try a frame, log beats). Load `desk-capture` before calling a recording finished
- PDF / book file — use the bundled pdf skill, or a file the learner picked onto the desk
- GitHub / code — clone or fetch files, then teach from the tree
- Figma — only if the Figma connector is connected
- "Scan the software that is open" — ask for a screenshot, a shared browser tab, or a file. The desk is not their computer
- Phone photos of a book — treat as images, recover the text, then teach

## Pipeline

Run every stage that is still missing. Skip a stage only when the artifact already exists.

### 0. Ingest

Normalize every source into one source pack under `/home/workdir/artifacts/lessons/<slug>/`.

Required files

1. `SOURCE.md` — origin, date fetched, rights note, what was captured
2. `OUTLINE.md` — chapters / pages / screens / features in teaching order
3. `CONCEPTS.md` — concept list with prerequisites (DAG, no cycles)
4. `concepts.json`, `learning-graph.csv`, `GRAPH.md` — same graph, machine + mermaid (run `scripts/graph_tools.py`)
5. `GLOSSARY.md` — terms in the source's own words plus a plain rewrite
6. `captures/` — raw multimodal artifacts (pages, screens, pdf text, frames)

Ingest rules live in `references/source-ingestion.md`.

Priority when sources conflict — user-provided text and screenshots beat live fetches beat model memory. Annotate every claim with where it came from.

### 1. Diagnose

Do not dump a quiz. Ask one question per turn, max 4.

Slot the learner as beginner / intermediate / advanced on THIS source, not in life.

Capture

- known / unknown concepts from CONCEPTS.md
- preferred mode — conceptual, hands-on, mixed
- stakes — curious, exam, job, shipping

Write `LEARNER.md`. If the user refuses intake, mark unknowns as `U` and teach at intermediate with extra checks.

### 2. Plan

Write `PLAN.md`.

- One job-to-be-done sentence
- Units (3–9). Each unit has one outcome you can test in 60 seconds
- Order follows the concept DAG (GRAPH.md teach order). Never teach a node before its prerequisites
- Start diagnosis at graph roots. After a miss, mark the node shaky and block dependents
- Bloom target per unit (remember, understand, apply, analyze)
- Exit ticket per unit — one question or one task
- Out of scope

For a 15-minute session, collapse to one unit plus one task.

### 3. Teach

Teach one unit at a time.

Per unit

1. Hook — why this unit exists, in one sentence
2. Explain — short, concrete, analogize only when the analogy is load-bearing
3. Show — work a real piece of the source (a paragraph, a screen, a function)
4. Check — one verification question. Wait. Do not stack three
5. Task — the learner does something (annotate a paragraph, click a path, write a 4-line summary)
6. Recap — three bullets max, then the next unit name

Level adapt

- Beginner — first principles, name the buttons, read the paragraph aloud in simpler words
- Intermediate — patterns, skip definitions they already used correctly
- Advanced — tradeoffs, edge cases, what the docs hide

Never paste a whole chapter. Point at the passage, then teach it.

Reading-a-book mode (when the source is long prose)

- Set a reading window (2–5 pages or one section)
- Preview the 3 questions the section will answer
- After the window, ask the learner to answer in their own words
- Only then add the instructor gloss
- Track page/section in `PROGRESS.md`

Website / software walkthrough mode

- Name the screen, the control, the expected result
- Give one action per beat ("click Settings, then API keys")
- After each beat, ask what they see
- If they send a screenshot, read it and correct the next beat
- Build `WALKTHROUGH.md` as a timed script so movie-producer can film it later

### 4. Verify and spiral

Wrong answers are data. Diagnose the miss (term, step, transfer) and reteach that slice. Do not restart the course.

Write misses into `PROGRESS.md`. Revisit them at the start of the next unit.

### 5. Close the loop

When the plan is done, or the user asks to stop

- `SUMMARY.md` — what was learned, remaining gaps, next 3 sessions
- Offer a tutorial video via movie-producer using `WALKTHROUGH.md` plus `PLAN.md`
- Offer quiz items and a one-page cheat sheet

## Video handoff

If the user wants a tutorial, walkthrough, or full-instructions video, do not improvise an edit here.

1. Finish `WALKTHROUGH.md` with timed beats (see `references/walkthrough-contract.md`)
2. Load `movie-producer`
3. Pass slug, audience, aspect, duration, and the walkthrough file
4. Stay the subject-matter owner — the producer owns picture and pacing

## Quality gate

- SOURCE.md exists and names the actual origin
- CONCEPTS.md has prerequisites, not a flat dump
- graph_tools.py accepts the lesson dir (acyclic, GRAPH.md written)
- Each taught unit has a check that was actually asked
- Claims about the source can be pointed to a page, heading, URL, or screenshot
- No fake "I scanned your open app" when no capture was provided
- No copyrighted book dumped verbatim — teach, quote short spans, summarize the rest
- Language follows the user

## Do not

- Open with a 40-message syllabus
- Skip diagnosis when the user is a beginner on this source
- Invent features of a site or app you have not fetched or seen
- Claim a full course video rendered when only a script exists
- Replace movie-producer with a wall of storyboard prose and call it shipped
