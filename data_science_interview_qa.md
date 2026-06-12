# Data Science Interview Preparation Guide: Basic & Intermediate

This guide categorizes common interview questions into Basic and Intermediate levels to help you prepare systematically.

---

## 1. Statistics & Probability

### [Basic]
**Q1: What is the difference between Mean, Median, and Mode?**
- **Mean:** The average of all numbers (sensitive to outliers).
- **Median:** The middle value when data is sorted (robust to outliers).
- **Mode:** The most frequent value in the dataset.

**Q2: What is a Normal Distribution?**
- A bell-shaped curve where the mean, median, and mode are equal. 
- Approximately 68% of data falls within 1 standard deviation, 95% within 2, and 99.7% within 3 (Empirical Rule).

**Q3: What is the difference between Population and Sample?**
- **Population:** The entire group you want to draw conclusions about.
- **Sample:** A specific group (subset) that you collect data from.

### [Intermediate]
**Q4: Explain the Central Limit Theorem (CLT).**
- Regardless of the population's distribution, the distribution of sample means will approach a normal distribution as the sample size increases ($n \ge 30$). This allows us to perform hypothesis testing on non-normal populations.

**Q5: What is P-value and Level of Significance ($\alpha$)?**
- **P-value:** Probability of observing results as extreme as the ones obtained, assuming the null hypothesis is true.
- **$\alpha$:** The threshold (e.g., 0.05) below which we reject the null hypothesis.

**Q6: What is Bayes' Theorem?**
- It describes the probability of an event based on prior knowledge of conditions related to the event: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$.

---

## 2. Machine Learning

### [Basic]
**Q7: What is the difference between Supervised and Unsupervised Learning?**
- **Supervised:** The model is trained on labeled data (Input + Target). Examples: Linear Regression, SVM.
- **Unsupervised:** The model finds hidden patterns in unlabeled data. Examples: K-Means, PCA.

**Q8: What is Overfitting and how do you prevent it?**
- **Overfitting:** When a model learns noise in the training data and performs poorly on new data.
- **Prevention:** Cross-validation, Regularization (L1/L2), Pruning (in trees), or adding more data.

**Q9: What are the main evaluation metrics for Classification?**
- **Accuracy:** Total correct / Total predictions.
- **Precision:** $TP / (TP + FP)$ (Focus on minimizing False Positives).
- **Recall:** $TP / (TP + FN)$ (Focus on minimizing False Negatives).
- **F1-Score:** Harmonic mean of Precision and Recall.

### [Intermediate]
**Q10: Explain the Bias-Variance Tradeoff.**
- **Bias:** Error from overly simple models (Underfitting).
- **Variance:** Error from overly complex models (Overfitting).
- **Goal:** Find a balance that minimizes total error.

**Q11: How does the Random Forest algorithm work?**
- It is an ensemble method (Bagging) that builds multiple decision trees using random subsets of data and features. The final prediction is based on the majority vote (Classification) or average (Regression).

**Q12: What is the difference between L1 and L2 Regularization?**
- **L1 (Lasso):** Adds absolute value of coefficients. Can lead to feature selection (zeroing out coefficients).
- **L2 (Ridge):** Adds squared value of coefficients. Shrinks coefficients but rarely to zero.

---

## 3. Python for Data Science

### [Basic]
**Q13: What are the main data structures in Python?**
- **Lists:** Ordered, mutable, allows duplicates.
- **Tuples:** Ordered, immutable.
- **Dictionaries:** Unordered, key-value pairs.
- **Sets:** Unordered, unique elements.

**Q14: What is the difference between `list.append()` and `list.extend()`?**
- `append()` adds an element to the end.
- `extend()` adds elements from another iterable (concatenates).

### [Intermediate]
**Q15: What is the difference between `map`, `filter`, and `reduce`?**
- `map`: Applies a function to all items in an input list.
- `filter`: Creates a list of elements for which a function returns true.
- `reduce`: Performs a rolling computation to a sequential pair of values (e.g., sum of list).

