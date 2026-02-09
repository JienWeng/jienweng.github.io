+++
title = "Correlation"
description = "Defining the Pearson correlation coefficient using Sxx, Syy, Sxy, Sx, and Sy notation, and exploring its properties."
date = 2026-01-23
updated = 2026-01-23
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
4. **Correlation** (You are here)
5. [R-squared: SST, SSE, SSR and the Relationship with Correlation](/posts/regression-05-r-squared-and-correlation)
6. [Standard Error in Regression](/posts/regression-06-standard-error)
7. [Confidence Intervals for Regression Coefficients](/posts/regression-07-confidence-intervals)
8. [Statistical Testing in Regression](/posts/regression-08-statistical-testing)
9. [ANOVA in Regression: SST, SSR, SSE and the F-Test](/posts/regression-09-anova)
{% end %}

In the previous posts, we built the regression framework using $S_{xx}$ and $S_{xy}$ to derive the OLS estimators. Before we move to deeper inferential topics, it is essential to formalize a measure of the strength of the linear association between two variables. This measure is the Pearson correlation coefficient.

## Recap of Key Notation

In [Post 1](/posts/regression-01-simple-linear-regression), we introduced:

$$S_{xx} = \sum^n_{i=1}(x_i - \bar{x})^2,$$

$$S_{xy} = \sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y}).$$

We now introduce the remaining quantity:

$$S_{yy} = \sum^n_{i=1}(y_i - \bar{y})^2.$$

These three summary statistics capture the variability of $x$, the variability of $y$, and their joint variability, respectively.

## Sample Standard Deviations

The sample standard deviations are defined as:

$$S_x = \sqrt{\frac{S_{xx}}{n - 1}} = \sqrt{\frac{1}{n-1}\sum^n_{i=1}(x_i - \bar{x})^2},$$

$$S_y = \sqrt{\frac{S_{yy}}{n - 1}} = \sqrt{\frac{1}{n-1}\sum^n_{i=1}(y_i - \bar{y})^2}.$$

Note that $S_x$ and $S_y$ are the standard deviations using the $n - 1$ denominator (Bessel's correction), which gives unbiased estimates of the population standard deviations $\sigma_x$ and $\sigma_y$.

The sample variances are simply:

$$S_x^2 = \frac{S_{xx}}{n-1}, \quad S_y^2 = \frac{S_{yy}}{n-1}.$$

## The Pearson Correlation Coefficient

The sample Pearson correlation coefficient is defined as:

$$r = \frac{S_{xy}}{\sqrt{S_{xx} \cdot S_{yy}}}.$$

Equivalently, using the standard deviations:

$$r = \frac{\sum^n_{i=1}(x_i - \bar{x})(y_i - \bar{y})}{(n-1) S_x S_y} = \frac{S_{xy}}{(n-1) S_x S_y}.$$

The first form (using $S_{xx}$, $S_{yy}$, $S_{xy}$) is often more convenient for algebraic manipulation, while the second form highlights that $r$ is a standardized measure of covariation.

## Properties of the Correlation Coefficient

The Pearson correlation coefficient has several important properties:

### 1. Bounded between -1 and 1

$$-1 \leq r \leq 1.$$

This follows from the Cauchy-Schwarz inequality, which states that $(S_{xy})^2 \leq S_{xx} \cdot S_{yy}$, with equality only when all data points lie exactly on a line.

### 2. Interpretation of values

- $r = 1$: perfect positive linear relationship (all points on a line with positive slope).
- $r = -1$: perfect negative linear relationship (all points on a line with negative slope).
- $r = 0$: no linear relationship (but there may be a nonlinear relationship).
- $0 < |r| < 1$: partial linear association, with strength increasing as $|r|$ approaches 1.

### 3. Symmetry

$$r_{xy} = r_{yx}.$$

The correlation between $x$ and $y$ is the same as the correlation between $y$ and $x$. This follows because $S_{xy}$ is symmetric in $x$ and $y$.

### 4. Invariance under linear transformation

If we define $u_i = a + bx_i$ and $v_i = c + dy_i$ with $b > 0$ and $d > 0$, then the correlation between $u$ and $v$ equals the correlation between $x$ and $y$. If either $b$ or $d$ is negative (but not both), the sign of $r$ flips.

### 5. Dimensionless

The correlation coefficient has no units. The numerator $S_{xy}$ has units of $x$ times $y$, and the denominator $\sqrt{S_{xx} \cdot S_{yy}}$ also has units of $x$ times $y$, so they cancel.

## Relationship to the Regression Slope

Recall from Post 1 that the OLS slope estimator is $\hat{\beta}_1 = S_{xy}/S_{xx}$. The correlation coefficient can be expressed in terms of $\hat{\beta}_1$:

$$r = \hat{\beta}_1 \sqrt{\frac{S_{xx}}{S_{yy}}} = \hat{\beta}_1 \cdot \frac{S_x}{S_y}.$$

This shows that $r$ and $\hat{\beta}_1$ always share the same sign. A positive slope corresponds to a positive correlation, and a negative slope corresponds to a negative correlation.

Conversely, we can write the slope as:

$$\hat{\beta}_1 = r \cdot \frac{S_y}{S_x}.$$

This expresses the regression slope as the correlation times the ratio of the standard deviations.

## Population Correlation

The sample correlation $r$ estimates the population correlation coefficient $\rho$ (rho), defined for a bivariate population as:

$$\rho = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{E[(X - \mu_X)(Y - \mu_Y)]}{\sigma_X \sigma_Y}.$$

When the data $(x_i, y_i)$ are sampled from a bivariate normal distribution, $r$ is a consistent estimator of $\rho$.

## Correlation Does Not Imply Causation

A frequently cited caveat: a strong correlation between two variables does not mean that one causes the other. The association might be due to a lurking variable, reverse causation, or coincidence. Regression models describe associations; establishing causation requires careful experimental design or additional assumptions.

## Summary

In this post, we introduced the Pearson correlation coefficient:

- $S_{yy} = \sum(y_i - \bar{y})^2$ completes the set of summary statistics alongside $S_{xx}$ and $S_{xy}$.
- The sample standard deviations $S_x = \sqrt{S_{xx}/(n-1)}$ and $S_y = \sqrt{S_{yy}/(n-1)}$ measure spread.
- The correlation $r = S_{xy}/\sqrt{S_{xx} \cdot S_{yy}}$ quantifies the strength of the linear relationship.
- $r$ is bounded between $-1$ and $1$, symmetric, and dimensionless.
- The regression slope and correlation are related by $\hat{\beta}_1 = r \cdot S_y / S_x$.

In the next post, we will define $R^2$ using SST, SSE, and SSR, and prove mathematically that $R^2 = r^2$ for simple linear regression.
