+++
title = "Statistical Testing in Regression"
description = "Performing hypothesis tests on regression coefficients using t-tests, p-values, and the connection to confidence intervals."
date = 2026-02-20
updated = 2026-02-20
draft = false
aliases = ["/posts/regression-08-statistical-testing/"]

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

Hypothesis tests ask whether the data provide enough evidence against a specified regression claim. This note covers test setup, assumptions, p-values, and the boundary between evidence and overclaiming.


The [previous note](/posts/regression-07-confidence-intervals) constructed confidence intervals for regression coefficients. Confidence intervals and hypothesis tests answer related questions. Here, we formalize the hypothesis-testing framework for regression coefficients.

## Hypothesis Testing for Individual Coefficients

The most common test in regression asks whether a particular predictor has a significant linear effect on the response. For coefficient $\beta\_j$, the hypotheses are:

$$H\_0: \beta\_j = 0 \quad \text{(the predictor has no effect)},$$
$$H\_1: \beta\_j \neq 0 \quad \text{(the predictor has an effect)}.$$

This is a two-sided test. One-sided alternatives ($H\_1: \beta\_j > 0$ or $H\_1: \beta\_j < 0$) are also possible when the direction of the effect is of interest.

## The t-Test Statistic

Under $H\_0: \beta\_j = 0$, the test statistic is:

$$t = \frac{\hat{\beta}\_j - 0}{SE(\hat{\beta}\_j)} = \frac{\hat{\beta}\_j}{SE(\hat{\beta}\_j)}.$$

Under the null hypothesis and the normality assumption, this statistic follows a t-distribution:

$$t \sim t\_{n-p},$$

where $n - p$ is the residual degrees of freedom.

### For Simple Linear Regression

Testing $H\_0: \beta\_1 = 0$ (the slope is zero):

$$t = \frac{\hat{\beta}\_1}{SE(\hat{\beta}\_1)} = \frac{\hat{\beta}\_1}{\sqrt{MSE/S\_{xx}}} = \frac{S\_{xy}/S\_{xx}}{\sqrt{MSE/S\_{xx}}} = \frac{S\_{xy}}{\sqrt{MSE \cdot S\_{xx}}}.$$

This statistic follows $t\_{n-2}$ under $H\_0$.

Testing $H\_0: \beta\_0 = 0$ (the intercept is zero):

$$t = \frac{\hat{\beta}\_0}{SE(\hat{\beta}\_0)} = \frac{\hat{\beta}\_0}{\sqrt{MSE(1/n + \bar{x}^2/S\_{xx})}}.$$

### For Multiple Regression

Testing $H\_0: \beta\_i = 0$ for any coefficient $\beta\_i$:

$$t = \frac{\hat{\beta}\_i}{SE(\hat{\beta}\_i)} = \frac{\hat{\beta}\_i}{\sqrt{MSE \cdot C\_{ii}}},$$

where $C\_{ii}$ is the appropriate diagonal element of $(\mathbf{X}^T\mathbf{X})^{-1}$.

## Decision Rule

For a significance level $\alpha$ (commonly $\alpha = 0.05$):

**Reject $H\_0$** if $|t| > t\_{\alpha/2, n-p}$.

**Fail to reject $H\_0$** if $|t| \leq t\_{\alpha/2, n-p}$.

Rejecting $H\_0$ means we have sufficient evidence that $\beta\_j \neq 0$, suggesting that the predictor $x\_j$ has a statistically significant effect on $y$.

## P-Values

The p-value provides a continuous measure of the evidence against $H\_0$. For a two-sided test:

$$p\text{-value} = 2 \cdot P(T > |t\_{\text{obs}}|),$$

where $T \sim t\_{n-p}$ and $t\_{\text{obs}}$ is the observed test statistic.

Interpretation:

