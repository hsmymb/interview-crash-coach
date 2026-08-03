# Analysis and Planning Rules

## Contents

1. Input normalization
2. Requirement matrix
3. Priority calculation
4. Time-box profiles
5. Learning cards
6. Project evidence audit
7. Generalization rules

## 1. Input normalization

Create three separate evidence stores:

- `jd_evidence`: responsibilities, requirements, preferences, domain, interview format clues.
- `resume_evidence`: education, skills, experience, projects, metrics, portfolio links.
- `candidate_report`: skills or constraints stated by the candidate but not supported in the resume.

Never silently merge the stores. A self-reported skill may reduce study time, but it does not become resume evidence.

If a JD is an image, transcribe its headings and bullets before analysis. If a resume has layout-dependent sections, preserve which company, project, role, and date each bullet belongs to.

## 2. Requirement matrix

Represent each meaningful requirement with:

| Field | Meaning |
|---|---|
| Requirement | Normalized capability or responsibility |
| JD evidence | Exact phrase or close paraphrase |
| Type | Responsibility, must-have, preferred, domain, logistics |
| Role criticality | 1–5; 5 defines the job's core output |
| Resume evidence | Direct project, work, course, or skill evidence |
| Candidate report | Relevant self-assessment outside the resume |
| Evidence status | Proven, partial, self-reported-only, missing, unknown |
| Interview likelihood | 1–5 |
| Learnability | 1–5 within the available window |
| Priority | P0, P1, P2, or skip |

Determine role criticality from responsibilities and dependency structure, not mention counts. Example: a graph database may occur once but define an entire risk-propagation responsibility.

Use `unknown` when the resume is silent and the candidate has not answered. Do not use `missing` merely because a keyword is absent.

## 3. Priority calculation

Use this heuristic, not false precision:

`priority signal = 0.40 × criticality + 0.25 × evidence gap + 0.20 × interview likelihood + 0.15 × learnability`

Normalize inputs to 1–5. Assign evidence gap approximately as:

- proven: 1
- partial: 3
- self-reported-only: 2 for learning, 4 for resume defense
- missing: 5
- unknown: 4 until clarified

Override the score when:

- an unsupported capability is necessary to perform a core responsibility → P0;
- the topic cannot be learned meaningfully in time → prepare boundaries and an approach, not fake mastery;
- a resume claim is highly prominent or numeric → include claim defense even if it is already a strength;
- several gaps share one mental model or proof artifact → combine them.

Avoid more than five active learning topics. State the deferred topics explicitly.

## 4. Time-box profiles

### Up to 3 hours: emergency

- 15 min: role thesis and evidence map.
- 55 min: highest-return P0 topic.
- 35 min: second P0 topic or boundary answer.
- 40 min: resume project and metric defense.
- 20 min: predicted-question rapid recall.
- 15 min: mini mock and final checklist.

Do not recommend coding a new project. Produce a single compact sheet.

### 4–6 hours: half day

- 30 min: analysis and self-introduction.
- 120 min: two or three P0 learning cards.
- 60 min: project-deep-dive defense.
- 60 min: role-specific question drills.
- 45 min: mock interview.
- 15 min: remediation checklist.

Allow a tiny query, diagram, or code exercise only when it directly improves explanation.

### 6–10 hours: one day

- 45 min: evidence map and baseline mock.
- 180 min: three to four P0 topics.
- 90 min: one narrow proof artifact or system-design diagram.
- 75 min: resume defense and answer skeletons.
- 60 min: technical mock.
- 30 min: error-driven review.

### 12–20 hours: two days

Day 1: analyze, learn core gaps, build one narrow proof artifact, and audit resume claims.

Day 2: complete high-frequency topics, rehearse system design, run two adaptive mocks, and patch only observed weaknesses.

Keep optional videos and papers outside the committed schedule.

### Unknown deadline

Ask before planning. If the user refuses or says “as soon as possible,” default to a four-hour emergency plan and label the assumption.

## 5. Learning cards

Build one card per selected topic:

```markdown
### Topic — time budget

Why it will be asked: <JD trace>

Must understand:
- <3–5 concepts>

Read now:
- <official/primary resource, exact section, estimated minutes>

Produce:
- <diagram/query/explanation/answer outline>

Verify:
- <closed-book question or small task>

Interview skeleton:
- Conclusion → mechanism → project/JD application → tradeoff/boundary

If time remains:
- <video or paper>
```

Prefer documentation that can be skimmed selectively. Provide paper abstracts or sections only when the interview is likely to test research depth. Never pad a plan with courses longer than the total time window.

## 6. Project evidence audit

For each likely deep-dive project, build a defense card:

1. One-sentence problem and user.
2. Candidate's exact ownership.
3. Data flow and architecture.
4. Hardest technical choice and rejected alternative.
5. Metric definition, baseline, sample, and result.
6. Failure case and remediation.
7. What changes at ten times the scale.
8. Connection to one JD responsibility.

For numeric claims, ask whether the change is absolute or relative and whether the statistic is mean, median, percentile, or an internal sample. Accept an honest limitation; reject invented rigor.

## 7. Generalization rules

Derive the domain curriculum from the JD every time. Do not carry NLP, frontend, data, finance, or graph-specific topics into unrelated roles.

Reuse only the process:

- evidence separation;
- role-critical weighting;
- time-boxed prioritization;
- official-source learning cards;
- claim defense;
- adaptive mock and remediation.

For coding-heavy roles, include short implementation drills. For architecture roles, emphasize diagrams and tradeoffs. For analytics roles, include queries, metric definitions, and business interpretation. For research roles, include paper reasoning and experiment design.
