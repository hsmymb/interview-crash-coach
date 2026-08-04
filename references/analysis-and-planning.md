# Analysis and Planning Rules

## Contents

1. Input normalization
2. Requirement and evidence matrix
3. Priority and teaching-depth decisions
4. Time-box and output budgets
5. Diagnostic-teaching-rehearsal pipeline
6. Project evidence and story mapping
7. Source and localization policy
8. Generalization rules

## 1. Input normalization

Maintain four separate stores:

- `jd_evidence`: responsibilities, requirements, preferences, domain, and interview clues.
- `resume_evidence`: education, skills, experience, projects, metrics, and portfolio links.
- `candidate_report`: candidate-stated skills or constraints absent from the resume.
- `interview_feedback`: stage, interviewer feedback, failed questions, and unresolved concerns from earlier rounds.

Never silently merge stores. Self-report may reduce teaching time but does not become resume evidence. Previous-round feedback must be attributable, not inferred.

For image JDs, transcribe headings and bullets before analysis. For layout-dependent resumes, preserve which role, project, date, and organization owns each bullet. When multiple resume versions exist, prefer the exact version submitted for this application.

## 2. Requirement and evidence matrix

Represent each meaningful requirement with:

| Field | Meaning |
|---|---|
| Requirement | Normalized capability or responsibility |
| JD trace | Exact phrase or close paraphrase |
| Type | Responsibility, must-have, preferred, domain, logistics |
| Role criticality | 1–5; 5 defines the role's core output |
| Resume evidence | Direct project, work, course, or skill evidence |
| Candidate report | Relevant self-assessment outside the resume |
| Prior feedback | Verified signal from an earlier round |
| Evidence status | Proven, partial, self-reported-only, missing, unknown |
| Interview likelihood | 1–5 for this round |
| Learnability | 1–5 within the available window |
| Priority | P0, P1, P2, or skip |

Determine criticality from responsibilities and dependency structure, not keyword counts. A capability mentioned once may define an entire responsibility.

Use `unknown` when the material is silent. Use `missing` only after confirmation. Label inferred interview likelihood as an inference.

## 3. Priority and teaching-depth decisions

Use this heuristic as a ranking aid, not a pseudo-precise score:

`priority signal = 0.35 × criticality + 0.25 × evidence gap + 0.20 × round likelihood + 0.15 × learnability + 0.05 × feedback signal`

Approximate evidence gap as:

- proven: 1
- partial: 3
- self-reported-only: 2 for learning, 4 for resume defense
- missing: 5
- unknown: 4 until clarified

Override the score when:

- verified previous feedback identifies the issue → raise it to P0 or P1;
- an unsupported capability is necessary for a core responsibility → P0;
- a prominent numeric or architecture claim is likely to be challenged → include project defense;
- several gaps share one mental model or exercise → combine them;
- meaningful mastery is impossible in time → teach the interview-safe minimum and boundaries.

Set teaching depth by evidence status:

| Status | Default treatment |
|---|---|
| Missing or beginner self-report | Definition, mechanism, worked example, pitfalls, spoken answer |
| Partial | Key distinctions, design choices, follow-ups, applied example |
| Proven | Claim audit, edge cases, alternatives, scale and failure probes |
| Unknown | Ask once if it changes priority; otherwise teach conservatively and mark assumption |

Do not carry more than five active learning topics. List deferred topics explicitly.

## 4. Time-box and output budgets

The line budgets are guardrails, not reasons to omit a necessary answer. Count only the main Markdown deliverable.

### Up to 3 hours: emergency

- 15 min: role thesis, evidence map, and two-question baseline probe.
- 70 min: one or two P0 teaching chapters.
- 40 min: top project and metric defense.
- 25 min: must-answer rehearsal.
- 20 min: variant retry and final recall.

Use at most two active P0 topics, 6–8 must-answer questions, and 4 likely questions. Omit stretch questions. Target roughly 150–300 lines. Do not assign a new project.

Use no more than two teaching chapters and one project defense card. Each chapter gets at most one worked example, one spoken answer, and two answered follow-ups. Keep likely questions to question plus one-line focus. If the draft exceeds about 300 lines, remove P1 exposition and likely-question explanations first; preserve P0 mechanisms and must-answer reference answers.

### 4–6 hours: half day

