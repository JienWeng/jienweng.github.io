+++
title = "R-squared: SST, SSE, SSR and the Relationship with Correlation"
description = "Defining the coefficient of determination from the sum of squares decomposition and proving that R-squared equals the square of the correlation coefficient."
date = 2026-01-30
updated = 2026-01-30
draft = false
aliases = ["/posts/regression-05-r-squared-and-correlation/"]

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

SST, SSR, and SSE split the variation in a response into a fitted part and a residual part. This note uses that decomposition to derive $R^2$, connect it to correlation, and show why a high $R^2$ can still mislead.


The [previous note](@/notes/regression_04_correlation.md) introduced the Pearson correlation coefficient $r$. Here, the coefficient of determination $R^2$ comes from the decomposition of total variability, and for simple linear regression it satisfies $R^2 = r^2$.

## The Sum of Squares Decomposition

The total variability in the observed response values can be decomposed into two components: the variability explained by the regression model and the variability left unexplained (the residuals).

### Total Sum of Squares (SST)

$$SST = \sum^n\_{i=1}(y\_i - \bar{y})^2 = S\_{yy}.$$

This measures the total variability of $y$ around its mean.

### Sum of Squares due to Regression (SSR)

$$SSR = \sum^n\_{i=1}(\hat{y}\_i - \bar{y})^2.$$

This measures the variability in $y$ that is explained by the regression model.

### Sum of Squared Errors (SSE)

$$SSE = \sum^n\_{i=1}(y\_i - \hat{y}\_i)^2.$$

This measures the variability in $y$ that remains unexplained.

### The Identity

The fundamental decomposition is:

$$SST = SSR + SSE.$$

To see why this holds, write:

$$y\_i - \bar{y} = (\hat{y}\_i - \bar{y}) + (y\_i - \hat{y}\_i).$$

Squaring both sides and summing over all observations:

$$\sum\_{i=1}^n (y\_i - \bar{y})^2 = \sum\_{i=1}^n (\hat{y}\_i - \bar{y})^2 + \sum\_{i=1}^n (y\_i - \hat{y}\_i)^2 + 2\sum\_{i=1}^n (\hat{y}\_i - \bar{y})(y\_i - \hat{y}\_i).$$

The cross term vanishes because of the properties of OLS residuals:

$$\sum\_{i=1}^n (\hat{y}\_i - \bar{y})(y\_i - \hat{y}\_i) = \sum\_{i=1}^n (\hat{y}\_i - \bar{y})\,e\_i = 0.$$ 

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

### Step 1: Express SSR in terms of $S\_{xx}$, $S\_{xy}$

For simple linear regression, the fitted values are:

$$\hat{y}\_i = \hat{\beta}\_0 + \hat{\beta}\_1 x\_i = (\bar{y} - \hat{\beta}\_1\bar{x}) + \hat{\beta}\_1 x\_i = \bar{y} + \hat{\beta}\_1(x\_i - \bar{x}).$$

Therefore:

$$\hat{y}\_i - \bar{y} = \hat{\beta}\_1(x\_i - \bar{x}).$$

Substituting into SSR:

$$SSR = \sum\_{i=1}^n (\hat{y}\_i - \bar{y})^2 = \hat{\beta}\_1^2 \sum\_{i=1}^n (x\_i - \bar{x})^2 = \hat{\beta}\_1^2 \cdot S\_{xx}.$$ 

Since $\hat{\beta}\_1 = S\_{xy}/S\_{xx}$:

$$SSR = \left(\frac{S\_{xy}}{S\_{xx}}\right)^2 S\_{xx} = \frac{S\_{xy}^2}{S\_{xx}}.$$

### Step 2: Compute $R^2$

$$R^2 = \frac{SSR}{SST} = \frac{S\_{xy}^2 / S\_{xx}}{S\_{yy}} = \frac{S\_{xy}^2}{S\_{xx} \cdot S\_{yy}}.$$

### Step 3: Compare with $r^2$

From the [previous note](@/notes/regression_04_correlation.md), the correlation coefficient is:

$$r = \frac{S\_{xy}}{\sqrt{S\_{xx} \cdot S\_{yy}}}.$$

Squaring both sides:

$$r^2 = \frac{S\_{xy}^2}{S\_{xx} \cdot S\_{yy}}.$$

Therefore:

$$R^2 = r^2. \quad \blacksquare$$

This result is elegant and important. It tells us that for simple linear regression, the proportion of variance explained by the model is exactly the square of the correlation between $x$ and $y$.

