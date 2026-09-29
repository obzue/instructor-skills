#!/usr/bin/env python3
"""SM-2 scheduler. Grades are integers 0-5. Ease never drops below 1.3."""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta


def review(card: dict, q: int, today: date | None = None, cap_days: int = 180) -> dict:
    if q < 0 or q > 5:
        raise ValueError("q must be 0..5")
    today = today or date.today()
    ease = float(card.get("ease", 2.5))
    interval = int(card.get("interval_days", 0))
    reps = int(card.get("repetitions", 0))
    lapses = int(card.get("lapses", 0))
    ease = ease + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    if ease < 1.3:
        ease = 1.3
    if q < 3:
        reps = 0
        interval = 1
        lapses += 1
    else:
        reps += 1
        if reps == 1:
            interval = 1
        elif reps == 2:
            interval = 6
        else:
            interval = int(round(interval * ease))
    if interval > cap_days:
        interval = cap_days
    if interval < 1:
        interval = 1
    out = dict(card)
    out.update(
        {
            "ease": round(ease, 4),
            "interval_days": interval,
            "repetitions": reps,
            "lapses": lapses,
            "due": (today + timedelta(days=interval)).isoformat(),
            "last_q": q,
        }
    )
    return out


def main() -> None:
    raw = json.load(sys.stdin)
    card = raw["card"]
    q = int(raw["q"])
    today = date.fromisoformat(raw["today"]) if raw.get("today") else date.today()
    json.dump(review(card, q, today), sys.stdout)


if __name__ == "__main__":
    main()
