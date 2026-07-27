# Lab 9 — Assist Documentation, Communication and Testing

**Topic 03:** AI for Sprints, Standups and Delivery  |  **Day 2**  |  **Approx. 60 min**  |  **Course:** Generative AI for Agile Project Management (C324)

## Scenario

Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project or team is always welcome.

## Goal

Use AI to draft the sprint's routine documentation, tailor the same update for different audiences, and generate test scenarios and a definition-of-done check from acceptance criteria — reviewing each so quality stays the team's call.

## What you'll build

AI-assisted sprint documentation (release notes, a decision log entry, meeting minutes), one update re-pitched for the team, stakeholders and leadership, and test scenarios plus a definition-of-done check generated from your acceptance criteria — all reviewed and saved.

**Tools and techniques:** Any assistant, documentation drafting, audience-tailored communication, test-scenario generation from acceptance criteria, a definition-of-done check

## Prerequisites

- Completed Lab 4 (you have acceptance criteria to test against) and Lab 7 (you have an update to re-pitch).
- Your Definition of Done, and Your responsible-AI checklist from Lab 3 open beside you.

## Steps

### Step 1

Draft the routine documentation. Using what the sprint has delivered so far, generate release notes with the prompt below, then repeat the idea for a decision-log entry and short meeting minutes.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
You are a delivery documentation assistant. Based on the work completed in our Tempo 2.0 sprint so far:
<PASTE THE COMPLETED ITEMS>
Task: write concise release notes under 'New', 'Improved' and 'Fixed'. Then, separately, draft a one-paragraph decision-log entry template and a short meeting-minutes template we can reuse. Constraints: use only the information given, and mark anything uncertain as '[to confirm]' rather than inventing it.
```

### Step 2

Review the docs for invented detail. Check the release notes claim only what was actually done, and that every '[to confirm]' is a real gap for a human to fill. Correct anything overstated.

### Step 3

Tailor communication for three audiences. Take one progress update and re-pitch it with the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Here is a sprint progress update:
<PASTE YOUR PROGRESS UPDATE FROM LAB 7>
Rewrite it for three audiences: (1) the development team — technical, detailed, honest about blockers; (2) stakeholders — plain language, focused on value and dates; (3) leadership — three lines, the headline, the risk and the ask. Keep every version truthful to the same facts; only change tone and detail.
```

### Step 4

Check the tone yourself. Read the leadership version as if you were the executive: is it clear, honest and free of jargon and spin? Adjust it — you own how the team communicates, not the AI.

### Step 5

Generate test scenarios from acceptance criteria. Feed your Lab 4 acceptance criteria in with the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
For the user story and acceptance criteria below:
<PASTE A KEY STORY AND ITS GIVEN/WHEN/THEN CRITERIA>
Task: write test scenarios that would verify each acceptance criterion, including edge cases and error conditions (offline, permissions denied, an empty state, a shared-habit conflict). Format: a numbered checklist of 'Given/When/Then' test cases. Note any acceptance criterion that is not actually testable as written.
```

### Step 6

Run a definition-of-done check. Ask the AI to test a story against your Definition of Done, then apply your own judgement.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Here is our Definition of Done:
<PASTE OR LIST YOUR DEFINITION OF DONE>
and here is a story we think is finished:
<PASTE THE STORY AND WHAT WAS DELIVERED>
Task: check it against each Definition-of-Done item and list what is met, not met or unclear. Do not pass anything you cannot verify from the information given.
```

### Step 7

Save the documentation, communication and testing section of your Tempo-2.0-Playbook folder: the reviewed release notes and templates, the three audience-tailored updates, and the test scenarios and definition-of-done check.

## Test it

You have AI-assisted sprint documentation with invented detail removed and gaps marked '[to confirm]', one update correctly re-pitched for the team, stakeholders and leadership, and test scenarios plus a definition-of-done check generated from your acceptance criteria and reviewed by you — all saved to your playbook.

## Troubleshooting

- **Release notes claim work that was not done.** Re-prompt with 'use only the completed items' and mark anything uncertain '[to confirm]' rather than letting the AI fill the gap.
- **All three audience versions sound the same.** Push the contrast — technical detail for the team, value and dates for stakeholders, three lines for leadership.
- **Test scenarios miss error paths.** Prompt explicitly for offline, permission-denied, empty-state and conflict cases, and note any criterion that is not testable as written.

## Challenge

Generate a test checklist for the smarter-reminder engine and identify one acceptance criterion that is impossible to test as currently written — then fix the criterion.

## Reflection

LO9 — In your own words: Assist documentation, communication, quality and testing across the sprint with AI?

## Deliverable

Keep the documentation, the three audience-tailored updates, and the test scenarios and definition-of-done check — reusable every sprint.

---

*Generative AI for Agile Project Management (C324) · C324 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