## Alternative Proof via SSE

We can also prove the result by expressing SSE in terms of $S\_{xx}$, $S\_{yy}$, $S\_{xy}$.

Since $e\_i = y\_i - \hat{y}\_i = y\_i - \bar{y} - \hat{\beta}\_1(x\_i - \bar{x})$:

$$\begin{aligned}
SSE &= \sum\_{i=1}^n \big[(y\_i - \bar{y}) - \hat{\beta}\_1 (x\_i - \bar{x})\big]^2 \\\\
&= \sum\_{i=1}^n (y\_i - \bar{y})^2 - 2\hat{\beta}\_1 \sum\_{i=1}^n (x\_i - \bar{x})(y\_i - \bar{y}) + \hat{\beta}\_1^2 \sum\_{i=1}^n (x\_i - \bar{x})^2 \\\\
&= S\_{yy} - 2\hat{\beta}\_1 S\_{xy} + \hat{\beta}\_1^2 S\_{xx}.
\end{aligned}$$

Substituting $\hat{\beta}\_1 = S\_{xy}/S\_{xx}$:

$$\begin{aligned}
SSE &= S\_{yy} - 2\cdot\frac{S\_{xy}}{S\_{xx}}\cdot S\_{xy} + \frac{S\_{xy}^2}{S\_{xx}^2}\cdot S\_{xx} \\\\
&= S\_{yy} - \frac{2S\_{xy}^2}{S\_{xx}} + \frac{S\_{xy}^2}{S\_{xx}} \\\\
&= S\_{yy} - \frac{S\_{xy}^2}{S\_{xx}}.
\end{aligned}$$

Therefore:

$$R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{S\_{yy} - S\_{xy}^2/S\_{xx}}{S\_{yy}} = \frac{S\_{xy}^2}{S\_{xx} \cdot S\_{yy}} = r^2.$$

## Adjusted $R^2$ for Multiple Regression

For multiple regression with $p$ parameters, $R^2$ always increases (or stays the same) when additional predictors are added, even if those predictors have no real relationship with $y$. To account for this, the adjusted $R^2$ penalizes for the number of predictors:

$$R^2\_{\text{adj}} = 1 - \frac{SSE/(n - p)}{SST/(n - 1)} = 1 - \frac{n - 1}{n - p}(1 - R^2).$$

Unlike $R^2$, the adjusted version can decrease when an uninformative predictor is added, making it more suitable for model comparison.

Note that for simple linear regression ($p = 2$), $R^2 = r^2$ still holds, and $R^2\_{\text{adj}}$ simplifies accordingly.

## Where a High R-squared Can Mislead

Everything above describes what $R^2$ measures. It is equally important to be clear about what it does not measure.

First, $R^2$ quantifies fit, not correctness. It tells us how much of the variability in $y$ is captured by the fitted line, but it says nothing about whether a line was the right model to fit. A clearly nonlinear pattern can still produce a high $R^2$ if the linear component happens to be strong. Anscombe's quartet is the classic reference here: four datasets with essentially identical $R^2$ (and identical fitted lines), one of which is a clean linear relationship, one a perfect parabola, and two dominated by single outlying points. The residual plot distinguishes them; $R^2$ does not.

Second, plain $R^2$ never decreases when a predictor is added. Since OLS minimizes SSE over a strictly larger space of models, SSE can only stay the same or shrink, so $R^2 = 1 - SSE/SST$ can only stay the same or grow, even when the new predictor is pure noise. This is exactly the problem the adjusted $R^2$ above is designed to correct.

Third, a high $R^2$ is not evidence of causation, and it is not a measure of predictive performance on new data. It is computed on the same observations used to fit the model, so it says nothing about how the model generalizes out of sample.

## Summary

The sum-of-squares decomposition gives four useful results:

- $SST = SSR + SSE$ decomposes total variability into explained and unexplained components.
- $R^2 = SSR/SST = 1 - SSE/SST$ measures the proportion of variance explained.
- For simple linear regression, $R^2 = r^2 = S\_{xy}^2/(S\_{xx} \cdot S\_{yy})$, proven by expressing SSR in terms of $S\_{xx}$ and $S\_{xy}$.
- Adjusted $R^2$ penalizes for model complexity in multiple regression.

The next note derives the standard errors of $\hat{\beta}\_0$ and $\hat{\beta}\_1$ using $S\_{xx}$ and MSE.
