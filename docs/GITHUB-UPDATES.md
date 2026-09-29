# GitHub updates

The company name is **ObzueAI**. Do not spell it any other way in a commit, a skill, or this repository.

This repository holds Professor's skills and the how-to. It is not the running window. Pushing here does not by itself change the live room.

## When to push

Push after a skill, the how-to, or this instruction changes. One change, one commit, then `main`.

## What goes in the commit

- The skill folder under `skills/<name>/`, including `SKILL.md` and any reference or script that changed
- `docs/HOW-TO-USE.md` if the room, the desk, the languages, or the script behavior changed
- `README.md` if the installed skill list changed

## What stays out

- `__pycache__` and any bytecode
- Secrets, tokens, and local notes
- A copy of someone else's skill text. Write the procedure in our words

## Message

Say what Professor can do now. Do not write "update" alone.

## After the push

`main` on [obzue/instructor-skills](https://github.com/obzue/instructor-skills) is the record. If the how-to PDF was regenerated, replace `docs/obzueai-professor-how-to.pdf` in the same commit as the how-to.
