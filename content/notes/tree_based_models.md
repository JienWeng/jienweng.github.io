+++
title = "Tree-Based Models Explained: From Decision Trees to Random Forest and XGBoost"
description = "An intuition-first but math-heavy walkthrough from decision tree splits to bagging in Random Forests and boosting in XGBoost."
date = 2026-05-11
updated = 2026-05-11
draft = false
aliases = ["/posts/tree-based-models/"]

[taxonomies]
categories = ["2026"]
tags = ["math", "ai", "machine learning", "trees", "ensemble", "classification", "optimization"]

[extra]
topic = "Machine Learning"
lang = "en"
toc = true
comment = true
copy = true
outdate_alert = true
outdate_alert_days = 120
math = true
mermaid = false
featured = false
reaction = true
+++

A single decision tree is powerful but unstable. Nearly everything about Random Forests and XGBoost follows from that one sentence, so that is where this note starts, not at the formulas. Forests and boosting are just two different answers to the instability problem.

The path is:

$$
\text{decision rules} \to \text{decision trees} \to \text{bagging} \to \text{Random Forest} \to \text{boosting} \to \text{XGBoost}.
$$

Intuition first, but the math is written out in full. I dislike formulas that appear from nowhere.

> **Run it yourself.** The worked example is collected in a runnable notebook: [**download `tree-based-models.ipynb`**](/notebooks/tree-based-models.ipynb). It uses `numpy`, `scikit-learn`, and (optionally) `xgboost`.

## Why People Reach for Trees, Random Forests, and XGBoost

The motivation usually looks like this:

- **Linear models miss nonlinear structure.** Trees capture nonlinear, rule-like boundaries without feature engineering.
- **Single trees are unstable.** They are accurate but high-variance.
- **Random Forests stabilize trees.** Bagging reduces variance by averaging many noisy trees.
- **Boosting repairs bias.** XGBoost builds trees sequentially to correct systematic mistakes.

So the choice is not "trees vs. XGBoost". It is more like this:

- Use a **single tree** to explain a small, interpretable rule set.
- Use a **Random Forest** when you want strong performance with low tuning risk.
- Use **XGBoost** when you want maximum accuracy and can tune regularization.

## Start with the Simplest Useful Model: A Decision Rule

Imagine a classifier that uses a single rule:

$$
\text{if } x_1 \le 3.5, \text{ predict class 0, else class 1}.
$$

This is a decision stump. It is weak, but it is easy to interpret. The point is not accuracy. The point is that rules like this are already nonlinear in the raw feature space.

Now chain many rules in sequence, and you get a decision tree.

{{ figure(src="/img/notes/tree-based-models/single_split_2d.png", alt="Single split in 2D", caption="A single decision rule creates a nonlinear boundary from a linear threshold.") }}

## Decision Trees as Greedy Partitioning

A decision tree repeatedly splits the feature space into regions. Each split chooses a feature and a threshold. The goal is to make the resulting child nodes more "pure" than the parent node.

For classification, the standard impurity measures are **entropy** and **Gini**.

Entropy for a node with class proportions $p_k$ is

$$
H(S) = -\sum_{k=1}^{K} p_k \log p_k.
$$

Gini impurity is

$$
G(S) = 1 - \sum_{k=1}^{K} p_k^2.
$$

Both measures are $0$ when a node is perfectly pure and larger when it is mixed.

### Information Gain

Suppose a candidate split divides a node $S$ into children $S_L$ and $S_R$. Let $n$ be the total samples in $S$, with $n_L$ and $n_R$ in the children. The **information gain** is

$$
\text{IG}(S, \text{split}) = H(S) - \frac{n_L}{n} H(S_L) - \frac{n_R}{n} H(S_R).
$$

Using Gini, replace $H$ with $G$ in the same formula.

The tree algorithm is greedy: at each node it chooses the split that maximizes this gain.

### A Small Example

Assume a node has $10$ samples: $6$ of class 1 and $4$ of class 0. The entropy is

$$
H(S) = -\left(\frac{6}{10}\log\frac{6}{10} + \frac{4}{10}\log\frac{4}{10}\right).
$$

Now imagine a split that creates:

- Left child: $4$ class 1, $1$ class 0 ($n_L=5$)
- Right child: $2$ class 1, $3$ class 0 ($n_R=5$)

