# Chapter 2 Exercise Solutions  
## Prediction, Loss, and Decision Rules

**Instructor Notes**: This chapter establishes evaluation discipline that prevents common ML mistakes. Students struggle most with threshold choice, calibration concepts, and train/validation/test discipline. The evaluation plan artifact forces systematic thinking before training begins.

---

## **Quick Checks - Solutions**

### **1. Metric Calculations [2.1]**
**Problem**: Given confusion matrix for binary classification (200 total examples):
```
           Predicted
Actual     0    1
   0      85   15  
   1      20   80
```
Calculate: accuracy, precision, recall, F1, false positive rate.

**Solutions**:
- **Accuracy**: (85 + 80) / 200 = 0.825
- **Precision**: 80 / (80 + 15) = 0.842  
- **Recall**: 80 / (80 + 20) = 0.80
- **F1**: 2 × (0.842 × 0.80) / (0.842 + 0.80) = 0.821
- **False Positive Rate**: 15 / (85 + 15) = 0.15

**Common Mistakes**: Confusing precision/recall denominators. Emphasize: precision = "of positive predictions, how many correct?" vs recall = "of actual positives, how many found?"

### **2. Same Accuracy, Different Usefulness [2.2]**
**Problem**: Two models both achieve 85% accuracy on email classification. Model A has precision=0.95, recall=0.75. Model B has precision=0.75, recall=0.95. Which is better for:
a) Spam detection (false positives very costly)
b) Security alerts (false negatives very costly)

**Solutions**:
- a) **Model A** - High precision means fewer legitimate emails marked as spam
- b) **Model B** - High recall means fewer genuine threats missed

**Teaching Point**: Accuracy alone doesn't capture decision costs; precision/recall tradeoffs matter for operational deployment.

### **3. Data Split Roles [2.3]**  
**Problem**: Explain why each split exists and what would go wrong without it:
- Training set
- Validation set  
- Test set

**Solution**:
- **Training**: Fit model parameters; without it, no learning occurs
- **Validation**: Tune hyperparameters, choose models; without it, overfitting to training data
- **Test**: Final unbiased evaluation; without it, overstating performance due to validation leakage

**Key Insight**: Each split protects against a different type of overfitting.

### **4. Leakage Identification [2.4]**
**Problem**: Spot leakage in this setup: "Predict patient readmission using medical records. Features include admission diagnosis, length of stay, discharge medications, and readmission status."

**Solution**: **"Readmission status"** is leakage - it's exactly what we're trying to predict! Including target variable as feature makes problem artificially easy.

---

## **Applied Problems - Solutions**

### **Applied Problem 1: Threshold Selection [2.A]**
**Problem**: A hiring model outputs scores 0-1. HR can interview 20 candidates weekly from 100 applicants. Current threshold 0.8 yields 15 interviews, 12 successful hires. Threshold 0.6 would yield 30 interviews, 18 successful hires. What threshold should they use?

**Solution Analysis**:

**Current (0.8 threshold)**:
- Interview load: 15/week (under capacity)
- Success rate: 12/15 = 80%
- Weekly hires: 12
- Precision: High, recall: Lower

**Alternative (0.6 threshold)**:  
- Interview load: 30/week (over capacity)  
- Success rate: 18/30 = 60%
- Weekly hires: 18 (but unsustainable)
- Precision: Lower, recall: Higher

**Recommendation**: **Intermediate threshold ~0.7** to get ~20 interviews/week matching capacity while optimizing hire volume within operational constraints.

**Teaching Point**: Operational constraints (interview capacity) determine optimal threshold, not just model performance.

### **Applied Problem 2: Calibration Assessment [2.B]**
**Problem**: A model predicts loan default probabilities. For applications scoring 0.6-0.7, actual default rate is 45%. For scores 0.8-0.9, actual default rate is 70%. Is this model well-calibrated?

**Solution**: 
**No, poorly calibrated**:
- 0.6-0.7 range: Predicted ~65%, Actual 45% → **Overestimating risk**
- 0.8-0.9 range: Predicted ~85%, Actual 70% → **Overestimating risk**

**Implication**: Model systematically overpredicts defaults, may reject viable applicants.

**Fix Options**: 
1. Recalibration using Platt scaling or isotonic regression
2. Threshold adjustment based on empirical calibration curve
3. Retrain with better probability estimation objective

### **Applied Problem 3: Train/Validation Curves Diagnosis [2.C]**  
**Problem**: Interpret these learning curves:
- Training accuracy: increases from 60% → 95% over epochs
- Validation accuracy: increases 60% → 78%, then decreases to 72%
- Test accuracy: 71%

**Diagnosis**: **Classic overfitting pattern**
- **Training**: Continuous improvement suggests model learning training data well
- **Validation**: Peak at 78%, then decline indicates overfitting after optimal point  
- **Test**: 71% close to validation minimum suggests realistic performance estimate

**Recommendations**:
1. **Early stopping** around validation peak (78%)
2. **Regularization** to reduce overfitting  
3. **More training data** if available
4. **Model simplification** if overfitting persists

---

