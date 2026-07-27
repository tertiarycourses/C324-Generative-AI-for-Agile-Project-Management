# Lab 4 — Draft and Refine User Stories and Acceptance Criteria

**Topic 02:** AI for Backlogs, User Stories and Planning  |  **Day 1**  |  **Approx. 52 min**  |  **Course:** Generative AI for Agile Project Management (C324)

## Scenario

Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project or team is always welcome.

## Goal

Turn raw Tempo 2.0 feature ideas into INVEST-quality user stories with AI, then draft and refine testable acceptance criteria, reviewing every one so it reflects the real user and real value.

## What you'll build

A set of INVEST-checked Tempo 2.0 user stories (with over-large ones split) and, for the key stories, testable Given/When/Then acceptance criteria — all reviewed by you and saved as the stories section of your playbook.

**Tools and techniques:** Any assistant, the user-story template from your prompt library, the INVEST checklist, story splitting, Given/When/Then acceptance criteria

## Prerequisites

- Completed Labs 1-3 (toolkit, prompt library and responsible-AI checklist ready).
- Your user-story template from your prompt library, and Your Tempo-2.0-Playbook folder and the supplied Tempo 2.0 project brief (labs/reference-pack/) open.

## Steps

### Step 1

Open the Tempo 2.0 brief and copy the raw feature ideas for the 2.0 release (shared team habits, the smarter reminder engine, the insights dashboard, and the listed bug fixes). Open your agile prompt library and grab your user-story template.

### Step 2

Draft the first batch of stories. Paste the prompt below, filling the context slot with the raw ideas.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
You are an experienced Agile Product Owner for Tempo, a habit-tracking app. Context: here are the raw feature ideas for our 2.0 release:
<PASTE THE RAW FEATURE IDEAS>
Task: write clear user stories in the form 'As a <role>, I want <goal>, so that <benefit>'. Format: group them under the three feature themes (shared team habits, smarter reminders, insights dashboard). Constraints: focus on user value, keep each story to one sentence, and cover the main users (an individual user, a team member, a team admin).
```

### Step 3

Quality-check against INVEST. Ask the AI to grade its own stories and flag the weak ones, using the prompt below, then read its judgement critically.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Review each story above against INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable). Present a table: Story | INVEST issues | Suggested fix. Be strict — flag any story that is too big or vague to estimate in one sprint.
```

### Step 4

Split the over-large stories. Take one story the AI flagged as too big and ask it to split the work into smaller, independently valuable stories.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Split this user story into 2-4 smaller stories that are each independently valuable, small enough to finish in one sprint, and testable. Keep the same 'As a / I want / so that' form:
<PASTE THE OVER-LARGE STORY>
```

### Step 5

Draft acceptance criteria for your key stories. Choose the three most important stories and generate testable criteria with the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
For each of the three user stories below, write acceptance criteria in Given/When/Then form that define exactly when the story is done. Include at least one edge case or error condition per story. Keep each criterion testable and unambiguous.
<PASTE THE THREE KEY STORIES>
```

### Step 6

Review the acceptance criteria as a human. For each story ask: does 'done' really mean done here? Is a realistic edge case missing (offline, permissions, an empty state, a shared-habit conflict)? Add or correct criteria yourself where the AI missed something.

### Step 7

Save the stories section of your playbook: the INVEST-checked stories grouped by theme, the split of the over-large story, and the reviewed Given/When/Then acceptance criteria for the key stories, in your Tempo-2.0-Playbook folder.

## Test it

You have a reviewed set of Tempo 2.0 user stories in proper form, checked against INVEST with at least one over-large story split into smaller ones, and testable Given/When/Then acceptance criteria (including edge cases) for your key stories — all human-reviewed and saved to your playbook.

## Troubleshooting

- **Stories describe a solution, not a need.** Re-prompt to keep the 'so that <benefit>' focused on user value and remove technical how-to wording.
- **Everything comes back as one giant story.** Ask the AI to split against INVEST until each story fits one sprint and is testable.
- **Acceptance criteria miss edge cases.** Prompt explicitly for offline, permissions, empty-state and conflict cases — then add any the AI still misses yourself.

## Challenge

Write acceptance criteria for a tricky shared-habit conflict (two people edit the same team habit at once) and check the AI's criteria actually cover it.

## Reflection

LO4 — In your own words: Draft and refine clear, INVEST-quality user stories and acceptance criteria with AI assistance?

## Deliverable

Keep the INVEST-checked stories and Given/When/Then acceptance criteria — they feed the backlog in Lab 5 and the test scenarios in Lab 9.

---

*Generative AI for Agile Project Management (C324) · C324 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
