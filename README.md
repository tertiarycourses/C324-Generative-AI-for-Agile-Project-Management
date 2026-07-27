# C324 — Generative AI for Agile Project Management

Run your Agile delivery faster and smarter with AI. This two-day, hands-on course teaches you to use
general-purpose generative AI assistants — **ChatGPT**, **Claude** and **Gemini** — across the entire
Scrum cycle: drafting user stories and acceptance criteria, grooming and prioritising the backlog,
planning sprints and estimating, summarising stand-ups, surfacing risks and dependencies, assisting
documentation and testing, generating status reports and dashboards, analysing velocity, and running
retrospectives — while keeping every decision firmly human.

## Course Information

- **Course Code:** C324
- **Course Title:** Generative AI for Agile Project Management
- **Duration:** 2 days / 15 hours
- **Level:** Beginner–Intermediate
- **Mode:** Instructor-led, hands-on practical labs
- **Course Registration:** [Generative AI for Agile Project Management](https://www.tertiarycourses.com.sg/generative-ai-for-agile-project-management.html)

## One Connected Project

Every lab builds one **connected deliverable** — the **Tempo 2.0 Agile AI Playbook**, for a fictional
habit-tracking app, **Tempo**, from the studio Cadence Labs, planning and delivering its 2.0 release.
You start in Lab 1 by setting up an AI toolkit and prompt library, and across the two days take the
delivery all the way to a retrospective by Lab 12: refined user stories, a groomed and prioritised
backlog, a sprint plan and roadmap, stand-up summaries, a risk and dependency log, AI-assisted docs
and test scenarios, stakeholder reports and a dashboard, a velocity analysis, and a
continuous-improvement plan. Wherever possible you use your **own** non-confidential project; a Tempo
2.0 project brief with sample inputs is supplied in [labs/reference-pack/](labs/reference-pack/) for
everyone to follow along.

There is **no assessment** — this is a commercial short course. Each lab proves itself with an
explicit *Test it* verification step instead.

## What You'll Learn

| Topic | Coverage |
|---|---|
| 01 — Getting Started with Generative AI for Agile | Introduction to Agile, Scrum & generative AI · setting up AI tools for agile PM · effective prompting for agile tasks · responsible & human-in-the-loop use of AI |
| 02 — AI for Backlogs, User Stories and Planning | Drafting & refining user stories and acceptance criteria · grooming & prioritising the backlog · sprint planning & estimation support · generating roadmaps & release plans |
| 03 — AI for Sprints, Standups and Delivery | Summarising stand-ups & tracking progress · identifying risks, blockers & dependencies · assisting documentation & communication · supporting quality, testing & delivery |
| 04 — AI for Reporting, Retrospectives and Improvement | Generating status reports & dashboards · analysing velocity & metrics · running AI-assisted retrospectives · driving continuous improvement |

## Labs

Twelve connected hands-on labs (3 per topic, 6 per day). See [labs/README.md](labs/README.md) for the
index, [labs/tools.md](labs/tools.md) for the accounts and tools used, and
[labs/reference-pack/](labs/reference-pack/) for the Tempo 2.0 project brief and sample inputs.

## Courseware

Built artifacts live in [`courseware/`](courseware/):

- Trainer slide deck — `Generative AI for Agile Project Management (C324)-v1.0.pptx` (+ PDF)
- Learner Guide — `LG-*.docx` (+ PDF); the Markdown mirror is at the repo root
- Lesson Plan — `LP-*.docx` (+ PDF)

## Building the Courseware

Everything is generated from a single source (`course_data.py` + `data_domainN.py`) so the deck,
Lesson Plan, Learner Guide and labs stay 100% aligned:

```bash
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
```

## Non-WSQ

This is a **non-WSQ** commercial short course. It carries **no** WSQ, SSG/SkillsFuture, TRAQOM,
digital-attendance, funding/subsidy or assessment content — those are deliberately excluded.

---

© 2026 Tertiary Infotech Academy Pte Ltd · UEN 201200696W
