# Sample daily stand-up notes — Tempo 2.0, Sprint 1 (reference pack)

Raw, informal notes from the daily stand-up, in the team's own words. This is the
messy input you feed to AI in **Lab 7** (summaries and tracking) and reuse in
**Lab 8** (risks and dependencies). It is fictional. Sprint 1 goal, for context:

> **Sprint 1 goal:** Ship the core of shared team habits (create, invite, join,
> combined streak) and fix the midnight streak-reset and Android reminder bugs.

Sprint started with **34 story points** committed over 10 working days.

---

## Day 1 (Mon)

- **Wei:** Done: nothing yet. Today: starting the shared-habit data model. No blockers.
- **Marcus:** Today: picking up the midnight streak-reset bug, looks like a timezone issue. No blockers.
- **Sofia:** Today: invite-flow screens with Ken. Waiting on final designs.
- **Ken:** Designs for invite flow 80% done, will finish tomorrow. Reminder: I'm on leave Thu–Mon.
- **Priya (PO):** Available for questions on shared-habit rules all week.

## Day 2 (Tue)

- **Wei:** Done: shared-habit data model draft. Today: create-shared-habit endpoint. No blockers.
- **Marcus:** Done: reproduced the streak-reset bug, it's a UTC-vs-local mismatch. Today: fix + tests.
- **Sofia:** Blocked: still waiting on final invite-flow designs from Ken before I can build.
- **Ken:** Finishing invite designs today, will hand over before leave. Sorry for the delay.
- **Priya:** Clarified: if one member misses a day, the combined streak pauses, it doesn't reset.

## Day 3 (Wed)

- **Wei:** Done: create endpoint. Today: join-by-code. No blockers.
- **Marcus:** Done: streak-reset fix + tests, in review. Today: starting the Android reminder bug.
- **Sofia:** Unblocked — got the designs. Today: building the invite screens. Behind by ~a day though.
- **Ken:** Handover done. On leave from tomorrow. Reachable only for emergencies.
- **Priya:** Reminder engine — legal is checking the third-party push service's data terms. Not cleared yet.

## Day 4 (Thu)

- **Wei:** Done: join-by-code. Today: combined-streak logic. Blocked a bit: need Priya to confirm edge cases.
- **Marcus:** Android reminder bug is deeper than expected — reminders die after OS restart, may need a workaround. Might slip.
- **Sofia:** Building invite screens. Design questions now go unanswered with Ken away.
- **Priya:** Confirmed combined-streak edge cases with Wei. Still no legal clearance on the push service.

## Day 5 (Fri)

- **Wei:** Done: combined-streak logic first cut, in review. Today: leaderboard (stretch).
- **Marcus:** Android reminder bug — found a workaround but it needs QA on several devices. Behind.
- **Sofia:** Invite screens mostly done, but a couple of states need design input I can't get until Ken's back.
- **Priya:** Legal still reviewing the push-service terms. Flagging this as a risk to the reminder work.
