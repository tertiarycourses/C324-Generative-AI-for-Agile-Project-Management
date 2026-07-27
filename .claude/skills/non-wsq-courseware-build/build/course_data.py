"""
SINGLE SOURCE OF TRUTH — C324 Generative AI for Agile Project Management (non-WSQ).

A hands-on, two-day course on using general-purpose generative AI assistants
(ChatGPT, Claude and Gemini) to run an Agile/Scrum delivery end to end — from
setting up an AI toolkit and prompt library, through drafting user stories,
grooming and prioritising the backlog, planning sprints and estimating, running
stand-ups and tracking progress, surfacing risks and dependencies, assisting
documentation, testing and communication, to generating status reports,
analysing velocity, running retrospectives and driving continuous improvement.
Every artifact (PPT, LP, LG, LG.md) and every lab is generated from this module
+ data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C324.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Generative AI for Agile Project Management (C324)"
SHORT_TITLE  = "Generative AI for Agile Project Management (C324)"   # used in output filenames
COURSE_CODE  = "C324"                                                # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain how generative AI assistants (ChatGPT, Claude, Gemini) support Agile and Scrum, and set up an AI toolkit and workspace for agile project management.",
    "LO2: Write effective, structured prompts for agile tasks and build a reusable prompt library the whole team can use.",
    "LO3: Apply responsible, human-in-the-loop AI practices — reviewing, fact-checking and protecting sensitive data — across agile work.",
    "LO4: Draft and refine clear, INVEST-quality user stories and acceptance criteria with AI assistance.",
    "LO5: Groom and prioritise a product backlog with AI using INVEST, MoSCoW and value-versus-effort thinking.",
    "LO6: Plan a sprint, estimate work, and generate a release roadmap and plan with AI support.",
    "LO7: Summarise stand-ups and track sprint progress with AI while keeping the team's judgement in the loop.",
    "LO8: Identify risks, blockers and dependencies with AI and plan mitigations and escalations.",
    "LO9: Assist documentation, communication, quality and testing across the sprint with AI.",
    "LO10: Generate status reports and a delivery dashboard for different stakeholders with AI.",
    "LO11: Analyse velocity and delivery metrics with AI to surface trends and honest insights.",
    "LO12: Run an AI-assisted retrospective and turn its output into a concrete continuous-improvement plan.",
]
LO_TITLES = [
    "AI toolkit for Agile",
    "Prompting for agile",
    "Responsible AI",
    "User stories & AC",
    "Backlog & priorities",
    "Sprint plan & roadmap",
    "Standups & tracking",
    "Risks & blockers",
    "Docs, comms & QA",
    "Reports & dashboards",
    "Velocity & metrics",
    "Retro & improvement",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with Generative AI for Agile",
         subtitle="Introduction to Agile, Scrum and generative AI · Setting up AI tools for agile project management · Effective prompting for agile tasks · Responsible and human-in-the-loop use of AI",
         weighting="25%",
         concepts=[
            "Agile and Scrum in one view — Agile is a way of delivering value in small, inspect-and-adapt increments; Scrum is the most common framework, with roles (Product Owner, Scrum Master, Developers), events (sprint planning, daily stand-up, review, retrospective) and artifacts (product backlog, sprint backlog, increment).",
            "Where generative AI fits — a generative AI assistant is a drafting, summarising and analysis partner across the whole Scrum cycle; it speeds up the writing and thinking work (stories, plans, summaries, reports) so the team spends more time on judgement, collaboration and delivery.",
            "The three assistants — ChatGPT, Claude and Gemini are general-purpose chat assistants that all take a text prompt and return a draft; they differ in interface, context length and integrations, but the prompting and review skills you learn here transfer across all three.",
            "AI is a co-pilot, not the pilot — the AI drafts and suggests; the Product Owner, Scrum Master and team still own every decision, estimate and commitment. Nothing goes into the backlog, plan or report without a human reviewing it.",
            "Setting up your AI workspace — you sign in to an assistant, learn to start a focused chat per task, paste in the relevant context (the project brief, backlog, notes), and keep your AI work organised alongside your agile tooling.",
            "Prompting is the core skill — a good agile prompt gives the AI a role, the context, the exact task, the format you want back and any constraints; a vague ask gives a vague draft, a structured ask gives a usable one.",
            "A reusable prompt library — the same agile tasks recur every sprint (write stories, groom the backlog, summarise the stand-up, draft the report), so you save your best prompts as reusable templates the whole team can run.",
            "Human-in-the-loop review — every AI output is a first draft to be checked: is it accurate, does it fit our context, is anything invented (a 'hallucination'), is it fair and clear? You review, correct and own the result.",
            "Responsible and safe use — you avoid pasting confidential customer data, credentials or personal information into a public assistant, you check the facts and figures the AI states, and you are transparent with the team about what was AI-assisted.",
         ]),
    dict(num=2, code="02",
         title="AI for Backlogs, User Stories and Planning",
         subtitle="Drafting and refining user stories and acceptance criteria · Grooming and prioritising the backlog with AI · Sprint planning and estimation support · Generating roadmaps and release plans",
         weighting="25%",
         concepts=[
            "User stories with AI — the AI turns a rough feature idea into a well-formed user story in the 'As a <role>, I want <goal>, so that <benefit>' form, and you refine it so it reflects the real user and real value.",
            "INVEST-quality stories — good stories are Independent, Negotiable, Valuable, Estimable, Small and Testable; you prompt the AI to draft against INVEST and to flag stories that are too big or vague to estimate.",
            "Acceptance criteria — the AI drafts clear, testable acceptance criteria (often in Given/When/Then form) that define 'done' for a story, which you then check for gaps, edge cases and testability.",
            "Grooming the backlog — the AI helps refine, split, merge and de-duplicate backlog items, clarify wording and add missing detail, turning a messy raw list into a groomed, ready backlog.",
            "Prioritising with AI — the AI applies frameworks such as MoSCoW (Must / Should / Could / Won't) and value-versus-effort to suggest a priority order and explain its reasoning; the Product Owner makes the final call.",
            "Sprint planning support — given the team's capacity and the top of the backlog, the AI proposes a realistic sprint goal and a candidate sprint backlog, and helps break stories into tasks.",
            "Estimation support — the AI suggests relative story-point estimates and surfaces the assumptions and risks behind each, giving the team a sensible starting point for planning-poker discussion rather than a number to accept blindly.",
            "Roadmaps and release plans — the AI drafts a multi-sprint roadmap and a release plan from the prioritised backlog, grouping work into themes and releases and making dependencies and milestones explicit.",
            "Keeping ownership — AI accelerates the drafting, but the team still negotiates scope, commits to the sprint and owns the estimates; the AI's numbers are inputs to the conversation, never the decision.",
         ]),
    dict(num=3, code="03",
         title="AI for Sprints, Standups and Delivery",
         subtitle="Summarising stand-ups and tracking progress · Identifying risks, blockers and dependencies with AI · Assisting documentation and communication · Supporting quality, testing and delivery",
         weighting="25%",
         concepts=[
            "Summarising stand-ups — the AI turns raw daily-stand-up notes into a clear summary of what was done, what is planned and what is blocked, so the team and stakeholders get a consistent update without extra writing.",
            "Tracking progress — from stand-up notes and board status, the AI helps describe sprint progress against the goal, highlight what has moved and what is stuck, and draft a plain-language burndown narrative.",
            "Surfacing risks and blockers — the AI reads the team's notes and backlog and flags likely risks, blockers and impediments early, so the Scrum Master can act before they derail the sprint.",
            "Mapping dependencies — the AI identifies dependencies between stories, teams and external parties, and helps sequence work so blocked items are unblocked in the right order.",
            "Mitigation and escalation — for each risk or blocker the AI suggests mitigation options and a clear escalation path, which the Scrum Master reviews and turns into real actions and owners.",
            "Assisting documentation — the AI drafts the routine sprint documentation (definition of done notes, decision logs, release notes, meeting minutes) so it is written consistently and kept up to date with far less effort.",
            "Assisting communication — the AI tailors the same update for different audiences — a technical note for the team, a plain summary for stakeholders, a short message for leadership — keeping tone and detail appropriate to each.",
            "Supporting quality and testing — the AI drafts test scenarios and checklists from acceptance criteria, suggests edge cases, and helps review whether a story truly meets its definition of done.",
            "Human judgement in delivery — the AI drafts and flags, but the Scrum Master and team validate every risk, dependency and test; the AI widens what you notice, it does not replace the team's call.",
         ]),
    dict(num=4, code="04",
         title="AI for Reporting, Retrospectives and Improvement",
         subtitle="Generating status reports and dashboards · Analysing velocity and metrics with AI · Running AI-assisted retrospectives · Driving continuous improvement",
         weighting="25%",
         concepts=[
            "Status reports with AI — the AI turns sprint data and notes into a clear status report — progress against goal, completed and outstanding work, risks and next steps — pitched at the right level for its reader.",
            "Dashboards and summaries — the AI helps design and describe a simple delivery dashboard (goal, scope, burndown, velocity, risks) and writes the narrative that explains what the numbers mean.",
            "Analysing velocity — given past sprint data, the AI analyses velocity trends, flags a rising or falling trend, and helps forecast how much scope is realistic for coming sprints, with its assumptions stated.",
            "Reading the metrics honestly — the AI helps interpret metrics (velocity, throughput, cycle time, completion rate) as signals for conversation and improvement, not as targets to game or sticks to beat the team with.",
            "AI-assisted retrospectives — the AI helps design a retrospective, group and theme the team's raw input into patterns, and surface candid discussion points, so the facilitator can focus on the conversation.",
            "From retro to actions — the AI drafts a small set of specific, owned, time-bound improvement actions from the retrospective themes, which the team reviews, commits to and carries into the next sprint.",
            "Continuous improvement — the AI helps track improvement actions across sprints, spot recurring themes, and keep an honest record of what the team tried and what changed, feeding the inspect-and-adapt loop.",
            "Psychological safety — retrospective input is sensitive; you anonymise and aggregate it, keep it inside the team, and use AI to find themes, never to judge or expose individuals.",
            "Closing the loop — reporting, metrics and retrospectives only add value when they change what the team does next; the whole point of AI here is faster insight so the team spends its time acting on it.",
         ]),
]

# ------------------------------------------------------------------ day themes (7.5 instructional hours/day)
DAY_THEMES = {
    1: "Stand up the Tempo 2.0 delivery on an AI toolkit — set up ChatGPT, Claude and Gemini for agile work, build a reusable prompt library and a responsible-AI checklist, then draft and refine the user stories, groom and prioritise the product backlog, and plan the first sprint with a release roadmap",
    2: "Run and close out the Tempo 2.0 sprints with AI — summarise stand-ups and track progress, surface risks, blockers and dependencies, assist documentation, communication and testing, then generate status reports and a dashboard, analyse velocity, and run an AI-assisted retrospective that drives a real continuous-improvement plan",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. Each day totals exactly 480 scheduled minutes
# (excluding the 1-hour lunch); the 30 minutes of tea breaks sit inside that, so
# the instructional total is 7.5 hours per day (15 hours across the 2 days).
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:00","9:20",20,"admin","Welcome, course introduction and ground rules, and setup: signing in to ChatGPT, Claude and Gemini and confirming each assistant is ready for the labs"),
        ("9:20","10:00",40,"topic","TOPIC 01 — Getting Started with Generative AI for Agile: introduction to Agile, Scrum and generative AI; setting up AI tools for agile project management; effective prompting for agile tasks; responsible and human-in-the-loop use of AI (concepts + live demo)"),
        ("10:00","10:45",45,"lab","Hands-on: "+lab_titles([1])),
        ("10:45","11:00",15,"break","Tea break"),
        ("11:00","13:00",120,"lab","Hands-on: "+lab_titles([2,3])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:30",30,"topic","TOPIC 02 — AI for Backlogs, User Stories and Planning: drafting and refining user stories and acceptance criteria; grooming and prioritising the backlog with AI; sprint planning and estimation support; generating roadmaps and release plans (concepts + live demo)"),
        ("14:30","16:15",105,"lab","Hands-on: "+lab_titles([4,5])),
        ("16:15","16:30",15,"break","Tea break"),
        ("16:30","17:50",80,"lab","Hands-on: "+lab_titles([6])),
        ("17:50","18:00",10,"recap","Day 1 recap: the AI toolkit, the groomed and prioritised backlog, the first sprint plan and roadmap, and Q&A"),
     ]),
     2: (DAY_THEMES[2], [
        ("9:00","9:15",15,"admin","Day 1 recap, questions, and Day 2 introduction: from planning the sprint to running and closing it out with AI"),
        ("9:15","9:55",40,"topic","TOPIC 03 — AI for Sprints, Standups and Delivery: summarising stand-ups and tracking progress; identifying risks, blockers and dependencies with AI; assisting documentation and communication; supporting quality, testing and delivery (concepts + live demo)"),
        ("9:55","10:45",50,"lab","Hands-on: "+lab_titles([7])),
        ("10:45","11:00",15,"break","Tea break"),
        ("11:00","13:00",120,"lab","Hands-on: "+lab_titles([8,9])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:30",30,"topic","TOPIC 04 — AI for Reporting, Retrospectives and Improvement: generating status reports and dashboards; analysing velocity and metrics with AI; running AI-assisted retrospectives; driving continuous improvement (concepts + live demo)"),
        ("14:30","16:15",105,"lab","Hands-on: "+lab_titles([10,11])),
        ("16:15","16:30",15,"break","Tea break"),
        ("16:30","17:50",80,"lab","Hands-on: "+lab_titles([12])),
        ("17:50","18:00",10,"recap","Course wrap-up: the end-to-end Tempo 2.0 Agile AI Playbook, responsible-AI recap, and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="What Generative AI for Agile Really Is",
    concepts=[
        "A drafting and thinking partner — you describe an agile task in words and the assistant returns a usable first draft (a story, a plan, a summary, a report) in seconds, which you then refine.",
        "Across the whole Scrum cycle — the same skill applies to backlog, planning, stand-ups, delivery, reporting and retrospectives; AI helps at every event, not just one.",
        "Prompt, review, own — the workflow is always the same: give a structured prompt, review and correct the draft, and take ownership of the result. The AI never decides.",
        "The same three tools — ChatGPT, Claude and Gemini all work the same way from your point of view; learn the prompting and review skills once and use whichever tool your team has.",
    ],
    framework_title="The AI-Assisted Agile Loop",
    framework=[
        ("Set up", "Sign in to your assistant, start a focused chat, and paste in the context — the project brief, backlog or notes the task needs."),
        ("Prompt", "Give the AI a role, the context, the exact task, the output format and any constraints, so it drafts what you actually need."),
        ("Review", "Check the draft for accuracy, fit, invented facts, fairness and clarity — the human-in-the-loop step that makes the output safe to use."),
        ("Refine", "Correct, tighten and adapt the draft with follow-up prompts and your own edits until it meets the team's standard."),
        ("Apply", "Put the reviewed result into the real agile artifact — the backlog, plan, report or retro — and save the prompt for reuse next sprint."),
    ],
    statement=dict(
        headline="Generative AI gives an agile team a fast first draft of almost every written and analytical task — the craft is prompting well, reviewing with judgement, and keeping every decision human.",
        body="This course is hands-on: you take one product — Tempo, a habit-tracking app from the fictional studio Cadence Labs — through a full AI-assisted delivery of its 2.0 release, building a connected 'Tempo 2.0 Agile AI Playbook' from setup and prompts, to backlog, planning, sprint execution, reporting and a retrospective, using ChatGPT, Claude and Gemini.",
        kicker="THE AGILE-AI RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("An AI toolkit for Agile", ["ChatGPT, Claude and Gemini set up for agile work", "A reusable agile prompt library", "A responsible, human-in-the-loop AI checklist"]),
        ("A planned, prioritised backlog", ["INVEST-quality user stories and acceptance criteria", "A groomed, MoSCoW-prioritised product backlog", "A sprint plan, estimates and a release roadmap"]),
        ("A running, tracked sprint", ["Stand-up summaries and progress tracking", "A risk, blocker and dependency log", "AI-assisted docs, comms and test scenarios"]),
        ("Reporting and improvement", ["Stakeholder status reports and a delivery dashboard", "A velocity and metrics analysis", "An AI-assisted retrospective and improvement plan"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the AI technique on the shared Tempo 2.0 example.",
        "You run it yourself in ChatGPT, Claude or Gemini using the supplied Tempo project brief and inputs.",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You review and refine — correct the draft, fix any invented detail, and adapt it — until it meets the team's standard.",
        "You save the reviewed output and the prompt — each becomes the next section of your Tempo 2.0 Agile AI Playbook.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Generative AI for Agile Project Management (C324) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 12 hands-on labs, in the order you "
    "will run them across the two days, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build a single, connected deliverable — the Tempo 2.0 Agile AI Playbook, for a fictional "
    "habit-tracking app called Tempo from the studio Cadence Labs, planning and delivering its 2.0 release. You "
    "start in Lab 1 by setting up ChatGPT, Claude and Gemini as an agile toolkit, then in every lab you take the "
    "delivery one stage further — a reusable prompt library, a responsible-AI checklist, refined user stories "
    "and acceptance criteria, a groomed and prioritised backlog, a sprint plan and release roadmap, stand-up "
    "summaries and progress tracking, a risk and dependency log, AI-assisted documentation and test scenarios, "
    "stakeholder status reports and a dashboard, a velocity analysis, and finally an AI-assisted retrospective "
    "and continuous-improvement plan. A Tempo 2.0 project brief with sample inputs is supplied in "
    "labs/reference-pack/; you may substitute your own non-confidential project wherever you prefer."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection — every generative feature runs in the cloud.",
        "Access to at least one, ideally all three, generative AI assistants: ChatGPT (chat.openai.com), Claude (claude.ai) and Gemini (gemini.google.com). A free account for each is enough to follow the labs; the trainer will confirm what is available.",
        "A signed-in account for each assistant you will use, tested before Lab 1 with a simple 'hello' prompt so you know it responds.",
        "A place to keep your work — a documents folder or note-taking app — to save each reviewed AI output and prompt as a section of your Tempo 2.0 Agile AI Playbook.",
        "The supplied Tempo 2.0 project brief and sample inputs (product vision, team, raw backlog, sample stand-up notes and sprint metrics) in labs/reference-pack/ — or a few notes and sample inputs from your own non-confidential project to use instead.",
    ],
    verify_text="Before Lab 1, confirm you can open and sign in to at least one assistant, send a simple prompt and get a reply, and that you have the Tempo 2.0 project brief to hand. If anything is missing, tell the trainer.",
    verify_code="Open chat.openai.com (ChatGPT) · claude.ai (Claude) · gemini.google.com (Gemini)  ·  sign in  ·  send \"Hello, are you ready to help me with agile project management?\"  ·  confirm a reply",
    conventions=[
        "Placeholders such as <YOUR PROJECT>, <TEAM CAPACITY> or <PASTE NOTES> are replaced with your own values before you send a prompt.",
        "Prompts to paste into ChatGPT, Claude or Gemini are shown in the 'Prompt to use' blocks — adapt the bracketed parts to your own project.",
        "Where a lab says 'any assistant', use whichever of the three you prefer; a few labs ask you to compare the same prompt across two tools.",
        "Every lab ends with a 'Test it' step — an explicit check that the reviewed output meets the standard before you move on.",
        "Keep every reviewed output and prompt in one project folder (Tempo-2.0-Playbook) so your playbook stays together and consistent.",
    ],
)
LAB_NOTE = (
    "Use only projects, data and notes you are authorised to use. Do not paste confidential customer data, "
    "personal information, credentials or proprietary code into a public AI assistant. Use the supplied Tempo "
    "2.0 project brief rather than real client material, treat every AI output as a first draft to be reviewed "
    "and fact-checked, and be transparent with your team about what was AI-assisted before it goes into a real "
    "backlog, plan, report or decision."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="You have taken one product — Tempo 2.0 — through an entire AI-assisted agile delivery across two days, from setting up an AI toolkit to running a retrospective, using ChatGPT, Claude and Gemini as a drafting and analysis partner while keeping every decision human.",
    sections=[
        dict(title="What you built", bullets=[
            "An AI toolkit for agile work — ChatGPT, Claude and Gemini set up, a reusable agile prompt library, and a responsible, human-in-the-loop checklist.",
            "A planned delivery — INVEST-quality user stories and acceptance criteria, a groomed and MoSCoW-prioritised product backlog, and a sprint plan, estimates and release roadmap.",
            "A running sprint — stand-up summaries and progress tracking, a risk, blocker and dependency log, and AI-assisted documentation, communication and test scenarios.",
            "A closed-out sprint — stakeholder status reports and a delivery dashboard, a velocity and metrics analysis, and an AI-assisted retrospective with a concrete continuous-improvement plan.",
            "One connected Tempo 2.0 Agile AI Playbook that carries the whole delivery, section by section.",
        ]),
        dict(title="What to do next", bullets=[
            "Rebuild the playbook for a real, non-confidential project of your own using the same prompts and templates.",
            "Introduce your saved prompt library to your team so everyone drafts stories, summaries and reports the same way.",
            "Keep your responsible-AI checklist visible in every sprint — review, fact-check and protect data every time.",
            "Always keep the team's judgement in the loop: the AI drafts and analyses, but the Product Owner, Scrum Master and team own every decision.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rerun the key labs on your own real, non-confidential project, from setup and prompts to a retrospective.",
    "Introduce your prompt library and responsible-AI checklist to your team so the practice sticks beyond the course.",
    "Review each lab's detailed steps in this guide and re-create the playbook in your own AI assistant.",
]
LG_GLOSSARY = [
    ("Agile", "An iterative approach to delivering value in small increments, inspecting and adapting frequently rather than following one big up-front plan."),
    ("Scrum", "The most common Agile framework, with fixed roles, events and artifacts organised around short iterations called sprints."),
    ("Sprint", "A short, fixed-length iteration (commonly 1–4 weeks) in which the team delivers a usable increment toward the product goal."),
    ("Product Owner", "The Scrum role accountable for the product backlog, its priority, and maximising the value the team delivers."),
    ("Scrum Master", "The Scrum role that facilitates the process, removes impediments, and helps the team improve; the main AI user in several of these labs."),
    ("Product backlog", "The ordered, evolving list of everything that might be built — features, fixes and work — from which sprints are planned."),
    ("Sprint backlog", "The set of backlog items the team commits to for a sprint, plus the plan (tasks) for delivering them."),
    ("User story", "A short, user-centred description of a feature in the form 'As a <role>, I want <goal>, so that <benefit>'."),
    ("INVEST", "A checklist for good user stories — Independent, Negotiable, Valuable, Estimable, Small, Testable."),
    ("Acceptance criteria", "The conditions, often written Given/When/Then, that a story must meet to be considered done."),
    ("Backlog grooming (refinement)", "The ongoing work of clarifying, splitting, merging, estimating and ordering backlog items so they are ready for planning."),
    ("MoSCoW", "A prioritisation method sorting work into Must have, Should have, Could have and Won't have (this time)."),
    ("Story point", "A unit of relative estimate for the effort of a story, used instead of hours to size work by comparison."),
    ("Velocity", "The amount of work (usually story points) a team completes per sprint, used as a trend to forecast realistic scope."),
    ("Burndown", "A chart or narrative showing how much work remains in a sprint or release over time."),
    ("Daily stand-up", "The short daily Scrum event where the team syncs on progress, plans and blockers."),
    ("Blocker / impediment", "Anything stopping a team member or story from progressing, which the Scrum Master works to remove."),
    ("Dependency", "A relationship where one item, team or external party must be done or available before another can proceed."),
    ("Definition of Done", "The team's shared, agreed checklist of what must be true for a story or increment to count as complete."),
    ("Retrospective", "The Scrum event at the end of a sprint where the team reflects on how it worked and agrees improvements."),
    ("Continuous improvement", "The ongoing inspect-and-adapt practice of making small, owned changes each sprint based on evidence and reflection."),
    ("Roadmap", "A higher-level, multi-sprint view of the themes and releases planned over time, kept deliberately flexible."),
    ("Release plan", "A plan grouping backlog items into releases with target dates, dependencies and milestones."),
    ("Generative AI assistant", "A general-purpose chat tool (ChatGPT, Claude, Gemini) that generates text drafts and analysis from a prompt."),
    ("Prompt", "The instruction you give the assistant; a structured prompt with role, context, task, format and constraints produces a far better draft than a vague one."),
    ("Prompt library", "A saved, reusable set of prompt templates for the recurring agile tasks, shared across the team."),
    ("Human-in-the-loop", "Keeping a person responsible for reviewing, correcting and approving every AI output before it is used."),
    ("Hallucination", "A confident but false or invented statement from an AI, which is why every output must be fact-checked."),
    ("Responsible AI use", "Using AI safely and ethically — protecting sensitive data, checking facts, being fair, and being transparent about AI assistance."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C324 Generative AI for Agile Project Management courseware.", TRAINER),
]
