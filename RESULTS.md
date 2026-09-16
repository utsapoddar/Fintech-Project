# Results

Output of `model.py` on the ULB credit-card fraud dataset (284,807 transactions,
492 fraudulent, 0.173% positive class).

Run 16 September 2026 · Python 3.14 · pandas 3.0.1 · scikit-learn 1.8.0
Random Forest, 100 trees, `class_weight="balanced"`, stratified 80/20 split, `random_state=42`.

```
Training set: 227845 samples
Test set:     56962 samples
Fraud in train: 394 (0.17%)
Fraud in test:  98 (0.17%)

Confusion Matrix:
[[56861     3]
 [   25    73]]

Classification Report:
              precision    recall  f1-score   support

      Normal       1.00      1.00      1.00     56864
       Fraud       0.96      0.74      0.84        98

    accuracy                           1.00     56962
   macro avg       0.98      0.87      0.92     56962
weighted avg       1.00      1.00      1.00     56962
```

## Reading these numbers

Accuracy is meaningless here. Predicting "not fraud" for every transaction scores
99.83%, so the only figures worth reading are the fraud-row precision and recall.

**Precision 0.96** - of 76 transactions flagged as fraud, 73 were genuinely fraudulent
and 3 were false alarms. Low false-positive cost: few legitimate customers get blocked.

**Recall 0.74** - of 98 actual frauds, 73 were caught and **25 were missed**. That is the
real weakness, and it is the number a payments team would push on.

**The trade-off is deliberate, not incidental.** `class_weight="balanced"` already
re-weights the 0.17% positive class. Pushing recall higher means lowering the decision
threshold, which trades false negatives for false positives. Which direction is correct
depends on the relative cost of a missed fraud versus a blocked legitimate transaction,
and that is a business input this model does not have.

**Stratified splitting is not optional** at this class balance. A random split can easily
produce test folds whose fraud counts differ enough to move recall by several points.

## What would improve it

- Tune the decision threshold against an explicit cost matrix rather than accepting 0.5
- Report precision-recall AUC, which is the appropriate curve for heavy imbalance; ROC-AUC
  flatters imbalanced classifiers
- Cross-validate rather than relying on one split
- Compare against gradient boosting, which usually edges out Random Forest on this dataset
