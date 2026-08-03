# Mock Interview Protocol

## Contents

1. Question construction
2. Static question pack
3. Live mock
4. Scoring
5. Feedback and remediation

## 1. Question construction

Construct questions from four pools:

1. **Resume deep dive (40–55%)**: prominent projects, numeric claims, architecture, contribution, failures, tradeoffs.
2. **JD core knowledge (30–40%)**: role-defining requirements and priority gaps.
3. **Applied design or coding (10–20%)**: system design, debugging, query, algorithm, experiment, or case analysis appropriate to the role.
4. **Motivation and boundary (5–10%)**: why the role, learning gap, honest handling of unfamiliar topics.

Adjust the mix to the stated format. For an internship technical interview with no coding round, favor project deep dives and applied concepts.

Apply a hard size limit:

| Available time | Must answer | Likely | Stretch |
|---|---:|---:|---:|
| ≤3 hours | 6–8 | ≤4 | 0 |
| 4–6 hours | ≤10 | ≤6 | ≤2 |
| 1–2 days | ≤12 | ≤8 | ≤4 |

If more questions are plausible, rank and omit them. A short pack that is rehearsed beats a comprehensive pack that is merely read.

For each question, record privately or in a static pack:

- why it is likely;
- evidence source in JD or resume;
- expected concepts;
- two follow-ups;
- red flags;
- concise answer structure.

Do not create trivia that is disconnected from the work.

## 2. Static question pack

Group questions by probability:

- **Must answer**: direct resume claims and job-defining topics.
- **Likely**: adjacent fundamentals and design tradeoffs.
- **Stretch**: deeper topics or preferred qualifications.

For each must-answer question, provide an answer skeleton rather than a fabricated full answer:

`Conclusion → context → mechanism/action → metric/evidence → tradeoff or limitation`

Mark facts the candidate must fill in. Never fill sample sizes, personal ownership, baselines, or production details without evidence.

Keep likely and stretch questions to the question plus one-line focus. Do not provide full tutorials inside the question pack; point back to the relevant learning card.

## 3. Live mock

Start with a brief interviewer frame: role, round, expected duration, and feedback timing.

Then:

1. Ask one question and wait.
2. Choose the next move from the answer:
   - vague answer → ask for a concrete example;
   - numeric claim → ask for definition, baseline, and measurement;
   - architecture claim → ask for data flow, failure path, and alternative;
   - correct but shallow → ask “why” or a scaling variant;
   - incorrect → test adjacent fundamentals once, then move on;
   - honest unknown → ask how the candidate would reason or learn.
3. Avoid coaching during the mock unless the user requests coaching mode.
4. Keep questions realistic and professional, not adversarial theater.
5. Stop when the scheduled time expires or the evidence is sufficient to identify the top three weaknesses.

In coaching mode, give a short hint after the first failed attempt and ask the candidate to retry. Score the final independent attempt separately from the coached attempt.

## 4. Scoring

Score each answer from 0–4 on five dimensions:

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Correctness | Wrong or contradictory | Partly correct | Correct and precise |
| Depth | Slogan only | Explains mechanism | Handles tradeoffs and edge cases |
| Evidence | Unsupported | General example | Specific, attributable evidence |
| Structure | Hard to follow | Understandable | Conclusion-first and concise |
| Boundaries | Bluffs | Admits gaps | States limits and a sound approach |

Convert to 100 only for the session summary. Keep per-question notes more useful than the number.

Penalize heavily for fabricated ownership, metrics, or experience. Do not penalize an honest unknown as harshly as confident misinformation.

Maintain an error log:

| Question | Error type | Missing concept/evidence | Repair task | Minutes |
|---|---|---|---|---:|

Use error types: knowledge, project evidence, reasoning, communication, or boundary handling.

## 5. Feedback and remediation

After the mock, deliver:

1. Interviewer verdict in two or three sentences.
2. Three strongest signals.
3. Three highest-risk signals.
4. Question-level corrections without rewriting the candidate into someone else.
5. A remediation schedule that fits the time remaining.
6. A second-round focus list.

Rewrite only one or two representative answers. Ask the candidate to produce the rest using the pattern, then rescore.

If less than one hour remains, prioritize:

- correcting dangerous misconceptions;
- defining resume metrics;
- stabilizing the self-introduction and top project;
- rehearsing honest gap language;
- one final rapid mock.
