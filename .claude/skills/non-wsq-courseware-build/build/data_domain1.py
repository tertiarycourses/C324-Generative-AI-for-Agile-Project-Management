"""
Domain 1 — Getting Started with Generative AI for Agile. Labs 1-3.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab in this course takes one connected deliverable — the Tempo 2.0 Agile AI
Playbook, for a fictional habit-tracking app called Tempo from the studio Cadence
Labs, planning and delivering its 2.0 release — one stage further. Lab 1 sets up
ChatGPT, Claude and Gemini as an agile toolkit and establishes the human-in-the-
loop habit; Lab 2 builds a reusable agile prompt library; Lab 3 builds and applies
a responsible-AI checklist. A Tempo 2.0 project brief with sample inputs is
supplied; use your own non-confidential project instead wherever you prefer.
"""

SCENARIO = (
 "Tempo is a fictional Singapore habit- and routine-tracking mobile app from the small product studio Cadence "
 "Labs. The team is a standard Scrum team — a Product Owner, a Scrum Master and a handful of developers and a "
 "designer — and they are planning the 'Tempo 2.0' release, which adds shared team habits, a smarter reminder "
 "engine and an insights dashboard. The raw material is realistic and messy: a rough list of feature ideas and "
 "bug reports, a stakeholder wish-list, sample daily stand-up notes, and metrics from the last few sprints. You "
 "play the Scrum Master and delivery lead, and across this course you use ChatGPT, Claude and Gemini to take "
 "Tempo 2.0 from raw ideas all the way through planning, a running sprint, reporting and a retrospective — "
 "building one connected Tempo 2.0 Agile AI Playbook. Use this scenario only if you cannot use a real, "
 "non-confidential project of your own; your own project or team is always welcome."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes a section of your Tempo 2.0 Agile AI Playbook, "
 "the connected project you assemble across all 12 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Set Up Your AI Toolkit for Agile Project Management",
 objective="Sign in to ChatGPT, Claude and Gemini, give the same agile task to each, compare their drafts, and set up your Tempo 2.0 workspace and the human-in-the-loop review habit that every later lab depends on.",
 desc="This lab gets you comfortable with the tools before any real planning begins. You open ChatGPT, Claude "
 "and Gemini in your browser, sign in to each, and read the supplied Tempo 2.0 project brief so you know the "
 "product you will be working on. You give all three assistants the same simple agile task, compare how they "
 "respond, and see that they work the same way from your point of view — a prompt in, a draft out. You then "
 "establish the two habits that run through the whole course: keeping an organised project folder for your "
 "playbook, and treating every AI answer as a first draft you review rather than a fact you accept. " + PROJECT_NOTE,
 build="A working AI toolkit — ChatGPT, Claude and Gemini signed in and tested — plus a Tempo-2.0-Playbook project folder, a short written note on how the three assistants differed on the same task, and a clear grasp of the prompt-review-own workflow.",
 services="ChatGPT (chat.openai.com), Claude (claude.ai), Gemini (gemini.google.com), the Tempo 2.0 project brief, a project folder, the prompt-review-own workflow",
 steps=[
 ("Create a folder on your machine called 'Tempo-2.0-Playbook' so every reviewed output and prompt you make across the course stays together. Open the supplied Tempo 2.0 project brief (labs/reference-pack/) and skim the product vision, the team and the sample inputs so you know what you are working on.", ""),
 ("Open all three assistants in separate browser tabs — chat.openai.com (ChatGPT), claude.ai (Claude) and gemini.google.com (Gemini) — and sign in to each. Send each a simple 'hello' to confirm it responds.", ""),
 ("Give the SAME agile task to each assistant so you can compare them. Paste the prompt below into ChatGPT, then into Claude, then into Gemini.",
  "You are an Agile coach. In plain language, explain to a new Scrum team the purpose of the four main Scrum events — sprint planning, the daily stand-up, the sprint review and the retrospective — in one short sentence each. Keep it under 120 words total."),
 ("Read the three answers side by side. Note in one or two lines where they differ — length, tone, clarity, formatting. This is your first evidence that the tool matters less than the prompt and your review.", ""),
 ("Now feel how context changes the answer. Copy the product-vision paragraph from the Tempo 2.0 brief and paste it into any one assistant with the prompt below.",
  "Here is the product vision for our app, Tempo:\n<PASTE THE TEMPO 2.0 PRODUCT VISION HERE>\nIn three bullet points, summarise what this product is for and who it serves, using only the information above. Do not invent features that are not stated."),
 ("Deliberately test the review habit: check the assistant's summary against the brief. Did it stick to what the brief actually says, or did it add something that is not there? Note anything invented — this is exactly the human-in-the-loop check you will do on every output.", ""),
 ("Write a short 'how I'll work' note for yourself and save it in your Tempo-2.0-Playbook folder: which assistant(s) you will use, and the three-step rule you will follow every time — prompt, review, own. This note opens your playbook.", ""),
 ],
 test="You have ChatGPT, Claude and Gemini signed in and responding, a Tempo-2.0-Playbook folder created, a written note comparing how the three tools answered the same agile task, and you have practised the prompt-review-own workflow — including catching whether a summary stayed true to the brief.",
 ),
 dict(
 num=2, topic=1,
 title="Write Effective Prompts and Build an Agile Prompt Library",
 objective="Learn the role-context-task-format-constraints structure for agile prompts, refine a weak prompt into a strong one, and save a reusable agile prompt library you will use for the rest of the course.",
 desc="A good AI draft starts with a good prompt, not a lucky one. In this lab you learn a simple, reliable "
 "structure for agile prompts — give the AI a role, the context, the exact task, the output format you want, "
 "and any constraints — and you see how each part changes the result. You take a deliberately weak, vague "
 "prompt and improve it one part at a time until it produces a genuinely usable draft. Then, because the same "
 "agile tasks recur every sprint, you save your best prompts as a reusable prompt library with clearly marked "
 "slots, so you (and your team) never start from a blank box again. " + PROJECT_NOTE,
 build="A reusable agile prompt library saved in your project folder — structured, slot-based prompt templates for the recurring agile tasks (user stories, backlog grooming, stand-up summary, status report, retrospective) — plus a before/after example proving a structured prompt beats a vague one.",
 services="Any assistant (ChatGPT, Claude or Gemini), the role-context-task-format-constraints prompt structure, single-change prompt edits, a saved slot-based prompt library",
 steps=[
 ("Start with a deliberately weak prompt so you can feel the difference. In any assistant, send: 'Write some user stories for a habit app.' Read the vague, generic result and keep it to compare against.", ""),
 ("Now rebuild the same request with structure. Send the prompt below and compare the result with the weak one — notice how much more usable it is.",
  "You are an experienced Agile Product Owner. Context: we are building Tempo 2.0, a habit-tracking app; a key new feature is shared team habits, where a group tracks a habit together. Task: write three user stories for this feature. Format: use the form 'As a <role>, I want <goal>, so that <benefit>', one per line. Constraints: keep each to one sentence, make them independent, and focus on the user's value, not the technical solution."),
 ("Change exactly one part and regenerate, so you can attribute the change. First change the ROLE (for example to 'a strict Agile coach who insists on INVEST'); read how the emphasis shifts.", ""),
 ("Now change only the FORMAT — ask for the same three stories as a markdown table with columns Role, Goal, Benefit, Priority. Notice format is independent of content.",
  "Re-present exactly those three user stories as a markdown table with the columns: Role | Goal | Benefit | Priority (High/Medium/Low). Do not change the stories' wording."),
 ("Now change only the CONSTRAINTS — add 'each story must be small enough to finish in one sprint, and add one acceptance criterion per story'. See how constraints tighten quality without you rewriting the whole prompt.", ""),
 ("Extract the pattern into a reusable template. Ask the assistant to help, then save the result. Paste the prompt below.",
  "Turn the effective prompt we just refined into a reusable template with clearly marked slots: [ROLE], [CONTEXT], [TASK], [FORMAT], [CONSTRAINTS]. Then create four more templates in the same slot style for these recurring agile tasks: grooming a backlog, summarising a daily stand-up from raw notes, writing a sprint status report for stakeholders, and running a retrospective. Present all five as a clean, copy-ready prompt library."),
 ("Review and save. Read each template critically — would it work on a real task? Fix anything weak, then save the five-template set as 'agile-prompt-library' in your Tempo-2.0-Playbook folder. Keep the weak-vs-structured example next to it as a reminder of why structure matters.", ""),
 ],
 test="You have a saved agile prompt library of at least five slot-based templates (user stories, backlog grooming, stand-up summary, status report, retrospective) built on the role-context-task-format-constraints structure, and a before/after example that shows a structured prompt clearly beats a vague one.",
 ),
 dict(
 num=3, topic=1,
 title="Apply Responsible, Human-in-the-Loop AI Practices",
 objective="Build a responsible-AI checklist for agile work and apply it — catching an invented 'fact', rewriting a prompt to protect sensitive data, and confirming a draft is fair, clear and owned by a human.",
 desc="Using AI in a real delivery brings real responsibilities. In this lab you build and apply the "
 "human-in-the-loop discipline that keeps AI use safe. You deliberately prompt an assistant into stating "
 "something confidently wrong (a 'hallucination') and practise catching and correcting it. You learn what "
 "never to paste into a public assistant — customer data, personal information, credentials, proprietary code "
 "— and rewrite a risky prompt to remove it. You check a draft for fairness and clarity, and you decide how "
 "your team will be transparent about what was AI-assisted. The output is a short, reusable responsible-AI "
 "checklist you keep visible for the rest of the course. " + PROJECT_NOTE,
 build="A one-page responsible-AI checklist for agile work (fact-check, protect data, be fair and clear, disclose AI use, keep a human owner) plus worked examples — a caught-and-corrected hallucination and a risky prompt rewritten to remove sensitive data.",
 services="Any assistant, fact-checking against the brief, data-safety rewriting, a fairness and clarity review, a transparency and ownership decision",
 steps=[
 ("See a hallucination for yourself. Ask an assistant a specific, checkable question it is likely to get wrong or invent, for example the prompt below. Read how confident the answer sounds.",
  "According to the official Scrum Guide, exactly how many minutes long must a daily stand-up be, and on which page is that stated? Give the exact page number."),
 ("Fact-check it. The Scrum Guide time-boxes the daily stand-up to 15 minutes but does not mandate an exact length by page number — so any confident 'page number' is invented. Note this as your first checklist rule: verify specific facts, figures and citations before you trust them.", ""),
 ("Practise data safety. Look at this risky prompt a busy Scrum Master might send: 'Here is our customer list with emails and phone numbers <pasted>, and our AWS admin password is <pasted> — write release notes.' Identify everything in it that must never go into a public assistant.", ""),
 ("Rewrite it safely. Redraft the same request so it gets the job done with no sensitive data, using the prompt below as your safe version.",
  "You are a release manager. Write concise release notes for a mobile app update that adds shared team habits, a smarter reminder engine and an insights dashboard, and fixes several reminder-reliability bugs. Use only this description — do not ask for or include any customer data, personal information or credentials. Format: a short 'New', 'Improved' and 'Fixed' list."),
 ("Check for fairness and clarity. Take any draft the AI has written for you so far and ask it to review itself with the prompt below; then read its answer critically — you, not the AI, are the judge.",
  "Review the text above for clarity and fairness: is anything ambiguous, biased, exclusionary or likely to be misread by a non-technical stakeholder? List specific issues and suggest plain, neutral rewrites. Do not change the meaning."),
 ("Decide on transparency and ownership. Write one line on how your team will note when something was AI-assisted (for example a small 'AI-assisted, reviewed by <name>' tag on drafts), and confirm the rule that a named human owns and approves every output before it is used.", ""),
 ("Assemble your responsible-AI checklist. Combine what you practised into a short, reusable checklist — fact-check specifics; never paste sensitive data; review for fairness and clarity; disclose AI assistance; a human owns and approves — and save it as 'responsible-ai-checklist' in your Tempo-2.0-Playbook. Keep it open beside you for every remaining lab.", ""),
 ],
 test="You have a saved one-page responsible-AI checklist, and you have applied it in practice: you caught and corrected an invented 'fact', you identified and removed sensitive data by rewriting a risky prompt safely, and you reviewed a draft for fairness, clarity, disclosure and human ownership.",
 ),
]
