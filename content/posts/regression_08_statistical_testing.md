+++
title = "Statistical Testing in Regression"
description = "Performing hypothesis tests on regression coefficients using t-tests, p-values, and the connection to confidence intervals."
date = 2026-02-20
updated = 2026-02-20
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
6. [Standard Error in Regression](/posts/regression-06-standard-error)
7. [Confidence Intervals for Regression Coefficients](/posts/regression-07-confidence-intervals)
8. **Statistical Testing in Regression** (You are here)
9. [ANOVA in Regression: SST, SSR, SSE and the F-Test](/posts/regression-09-anova)
{% end %}

In the [previous post](/posts/regression-07-confidence-intervals), we constructed confidence intervals for regression coefficients. Confidence intervals and hypothesis tests are two sides of the same coin. In this post, we formalize the hypothesis testing framework for regression coefficients.

## Hypothesis Testing for Individual Coefficients

The most common test in regression asks whether a particular predictor has a significant linear effect on the response. For coefficient $\beta_j$, the hypotheses are:

$$H_0: \beta_j = 0 \quad \text{(the predictor has no effect)},$$
$$H_1: \beta_j \neq 0 \quad \text{(the predictor has an effect)}.$$

This is a two-sided test. One-sided alternatives ($H_1: \beta_j > 0$ or $H_1: \beta_j < 0$) are also possible when the direction of the effect is of interest.

## The t-Test Statistic

Under $H_0: \beta_j = 0$, the test statistic is:

$$t = \frac{\hat{\beta}_j - 0}{SE(\hat{\beta}_j)} = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}.$$

Under the null hypothesis and the normality assumption, this statistic follows a t-distribution:

$$t \sim t_{n-p},$$

where $n - p$ is the residual degrees of freedom.

### For Simple Linear Regression

Testing $H_0: \beta_1 = 0$ (the slope is zero):

$$t = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)} = \frac{\hat{\beta}_1}{\sqrt{MSE/S_{xx}}} = \frac{S_{xy}/S_{xx}}{\sqrt{MSE/S_{xx}}} = \frac{S_{xy}}{\sqrt{MSE \cdot S_{xx}}}.$$

This statistic follows $t_{n-2}$ under $H_0$.

Testing $H_0: \beta_0 = 0$ (the intercept is zero):

$$t = \frac{\hat{\beta}_0}{SE(\hat{\beta}_0)} = \frac{\hat{\beta}_0}{\sqrt{MSE(1/n + \bar{x}^2/S_{xx})}}.$$

### For Multiple Regression

Testing $H_0: \beta_i = 0$ for any coefficient $\beta_i$:

$$t = \frac{\hat{\beta}_i}{SE(\hat{\beta}_i)} = \frac{\hat{\beta}_i}{\sqrt{MSE \cdot C_{ii}}},$$

where $C_{ii}$ is the appropriate diagonal element of $(\mathbf{X}^T\mathbf{X})^{-1}$.

## Decision Rule

For a significance level $\alpha$ (commonly $\alpha = 0.05$):

**Reject $H_0$** if $|t| > t_{\alpha/2, n-p}$.

**Fail to reject $H_0$** if $|t| \leq t_{\alpha/2, n-p}$.

Rejecting $H_0$ means we have sufficient evidence that $\beta_j \neq 0$, suggesting that the predictor $x_j$ has a statistically significant effect on $y$.

## P-Values

The p-value provides a continuous measure of the evidence against $H_0$. For a two-sided test:

$$p\text{-value} = 2 \cdot P(T > |t_{\text{obs}}|),$$

where $T \sim t_{n-p}$ and $t_{\text{obs}}$ is the observed test statistic.

Interpretation:

- The p-value is the probability of observing a test statistic at least as extreme as the one computed, assuming $H_0$ is true.
- A small p-value (typically $< 0.05$) provides evidence against $H_0$.
- A large p-value does not prove $H_0$ is true; it simply means the data do not provide strong evidence against it.

The decision rule using p-values is equivalent to using critical values: reject $H_0$ if $p\text{-value} < \alpha$.

## Testing Against a Non-Zero Value

More generally, we can test $H_0: \beta_j = \beta_{j,0}$ for any hypothesized value $\beta_{j,0}$:

$$t = \frac{\hat{\beta}_j - \beta_{j,0}}{SE(\hat{\beta}_j)}.$$

The test for $\beta_j = 0$ is simply the special case where $\beta_{j,0} = 0$.

## Connection to Confidence Intervals

There is a direct equivalence between hypothesis tests and confidence intervals:

- **Reject** $H_0: \beta_j = \beta_{j,0}$ at level $\alpha$ if and only if $\beta_{j,0}$ falls outside the $(1 - \alpha) \times 100\%$ confidence interval for $\beta_j$.
- **Fail to reject** $H_0$ if and only if $\beta_{j,0}$ falls inside the confidence interval.

This means that when we check whether a 95% confidence interval for $\beta_1$ contains zero, we are implicitly performing a t-test at the $\alpha = 0.05$ level.

## Testing the Correlation

For simple linear regression, testing $H_0: \beta_1 = 0$ is equivalent to testing $H_0: \rho = 0$ (the population correlation is zero). This is because $\hat{\beta}_1 = r \cdot S_y/S_x$, and $\hat{\beta}_1 = 0$ if and only if $r = 0$.

The test statistic can also be written in terms of $r$:

$$t = r\sqrt{\frac{n - 2}{1 - r^2}},$$

which follows $t_{n-2}$ under $H_0: \rho = 0$.

## Practical vs. Statistical Significance

A statistically significant result (small p-value) does not necessarily mean the result is practically important. With a large sample size, even a tiny effect can be statistically significant because the standard error shrinks with $n$.

Conversely, a non-significant result does not mean the effect is zero; it may reflect insufficient sample size (low statistical power).

When interpreting regression results, consider both:

1. **Statistical significance**: Is the p-value small enough to reject $H_0$?
2. **Practical significance**: Is the estimated effect $\hat{\beta}_j$ large enough to matter in the context of the problem?

The confidence interval is particularly helpful here because it shows both the direction and the plausible range of the effect size.

## Multiple Testing Considerations

When testing multiple coefficients in a regression model, each at level $\alpha$, the probability of at least one false rejection increases. If you test $k$ independent hypotheses at $\alpha = 0.05$, the family-wise error rate is approximately $1 - (1 - \alpha)^k$.

Common corrections include:

- **Bonferroni correction**: Test each hypothesis at $\alpha/k$.
- **Holm-Bonferroni method**: A sequential version that is less conservative.
- **False Discovery Rate (FDR) control**: Controls the expected proportion of false rejections.

In regression, the overall model significance is typically assessed using the F-test (covered in the next post), which tests all predictors simultaneously.

## Summary

In this post, we covered hypothesis testing for regression coefficients:

- The t-statistic $t = \hat{\beta}_j / SE(\hat{\beta}_j)$ follows $t_{n-p}$ under $H_0: \beta_j = 0$.
- Reject $H_0$ when $|t| > t_{\alpha/2, n-p}$ or equivalently when $p\text{-value} < \alpha$.
- For $\beta_1$ in SLR: $t = S_{xy}/\sqrt{MSE \cdot S_{xx}}$ with $n - 2$ degrees of freedom.
- Testing $\beta_1 = 0$ is equivalent to testing $\rho = 0$.
- Confidence intervals and hypothesis tests provide equivalent information.
- Always consider practical significance alongside statistical significance.

In the next post, we will examine the ANOVA framework, which tests the overall significance of the regression model using the F-test.
