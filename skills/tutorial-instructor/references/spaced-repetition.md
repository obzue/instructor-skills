# Spaced repetition

Review a concept just before it is likely forgotten. Default scheduler is SM-2 (Wozniak). FSRS is the upgrade path once a review log exists. Do not invent a third formula.

## Card

A card is one concept at one Bloom slice.

```
id, concept_id, prompt, answer, bloom
ease: 2.5
interval_days: 0
repetitions: 0
due: ISO date
lapses: 0
```

Prompt matches the level. Remember asks for the term. Apply asks for the next action on a fresh case. Do not put an evaluate essay on a 10-second card.

## SM-2

Grade `q` from 0 to 5.

- 0 blackout
- 1 wrong, remembered after seeing the answer
- 2 wrong, answer felt familiar
- 3 correct with serious difficulty
- 4 correct after a hesitation
- 5 perfect

Ease update, then clamp ease to at least 1.3:

```
ease = ease + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
```

Schedule:

- if q < 3: repetitions = 0, interval_days = 1, lapses += 1
- else: repetitions += 1
  - repetitions == 1 → interval 1
  - repetitions == 2 → interval 6
  - else → interval = round(interval * ease)

Cap interval at 180 days for a course. A card whose ease sits on 1.3 for three lapses is a teaching failure, not a scheduling failure. Reteach that node before the next review.

Map UI buttons: Again=1, Hard=3, Good=4, Easy=5.

## When to schedule

- After a unit is checked, enqueue its concept at the exit Bloom level
- Due cards open the next session before new material
- A shaky graph node is due immediately, ignoring the interval

## FSRS later

Do not implement FSRS weights in this skill. Log every review (`q`, timestamp, interval, ease) in `reviews.jsonl` so a stability/difficulty model can be fit later. SM-2 does not predict a recall probability. Do not pretend it does.

## Code

`scripts/sm2.py` is the reference implementation. The instructor app must match it.
