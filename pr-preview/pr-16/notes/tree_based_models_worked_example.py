# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Tree-Based Models Worked Example
#
# This notebook follows the note and implements a worked regression example with decision trees, Random Forests, and XGBoost. It also defines the gradients and Hessians used in XGBoost for a squared error loss.
#
# Sections:
# 1. Define loss gradients and Hessians.
# 2. Load and inspect a regression dataset.
# 3. Train XGBoost with a custom objective.
# 4. Train a Random Forest baseline.
# 5. Compare metrics and predictions.
# 6. Add visualization placeholders.
#

# %% [markdown]
# ## 1. Define Loss Gradients and Hessians
#
# We use squared error loss $l(y, \hat{y}) = \frac{1}{2}(y-\hat{y})^2$ so that:
#
# $$
#  g_i = \partial_{\hat{y}}\,l\left(y_i, \hat{y}_i^{(t-1)}\right) = \hat{y}_i^{(t-1)} - y_i,
#  \qquad
#  h_i = \partial_{\hat{y}}^2\,l\left(y_i, \hat{y}_i^{(t-1)}\right) = 1.
# $$
#

# %%
import numpy as np


def squared_error_grad_hess(y_true, y_pred):
    """Return gradients and Hessians for squared error loss."""
    grad = y_pred - y_true
    hess = np.ones_like(grad)
    return grad, hess


# Quick sanity check
_y = np.array([3.0, -1.0, 2.0])
_yhat = np.array([2.5, -2.0, 2.5])
_g, _h = squared_error_grad_hess(_y, _yhat)
_g, _h

# %% [markdown]
# ## 2. Load and Inspect Example Dataset
#
# We use a synthetic regression dataset with nonlinear structure so trees have something meaningful to learn.

# %%
import pandas as pd
from sklearn.datasets import make_friedman1
from sklearn.model_selection import train_test_split

X, y = make_friedman1(n_samples=2500, n_features=12, noise=1.0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("X shape:", X.shape)
print("y shape:", y.shape)

pd.DataFrame({"y": y}).describe()

# %% [markdown]
# ## 3. Train XGBoost with Custom Objective (Derivatives)
#
# If `xgboost` is not installed, run the next cell. Otherwise you can skip it.

# %%
# Optional: install xgboost if needed
# # %pip install xgboost

# %%
import warnings

try:
    import xgboost as xgb
except Exception as exc:
    xgb = None
    warnings.warn(f"XGBoost not available: {exc}")

xgb_preds = None
xgb_model = None

if xgb is not None:
    def squared_error_obj(preds, dtrain):
        labels = dtrain.get_label()
        grad = preds - labels
        hess = np.ones_like(grad)
        return grad, hess

    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    params = {
        "max_depth": 4,
        "eta": 0.05,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "objective": "reg:squarederror",
        "eval_metric": "rmse",
        "seed": 42,
    }

    xgb_model = xgb.train(
        params,
        dtrain,
        num_boost_round=400,
        obj=squared_error_obj,
        evals=[(dtrain, "train"), (dtest, "test")],
        verbose_eval=False,
    )

    xgb_preds = xgb_model.predict(dtest)

xgb_preds is not None

# %% [markdown]
# ## 4. Train Random Forest Baseline

# %%
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

models = {}

models["tree"] = DecisionTreeRegressor(max_depth=4, random_state=42)
models["rf"] = RandomForestRegressor(n_estimators=300, random_state=42)

for name, model in models.items():
    model.fit(X_train, y_train)

rf_preds = models["rf"].predict(X_test)
rf_preds[:5]

# %% [markdown]
# ## 5. Compare Metrics and Predictions

# %%
from sklearn.metrics import mean_squared_error, mean_absolute_error

results = []

for name, model in models.items():
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)
    results.append({"model": name, "rmse": rmse, "mae": mae})

if xgb_preds is not None:
    rmse = np.sqrt(mean_squared_error(y_test, xgb_preds))
    mae = mean_absolute_error(y_test, xgb_preds)
    results.append({"model": "xgb", "rmse": rmse, "mae": mae})

metrics_df = pd.DataFrame(results).sort_values("rmse")
metrics_df

# %%
pred_table = pd.DataFrame({
    "y_true": y_test,
    "tree": models["tree"].predict(X_test),
    "rf": models["rf"].predict(X_test),
})

if xgb_preds is not None:
    pred_table["xgb"] = xgb_preds

pred_table.head(10)

# %% [markdown]
# ## 6. Add Code Snippets for Visualization Placeholders
#
# These plots are useful for later screenshots. You can run them and save figures to add into the note.

# %%
import matplotlib.pyplot as plt

# Residuals for the Random Forest
rf_residuals = y_test - models["rf"].predict(X_test)

plt.figure(figsize=(6, 4))
plt.hist(rf_residuals, bins=30, color="#4C72B0", alpha=0.8)
plt.title("Random Forest Residuals")
plt.xlabel("Residual")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# %%
# Feature importance for Random Forest
rf_importances = models["rf"].feature_importances_

plt.figure(figsize=(6, 4))
plt.bar(range(len(rf_importances)), rf_importances, color="#55A868")
plt.title("Random Forest Feature Importances")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.tight_layout()
plt.show()

# Feature importance for XGBoost (if available)
if xgb_model is not None:
    xgb_importance = xgb_model.get_score(importance_type="gain")
    xgb_keys = list(xgb_importance.keys())
    xgb_vals = [xgb_importance[k] for k in xgb_keys]

    plt.figure(figsize=(6, 4))
    plt.bar(range(len(xgb_vals)), xgb_vals, color="#C44E52")
    plt.title("XGBoost Feature Importances (Gain)")
    plt.xlabel("Feature")
    plt.ylabel("Gain")
    plt.tight_layout()
    plt.show()

# %% [markdown]
# ## Summary and Next Steps
#
# - Random Forest should reduce variance compared to a single tree.
# - XGBoost should improve accuracy if its regularization is tuned well.
# - Try increasing `max_depth`, adjusting `eta`, or adding more data to see bias/variance tradeoffs.
#
# You can save the residual and feature importance plots to insert into the written note later.
