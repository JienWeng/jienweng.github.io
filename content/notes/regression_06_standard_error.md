+++
title = "Standard Error in Regression"
description = "Deriving the standard errors of the regression coefficients using MSE, Sxx, and the variance-covariance matrix."
date = 2026-02-06
updated = 2026-02-06
draft = false
aliases = ["/posts/regression-06-standard-error/"]

[taxonomies]
categories = ["2026"]
tags = ["math", "statistics", "regression"]

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

This note explains standard error in regression as a measure of uncertainty in coefficient estimates, not model quality by itself. The practical question is how noisy your estimate is if the data-generating process were repeated. I connect residual variance, sample size, and confidence in coefficients.

## Estimating the Error Variance

Under the linear model $y\_i = \beta\_0 + \beta\_1 x\_i + \varepsilon\_i$ with $\varepsilon\_i \sim N(0, \sigma^2)$, the error variance $\sigma^2$ is unknown and must be estimated from the data.

The natural estimate is based on the residuals. The Mean Squared Error (MSE) is defined as:

$$MSE = \frac{SSE}{n - 2} = \frac{\sum^n\_{i=1}(y\_i - \hat{y}\_i)^2}{n - 2}.$$

The denominator is $n - 2$ (not $n$) because we lose two degrees of freedom for estimating $\hat{\beta}\_0$ and $\hat{\beta}\_1$. This correction ensures that MSE is an unbiased estimator of $\sigma^2$:

$$E(MSE) = \sigma^2.$$

For multiple regression with $p$ parameters, the denominator becomes $n - p$:

$$MSE = \frac{SSE}{n - p}.$$

## Variance of the OLS Estimators

### Simple Linear Regression

The OLS estimators are functions of the random variable $\mathbf{Y}$ (since $\mathbf{X}$ is treated as fixed). Their variances can be derived from the model assumptions.

**Variance of $\hat{\beta}\_1$:**

Since $\hat{\beta}\_1 = S\_{xy}/S\_{xx} = \sum^n\_{i=1}c\_i y\_i$ where $c\_i = (x\_i - \bar{x})/S\_{xx}$, and the $y\_i$ are independent with variance $\sigma^2$:

$$\text{Var}(\hat{\beta}\_1) = \sum^n\_{i=1}c\_i^2 \text{Var}(y\_i) = \sigma^2 \sum^n\_{i=1}\frac{(x\_i - \bar{x})^2}{S\_{xx}^2} = \sigma^2 \cdot \frac{S\_{xx}}{S\_{xx}^2} = \frac{\sigma^2}{S\_{xx}}.$$

**Variance of $\hat{\beta}\_0$:**

Since $\hat{\beta}\_0 = \bar{y} - \hat{\beta}\_1\bar{x}$:

$$\text{Var}(\hat{\beta}\_0) = \text{Var}(\bar{y}) + \bar{x}^2 \text{Var}(\hat{\beta}\_1) = \frac{\sigma^2}{n} + \bar{x}^2 \cdot \frac{\sigma^2}{S\_{xx}} = \sigma^2\left(\frac{1}{n} + \frac{\bar{x}^2}{S\_{xx}}\right).$$

Note that $\text{Var}(\hat{\beta}\_0)$ depends on the mean of $x$: the further $\bar{x}$ is from zero, the larger the variance of the intercept estimate.

## Standard Errors

The standard error of an estimator is the square root of its estimated variance, obtained by replacing $\sigma^2$ with MSE.

**Standard error of $\hat{\beta}\_1$:**

$$SE(\hat{\beta}\_1) = \sqrt{\frac{MSE}{S\_{xx}}}.$$

**Standard error of $\hat{\beta}\_0$:**

$$SE(\hat{\beta}\_0) = \sqrt{MSE\left(\frac{1}{n} + \frac{\bar{x}^2}{S\_{xx}}\right)}.$$

These formulas show that the precision of our estimates improves (standard errors decrease) when:

- $MSE$ is small (the model fits the data well).
- $S\_{xx}$ is large (there is more spread in the $x$ values).
- $n$ is large (we have more data).

