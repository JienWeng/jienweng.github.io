+++
title = "Standard Error in Regression"
description = "Deriving the standard errors of the regression coefficients using MSE, Sxx, and the variance-covariance matrix."
date = 2026-02-06
updated = 2026-02-06
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

1. [Simple Linear Regression](/posts/regression-01-simple-linear-regression)
2. [Multiple Linear Regression](/posts/regression-02-multiple-linear-regression)
3. [Polynomial Regression](/posts/regression-03-polynomial-regression)
4. [Correlation](/posts/regression-04-correlation)
5. [R-squared: SST, SSE, SSR and the Relationship with Correlation](/posts/regression-05-r-squared-and-correlation)
6. **Standard Error in Regression** (You are here)
7. [Confidence Intervals for Regression Coefficients](/posts/regression-07-confidence-intervals)
8. [Statistical Testing in Regression](/posts/regression-08-statistical-testing)
9. [ANOVA in Regression: SST, SSR, SSE and the F-Test](/posts/regression-09-anova)
{% end %}

In the [previous post](/posts/regression-05-r-squared-and-correlation), we measured how well the regression model fits the data through $R^2$. But a good fit alone is not enough. We also need to quantify the uncertainty in our coefficient estimates. This is where the standard error comes in.

## Estimating the Error Variance

Under the linear model $y_i = \beta_0 + \beta_1 x_i + \varepsilon_i$ with $\varepsilon_i \sim N(0, \sigma^2)$, the error variance $\sigma^2$ is unknown and must be estimated from the data.

The natural estimate is based on the residuals. The Mean Squared Error (MSE) is defined as:

$$MSE = \frac{SSE}{n - 2} = \frac{\sum^n_{i=1}(y_i - \hat{y}_i)^2}{n - 2}.$$

The denominator is $n - 2$ (not $n$) because we lose two degrees of freedom for estimating $\hat{\beta}_0$ and $\hat{\beta}_1$. This correction ensures that MSE is an unbiased estimator of $\sigma^2$:

$$E(MSE) = \sigma^2.$$

For multiple regression with $p$ parameters, the denominator becomes $n - p$:

$$MSE = \frac{SSE}{n - p}.$$

## Variance of the OLS Estimators

### Simple Linear Regression

The OLS estimators are functions of the random variable $\mathbf{Y}$ (since $\mathbf{X}$ is treated as fixed). Their variances can be derived from the model assumptions.

**Variance of $\hat{\beta}_1$:**

Since $\hat{\beta}_1 = S_{xy}/S_{xx} = \sum^n_{i=1}c_i y_i$ where $c_i = (x_i - \bar{x})/S_{xx}$, and the $y_i$ are independent with variance $\sigma^2$:

\begin{align*}
\text{Var}(\hat{\beta}_1) &= \sum^n_{i=1}c_i^2 \text{Var}(y_i) = \sigma^2 \sum^n_{i=1}\frac{(x_i - \bar{x})^2}{S_{xx}^2} \\
&= \sigma^2 \cdot \frac{S_{xx}}{S_{xx}^2} = \frac{\sigma^2}{S_{xx}}.
\end{align*}

**Variance of $\hat{\beta}_0$:**

Since $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$:

\begin{align*}
\text{Var}(\hat{\beta}_0) &= \text{Var}(\bar{y}) + \bar{x}^2 \text{Var}(\hat{\beta}_1) \\
&= \frac{\sigma^2}{n} + \bar{x}^2 \cdot \frac{\sigma^2}{S_{xx}} \\
&= \sigma^2\left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right).
\end{align*}

Note that $\text{Var}(\hat{\beta}_0)$ depends on the mean of $x$: the further $\bar{x}$ is from zero, the larger the variance of the intercept estimate.

## Standard Errors

The standard error of an estimator is the square root of its estimated variance, obtained by replacing $\sigma^2$ with MSE.

**Standard error of $\hat{\beta}_1$:**

