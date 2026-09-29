# Capture contract

A finished desk take has three files, or an honest note that one is missing.

| File | Required | Contents |
| beats.json | yes | intent, ordered beats, no secrets |
| desk.webm | when a film was asked for | readable desk, or a tab share the learner accepted |
| NOTE.md | when something failed | which surface was refused, and what was captured instead |

## Beat

- `t` is seconds from the start of the take, non-decreasing
- `kind` is one of open, back, forward, file, note, film-start, film-stop
- `label` is a short human sentence, at most 180 characters
- `url` is a public http(s) address, or the literal `local-file` when the learner picked a file
- Never put a password, bearer token, or API key in any field

## Picture rules taken from the three sources, restated

- Log the action first, then the words. A label that appears before the page changes is a lie
- Pause, then one annotation. Do not cover the control the learner is supposed to see
- Scripted replay uses the beat timestamps, not the time the model spent deciding
- The manifest is the beats file. A film without a log is a clip, not a lesson

## Surfaces

| Surface | Capture |
| Virtual desk | Address plus extracted text plus optional frame |
| Learner-picked file | The file they chose, opened on the desk |
| Shared browser tab | Only after the browser permission prompt |
| Phone, locked desktop, another user's machine | Do not capture. Say so |
