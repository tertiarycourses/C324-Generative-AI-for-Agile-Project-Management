#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate the labs/ markdown from the SAME single source as the deck/LP/LG
(course_data.py + data_domainN.py), so labs stay 100% aligned with the other
artifacts. Emits labs/lab-NN-*.md and labs/README.md. tools.md and the
reference-pack are hand-authored. Enrichment sections (Prerequisites,
Troubleshooting, Challenge, Reflection, Deliverable) live in the ENRICH table
below, keyed by lab number. Day and approx-minutes for each lab are derived from
course_data.SCHEDULE so the labs match the Lesson Plan exactly.

Run:  python gen_labs.py
"""
import os, re, sys, glob, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C


def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))


REPO = find_repo(HERE)
LABS = os.path.join(REPO, "labs")

# ------------------------------------------------------------------ load labs
DOMS = []
for f in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
    mod = importlib.import_module(os.path.splitext(os.path.basename(f))[0])
    key = [k for k in dir(mod) if k.startswith("DOMAIN")][0]
    DOMS.append((getattr(mod, key), getattr(mod, "SCENARIO", None)))

LABSLIST = []
SCENARIO = None
for dom, scen in DOMS:
    if scen and not SCENARIO:
        SCENARIO = scen
    LABSLIST.extend(dom)

TOPIC_TITLE = {t["num"]: t["title"] for t in C.TOPICS}

# ------------------------------------------------------------------ per-lab day + minutes
# Derived from the schedule lab blocks so the labs match the Lesson Plan.
def _sched():
    return C.SCHEDULE(lambda nums: "\x00".join(str(n) for n in nums)) \
        if callable(getattr(C, "SCHEDULE", None)) else getattr(C, "SCHEDULE", {})


def approx_minutes():
    mins = {}
    for _day, (_theme, rows) in _sched().items():
        for row in rows:
            if row[3] == "lab":
                nums = [int(x) for x in row[4].split("Hands-on: ")[-1].split("\x00")]
                per = round(row[2] / len(nums))
                for n in nums:
                    mins[n] = per
    return mins


def lab_days():
    days = {}
    for day, (_theme, rows) in _sched().items():
        for row in rows:
            if row[3] == "lab":
                nums = [int(x) for x in row[4].split("Hands-on: ")[-1].split("\x00")]
                for n in nums:
                    days[n] = day
    return days


MINS = approx_minutes()
DAYS = lab_days()

# ------------------------------------------------------------------ per-lab enrichment
_PRE_TOOLKIT = "Your AI toolkit ready — signed in to ChatGPT, Claude or Gemini in a browser."
_PRE_PLAYBOOK = "Your Tempo-2.0-Playbook folder and the supplied Tempo 2.0 project brief (labs/reference-pack/) open."
_PRE_RESP = "Your responsible-AI checklist from Lab 3 open beside you."

ENRICH = {
 1: dict(
    prereqs=[
        "A laptop with a modern browser and a reliable internet connection — every AI feature runs in the cloud.",
        "An account for at least one of ChatGPT (chat.openai.com), Claude (claude.ai) or Gemini (gemini.google.com); a free account for each is enough.",
        "The supplied Tempo 2.0 project brief (labs/reference-pack/) to hand.",
    ],
    trouble=[
        "**An assistant asks you to sign in or hits a usage limit.** Sign in with a free account; if one tool is rate-limited, switch to another — the labs work with any of the three.",
        "**The three tools give quite different answers.** That is expected and is the point of the lab — the prompt and your review matter more than which tool you use.",
        "**The summary added something not in the brief.** Good — you have just seen a hallucination. Note it and correct it; this is the review habit every later lab relies on.",
    ],
    challenge="Give all three assistants a slightly harder Tempo task (for example 'suggest three risks in adding shared team habits') and note which gave the most useful, specific answer — and why.",
    deliverable="Keep your 'how I'll work' note and the tool-comparison note in your Tempo-2.0-Playbook — they open the playbook and set the prompt-review-own habit for every later lab.",
 ),
 2: dict(
    prereqs=[
        "Completed Lab 1 (your AI toolkit is set up and tested).",
        _PRE_PLAYBOOK,
    ],
    trouble=[
        "**The structured prompt still gives a generic answer.** Make the context slot more specific to Tempo, and tighten the constraints; vague context is the usual cause.",
        "**Changing one part changes everything.** Keep role, context, task, format and constraints in separate lines so you can vary one at a time and see its effect.",
        "**The template has no clear slots.** Ask the assistant to mark every variable part with [SQUARE BRACKETS] so anyone can reuse it without rewriting it.",
    ],
    challenge="Add a sixth template of your own for a recurring agile task not covered (for example writing a sprint review agenda) using the same slot structure.",
    deliverable="Keep the saved agile prompt library and the weak-vs-structured example — you reuse the templates in almost every remaining lab.",
 ),
 3: dict(
    prereqs=[
        "Completed Lab 2 (you have a prompt library to apply the checklist to).",
        _PRE_PLAYBOOK,
    ],
    trouble=[
        "**The assistant refuses to invent a fake fact.** Good — but many still will; if it does not, ask a different obscure specific question and fact-check whatever it returns.",
        "**Unsure what counts as sensitive data.** Treat anything that identifies a real person, a customer, a credential or proprietary code as off-limits for a public assistant — when in doubt, leave it out.",
        "**The fairness review feels subjective.** It is — that is why a human owns the call; use the AI's list as prompts to think, not as verdicts.",
    ],
    challenge="Take a real prompt you might genuinely send at work and rewrite it to be data-safe, proving the checklist works on your own material.",
    deliverable="Keep your one-page responsible-AI checklist open beside you for every remaining lab — it is the discipline that makes all the AI use safe.",
 ),
 4: dict(
    prereqs=[
        "Completed Labs 1-3 (toolkit, prompt library and responsible-AI checklist ready).",
        "Your user-story template from your prompt library, and " + _PRE_PLAYBOOK,
    ],
    trouble=[
        "**Stories describe a solution, not a need.** Re-prompt to keep the 'so that <benefit>' focused on user value and remove technical how-to wording.",
        "**Everything comes back as one giant story.** Ask the AI to split against INVEST until each story fits one sprint and is testable.",
        "**Acceptance criteria miss edge cases.** Prompt explicitly for offline, permissions, empty-state and conflict cases — then add any the AI still misses yourself.",
    ],
    challenge="Write acceptance criteria for a tricky shared-habit conflict (two people edit the same team habit at once) and check the AI's criteria actually cover it.",
    deliverable="Keep the INVEST-checked stories and Given/When/Then acceptance criteria — they feed the backlog in Lab 5 and the test scenarios in Lab 9.",
 ),
 5: dict(
    prereqs=[
        "Completed Lab 4 (you have user stories to backlog).",
        "The backlog-grooming template from your prompt library, and " + _PRE_RESP,
    ],
    trouble=[
        "**The AI silently dropped or invented items.** Always diff the groomed list against your raw list; re-prompt with 'do not add or remove items, only clarify, split or merge'.",
        "**Everything is a 'Must have'.** Force trade-offs: tell the AI only a set fraction can be Must, tied to the release goal, so priority means something.",
        "**Value/effort ratings feel arbitrary.** They are a starting point — adjust them with what you know about the team and the product; you own the final order.",
    ],
    challenge="Ask the AI to identify the single item you should drop entirely from the release, and decide whether you agree — practising the Product Owner's hardest call.",
    deliverable="Keep the groomed, MoSCoW- and value/effort-tagged, ordered backlog with your override notes — it is the input to sprint planning in Lab 6.",
 ),
 6: dict(
    prereqs=[
        "Completed Lab 5 (you have a prioritised backlog).",
        "The team capacity from the brief, and " + _PRE_PLAYBOOK,
    ],
    trouble=[
        "**The AI over-commits the sprint.** Give it the real capacity and tell it to leave slack for the unknown; a plausible-looking full sprint is usually over-full.",
        "**Estimates come with no reasoning.** Insist every story point is accompanied by its assumption and main risk — the reasoning is worth more than the number.",
        "**The roadmap ignores dependencies.** Feed it your Lab 5 ordering and ask it to make every cross-item and external dependency explicit, then sequence around them.",
    ],
    challenge="Re-run the sprint plan assuming one developer is on leave for half the sprint, and see how the AI (and you) re-scope the goal.",
    deliverable="Keep the Sprint 1 plan, the estimates with assumptions, and the roadmap and release plan — Day 1's deliverable and the basis for the running sprint on Day 2.",
 ),
 7: dict(
    prereqs=[
        "Completed Day 1 (you have a planned sprint and a prioritised backlog).",
        "The supplied raw stand-up notes (labs/reference-pack/), your stand-up template, and " + _PRE_RESP,
    ],
    trouble=[
        "**A blocker got buried in the summary.** Prompt the AI to always list blockers separately and never merge them into general progress.",
        "**The summary invented progress.** It can only use the notes given — re-prompt with 'use only what the notes say' and correct anything not supported.",
        "**The burndown read feels too rosy.** Compare it with your own sense of the sprint and rewrite it honestly; an optimistic burndown helps no one.",
    ],
    challenge="Feed the AI a deliberately contradictory day of notes (one person says done, another says blocked on the same item) and see whether it flags the conflict — then resolve it yourself.",
    deliverable="Keep the stand-up summary, progress-against-goal update and burndown narrative — they feed the risk log (Lab 8) and the status report (Lab 10).",
 ),
 8: dict(
    prereqs=[
        "Completed Lab 7 (you have stand-up summaries and a burndown).",
        "Your sprint plan and backlog, and " + _PRE_RESP,
    ],
    trouble=[
        "**The AI lists generic project risks.** Re-prompt to tie every risk to something specific in this sprint's notes, plan or backlog.",
        "**Dependencies are vague.** Ask for explicit 'A depends on B because…' statements and an unblocking order, not a general discussion.",
        "**The risk log gets too long to act on.** Cut it to the real, high-likelihood/high-impact items with owners; a log no one reads is worse than none.",
    ],
    challenge="Add an external dependency the AI did not consider (for example an app-store review window over a public holiday) and plan its mitigation.",
    deliverable="Keep the risk, blocker and dependency log with owners and actions — it feeds the status report (Lab 10) and the retrospective (Lab 12).",
 ),
 9: dict(
    prereqs=[
        "Completed Lab 4 (you have acceptance criteria to test against) and Lab 7 (you have an update to re-pitch).",
        "Your Definition of Done, and " + _PRE_RESP,
    ],
    trouble=[
        "**Release notes claim work that was not done.** Re-prompt with 'use only the completed items' and mark anything uncertain '[to confirm]' rather than letting the AI fill the gap.",
        "**All three audience versions sound the same.** Push the contrast — technical detail for the team, value and dates for stakeholders, three lines for leadership.",
        "**Test scenarios miss error paths.** Prompt explicitly for offline, permission-denied, empty-state and conflict cases, and note any criterion that is not testable as written.",
    ],
    challenge="Generate a test checklist for the smarter-reminder engine and identify one acceptance criterion that is impossible to test as currently written — then fix the criterion.",
    deliverable="Keep the documentation, the three audience-tailored updates, and the test scenarios and definition-of-done check — reusable every sprint.",
 ),
 10: dict(
    prereqs=[
        "Completed Labs 7-8 (you have progress, burndown and a risk log).",
        "Your status-report template, your real sprint data, and " + _PRE_RESP,
    ],
    trouble=[
        "**The report overstates progress.** Fact-check every number and claim against your real data and rewrite honestly; a report the team cannot stand behind destroys trust.",
        "**The dashboard is cluttered with vanity metrics.** Cut to the few that drive decisions (goal status, scope, burndown, velocity, top risks) and say what each does not tell you.",
        "**The leadership summary is too long.** Force it to three lines — headline, risk, ask — nothing more.",
    ],
    challenge="Write the status report twice — once for a sprint that went well and once for one that slipped — and check both stay equally honest and clear.",
    deliverable="Keep the status report, leadership summary, dashboard design and metrics narrative — the reporting section of your playbook.",
 ),
 11: dict(
    prereqs=[
        "Completed Lab 10 (you have reported this sprint).",
        "The supplied sprint metrics history (labs/reference-pack/), and " + _PRE_RESP,
    ],
    trouble=[
        "**The AI claims a strong trend from little data.** Tell it to state when the data is too small to be reliable and to avoid over-confident trends.",
        "**The average velocity looks wrong.** Recompute it yourself from the raw numbers — never report a metric you have not verified.",
        "**Metrics get framed as targets.** Re-prompt to treat every metric as a signal for conversation, and to warn against gaming or using it to pressure individuals.",
    ],
    challenge="Ask the AI to identify which single metric would most mislead a stakeholder if shown alone, and write one line on how you would present it responsibly instead.",
    deliverable="Keep the velocity-trend read, scope forecast and signals interpretation with your own commentary — it feeds the retrospective in Lab 12.",
 ),
 12: dict(
    prereqs=[
        "Completed Labs 7-11 (you have tracking, risks, reports and metrics to reflect on).",
        "The supplied anonymised retro input (labs/reference-pack/), and " + _PRE_RESP,
    ],
    trouble=[
        "**The themes name or imply individuals.** Re-prompt to keep it anonymous, neutral and about the system, not people; strip any name before you paste input.",
        "**The action list is too long to do.** Cut to 3-4 specific, owned, time-bound actions — a long improvement list improves nothing.",
        "**Actions are vague ('communicate better').** Force each to be specific, measurable and owned, with a 'done by when' the team can actually check next sprint.",
    ],
    challenge="Design how you would carry these actions into next sprint's retrospective so you can prove what actually changed — closing the continuous-improvement loop.",
    deliverable="Keep the retrospective format, themed feedback, discussion points and improvement-action tracker — and your complete, reviewed Tempo 2.0 Agile AI Playbook. This is the end-to-end deliverable the course set out to build.",
 ),
}


def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(s) > 60:
        s = s[:60].rstrip("-")
    return s


def steps_md(steps):
    out = []
    for i, (instr, cmd) in enumerate(steps, 1):
        out.append(f"### Step {i}\n\n{instr}")
        if cmd:
            out.append("Prompt to use (paste into ChatGPT, Claude or Gemini — adapt the bracketed parts):\n\n```text\n" + cmd + "\n```")
    return "\n\n".join(out)


def lab_filename(lab):
    return f"lab-{lab['num']:02d}-{slug(lab['title'])}.md"


def build_lab(lab):
    e = ENRICH[lab["num"]]
    topic = lab["topic"]
    mins = MINS.get(lab["num"], 45)
    day = DAYS.get(lab["num"], 1)
    parts = []
    parts.append(f"# Lab {lab['num']} — {lab['title']}\n")
    parts.append(
        f"**Topic 0{topic}:** {TOPIC_TITLE[topic]}  |  **Day {day}**  |  "
        f"**Approx. {mins} min**  |  **Course:** {C.TITLE}\n"
    )
    if SCENARIO:
        parts.append("## Scenario\n\n" + SCENARIO + "\n")
    parts.append("## Goal\n\n" + lab["objective"] + "\n")
    parts.append("## What you'll build\n\n" + lab["build"] + "\n")
    parts.append("**Tools and techniques:** " + lab["services"] + "\n")
    parts.append("## Prerequisites\n\n" + "\n".join("- " + p for p in e["prereqs"]) + "\n")
    parts.append("## Steps\n\n" + steps_md(lab["steps"]) + "\n")
    parts.append("## Test it\n\n" + lab["test"] + "\n")
    parts.append("## Troubleshooting\n\n" + "\n".join("- " + t for t in e["trouble"]) + "\n")
    parts.append("## Challenge\n\n" + e["challenge"] + "\n")
    lo = C.LEARNING_OUTCOMES[lab["num"] - 1]
    lo_text = lo.split(":", 1)[1].strip().rstrip(".")
    parts.append(f"## Reflection\n\nLO{lab['num']} — In your own words: {lo_text}?\n")
    parts.append("## Deliverable\n\n" + e["deliverable"] + "\n")
    parts.append("---\n")
    parts.append(
        f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*"
    )
    return "\n".join(parts) + "\n"


def build_readme(files):
    rows = []
    for lab in LABSLIST:
        fn = files[lab["num"]]
        day = DAYS.get(lab["num"], 1)
        rows.append(
            f"| {day} | 0{lab['topic']} | {lab['num']:02d} | [{lab['title']}]({fn}) |"
        )
    md = []
    md.append(f"# Labs — {C.TITLE}\n")
    md.append(f"**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**\n")
    md.append(
        "All 12 labs build one connected **Tempo 2.0 Agile AI Playbook**, which you begin in Lab 1 and finish "
        "in Lab 12 — from setting up ChatGPT, Claude and Gemini as an agile toolkit and prompt library, through "
        "user stories, a groomed and prioritised backlog, a sprint plan and roadmap, stand-up summaries, a risk "
        "and dependency log, AI-assisted docs and testing, status reports and a dashboard, a velocity analysis, "
        "and an AI-assisted retrospective and continuous-improvement plan. A Tempo 2.0 project brief with sample "
        "inputs is supplied in `reference-pack/`; use your own non-confidential project wherever you prefer. "
        "There is **no assessment** — each lab verifies itself with a 'Test it' step.\n"
    )
    md.append("| Day | Topic | Lab | Title |")
    md.append("|---:|---|---:|---|")
    md.extend(rows)
    md.append("")
    md.append("## Tools\n")
    md.append("See [tools.md](tools.md) for the accounts and tools used across the labs, and "
              "[reference-pack/](reference-pack/) for the Tempo 2.0 project brief and sample inputs.")
    return "\n".join(md) + "\n"


def main():
    os.makedirs(LABS, exist_ok=True)
    # remove stale lab-*.md so renamed labs don't linger
    for old in glob.glob(os.path.join(LABS, "lab-*.md")):
        os.remove(old)
    files = {}
    for lab in LABSLIST:
        fn = lab_filename(lab)
        files[lab["num"]] = fn
        with open(os.path.join(LABS, fn), "w", encoding="utf-8") as fh:
            fh.write(build_lab(lab))
        print("wrote labs/" + fn)
    with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(build_readme(files))
    print("wrote labs/README.md")


if __name__ == "__main__":
    main()
