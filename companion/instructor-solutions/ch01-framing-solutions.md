# Chapter 1 Exercise Solutions
## Framing Learning Problems

**Instructor Notes**: This chapter introduces the foundational methodology. Students often struggle with the transition from vague goals to specific learning tasks. The framing memo artifact is the most important deliverable of the entire book.

---

## **Quick Checks - Solutions**

### **1. Prediction vs. Decision [1.1]**
**Problem**: In each scenario, identify whether the system produces a prediction, makes a decision, or both:
a) Spam filter marks email with "spam probability: 0.73"  
b) Email client moves message to spam folder
c) Dashboard shows "Student risk score: 0.45"
d) System automatically sends advisor alert

**Solutions**: 
- a) **Prediction only** - outputs a score/probability
- b) **Decision only** - takes action based on some threshold
- c) **Prediction only** - displays information for human judgment  
- d) **Decision** - automated action (though based on internal prediction)

**Common Mistakes**: Students confuse displaying a score with making a decision. Emphasize that predictions need human or automated policy to become actions.

### **2. Rewrite Vague Tasks [1.2]**
**Problem**: Transform this vague request into a defensible learning task:
"Use AI to help students succeed in introductory programming"

**Model Solution**: 
**Goal**: Support timely intervention for at-risk students
**Proxy Target**: Predict probability student will miss first two major deadlines
**Acceptable Inputs**: Early assignment scores, attendance, help-session participation, lab completion times
**Excluded Inputs**: Demographics, prior academic record outside course, personal information
**Decision User**: Course instructor or TA coordinator  
**Action**: Invitation to office hours/study group, not grade penalty
**Success Metric**: Increased assignment completion rate among flagged students

**Grading Notes**: Look for specific, measurable targets rather than vague goals. Students should exclude inappropriate features and specify decision context.

### **3. Threshold Effects [1.3]**
**Problem**: A lending model outputs risk scores 0-1. Current threshold is 0.6. What happens to approval rates and risk if threshold moves to:
a) 0.4  b) 0.8

**Solution**:
- a) **Threshold 0.4**: More approvals (higher volume), higher risk (more defaults), lower precision
- b) **Threshold 0.8**: Fewer approvals (lower volume), lower risk (fewer defaults), higher precision

**Key Insight**: Threshold choice determines business/operational tradeoffs, not just model performance.

### **4. Dataset Bias Scenarios [1.4]**
**Problem**: Identify the bias pattern in each scenario:
a) Resume screening: 90% historical hires were from 5 universities
b) Medical diagnosis: Training data from one geographic region  
c) Content moderation: Annotators all native English speakers

**Solutions**:
- a) **Selection bias** - historical hiring practices don't reflect optimal candidates
- b) **Population bias** - geographic/demographic constraints limit generalization
- c) **Annotator bias** - cultural/linguistic limitations in labeling standards

**Teaching Point**: Help students distinguish different bias sources (historical, sampling, annotation, measurement).

---

## **Applied Problems - Solutions**

### **Applied Problem 1: System Description Critique [1.A]**
**Problem**: "Our AI customer service bot answers 80% of questions correctly and reduces support costs by 40%."

**Solution Framework**:
**Missing Elements**: 
- No decision context (what questions? which customers?)
- No proxy audit (correct according to whom? under what policy?)
- No acceptable inputs specified (customer data? conversation history?)
- No escalation path mentioned
- No threshold justification ("80%" optimal how?)
- No failure modes identified

**Stronger Version**: 
"Our support assistant handles routine policy questions (refunds, shipping, account) with 80% customer satisfaction using only FAQ content and order history, escalating complex/sensitive issues to human agents within 15 seconds."

**Grading Rubric**: 
- Identifies 3+ missing memo fields (3 pts)
- Suggests specific improvements (2 pts)  
- Total: 5 pts

### **Applied Problem 2: Proxy Target Comparison [1.B]**  
**Problem**: Compare these proxy targets for "identify students needing help":
- Option A: Grade on next exam < 70%
- Option B: Miss next assignment deadline
- Option C: Fail to attend next two classes

**Model Analysis**:
**Option A (Grade < 70%)**:
- *Pros*: Direct academic performance measure, clear threshold
- *Cons*: Only available after exam (too late for intervention), doesn't capture non-academic barriers
- *Timing*: Post-facto, limited intervention window

**Option B (Miss deadline)**:  
- *Pros*: Actionable timing, clear behavioral signal, intervention possible
- *Cons*: Single event may not indicate pattern, technical issues could cause false positives
- *Best for*: Time management or engagement issues

