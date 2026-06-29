+++
title = "An Introduction to MLOps: A Short Tutorial with a Hands-On"
description = "A plain-language tutorial on MLOps — reproducibility, the ML lifecycle, and DevOps for machine learning — with a runnable MLflow hands-on you can finish in ten minutes."
date = 2026-06-29
updated = 2026-06-29
draft = false
aliases = ["/posts/intro-to-mlops-tutorial/"]

[taxonomies]
categories = ["2026"]
tags = ["mlops", "ai", "reproducibility", "tools", "mlflow"]

[extra]
lang = "en"
toc = true
+++

This is the written companion to the [**Introduction to MLOps** slides](/slides/2026/intro-to-mlops/). The slides give the picture; this note gives you something you can read at your own pace and, more importantly, **run**. By the end you will have tracked a real machine-learning experiment, compared two runs, and inspected them in a web UI — the smallest possible version of an MLOps workflow.

It is deliberately short. The goal is to get the core idea into your hands, not to be exhaustive.

## Why MLOps exists

A model that runs once, in one notebook, on your laptop, is not a system. The moment someone else needs to reproduce your result — or *you* need to, three months later — the questions start:

- Which version of the **code** produced this model?
- Which **data** did it train on?
- Which **hyperparameters** were used?
- What **score** did it actually get, and how does that compare to last week's attempt?

In ordinary software you answer these with version control and tests. Machine learning is harder because **three things change over time**, not one:

| Artifact | Changes because… |
|----------|------------------|
| **Code** | the usual reasons — refactors, bug fixes, new features |
| **Data** | new data arrives, distributions drift, labels get corrected |
| **Model** | it is retrained, fine-tuned, or replaced |

MLOps is the practice of bringing the discipline of software engineering — automation, reproducibility, monitoring — to all three. The one-line definition worth memorising:

> **MLOps = DevOps principles applied to machine-learning systems.**

## From the software cycle to the *automated* software cycle

Classic software moves through a cycle: **plan → code → build → test → release → deploy → monitor**, then back to plan. DevOps automates that loop so that every change flows through it continuously instead of in big manual batches:

- **Continuous Integration (CI)** — every commit is automatically built and tested.
- **Continuous Delivery (CD)** — passing builds are automatically packaged and deployed.
- **Continuous Monitoring** — the running system is watched for errors and feedback.

This is the "DevOps loop" you see drawn as an infinity symbol. CI/CD pipelines (GitHub Actions, GitLab CI, etc.) are the machinery that runs it.

## The machine-learning lifecycle

ML adds its own stages on top of the software cycle:

1. **Data extraction** — fetch the data.
2. **Data analysis** — understand its nature and quirks.
3. **Data preparation** — clean it, engineer features, split into train/validation/test.
4. **Model training** — fit the model, tune hyperparameters.
5. **Model evaluation** — measure quality on held-out data.
6. **Model validation** — confirm it beats a baseline and is fit to deploy.
7. **Model serving** — package and deploy it to make predictions.
8. **Model monitoring** — watch performance and decide when to retrain.

Notice the loop at the end: monitoring feeds back into the data and training stages. An ML system is never "done."

## MLOps = DevOps for ML

When you apply the DevOps loop to that lifecycle, each "continuous" practice gains an ML twist:

- **Continuous Integration** is no longer only about testing code — it now also **tests and validates data, schemas, and models**.
- **Continuous Delivery** ships not a single package but **a whole pipeline** that can deploy a model-serving service.
- **Continuous Training (CT)** is unique to ML: the system can **automatically retrain** and redeploy models as new data arrives.
- **Continuous Monitoring** tracks **model decay** and can trigger retraining when quality drops.

CT and model/data monitoring are the parts that have no equivalent in plain DevOps. They are what make MLOps its own discipline.

## The first practical step: experiment tracking

You do not adopt all of MLOps on day one. The single highest-leverage habit — the one that pays off immediately even in a solo project — is **experiment tracking**: recording, for every run, the parameters, metrics, artifacts, and code version that produced a result.

