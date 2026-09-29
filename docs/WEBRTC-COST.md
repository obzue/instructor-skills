# Live room cost

Prices checked September 2026. A live class is not free just because the window is installed.

## Published rates

| Service | Price | Source |
|---|---|---|
| Cloudflare Realtime SFU and TURN | $0.05 per GB sent to clients. First 1,000 GB each month is free, shared by both. Inbound is not billed. TURN into the same SFU is not billed twice. | Cloudflare Realtime pricing, updated 22 September 2026 |
| Cloudflare RealtimeKit | $0.002 per video participant-minute. $0.0005 audio-only. $0.010 per minute to record or stream out. | Cloudflare RealtimeKit pricing, updated 3 September 2026 |

## One class

Assumption: 1 presenter, 29 students, 60 minutes, only the desk is video at about 1.5 Mbit/s, students do not send cameras.

- Desk video to 29 people is about 19 GB.
- At $0.05 per GB that is about $0.96, after the free 1,000 GB is used up.
- RealtimeKit, if all 30 people are video participants: 30 × 60 × $0.002 = $3.60.
- Audio-only students plus one video desk: about $0.87 of participant time, plus the desk egress if you are on the GB rate instead.

If every student also sends a camera, the GB bill grows by roughly the number of cameras. Do not build it that way. One desk, voices, and a raised hand.

Twenty such classes a week in a term of 36 weeks is on the order of $700 to $2,600 a year of media, depending on which price you are on and whether the free gigabytes are still available. Recording adds $0.60 an hour at the RealtimeKit export rate.

The $12 a host a month suggested earlier covers this for a normal department. It does not cover a campus that records every camera.
