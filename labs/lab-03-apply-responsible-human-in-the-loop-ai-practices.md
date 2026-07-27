# Lab 3 — Apply Responsible, Human-in-the-Loop AI Practices

**Topic 01:** Getting Started with Generative AI for Agile  |  **Day 1**  |  **Approx. 60 min**  |  **Course:** Generative AI for Agile Project Management (C324)

## Scenario

Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, non-confidential project of your own; your own project or team is always welcome.

## Goal

Build a responsible-AI checklist for agile work and apply it — catching an invented 'fact', rewriting a prompt to protect sensitive data, and confirming a draft is fair, clear and owned by a human.

## What you'll build

A one-page responsible-AI checklist for agile work (fact-check, protect data, be fair and clear, disclose AI use, keep a human owner) plus worked examples — a caught-and-corrected hallucination and a risky prompt rewritten to remove sensitive data.

**Tools and techniques:** Any assistant, fact-checking against the brief, data-safety rewriting, a fairness and clarity review, a transparency and ownership decision

## Prerequisites

- Completed Lab 2 (you have a prompt library to apply the checklist to).
- Your Tempo-2.0-Playbook folder and the supplied Tempo 2.0 project brief (labs/reference-pack/) open.

## Steps

### Step 1

See a hallucination for yourself. Ask an assistant a specific, checkable question it is likely to get wrong or invent, for example the prompt below. Read how confident the answer sounds.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
According to the official Scrum Guide, exactly how many minutes long must a daily stand-up be, and on which page is that stated? Give the exact page number.
```

### Step 2

Fact-check it. The Scrum Guide time-boxes the daily stand-up to 15 minutes but does not mandate an exact length by page number — so any confident 'page number' is invented. Note this as your first checklist rule: verify specific facts, figures and citations before you trust them.

### Step 3

Practise data safety. Look at this risky prompt a busy Scrum Master might send: 'Here is our customer list with emails and phone numbers <pasted>, and our AWS admin password is <pasted> — write release notes.' Identify everything in it that must never go into a public assistant.

### Step 4

Rewrite it safely. Redraft the same request so it gets the job done with no sensitive data, using the prompt below as your safe version.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
You are a release manager. Write concise release notes for a mobile app update that adds shared team habits, a smarter reminder engine and an insights dashboard, and fixes several reminder-reliability bugs. Use only this description — do not ask for or include any customer data, personal information or credentials. Format: a short 'New', 'Improved' and 'Fixed' list.
```

### Step 5

Check for fairness and clarity. Take any draft the AI has written for you so far and ask it to review itself with the prompt below; then read its answer critically — you, not the AI, are the judge.

Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):

```text
Review the text above for clarity and fairness: is anything ambiguous, biased, exclusionary or likely to be misread by a non-technical stakeholder? List specific issues and suggest plain, neutral rewrites. Do not change the meaning.
```

### Step 6

Decide on transparency and ownership. Write one line on how your team will note when something was AI-assisted (for example a small 'AI-assisted, reviewed by <name>' tag on drafts), and confirm the rule that a named human owns and approves every output before it is used.

### Step 7

Assemble your responsible-AI checklist. Combine what you practised into a short, reusable checklist — fact-check specifics; never paste sensitive data; review for fairness and clarity; disclose AI assistance; a human owns and approves — and save it as 'responsible-ai-checklist' in your Tempo-2.0-Playbook. Keep it open beside you for every remaining lab.

## Test it

You have a saved one-page responsible-AI checklist, and you have applied it in practice: you caught and corrected an invented 'fact', you identified and removed sensitive data by rewriting a risky prompt safely, and you reviewed a draft for fairness, clarity, disclosure and human ownership.

## Troubleshooting

- **The assistant refuses to invent a fake fact.** Good — but many still will; if it does not, ask a different obscure specific question and fact-check whatever it returns.
- **Unsure what counts as sensitive data.** Treat anything that identifies a real person, a customer, a credential or proprietary code as off-limits for a public assistant — when in doubt, leave it out.
- **The fairness review feels subjective.** It is — that is why a human owns the call; use the AI's list as prompts to think, not as verdicts.

## Challenge

Take a real prompt you might genuinely send at work and rewrite it to be data-safe, proving the checklist works on your own material.

## Reflection

LO3 — In your own words: Apply responsible, human-in-the-loop AI practices — reviewing, fact-checking and protecting sensitive data — across agile work?

## Deliverable

Keep your one-page responsible-AI checklist open beside you for every remaining lab — it is the discipline that makes all the AI use safe.

---

*Generative AI for Agile Project Management (C324) · C324 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
