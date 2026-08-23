+++
title = "Proof of Ordinary Least Square (OLS) in Linear Regression"
description = "Understanding the mathematical foundation of OLS"
date = 2025-11-10
updated = 2025-11-10
draft = true
aliases = ["/posts/proof-of-ordinary-least-square/"]

[taxonomies]
categories = ["2025"]
tags = ["math", "ai"]

[extra]
topic = "Regression"
lang = "en"
toc = true
comment = true
copy = false
outdate_alert = false
outdate_alert_days = 120
math = true
mermaid = false
featured = false
reaction = true
+++

Ordinary least squares chooses the line that minimizes squared residuals. This note derives the estimator from that objective, so the closed-form solution follows from the algebra instead of appearing as a formula to memorize.

In secondary school, we've been taught that the formula for a straight line is given by $y=mx+c$, where $m$ is the slope and $c$ is the y-intercept. This formula represents a linear relationship between the independent variable $x$ and the dependent variable $y$. In statistics and machine learning, we often use a more general form of this equation to represent linear relationships between multiple independent variables and a dependent variable. This is known as linear regression.

In linear regression, we express the relationship as:

$$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$$,

you can somehow realize that this is similar to the $y=mx+c$ formula, where $\hat{y}_i$ is the predicted value of the dependent variable for the $i$-th observation, $\hat{\beta}_0$ is the estimated y-intercept, $\hat{\beta}_1$ is the estimated slope (or coefficient) for the independent variable $x_i$. The "hat" notation indicates that these are estimates derived from data.

But the question is, how do we estimate the values of $\hat{\beta}_0$ and $\hat{\beta}_1$? We cannot simply guess them and assign a number that we think fits best. We need a systematic way to find the best-fitting line that represents the relationship between $x$ and $y$.

Ordinary Least Squares (OLS) minimizes the squared differences between the observed values ($y_i$) and the predicted values ($\hat{y}_i$). These differences are residuals. Squaring them treats positive and negative errors equally while giving larger errors more weight. For example, errors of +2 and -2 cancel when added, but their squared values contribute 4 each to the objective.

Mathematically, we can express the OLS objective as minimizing the following cost function, we called as Sum of Squared Errors (SSE):

$$ SSE = \sum^n_{i=1} (y_i - \hat{y}_i)^2$$

By substituting the linear regression equation into the SSE, we have:

$$ SSE = \sum^n_{i=1}(y_i - (\hat{\beta}_0 + \hat{\beta}_1 x_i))^2 $$

To find the optimal values of $\hat{\beta}_0$ and $\hat{\beta}_1$ that minimize the SSE, we take the partial derivatives of the SSE with respect to each parameter and set them to zero. This gives us a system of equations known as the normal equations. The rationale for setting the derivatives to zero is that at the minimum point of a function, the slope (or derivative) is zero. By solving these equations, we can find the values of $\hat{\beta}_0$ and $\hat{\beta}_1$ that minimize the SSE.

Taking the partial derivative of SSE with respect to $\hat{\beta}_0$ and setting it to zero:

$$ \frac{\partial SSE}{\partial \hat{\beta}_0} = -2 \sum^n_{i=1}(y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0 $$
