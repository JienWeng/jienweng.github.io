+++
title = "R-squared: SST, SSE, SSR and the Relationship with Correlation"
description = "Defining the coefficient of determination from the sum of squares decomposition and proving that R-squared equals the square of the correlation coefficient."
date = 2026-01-30
updated = 2026-01-30
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
5. **R-squared: SST, SSE, SSR and the Relationship with Correlation** (You are here)
6. [Standard Error in Regression](/posts/regression-06-standard-error)
7. [Confidence Intervals for Regression Coefficients](/posts/regression-07-confidence-intervals)
8. [Statistical Testing in Regression](/posts/regression-08-statistical-testing)
9. [ANOVA in Regression: SST, SSR, SSE and the F-Test](/posts/regression-09-anova)
{% end %}

In the [previous post](/posts/regression-04-correlation), we introduced the Pearson correlation coefficient $r$. In this post, we define the coefficient of determination $R^2$ through the decomposition of total variability, and then prove that $R^2 = r^2$ for simple linear regression.

## The Sum of Squares Decomposition

The total variability in the observed response values can be decomposed into two components: the variability explained by the regression model and the variability left unexplained (the residuals).

### Total Sum of Squares (SST)

$$SST = \sum^n_{i=1}(y_i - \bar{y})^2 = S_{yy}.$$

This measures the total variability of $y$ around its mean.

### Sum of Squares due to Regression (SSR)

$$SSR = \sum^n_{i=1}(\hat{y}_i - \bar{y})^2.$$

This measures the variability in $y$ that is explained by the regression model.

### Sum of Squared Errors (SSE)

$$SSE = \sum^n_{i=1}(y_i - \hat{y}_i)^2 = \sum^n_{i=1}e_i^2.$$

This measures the variability in $y$ that remains unexplained.

### The Identity

The fundamental decomposition is:

$$SST = SSR + SSE.$$

To see why this holds, write:

$$y_i - \bar{y} = (\hat{y}_i - \bar{y}) + (y_i - \hat{y}_i).$$

Squaring both sides and summing over all observations:

$$\sum^n_{i=1}(y_i - \bar{y})^2 = \sum^n_{i=1}(\hat{y}_i - \bar{y})^2 + \sum^n_{i=1}(y_i - \hat{y}_i)^2 + 2\sum^n_{i=1}(\hat{y}_i - \bar{y})(y_i - \hat{y}_i).$$

The cross term vanishes because of the properties of OLS residuals:

$$\sum^n_{i=1}(\hat{y}_i - \bar{y})(y_i - \hat{y}_i) = \sum^n_{i=1}(\hat{y}_i - \bar{y})e_i = 0.$$

This holds because OLS residuals are orthogonal to the fitted values. Therefore:

$$SST = SSR + SSE.$$

## The Coefficient of Determination $R^2$

The coefficient of determination is defined as:

$$R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}.$$

Both expressions are equivalent because $SSR = SST - SSE$.

The value of $R^2$ represents the proportion of the total variability in $y$ that is explained by the regression model:

- $R^2 = 1$: the model explains all the variability (all data points lie exactly on the fitted line).
- $R^2 = 0$: the model explains none of the variability (the fitted line is just $\hat{y} = \bar{y}$).
- $0 \leq R^2 \leq 1$: in general, $R^2$ lies between 0 and 1 for models with an intercept.

## Proof that $R^2 = r^2$ for Simple Linear Regression

We now prove that for simple linear regression, the coefficient of determination equals the square of the Pearson correlation coefficient.

### Step 1: Express SSR in terms of $S_{xx}$, $S_{xy}$

For simple linear regression, the fitted values are:

$$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i = (\bar{y} - \hat{\beta}_1\bar{x}) + \hat{\beta}_1 x_i = \bar{y} + \hat{\beta}_1(x_i - \bar{x}).$$

Therefore:

$$\hat{y}_i - \bar{y} = \hat{\beta}_1(x_i - \bar{x}).$$

Substituting into SSR:

$$SSR = \sum^n_{i=1}(\hat{y}_i - \bar{y})^2 = \hat{\beta}_1^2 \sum^n_{i=1}(x_i - \bar{x})^2 = \hat{\beta}_1^2 \cdot S_{xx}.$$