[**MLflow**](https://mlflow.org) is the open-source standard for this. Think of an ML experiment as *environment + data + code*, and MLflow as the logbook that records **hyperparameters + results + plots** for each run, so you can compare them later in a web UI. It is framework-agnostic (scikit-learn, PyTorch, TensorFlow, XGBoost…) and — usefully — it works for *any* software experiment, not just ML.

MLflow has a few components, but for tracking you only need two ideas:

- A **tracking server / store** — where runs are saved (a local folder is fine to start).
- The **tracking API** — `mlflow.log_param`, `mlflow.log_metric`, `mlflow.log_artifact`, wrapped in an `mlflow.start_run()` context.

---

## Hands-on: track your first experiment

Everything below is self-contained and runs on a laptop in under ten minutes. We will train two small classifiers, log them to MLflow, and compare them in the UI.

> **Want to just clone and run?** The full source lives in the companion repo: [**github.com/JienWeng/mlops-tutorial**](https://github.com/JienWeng/mlops-tutorial). `git clone` it, `pip install -r requirements.txt`, and run `python train.py`. The steps below explain what that code does, line by line.

### 1. Install

```shell
python -m pip install mlflow scikit-learn matplotlib
```

### 2. Point MLflow at a store

We will use a local **SQLite** database as the tracking store. This keeps everything on your laptop — no server to run — while using the backend MLflow recommends.

> **Heads-up (MLflow 3.x):** the old plain-folder store (`./mlruns` on its own) is now in maintenance mode and will raise an error unless you opt in. Using a SQLite URI like `sqlite:///mlflow.db` is the current, friction-free local setup, so that is what we do below. (On MLflow 2.x this same code still works.)

We set the store directly in the script (next step), so there is nothing to configure here.

### 3. The experiment script

Save this as `train.py`. It trains a logistic-regression classifier on the classic breast-cancer dataset, then logs the parameters, the accuracy, the trained model, and a confusion-matrix plot.

```python
# train.py
import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, f1_score
from sklearn.model_selection import train_test_split

# Where to store runs: a local SQLite db (metadata) + ./mlruns (artifacts)
mlflow.set_tracking_uri("sqlite:///mlflow.db")
# Group related runs under a named experiment
mlflow.set_experiment("intro-to-mlops")

# --- data ---
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# A hyperparameter we want to track and vary later
C = 1.0  # inverse regularisation strength

with mlflow.start_run(run_name=f"logreg-C={C}"):
    # --- train ---
    model = LogisticRegression(C=C, max_iter=10_000)
    model.fit(X_train, y_train)

    # --- evaluate ---
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    # --- log: parameters, metrics, the model itself ---
    mlflow.log_param("model", "LogisticRegression")
    mlflow.log_param("C", C)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1", f1)
    mlflow.sklearn.log_model(model, name="model")

    # --- log: a plot as an artifact ---
    ConfusionMatrixDisplay.from_predictions(y_test, preds)
    plt.title(f"Confusion matrix (C={C})")
    plt.savefig("confusion_matrix.png", bbox_inches="tight")
    mlflow.log_artifact("confusion_matrix.png")

    print(f"Logged run: accuracy={acc:.4f}, f1={f1:.4f}")
```

Run it:

```shell
python train.py
```

You just produced your first tracked run. The parameters, metrics, the serialised model, and the plot are all saved under `./mlruns`.

### 4. Make a second run to compare against

Change one line — `C = 0.01` — and run `python train.py` again. (Stronger regularisation; the score should move.) Now you have **two runs to compare**, which is the whole point of tracking.

> **Tip — skip the boilerplate.** For supported libraries, `mlflow.sklearn.autolog()` (or `mlflow.tensorflow.autolog()`, `mlflow.pytorch.autolog()`) auto-captures parameters, metrics, and the model with a single line, before you call `fit()`. Manual logging gives you the most control; autolog gives you 80% of the value for one line of code.

### 5. Inspect and compare in the UI

From the same folder, start the UI — pointing it at the same SQLite store:

```shell
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Open <http://127.0.0.1:5000>. You will see the `intro-to-mlops` experiment with both runs. From here you can:

- sort and filter runs by `accuracy` or `f1`,
- tick two runs and click **Compare** to see parameters and metrics side by side,
- open a run to view its **confusion-matrix plot** and download the saved model.

That comparison view — *"which settings gave the best score, and exactly how were they produced?"* — is the question MLOps is built to answer, and you now have a reproducible record of it.

### What you just built (and what comes next)

You have implemented the smallest real MLOps loop: **parameterise → run → log → compare**. The natural extensions, in rough order of payoff:

1. **Commit `train.py` to git** so each run is tied to a code version.
2. **Register the best model** in MLflow's Model Registry to give it a name and version.
3. **Automate the run in CI** so a push retrains and re-logs.
4. **Serve the model** (`mlflow models serve`) and **monitor** its predictions, closing the loop back to data.

## Take-home message

Research — and production work — should be **reproducible** and, where possible, **open**. If your work involves machine learning, that means using dedicated tools to make experiments reproducible rather than relying on memory and scattered notebooks.

Adopting these habits in your daily workflow pays off quickly: time saved in the long run, engineering skill gained, and trust earned among collaborators. And MLflow in particular is **not just for machine learning** — it is a capable logbook for tracking *any* computational experiment and keeping your results reproducible over time.

---

.small[This tutorial is adapted from the lecture **"An introduction to MLOps"** by [Alexandre Boucaud](https://aboucaud.github.io/slides/2023/lsst-france-mlops) (LSST France, Lyon, December 2023), licensed under [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0). The accompanying [slides](/slides/2026/intro-to-mlops/) are re-hosted under the same license; this written tutorial and hands-on are an original adaptation and are likewise shared under CC BY-SA 4.0.]
