# Walkthrough contract

The file movie-producer consumes. Write it as soon as website/software teaching starts.

Path: `/home/workdir/artifacts/lessons/<slug>/WALKTHROUGH.md`

```
# Walkthrough
job:
audience:
aspect: 16:9 | 9:16 | 1:1
duration_s:
source_slug:
vo_wpm: 150

## Beats

### Beat 01
clock: 0-4
screen: Dashboard / empty state
action: Point at the Create button in the top right
vo: Start on the dashboard. The thing you need is Create, top right.
expect: Create dialog opens
recover: If you see Billing instead, you are on the wrong workspace.
passport: ui-dashboard
verified: yes | UNVERIFIED
```

Rules

- clock ranges must sum to duration_s plus or minus 10 percent
- vo is speakable. Read it out loud in your head. Cut clauses that trip
- action is what the picture shows, not a paraphrase of the vo
- verified=yes only if this session captured that screen or the user confirmed it
- passport ids must exist in the film PASSPORTS folder once movie-producer runs
