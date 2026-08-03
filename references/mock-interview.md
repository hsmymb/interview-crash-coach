# Mock Interview Protocol

## Contents

1. Round-aware question construction
2. Static question pack and answer depth
3. Baseline, mock, and coaching modes
4. Adaptive follow-ups
5. Scoring and error log
6. Feedback, retry, and remediation

## 1. Round-aware question construction

Derive questions from these sources in priority order:

1. Verified feedback or unresolved concerns from earlier rounds.
2. Prominent resume claims, numbers, architecture, and personal contribution.
3. Role-defining JD responsibilities and P0/P1 gaps.
4. Applied design, coding, query, experiment, or case work appropriate to the role.
5. Motivation, company/role understanding, and honest boundary handling.

Adjust the mix by round:

| Round | Emphasis |
|---|---|
| Recruiter or HR screen | Motivation, timeline, logistics, concise fit, obvious risks |
| Technical screen | Core fundamentals, project evidence, short applied tasks |
| Project deep dive | Ownership, data flow, metrics, decisions, failures, scaling |
| Coding or SQL | Clarification, reasoning, correctness, complexity, edge cases |
| System or case | Constraints, decomposition, tradeoffs, failure handling, communication |
| Final or panel | Cross-functional judgment, consistency, values, unresolved reservations |

For an internship technical interview without a coding round, usually allocate 40–55% to resume/project deep dives, 30–40% to JD core knowledge, 10–20% to applied design or analysis, and 5–10% to motivation and boundaries.

Apply hard size limits:

| Available time | Must answer | Likely | Stretch |
|---|---:|---:|---:|
| Up to 3 hours | 6–8 | up to 4 | 0 |
| 4–6 hours | up to 10 | up to 6 | up to 2 |
| 1–2 days | up to 12 | up to 8 | up to 4 |

Rank and omit excess questions. Do not generate trivia disconnected from the work.

## 2. Static question pack and answer depth

Group questions as must-answer, likely, and stretch. For every must-answer question record:

- why it is likely;
- JD, resume, or feedback trace;
- question type;
- expected concepts or evidence;
- a suitable reference answer or evidence-bound structure;
- two realistic follow-ups;
- red flags.

Apply the answer policy from [teaching-and-answering.md](teaching-and-answering.md):

- technical knowledge → complete reference answer;
- system/case → worked framework and tradeoffs;
- coding/SQL → representative solution and reasoning;
- project/behavioral → evidence-bound structure with placeholders;
- metrics → six-part audit;
- unfamiliar topic → honest bridge.

Likely questions may use a shorter reference focus. Stretch questions can be question-only when the relevant learning chapter already contains sufficient depth.

## 3. Baseline, mock, and coaching modes

### Baseline probe

Use two to five short questions before deep teaching when time allows. Cover the highest-risk knowledge topic, top project, one metric, and one boundary. Do not score the candidate as interview-ready from resume evidence alone.

### Strict mock

Set the role, round, duration, and feedback timing. Ask one question at a time and wait. Do not coach or reveal ideal answers until the mock segment ends.

### Coaching mode

After the first failed attempt:

1. identify the missing concept without giving the final wording;
2. provide one small hint or a short teaching correction;
3. ask the candidate to answer again;
4. later ask a related variant without assistance;
5. score independent and coached attempts separately.

Use coaching mode by request or during a crash-pack rehearsal. Do not confuse coached performance with independent readiness.

## 4. Adaptive follow-ups

Choose the next move from the answer:

- vague claim → request a concrete example and personal action;
- numeric claim → ask definition, baseline, sample/window, and measurement;
- architecture claim → ask data flow, failure path, observability, and alternative;
- correct but shallow → ask why, tradeoff, or a scale variant;
- technically wrong → test one adjacent fundamental, then teach or move on;
- honest unknown → ask for reasoning and first validation steps;
- memorized answer → change the scenario or constraint;
- strong answer → probe an edge case, limitation, or rejected alternative.

Keep the tone professional and realistic. Stop when time expires or evidence is sufficient to identify the top weaknesses.

## 5. Scoring and error log

Score each independent answer from 0–4:

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Correctness | Wrong or contradictory | Partly correct | Correct and precise |
| Depth | Slogan only | Explains mechanism | Handles tradeoffs and edge cases |
| Evidence | Unsupported | General example | Specific, attributable evidence |
| Structure | Hard to follow | Understandable | Conclusion-first and concise |
| Boundaries | Bluffs | Admits a gap | States limits and a sound approach |

Not every dimension applies equally. For pure knowledge questions, do not penalize the absence of personal evidence. For project questions, evidence and attribution are essential.

Convert scores to 100 only for a session summary. Per-question notes are more valuable than a single number. Penalize fabricated ownership, metrics, or experience more heavily than an honest unknown.

Maintain an error log:

| Question | Attempt | Error type | Missing concept/evidence | Repair task | Minutes | Retry result |
|---|---:|---|---|---|---:|---|

Use error types: knowledge, project evidence, reasoning, communication, or boundary handling.

## 6. Feedback, retry, and remediation

After a strict mock, provide:

1. Interviewer verdict in two or three sentences.
2. Three strongest signals.
3. Three highest-risk signals.
4. Question-level corrections.
5. A remediation schedule that fits the remaining time.
6. A variant retry set focused on the same underlying skills.

Use this repair loop:

`identify error → teach the missing unit → candidate retries → ask a variant → rescore independent transfer`

Rewrite only representative personal answers. Let the candidate fill and retry the rest so facts remain theirs.

If less than one hour remains, prioritize dangerous misconceptions, metric definitions, the top project's ownership and architecture, self-introduction, honest gap language, and one rapid variant round.