## **Synthesis Task: Evaluation Plan [2.S]**

**Assignment**: Create an evaluation plan for the Chapter 1 framing memo (student support system).

**Model Solution**:

```
EVALUATION PLAN: Student Support Prioritization System

SEVEN-QUESTION FOCUS:
Supporting instructors in identifying students who would benefit from early academic intervention.

DECISION CONTEXT:  
Weekly review capacity: 5-8 students per instructor. Cost of missing struggling student >> cost of unnecessary outreach.

PRIMARY METRIC:
Recall at top-5 ranked students (operational constraint). Target: >80% of students who eventually need intervention captured in weekly review list.

SUPPORTING METRICS:
- Precision at top-5 (avoid alert fatigue) 
- Intervention success rate (improved assignment completion)
- False negative analysis (missed students who dropped/failed)

THRESHOLD POLICY:
Rank-based system: review top 5-8 students by risk score weekly, rather than fixed threshold. Allows adaptation to class size.

CALIBRATION CHECK:  
Monthly review: do students scoring 0.7 actually need intervention 70% of the time? Recalibrate if systematic bias detected.

SPLIT PROTOCOL:
- Temporal split: Train on Fall 2025, validate on Spring 2026, test on Fall 2026
- No student leakage across splits
- Evaluation after intervention outcome observable (4-6 weeks into semester)

LEAKAGE CONTROLS:
- No final grades or post-intervention data in features
- No information available after prediction time (week 3 of semester)
- Cross-semester validation to check temporal stability

BASELINE LADDER:
1. Random selection (should beat easily)
2. Prior course GPA only (domain knowledge baseline)  
3. Instructor intuition (existing process benchmark)
4. Proposed ML system

CLAIM STATEMENT:
"ML-assisted prioritization improves early intervention effectiveness compared to instructor intuition alone, measured by student success rates 6 weeks after intervention."
```

**Grading Rubric (10 points)**:
- Operationally realistic metrics (2 pts)
- Proper threshold/ranking policy (2 pts)  
- Sound split protocol with leakage controls (3 pts)
- Meaningful baseline comparisons (2 pts)
- Clear, testable claim statement (1 pt)

---

## **Challenge Exercise Solutions**

### **Challenge 1: Base Rate Shift [2.C1]**  
**Problem**: Model trained when 2% of emails were spam now deployed when 15% are spam. Performance impacts?

**Solution**: 
**Severe degradation expected**:
- **Precision drops**: More false positives as base rate increases
- **Calibration broken**: Probabilities no longer meaningful  
- **Threshold obsolete**: Original threshold now too conservative

**Fixes**: 
1. Retrain on recent data with current base rates
2. Recalibrate probabilities using recent data  
3. Adjust threshold based on new operating conditions
4. Monitor performance continuously for drift

### **Challenge 2: Evaluation Leakage [2.C2]**
**Problem**: Team splits data randomly, trains model, then realizes test set contains emails from same users as training set. What's wrong?

**Solution**: **User-level leakage** - model may memorize user-specific patterns rather than generalizable spam detection. 

**Impact**: Inflated performance estimates; poor generalization to new users.

**Fix**: Split by users, not emails - ensure no user appears in both training and test.

---

## **Common Student Misconceptions**

### **Misconception 1**: "Higher accuracy always means better model"
**Reality**: Accuracy depends on class balance and doesn't capture decision costs

**Teaching Fix**: Show examples where 90% accuracy is terrible (rare disease detection) vs. good (spam filtering)

### **Misconception 2**: "Validation set is for final evaluation"  
**Reality**: Test set is for final evaluation; validation is for model development

**Teaching Fix**: Emphasize: touch test set only once, after all development decisions made

### **Misconception 3**: "Random splits always work fine"
**Reality**: Random splits can create leakage in temporal, user, or grouped data

**Teaching Fix**: Practice identifying appropriate split strategies for different data types

### **Misconception 4**: "Model probabilities are always calibrated"
**Reality**: Most models produce poorly calibrated probabilities requiring adjustment

**Teaching Fix**: Show calibration plots for real models; demonstrate miscalibration consequences

---

## **Teaching Recommendations**

### **Active Learning Strategies**:
1. **Threshold demo**: Interactive tool showing precision/recall changes with threshold
2. **Split visualization**: Show leakage examples with real data patterns  
3. **Calibration plotting**: Students create calibration curves from model outputs
4. **Baseline challenge**: Students must beat simple baseline before trying complex models

### **Common Instructor Mistakes to Avoid**:
1. Teaching metrics in isolation without decision context
2. Skipping calibration (most students never encounter this concept)
3. Allowing random splits without checking for leakage
4. Not connecting evaluation metrics to business/operational constraints

### **Assessment Recommendations**:
- **Weekly check**: Can student explain chosen metric in decision context? 
- **Monthly artifact**: Evaluation plan for real or realistic problem
- **Semester project**: Full evaluation cycle from design through analysis

**Key Insight**: Students who master Chapter 2 thinking (metrics tied to decisions, proper splits, calibration awareness) make far fewer costly ML mistakes in practice.
