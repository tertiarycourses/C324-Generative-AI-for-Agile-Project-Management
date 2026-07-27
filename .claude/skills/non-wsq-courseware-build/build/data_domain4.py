"""
Domain 4 — AI for Reporting, Retrospectives and Improvement. Labs 10-12.

Closes out the connected Tempo 2.0 Agile AI Playbook. With the sprint run and
tracked, these labs report and improve: Lab 10 generates stakeholder status
reports and a delivery dashboard; Lab 11 analyses velocity and metrics; Lab 12
runs an AI-assisted retrospective and turns it into a continuous-improvement plan,
completing the end-to-end playbook.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes a section of your Tempo 2.0 Agile AI Playbook, "
 "the connected project you assemble across all 12 labs."
)

DOMAIN4 = [
 dict(
 num=10, topic=4,
 title="Generate Status Reports and a Delivery Dashboard",
 objective="Use AI to turn sprint data and notes into a clear status report pitched for its reader, and to design and describe a simple delivery dashboard with the narrative that explains what the numbers mean.",
 desc="At the end of a sprint the team must tell its story to others. In this lab you use an assistant to "
 "produce reporting that is clear and honest. You feed the sprint's goal, completed and outstanding work, "
 "risks and next steps to the AI and have it draft a status report — then re-pitch it for the right reader, "
 "from a one-page stakeholder update to a three-line leadership summary. You then design a simple delivery "
 "dashboard: you ask the AI which few metrics matter (goal, scope, burndown, velocity, risks), how to lay them "
 "out, and — most importantly — to write the narrative that explains what the numbers actually mean, so a "
 "dashboard informs rather than misleads. You review every figure the AI states against your real data. " + PROJECT_NOTE,
 build="A reviewed Tempo 2.0 sprint status report pitched for its audience, and a simple delivery-dashboard design (the few metrics that matter, a layout, and the plain-language narrative that explains them) — saved as the reporting section of your playbook.",
 services="Any assistant, the status-report template from your prompt library, audience-pitched reporting, dashboard design, a metrics narrative",
 steps=[
 ("Gather your sprint data: the sprint goal, what was completed and what slipped, your risk log from Lab 8, and the burndown from Lab 7. Grab your status-report template from your prompt library.", ""),
 ("Draft the status report. Paste the prompt below with your data.",
  "You are a delivery lead writing a sprint status report for stakeholders. Here is our Tempo 2.0 Sprint 1 data:\n<PASTE GOAL, COMPLETED, OUTSTANDING, RISKS, NEXT STEPS>\nTask: write a one-page status report with these sections — Sprint goal and whether we met it, What we delivered, What is outstanding and why, Risks and mitigations, Next sprint focus. Format: clear headings and short bullets. Constraints: be honest about what slipped, use only the data given, and do not overstate progress."),
 ("Re-pitch for leadership. Ask the AI to compress the same report for executives with the prompt below.",
  "Compress that status report into a three-line leadership summary: line 1 the headline (did we meet the sprint goal), line 2 the main risk, line 3 the ask or decision needed. Keep it truthful to the full report."),
 ("Fact-check the report. Check every number and claim against your real data — completed points, dates, risk status. Correct anything the AI rounded, guessed or overstated. A status report the team cannot stand behind is worse than none.", ""),
 ("Design a delivery dashboard. Ask the AI what to show and how, using the prompt below.",
  "Design a simple one-screen delivery dashboard for the Tempo 2.0 release that a mixed audience could read at a glance. Task: recommend the few metrics that matter most (for example sprint goal status, scope completed vs planned, burndown, velocity trend, top risks), describe a clean layout for them, and say what each metric should and should not be used to conclude. Do not add vanity metrics."),
 ("Write the metrics narrative. Have the AI explain the numbers in words, then review it.",
  "Write a short narrative to sit beside the dashboard that explains what this sprint's numbers actually mean for a non-technical reader — what is going well, what to watch, and what the numbers do NOT tell us. Base it on:\n<PASTE YOUR REAL SPRINT METRICS>\nBe honest and avoid making the metrics sound better than they are."),
 ("Review and save. Confirm the dashboard would inform, not mislead, and that the narrative is honest. Save the status report, dashboard design and narrative as the reporting section of your Tempo-2.0-Playbook folder.", ""),
 ],
 test="You have a reviewed Tempo 2.0 status report with an audience-pitched leadership summary and every figure fact-checked against real data, plus a simple delivery-dashboard design with an honest narrative explaining what the metrics do and do not mean — all saved to your playbook.",
 ),
 dict(
 num=11, topic=4,
 title="Analyse Velocity and Metrics with AI",
 objective="Use AI to analyse past sprint data — velocity trend, throughput, cycle time and completion rate — to forecast realistic scope, and to interpret the metrics honestly as signals for conversation, not targets to game.",
 desc="Metrics only help if they are read well. In this lab you use an assistant as an analyst on the supplied "
 "Tempo history — several sprints of velocity and delivery data. You ask the AI to analyse the velocity trend, "
 "flag whether it is rising, falling or noisy, and forecast how much scope is realistic for the next sprints, "
 "with its assumptions stated. You have it interpret throughput, cycle time and completion rate as signals — "
 "what each suggests to talk about — and you explicitly guard against misusing them: metrics are for the team "
 "to improve, not targets to hit or sticks to beat people with. You review every calculation and reading, "
 "because a confident but wrong analysis is worse than none. " + PROJECT_NOTE,
 build="An AI-assisted analysis of the Tempo velocity and delivery metrics — a velocity-trend read, a realistic scope forecast with assumptions, and an honest interpretation of throughput, cycle time and completion rate as signals — reviewed by you and saved.",
 services="Any assistant, the sprint metrics history, velocity-trend analysis, scope forecasting, honest metric interpretation",
 steps=[
 ("Open the supplied sprint metrics history for Tempo (labs/reference-pack/) — several sprints of committed vs completed points, and any throughput or cycle-time figures. Paste it into any assistant.", ""),
 ("Analyse the velocity trend. Use the prompt below.",
  "You are an Agile delivery analyst. Here is our Tempo sprint history:\n<PASTE THE SPRINT METRICS>\nTask: analyse our velocity trend across these sprints — is it rising, falling, stable or too noisy to tell? Show the average and the range, and explain what could be driving the pattern. Constraints: state clearly if the data is too little to be reliable, and do not present a trend more confident than the data supports."),
 ("Forecast realistic scope. Ask the AI to project the next sprints with assumptions stated.",
  "Based on that velocity analysis, forecast how many story points we could realistically commit to in each of the next 2 sprints, giving a conservative and an optimistic figure. State every assumption (team availability, no major disruption, similar work type). Make clear this is a planning aid, not a promise."),
 ("Verify the maths. Recompute the average velocity yourself from the raw numbers and compare it to the AI's. If they differ, find out why. Never report a metric you have not checked.", ""),
 ("Interpret the wider metrics as signals. Use the prompt below for throughput, cycle time and completion rate.",
  "Interpret our throughput, cycle time and sprint completion rate as signals for a retrospective conversation, not as performance targets. For each metric: what a healthy pattern looks like, what our numbers might be signalling, and one question the team should discuss. Explicitly warn against any way this metric could be gamed or misused to pressure individuals."),
 ("Add the human read. Write two or three lines of your own on what the metrics really suggest for Tempo, and note one thing the numbers do not capture (for example quality, morale, or hidden rework). Metrics inform the conversation; they do not end it.", ""),
 ("Save the metrics analysis as a section of your Tempo-2.0-Playbook folder: the velocity-trend read, the scope forecast with assumptions, the signals interpretation, and your own honest commentary — ready to feed the retrospective.", ""),
 ],
 test="You have an AI-assisted metrics analysis for Tempo — a velocity-trend read you verified by re-computing the average, a scope forecast with explicit assumptions, and an honest interpretation of throughput, cycle time and completion rate as signals (not targets) — with your own commentary, saved to your playbook.",
 ),
 dict(
 num=12, topic=4,
 title="Run an AI-Assisted Retrospective and Plan Continuous Improvement",
 objective="Use AI to design a retrospective, theme the team's anonymised input into patterns, surface candid discussion points, and turn the themes into a small set of specific, owned, time-bound improvement actions — completing the end-to-end playbook.",
 desc="A sprint ends by learning from it. In this final lab you use an assistant to make a retrospective sharper "
 "and its follow-through real, while protecting the people in it. You ask the AI to design a retrospective "
 "format suited to this sprint, then feed it the team's raw, anonymised retro input and have it group and "
 "theme the feedback into patterns and surface honest discussion points — the facilitator's prep done in "
 "seconds. Crucially, you handle the input responsibly: it is anonymised and aggregated, kept inside the team, "
 "and used to find themes, never to judge individuals. From the themes the AI drafts a few specific, owned, "
 "time-bound improvement actions, which you review and commit to, and you set up a simple way to track them "
 "across sprints so the inspect-and-adapt loop actually closes. This assembles your complete Tempo 2.0 Agile "
 "AI Playbook. " + PROJECT_NOTE,
 build="An AI-assisted retrospective — a fit-for-purpose format, the team's anonymised input themed into patterns with candid discussion points, and a small set of specific, owned, time-bound improvement actions with a way to track them — completing your end-to-end Tempo 2.0 Agile AI Playbook.",
 services="Any assistant, retrospective design, anonymised theming of team input, discussion-point surfacing, improvement-action planning, continuous-improvement tracking",
 steps=[
 ("Design the retrospective. Ask the AI for a format suited to this sprint, using the prompt below.",
  "You are an Agile facilitator. Our Tempo 2.0 Sprint 1 had a strong start but slipped on the reminder-engine work and had a dependency block. Task: suggest a retrospective format suited to this sprint (for example Start/Stop/Continue, Glad/Sad/Mad, or 4Ls), with a short agenda and 4-5 good opening questions. Explain in one line why this format fits this sprint."),
 ("Prepare the input responsibly. Take the supplied raw retro input (labs/reference-pack/) and confirm it is anonymised before you use it — no names, no blame. If your own team's input had names, strip them first. Note this as the rule: retro input is aggregated and stays inside the team.", ""),
 ("Theme the feedback. Feed the anonymised input in with the prompt below.",
  "Here is the anonymised raw input from our sprint retrospective:\n<PASTE THE ANONYMISED RETRO INPUT>\nTask: group it into 4-6 themes, showing how many comments support each and summarising the point of view within each theme fairly. Format: Theme | Summary | How many mentioned it. Constraints: keep it anonymous and neutral, represent minority views too, and do not single out or infer any individual."),
 ("Surface candid discussion points. Ask the AI to turn themes into questions the team should actually discuss.",
  "From those themes, suggest 4-5 candid but constructive discussion points for the retrospective — the things the team most needs to talk about honestly to improve, phrased as questions, not accusations. Focus on the system and process, not people."),
 ("Draft improvement actions. Convert the discussion into commitments with the prompt below.",
  "Turn the top themes into a SMALL set (3-4) of improvement actions for next sprint. Each must be specific, have a suggested owner role, and be time-bound (done by when). Format: Action | Owner (role) | By when | The theme it addresses. Constraints: keep it to a few actions the team can actually do — a long list improves nothing."),
 ("Commit and set up tracking as a human. Review the actions with the team's hat on: are they genuinely doable, do they address the real themes? Adjust, assign real owners, and set up a simple tracker (a short list carried into next sprint's retro) so you can check what actually changed — closing the inspect-and-adapt loop.", ""),
 ("Assemble the complete playbook. Save the retrospective format, themed feedback, discussion points and improvement-action tracker as the final section of your Tempo-2.0-Playbook folder. Then review the whole folder end to end — toolkit, prompts, responsible-AI checklist, stories, backlog, plan, tracking, risks, docs, reports, metrics and retro — as one connected Tempo 2.0 Agile AI Playbook. This is the deliverable the course set out to build.", ""),
 ],
 test="You have an AI-assisted retrospective — a fit-for-purpose format, the team's anonymised input themed into patterns with candid discussion points, and 3-4 specific, owned, time-bound improvement actions with a tracker — handled responsibly (anonymised, no blame), and your complete end-to-end Tempo 2.0 Agile AI Playbook is assembled and reviewed.",
 ),
]
