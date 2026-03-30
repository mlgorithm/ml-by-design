# Positioning Memo

## Working Position

**Machine Learning by Design: From Problem Framing to Reliable Systems** is an undergraduate-first bridge text in **machine learning, evaluation, and reliable AI systems**.

It is **not** a full survey of artificial intelligence. It focuses on the machine-learning core of modern AI and on the habits required to frame, justify, stress-test, and operationalize model-based systems.

The title is broad, but the shelf is not. In metadata, proposal copy, cover copy, and reviewer outreach, the book should always be introduced with its subtitle or with an equally explicit machine-learning shelf description.

## Shelf

This book should be positioned on the shelf between:

- introductory machine learning texts that emphasize methods and code
- deep learning texts that emphasize architectures and optimization
- systems texts that emphasize deployment and monitoring

The distinctive claim is that this book teaches the **whole modeling arc**:

1. frame the decision
2. choose a defensible proxy task
3. inspect the data as evidence
4. choose a representation
5. establish a serious baseline
6. justify the claim with evaluation
7. turn prediction into a working system

## Market Gap

This manuscript is strongest when presented as the missing bridge between three existing shelves:

- `Methods-first ML texts`
  Strong on algorithms and exercises, weaker on framing, failure analysis, and deployment judgment.
- `Deep-learning texts`
  Strong on architectures and optimization, weaker on the broader discipline of evaluation, reliability, and system readiness.
- `ML systems texts`
  Strong on production concerns, but usually too late-stage or industry-specific to serve as a first serious undergraduate textbook.

The book should therefore be sold as:

- earlier and more teachable than a systems book
- broader and more deployment-aware than a standard intro ML text
- less trend-dependent than a code-first or model-brand-driven book

## Primary Reader

The primary reader is a bachelor-level student in computer science, data science, engineering, mathematics, or a nearby field who:

- can program in Python
- has high-school algebra and basic probability maturity
- wants a coherent first serious book on modern machine learning
- needs help connecting models, evidence, and real deployment constraints

## Adoption Case

The clearest adoption path is:

- a later-bachelor machine-learning course that wants stronger framing, evaluation, and reliability habits
- a first ML course for departments that do not want to split ``technical ML'' and ``responsible AI'' into separate silos
- a bridge course between introductory modeling and later systems, capstone, or project-based work

The book is also usable as:

- a companion text for instructors who want reusable chapter artifacts, discussion prompts, and design sheets
- a self-study text for strong readers who want judgment, not only recipes

## Secondary Reader

A secondary reader is an advanced secondary-school reader, mathematically mature beginner, or ambitious self-learner who wants a university-style conceptual foundation.

That audience should be served through:

- explicit prerequisite bridges
- advanced notes
- challenge exercises
- companion code

The book should **not** quietly bend the whole narrative toward acceleration for a narrow subgroup. If support for faster-track readers is important, it should be labeled as an explicit bridge or supplement.

## Core Promise

A student who finishes this book should be able to take a vague AI idea and turn it into a defensible machine-learning project or system proposal.

They should be able to answer:

- what decision is being supported
- what proxy target is being used
- what data and representation make the task visible
- what baseline deserves to be beaten
- what evidence actually supports the result
- what reliability and deployment constraints shape the final system

## Acquisition Claim

The central acquisition claim is not ``this is another introduction to AI.'' It is:

**this is a first serious machine-learning textbook that treats framing, evaluation, reliability, and deployment as one continuous technical story.**

## What Makes It Distinct

The manuscript should stand apart through five things:

1. **Problem-first organization**
   Methods appear as answers to modeling dilemmas, not as a catalog.
2. **Named reusable habits**
   Decision-first framing, proxy audit, baseline ladder, claim audit, slice diagnosis, threshold as policy, and pipeline realism are reusable tools, not chapter slogans.
3. **Evidence-first teaching**
   Evaluation, error analysis, and reliability are core technical content, not an ethics appendix.
4. **Model-to-system continuity**
   The same book carries students from linear models to deep learning to grounded language systems to experiments, reliability review, and deployment constraints.
5. **Durable teaching artifacts**
   Each chapter should leave the reader with a concrete artifact such as a memo, card, sheet, or checklist that can be reused on real projects.
6. **Cross-domain back-half proof**
   The systems chapters should not rely only on one education-domain language example; they should also cross-check the same questions against a contrasting vision system.

## Where It Wins And Where It Does Not

This positioning is strongest when it is honest about tradeoffs:

- It wins on judgment, continuity, and teachability across the full modeling arc.
- It does not aim to win on deepest mathematical coverage.
- It does not aim to win on maximum framework or API depth.
- It does not aim to win on production-platform specifics or vendor workflows.

That honesty matters because it helps the right readers and reviewers see the intended value immediately.

## What It Is Not

The book should explicitly avoid being mistaken for:

- a full classical AI survey covering search, planning, logic, robotics, and reinforcement learning in equal depth
- a code cookbook built around fast-changing APIs or vendor tools
- a theorem-first mathematical reference
- a trend book about current model brands
- a niche acceleration manual

## Language To Use

Preferred framing:

- first serious machine-learning textbook
- undergraduate-first
- problem-driven
- evaluation and reliability as core technical content
- bridge from models to systems
- machine-learning textbook with an AI-systems endgame

Language to avoid:

- broad AI survey
- comprehensive AI reference
- toolchain or platform guide
- up-to-the-minute AI trends

## Structural Consequences

This positioning implies four editorial rules:

1. Every chapter should visibly connect back to the seven-question framework.
2. Every chapter should produce a reusable chapter artifact.
3. The companion code should reinforce judgment, not just implementation.
4. Recurrent examples should show range across more than one domain, but the final arc should keep one primary running system so the closing chapters feel cumulative rather than episodic.
   The cleanest version is one primary running case plus one explicit contrast case that proves the same habits transfer.

## Packaging Consequences

Retail metadata, proposal copy, and reviewer outreach should lead with `machine learning` before `AI`.

Use forms such as:

- problem-driven machine learning
- machine-learning textbook with evaluation and reliable systems
- bridge from machine-learning models to deployed AI systems

Avoid leading metadata such as:

- introduction to AI
- AI textbook
- AI survey

## Submission Consequences

Proposal and sample-chapter packets should lead with the parts that prove the book is distinctive:

- Chapter 1 for framing and shelf signal
- Chapter 2 for evidence and evaluation discipline
- Chapter 10 or Chapter 12 for the back-half differentiator

If the packet leads only with standard method chapters, the book risks being misread as more generic than it is.

## Editorial One-Sentence Pitch

**A first serious undergraduate textbook in machine learning that teaches readers how to frame tasks, justify claims, diagnose failures, and turn models into reliable AI systems.**