Compute $H(S_L)$ and $H(S_R)$, and you get a positive information gain. The split is not perfect, but it is better than the parent. That is enough to move the algorithm forward.

{{ figure(src="/img/notes/tree-based-models/tree_impurity_reduction.png", alt="Impurity reduction example", caption="A split is chosen because it reduces impurity, not because it is globally optimal.") }}

### Leaf Predictions

Once a node stops splitting, it becomes a leaf. For classification, the leaf prediction is

$$
\hat{p}_k = \frac{\text{count of class } k \text{ in leaf}}{\text{samples in leaf}},
$$

and the predicted class is the argmax of $\hat{p}_k$.

For regression, the leaf prediction is typically the mean:

$$
\hat{y} = \frac{1}{|S|} \sum_{i \in S} y_i.
$$

### Why Trees Are Unstable

A tree is a high-variance model. A small change in the dataset can change an early split, which changes every downstream region. Trees can overfit without strong regularization such as max depth, minimum samples per leaf, or pruning.

This is where ensembles enter the story.

## Bagging: Reduce Variance by Averaging

Bagging (bootstrap aggregating) trains many trees on different bootstrap samples of the data and averages their predictions.

Let $\hat{f}_1, \dots, \hat{f}_M$ be $M$ trees. The bagged predictor is

$$
\hat{f}_{\text{bag}}(x) = \frac{1}{M} \sum^M \hat{f}_m(x).
$$

If each tree has variance $\sigma^2$ and pairwise correlation $\rho$, then

$$
\text{Var}(\hat{f}_{\text{bag}}) = \frac{1}{M}(1-\rho)\sigma^2 + \rho\sigma^2.
$$

So averaging reduces variance, but correlation limits how much we gain.

## Random Forest: Bagging + Feature Randomness

Random Forests go one step further. They reduce correlation by forcing each split to consider only a random subset of features.

This does two things:

1. It decorrelates the trees, which reduces the $\rho$ term above.
2. It prevents strong predictors from dominating every split.

The forest prediction is still an average (regression) or a majority vote (classification). The math is the same as bagging, but the diversity is higher.

{{ figure(src="/img/notes/tree-based-models/random_forest_bagging.png", alt="Bootstrap aggregation", caption="Random Forests reduce variance by averaging many decorrelated trees.") }}

## Boosting: Reduce Bias by Building Sequentially

Bagging attacks variance. Boosting attacks bias.

The idea is to build an additive model that corrects its own mistakes:

$$
\hat{y}^{(t)}(x) = \hat{y}^{(t-1)}(x) + f_t(x),
$$

where each $f_t$ is a small tree and the sequence is trained to reduce a loss function.

Boosting is best understood as **functional gradient descent**: we are minimizing a loss by moving in function space, one tree at a time.

## XGBoost: Boosting with a Second-Order Objective

XGBoost formalizes this with an objective that includes regularization. At step $t$:

$$
\mathcal{L}^{(t)} = \sum_{i=1}^n l\left(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)\right) + \Omega(f_t),
$$

where $l$ is the training loss and the regularization term is

$$
\Omega(f) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^{T} w_j^2.
$$

Here $T$ is the number of leaves and $w_j$ is the score assigned to leaf $j$.

### Second-Order Approximation

Let

$$
g_i = \partial_{\hat{y}} l(y_i, \hat{y}_i^{(t-1)}),
$$

$$
h_i = \partial_{\hat{y}}^2 l(y_i, \hat{y}_i^{(t-1)}).
$$

Using a second-order Taylor expansion around $\hat{y}_i^{(t-1)}$, the objective becomes

$$
\tilde{\mathcal{L}}^{(t)} = \sum_{i=1}^n \left[g_i f_t(x_i) + \frac{1}{2} h_i f_t(x_i)^2\right] + \Omega(f_t).
$$

Because a tree predicts a constant weight $w_j$ for all samples in leaf $j$, we can group terms per leaf. Let $I_j$ be the indices in leaf $j$ and define

$$
G_j = \sum_{i \in I_j} g_i, \qquad H_j = \sum_{i \in I_j} h_i.
$$

Then the optimal leaf weight is

$$
w_j^* = -\frac{G_j}{H_j + \lambda},
$$

and the best value of the objective for that leaf is

$$
-\frac{1}{2} \frac{G_j^2}{H_j + \lambda}.
$$

### Split Gain

A split is good if it improves the objective. The gain of splitting a node into left and right children is

