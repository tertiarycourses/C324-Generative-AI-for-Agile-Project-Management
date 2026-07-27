# Tempo 2.0 — Project Brief (reference pack)

This is the shared, fictional project used across all 12 labs. It is deliberately
realistic and slightly messy — that is what you will use AI to make sense of.
**Use this brief only if you cannot use a real, non-confidential project of your
own.** Everything here is made up; there is no real company, customer or data.

---

## Product vision

> **Tempo** helps people build and keep good habits by making progress visible,
> gentle and social. Where most habit apps track one person in isolation, Tempo
> lets small groups — a family, a team, a group of friends — keep a shared habit
> together, nudge each other, and see their combined streaks. Tempo 2.0 turns
> Tempo from a solo tracker into a **shared, smart and insightful** habit
> companion.

Tempo is made by **Cadence Labs**, a small Singapore product studio. Tempo 1.0
has been live for a year with a modest, loyal user base; the 2.0 release is the
studio's bet on growth.

## The 2.0 release — what we want to add

Three feature themes plus a round of fixes:

1. **Shared team habits** — a group can create a habit, invite members, and track
   it together with a combined streak and a simple leaderboard.
2. **A smarter reminder engine** — reminders that adapt to when a user actually
   completes a habit, instead of firing at one fixed time, with quiet hours and
   per-habit control.
3. **An insights dashboard** — a personal view showing streaks, best times of
   day, and week-over-week trends, with a gentle weekly summary.
4. **Fixes and polish** — clear the top reliability and usability bugs (below).

## The team & capacity

- **Product Owner:** Priya — owns the backlog and priorities.
- **Scrum Master / delivery lead:** *you*.
- **Developers:** Wei, Marcus, Sofia (3 developers).
- **Designer:** Ken (shared across two products, roughly half-time on Tempo).
- **Sprint length:** 2 weeks. **Working days per sprint:** 10.
- **Known constraints:** Ken (design) is on leave for 3 days in the first sprint;
  the reminder engine may depend on a third-party push-notification service.

## Raw feature ideas & wish-list (unsorted — this is what you'll groom)

- As a group, we want to track a habit together so we stay motivated.
- Shared habit needs an invite flow (link or code).
- Combined streak for a shared habit — how does it work if one person misses?
- Leaderboard for a shared habit (keep it friendly, not competitive/toxic).
- Reminders should learn my usual completion time and shift to it.
- Quiet hours — no reminders overnight.
- Let me set a different reminder per habit.
- Snooze a reminder for later today.
- Insights: show my current and longest streak per habit.
- Insights: "best time of day" for each habit.
- Insights: week-over-week trend chart.
- Weekly summary email/notification ("here's your week").
- Dark mode (much requested).
- Export my data (CSV).
- Bug: reminders sometimes don't fire on Android after a phone restart.
- Bug: streak occasionally resets to 0 after crossing midnight in some timezones.
- Bug: shared-habit member list doesn't refresh until app restart.
- Bug: completing a habit twice quickly counts it twice.
- Widget for the home screen (nice to have).
- Apple Watch / Wear OS complication (someday).
- Onboarding is confusing for first-time users (drop-off after signup).

## Definition of Done (team's agreed checklist)

A story is **Done** when: code is reviewed and merged; it meets its acceptance
criteria; it has passing tests; it works offline where relevant and degrades
gracefully; it has been checked on both iOS and Android; copy has been reviewed;
and the Product Owner has accepted it.

## Notes on priority (from Priya, the Product Owner)

> "The release stands or falls on **shared team habits** working well and
> reminders being **reliable** — that's the growth story and the top complaint.
> The insights dashboard is important but can follow. Dark mode and export are
> nice-to-haves. The midnight streak-reset and the Android reminder bug are
> embarrassing and should be fixed early."
