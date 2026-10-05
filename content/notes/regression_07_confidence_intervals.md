+++
title = "Confidence Intervals for Regression Coefficients"
description = "Constructing confidence intervals for beta_0, beta_1, and beta_i using the t-distribution and standard errors."
date = 2026-02-13
updated = 2026-02-13
draft = false
aliases = ["/posts/regression-07-confidence-intervals/"]

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

Confidence intervals turn a coefficient estimate into a range that reflects sampling uncertainty. This note connects standard errors and critical values to that range, then works through its interpretation.


The [previous note](@/notes/regression_06_standard_error.md) derived the standard errors of the regression coefficients. Standard errors describe estimate precision, but they do not give a range of plausible values for the true parameters. Confidence intervals do.

## The Sampling Distribution of $\hat{\beta}\_j$

Under the normality assumption $\varepsilon\_i \sim N(0, \sigma^2)$, the OLS estimators are also normally distributed:

$$\hat{\beta}\_j \sim N\left(\beta\_j, \sigma^2 C\_{jj}\right),$$

where $C\_{jj}$ is the appropriate diagonal element of $(\mathbf{X}^T\mathbf{X})^{-1}$.

Standardizing gives:

$$\frac{\hat{\beta}\_j - \beta\_j}{\sigma\sqrt{C\_{jj}}} \sim N(0, 1).$$

However, $\sigma^2$ is unknown and we replace it with $MSE$. This introduces additional uncertainty, and the resulting distribution changes from a standard normal to a t-distribution:

$$\frac{\hat{\beta}\_j - \beta\_j}{SE(\hat{\beta}\_j)} \sim t\_{n - p},$$

where $SE(\hat{\beta}\_j) = \sqrt{MSE \cdot C\_{jj}}$ and $n - p$ is the degrees of freedom.

## Confidence Interval Formula

A confidence interval with confidence level $1 - \alpha$ for $\beta\_j$ is:

$$\hat{\beta}\_j \pm t\_{\alpha/2,\, n-p} \cdot SE(\hat{\beta}\_j),$$

where $t\_{\alpha/2, n-p}$ is the critical value from the t-distribution with $n - p$ degrees of freedom such that $P(|T| > t\_{\alpha/2, n-p}) = \alpha$.

Equivalently, the interval is:

$$\left[\hat{\beta}\_j - t\_{\alpha/2,\, n-p} \cdot SE(\hat{\beta}\_j), \quad \hat{\beta}\_j + t\_{\alpha/2,\, n-p} \cdot SE(\hat{\beta}\_j)\right].$$

## Confidence Interval for $\beta\_1$ (Simple Linear Regression)

For the slope in simple linear regression, $n - p = n - 2$:

$$\hat{\beta}\_1 \pm t\_{\alpha/2,\, n-2} \cdot SE(\hat{\beta}\_1),$$

where:

$$SE(\hat{\beta}\_1) = \sqrt{\frac{MSE}{S\_{xx}}}.$$

Expanding fully:

$$\hat{\beta}\_1 \pm t\_{\alpha/2,\, n-2} \cdot \sqrt{\frac{SSE}{(n-2) \cdot S\_{xx}}}.$$

This interval is centered at the OLS estimate $\hat{\beta}\_1$ and its width depends on three factors:

1. **Confidence level** ($1 - \alpha$): Higher confidence means a wider interval (larger $t\_{\alpha/2}$).
2. **Residual variability** ($MSE$): More noise means a wider interval.
3. **Predictor variability** ($S\_{xx}$): More spread in $x$ means a narrower interval.

## Confidence Interval for $\beta\_0$ (Simple Linear Regression)

For the intercept:

$$\hat{\beta}\_0 \pm t\_{\alpha/2,\, n-2} \cdot SE(\hat{\beta}\_0),$$

where:

$$SE(\hat{\beta}\_0) = \sqrt{MSE\left(\frac{1}{n} + \frac{\bar{x}^2}{S\_{xx}}\right)}.$$

The intercept's confidence interval is typically wider than the slope's because the variance of $\hat{\beta}\_0$ includes an extra term involving $\bar{x}^2/S\_{xx}$. When $\bar{x}$ is far from zero, the intercept estimate becomes less precise.

## General Confidence Interval for $\beta\_i$ (Multiple Regression)

For any coefficient $\beta\_i$ in the multiple regression model:

$$\hat{\beta}\_i \pm t\_{\alpha/2,\, n-p} \cdot SE(\hat{\beta}\_i),$$

where:

$$SE(\hat{\beta}\_i) = \sqrt{MSE \cdot C\_{ii}}$$

and $C\_{ii}$ is the $(i+1)$-th diagonal element of $(\mathbf{X}^T\mathbf{X})^{-1}$.

The degrees of freedom are $n - p$, reflecting that $p$ parameters have been estimated. As more predictors are included (larger $p$), fewer degrees of freedom remain, and the critical value $t\_{\alpha/2, n-p}$ increases, widening the intervals.

## Interpretation of Confidence Intervals

A 95% confidence interval for $\beta\_1$ does not mean there is a 95% probability that $\beta\_1$ lies within the interval. The true parameter $\beta\_1$ is a fixed (though unknown) constant; it either lies in the interval or it does not.

The correct interpretation is: if we were to repeat the experiment many times and construct a 95% confidence interval each time, approximately 95% of those intervals would contain the true value $\beta\_1$.

## When the Interval Contains Zero

If the confidence interval for $\beta\_j$ includes zero, this suggests that the data are consistent with $\beta\_j = 0$, meaning the predictor $x\_j$ may not have a statistically significant linear effect on $y$ at the chosen confidence level.

Conversely, if the interval does not include zero, we have evidence that the predictor has a significant effect. The next note connects this result to formal hypothesis tests.

## Confidence Interval for the Mean Response

We can also construct a confidence interval for the mean response at a given value $x\_0$. The estimated mean response is:

$$\hat{y}\_0 = \hat{\beta}\_0 + \hat{\beta}\_1 x\_0.$$

The variance of this estimate is:

$$\text{Var}(\hat{y}\_0) = \sigma^2\left(\frac{1}{n} + \frac{(x\_0 - \bar{x})^2}{S\_{xx}}\right).$$

The confidence interval for the mean response is:

$$\hat{y}\_0 \pm t\_{\alpha/2,\, n-2} \cdot \sqrt{MSE\left(\frac{1}{n} + \frac{(x\_0 - \bar{x})^2}{S\_{xx}}\right)}.$$

Notice that this interval is narrowest when $x\_0 = \bar{x}$ and grows wider as $x\_0$ moves away from $\bar{x}$. This reflects the fact that we are most confident about predictions near the center of the data.

## Summary

Confidence intervals for regression coefficients follow from these five facts:

- The pivotal quantity $(\hat{\beta}\_j - \beta\_j)/SE(\hat{\beta}\_j) \sim t\_{n-p}$ forms the basis for inference.
- For $\beta\_1$: $\hat{\beta}\_1 \pm t\_{\alpha/2, n-2} \cdot \sqrt{MSE/S\_{xx}}$.
- For $\beta\_0$: $\hat{\beta}\_0 \pm t\_{\alpha/2, n-2} \cdot \sqrt{MSE(1/n + \bar{x}^2/S\_{xx})}$.
- For any $\beta\_i$ in multiple regression: $\hat{\beta}\_i \pm t\_{\alpha/2, n-p} \cdot \sqrt{MSE \cdot C\_{ii}}$.
- Interval width depends on the confidence level, residual variability, predictor spread, and sample size.

The next note uses the same t-distribution framework for formal hypothesis tests on regression coefficients.
