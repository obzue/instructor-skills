---
name: obzue-sd-drop
description: Produce ObzueAI Enterprise product videos and lifestyle stills from an SD list. Use when Obzue, ObzueAI, a new drop, SD list, bomber, varsity, Etsy listing, print lock, or same-manner video and images is requested.
metadata:
  type: workflow
  version: "1.0"
  brand: ObzueAI Enterprise
---

# ObzueAI SD Drop Pipeline

Every new SD list (style/design list) uses this exact manner. Do not invent a new process.

## Brand lock

- Brand names: ObzueAI Enterprise on camera and end card. In prose the company is ObzueAI. Shop handle Obzue Enterprise.
- Shop URL: https://www.etsy.com/shop/ObzueEnterprise
- Accent: cyan `#2AD4EE` on dark `#07090C`
- End card copy, always: `ObzueAI Enterprise` / `Job is live.` / `etsy.com/shop/ObzueEnterprise`
- Never put the standalone mascot image in a scene. It is a print-check reference only.

## Print lock (non-negotiable)

Official product plates are the only legal print.

| Plate | File pattern | Must show |
| Front | SWEAT1A / front | Cyan robot, visor OBZUE, chest OBZUE |
| Back | SWEAT1B / back | ObzueAI wordmark, SINCE 2024 |
| Left | SWEAT1C / left | White sleeve, black rib, wrap |
| Right | SWEAT1D / right | Sleeve mark, black cuff, same type |

Rules:

- Do not generate a new chest graphic or a new back wordmark.
- If I2V or I2I drifts the print, drop that take. Cut to the official plate.
- If a shot at any timestamp shows a different logo or font, cut it. Do not prompt a fix.
- Front of the garment stays visible in talent shots. Back coverage uses the official back plate.

## Talent and wardrobe lock

Unless the new SD list names a different model, keep:

- Same man as the locked hero still
- Blue baseball cap
- The drop garment from the official plates
- Blue jeans
- Blue and white Jordan-style highs

Do not change face, cap, jeans, or sneakers across a set.

## Video manner (every drop)

Runtime at least 50 seconds. 16:9, 1280x720, 30 fps.

Script template (stretch, do not shrink):

1. He walks into a clothing store in the locked outfit.
2. Someone asks: `Where'd you get that sweater from?`
3. He answers: `At the Etsy store with Obzue Enterprise.`
4. VO can expand around front print, back wordmark, and the shop link.
5. End card as specified above.

Shot order (commercial camera, human action, not stills-only):

| t | Shot | Camera |
| 0-6 | Walk-in | Slow zoom out / pull |
| 6-12 | Jacket hero | Slow zoom in / push, front print readable |
| 12-18 | Face from the right | Dolly from his right |
| 18-24 | Face from the left | Dolly from his left |
| 24-32 | The ask | Two-shot, talking, jacket front on him |
| 32-38 | The reply | Talking, gesture, jacket front |
| 38-41 | Official front plate | Ken Burns zoom in |
| 41-44 | Official back plate | Ken Burns zoom out |
| 44-52 | End card | Slow push |

Motion rules:

- I2V from locked talent stills for walk, talk, and profiles.
- Ken Burns only on official plates and the end card.
- Subtle commercial moves (push, pull, left, right). No random handheld that crops the print.
- Dialogue starts at the ask, not over the walk-in.

## Still manner (every drop)

Produce three packs of four. Same guy, same garment, same sneakers, same cap.

Pack A — one setting, four poses (example locked setting: premium e-bike in a busy city at dusk).

- Bike lock when used: matte-black e-bike, cyan/blue LED trim around both wheels.
- Poses: ride toward camera, side profile, look-back one foot down, parked turned to camera.

Pack B — same setting, four camera angles.

- Low hero at wheel height
- High 45-degree overhead
- From behind / over the shoulder
- Handlebar-height wide, wheel in the foreground

Pack C — new setting, four angles, standing in front of the same bike.

- Locked example: train yard, graffiti freight cars, tracks, ice-cold cup in hand.
- Looking up at the sky, looking to the right, low angle at the tracks, open to camera with cup raised.

Crop generator watermarks before publishing.

## Etsy manner (every drop)

Title pattern: `[Product], [Color Graphic Cut], [Audience Style]`

Locked example title: `AI Robot Bomber Jacket, Cyan Graphic Varsity, Unisex Streetwear`

- Under 15 words. No pipes. No gift words in the title.
- Exactly 13 tags, each ≤20 characters, none echoing title words.
- Photo 1 is the clean official front plate, no type overlay.
- Lifestyle stills and title cards go in slots 2–10 plus video.
- First sentence of the description restates the title.

## New SD list intake

When the user sends a new SD list, collect only what changed. Keep everything else from this skill.

Required fields:

```
DROP:
GARMENT:
FRONT PRINT LOCK:
BACK PRINT LOCK:
PLATE FILES:
TALENT CHANGE (yes/no):
SETTING A:
SETTING B:
ASK LINE:
REPLY LINE:
ETSY TITLE:
```

Then run, in order:

1. Confirm plates. Refuse to invent print.
2. Lock talent stills from plates + wardrobe.
3. Shoot the 52s commercial cut with the shot table above.
4. Shoot Pack A, B, and C stills.
5. Write title, 13 tags, opening description.
6. QC print on every frame. Cut drifted takes.

## QC gate

Do not deliver if any of these fail:

- Front print is a different robot, visor, or font
- Back says anything other than the official back plate
- Standalone mascot fills the frame as a character
- People are frozen stills with no I2V action in the story beats
- Runtime under 50 seconds
- End card missing ObzueAI Enterprise, Job is live, or the Etsy URL