$$SE(\hat{\beta}_1) = \sqrt{\frac{MSE}{S_{xx}}}.$$

**Standard error of $\hat{\beta}_0$:**

$$SE(\hat{\beta}_0) = \sqrt{MSE\left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right)}.$$

These formulas show that the precision of our estimates improves (standard errors decrease) when:

- $MSE$ is small (the model fits the data well).
- $S_{xx}$ is large (there is more spread in the $x$ values).
- $n$ is large (we have more data).

## General Case: Multiple Regression

For the multiple regression model $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, the variance-covariance matrix of $\hat{\boldsymbol{\beta}}$ is:

$$\text{Var}(\hat{\boldsymbol{\beta}}) = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}.$$

The estimated variance-covariance matrix is:

$$\widehat{\text{Var}}(\hat{\boldsymbol{\beta}}) = MSE \cdot (\mathbf{X}^T\mathbf{X})^{-1}.$$

Let $(\mathbf{X}^T\mathbf{X})^{-1} = \mathbf{C}$, and let $C_{jj}$ denote the $(j+1)$-th diagonal element of $\mathbf{C}$ (corresponding to $\hat{\beta}_j$). Then:

$$\text{Var}(\hat{\beta}_j) = \sigma^2 C_{jj},$$

$$SE(\hat{\beta}_j) = \sqrt{MSE \cdot C_{jj}}.$$

### Verification for Simple Linear Regression

For simple linear regression, the design matrix is:

$$\mathbf{X} = \begin{pmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n \end{pmatrix}, \quad \mathbf{X}^T\mathbf{X} = \begin{pmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2 \end{pmatrix}.$$

The inverse is:

$$(\mathbf{X}^T\mathbf{X})^{-1} = \frac{1}{n\sum x_i^2 - (\sum x_i)^2}\begin{pmatrix} \sum x_i^2 & -\sum x_i \\ -\sum x_i & n \end{pmatrix}.$$

Since $n\sum x_i^2 - (\sum x_i)^2 = n \cdot S_{xx}$, the diagonal elements are:

$$C_{00} = \frac{\sum x_i^2}{n \cdot S_{xx}} = \frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}, \quad C_{11} = \frac{n}{n \cdot S_{xx}} = \frac{1}{S_{xx}}.$$

These give us:

$$\text{Var}(\hat{\beta}_0) = \sigma^2\left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right), \quad \text{Var}(\hat{\beta}_1) = \frac{\sigma^2}{S_{xx}},$$

which matches our earlier derivations.

## Interpreting the Standard Error

The standard error measures the typical size of the sampling variability in the estimated coefficient. If we were to repeatedly draw new samples of size $n$ from the same population and compute $\hat{\beta}_1$ each time, the standard deviation of these estimates would be approximately $SE(\hat{\beta}_1)$.

A small standard error relative to the coefficient estimate suggests that the estimate is precise. A large standard error suggests substantial uncertainty. We will use the standard error to construct confidence intervals (Post 7) and perform hypothesis tests (Post 8).

## Summary

In this post, we derived the standard errors of the regression coefficients:

- $MSE = SSE/(n-2)$ estimates the error variance $\sigma^2$ for simple linear regression, or $MSE = SSE/(n-p)$ for multiple regression.
- $SE(\hat{\beta}_1) = \sqrt{MSE/S_{xx}}$ measures the precision of the slope estimate.
- $SE(\hat{\beta}_0) = \sqrt{MSE(1/n + \bar{x}^2/S_{xx})}$ measures the precision of the intercept estimate.
- For multiple regression, $SE(\hat{\beta}_j) = \sqrt{MSE \cdot C_{jj}}$ where $C_{jj}$ is the $j$-th diagonal element of $(\mathbf{X}^T\mathbf{X})^{-1}$.
- Precision improves with larger $S_{xx}$, smaller $MSE$, and larger $n$.

In the next post, we will use these standard errors to construct confidence intervals for $\beta_0$, $\beta_1$, and $\beta_i$.
