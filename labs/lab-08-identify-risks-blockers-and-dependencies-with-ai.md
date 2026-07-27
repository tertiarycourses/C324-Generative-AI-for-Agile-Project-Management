# Lab 8 — Identify Risks, Blockers and Dependencies with AI

**Topic 03:** AI for Sprints, Standups and Delivery  |  **Day 2**  |  **Approx. 60 min**  |  **Course:** Generative AI for Agile Project Management (C324)

## Scenario

Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project or team is always welcome.

## Goal

Use AI to read the team's notes and backlog and surface likely risks, blockers and dependencies early, map how the work depends on itself and on outside parties, and turn each into a mitigation and escalation the Scrum Master owns.

## What you'll build

A reviewed Tempo 2.0 risk, blocker and dependency log — likely risks and impediments surfaced from the notes, a dependency map with a suggested unblocking sequence, and a mitigation and escalation path with an owner for each real item.

**Tools and techniques:** Any assistant, the sprint notes and backlog, risk and blocker identification, dependency mapping, mitigation and escalation planning, a Scrum-Master review

## Prerequisites

- Completed Lab 7 (you have stand-up summaries and a burndown).
- Your sprint plan and backlog, and Your responsible-AI checklist from Lab 3 open beside you.

## Steps

### Step 1

Gather the evidence: your stand-up summaries and burndown from Lab 7, your sprint plan from Lab 6, and the backlog. Paste the relevant parts into any assistant.

### Step 2

Surface risks and blockers. Use the prompt below to have the AI flag trouble early.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
You are an experienced Scrum Master. Based on this Tempo 2.0 sprint information:
<PASTE STAND-UP SUMMARIES, PLAN AND BACKLOG>
Task: identify the likely risks, blockers and impediments to finishing this sprint — including ones the team has not explicitly named. Format: a table with Risk/Blocker | Why it matters | Likelihood (H/M/L) | Impact (H/M/L). Be specific to this sprint; do not list generic project risks.
```

### Step 3

Map dependencies. Ask the AI to make the dependencies explicit with the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
From the same sprint information, map the dependencies: which stories or tasks depend on another being done first, which depend on another team or an external party (for example an app-store review, a third-party reminder/push service, or a design sign-off), and where a dependency could block the sprint goal. Present as a list of 'A depends on B because…' statements, then suggest an order of work that unblocks things in the right sequence.
```

### Step 4

Sanity-check the AI's read. Go through its risks and dependencies and mark each as real, over-stated or missed. Add at least one risk or dependency you know about from context that the AI did not surface. The AI widens your view; it does not replace it.

### Step 5

Plan mitigations and escalations. For the real risks and blockers, generate options with the prompt below.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
For each of these confirmed risks and blockers:
<PASTE THE CONFIRMED LIST>
suggest one or two practical mitigation options and a clear escalation path (who to raise it to and when). Format: Risk/Blocker | Mitigation | Escalation. Keep the actions concrete and doable within a sprint.
```

### Step 6

Assign owners and decide actions. As the Scrum Master, put a named owner and a next action against each real risk and blocker — the AI proposes, you commit. Remove anything that is noise so the log stays trusted and short.

### Step 7

Save the risk, blocker and dependency log as a section of your Tempo-2.0-Playbook folder: the confirmed items with likelihood/impact, the dependency map and unblocking order, and each item's mitigation, escalation, owner and next action.

## Test it

You have a reviewed Tempo 2.0 risk, blocker and dependency log — likely items surfaced early, a dependency map with a sensible unblocking order, at least one risk you added from your own knowledge, and a mitigation, escalation, owner and next action for every real item — saved to your playbook.

## Troubleshooting

- **The AI lists generic project risks.** Re-prompt to tie every risk to something specific in this sprint's notes, plan or backlog.
- **Dependencies are vague.** Ask for explicit 'A depends on B because…' statements and an unblocking order, not a general discussion.
- **The risk log gets too long to act on.** Cut it to the real, high-likelihood/high-impact items with owners; a log no one reads is worse than none.

## Challenge

Add an external dependency the AI did not consider (for example an app-store review window over a public holiday) and plan its mitigation.

## Reflection

LO8 — In your own words: Identify risks, blockers and dependencies with AI and plan mitigations and escalations?

## Deliverable

Keep the risk, blocker and dependency log with owners and actions — it feeds the status report (Lab 10) and the retrospective (Lab 12).

---

*Generative AI for Agile Project Management (C324) · C324 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
