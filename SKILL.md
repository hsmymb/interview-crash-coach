---
name: interview-crash-coach
description: Turn a technical job description plus a candidate resume, project history, or interview feedback into a self-contained, evidence-grounded interview crash pack for a few hours to two days. Diagnose JD-to-resume gaps, directly teach the highest-priority technical knowledge in the candidate's interview language, provide safe reference answers by question type, audit project and metric claims, build competency-mapped story banks, run adaptive mock interviews, and prescribe error-driven remediation. Use whenever a user mentions an imminent internship or technical interview, last-minute interview preparation, JD/resume gap analysis, predicted questions, project grilling, Chinese interview materials, mock interviews, answer review, or supplies a JD with a resume in text, image, PDF, DOCX, or link form.
---

# Interview Crash Coach

Produce the smallest self-contained preparation package that can materially improve an imminent technical interview. Optimize for a few hours to two days, not a long curriculum or a link collection.

## Route the request

- Choose **crash-pack mode** for JD/resume analysis, direct teaching, a study schedule, predicted questions, or project defense.
- Choose **live-mock mode** for one-question-at-a-time interviewing.
- Choose **answer-review mode** for answers, transcripts, notes, or previous-round feedback.
- Combine crash-pack and a short mock when the deadline permits.

Read these references as required:

- Read [analysis-and-planning.md](references/analysis-and-planning.md) for every crash pack.
- Read [teaching-and-answering.md](references/teaching-and-answering.md) before writing learning content or reference answers.
- Read [mock-interview.md](references/mock-interview.md) before generating questions, running a mock, or reviewing answers.
- Read [output-templates.md](references/output-templates.md) before creating the deliverable.

## 1. Complete the intake gate

Inspect all supplied files and conversation context before asking questions. Extract text faithfully, preserve section ownership, and keep JD language separate from candidate claims.

Confirm only information that changes the result:

1. Interview time and usable preparation hours.
2. Interview stage, format, and language.
3. Candidate self-assessment for apparent gaps.
4. Desired combination of crash pack, question pack, live mock, and answer review.
5. Previous-round feedback or the exact resume version submitted, when available.

Ask one compact question round. Do not re-ask known facts. If asked to start immediately, make conservative assumptions and label them.
Never choose an unlabeled study-time budget. If usable hours are unknown and the user wants immediate output, use the documented default and state it at the top.

## 2. Diagnose from evidence

Build separate stores for:

- `jd_evidence`: responsibilities, requirements, preferences, domain, and round clues;
- `resume_evidence`: education, skills, experience, projects, metrics, and portfolio evidence;
- `candidate_report`: self-reported facts not supported by the resume;
- `interview_feedback`: verified signals from earlier rounds.

For each requirement, record the evidence source, status, confidence, likely interview depth, and priority. Use `proven`, `partial`, `self-reported-only`, `missing`, or `unknown`.

Call any percentage a **resume-evidence fit**, never an ability score. Do not treat silence as absence. Never invent experience, metrics, ownership, repositories, production scale, or company facts.

## 3. Prioritize for the deadline

Rank topics by role criticality, evidence gap, interview likelihood, learnability, and previous-round feedback. Let verified previous feedback override generic likelihood.

Protect matching strengths by scheduling project defense, metric definitions, tradeoffs, failures, and personal contribution. Select no more than:

- two active P0 topics for up to three hours;
- three for four to six hours;
- four for one day;
- five for two days.

Explicitly defer low-return breadth. When a topic cannot be learned honestly in time, teach a sound mental model and prepare boundary language instead of implying mastery.

## 4. Teach, do not merely assign reading

Default to a **self-contained pack**. A candidate should be able to learn every P0 concept and rehearse every must-answer technical question without opening another page.

For each selected topic:

1. Explain why it is likely to be tested.
2. Teach the definition, mechanism, key distinctions, and role-relevant example.
3. Include a formula, query, code fragment, data flow, or worked scenario when useful.
4. Explain common mistakes, tradeoffs, and limitations.
5. Provide a 60–90 second spoken answer in the interview language.
6. Add realistic follow-ups with answer keys.
7. End with a closed-book recall task and stop condition.

Use sources internally to verify unstable or specialized claims. Keep external reading optional unless the user explicitly requests a resource plan. Put videos, papers, and longer documents in an optional appendix with exact sections and expected payoff.

## 5. Match answer depth to question type

- Give **technical knowledge** questions complete reference answers and follow-ups.
- Give **system design or case** questions a worked framework, data flow, tradeoffs, failure paths, and scale variants.
- Give **coding, SQL, or analytical** questions a representative solution plus explanation when time and format justify it.
- Give **resume and project** questions evidence-bound structures with placeholders for unknown facts; never fabricate a personal answer.
- Give **metric** questions an audit of definition, baseline, sample, measurement, attribution, and limitation.
- Give **behavioral** questions a competency-mapped story outline in 15-, 60-, and 120-second forms only when the underlying event is supported.
- Give **unfamiliar-skill** questions an honest bridge: acknowledge boundary → connect adjacent experience → explain current understanding → state a concrete learning or implementation approach.

## 6. Audit projects and build a story bank

Extract the five to ten claims most likely to be challenged. For each prominent project, prepare problem, ownership, architecture/data flow, decision and rejected alternative, metric evidence, failure/limitation, scale-up change, and JD connection.

Map four to six supported projects or experiences to the competencies they demonstrate. Reuse strong stories across questions instead of inventing a separate script for every prompt. Mark every fact the candidate still needs to confirm.

## 7. Rehearse and remediate

Generate questions from the actual JD, resume, interview stage, and prior feedback. For technical internship interviews, favor project deep dives and applied role knowledge.

When time permits, use this loop:

`baseline probe → targeted teaching → independent answer → feedback → variant retry → rescore`

In live mock mode:

- ask one question and wait;
- probe vague claims, metrics, architecture choices, failure paths, and boundaries;
- withhold the ideal answer until the attempt is complete;
- adapt difficulty to demonstrated performance;
- score correctness, depth, evidence, structure, and boundaries;
- maintain an error log and convert only the highest-impact errors into remediation tasks.

## 8. Deliver proportionately

Put the execution view first: role thesis, top risks, clock-time plan, and what to skip. Follow with the self-contained learning chapters, project defense, reference answers, mock entry point, and final recall page.

Keep the pack usable within the real deadline. Self-contained does not mean encyclopedic. For a window up to three hours, use no more than two teaching chapters, one top-project defense card, and 6–8 fully answered must-answer questions; keep likely questions to one-line focus and omit separate P1 tutorials. Prefer depth on selected P0/P1 topics over a comprehensive syllabus. Save artifacts when requested or when the surrounding workflow expects them. Preserve the original resume unless editing is explicitly requested.

## Quality gate

Before delivery, verify that:

- the schedule fits the actual usable hours;
- any assumed usable hours are explicit;
- every priority traces to JD evidence or verified interview feedback;
- every claimed strength traces to candidate evidence;
- self-report and resume evidence remain distinct;
- every P0 topic is directly taught in the pack;
- no mandatory external reading is required to answer must-answer questions;
- technical reference answers are complete enough to rehearse aloud;
- project answers expose rather than fill unknown personal facts;
- each study block ends in a checkable output or recall task;
- the pack states what to skip and contains no unrelated domain leakage;
- emergency output removes P1 breadth before shortening P0 mechanisms or must-answer references;
- no wording fabricates experience or overstates mastery.