- The p-value is the probability of observing a test statistic at least as extreme as the one computed, assuming $H\_0$ is true.
- A small p-value (typically $< 0.05$) provides evidence against $H\_0$.
- A large p-value does not prove $H\_0$ is true; it simply means the data do not provide strong evidence against it.

The decision rule using p-values is equivalent to using critical values: reject $H\_0$ if $p\text{-value} < \alpha$.

## Testing Against a Non-Zero Value

More generally, we can test $H\_0: \beta\_j = \beta\_{j,0}$ for any hypothesized value $\beta\_{j,0}$:

$$t = \frac{\hat{\beta}\_j - \beta\_{j,0}}{SE(\hat{\beta}\_j)}.$$

The test for $\beta\_j = 0$ is simply the special case where $\beta\_{j,0} = 0$.

## Connection to Confidence Intervals

There is a direct equivalence between hypothesis tests and confidence intervals:

- **Reject** $H\_0: \beta\_j = \beta\_{j,0}$ at level $\alpha$ if and only if $\beta\_{j,0}$ falls outside the confidence interval with confidence level $1 - \alpha$ for $\beta\_j$.
- **Fail to reject** $H\_0$ if and only if $\beta\_{j,0}$ falls inside the confidence interval.

This means that when we check whether a 95% confidence interval for $\beta\_1$ contains zero, we are implicitly performing a t-test at the $\alpha = 0.05$ level.

## Testing the Correlation

For simple linear regression, testing $H\_0: \beta\_1 = 0$ is equivalent to testing $H\_0: \rho = 0$ (the population correlation is zero). This is because $\hat{\beta}\_1 = r \cdot S\_y/S\_x$, and $\hat{\beta}\_1 = 0$ if and only if $r = 0$.

The test statistic can also be written in terms of $r$:

$$t = r\sqrt{\frac{n - 2}{1 - r^2}},$$

which follows $t\_{n-2}$ under $H\_0: \rho = 0$.

## Practical vs. Statistical Significance

A statistically significant result (small p-value) does not necessarily mean the result is practically important. With a large sample size, even a tiny effect can be statistically significant because the standard error shrinks with $n$.

Conversely, a non-significant result does not mean the effect is zero; it may reflect insufficient sample size (low statistical power).

When interpreting regression results, consider both:

1. **Statistical significance**: Is the p-value small enough to reject $H\_0$?
2. **Practical significance**: Is the estimated effect $\hat{\beta}\_j$ large enough to matter in the context of the problem?

The confidence interval is particularly helpful here because it shows both the direction and the plausible range of the effect size.

## Multiple Testing Considerations

When testing multiple coefficients in a regression model, each at level $\alpha$, the probability of at least one false rejection increases. If you test $k$ independent hypotheses at $\alpha = 0.05$, the family-wise error rate is approximately $1 - (1 - \alpha)^k$.

Common corrections include:

- **Bonferroni correction**: Test each hypothesis at $\alpha/k$.
- **Holm-Bonferroni method**: A sequential version that is less conservative.
- **False Discovery Rate (FDR) control**: Controls the expected proportion of false rejections.

In regression, the overall model significance is typically assessed using the F-test, which tests all predictors simultaneously. The next note develops that test through ANOVA.

## Summary

Hypothesis testing for regression coefficients rests on six points:

- The t-statistic $t = \hat{\beta}\_j / SE(\hat{\beta}\_j)$ follows $t\_{n-p}$ under $H\_0: \beta\_j = 0$.
- Reject $H\_0$ when $|t| > t\_{\alpha/2, n-p}$ or equivalently when $p\text{-value} < \alpha$.
- For $\beta\_1$ in SLR: $t = S\_{xy}/\sqrt{MSE \cdot S\_{xx}}$ with $n - 2$ degrees of freedom.
- Testing $\beta\_1 = 0$ is equivalent to testing $\rho = 0$.
- Confidence intervals and hypothesis tests provide equivalent information.
- Always consider practical significance alongside statistical significance.

The next note examines the ANOVA framework and its F-test for overall model significance.
