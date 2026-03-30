# Chapter 8 Exercise Solutions
## Language: Context and Grounding  

**Instructor Notes**: This chapter introduces the context audit methodology - one of the book's most innovative contributions to NLP education. Students often jump to complex models without understanding what linguistic structure their task actually requires. The context audit flowchart forces systematic analysis before architecture selection.

---

## **Quick Checks - Solutions**

### **1. Representation Choice [8.1]**
**Problem**: For each task, identify minimum sufficient representation:
a) Email spam detection based on sender reputation and keyword lists
b) Sentiment analysis: "The movie was not bad" vs "The movie was not good"  
c) Chatbot response: "Book me a flight to Paris next Tuesday"
d) Document similarity for legal case matching

**Solutions**:
- a) **Bag-of-words sufficient** - No order dependency, keyword presence matters most
- b) **Local order required** - Negation ("not bad" ≠ "not good") requires bigram+ awareness
- c) **Sequence + entity extraction** - Need slot filling ("Paris", "Tuesday") plus intent recognition
- d) **Dense representation + similarity** - Semantic similarity beyond keyword overlap

**Teaching Point**: Match representation complexity to task requirements; don't over-engineer.

### **2. Identical BOW, Different Meaning [8.2]**  
**Problem**: Create two sentences with identical bag-of-words but opposite meanings for a movie review task.

**Model Solution**:
- Sentence A: "This movie is not boring but exciting"
- Sentence B: "This movie is not exciting but boring"

**BOW**: {this, movie, is, not, boring, but, exciting} (identical)
**Meanings**: Positive vs. Negative (opposite)

**Key Insight**: Word order and syntactic structure carry critical meaning that bag-of-words discards.

### **3. Local vs. External Grounding [8.3]**
**Problem**: Categorize these NLP tasks:
a) Spell checking  
b) Fact verification ("Paris is the capital of Germany")
c) Grammar correction
d) Question answering about current events

**Solutions**:
- a) **Local order** - Requires context for disambiguation but not external knowledge
- b) **External grounding** - Requires world knowledge beyond input text  
- c) **Local order** - Syntactic rules, no external facts needed
- d) **External grounding** - Current events require up-to-date knowledge base

### **4. High Probability ≠ True [8.4]**
**Problem**: Explain why language models can assign high probability to false sentences: "The Eiffel Tower is located in London."

**Solution**: 
Language models learn **statistical patterns** from text, not **truth values**. High probability indicates:
- Syntactically well-formed sentence  
- Common word combinations ("Eiffel Tower", "located in")
- Frequent sentence patterns

**But doesn't guarantee**:
- Factual accuracy
- Real-world correspondence  
- Logical consistency

**Implication**: Fluency ≠ accuracy; grounding requires external knowledge verification.

---

## **Applied Problems - Solutions**

### **Applied Problem 1: Context Audit for Document Q&A [8.A]**
**Problem**: Design a context audit for a system answering questions about university policies using official documents.

**Model Context Audit**:

**Token Presence**: 
- ✅ Insufficient - Questions like "What is the refund policy?" require semantic matching beyond keywords

**Local Order**:  
- ✅ Required - Negations ("Students may NOT submit after deadline"), conditionals ("IF enrolled full-time")

**Long-Range Context**:
- ✅ Critical - Policies have dependencies ("As stated in Section 3.2..."), cross-references

**External Knowledge**:
- ✅ Essential - Need current policy database, document versioning, effective dates

**Dialect/Register Variation**:
- ⚠️ Moderate concern - Formal policy language vs. student casual questions ("Can I get money back?")

**Output Requirements**:
- **Extractive preferred** - Quote exact policy text with citations
- **Fallback to human** - For ambiguous or high-stakes questions (grade appeals, disciplinary)

**System Architecture Implications**:
- Retrieval-augmented architecture required
- Citation and source tracking essential  
- Confidence scoring for escalation decisions
- Regular policy update synchronization