**Q16: Explain List Comprehension with an example.**
- A concise way to create lists: `[x**2 for x in range(10) if x % 2 == 0]` (Squares of even numbers).

---

## 4. SQL for Data Science

### [Basic]
**Q17: What are the different types of Joins?**
- **Inner Join:** Returns records with matching values in both tables.
- **Left Join:** Returns all records from the left table and matched records from the right.
- **Right Join:** Returns all records from the right table and matched records from the left.
- **Full Join:** Returns all records when there is a match in either table.

**Q18: What is the difference between `WHERE` and `HAVING`?**
- `WHERE` filters rows before grouping.
- `HAVING` filters groups after `GROUP BY`.

### [Intermediate]
**Q19: What are Window Functions?**
- Functions that perform calculations across a set of table rows related to the current row (e.g., `ROW_NUMBER()`, `RANK()`, `LEAD()`, `LAG()`).
- Example: `RANK() OVER (PARTITION BY department ORDER BY salary DESC)`.

**Q20: How do you handle duplicate records in a table?**
- Using `DISTINCT` in a SELECT statement.
- Using `GROUP BY` on all columns.
- Using `ROW_NUMBER()` in a CTE to identify and delete duplicates where row number > 1.

---

## 5. Most Asked Data Science Interview Questions

**Q21: How do you handle imbalanced datasets?**
- **Resampling:** Oversample the minority class (e.g., SMOTE) or undersample the majority class.
- **Algorithmic approaches:** Use tree-based algorithms like Random Forest or XGBoost which often perform better on imbalanced data.
- **Cost-sensitive learning:** Assign higher penalties to misclassifications of the minority class.
- **Evaluation metrics:** Avoid using Accuracy. Use Precision, Recall, F1-Score, or AUC-ROC instead.

**Q22: Explain the difference between Bagging and Boosting.**
- **Bagging (Bootstrap Aggregating):** Trains multiple independent models (often of the same type) in parallel on random subsets of the data with replacement. The final prediction is an average or majority vote. Example: Random Forest. Reduces variance.
- **Boosting:** Trains multiple models sequentially. Each new model attempts to correct the errors made by the previous models. Example: Gradient Boosting, XGBoost. Reduces bias and variance but is more prone to overfitting.

**Q23: What is the Curse of Dimensionality and how do you solve it?**
- **Concept:** As the number of features (dimensions) increases, the volume of the feature space grows exponentially, making the data sparse. This makes it difficult for algorithms to find meaningful patterns and increases computational cost.
- **Solutions:** Feature Selection (removing irrelevant features) and Feature Extraction/Dimensionality Reduction techniques like PCA (Principal Component Analysis) or t-SNE.

**Q24: Explain Principal Component Analysis (PCA).**
- PCA is an unsupervised dimensionality reduction technique. It transforms the original features into a new set of orthogonal (uncorrelated) variables called Principal Components. These components are ordered by the amount of variance they explain in the data, allowing you to discard lower-variance components while retaining most of the information.

**Q25: Describe the steps you take in a typical Data Science project (The Data Science Lifecycle).**
1. **Business Understanding:** Define the problem, objective, and success metrics.
2. **Data Collection/Extraction:** Gather relevant data from databases, APIs, or files.
3. **Data Cleaning & Preprocessing:** Handle missing values, outliers, and format data correctly.
4. **Exploratory Data Analysis (EDA):** Visualize data, find correlations, and understand distributions.
5. **Feature Engineering:** Create new relevant features from existing data.
6. **Model Selection & Training:** Choose appropriate algorithms and train the models.
7. **Model Evaluation & Tuning:** Evaluate using appropriate metrics and tune hyperparameters (e.g., Grid Search).
8. **Deployment & Monitoring:** Deploy the model to production and monitor its performance over time.
