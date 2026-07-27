"""
Domain 2 — AI for Backlogs, User Stories and Planning. Labs 4-6.

Continues the connected Tempo 2.0 Agile AI Playbook. With the AI toolkit, prompt
library and responsible-AI checklist from Domain 1 in place, these labs turn the
raw Tempo 2.0 ideas into a planned delivery: Lab 4 drafts and refines user stories
and acceptance criteria; Lab 5 grooms and prioritises the product backlog; Lab 6
plans the first sprint, estimates the work and builds a release roadmap.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes a section of your Tempo 2.0 Agile AI Playbook, "
 "the connected project you assemble across all 12 labs."
)

DOMAIN2 = [
 dict(
 num=4, topic=2,
 title="Draft and Refine User Stories and Acceptance Criteria",
 objective="Turn raw Tempo 2.0 feature ideas into INVEST-quality user stories with AI, then draft and refine testable acceptance criteria, reviewing every one so it reflects the real user and real value.",
 desc="Planning starts with well-formed stories. In this lab you take the rough feature ideas from the Tempo "
 "2.0 brief and use an assistant to draft them as proper user stories in the 'As a <role>, I want <goal>, so "
 "that <benefit>' form. You prompt the AI to check its own stories against INVEST and to flag any that are too "
 "big or vague to estimate, then split those with its help. For your key stories you draft acceptance criteria "
 "in Given/When/Then form and review them for gaps, edge cases and testability. Throughout, you apply your "
 "responsible-AI checklist — the AI drafts, you decide what is right for the real user. " + PROJECT_NOTE,
 build="A set of INVEST-checked Tempo 2.0 user stories (with over-large ones split) and, for the key stories, testable Given/When/Then acceptance criteria — all reviewed by you and saved as the stories section of your playbook.",
 services="Any assistant, the user-story template from your prompt library, the INVEST checklist, story splitting, Given/When/Then acceptance criteria",
 steps=[
 ("Open the Tempo 2.0 brief and copy the raw feature ideas for the 2.0 release (shared team habits, the smarter reminder engine, the insights dashboard, and the listed bug fixes). Open your agile prompt library and grab your user-story template.", ""),
 ("Draft the first batch of stories. Paste the prompt below, filling the context slot with the raw ideas.",
  "You are an experienced Agile Product Owner for Tempo, a habit-tracking app. Context: here are the raw feature ideas for our 2.0 release:\n<PASTE THE RAW FEATURE IDEAS>\nTask: write clear user stories in the form 'As a <role>, I want <goal>, so that <benefit>'. Format: group them under the three feature themes (shared team habits, smarter reminders, insights dashboard). Constraints: focus on user value, keep each story to one sentence, and cover the main users (an individual user, a team member, a team admin)."),
 ("Quality-check against INVEST. Ask the AI to grade its own stories and flag the weak ones, using the prompt below, then read its judgement critically.",
  "Review each story above against INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable). Present a table: Story | INVEST issues | Suggested fix. Be strict — flag any story that is too big or vague to estimate in one sprint."),
 ("Split the over-large stories. Take one story the AI flagged as too big and ask it to split the work into smaller, independently valuable stories.",
  "Split this user story into 2-4 smaller stories that are each independently valuable, small enough to finish in one sprint, and testable. Keep the same 'As a / I want / so that' form:\n<PASTE THE OVER-LARGE STORY>"),
 ("Draft acceptance criteria for your key stories. Choose the three most important stories and generate testable criteria with the prompt below.",
  "For each of the three user stories below, write acceptance criteria in Given/When/Then form that define exactly when the story is done. Include at least one edge case or error condition per story. Keep each criterion testable and unambiguous.\n<PASTE THE THREE KEY STORIES>"),
 ("Review the acceptance criteria as a human. For each story ask: does 'done' really mean done here? Is a realistic edge case missing (offline, permissions, an empty state, a shared-habit conflict)? Add or correct criteria yourself where the AI missed something.", ""),
 ("Save the stories section of your playbook: the INVEST-checked stories grouped by theme, the split of the over-large story, and the reviewed Given/When/Then acceptance criteria for the key stories, in your Tempo-2.0-Playbook folder.", ""),
 ],
 test="You have a reviewed set of Tempo 2.0 user stories in proper form, checked against INVEST with at least one over-large story split into smaller ones, and testable Given/When/Then acceptance criteria (including edge cases) for your key stories — all human-reviewed and saved to your playbook.",
 ),
 dict(
 num=5, topic=2,
 title="Groom and Prioritise the Product Backlog with AI",
 objective="Use AI to groom a messy raw backlog — clarifying, splitting, merging and de-duplicating items — then prioritise it with MoSCoW and value-versus-effort, keeping the final ordering a human decision.",
 desc="A raw idea list is not a backlog. In this lab you turn the Tempo 2.0 stories and remaining raw items "
 "into a groomed, ordered product backlog. You use an assistant to clean the list — clarify vague wording, "
 "split items that are really several, merge duplicates, and fill obvious gaps — so every item is ready. Then "
 "you prioritise: the AI applies MoSCoW (Must / Should / Could / Won't) and a value-versus-effort view and "
 "explains its reasoning, and you, in the Product Owner's seat, make the final call and adjust the order. The "
 "result is a ready, prioritised backlog you can plan a sprint from. " + PROJECT_NOTE,
 build="A groomed, prioritised Tempo 2.0 product backlog — cleaned and de-duplicated, each item tagged with a MoSCoW category and a value/effort view, ordered for planning, with your Product-Owner adjustments applied.",
 services="Any assistant, the backlog-grooming template from your prompt library, MoSCoW prioritisation, value-versus-effort analysis, Product-Owner review",
 steps=[
 ("Assemble your raw backlog: your Lab 4 stories plus any remaining raw ideas and bug fixes from the Tempo 2.0 brief that are not yet stories. Paste them into any assistant as one messy list so you can groom it.", ""),
 ("Groom the list. Use the prompt below to clarify, split, merge and de-duplicate.",
  "You are helping a Product Owner groom a product backlog. Here is our raw Tempo 2.0 backlog:\n<PASTE THE RAW BACKLOG>\nTask: return a cleaned, ready backlog. Clarify any vague item, split any item that is really several, merge duplicates, and flag anything missing important detail. Present it as a numbered list with a one-line description per item. Do not invent new features that are not implied by the list."),
 ("Review the grooming. Check the AI did not quietly drop or invent items. Confirm each split and merge makes sense to you; undo any you disagree with. Grooming is a judgement call, not an automatic one.", ""),
 ("Prioritise with MoSCoW. Ask the AI to categorise and explain, using the prompt below.",
  "Prioritise the groomed backlog using MoSCoW (Must have, Should have, Could have, Won't have this release). For the Tempo 2.0 release, our goal is to ship shared team habits and reliable reminders first. Present a table: Item | MoSCoW | One-line reason. Then list the 'Must have' items in the order you would build them and explain the ordering."),
 ("Add a value-versus-effort view. Ask the AI to estimate relative value and effort so you can spot quick wins and expensive extras.",
  "For each backlog item, add a rough Value (High/Medium/Low) and Effort (High/Medium/Low) rating and mark any that are High-value / Low-effort as 'quick win'. Present as a table and briefly note which items look like poor value for their effort."),
 ("Make the Product Owner's call. Reconcile MoSCoW and value/effort into one ordered backlog. Move at least two items yourself against the AI's suggestion where you disagree, and write one line explaining each override — this is the human decision the AI supports but does not make.", ""),
 ("Save the prioritised backlog section of your playbook: the groomed items, their MoSCoW and value/effort tags, the final ordering, and your override notes, in your Tempo-2.0-Playbook folder.", ""),
 ],
 test="You have a groomed, de-duplicated Tempo 2.0 backlog with every item tagged by MoSCoW and value/effort, ordered ready for planning, and you have made at least two Product-Owner overrides against the AI's suggestion with reasons — a backlog you own, not one the AI decided.",
 ),
 dict(
 num=6, topic=2,
 title="Plan the Sprint, Estimate, and Build the Release Roadmap",
 objective="Use AI to propose a sprint goal and candidate sprint backlog from the team's capacity, get relative estimates with their assumptions surfaced, and draft a multi-sprint roadmap and release plan — with the team owning every commitment.",
 desc="With a prioritised backlog you can plan. In this lab you use an assistant to support sprint planning "
 "end to end. Given the team's capacity and the top of the backlog, the AI proposes a realistic sprint goal "
 "and a candidate sprint backlog and helps break the top stories into tasks. It suggests relative "
 "story-point estimates and — crucially — surfaces the assumptions and risks behind each, giving the team a "
 "starting point for a planning-poker conversation rather than numbers to accept. Finally it drafts a "
 "multi-sprint roadmap and a release plan from the backlog, making themes, dependencies and milestones "
 "explicit. You keep ownership throughout: the AI's numbers are inputs, the team's commitment is the "
 "decision. This lab completes Day 1. " + PROJECT_NOTE,
 build="A first-sprint plan for Tempo 2.0 (a sprint goal, a candidate sprint backlog broken into tasks), relative estimates with their assumptions and risks surfaced, and a multi-sprint roadmap and release plan — all reviewed and adjusted by you.",
 services="Any assistant, the prioritised backlog from Lab 5, team capacity, sprint-goal and task breakdown, story-point estimation support, roadmap and release planning",
 steps=[
 ("Gather your inputs: your prioritised backlog from Lab 5 and the team's capacity from the brief (team size, sprint length, and any planned leave). Note the sprint length is two weeks.", ""),
 ("Propose a sprint goal and candidate sprint backlog. Paste the prompt below with your inputs.",
  "You are an Agile delivery assistant. Context: here is our prioritised Tempo 2.0 backlog:\n<PASTE THE PRIORITISED BACKLOG>\nOur team capacity for a 2-week sprint is <TEAM CAPACITY>. Task: propose one clear sprint goal for Sprint 1 and a candidate sprint backlog of items that fit the capacity and serve that goal. Format: state the sprint goal in one sentence, then list the selected items. Constraints: prefer the 'Must have' items and a coherent goal over cramming in unrelated work."),
 ("Break the top stories into tasks. Ask the AI to decompose the candidate sprint backlog into concrete tasks.",
  "Break each item in the candidate sprint backlog into the concrete tasks needed to deliver it (design, build, test, review, etc.). Present as a checklist grouped by story. Keep tasks small enough to finish in a day or two."),
 ("Get estimation support with assumptions surfaced. Use the prompt below — the assumptions matter more than the numbers.",
  "Suggest a relative story-point estimate (using the sequence 1, 2, 3, 5, 8, 13) for each item in the candidate sprint backlog. For every estimate, state the key assumption and the main risk behind it in one line. Make clear these are a starting point for the team's planning-poker discussion, not final numbers."),
 ("Run the human estimation check. Pick two items where you disagree with the AI's story points and write your own estimate and reasoning. This mirrors the planning-poker conversation the team would have — the AI opens it, the team settles it.", ""),
 ("Draft the roadmap and release plan. Generate a higher-level view with the prompt below.",
  "From the full prioritised backlog, draft a multi-sprint roadmap for Tempo 2.0 across the next 4 sprints, grouping work into themes (shared team habits, smarter reminders, insights dashboard, fixes and polish). Then draft a release plan showing which themes ship in which release, and list the key dependencies and milestones. Present the roadmap as a table (Sprint | Theme | Main items) and the release plan as a short bulleted plan. State any assumption you make."),
 ("Review and save. Sanity-check the roadmap against reality — is the sequence sensible, are dependencies right, is anything over-committed? Adjust it yourself, then save the sprint plan, estimates and roadmap as the planning section of your Tempo-2.0-Playbook. Day 1 is complete: you have a toolkit, a prioritised backlog and a plan.", ""),
 ],
 test="You have a reviewed Sprint 1 plan (a one-sentence sprint goal and a capacity-fit sprint backlog broken into tasks), story-point estimates with their assumptions and risks surfaced and at least two you re-estimated yourself, and a multi-sprint roadmap and release plan with dependencies and milestones — all saved to your playbook.",
 ),
]
