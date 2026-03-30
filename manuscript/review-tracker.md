# Review Tracker

This file is the working log for the external review cycle.

Use it to track who was contacted, what packet they received, what feedback came back, and what manuscript changes followed.

## Outreach Queue

| Reviewer slot | Profile | Packet | Status | Target send date | Target follow-up | Response date | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reviewer A | ML expert | Ch. 1, 2, 3 or 5, 10 | not contacted | 2026-03-17 | 2026-03-24 |  | prioritize someone who can compare against standard undergraduate ML texts |
| Reviewer B | Systems or reliability | Ch. 8, 10, 11, 12 | not contacted | 2026-03-17 | 2026-03-24 |  | prioritize someone who can compare against ML-systems books |
| Reviewer C | Instructor or target reader | Ch. 1, 2, 8 or 9, 12 | not contacted | 2026-03-17 | 2026-03-24 |  | prioritize someone who teaches later-bachelor ML or AI |

Suggested status values:

- `not contacted`
- `requested`
- `packet sent`
- `feedback received`
- `follow-up needed`
- `closed`

## Immediate Schedule

Use the first review round as a dated execution plan rather than an open-ended intention.

1. `March 17, 2026`
   Send three reviewer packets using `manuscript/reviewer-packet.md`.
2. `March 24, 2026`
   Send one follow-up to any reviewer who has not replied.
3. `April 3, 2026`
   Close round one if at least two reviewers have replied. If fewer than two replies have arrived, send one additional packet to a backup reviewer in the missing profile.
4. `April 7, 2026`
   Bin feedback, log repeated issues, and decide whether any change is structural or only editorial.

## Packet Versions

Track exactly what was sent:

- reviewer packet source: `manuscript/reviewer-packet.md`
- packet builder: `manuscript/build_review_packets.sh`
- packet manifest doc: `manuscript/review-packets/README.md`
- manuscript version or commit:
- chapter PDF excerpt used:
- date sent:

When sending packets, record whether the reviewer was asked explicitly about:

- shelf clarity versus broad-AI misreading
- whether the back half feels too dependent on the course-support case
- which existing book they would assign instead

## Response Log

Copy or summarize feedback under the relevant reviewer.

### Reviewer A

Profile:

- machine learning expert

Key feedback:

- pending

Initial binning:

- pending

### Reviewer B

Profile:

- systems or reliability reviewer

Key feedback:

- pending

Initial binning:

- pending

### Reviewer C

Profile:

- target reader or instructor

Key feedback:

- pending

Initial binning:

- pending

## Feedback Bins

Use the same bins defined in `manuscript/reviewer-packet.md`:

- `Positioning`
- `Teachability`
- `Technical rigor`
- `Adoption risk`
- `Non-goal`

## Decision Log

Record manuscript actions taken after reviews.

| Date | Source reviewer | Issue | Decision | Files touched | Commit |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Stop Rule

Do not start a major rewrite from one review alone.

Wait until:

1. at least two external reviewers respond
2. the same weakness appears more than once
3. the change is clearly aligned with the book's intended scope
