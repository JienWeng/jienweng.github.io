+++
title = "Simple Linear Regression"
description = "An introduction to simple linear regression, the OLS method, and deriving the estimators using Sxx and Sxy notation."
date = 2026-01-02
updated = 2026-01-02
draft = false

[taxonomies]
categories = ["2026"]
tags = ["math", "statistics", "regression"]

[extra]
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

{% note() %}
**Regression Analysis Series**

1. **Simple Linear Regression** (You are here)
2. [Multiple Linear Regression](/posts/regression-02-multiple-linear-regression)
3. [Polynomial Regression](/posts/regression-03-polynomial-regression)
4. [Correlation](/posts/regression-04-correlation)
5. [R-squared: SST, SSE, SSR and the Relationship with Correlation](/posts/regression-05-r-squared-and-correlation)
6. [Standard Error in Regression](/posts/regression-06-standard-error)
7. [Confidence Intervals for Regression Coefficients](/posts/regression-07-confidence-intervals)
8. [Statistical Testing in Regression](/posts/regression-08-statistical-testing)
9. [ANOVA in Regression: SST, SSR, SSE and the F-Test](/posts/regression-09-anova)
{% end %}

In secondary school, we learn that the equation of a straight line is given by $y = mx + c$, where $m$ is the slope and $c$ is the y-intercept. In statistics and machine learning, we use a similar but more general form to model the relationship between a dependent variable $y$ and an independent variable $x$. This is known as simple linear regression.

## The Model

In simple linear regression, we express the relationship as:

$$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i,$$

where $\hat{y}_i$ is the predicted value of the dependent variable for the $i$-th observation, $\hat{\beta}_0$ is the estimated y-intercept, and $\hat{\beta}_1$ is the estimated slope coefficient. The "hat" notation indicates that these are estimates derived from data, not the true (unknown) population parameters $\beta_0$ and $\beta_1$.

The true model is assumed to be:

$$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i,$$

where $\varepsilon_i$ represents the random error term for the $i$-th observation.

## Ordinary Least Squares (OLS)

The question is: how do we find the best estimates $\hat{\beta}_0$ and $\hat{\beta}_1$? We need a systematic method that determines the line of best fit. The most common approach is Ordinary Least Squares (OLS).

OLS minimizes the sum of the squared differences between the observed values $y_i$ and the predicted values $\hat{y}_i$. These differences are called residuals, defined as $e_i = y_i - \hat{y}_i$. By squaring the residuals, we treat positive and negative errors equally and penalize larger deviations more heavily.

The objective function is the Sum of Squared Errors (SSE):

$$SSE = \sum^n_{i=1}(y_i - \hat{y}_i)^2 = \sum^n_{i=1}(y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2.$$

## Deriving the Normal Equations

To minimize the SSE, we take partial derivatives with respect to $\hat{\beta}_0$ and $\hat{\beta}_1$ and set them equal to zero.

### Partial derivative with respect to $\hat{\beta}_0$

$$\frac{\partial SSE}{\partial \hat{\beta}_0} = -2\sum^n_{i=1}(y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0.$$

Dividing both sides by $-2$ and expanding the sum:

$$\sum^n_{i=1} y_i - n\hat{\beta}_0 - \hat{\beta}_1 \sum^n_{i=1} x_i = 0.$$

Solving for $\hat{\beta}_0$:

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x},$$

where $\bar{x} = \frac{1}{n}\sum^n_{i=1}x_i$ and $\bar{y} = \frac{1}{n}\sum^n_{i=1}y_i$ are the sample means.

### Partial derivative with respect to $\hat{\beta}_1$

$$\frac{\partial SSE}{\partial \hat{\beta}_1} = -2\sum^n_{i=1}x_i(y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0.$$

Dividing by $-2$ and expanding:

$$\sum^n_{i=1} x_i y_i - \hat{\beta}_0 \sum^n_{i=1} x_i - \hat{\beta}_1 \sum^n_{i=1} x_i^2 = 0.$$

Substituting $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$:

$$\sum^n_{i=1} x_i y_i - (\bar{y} - \hat{\beta}_1 \bar{x})\sum^n_{i=1} x_i - \hat{\beta}_1 \sum^n_{i=1} x_i^2 = 0.$$

After simplification, we obtain:

$$\hat{\beta}_1 = \frac{\sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y})}{\sum^n_{i=1}(x_i - \bar{x})^2}.$$

## Introducing $S_{xx}$ and $S_{xy}$ Notation

To write the estimators more concisely, we define the following summary statistics:

$$S_{xx} = \sum^n_{i=1}(x_i - \bar{x})^2 = \sum^n_{i=1}x_i^2 - n\bar{x}^2,$$

$$S_{xy} = \sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y}) = \sum^n_{i=1}x_i y_i - n\bar{x}\bar{y}.$$

Using this notation, the OLS estimators become:

$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}},$$

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}.$$

These are elegant expressions that reveal the structure of the estimates. The slope $\hat{\beta}_1$ is the ratio of the joint variability of $x$ and $y$ (captured by $S_{xy}$) to the variability of $x$ alone (captured by $S_{xx}$). The intercept $\hat{\beta}_0$ ensures the regression line passes through the point $(\bar{x}, \bar{y})$.

## Residuals and Fitted Values

Once we have $\hat{\beta}_0$ and $\hat{\beta}_1$, we can compute:

- **Fitted values**: $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ for each observation.
- **Residuals**: $e_i = y_i - \hat{y}_i$ for each observation.

Two important properties of OLS residuals are worth noting:

1. The residuals sum to zero: $\sum^n_{i=1} e_i = 0$.
2. The residuals are uncorrelated with the fitted values: $\sum^n_{i=1} e_i \hat{y}_i = 0$.

These properties follow directly from the normal equations.

## Key Assumptions

For OLS to produce reliable estimates, the following assumptions are typically required:

1. **Linearity**: The relationship between $x$ and $y$ is linear in the parameters.
2. **Independence**: The observations are independent of one another.
3. **Homoscedasticity**: The variance of the error terms $\varepsilon_i$ is constant across all values of $x$.
4. **Normality**: The error terms are normally distributed, that is, $\varepsilon_i \sim N(0, \sigma^2)$.

When these assumptions hold, OLS produces the Best Linear Unbiased Estimators (BLUE) according to the Gauss-Markov theorem.

## Summary

In this post, we covered the fundamentals of simple linear regression:

- The model $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ describes the estimated linear relationship between $x$ and $y$.
- OLS minimizes the sum of squared errors to find the best-fitting line.
- The estimators $\hat{\beta}_1 = S_{xy}/S_{xx}$ and $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$ are derived from the normal equations.
- The $S_{xx}$ and $S_{xy}$ notation provides a compact way to express these results.

In the next post, we will extend this framework to handle multiple independent variables through multiple linear regression.
