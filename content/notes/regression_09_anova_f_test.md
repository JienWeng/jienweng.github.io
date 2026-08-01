+++
title = "ANOVA and the F-Test in Regression"
description = "Building the ANOVA table from the sum of squares decomposition, deriving the F statistic as MSR/MSE, and showing that F = t-squared in simple linear regression."
date = 2026-07-02
updated = 2026-07-02
draft = true
aliases = ["/posts/regression-09-anova-f-test/"]

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

This note builds the ANOVA framework for regression and derives the F-test for overall model significance. The question it answers is whether the model as a whole explains anything, before asking which individual predictors matter. It also shows that in simple linear regression the F-test and the slope t-test are the same test.

In the [previous post](/posts/regression-08-statistical-testing), we tested regression coefficients one at a time with t-tests. Each t-test asks a narrow question: does this particular predictor have an effect? The F-test asks the broader question first: does the model explain any of the variability in $y$ at all? The machinery for answering it is the Analysis of Variance (ANOVA), and it is built entirely from quantities we already have.

## The Question the F-Test Asks

Consider the multiple regression model with $p$ parameters (an intercept and $k = p - 1$ slopes):

$$y\_i = \beta\_0 + \beta\_1 x\_{i1} + \beta\_2 x\_{i2} + \cdots + \beta\_k x\_{ik} + \varepsilon\_i.$$

The overall significance test puts every slope on trial simultaneously:

$$H\_0: \beta\_1 = \beta\_2 = \cdots = \beta\_k = 0,$$
$$H\_1: \text{at least one } \beta\_j \neq 0.$$

Under $H\_0$, none of the predictors carries any linear information about $y$, and the best model is simply $\hat{y} = \bar{y}$. Under $H\_1$, at least one predictor helps. Note what the alternative does not say: it does not tell us which slope is nonzero, only that the model is not entirely useless. Identifying the responsible predictors is the job of the individual t-tests from the previous post.

## Revisiting the Sum of Squares Decomposition

The starting point is the identity we proved in the [post on R-squared](/posts/regression-05-r-squared-and-correlation):

$$SST = SSR + SSE,$$

where

$$SST = \sum^n\_{i=1}(y\_i - \bar{y})^2, \quad SSR = \sum^n\_{i=1}(\hat{y}\_i - \bar{y})^2, \quad SSE = \sum^n\_{i=1}(y\_i - \hat{y}\_i)^2.$$

The total variability of $y$ splits cleanly into a part the model explains (SSR) and a part it does not (SSE). The whole idea of ANOVA is to compare the sizes of these two pieces. If the model is genuinely useful, SSR should be large relative to SSE. But "large relative to" needs a fair basis of comparison, because SSR and SSE are sums over different numbers of free quantities. That is what degrees of freedom provide.

## Degrees of Freedom

Each sum of squares has an associated number of degrees of freedom, counting how many independent pieces of information it is built from:

- **SST** has $n - 1$ degrees of freedom: there are $n$ deviations $y\_i - \bar{y}$, but they sum to zero, which removes one.
- **SSR** has $p - 1 = k$ degrees of freedom: the fitted values are determined by the $p$ estimated parameters, and one of them (the intercept) is absorbed by centering around $\bar{y}$.
- **SSE** has $n - p$ degrees of freedom: $n$ residuals, constrained by the $p$ normal equations.

The degrees of freedom add up exactly as the sums of squares do:

$$(n - 1) = (p - 1) + (n - p).$$

For simple linear regression ($p = 2$), this reads $(n-1) = 1 + (n-2)$: one degree of freedom for the slope, $n - 2$ for the residuals, matching the denominator of MSE from the [standard error post](/posts/regression-06-standard-error).

## Mean Squares

Dividing each sum of squares by its degrees of freedom gives a mean square, which is a variance-like quantity on a per-degree-of-freedom scale:

$$MSR = \frac{SSR}{p - 1}, \quad MSE = \frac{SSE}{n - p}.$$

We already know from the standard error post that MSE is an unbiased estimator of the error variance:

$$E(MSE) = \sigma^2.$$

The expectation of MSR is what makes the test work. For simple linear regression, it can be shown that:

$$E(MSR) = \sigma^2 + \beta\_1^2 S\_{xx}.$$

Read these two expectations side by side. If $H\_0$ is true ($\beta\_1 = 0$), then $E(MSR) = \sigma^2 = E(MSE)$: both mean squares estimate the same quantity, and their ratio should hover around 1. If $H\_0$ is false, MSR picks up the extra term $\beta\_1^2 S\_{xx} > 0$ and systematically exceeds MSE. The same logic carries over to multiple regression, where the extra term involves all the slopes. A useful model inflates MSR; a useless one does not.

## The F Statistic

This suggests the test statistic:

$$F = \frac{MSR}{MSE} = \frac{SSR / (p - 1)}{SSE / (n - p)}.$$

Under $H\_0$ and the normality assumption, SSR and SSE are independent scaled chi-squared random variables with $p - 1$ and $n - p$ degrees of freedom respectively, so their ratio of mean squares follows an F-distribution:

$$F \sim F\_{p-1,\, n-p}.$$

The decision rule at significance level $\alpha$ is:

**Reject $H\_0$** if $F > F\_{\alpha,\, p-1,\, n-p}$.

Note that the test is one-sided even though the alternative hypothesis is not directional in the usual sense. Departures from $H\_0$ in any direction inflate SSR, so only large values of $F$ constitute evidence against the null. A value of $F$ near 1 means the model explains about as much per degree of freedom as random noise would.