## General Case: Multiple Regression

For the multiple regression model $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, the variance-covariance matrix of $\hat{\boldsymbol{\beta}}$ is:

$$\text{Var}(\hat{\boldsymbol{\beta}}) = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}.$$

The estimated variance-covariance matrix is:

$$\widehat{\text{Var}}(\hat{\boldsymbol{\beta}}) = MSE \cdot (\mathbf{X}^T\mathbf{X})^{-1}.$$

Let $(\mathbf{X}^T\mathbf{X})^{-1} = \mathbf{C}$, and let $C\_{jj}$ denote the $(j+1)$-th diagonal element of $\mathbf{C}$ (corresponding to $\hat{\beta}\_j$). Then:

$$\text{Var}(\hat{\beta}\_j) = \sigma^2 C\_{jj},$$

$$SE(\hat{\beta}\_j) = \sqrt{MSE \cdot C\_{jj}}.$$

### Verification for Simple Linear Regression

For simple linear regression, the design matrix is:

$$\mathbf{X} = \begin{pmatrix} 1 & x\_1 \\\\ 1 & x\_2 \\\\ \vdots & \vdots \\\\ 1 & x\_n \end{pmatrix}, \quad \mathbf{X}^T\mathbf{X} = \begin{pmatrix} n & \sum x\_i \\\\ \sum x\_i & \sum x\_i^2 \end{pmatrix}.$$

The inverse is:

$$(\mathbf{X}^T\mathbf{X})^{-1} = \frac{1}{n\sum x\_i^2 - (\sum x\_i)^2}\begin{pmatrix} \sum x\_i^2 & -\sum x\_i \\\\ -\sum x\_i & n \end{pmatrix}.$$

Since $n\sum x\_i^2 - (\sum x\_i)^2 = n \cdot S\_{xx}$, the diagonal elements are:

$$C\_{00} = \frac{\sum x\_i^2}{n \cdot S\_{xx}} = \frac{1}{n} + \frac{\bar{x}^2}{S\_{xx}}, \quad C\_{11} = \frac{n}{n \cdot S\_{xx}} = \frac{1}{S\_{xx}}.$$

These give us:

$$\text{Var}(\hat{\beta}\_0) = \sigma^2\left(\frac{1}{n} + \frac{\bar{x}^2}{S\_{xx}}\right), \quad \text{Var}(\hat{\beta}\_1) = \frac{\sigma^2}{S\_{xx}},$$

which matches our earlier derivations.

## Interpreting the Standard Error

The standard error measures the typical size of the sampling variability in the estimated coefficient. If we were to repeatedly draw new samples of size $n$ from the same population and compute $\hat{\beta}\_1$ each time, the standard deviation of these estimates would be approximately $SE(\hat{\beta}\_1)$.

A small standard error relative to the coefficient estimate suggests that the estimate is precise. A large standard error suggests substantial uncertainty. We will use the standard error to construct confidence intervals (Post 7) and perform hypothesis tests (Post 8).

## Summary

In this post, we derived the standard errors of the regression coefficients:

- $MSE = SSE/(n-2)$ estimates the error variance $\sigma^2$ for simple linear regression, or $MSE = SSE/(n-p)$ for multiple regression.
- $SE(\hat{\beta}\_1) = \sqrt{MSE/S\_{xx}}$ measures the precision of the slope estimate.
- $SE(\hat{\beta}\_0) = \sqrt{MSE(1/n + \bar{x}^2/S\_{xx})}$ measures the precision of the intercept estimate.
- For multiple regression, $SE(\hat{\beta}\_j) = \sqrt{MSE \cdot C\_{jj}}$ where $C\_{jj}$ is the $(j+1)$-th diagonal element of $(\mathbf{X}^T\mathbf{X})^{-1}$.
- Precision improves with larger $S\_{xx}$, smaller $MSE$, and larger $n$.

In the next post, we will use these standard errors to construct confidence intervals for $\beta\_0$, $\beta\_1$, and $\beta\_i$.