$$
\text{Gain} = \frac{1}{2}\left(\frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{G^2}{H + \lambda}\right) - \gamma.
$$

This is the exact reason XGBoost splits where it does. The split is not only about purity. It is about how much the second-order objective improves after regularization.

{{ figure(src="/img/notes/tree-based-models/xgboost_gain_split.png", alt="XGBoost split gain", caption="XGBoost chooses splits by maximizing second-order gain with regularization.") }}

## Why XGBoost Works So Well

The success of XGBoost is not a mystery. It is the combination of:

- **Sequential correction:** each tree targets the remaining error.
- **Second-order curvature:** Hessians stabilize the optimization.
- **Regularization:** the $\gamma$ and $\lambda$ terms actively penalize complexity.
- **Shrinkage:** a learning rate scales each tree so the model does not overreact.

In practice, these ideas mean the model stays expressive without exploding in variance.

{{ figure(src="/img/notes/tree-based-models/boosting_stages.png", alt="Boosting stages", caption="Boosting builds an additive model one small tree at a time.") }}

## A Few Practical Tradeoffs

Tree ensembles are strong, but their strengths are specific:

- **Interpretability:** single trees are readable, forests and boosted trees are not.
- **Bias vs variance:** Random Forests reduce variance, boosting reduces bias.
- **Overfitting:** deep trees can overfit, especially in boosting without regularization.
- **Data leakage:** trees can memorize target leakage quickly, so features must be clean.
- **Class imbalance:** impurity is dominated by the majority class unless weighted.
- **Compute cost:** XGBoost is fast for trees, but still heavier than linear models.

## A Worked Dataset Example (Synthetic Regression)

To make this concrete, we use a small synthetic regression dataset from scikit-learn. It is numeric, quick to run, and avoids any external downloads. The idea is to compare a single tree, a Random Forest, and XGBoost on the same train/test split.

{{ figure(src="/img/notes/tree-based-models/regression_overview.png", alt="Regression dataset overview", caption="A synthetic regression dataset with noise and nonlinear structure.") }}

Below is a compact code snippet. The [full notebook](/notebooks/tree-based-models.ipynb) is provided separately so you can run it end-to-end.

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

try:
	from xgboost import XGBRegressor
except ImportError:
	XGBRegressor = None

X, y = make_regression(n_samples=2000, n_features=12, noise=15.0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.2, random_state=42
)

tree = DecisionTreeRegressor(max_depth=4, random_state=42)
rf = RandomForestRegressor(n_estimators=300, random_state=42)

models = {"tree": tree, "rf": rf}
if XGBRegressor is not None:
	xgb = XGBRegressor(
		n_estimators=400,
		max_depth=4,
		learning_rate=0.05,
		subsample=0.8,
		colsample_bytree=0.8,
		reg_lambda=1.0,
		random_state=42,
	)
	models["xgb"] = xgb

for name, model in models.items():
	model.fit(X_train, y_train)
	preds = model.predict(X_test)
	rmse = np.sqrt(mean_squared_error(y_test, preds))
	mae = mean_absolute_error(y_test, preds)
	print(name, "rmse", round(rmse, 3), "mae", round(mae, 3))
```

{{ figure(src="/img/notes/tree-based-models/model_comparison_bars.png", alt="Model comparison", caption="RMSE and MAE comparison across a single tree, Random Forest, and XGBoost.") }}

{{ figure(src="/img/notes/tree-based-models/feature_importance.png", alt="Feature importances", caption="Feature importance comparison for Random Forest and XGBoost.") }}

## What Code to Look At

If you want to read real implementations, start here:

- `sklearn.tree.DecisionTreeClassifier` for tree splits, impurity, and pruning logic.
- `sklearn.ensemble.RandomForestClassifier` for bagging and feature subsampling.
- `xgboost.XGBClassifier` for second-order boosting with regularization.

## The Big Picture

We started with simple decision rules. That gave us decision trees.

Decision trees are powerful but unstable, so we average them. That gives us bagging, and then Random Forests.

Random Forests reduce variance but still leave bias on the table, so we build trees sequentially to correct errors. That gives us boosting, and XGBoost.

Trees define nonlinear partitions, bagging stabilizes them, boosting makes them accurate. That is the whole story, and every formula above is one of those three moves written out.

At some point I may extend the notebook with hyperparameter tuning and a multi-class example. If you want that sooner, leave a comment.
