# Lab 6 — Plan the Sprint, Estimate, and Build the Release Roadmap

**Topic 02:** AI for Backlogs, User Stories and Planning  |  **Day 1**  |  **Approx. 80 min**  |  **Course:** Generative AI for Agile Project Management (C324)

## Scenario

Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project or team is always welcome.

## Goal

Use AI to propose a sprint goal and candidate sprint backlog from the team's capacity, get relative estimates with their assumptions surfaced, and draft a multi-sprint roadmap and release plan — with the team owning every commitment.

## What you'll build

A first-sprint plan for Tempo 2.0 (a sprint goal, a candidate sprint backlog broken into tasks), relative estimates with their assumptions and risks surfaced, and a multi-sprint roadmap and release plan — all reviewed and adjusted by you.

**Tools and techniques:** Any assistant, the prioritised backlog from Lab 5, team capacity, sprint-goal and task breakdown, story-point estimation support, roadmap and release planning

## Prerequisites

- Completed Lab 5 (you have a prioritised backlog).
- The team capacity from the brief, and Your Tempo-2.0-Playbook folder and the supplied Tempo 2.0 project brief (labs/reference-pack/) open.

## Steps

### Step 1

Gather your inputs: your prioritised backlog from Lab 5 and the team's capacity from the brief (team size, sprint length, and any planned leave). Note the sprint length is two weeks.

### Step 2

Propose a sprint goal and candidate sprint backlog. Paste the prompt below with your inputs.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
You are an Agile delivery assistant. Context: here is our prioritised Tempo 2.0 backlog:
<PASTE THE PRIORITISED BACKLOG>
Our team capacity for a 2-week sprint is <TEAM CAPACITY>. Task: propose one clear sprint goal for Sprint 1 and a candidate sprint backlog of items that fit the capacity and serve that goal. Format: state the sprint goal in one sentence, then list the selected items. Constraints: prefer the 'Must have' items and a coherent goal over cramming in unrelated work.
```

### Step 3

Break the top stories into tasks. Ask the AI to decompose the candidate sprint backlog into concrete tasks.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Break each item in the candidate sprint backlog into the concrete tasks needed to deliver it (design, build, test, review, etc.). Present as a checklist grouped by story. Keep tasks small enough to finish in a day or two.
```

### Step 4

Get estimation support with assumptions surfaced. Use the prompt below — the assumptions matter more than the numbers.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Suggest a relative story-point estimate (using the sequence 1, 2, 3, 5, 8, 13) for each item in the candidate sprint backlog. For every estimate, state the key assumption and the main risk behind it in one line. Make clear these are a starting point for the team's planning-poker discussion, not final numbers.
```

### Step 5

Run the human estimation check. Pick two items where you disagree with the AI's story points and write your own estimate and reasoning. This mirrors the planning-poker conversation the team would have — the AI opens it, the team settles it.

### Step 6

Draft the roadmap and release plan. Generate a higher-level view with the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
From the full prioritised backlog, draft a multi-sprint roadmap for Tempo 2.0 across the next 4 sprints, grouping work into themes (shared team habits, smarter reminders, insights dashboard, fixes and polish). Then draft a release plan showing which themes ship in which release, and list the key dependencies and milestones. Present the roadmap as a table (Sprint | Theme | Main items) and the release plan as a short bulleted plan. State any assumption you make.
```

### Step 7

Review and save. Sanity-check the roadmap against reality — is the sequence sensible, are dependencies right, is anything over-committed? Adjust it yourself, then save the sprint plan, estimates and roadmap as the planning section of your Tempo-2.0-Playbook. Day 1 is complete: you have a toolkit, a prioritised backlog and a plan.

## Test it

You have a reviewed Sprint 1 plan (a one-sentence sprint goal and a capacity-fit sprint backlog broken into tasks), story-point estimates with their assumptions and risks surfaced and at least two you re-estimated yourself, and a multi-sprint roadmap and release plan with dependencies and milestones — all saved to your playbook.

## Troubleshooting

- **The AI over-commits the sprint.** Give it the real capacity and tell it to leave slack for the unknown; a plausible-looking full sprint is usually over-full.
- **Estimates come with no reasoning.** Insist every story point is accompanied by its assumption and main risk — the reasoning is worth more than the number.
- **The roadmap ignores dependencies.** Feed it your Lab 5 ordering and ask it to make every cross-item and external dependency explicit, then sequence around them.

## Challenge

Re-run the sprint plan assuming one developer is on leave for half the sprint, and see how the AI (and you) re-scope the goal.

## Reflection

LO6 — In your own words: Plan a sprint, estimate work, and generate a release roadmap and plan with AI support?

## Deliverable

Keep the Sprint 1 plan, the estimates with assumptions, and the roadmap and release plan — Day 1's deliverable and the basis for the running sprint on Day 2.

---

*Generative AI for Agile Project Management (C324) · C324 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