Since $\hat{\beta}_1 = S_{xy}/S_{xx}$:

$$SSR = \left(\frac{S_{xy}}{S_{xx}}\right)^2 S_{xx} = \frac{S_{xy}^2}{S_{xx}}.$$

### Step 2: Compute $R^2$

$$R^2 = \frac{SSR}{SST} = \frac{S_{xy}^2 / S_{xx}}{S_{yy}} = \frac{S_{xy}^2}{S_{xx} \cdot S_{yy}}.$$

### Step 3: Compare with $r^2$

From the [previous post](/posts/regression-04-correlation), the correlation coefficient is:

$$r = \frac{S_{xy}}{\sqrt{S_{xx} \cdot S_{yy}}}.$$

Squaring both sides:

$$r^2 = \frac{S_{xy}^2}{S_{xx} \cdot S_{yy}}.$$

Therefore:

$$R^2 = r^2. \quad \blacksquare$$

This result is elegant and important. It tells us that for simple linear regression, the proportion of variance explained by the model is exactly the square of the correlation between $x$ and $y$.

## Alternative Proof via SSE

We can also prove the result by expressing SSE in terms of $S_{xx}$, $S_{yy}$, $S_{xy}$.

Since $e_i = y_i - \hat{y}_i = y_i - \bar{y} - \hat{\beta}_1(x_i - \bar{x})$:

\begin{align*}
SSE &= \sum^n_{i=1}\left[(y_i - \bar{y}) - \hat{\beta}_1(x_i - \bar{x})\right]^2 \\
&= \sum^n_{i=1}(y_i - \bar{y})^2 - 2\hat{\beta}_1\sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y}) + \hat{\beta}_1^2\sum^n_{i=1}(x_i - \bar{x})^2 \\
&= S_{yy} - 2\hat{\beta}_1 S_{xy} + \hat{\beta}_1^2 S_{xx}.
\end{align*}

Substituting $\hat{\beta}_1 = S_{xy}/S_{xx}$:

\begin{align*}
SSE &= S_{yy} - 2 \cdot \frac{S_{xy}}{S_{xx}} \cdot S_{xy} + \frac{S_{xy}^2}{S_{xx}^2} \cdot S_{xx} \\
&= S_{yy} - \frac{2S_{xy}^2}{S_{xx}} + \frac{S_{xy}^2}{S_{xx}} \\
&= S_{yy} - \frac{S_{xy}^2}{S_{xx}}.
\end{align*}

Therefore:

$$R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{S_{yy} - S_{xy}^2/S_{xx}}{S_{yy}} = \frac{S_{xy}^2}{S_{xx} \cdot S_{yy}} = r^2.$$

## Adjusted $R^2$ for Multiple Regression

For multiple regression with $p$ parameters, $R^2$ always increases (or stays the same) when additional predictors are added, even if those predictors have no real relationship with $y$. To account for this, the adjusted $R^2$ penalizes for the number of predictors:

$$R^2_{\text{adj}} = 1 - \frac{SSE/(n - p)}{SST/(n - 1)} = 1 - \frac{n - 1}{n - p}(1 - R^2).$$

Unlike $R^2$, the adjusted version can decrease when an uninformative predictor is added, making it more suitable for model comparison.

Note that for simple linear regression ($p = 2$), $R^2 = r^2$ still holds, and $R^2_{\text{adj}}$ simplifies accordingly.

## Summary

In this post, we covered the sum of squares decomposition and the coefficient of determination:

- $SST = SSR + SSE$ decomposes total variability into explained and unexplained components.
- $R^2 = SSR/SST = 1 - SSE/SST$ measures the proportion of variance explained.
- For simple linear regression, $R^2 = r^2 = S_{xy}^2/(S_{xx} \cdot S_{yy})$, proven by expressing SSR in terms of $S_{xx}$ and $S_{xy}$.
- Adjusted $R^2$ penalizes for model complexity in multiple regression.

In the next post, we will derive the standard errors of the regression coefficients $\hat{\beta}_0$ and $\hat{\beta}_1$ using $S_{xx}$ and MSE.
