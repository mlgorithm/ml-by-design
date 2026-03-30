# Reviewer Packet

This packet is for external readers reviewing **Solving AI Problems**.

The goal is not to collect generic praise. The goal is to get sharp feedback that improves the manuscript before a final editorial pass.

## One-Paragraph Book Summary

**Solving AI Problems** is a problem-driven introduction to **machine learning, evaluation, and reliable AI systems** for undergraduate teaching. The book does not try to survey all of artificial intelligence. Instead, it teaches the machine-learning core of modern AI together with the habits needed to frame a real task, choose a defensible baseline, evaluate claims honestly, diagnose failures, and turn a model into a system that can be trusted in use. Its center of gravity is the full modeling arc from framing through deployment, not only algorithm catalog coverage.

## One-Sentence Pitch

**A first serious undergraduate textbook in machine learning that teaches readers how to frame tasks, justify claims, diagnose failures, and turn models into reliable AI systems.**

## Intended Shelf

The book should sit between:

- introductory machine learning texts that emphasize methods and code
- deep learning texts that emphasize architectures and optimization
- systems texts that emphasize deployment and monitoring

It is trying to win on continuity from problem framing to evidence to reliability to systems.

If the title suggests the wrong shelf to you, please treat that as a packaging risk and say so explicitly. The intended shelf is machine learning and AI systems, not a broad AI survey.

## Nearest Comparison Set

Review it against books in roughly these lanes:

- introductory machine learning texts
- deep learning texts
- machine-learning systems texts

The manuscript is not trying to beat each of those categories at its own narrow game. It is trying to be the bridge across them.

## Primary Reader

The primary reader is a bachelor-level student in computer science, data science, engineering, mathematics, or a nearby field who:

- can program in Python
- has high-school algebra and some probability maturity
- wants a first serious book on machine learning
- needs help connecting models, evidence, and deployment constraints

## What Makes The Manuscript Distinct

Reviewers should keep five intended differentiators in mind:

1. `Problem-first organization`
   Methods are introduced as answers to modeling dilemmas rather than as a catalog.
2. `Named reusable habits`
   The book teaches reusable techniques such as decision-first framing, proxy audit, representation audit, claim audit, threshold as policy, slice diagnosis, pipeline realism, and the modality-specific audits for reuse, invariance, context, and prediction time.
3. `Evidence-first teaching`
   Evaluation, error analysis, reliability, and system readiness are core technical content rather than late appendices.
4. `Model-to-system continuity`
   The same book carries students from linear models through deep learning and modality chapters into experiments, reliability review, and deployment.
5. `Durable teaching artifacts`
   Each chapter ends in a memo, card, sheet, or brief that should be reusable beyond the course.
6. `Cross-domain back-half coverage`
   The systems chapters should read as general ML-systems teaching, not as advice that works only for one education-domain language workflow.

## What Kind Of Review Is Most Helpful

Please review this as a manuscript with a specific market claim, not just as a set of chapters in isolation.

Most useful reviews do three things:

1. identify where the book is genuinely distinctive
2. identify where the manuscript still feels generic, under-argued, or mispositioned
3. identify what would block recommendation, adoption, or confidence in the manuscript

## What Reviewers Should Not Evaluate It As

Please do not review the manuscript as if it were trying to be:

- a full classical AI survey
- a theorem-first reference text
- a code cookbook built around current APIs
- a model-brand trend book
- a niche acceleration manual

## Recommended Reviewer Types

The ideal review cycle includes three reader profiles:

1. `Machine learning expert`
   Best at pressure-testing technical framing, modeling tradeoffs, and whether the method chapters are defensible.
2. `Systems or reliability reviewer`
   Best at pressure-testing Chapters 10 to 12 and the credibility of the deployment arc.
3. `Target reader or instructor`
   Best at judging teachability, chapter flow, exercise value, and whether the explanations land at the intended undergraduate level.

## What To Send To Each Reviewer

### Machine Learning Expert

Suggested packet:

- Chapter 1
- Chapter 2
- Chapter 3 or Chapter 5
- Chapter 10

Why:

- this packet tests whether the book's framing, evaluation, baseline, and experimental discipline are technically serious

### Systems Or Reliability Reviewer

Suggested packet:

- Chapter 8
- Chapter 10
- Chapter 11
- Chapter 12

Why:

- this packet tests whether the support-assistant spine, reliability framing, and systems endgame are credible rather than merely well written

### Target Reader Or Instructor

Suggested packet:

- Chapter 1
- Chapter 2
- Chapter 8 or Chapter 9
- Chapter 12

Why:

- this packet tests whether the book feels teachable, cumulative, and readable at the intended level

## Decision Questions For Every Reviewer

Ask every reviewer for a direct verdict on these:

1. Would you recommend this manuscript to its intended reader?
2. Would you consider assigning or recommending it in a course?
3. What is the main reason to say yes?
4. What is the main reason to hesitate?

## Review Questions For All Reviewers

Ask every reviewer to answer these:

1. What is the strongest genuinely distinctive feature of the book?
2. Where does the manuscript still feel conventional, generic, or textbook-flat?
3. Which chapter feels weakest relative to its importance?
4. Where does the book overclaim, under-explain, or compress too much?
5. If you had to cut one recurring idea or framework label, what would you cut?
6. Does the title, subtitle, and shelf language place the manuscript on the right shelf, or does it still invite the wrong comparison set?
7. What would make you more likely to recommend or adopt this book?
8. Which competing book would you choose instead, and why?

## Reviewer-Specific Questions

### For Machine Learning Experts

1. Do Chapters 1 to 3 teach the right habits for a first serious ML course?
2. Are the baseline and evaluation standards appropriately demanding for undergraduates?
3. Does Chapter 10 teach experimental reasoning in a way that is technically honest rather than merely stylistic?
4. Where does the manuscript flatten important tradeoffs or become too high-level?

### For Systems Or Reliability Reviewers

1. Do Chapters 10 to 12 form a coherent systems arc, or do they still read like separate topics?
2. Does Chapter 11 successfully integrate bias, robustness, privacy, and safety into one technical reliability story?
3. Does Chapter 12 teach real system design, or does it still stop too close to model evaluation?
4. Does the back half feel too dependent on the course-support assistant, or does the contrasting vision system make the systems lessons feel genuinely cross-domain?
5. Where would you raise the technical bar on deployment, monitoring, rollback, or human review?

### For Target Readers Or Instructors

1. Is the manuscript readable at a later-bachelor level without becoming shallow?
2. Which explanations feel clearest, and which still feel too compressed?
3. Do the chapter artifacts help you understand what to do, or do they feel like extra labels?
4. Does the manuscript feel broader than one education-domain case, especially in the back half?
5. Would you teach from this? If not, what is still missing?

## What Kind Of Feedback Is Most Useful

Most useful:

- specific passages or chapter sections that feel weak, unclear, overlong, or underdeveloped
- places where the teaching level is wrong for the intended audience
- places where the systems arc feels strongest or weakest
- comparisons to other books the reviewer would choose instead
- specific missing exercise, figure, or companion-material needs
- a short adoption or recommendation verdict with the main blocking issue named clearly

Less useful:

- generic praise without chapter-level detail
- requests to turn the manuscript into a full AI survey
- requests to chase current tool or vendor trends

## Suggested Reviewer Request Email

Use or adapt the note below.

> I’m looking for a sharp review of selected chapters from my book manuscript, **Solving AI Problems**. The book is a problem-driven introduction to machine learning, evaluation, and reliable AI systems for undergraduate teaching. I’m not looking for a broad AI-survey review; I’m trying to pressure-test whether the manuscript succeeds as a first serious ML text that carries readers from framing through evaluation, reliability, and deployment. If you’re willing, I’d like to send you a small packet of chapters plus a short list of focused questions. What would help me most is specific feedback on where the manuscript is genuinely distinctive, where it still feels conventional or weak, and what would most affect your willingness to recommend or adopt it.

## Internal Use: How To Process Responses

When reviews come back, sort comments into these bins:

1. `Positioning`
   The reviewer misunderstood what the book is trying to be.
2. `Teachability`
   The reviewer found the level, pacing, or artifacts weak.
3. `Technical rigor`
   The reviewer found a chapter too shallow, too compressed, or technically under-argued.
4. `Adoption risk`
   The reviewer would hesitate to assign the book because of missing exercises, solutions, visuals, or companion support.
5. `Non-goal`
   The reviewer wants the book to become a different kind of book.

This sorting matters because not every negative comment is a reason to rewrite the manuscript.