### **Applied Problem 2: Retrieval Metrics [8.B]**
**Problem**: Document retrieval system returns 4 documents for query. Relevance labels: [0, 1, 0, 1]. Collection has 3 total relevant documents. Calculate precision@2, recall@4, reciprocal rank.

**Solution**:
**Returned**: [Irrelevant, Relevant, Irrelevant, Relevant]  
**Total relevant in collection**: 3

**Precision@2**: 
- Top 2 results: [0, 1] → 1 relevant out of 2 returned
- P@2 = 1/2 = 0.50

**Recall@4**:
- All 4 results: [0, 1, 0, 1] → 2 relevant found out of 3 total  
- R@4 = 2/3 = 0.67

**Reciprocal Rank**:
- First relevant document at position 2
- RR = 1/2 = 0.50

**Interpretation**: System finds relevant documents but ranks irrelevant ones highly; needs ranking improvement.

### **Applied Problem 3: Auto vs. Escalation Decision [8.C]**
**Problem**: Classify these student messages for automatic response vs. human escalation:
a) "When is the final exam?"
b) "I was hospitalized and missed three exams"  
c) "How do I reset my password?"
d) "I think my grade was calculated incorrectly"

**Solution Framework**:

**Auto-Response Candidates**:
- a) **Final exam timing** - Factual, policy-based, low stakes
- c) **Password reset** - Technical, standard procedure, low stakes

**Human Escalation Required**:
- b) **Medical absence** - High stakes, requires documentation review, policy judgment
- d) **Grade dispute** - Requires record review, subjective evaluation, potential consequences

**Decision Criteria**:
- **Auto**: Factual queries answerable from policy/FAQ, low-stakes outcomes
- **Escalate**: Personal circumstances, grade-related issues, policy exceptions, high-stakes decisions

**System Design Implication**: Conservative escalation policy protects students while reserving automation for routine queries.

---

## **Challenge Exercises - Solutions**

### **Challenge 1: Bigram Necessity Proof [8.C1]**  
**Problem**: Prove algebraically that identical unigram distributions don't guarantee identical bigram distributions.

**Proof by Counterexample**:
- Text A: "good movie bad acting" = [good, movie, bad, acting]  
- Text B: "bad movie good acting" = [bad, movie, good, acting]

**Unigram counts**: Both have {good:1, movie:1, bad:1, acting:1} → **Identical distributions**

**Bigram counts**:
- Text A: {(good,movie):1, (movie,bad):1, (bad,acting):1}
- Text B: {(bad,movie):1, (movie,good):1, (good,acting):1}

→ **Different bigram distributions despite identical unigram distributions** ∎

**Implication**: Unigram success doesn't preclude bigram improvements; order information provides additional signal.

### **Challenge 2: Retrieval vs. Prompting Evidence [8.C2]**
**Problem**: How would you evaluate evidence that retrieval (not prompting) causes performance gains in RAG systems?

**Experimental Design**:

**Control Conditions**:  
1. **Baseline**: Model with prompts only, no retrieval
2. **Retrieval**: Model + retrieval + prompts  
3. **Retrieval-ablation**: Model + random documents + prompts
4. **Perfect retrieval**: Model + gold-standard documents + prompts

**Key Comparisons**:
- **Retrieval vs. Baseline**: Overall system benefit
- **Retrieval vs. Retrieval-ablation**: Benefit from relevant (not random) documents  
- **Perfect retrieval vs. Retrieval**: Upper bound on retrieval quality impact

**Evaluation Metrics**:
- Task accuracy (answer correctness)
- Answer attribution (citations to retrieved docs)
- Hallucination rate (inconsistent with retrieved evidence)

**Expected Result**: If retrieval causes gains, should see: Baseline < Retrieval-ablation < Retrieval < Perfect retrieval.

**Controls**: Same prompts, same model, only retrieval mechanism varies.

---

## **Synthesis Task: Context-and-Grounding Card [8.S]**

**Assignment**: Complete a context audit and grounding analysis for a legal document chatbot.

**Model Solution**:

```
CONTEXT-AND-GROUNDING CARD: Legal Document Assistant

TASK SCOPE:
Answer questions about contract terms, legal procedures, and regulatory compliance using firm's document database.

CONTEXT AUDIT:
✓ Token presence: Insufficient (legal queries require semantic understanding)
✓ Local order: Critical (negations, conditionals, legal phrasing)  
✓ Long-range context: Essential (cross-references, definitions, precedents)
✓ External knowledge: Required (current law, case updates, jurisdiction-specific rules)
✓ Dialect/register: High variation (legal jargon → client plain language)

OUTPUT REQUIREMENTS:
- Extractive with citations (exact text + document source)
- Confidence scoring for escalation decisions
- Plain language summaries with technical source material
- Explicit uncertainty acknowledgment for edge cases

GROUNDING STRATEGY:
- Primary: Firm document database (contracts, memos, policies)
- Secondary: Legal databases (case law, statutes) with date verification  
- Fallback: Attorney escalation for novel/high-stakes questions

QUALITY CONTROLS:
- Citation accuracy verification
- Legal reviewer spot-checks on automated responses
- User feedback loop for answer quality
- Regular legal database synchronization

FAILURE MODES & MITIGATIONS:
- Outdated law: Date-stamp all sources, flag old references
- Jurisdictional errors: Explicit jurisdiction modeling
- Unauthorized practice: Clear disclaimers, attorney escalation paths
- Hallucination: Require citations for all factual claims

EVALUATION CRITERIA:
- Citation accuracy: 95%+ of automated responses include correct source attribution  
- Attorney satisfaction: 80%+ of escalated cases deemed appropriate  
- Client comprehension: Plain-language summaries rated understandable by non-lawyers
- Risk mitigation: Zero instances of incorrect legal advice on high-stakes matters
```

**Grading Rubric (10 points)**:
- Complete context audit with justification (3 pts)
- Appropriate output format and grounding strategy (2 pts)  
- Realistic quality controls and failure mode analysis (3 pts)
- Domain-appropriate evaluation criteria (2 pts)

---

## **Common Student Misconceptions** 

### **Misconception 1**: "More complex models are always better"
**Reality**: Simple models often work when linguistic structure requirements are minimal

**Teaching Fix**: Show examples where bag-of-words beats transformers due to task mismatch or data limitations

### **Misconception 2**: "High perplexity means the model is bad"  
**Reality**: Perplexity measures predictability, not task performance or truthfulness

**Teaching Fix**: Demonstrate high-perplexity but task-appropriate outputs vs. low-perplexity but task-irrelevant ones

### **Misconception 3**: "Language models understand meaning"
**Reality**: Models learn statistical patterns; "understanding" requires careful definition

**Teaching Fix**: Show fluent but nonsensical completions; distinguish correlation from comprehension

### **Misconception 4**: "Retrieval always improves accuracy"  
**Reality**: Poor retrieval can introduce noise; retrieval quality matters more than retrieval presence

**Teaching Fix**: Demo with high-quality vs. low-quality retrieved documents

---

## **Teaching Recommendations**

### **Interactive Demonstrations**:
1. **Context audit walkthrough**: Live analysis of student-proposed NLP tasks
2. **Retrieval comparison**: Same questions with/without grounding documents
3. **Negation examples**: Show where bag-of-words fails, n-grams succeed
4. **Grounding failures**: Examples of fluent but factually incorrect generations

### **Assessment Strategies**:
- **Context audit practice**: Students analyze 3-4 NLP tasks using flowchart
- **Grounding evaluation**: Compare responses with/without source citations
- **Failure analysis**: Identify why a deployed NLP system failed using chapter frameworks

### **Connection to Earlier Chapters**:
- **Chapter 1**: NLP tasks need same framing discipline as any ML problem
- **Chapter 2**: Evaluation metrics change based on output type (classification vs. generation)
- **Chapter 7**: Similar invariance principles apply (linguistic vs. visual)

**Key Pedagogical Insight**: The context audit methodology transfers beyond NLP - students can apply similar systematic analysis to any representation choice problem.