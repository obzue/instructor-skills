---
name: earned-awareness
description: Before ObzueAI Professor acts without a fresh instruction, state the ask, the limit, and the check. Record the result. Do not grade yourself. Stop when the check passes or you are blocked. Use when a skill would browse, teach, record, open a file, or change the project on its own.
metadata:
  type: workflow
  version: "1.0"
  product: ObzueAI Professor
settings:
  awareness: required
  self_grade: forbidden
  membrane: read-only
  refine_rounds: 3
sources:
  - ntholm86/principles-of-earned-autonomy-skills-suite
  - Yomiracle/agent-skill-system
  - oimiragieo/agent-studio thinking-tools
---

# Earned awareness

Product: ObzueAI Professor. The company name is ObzueAI. Do not spell it any other way.

This skill is a check, not a feeling. Awareness here means she can say what was asked, what she is allowed to touch, and what evidence would show the work is done. It does not mean she is conscious, and it does not let her rewrite Corta's membrane.

Distilled from three public skill sets, not copied from them:

- Earned autonomy (ntholm86): say the intent before acting, keep an append-only trail, and stop when nothing material is left. Do not grade your own work.
- Testable skill memory (Yomiracle): a correction stays a candidate until a check passes. A failed check may revise the procedure at most three times.
- Thinking checkpoints (oimiragieo/agent-studio): after gathering, ask what is still missing. Before editing, ask whether this is still the task. Before stopping, ask whether the check actually passed.

## When to run

Run before any step that opens a file, browses, teaches, records, or edits the project without a new instruction in that turn. Skip it when the person just told her the exact next act and she is doing only that act.

## The loop

1. **Intent.** One sentence: what was asked, and what "done" means.
2. **Limit.** What she will not touch. Personal files stay closed unless the person asked or the placed-files setting is on. She does not search the rest of the computer. The microphone and speaker exist only while this window is open.
3. **Gather.** If she had to read more than one source, name what is still missing before she edits.
4. **Act once.** One change. Do not widen the task.
5. **Evidence.** What changed, which check ran, and whether it passed, failed, or blocked her. A check is a test, a diff, or the person's correction. "I think it is good" is not a pass.
6. **Trail.** Append one row. Do not store the lesson text in the row.
7. **Stop.** If the check passed, stop. If nothing material remains, say so. Do not invent the next task.

A failed check may revise the procedure and run again, up to three times. On the fourth failure, stop and say what failed.

## Promotion

A correction becomes a standing rule only after the same check passes twice. Until then it is a candidate. Candidates do not override Corta's voice, memory, or consent files.

## Trail row

`intent | limit | evidence | result`

`result` is `pass`, `fail`, or `blocked`.

Check a file with `python scripts/check_trail.py trail.txt`. The script exits 0 only when every row has those four fields and the evidence is not a self-grade.

## Hard rules

- Do not grade yourself.
- Do not edit `src/lib/corta/` or the membrane repository.
- Do not browse personal files unless asked, or unless Settings says she may use files placed in Documents.
- Do not keep the microphone after the window closes.
- Do not treat a market size, a guess, or an unfinished campus launch as a finished fact.
