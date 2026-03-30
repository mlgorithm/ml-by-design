# Problem-Solving Techniques

This catalog collects the manuscript's named problem-solving techniques so the book teaches a reusable way of thinking, not only chapter-local content.

The goal is not to maximize the number of labels. The goal is to keep a compact set of recurring moves that students can reuse across projects, research, and deployment work.

## Cross-cutting techniques

These should feel useful across many parts of the book.

### Decision-first framing

- Core question: What action is being supported, under what constraint, and with what cost of mistakes?
- Use when: a project begins with a vague goal or a model choice is being made too early.
- Main chapter anchor: Chapter 1.

### Proxy audit

- Core question: What real-world goal are we trying to support, and what measurable target are we actually using instead?
- Use when: labels, targets, or institutional goals may not align cleanly.
- Main chapter anchor: Chapter 1.

### Representation audit

- Core question: What information must the representation preserve for the task to be solvable at all?
- Use when: deciding whether the current features are adequate or whether the bottleneck is representational rather than algorithmic.
- Main chapter anchor: Chapter 3.

### Baseline ladder

- Core question: What is the simplest serious baseline, and what named missing structure would justify climbing to a more complex family?
- Use when: students want to jump to a larger or more fashionable model without a clean justification.
- Main chapter anchors: Chapters 2 and 3.

### Claim audit

- Core question: What exact claim does this result support, and what stronger claims remain unsupported?
- Use when: reading result tables, writing experiments, or interpreting benchmark gains.
- Main chapter anchor: Chapter 10.

### Slice diagnosis

- Core question: Where does performance fail, for whom, and with what deployment consequence?
- Use when: aggregate metrics look strong but hidden failures may matter operationally.
- Main chapter anchors: Chapters 10 and 11.

### Threshold as policy

- Core question: What workload, false-positive cost, false-negative cost, and abstention path does this threshold or operating point imply?
- Use when: turning model scores into actions.
- Main chapter anchors: Chapters 2 and 12.

### Pipeline realism

- Core question: What breaks when a notebook result becomes a real service?
- Use when: moving from offline model quality to operational system quality.
- Main chapter anchor: Chapter 12.

## AI-specific audits

These are still reusable, but they become especially important in certain modalities or workflows.

### Invariance audit

- Core question: What variation should preserve the label, and what variation should change it?
- Use when: working with vision or any task where nuisance variation and deployment sensors matter.
- Main chapter anchor: Chapter 7.

### Context audit

- Core question: How much context must be preserved, and when is retrieval or grounding required?
- Use when: working with language tasks or any workflow where local versus long-range context changes the method choice.
- Main chapter anchor: Chapter 8.

### Prediction-time audit

- Core question: What information is actually available at prediction time, and what future information must remain forbidden?
- Use when: working with forecasting, audio, time series, or any sequential pipeline.
- Main chapter anchor: Chapter 9.

### Reuse audit

- Core question: What is really being reused from pretraining, and what evidence shows that reuse rather than downstream complexity is doing the work?
- Use when: adapting embeddings, pretrained encoders, or foundation models.
- Main chapter anchor: Chapter 6.

## Editorial guidance

- Prefer reusing one of these names when it truly fits, instead of inventing a fresh label for every chapter.
- Add a new named technique only if it teaches a genuinely different reasoning move.
- A technique should help a student choose, judge, diagnose, or redesign something.
- Each technique should lead naturally to a concrete chapter artifact such as a memo, sheet, card, plan, or brief.
