# Lab 11 — Analyse Velocity and Metrics with AI

**Topic 04:** AI for Reporting, Retrospectives and Improvement  |  **Day 2**  |  **Approx. 52 min**  |  **Course:** Generative AI for Agile Project Management (C324)

## Scenario

Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project or team is always welcome.

## Goal

Use AI to analyse past sprint data — velocity trend, throughput, cycle time and completion rate — to forecast realistic scope, and to interpret the metrics honestly as signals for conversation, not targets to game.

## What you'll build

An AI-assisted analysis of the Tempo velocity and delivery metrics — a velocity-trend read, a realistic scope forecast with assumptions, and an honest interpretation of throughput, cycle time and completion rate as signals — reviewed by you and saved.

**Tools and techniques:** Any assistant, the sprint metrics history, velocity-trend analysis, scope forecasting, honest metric interpretation

## Prerequisites

- Completed Lab 10 (you have reported this sprint).
- The supplied sprint metrics history (labs/reference-pack/), and Your responsible-AI checklist from Lab 3 open beside you.

## Steps

### Step 1

Open the supplied sprint metrics history for Tempo (labs/reference-pack/) — several sprints of committed vs completed points, and any throughput or cycle-time figures. Paste it into any assistant.

### Step 2

Analyse the velocity trend. Use the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
You are an Agile delivery analyst. Here is our Tempo sprint history:
<PASTE THE SPRINT METRICS>
Task: analyse our velocity trend across these sprints — is it rising, falling, stable or too noisy to tell? Show the average and the range, and explain what could be driving the pattern. Constraints: state clearly if the data is too little to be reliable, and do not present a trend more confident than the data supports.
```

### Step 3

Forecast realistic scope. Ask the AI to project the next sprints with assumptions stated.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Based on that velocity analysis, forecast how many story points we could realistically commit to in each of the next 2 sprints, giving a conservative and an optimistic figure. State every assumption (team availability, no major disruption, similar work type). Make clear this is a planning aid, not a promise.
```

### Step 4

Verify the maths. Recompute the average velocity yourself from the raw numbers and compare it to the AI's. If they differ, find out why. Never report a metric you have not checked.

### Step 5

Interpret the wider metrics as signals. Use the prompt below for throughput, cycle time and completion rate.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Interpret our throughput, cycle time and sprint completion rate as signals for a retrospective conversation, not as performance targets. For each metric: what a healthy pattern looks like, what our numbers might be signalling, and one question the team should discuss. Explicitly warn against any way this metric could be gamed or misused to pressure individuals.
```

### Step 6

Add the human read. Write two or three lines of your own on what the metrics really suggest for Tempo, and note one thing the numbers do not capture (for example quality, morale, or hidden rework). Metrics inform the conversation; they do not end it.

### Step 7

Save the metrics analysis as a section of your Tempo-2.0-Playbook folder: the velocity-trend read, the scope forecast with assumptions, the signals interpretation, and your own honest commentary — ready to feed the retrospective.

## Test it

You have an AI-assisted metrics analysis for Tempo — a velocity-trend read you verified by re-computing the average, a scope forecast with explicit assumptions, and an honest interpretation of throughput, cycle time and completion rate as signals (not targets) — with your own commentary, saved to your playbook.

## Troubleshooting

- **The AI claims a strong trend from little data.** Tell it to state when the data is too small to be reliable and to avoid over-confident trends.
- **The average velocity looks wrong.** Recompute it yourself from the raw numbers — never report a metric you have not verified.
- **Metrics get framed as targets.** Re-prompt to treat every metric as a signal for conversation, and to warn against gaming or using it to pressure individuals.

## Challenge

Ask the AI to identify which single metric would most mislead a stakeholder if shown alone, and write one line on how you would present it responsibly instead.

## Reflection

LO11 — In your own words: Analyse velocity and delivery metrics with AI to surface trends and honest insights?

## Deliverable

Keep the velocity-trend read, scope forecast and signals interpretation with your own commentary — it feeds the retrospective in Lab 12.

---

*Generative AI for Agile Project Management (C324) · C324 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