## The ANOVA Table

The standard way to organize all of this is the ANOVA table, which every regression software prints in essentially the same layout:

| Source     | SS    | df      | MS                    | F           |
|------------|-------|---------|-----------------------|-------------|
| Regression | $SSR$ | $p - 1$ | $MSR = SSR/(p-1)$     | $MSR / MSE$ |
| Error      | $SSE$ | $n - p$ | $MSE = SSE/(n-p)$     |             |
| Total      | $SST$ | $n - 1$ |                       |             |

Each row is a bookkeeping line for one component of variability. The SS column adds down to SST, the df column adds down to $n - 1$, and the single number in the F column summarizes the overall test. The table also hands us $R^2 = SSR/SST$ for free, since both entries appear in the SS column.

## Relation to the t-Test: $F = t^2$

For simple linear regression there is only one slope, so the overall F-test and the t-test for $H\_0: \beta\_1 = 0$ are answering the same question. They are in fact the same test.

From the R-squared post, $SSR = S\_{xy}^2 / S\_{xx}$. With $p - 1 = 1$, we have $MSR = SSR$, so:

$$F = \frac{MSR}{MSE} = \frac{S\_{xy}^2 / S\_{xx}}{MSE} = \frac{S\_{xy}^2}{MSE \cdot S\_{xx}} = \left(\frac{S\_{xy}}{\sqrt{MSE \cdot S\_{xx}}}\right)^2.$$

The quantity inside the parentheses is exactly the t-statistic for the slope derived in the previous post:

$$t = \frac{\hat{\beta}\_1}{SE(\hat{\beta}\_1)} = \frac{S\_{xy}}{\sqrt{MSE \cdot S\_{xx}}}.$$

Therefore:

$$F = t^2.$$

The critical values agree as well: $F\_{\alpha,\, 1,\, n-2} = t\_{\alpha/2,\, n-2}^2$, so the two tests always reach the same decision and produce the same p-value. This identity holds only in simple regression. Once there are two or more slopes, the F-test aggregates evidence across all of them and is no longer equivalent to any single t-test.

## Worked Example

Consider five observations:

$$(x, y) \in \\{(1, 2),\ (2, 3),\ (3, 5),\ (4, 6),\ (5, 9)\\}.$$

The sample means are $\bar{x} = 3$ and $\bar{y} = 5$, and the summary statistics are:

$$S\_{xx} = 10, \quad S\_{yy} = 30, \quad S\_{xy} = 17.$$

The OLS estimates follow from the formulas in the [first post](/posts/regression-01-simple-linear-regression):

$$\hat{\beta}\_1 = \frac{S\_{xy}}{S\_{xx}} = \frac{17}{10} = 1.7, \quad \hat{\beta}\_0 = \bar{y} - \hat{\beta}\_1\bar{x} = 5 - 1.7 \times 3 = -0.1.$$

The sums of squares are:

$$SST = S\_{yy} = 30, \quad SSR = \frac{S\_{xy}^2}{S\_{xx}} = \frac{289}{10} = 28.9, \quad SSE = 30 - 28.9 = 1.1.$$

With $n = 5$ and $p = 2$, the ANOVA table is:

| Source     | SS     | df  | MS       | F       |
|------------|--------|-----|----------|---------|
| Regression | 28.9   | 1   | 28.9     | 78.82   |
| Error      | 1.1    | 3   | 0.3667   |         |
| Total      | 30     | 4   |          |         |

Here $MSE = 1.1/3 \approx 0.3667$ and $F = 28.9 / 0.3667 \approx 78.82$. The critical value at $\alpha = 0.05$ is $F\_{0.05,\, 1,\, 3} = 10.13$, so we reject $H\_0$ decisively: the regression explains a significant share of the variability in $y$. Consistently, $R^2 = 28.9/30 \approx 0.963$.

To verify the $F = t^2$ identity, compute the slope t-test from the previous post:

$$t = \frac{\hat{\beta}\_1}{\sqrt{MSE / S\_{xx}}} = \frac{1.7}{\sqrt{0.3667 / 10}} \approx \frac{1.7}{0.1915} \approx 8.878,$$

and indeed $t^2 \approx 78.82 = F$. The critical values match too: $t\_{0.025,\, 3} = 3.182$ and $3.182^2 \approx 10.13$.

## Summary

In this post, we built the ANOVA framework for regression:

- The F-test asks whether the model explains anything at all: $H\_0: \beta\_1 = \cdots = \beta\_k = 0$ against the alternative that at least one slope is nonzero.
- The decomposition $SST = SSR + SSE$ from the R-squared post carries over, with degrees of freedom $(n-1) = (p-1) + (n-p)$.
- Mean squares put the components on a comparable scale: $MSR = SSR/(p-1)$ and $MSE = SSE/(n-p)$, with $E(MSE) = \sigma^2$ always and $E(MSR) > \sigma^2$ only when some slope is nonzero.
- The statistic $F = MSR/MSE$ follows $F\_{p-1,\, n-p}$ under $H\_0$, and large values reject.
- In simple linear regression, $F = t^2$: the overall F-test and the slope t-test are the same test.
- The ANOVA table organizes the sums of squares, degrees of freedom, and the F statistic in one place.

A significant F tells us the model is better than no model; it does not tell us which predictors are responsible, whether the linear form is right, or whether the model predicts well out of sample. Those questions belong to the individual t-tests, residual diagnostics, and validation on new data.
