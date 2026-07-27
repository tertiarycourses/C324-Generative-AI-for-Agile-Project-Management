# Lab 5 — Groom and Prioritise the Product Backlog with AI

**Topic 02:** AI for Backlogs, User Stories and Planning  |  **Day 1**  |  **Approx. 52 min**  |  **Course:** Generative AI for Agile Project Management (C324)

## Scenario

Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project or team is always welcome.

## Goal

Use AI to groom a messy raw backlog — clarifying, splitting, merging and de-duplicating items — then prioritise it with MoSCoW and value-versus-effort, keeping the final ordering a human decision.

## What you'll build

A groomed, prioritised Tempo 2.0 product backlog — cleaned and de-duplicated, each item tagged with a MoSCoW category and a value/effort view, ordered for planning, with your Product-Owner adjustments applied.

**Tools and techniques:** Any assistant, the backlog-grooming template from your prompt library, MoSCoW prioritisation, value-versus-effort analysis, Product-Owner review

## Prerequisites

- Completed Lab 4 (you have user stories to backlog).
- The backlog-grooming template from your prompt library, and Your responsible-AI checklist from Lab 3 open beside you.

## Steps

### Step 1

Assemble your raw backlog: your Lab 4 stories plus any remaining raw ideas and bug fixes from the Tempo 2.0 brief that are not yet stories. Paste them into any assistant as one messy list so you can groom it.

### Step 2

Groom the list. Use the prompt below to clarify, split, merge and de-duplicate.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
You are helping a Product Owner groom a product backlog. Here is our raw Tempo 2.0 backlog:
<PASTE THE RAW BACKLOG>
Task: return a cleaned, ready backlog. Clarify any vague item, split any item that is really several, merge duplicates, and flag anything missing important detail. Present it as a numbered list with a one-line description per item. Do not invent new features that are not implied by the list.
```

### Step 3

Review the grooming. Check the AI did not quietly drop or invent items. Confirm each split and merge makes sense to you; undo any you disagree with. Grooming is a judgement call, not an automatic one.

### Step 4

Prioritise with MoSCoW. Ask the AI to categorise and explain, using the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Prioritise the groomed backlog using MoSCoW (Must have, Should have, Could have, Won't have this release). For the Tempo 2.0 release, our goal is to ship shared team habits and reliable reminders first. Present a table: Item | MoSCoW | One-line reason. Then list the 'Must have' items in the order you would build them and explain the ordering.
```

### Step 5

Add a value-versus-effort view. Ask the AI to estimate relative value and effort so you can spot quick wins and expensive extras.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
For each backlog item, add a rough Value (High/Medium/Low) and Effort (High/Medium/Low) rating and mark any that are High-value / Low-effort as 'quick win'. Present as a table and briefly note which items look like poor value for their effort.
```

### Step 6

Make the Product Owner's call. Reconcile MoSCoW and value/effort into one ordered backlog. Move at least two items yourself against the AI's suggestion where you disagree, and write one line explaining each override — this is the human decision the AI supports but does not make.

### Step 7

Save the prioritised backlog section of your playbook: the groomed items, their MoSCoW and value/effort tags, the final ordering, and your override notes, in your Tempo-2.0-Playbook folder.

## Test it

You have a groomed, de-duplicated Tempo 2.0 backlog with every item tagged by MoSCoW and value/effort, ordered ready for planning, and you have made at least two Product-Owner overrides against the AI's suggestion with reasons — a backlog you own, not one the AI decided.

## Troubleshooting

- **The AI silently dropped or invented items.** Always diff the groomed list against your raw list; re-prompt with 'do not add or remove items, only clarify, split or merge'.
- **Everything is a 'Must have'.** Force trade-offs: tell the AI only a set fraction can be Must, tied to the release goal, so priority means something.
- **Value/effort ratings feel arbitrary.** They are a starting point — adjust them with what you know about the team and the product; you own the final order.

## Challenge

Ask the AI to identify the single item you should drop entirely from the release, and decide whether you agree — practising the Product Owner's hardest call.

## Reflection

LO5 — In your own words: Groom and prioritise a product backlog with AI using INVEST, MoSCoW and value-versus-effort thinking?

## Deliverable

Keep the groomed, MoSCoW- and value/effort-tagged, ordered backlog with your override notes — it is the input to sprint planning in Lab 6.

---

*Generative AI for Agile Project Management (C324) · C324 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
