+++
title = "An Introduction to MLOps: A Complete Tutorial with a Hands-On"
description = "A plain-language tutorial that follows the Intro to MLOps slides end to end — reproducibility, the software cycle, DevOps, the ML lifecycle, MLOps, and MLflow — with diagrams and a runnable hands-on."
date = 2026-06-29
updated = 2026-06-30
draft = false
aliases = ["/posts/intro-to-mlops-tutorial/"]

[taxonomies]
categories = ["2026"]
tags = ["mlops", "ai", "reproducibility", "tools", "mlflow"]

[extra]
topic = "Machine Learning"
lang = "en"
toc = true
+++

This is the written companion to the [**Introduction to MLOps** slides](/slides/2026/intro-to-mlops/). It follows the deck section by section — the same chain of ideas, the same diagrams (redrawn), and then the hands-on the deck builds toward. The slides give the picture in a room; this note lets you read it at your own pace and, more importantly, **run** it. By the end you will have tracked a real machine-learning experiment, compared two runs, and inspected them in a web UI.

The chain the deck walks, and so will we:

> **reproducibility → the software cycle → DevOps → the ML lifecycle → MLOps → MLflow → a hands-on.**

## Why reproducibility — and why ML makes it hard

The starting motivation is research integrity. A result you cannot reproduce is hard to trust, hard to build on, and hard to defend. In software-heavy science this is why people publish code alongside papers (the [Papers with Code](https://paperswithcode.com) culture). But "publish the code" is not enough on its own.

Reproducibility really means being able to recreate a result from **all** of its ingredients:

- the **code** (which commit?),
- the **data** (which version, which split?),
- the **environment** (which library versions?),
- and the **parameters** that produced the run.

Machine learning makes this harder than ordinary software because **three things change over time**, not one:

| Artifact | Changes because… |
|----------|------------------|
| **Code** | the usual reasons — refactors, bug fixes, new features |
| **Data** | new data arrives, distributions drift, labels get corrected |
| **Model** | it is retrained, fine-tuned, or replaced |

Track only the code and you will still fail to reproduce a model, because the data and the trained model moved underneath you. MLOps is the practice of bringing software-engineering discipline — automation, reproducibility, monitoring — to all three. The one-line definition worth memorising:

> **MLOps = DevOps principles applied to machine-learning systems.**

To get there, we first need the software-engineering half of that sentence.

## The software development cycle

Classic software development moves through repeating stages:

1. **Development** — planning and coding.
2. **Integration** — quick tests and a build.
3. **Testing** — deeper tests, validation, and a release.
4. **Delivery** — final packaging and deployment to a running server.
5. **Monitoring** — collecting data, watching each component, gathering user feedback.

Run those once, by hand, and you have traditional software delivery: slow, batched, and error-prone at the hand-offs.

## Automating it: DevOps and CI/CD

DevOps is what you get when you **automate that cycle** so every change flows through it continuously instead of in big manual batches:

- **Continuous Integration (CI)** — every commit is automatically built and tested.
- **Continuous Delivery (CD)** — passing builds are automatically packaged and deployed.
- **Continuous Monitoring** — the running system is watched for errors and feedback, which flows back into planning.

{{ figure(src="/img/notes/intro-to-mlops/devops_loop.png", alt="The DevOps loop: Plan, Code, Build, Test on the Dev/CI side; Release, Deploy, Operate, Monitor on the Ops side, with feedback back to Plan", caption="The DevOps loop. Every change flows through the same automated cycle; monitoring feeds back into planning.") }}

DevOps is usually described as resting on three legs — often drawn as a trident:

- **People** — a culture where development and operations share ownership.
- **Process** — the automated CI/CD pipeline itself.
- **Tools** — the machinery that runs it (GitHub Actions, GitLab CI, containers, and so on).

The tools get the attention, but the culture and the process are what make the automation stick.

## The machine-learning lifecycle

Machine learning adds its own stages on top of the software cycle. A typical ML lifecycle runs:

1. **Data extraction** — fetch the data.
2. **Data analysis** — understand its nature and quirks.
3. **Data preparation** — clean it, engineer features, split into train/validation/test.
4. **Model training** — fit the model, tune hyperparameters.
5. **Model evaluation** — measure quality on held-out data.
6. **Model validation** — confirm it beats a baseline and is fit to deploy.
7. **Model serving** — package and deploy it to make predictions.
8. **Model monitoring** — watch performance and decide when to retrain.

{{ figure(src="/img/notes/intro-to-mlops/ml_lifecycle.png", alt="The ML lifecycle from data extraction through serving and monitoring, with a feedback arrow from monitoring back to data", caption="The ML lifecycle. Data stages feed model stages; monitoring loops back to the start, so the system is never truly 'done'.") }}

The loop at the end is the important part: monitoring feeds back into data and training. An ML system in production is a living thing, not a shipped artifact.

## MLOps = DevOps for ML

Now overlay the DevOps loop onto the ML lifecycle. Each "continuous" practice gains an ML twist:

{{ figure(src="/img/notes/intro-to-mlops/mlops_devops_ml.png", alt="Table mapping CI, CD, CT, CM to their ML-specific meaning, with Continuous Training and Continuous Monitoring marked as ML-only", caption="MLOps applies the DevOps loop to ML. Continuous Training and model/data monitoring are the parts with no equivalent in plain DevOps.") }}

- **Continuous Integration** is no longer only about testing code — it now also **tests and validates data, schemas, and models**.
- **Continuous Delivery** ships not a single package but **a whole pipeline** that can deploy a model-serving service.
- **Continuous Training (CT)** is unique to ML: the system can **automatically retrain** and redeploy as new data arrives.
- **Continuous Monitoring** tracks **model decay** and can trigger retraining when quality drops.

CT and model/data monitoring are what make MLOps its own discipline rather than "DevOps with notebooks".

## What an MLOps workflow looks like in practice

Put concretely, a working MLOps setup wires together a handful of pieces:

- **version control** for code (git),
- **data/version tracking** for datasets,
- an **experiment-tracking** server that records every run,
- a **model registry** that versions and stages models,
- a **CI/CD pipeline** that retrains and redeploys,
- and **monitoring** that watches the served model and closes the loop.

You do not build all of this on day one. The single highest-leverage habit — the one that pays off immediately even in a solo project — is **experiment tracking**. That is where we will get hands-on.

## MLflow: the tool we will use

[**MLflow**](https://mlflow.org) is the open-source standard for experiment tracking. The mental model: an ML experiment is *environment + data + code*, and MLflow is the logbook that records, for each run, its **hyperparameters + results + plots** so you can compare runs later in a web UI. It is framework-agnostic (scikit-learn, PyTorch, TensorFlow, XGBoost…) and works for *any* computational experiment, not just ML.

MLflow has four components:

{{ figure(src="/img/notes/intro-to-mlops/mlflow_components.png", alt="MLflow components: Tracking, Projects, Models, and Model Registry", caption="MLflow's four components. We use Tracking — the entry point that pays off first.") }}

- **Tracking** — log parameters, metrics, and artifacts per run (our focus).
- **Projects** — package code so a run is reproducible.
- **Models** — a standard packaging format so a trained model can be served anywhere.
- **Model Registry** — version models and move them through stages (staging → production).

## The MLflow tracking API

Tracking comes down to a few calls. First, name an experiment to group related runs, then wrap each run in a context manager:

```python
import mlflow

mlflow.set_experiment("intro-to-mlops")

with mlflow.start_run(run_name="my-first-run"):
    mlflow.log_param("learning_rate", 0.01)       # one hyperparameter
    mlflow.log_params({"epochs": 20, "batch": 32}) # several at once
    mlflow.log_metric("accuracy", 0.92)            # a result
    mlflow.sklearn.log_model(model, name="model")  # the model itself
```

The three verbs you will use constantly:

- `log_param` / `log_params` — key–value settings (hyperparameters, config).
- `log_metric` — numeric results (loss, accuracy); these become plots in the UI so you can compare runs.
- `log_model` — the trained model, in MLflow's portable format.

**Too lazy to log by hand?** For supported libraries, a single `autolog()` call before `fit()` captures parameters, metrics, and the model automatically:

```python
mlflow.sklearn.autolog()      # or mlflow.tensorflow.autolog(), mlflow.pytorch.autolog()
model.fit(X_train, y_train)   # params, metrics, and model are logged for you
```

Manual logging gives you the most control; `autolog` gives you most of the value for one line. And the feature people quietly love most — **logging plots as artifacts**, so a figure is stored with the run and viewable in the UI:

```python
plt.savefig("loss.png")
mlflow.log_artifact("loss.png")
```

## Where MLflow stores runs: three setup options

Before logging anything, MLflow needs to know *where* runs go. There are three options, in increasing order of scale:

{{ figure(src="/img/notes/intro-to-mlops/mlflow_tracking_setup.png", alt="Three MLflow tracking setup options: local filesystem, local database, remote server", caption="Three ways to store runs. We use a local SQLite database — no server, but the backend MLflow recommends.") }}

- **Option 1 — local filesystem** (`./mlruns`): the simplest default.
- **Option 2 — local database** (`sqlite:///mlflow.db`): still on your laptop, but the backend MLflow now recommends. **This is what we use below.**
- **Option 3 — remote server** (`http://server:5000`): a shared tracking server for a team.

---

## Hands-on: track your first experiment

Everything below is self-contained and runs on a laptop in under ten minutes. We will train two small classifiers, log them to MLflow, and compare them in the UI.

> **Want to just clone and run?** The full source — script **and** notebook — lives in the companion repo: [**github.com/JienWeng/mlops-tutorial**](https://github.com/JienWeng/mlops-tutorial). `git clone` it, `pip install -r requirements.txt`, then `python train.py` (or open `notebook.ipynb`). The steps below explain what that code does.

### 1. Install

```shell
python -m pip install mlflow scikit-learn matplotlib
```

### 2. Choose a store (Option 2: local SQLite)

We use a local SQLite database — Option 2 above. It keeps everything on your laptop with no server to run.

> **Heads-up (MLflow 3.x):** the plain-folder store (`./mlruns` on its own) is now in maintenance mode and will raise an error unless you opt in. A SQLite URI like `sqlite:///mlflow.db` is the friction-free local setup, so that is what we use. (On MLflow 2.x this same code still works.)

We set the store directly in the script, so there is nothing to configure separately.

### 3. The experiment script

Save this as `train.py`. It trains a logistic-regression classifier on the classic breast-cancer dataset, then logs the parameters, the metrics, the trained model, and a confusion-matrix plot.

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

You just produced your first tracked run. The parameters, metrics, the serialised model, and the plot are all saved.

### 4. Make a second run to compare against

Change one line — `C = 0.01` — and run `python train.py` again. (Stronger regularisation; the score should move.) Now you have **two runs to compare**, which is the whole point of tracking.

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

That list is exactly the MLOps workflow from earlier — you have now built its first link.

## Take-home message

Research — and production work — should be **reproducible** and, where possible, **open**. If your work involves machine learning, that means using dedicated tools to make experiments reproducible rather than relying on memory and scattered notebooks.

Adopting these habits in your daily workflow pays off quickly: time saved in the long run, engineering skill gained, and trust earned among collaborators. And MLflow in particular is **not just for machine learning** — it is a capable logbook for tracking *any* computational experiment and keeping your results reproducible over time.

---

.small[This tutorial follows and is adapted from the lecture **"An introduction to MLOps"** by [Alexandre Boucaud](https://aboucaud.github.io/slides/2023/lsst-france-mlops) (LSST France, Lyon, December 2023), licensed under [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0). The accompanying [slides](/slides/2026/intro-to-mlops/) are re-hosted under the same license. The diagrams here are original redrawings of the concepts, and this written tutorial and hands-on are an original adaptation, likewise shared under CC BY-SA 4.0.]