**Option C (Attendance)**:
- *Pros*: Early signal, behavioral pattern, clear measurement  
- *Cons*: May miss engaged students with scheduling conflicts, privacy concerns
- *Best for*: Engagement and connection issues

**Recommendation**: Option B with Option C as supporting signal - provides actionable timing with behavioral confirmation.

### **Applied Problem 3: Feature Inclusion Decisions [1.C]**
**Problem**: For student support system, evaluate whether to include:
- SAT scores
- First-generation college status  
- ZIP code
- Previous course performance
- Time spent on learning platform

**Solution Matrix**:

| Feature | Include? | Justification |
|---------|----------|---------------|
| SAT scores | **NO** | Irrelevant to current course performance; potential bias source |
| First-gen status | **DEPENDS** | Could enable supportive intervention but raises fairness concerns; needs policy review |
| ZIP code | **NO** | Proxy for socioeconomic status; high bias risk |
| Previous performance | **YES** | Directly relevant, actionable for academic support |
| Platform time | **YES** | Behavioral signal, actionable for engagement intervention |

**Key Principle**: Include features that are (1) relevant to current task, (2) actionable for intervention, (3) fair across student populations.

---

## **Synthesis Task: Complete Framing Memo [1.S]**

**Assignment**: Write a one-page framing memo for building an ML system to help university admissions staff identify applicants who need additional review.

**Model Solution Template**:

```
FRAMING MEMO: Admissions Review Prioritization System

DECISION AND USER: 
Admissions staff uses system to prioritize which applications need additional human review within daily review capacity (50 apps/day).

PROXY TARGET: 
Predict applications likely to benefit from expanded review (additional essays, recommendations analysis, context evaluation) rather than standard checklist review.

ACCEPTABLE INPUTS:
- Academic metrics (GPA, test scores, course rigor)
- Application completeness and timing
- Essay word counts and submission timing
- Geographic/institutional diversity factors (for context, not exclusion)

EXCLUDED INPUTS:  
- Applicant names or identifiable demographic information
- Social media or external data beyond application
- Financial aid status or ability to pay
- Legacy or donation history

COSTLIEST MISTAKE:
Missing applicants who would succeed at university but need contextual evaluation (false negatives worse than false positives given review capacity).

EVALUATION PREVIEW:
Success = increased matriculation and retention rates among reviewed applicants vs. standard process, measured after 2-year followup.

DOWNSTREAM ACTION:
Applications scored >0.7 → detailed review queue; <0.3 → standard review; 0.3-0.7 → random sampling for calibration.

REVIEW PATH:
Weekly calibration meetings with admissions staff; monthly threshold adjustment based on review capacity and outcome data.
```

**Grading Rubric (10 points total)**:
- Clear decision context and user (2 pts)
- Specific, measurable proxy target (2 pts)  
- Thoughtful feature inclusion/exclusion (2 pts)
- Realistic threshold policy (1 pt)
- Actionable evaluation plan (2 pts)
- Professional memo format (1 pt)

**Common Student Mistakes**:
1. **Vague goals**: "Improve admissions" vs. specific decision support
2. **Bias blindness**: Including demographics without considering fairness
3. **No threshold thinking**: Expecting binary accept/reject vs. review prioritization
4. **Post-hoc evaluation**: Measuring model accuracy vs. process improvement

---

## **Misconception Notes**

**Misconception 1**: "More data always improves fairness"
**Reality**: Biased data can amplify unfair patterns; data quality matters more than quantity

**Misconception 2**: "High accuracy means good system"  
**Reality**: Accuracy measured on what, for which decision, at what threshold?

**Misconception 3**: "AI should match human decisions"
**Reality**: Human decisions may be biased; AI should improve the process, not replicate it

**Misconception 4**: "Prediction equals automation"
**Reality**: Most systems should provide decision support, not automated decisions

---

## **Teaching Recommendations**

1. **Start with decision context** before discussing any models
2. **Make proxy audit concrete** with real examples of goal/proxy misalignment  
3. **Practice threshold thinking** using interactive demos
4. **Emphasize artifact creation** - framing memo is reusable skill
5. **Connect to ethics early** - bias isn't separate from technical design

**Instructor Prep Notes**: 
- Have 2-3 domain examples ready (healthcare, education, hiring)
- Prepare threshold demonstration using simple scoring scenario
- Keep bias discussion concrete and actionable, not abstract