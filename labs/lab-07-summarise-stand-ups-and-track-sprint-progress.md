# Lab 7 — Summarise Stand-ups and Track Sprint Progress

**Topic 03:** AI for Sprints, Standups and Delivery  |  **Day 2**  |  **Approx. 50 min**  |  **Course:** Generative AI for Agile Project Management (C324)

## Scenario

Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project or team is always welcome.

## Goal

Turn raw daily stand-up notes into a clear, consistent summary with AI, then track progress against the sprint goal and draft a plain-language burndown narrative — keeping the team's read of reality in the loop.

## What you'll build

A clean daily stand-up summary generated from raw notes, a progress-against-goal update, and a plain-language burndown narrative for the Tempo 2.0 sprint — all reviewed and saved as the tracking section of your playbook.

**Tools and techniques:** Any assistant, the stand-up-summary template from your prompt library, the raw stand-up notes, progress-against-goal tracking, a burndown narrative

## Prerequisites

- Completed Day 1 (you have a planned sprint and a prioritised backlog).
- The supplied raw stand-up notes (labs/reference-pack/), your stand-up template, and Your responsible-AI checklist from Lab 3 open beside you.

## Steps

### Step 1

Open the supplied raw daily stand-up notes for the Tempo 2.0 sprint (labs/reference-pack/) — several days of terse, informal updates from the team. Grab your stand-up-summary template from your prompt library.

### Step 2

Summarise one day's stand-up. Paste the prompt below with a single day's raw notes.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
You are a Scrum Master assistant. Here are today's raw daily stand-up notes for our Tempo 2.0 sprint:
<PASTE ONE DAY'S RAW NOTES>
Task: summarise them clearly under three headings — Done since yesterday, Planned today, Blockers. Format: short bullet points. Constraints: use only what the notes say, keep each person's items attributed, and list any blocker separately so nothing is buried.
```

### Step 3

Review the summary against reality. Check it captured every blocker and did not invent progress. If a note was ambiguous, decide what it really meant — the AI cannot know, you can.

### Step 4

Track progress against the sprint goal. Feed several days of notes and the sprint goal together with the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Here is our Sprint 1 goal:
<PASTE THE SPRINT GOAL>
and here are the stand-up summaries for the last few days:
<PASTE THE DAILY SUMMARIES>
Task: describe our progress toward the sprint goal — what has clearly moved forward, what is stuck, and whether the goal still looks achievable this sprint. Be honest and specific; do not sugar-coat. Flag anything that looks at risk.
```

### Step 5

Draft a burndown narrative. Ask the AI to describe the remaining work in plain language, using the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Given that the sprint started with <TOTAL STORY POINTS> points and roughly <REMAINING POINTS> remain with <DAYS LEFT> days left, write a short plain-language 'burndown' narrative a non-technical stakeholder could understand: are we ahead, on track or behind, and what would need to happen to finish on plan? State the assumption behind your read.
```

### Step 6

Apply your judgement. Compare the AI's 'on track / behind' read with your own sense of the sprint. Where they differ, write the truer version yourself. A burndown narrative is only useful if it is honest.

### Step 7

Save the tracking section of your playbook: the daily stand-up summary, the progress-against-goal update and the reviewed burndown narrative, in your Tempo-2.0-Playbook folder.

## Test it

You have turned raw stand-up notes into a clean, attributed summary under Done/Planned/Blockers, produced an honest progress-against-goal update and a plain-language burndown narrative for the Tempo 2.0 sprint, and reviewed each against what you actually know — all saved to your playbook.

## Troubleshooting

- **A blocker got buried in the summary.** Prompt the AI to always list blockers separately and never merge them into general progress.
- **The summary invented progress.** It can only use the notes given — re-prompt with 'use only what the notes say' and correct anything not supported.
- **The burndown read feels too rosy.** Compare it with your own sense of the sprint and rewrite it honestly; an optimistic burndown helps no one.

## Challenge

Feed the AI a deliberately contradictory day of notes (one person says done, another says blocked on the same item) and see whether it flags the conflict — then resolve it yourself.

## Reflection

LO7 — In your own words: Summarise stand-ups and track sprint progress with AI while keeping the team's judgement in the loop?

## Deliverable

Keep the stand-up summary, progress-against-goal update and burndown narrative — they feed the risk log (Lab 8) and the status report (Lab 10).

---

*Generative AI for Agile Project Management (C324) · C324 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
