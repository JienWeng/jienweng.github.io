+++
title = "Action-value methods with incremental step size in reinforcement learning"
description = "Deriving the incremental update rule for action-value estimation in k-armed bandits, and why constant step sizes suit nonstationary problems."
date = 2025-10-17
updated = 2025-10-17
draft = false
aliases = ["/posts/action-value-methods-with-incremental-step-size/"]

[taxonomies]
categories = ["2025"]
tags = ["math", "reinforcement learning", "ai"]

[extra]
topic = "Reinforcement Learning"
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

This note derives the incremental update rule for action-value estimation in k-armed bandits. The useful idea is simple: update an average using only the previous estimate and the newest reward, without storing the full reward history.

## The bandit setup

In a [k-armed bandit problem](https://en.wikipedia.org/wiki/Multi-armed_bandit), each action is like pulling one arm of a slot machine. At time step $t$, the agent selects action $A_t$ and receives reward $R_t$.

The expected reward of action $a$ is

$$q_*(a)=\mathbb{E}[R_t \mid A_t=a].$$

This is the action's true value. If we knew every $q_*(a)$, we could always choose the action with the highest value. In practice, those values are unknown, so the agent maintains an estimate $Q_t(a)$ and improves it as rewards arrive.

## From a sample average to an incremental update

The sample-average estimate for action $a$ is

$$Q_t(a)=\frac{\text{sum of rewards observed after taking $a$}}{\text{number of times $a$ has been taken}}.$$

Focus on one action. Let $R_i$ be the reward observed the $i$th time that action is selected, and let $Q_n$ be the estimate after the first $n-1$ rewards. Then

$$Q_n = \frac{1}{n-1}\sum_{i=1}^{n-1}R_i.$$

Recomputing this expression from the full history would require us to retain every reward. Instead, write the next estimate in terms of the current one:

$$ 
\begin{align*}
Q_{n+1} & = \frac{1}{n}\sum_{i=1}^{n}R_i \\\\
        & = \frac{1}{n}\left(R_n + \sum_{i=1}^{n-1}R_i\right) \\\\
        & = \frac{1}{n}\left(R_n + (n-1)\frac{1}{n-1}\sum_{i=1}^{n-1}R_i\right) \\\\
        & = \frac{1}{n}\left(R_n + (n-1)Q_n\right) \\\\
        & = \frac{1}{n}\left(R_n+nQ_n-Q_n \right) \\\\
        & = Q_n + \frac{1}{n}[R_n - Q_n].
\end{align*}
$$

The update has a useful form:

$$\text{new estimate}=\text{old estimate}+\text{step size}\times\text{prediction error}.$$

Here, $R_n-Q_n$ is the prediction error and $1/n$ is the step size. The first update gives $Q_2=R_1$ regardless of the initial $Q_1$. Later updates become smaller as the action is sampled more often.

For a stationary bandit, the sample average converges to the true action value under the usual law-of-large-numbers assumptions. In a nonstationary problem, however, the decreasing step size eventually makes the estimate slow to react. A constant step size $\alpha$, with $0<\alpha\leq1$, gives recent rewards more influence:

$$Q_{n+1}=Q_n+\alpha[R_n-Q_n].$$

## Pseudocode

{% detail(title="Bandit Problem with Incremental Step Size", default_open=false) %}
```python
Initialize Q(a) arbitrarily and N(a) = 0 for every action a
For each time step t = 1, 2, ...
    Select action A_t using a policy derived from Q (e.g., ε-greedy)
    Take action A_t and observe reward R_t
    N(A_t) = N(A_t) + 1
    Q(A_t) = Q(A_t) + (1 / N(A_t)) * [R_t - Q(A_t)]
End For
```
{% end %}
## Takeaway

The incremental rule reduces the memory cost from storing an entire reward history to storing one estimate and one counter per action. More importantly, it exposes a pattern that appears throughout reinforcement learning: update an estimate by moving it toward a new target in proportion to the current error.

## Reference

- Sutton, R. S., & Barto, A. G. (2018). *[Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html)* (2nd ed.). MIT Press.
