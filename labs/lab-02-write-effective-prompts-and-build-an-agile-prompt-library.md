# Lab 2 — Write Effective Prompts and Build an Agile Prompt Library

**Topic 01:** Getting Started with Generative AI for Agile  |  **Day 1**  |  **Approx. 60 min**  |  **Course:** Generative AI for Agile Project Management (C324)

## Scenario

Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project or team is always welcome.

## Goal

Learn the role-context-task-format-constraints structure for agile prompts, refine a weak prompt into a strong one, and save a reusable agile prompt library you will use for the rest of the course.

## What you'll build

A reusable agile prompt library saved in your project folder — structured, slot-based prompt templates for the recurring agile tasks (user stories, backlog grooming, stand-up summary, status report, retrospective) — plus a before/after example proving a structured prompt beats a vague one.

**Tools and techniques:** Any assistant (ChatGPT, Claude or Gemini), the role-context-task-format-constraints prompt structure, single-change prompt edits, a saved slot-based prompt library

## Prerequisites

- Completed Lab 1 (your AI toolkit is set up and tested).
- Your Tempo-2.0-Playbook folder and the supplied Tempo 2.0 project brief (labs/reference-pack/) open.

## Steps

### Step 1

Start with a deliberately weak prompt so you can feel the difference. In any assistant, send: 'Write some user stories for a habit app.' Read the vague, generic result and keep it to compare against.

### Step 2

Now rebuild the same request with structure. Send the prompt below and compare the result with the weak one — notice how much more usable it is.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
You are an experienced Agile Product Owner. Context: we are building Tempo 2.0, a habit-tracking app; a key new feature is shared team habits, where a group tracks a habit together. Task: write three user stories for this feature. Format: use the form 'As a <role>, I want <goal>, so that <benefit>', one per line. Constraints: keep each to one sentence, make them independent, and focus on the user's value, not the technical solution.
```

### Step 3

Change exactly one part and regenerate, so you can attribute the change. First change the ROLE (for example to 'a strict Agile coach who insists on INVEST'); read how the emphasis shifts.

### Step 4

Now change only the FORMAT — ask for the same three stories as a markdown table with columns Role, Goal, Benefit, Priority. Notice format is independent of content.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Re-present exactly those three user stories as a markdown table with the columns: Role | Goal | Benefit | Priority (High/Medium/Low). Do not change the stories' wording.
```

### Step 5

Now change only the CONSTRAINTS — add 'each story must be small enough to finish in one sprint, and add one acceptance criterion per story'. See how constraints tighten quality without you rewriting the whole prompt.

### Step 6

Extract the pattern into a reusable template. Ask the assistant to help, then save the result. Paste the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Turn the effective prompt we just refined into a reusable template with clearly marked slots: [ROLE], [CONTEXT], [TASK], [FORMAT], [CONSTRAINTS]. Then create four more templates in the same slot style for these recurring agile tasks: grooming a backlog, summarising a daily stand-up from raw notes, writing a sprint status report for stakeholders, and running a retrospective. Present all five as a clean, copy-ready prompt library.
```

### Step 7

Review and save. Read each template critically — would it work on a real task? Fix anything weak, then save the five-template set as 'agile-prompt-library' in your Tempo-2.0-Playbook folder. Keep the weak-vs-structured example next to it as a reminder of why structure matters.

## Test it

You have a saved agile prompt library of at least five slot-based templates (user stories, backlog grooming, stand-up summary, status report, retrospective) built on the role-context-task-format-constraints structure, and a before/after example that shows a structured prompt clearly beats a vague one.

## Troubleshooting

- **The structured prompt still gives a generic answer.** Make the context slot more specific to Tempo, and tighten the constraints; vague context is the usual cause.
- **Changing one part changes everything.** Keep role, context, task, format and constraints in separate lines so you can vary one at a time and see its effect.
- **The template has no clear slots.** Ask the assistant to mark every variable part with [SQUARE BRACKETS] so anyone can reuse it without rewriting it.

## Challenge

Add a sixth template of your own for a recurring agile task not covered (for example writing a sprint review agenda) using the same slot structure.

## Reflection

LO2 — In your own words: Write effective, structured prompts for agile tasks and build a reusable prompt library the whole team can use?

## Deliverable

Keep the saved agile prompt library and the weak-vs-structured example — you reuse the templates in almost every remaining lab.

---

*Generative AI for Agile Project Management (C324) · C324 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