- 25 min: analysis, self-introduction, and baseline probe.
- 140 min: two or three P0 teaching chapters.
- 70 min: project defense and story mapping.
- 60 min: reference-answer rehearsal.
- 45 min: mock interview and retry.
- 20 min: remediation and recall page.

Use at most three active P0 topics, 10 must-answer, 6 likely, and 2 stretch questions. Target roughly 300–500 lines. Allow a small query, diagram, or code exercise when it improves explanation.

If the draft exceeds the budget, compress repeated definitions and secondary examples before cutting P0 answer keys.

### 6–10 hours: one day

- 40 min: evidence matrix and baseline mock.
- 210 min: three or four P0/P1 teaching chapters.
- 90 min: narrow proof exercise or system-design walkthrough.
- 90 min: project defense and story bank.
- 70 min: technical mock, variant retries, and error repair.
- 30 min: final recall.

Use at most four active topics, 12 must-answer, 8 likely, and 4 stretch questions. Target roughly 500–800 lines.

### 12–20 hours: two days

Day 1: diagnose, learn core gaps, build one narrow proof artifact, and audit claims.

Day 2: complete high-frequency topics, rehearse project and design answers, run two adaptive mocks, and repair only observed weaknesses.

Use at most five active topics. Keep long videos, papers, and optional coding outside the committed schedule.

### Unknown deadline

Ask once. If the user declines or says “as soon as possible,” default to four usable hours and label the assumption.

## 5. Diagnostic-teaching-rehearsal pipeline

### Diagnose

1. State the role thesis: what this hire is expected to deliver.
2. Identify the strongest evidence and the deciding risks.
3. Select the smallest P0/P1 set.
4. If time permits, ask two to five baseline questions before writing deep remediation.

### Teach

Create self-contained chapters using [teaching-and-answering.md](teaching-and-answering.md). Each scheduled block must produce an observable result: spoken explanation, query, code trace, diagram, design walkthrough, or closed-book answer.

### Rehearse

1. Ask or present the highest-probability questions.
2. Test one level deeper than the prepared first answer.
3. Record knowledge, evidence, reasoning, communication, and boundary errors.
4. Teach only the highest-impact missing piece.
5. Ask a related variant without revealing the answer.
6. Score the independent retry separately.

## 6. Project evidence and story mapping

For each likely deep-dive project, build a defense card:

1. One-sentence problem and user.
2. Candidate's exact ownership versus team ownership.
3. Data flow and architecture.
4. Hardest decision and rejected alternative.
5. Metric definition, baseline, sample, measurement, and result.
6. Failure case, limitation, and remediation.
7. What changes at ten times the data, traffic, or team scale.
8. Connection to a JD responsibility.

For numeric claims, distinguish absolute versus relative change and mean, median, percentile, or sampled measurement. Accept honest limitations; reject invented rigor.

Build a story matrix from four to six supported experiences:

| Story | Technical depth | Problem solving | Collaboration | Failure/growth | Role relevance | Facts to confirm |
|---|---:|---:|---:|---:|---:|---|

Prepare 15-, 60-, and 120-second versions only after the underlying facts are supported. A single strong story may cover several competencies.

## 7. Source and localization policy

Separate **verification sources** from **candidate-facing delivery**:

- Browse when a technical claim, API, library, company fact, or standard may have changed.
- Prefer primary documentation and papers for verification.
- Synthesize the needed content directly in the interview language.
- Do not make a P0 or must-answer section depend on an external link.
- Put optional links in an appendix with the exact section, estimated minutes, and reason to read.
- Preserve important English technical terms in parentheses when that helps recognition in code or documentation.
- Write spoken answers naturally for the interview language; do not produce literal translated documentation prose.

## 8. Generalization rules

Derive the curriculum from each JD. Do not leak NLP, graph, frontend, finance, data, or backend topics into unrelated roles.

Adapt the proof format:

- coding-heavy role → short implementation, debugging, and complexity drills;
- architecture role → constraints, diagram, data flow, tradeoffs, and failure paths;
- analytics role → SQL, metric definitions, assumptions, and business interpretation;
- ML or research role → data, evaluation, leakage, experiment design, and paper reasoning;
- product or case role → problem framing, prioritization, metrics, and worked scenarios.

Reuse the process, not a domain syllabus: evidence separation, role-critical prioritization, self-contained teaching, claim defense, typed answers, adaptive rehearsal, and error-driven remediation.
