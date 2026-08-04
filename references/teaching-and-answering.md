# Teaching and Answering Rules

## Contents

1. Self-contained teaching contract
2. Teaching chapter template
3. Answer policy by question type
4. Spoken-answer design
5. Follow-ups and recall
6. Accuracy and evidence boundaries

## 1. Self-contained teaching contract

A crash pack is a study document, not merely a syllabus. After reading a P0 chapter, the candidate should be able to:

1. define the concept plainly;
2. explain its mechanism or data flow;
3. distinguish it from the most likely alternative;
4. apply it to a JD-relevant example;
5. state one tradeoff or limitation;
6. answer the likely first follow-up.

Do not substitute “read this article” for any of these outcomes. Use external sources for verification and optional depth, not as missing body content.

## 2. Teaching chapter template

Use the smallest subset that satisfies the learning outcome; do not pad simple topics.

```markdown
### <Topic> — <priority and minutes>

**Why this will be asked**
<JD trace, project trace, round signal, or previous feedback>

**One-sentence definition**
<Plain-language definition>

**How it works**
1. <Input or trigger>
2. <Key mechanism or processing stages>
3. <Output and how it is used>

**Key distinctions**
| Concept | Difference | When it matters |
|---|---|---|

**Worked example**
<Small query, code trace, formula, diagram, data flow, or scenario>

**Tradeoffs and common mistakes**
- <Tradeoff or boundary>
- <Frequent misconception>
- <Failure or scale concern>

**60–90 second interview answer**
<Natural spoken answer in the interview language>

**Likely follow-ups**
1. <Question>
   - Reference answer: <answer>
2. <Question>
   - Reference answer: <answer>

**Closed-book check**
- Task: <explain, draw, calculate, query, or compare without notes>
- Pass condition: <observable threshold>

**Optional depth**
- <Source, exact section, minutes, payoff>
```

Prefer concrete examples that reuse the JD's domain nouns without pretending they came from the candidate's project.

## 3. Answer policy by question type

### Technical knowledge

Provide a complete reference answer. Include:

- direct conclusion;
- mechanism;
- applied example;
- tradeoff, limitation, or alternative;
- one or two follow-ups.

Do not withhold a technical answer merely because project facts are unknown.

### System design or applied case

Use this sequence:

`clarify goal and constraints → define inputs/outputs → propose components and data flow → discuss key decisions → handle failures and observability → scale variant → summarize tradeoffs`

Provide a worked approach, not a memorized architecture. State assumptions explicitly. For regulated or safety-critical cases, include auditability, access control, human review, or explainability when relevant to the JD.

### Coding, SQL, and analytical tasks

When the interview format makes them likely, provide:

- a representative prompt;
- a correct reference solution;
- reasoning or query decomposition;
- complexity, indexes, data assumptions, or edge cases as appropriate;
- one small variant for independent practice.

Avoid large take-home projects during an emergency window.

### Resume and project deep dives

Never write an unsupported first-person story as if it were true. Use:

```text
Conclusion → problem/context → my verified ownership → mechanism/action → verified evidence → tradeoff/limitation
```

Mark gaps with explicit placeholders such as:

- `[confirm personal contribution]`
- `[confirm sample size]`
- `[confirm baseline and measurement window]`
- `[choose an actual failure example]`

Offer a sample structure using fictional or clearly labeled hypothetical facts only when it helps explain the form; never blend the example into the candidate answer.

### Metrics and numeric claims

Require six checks:

1. exact metric definition;
2. baseline and comparison group;
3. sample size or observation window;
4. measurement method and data source;
5. candidate versus team attribution;
6. limitation, uncertainty, or possible confounder.

If evidence is weak, teach safe wording such as “在当时的内部测试集上观察到……” rather than upgrading it into a production claim.

### Behavioral questions

Use a real event from the evidence stores. Map the event to competencies, then prepare:

- 15 seconds: headline and result;
- 60 seconds: concise STAR with emphasis on Action;
- 120 seconds: detail, decision, result, and reflection.

Do not force every experience into STAR. Motivation, self-introduction, and technical opinions often need a conclusion-first structure instead.

### Unfamiliar technology or missing experience

Use the honest bridge:

1. **Acknowledge** the boundary precisely.
2. **Connect** adjacent verified experience.
3. **Explain** the current mental model without overstating depth.
4. **Approach** the first implementation, validation, or learning steps.

Example pattern:

> 我还没有在生产环境中使用过 X。和它最接近的经历是 Y，其中我处理过 Z。我的理解是 X 主要通过……解决……。如果需要落地，我会先用……验证，再重点检查……和……。

## 4. Spoken-answer design

Write answers for speech, not documentation. Prefer:

- conclusion in the first sentence;
- three to five logical chunks;
- short sentences and explicit transitions;
- important English term once in parentheses when useful;
- one concrete example;
- an honest final boundary or tradeoff.

Avoid:

- encyclopedic definitions;
- long lists without causal links;
- claims that sound memorized but cannot survive “why”;
- excessive English in a Chinese interview;
- unexplained acronyms;
- production claims based on tutorials or coursework.

For must-answer topics, include a 60–90 second answer. Add a 15-second version when the topic may appear as a quick follow-up. Use a 120-second version only for projects, behavioral stories, or system walkthroughs.

## 5. Follow-ups and recall

Follow-ups should test depth, not trivia. Prefer:

- why this method over an alternative;
- what fails or becomes slow;
- how the metric is defined;
- what changes at larger scale;
- how to validate correctness;
- what part the candidate personally owned;
- how to handle incomplete or noisy data.

End each P0 chapter with one closed-book task. A pass condition must be observable, for example:

- explain the mechanism in 60 seconds without notes;
- draw the data flow with all critical components;
- write a query that handles duplicates and nulls;
- compare two methods with one advantage and one limitation each;
- answer the original and one variant question at score 3/4 or above.

Provide answer keys after the task or in a collapsible/clearly separated section. Do not make the candidate mistake the answer key for a personal claim.

## 6. Accuracy and evidence boundaries

Keep these distinctions explicit:

- **Technical reference answer**: may be complete when grounded in established knowledge.
- **JD-specific inference**: label as likely or inferred.
- **Candidate answer**: may contain only resume evidence, candidate-confirmed facts, or clearly marked placeholders.
- **Company fact**: verify before use and cite when current information matters.
- **Hypothetical example**: label it and do not merge it into candidate evidence.

When facts are unstable, browse and verify them. When facts are stable and well established, prioritize a clean self-contained explanation. Never add links simply to make the pack look researched.
