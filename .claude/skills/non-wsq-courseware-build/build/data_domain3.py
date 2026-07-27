"""
Domain 3 — AI for Sprints, Standups and Delivery. Labs 7-9. (Day 2 begins here.)

Continues the connected Tempo 2.0 Agile AI Playbook into sprint execution. With
the sprint planned, these labs run it with AI: Lab 7 summarises stand-ups and
tracks progress; Lab 8 surfaces risks, blockers and dependencies and plans
mitigations; Lab 9 assists documentation, communication, quality and testing.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes a section of your Tempo 2.0 Agile AI Playbook, "
 "the connected project you assemble across all 12 labs."
)

DOMAIN3 = [
 dict(
 num=7, topic=3,
 title="Summarise Stand-ups and Track Sprint Progress",
 objective="Turn raw daily stand-up notes into a clear, consistent summary with AI, then track progress against the sprint goal and draft a plain-language burndown narrative — keeping the team's read of reality in the loop.",
 desc="Once the sprint is running, a lot of the Scrum Master's time goes into writing updates. In this lab you "
 "hand that drafting to an assistant. You take the supplied raw daily stand-up notes for Tempo 2.0 — terse, "
 "messy, in everyone's own words — and prompt the AI to turn them into a clean summary of what was done, what "
 "is planned and what is blocked. You then track progress against the sprint goal: you ask the AI to describe "
 "what has moved and what is stuck, and to write a plain-language burndown narrative from the remaining work. "
 "You review every summary against what you actually know, because the AI can only work from the notes it is "
 "given. " + PROJECT_NOTE,
 build="A clean daily stand-up summary generated from raw notes, a progress-against-goal update, and a plain-language burndown narrative for the Tempo 2.0 sprint — all reviewed and saved as the tracking section of your playbook.",
 services="Any assistant, the stand-up-summary template from your prompt library, the raw stand-up notes, progress-against-goal tracking, a burndown narrative",
 steps=[
 ("Open the supplied raw daily stand-up notes for the Tempo 2.0 sprint (labs/reference-pack/) — several days of terse, informal updates from the team. Grab your stand-up-summary template from your prompt library.", ""),
 ("Summarise one day's stand-up. Paste the prompt below with a single day's raw notes.",
  "You are a Scrum Master assistant. Here are today's raw daily stand-up notes for our Tempo 2.0 sprint:\n<PASTE ONE DAY'S RAW NOTES>\nTask: summarise them clearly under three headings — Done since yesterday, Planned today, Blockers. Format: short bullet points. Constraints: use only what the notes say, keep each person's items attributed, and list any blocker separately so nothing is buried."),
 ("Review the summary against reality. Check it captured every blocker and did not invent progress. If a note was ambiguous, decide what it really meant — the AI cannot know, you can.", ""),
 ("Track progress against the sprint goal. Feed several days of notes and the sprint goal together with the prompt below.",
  "Here is our Sprint 1 goal:\n<PASTE THE SPRINT GOAL>\nand here are the stand-up summaries for the last few days:\n<PASTE THE DAILY SUMMARIES>\nTask: describe our progress toward the sprint goal — what has clearly moved forward, what is stuck, and whether the goal still looks achievable this sprint. Be honest and specific; do not sugar-coat. Flag anything that looks at risk."),
 ("Draft a burndown narrative. Ask the AI to describe the remaining work in plain language, using the prompt below.",
  "Given that the sprint started with <TOTAL STORY POINTS> points and roughly <REMAINING POINTS> remain with <DAYS LEFT> days left, write a short plain-language 'burndown' narrative a non-technical stakeholder could understand: are we ahead, on track or behind, and what would need to happen to finish on plan? State the assumption behind your read."),
 ("Apply your judgement. Compare the AI's 'on track / behind' read with your own sense of the sprint. Where they differ, write the truer version yourself. A burndown narrative is only useful if it is honest.", ""),
 ("Save the tracking section of your playbook: the daily stand-up summary, the progress-against-goal update and the reviewed burndown narrative, in your Tempo-2.0-Playbook folder.", ""),
 ],
 test="You have turned raw stand-up notes into a clean, attributed summary under Done/Planned/Blockers, produced an honest progress-against-goal update and a plain-language burndown narrative for the Tempo 2.0 sprint, and reviewed each against what you actually know — all saved to your playbook.",
 ),
 dict(
 num=8, topic=3,
 title="Identify Risks, Blockers and Dependencies with AI",
 objective="Use AI to read the team's notes and backlog and surface likely risks, blockers and dependencies early, map how the work depends on itself and on outside parties, and turn each into a mitigation and escalation the Scrum Master owns.",
 desc="A big part of the Scrum Master's value is seeing trouble early. In this lab you use an assistant to "
 "widen what you notice. You give the AI the sprint's stand-up notes, backlog and plan, and prompt it to flag "
 "likely risks, blockers and impediments — including ones the team has not named yet. You ask it to map "
 "dependencies between stories, between the team and other teams, and on external parties, and to suggest a "
 "sequence that unblocks work in the right order. For each risk or blocker it drafts mitigation options and a "
 "clear escalation path. You then review every item — the AI can over- or under-state risk — and turn the "
 "real ones into a risk log with owners and actions. " + PROJECT_NOTE,
 build="A reviewed Tempo 2.0 risk, blocker and dependency log — likely risks and impediments surfaced from the notes, a dependency map with a suggested unblocking sequence, and a mitigation and escalation path with an owner for each real item.",
 services="Any assistant, the sprint notes and backlog, risk and blocker identification, dependency mapping, mitigation and escalation planning, a Scrum-Master review",
 steps=[
 ("Gather the evidence: your stand-up summaries and burndown from Lab 7, your sprint plan from Lab 6, and the backlog. Paste the relevant parts into any assistant.", ""),
 ("Surface risks and blockers. Use the prompt below to have the AI flag trouble early.",
  "You are an experienced Scrum Master. Based on this Tempo 2.0 sprint information:\n<PASTE STAND-UP SUMMARIES, PLAN AND BACKLOG>\nTask: identify the likely risks, blockers and impediments to finishing this sprint — including ones the team has not explicitly named. Format: a table with Risk/Blocker | Why it matters | Likelihood (H/M/L) | Impact (H/M/L). Be specific to this sprint; do not list generic project risks."),
 ("Map dependencies. Ask the AI to make the dependencies explicit with the prompt below.",
  "From the same sprint information, map the dependencies: which stories or tasks depend on another being done first, which depend on another team or an external party (for example an app-store review, a third-party reminder/push service, or a design sign-off), and where a dependency could block the sprint goal. Present as a list of 'A depends on B because…' statements, then suggest an order of work that unblocks things in the right sequence."),
 ("Sanity-check the AI's read. Go through its risks and dependencies and mark each as real, over-stated or missed. Add at least one risk or dependency you know about from context that the AI did not surface. The AI widens your view; it does not replace it.", ""),
 ("Plan mitigations and escalations. For the real risks and blockers, generate options with the prompt below.",
  "For each of these confirmed risks and blockers:\n<PASTE THE CONFIRMED LIST>\nsuggest one or two practical mitigation options and a clear escalation path (who to raise it to and when). Format: Risk/Blocker | Mitigation | Escalation. Keep the actions concrete and doable within a sprint."),
 ("Assign owners and decide actions. As the Scrum Master, put a named owner and a next action against each real risk and blocker — the AI proposes, you commit. Remove anything that is noise so the log stays trusted and short.", ""),
 ("Save the risk, blocker and dependency log as a section of your Tempo-2.0-Playbook folder: the confirmed items with likelihood/impact, the dependency map and unblocking order, and each item's mitigation, escalation, owner and next action.", ""),
 ],
 test="You have a reviewed Tempo 2.0 risk, blocker and dependency log — likely items surfaced early, a dependency map with a sensible unblocking order, at least one risk you added from your own knowledge, and a mitigation, escalation, owner and next action for every real item — saved to your playbook.",
 ),
 dict(
 num=9, topic=3,
 title="Assist Documentation, Communication and Testing",
 objective="Use AI to draft the sprint's routine documentation, tailor the same update for different audiences, and generate test scenarios and a definition-of-done check from acceptance criteria — reviewing each so quality stays the team's call.",
 desc="Documentation, communication and testing quietly consume a sprint. In this lab you use an assistant to "
 "lift that load across all three. For documentation, you draft release notes, a decision log entry and "
 "meeting minutes so they are written consistently and kept current. For communication, you take one sprint "
 "update and have the AI re-pitch it for three audiences — the team, stakeholders and leadership — keeping "
 "tone and detail right for each. For quality, you turn your Lab 4 acceptance criteria into test scenarios and "
 "a checklist, ask the AI to suggest edge cases, and use it to check whether a story truly meets its "
 "definition of done. You review everything: the AI drafts, the team decides what 'done' and 'good enough' "
 "mean. " + PROJECT_NOTE,
 build="AI-assisted sprint documentation (release notes, a decision log entry, meeting minutes), one update re-pitched for the team, stakeholders and leadership, and test scenarios plus a definition-of-done check generated from your acceptance criteria — all reviewed and saved.",
 services="Any assistant, documentation drafting, audience-tailored communication, test-scenario generation from acceptance criteria, a definition-of-done check",
 steps=[
 ("Draft the routine documentation. Using what the sprint has delivered so far, generate release notes with the prompt below, then repeat the idea for a decision-log entry and short meeting minutes.",
  "You are a delivery documentation assistant. Based on the work completed in our Tempo 2.0 sprint so far:\n<PASTE THE COMPLETED ITEMS>\nTask: write concise release notes under 'New', 'Improved' and 'Fixed'. Then, separately, draft a one-paragraph decision-log entry template and a short meeting-minutes template we can reuse. Constraints: use only the information given, and mark anything uncertain as '[to confirm]' rather than inventing it."),
 ("Review the docs for invented detail. Check the release notes claim only what was actually done, and that every '[to confirm]' is a real gap for a human to fill. Correct anything overstated.", ""),
 ("Tailor communication for three audiences. Take one progress update and re-pitch it with the prompt below.",
  "Here is a sprint progress update:\n<PASTE YOUR PROGRESS UPDATE FROM LAB 7>\nRewrite it for three audiences: (1) the development team — technical, detailed, honest about blockers; (2) stakeholders — plain language, focused on value and dates; (3) leadership — three lines, the headline, the risk and the ask. Keep every version truthful to the same facts; only change tone and detail."),
 ("Check the tone yourself. Read the leadership version as if you were the executive: is it clear, honest and free of jargon and spin? Adjust it — you own how the team communicates, not the AI.", ""),
 ("Generate test scenarios from acceptance criteria. Feed your Lab 4 acceptance criteria in with the prompt below.",
  "For the user story and acceptance criteria below:\n<PASTE A KEY STORY AND ITS GIVEN/WHEN/THEN CRITERIA>\nTask: write test scenarios that would verify each acceptance criterion, including edge cases and error conditions (offline, permissions denied, an empty state, a shared-habit conflict). Format: a numbered checklist of 'Given/When/Then' test cases. Note any acceptance criterion that is not actually testable as written."),
 ("Run a definition-of-done check. Ask the AI to test a story against your Definition of Done, then apply your own judgement.",
  "Here is our Definition of Done:\n<PASTE OR LIST YOUR DEFINITION OF DONE>\nand here is a story we think is finished:\n<PASTE THE STORY AND WHAT WAS DELIVERED>\nTask: check it against each Definition-of-Done item and list what is met, not met or unclear. Do not pass anything you cannot verify from the information given."),
 ("Save the documentation, communication and testing section of your Tempo-2.0-Playbook folder: the reviewed release notes and templates, the three audience-tailored updates, and the test scenarios and definition-of-done check.", ""),
 ],
 test="You have AI-assisted sprint documentation with invented detail removed and gaps marked '[to confirm]', one update correctly re-pitched for the team, stakeholders and leadership, and test scenarios plus a definition-of-done check generated from your acceptance criteria and reviewed by you — all saved to your playbook.",
 ),
]
