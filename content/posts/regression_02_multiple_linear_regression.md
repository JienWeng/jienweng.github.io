+++
title = "Multiple Linear Regression"
description = "Extending simple linear regression to multiple predictors using matrix notation and deriving the OLS estimator in matrix form."
date = 2026-01-09
updated = 2026-01-09
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
2. **Multiple Linear Regression** (You are here)
3. [Polynomial Regression](/posts/regression-03-polynomial-regression)
4. [Correlation](/posts/regression-04-correlation)
5. [R-squared: SST, SSE, SSR and the Relationship with Correlation](/posts/regression-05-r-squared-and-correlation)
6. [Standard Error in Regression](/posts/regression-06-standard-error)
7. [Confidence Intervals for Regression Coefficients](/posts/regression-07-confidence-intervals)
8. [Statistical Testing in Regression](/posts/regression-08-statistical-testing)
9. [ANOVA in Regression: SST, SSR, SSE and the F-Test](/posts/regression-09-anova)
   {% end %}

In the [previous post](/posts/regression-01-simple-linear-regression), we explored simple linear regression with a single predictor. In practice, the response variable $y$ often depends on more than one predictor. Multiple linear regression extends the framework to accommodate $p - 1$ independent variables.

## The Model

The multiple linear regression model for the $i$-th observation is:

$$y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_{p-1} x_{i,p-1} + \varepsilon_i,$$

where $x\_{ij}$ is the value of the $j$-th predictor for the $i$-th observation, $\beta\_j$ are the regression coefficients, and $\varepsilon\_i$ is the error term. The total number of parameters is $p$ (including the intercept $\beta\_0$).

## Matrix Notation

Writing out the model for each observation individually becomes cumbersome as the number of predictors grows. Matrix notation provides a compact and powerful alternative.

Define the following:

$$\mathbf{Y} = \begin{pmatrix} y\_1 \\\\ y\_2 \\\\ \vdots \\\\ y\_n \end{pmatrix}, \quad \mathbf{X} = \begin{pmatrix} 1 & x\_{11} & x\_{12} & \cdots & x\_{1,p-1} \\\\ 1 & x\_{21} & x\_{22} & \cdots & x\_{2,p-1} \\\\ \vdots & \vdots & \vdots & \ddots & \vdots \\\\ 1 & x\_{n1} & x\_{n2} & \cdots & x\_{n,p-1} \end{pmatrix},$$

$$\boldsymbol{\beta} = \begin{pmatrix} \beta\_0 \\\\ \beta\_1 \\\\ \vdots \\\\ \beta\_{p-1} \end{pmatrix}, \quad \boldsymbol{\varepsilon} = \begin{pmatrix} \varepsilon\_1 \\\\ \varepsilon\_2 \\\\ \vdots \\\\ \varepsilon\_n \end{pmatrix}.$$

The model can now be written as:

$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}.$$

Here, $\mathbf{Y}$ is an $n \times 1$ vector of responses, $\mathbf{X}$ is an $n \times p$ design matrix (the first column of ones accounts for the intercept), $\boldsymbol{\beta}$ is a $p \times 1$ vector of coefficients, and $\boldsymbol{\varepsilon}$ is an $n \times 1$ vector of errors.

## OLS in Matrix Form

The sum of squared errors can be written in matrix form as:

$$SSE = (\mathbf{Y} - \mathbf{X}\boldsymbol{\beta})^T(\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}).$$

Expanding this expression:

$$SSE = \mathbf{Y}^T\mathbf{Y} - 2\boldsymbol{\beta}^T\mathbf{X}^T\mathbf{Y} + \boldsymbol{\beta}^T\mathbf{X}^T\mathbf{X}\boldsymbol{\beta}.$$

To minimize, we take the derivative with respect to $\boldsymbol{\beta}$ and set it to zero:

$$\frac{\partial SSE}{\partial \boldsymbol{\beta}} = -2\mathbf{X}^T\mathbf{Y} + 2\mathbf{X}^T\mathbf{X}\boldsymbol{\beta} = \mathbf{0}.$$

This gives us the normal equations in matrix form:

$$\mathbf{X}^T\mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{X}^T\mathbf{Y}.$$

Provided that $\mathbf{X}^T\mathbf{X}$ is invertible (that is, the columns of $\mathbf{X}$ are linearly independent), we can solve for the OLS estimator:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}.$$

This single formula generalizes the simple linear regression result. When $p = 2$ (one predictor plus the intercept), this reduces to $\hat{\beta}_1 = S_{xy}/S_{xx}$ and $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$ as derived in the previous post.

## Interpreting the Coefficients

Each coefficient $\hat{\beta}\_j$ (for $j = 1, 2, \ldots, p - 1$) represents the estimated change in $y$ for a one-unit increase in $x_j$, while holding all other predictors constant. This "holding other variables constant" interpretation is what distinguishes multiple regression from running separate simple regressions.

The intercept $\hat{\beta}\_0$ represents the estimated value of $y$ when all predictors are equal to zero.

## The Hat Matrix

The vector of fitted values is:

$$\hat{\mathbf{Y}} = \mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y} = \mathbf{H}\mathbf{Y},$$

where $\mathbf{H} = \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T$ is called the hat matrix. It "puts a hat on" $\mathbf{Y}$, transforming observed values into fitted values. The hat matrix is symmetric ($\mathbf{H}^T = \mathbf{H}$) and idempotent ($\mathbf{H}^2 = \mathbf{H}$).

The residual vector is:

$$\mathbf{e} = \mathbf{Y} - \hat{\mathbf{Y}} = (\mathbf{I} - \mathbf{H})\mathbf{Y}.$$

## Assumptions

The assumptions for multiple linear regression extend those of simple linear regression:

1. **Linearity**: $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, the model is linear in the parameters.
2. **Full rank**: The design matrix $\mathbf{X}$ has full column rank, meaning $\text{rank}(\mathbf{X}) = p$. This ensures $\mathbf{X}^T\mathbf{X}$ is invertible.
3. **Exogeneity**: $E(\boldsymbol{\varepsilon} | \mathbf{X}) = \mathbf{0}$, the errors have zero conditional mean.
4. **Homoscedasticity**: $\text{Var}(\boldsymbol{\varepsilon} | \mathbf{X}) = \sigma^2\mathbf{I}_n$, the errors have constant variance and are uncorrelated.
5. **Normality** (for inference): $\boldsymbol{\varepsilon} \sim N(\mathbf{0}, \sigma^2\mathbf{I}_n)$.

When assumptions 1 through 4 hold, the Gauss-Markov theorem guarantees that $\hat{\boldsymbol{\beta}}$ is the Best Linear Unbiased Estimator (BLUE).

## Connection to Simple Linear Regression

In the special case where $p = 2$, we have a single predictor $x$ and the design matrix becomes:

$$\mathbf{X} = \begin{pmatrix} 1 & x\_1 \\\\ 1 & x\_2 \\\\ \vdots & \vdots \\\\ 1 & x\_n \end{pmatrix}.$$

Computing $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ in this case yields the familiar results $\hat{\beta}_1 = S_{xy}/S_{xx}$ and $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$, confirming that the matrix formulation is a true generalization.

## Summary

In this post, we extended the regression framework to handle multiple predictors:

- The model $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ uses matrix notation to express the relationship compactly.
- The OLS estimator $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ generalizes the simple linear regression solution.
- Each $\hat{\beta}\_j$ measures the effect of one predictor while holding the others constant.
- The hat matrix $\mathbf{H}$ projects observed values onto fitted values.

In the next post, we will explore polynomial regression, which is a special case of multiple linear regression where the predictors are powers of a single variable.
