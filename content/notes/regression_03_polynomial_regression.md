+++
title = "Polynomial Regression"
description = "Understanding polynomial regression as a special case of multiple linear regression, with design matrix construction and overfitting considerations."
date = 2026-01-16
updated = 2026-01-16
draft = false
aliases = ["/posts/regression-03-polynomial-regression/"]

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

Polynomial regression keeps the linear estimation machinery but feeds it transformed features such as $x^2$ and $x^3$. This note shows when those terms capture curvature and when they mostly add variance.


The [previous note](@/notes/regression_02_multiple_linear_regression.md) introduced multiple linear regression using matrix notation. If the relationship between $x$ and $y$ is not a straight line, polynomial regression fits a polynomial in one variable. It is a special case of the multiple-regression framework.

## The Polynomial Model

A polynomial regression model of degree $d$ takes the form:

$$y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \cdots + \beta_d x_i^d + \varepsilon_i.$$

This model is nonlinear in the variable $x$, but it is still linear in the parameters $\beta_0, \beta_1, \ldots, \beta_d$. This distinction is important because it means we can use the same OLS estimation procedure from multiple linear regression.

For example, a quadratic model ($d = 2$) is:

$$y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \varepsilon_i,$$

and a cubic model ($d = 3$) is:

$$y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \beta_3 x_i^3 + \varepsilon_i.$$

## Design Matrix Construction

To fit a polynomial regression using the matrix approach, we define new variables:

$$z_1 = x, \quad z_2 = x^2, \quad z_3 = x^3, \quad \ldots, \quad z_d = x^d.$$

The design matrix for a polynomial of degree $d$ with $n$ observations is:

$$\mathbf{X} = \begin{pmatrix} 1 & x\_1 & x\_1^2 & \cdots & x\_1^d \\\\ 1 & x\_2 & x\_2^2 & \cdots & x\_2^d \\\\ \vdots & \vdots & \vdots & \ddots & \vdots \\\\ 1 & x\_n & x\_n^2 & \cdots & x\_n^d \end{pmatrix}.$$

This is exactly the design matrix for a multiple linear regression with $d$ predictors $z_1, z_2, \ldots, z_d$. Therefore, the OLS estimator is:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y},$$

which is the same formula derived in the previous note.

## Why Polynomial Regression is a Special Case of MLR

The key insight is that "linear" in "linear regression" refers to linearity in the parameters, not in the predictors. Although the polynomial model includes terms like $x^2$ and $x^3$, each coefficient $\beta\_j$ appears linearly. We can treat each power of $x$ as a separate predictor variable, and the entire OLS theory from multiple linear regression applies directly.

This means all the results we derived earlier carry over:

- The normal equations $\mathbf{X}^T\mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{X}^T\mathbf{Y}$ hold.
- The hat matrix $\mathbf{H} = \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T$ projects $\mathbf{Y}$ onto $\hat{\mathbf{Y}}$.
- Residual properties remain the same.

## Choosing the Degree

A natural question is: what degree $d$ should we use? The choice involves a tradeoff between model flexibility and model complexity.

- **Too low a degree** (underfitting): The model is not flexible enough to capture the true relationship, leading to large systematic errors.
- **Too high a degree** (overfitting): The model fits the training data very closely, including the noise, but performs poorly on new data.

A polynomial of degree $n - 1$ (where $n$ is the number of data points) can pass through every data point exactly, giving $SSE = 0$. However, such a model almost always overfits and generalizes badly.

Common approaches to select the degree include:

1. **Visual inspection**: Plot the data and the fitted curve for different degrees, and choose the one that captures the trend without fitting the noise.
2. **Cross-validation**: Split the data into training and validation sets, fit models of various degrees on the training set, and select the degree with the lowest prediction error on the validation set.
3. **Information criteria**: Use metrics such as the Akaike Information Criterion (AIC) or the Bayesian Information Criterion (BIC) to balance goodness of fit with model complexity.

## Multicollinearity Considerations

One practical concern with polynomial regression is multicollinearity. The predictors $x, x^2, x^3, \ldots$ are often highly correlated, especially when $x$ values span a narrow range. High multicollinearity inflates the variance of the coefficient estimates and makes $\mathbf{X}^T\mathbf{X}$ nearly singular.

A common remedy is to center the predictor before constructing polynomial terms. Instead of using $x$, we use $x - \bar{x}$:

$$z_1 = x - \bar{x}, \quad z_2 = (x - \bar{x})^2, \quad z_3 = (x - \bar{x})^3, \quad \ldots$$

Centering reduces the correlation among the polynomial terms and improves the numerical stability of the estimation.

Another approach is to use orthogonal polynomials, which are constructed so that $\mathbf{X}^T\mathbf{X}$ is diagonal, eliminating multicollinearity entirely.

## Example: Quadratic Fit

Consider a quadratic model $y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \varepsilon_i$ with the design matrix:

$$\mathbf{X} = \begin{pmatrix} 1 & x\_1 & x\_1^2 \\\\ 1 & x\_2 & x\_2^2 \\\\ \vdots & \vdots & \vdots \\\\ 1 & x\_n & x\_n^2 \end{pmatrix}.$$

There are $p = 3$ parameters. The OLS solution $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ gives us $\hat{\beta}\_0$, $\hat{\beta}\_1$, and $\hat{\beta}\_2$ simultaneously. The coefficient $\hat{\beta}\_2$ indicates the curvature of the fitted parabola: a positive $\hat{\beta}\_2$ means the curve opens upward, and a negative $\hat{\beta}\_2$ means it opens downward.

## Summary

Polynomial regression follows from five observations:

- The polynomial model $y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \cdots + \beta_d x_i^d + \varepsilon_i$ is nonlinear in $x$ but linear in the parameters.
- By treating each power of $x$ as a separate predictor, polynomial regression becomes a special case of multiple linear regression.
- The OLS estimator $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ applies directly.
- Choosing the polynomial degree requires balancing fit and complexity to avoid overfitting.
- Centering or using orthogonal polynomials helps address multicollinearity.

The next note uses $S\_{xx}$, $S\_{yy}$, and $S\_{xy}$ to define correlation.
