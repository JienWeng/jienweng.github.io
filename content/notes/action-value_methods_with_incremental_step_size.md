+++
title = "Action-value methods with incremental step size in reinforcement learning"
description = "How much we see on Internet is real?"
date = 2025-10-17
updated = 2025-10-17
draft = false
aliases = ["/posts/action-value-methods-with-incremental-step-size/"]

[taxonomies]
categories = ["2025"]
tags = ["math", "reinforcement learning", "ai"]

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

This note derives the incremental update rule for action-value estimation in k-armed bandits and explains why it is preferable to recomputing full averages. The problem is memory and compute cost when rewards accumulate over time. By the end, you get a practical update equation you can implement directly in RL experiments.

Consider any [k-armed bandit problem](https://en.wikipedia.org/wiki/Multi-armed_bandit), we consider each actions taken as pulling an arm of a slot machine, and the machine gives us a reward based on the action taken. We denote the action selected at time step $t$ as $A_t$, and the correspondiong reward received as $R_t$. Among the $k$ actions, the expected value of each action $a$ is denoted as $q_\*(a)=\mathbb{E}[R_t|A_t=a]$, which is also known as the *value* of that action $a$. It is rationale to choose the action with the highest value, however in the practical applications, the value of each action is unknown. Therefore, we need to estimate the value of each action, denoted as $Q_t(a)$, read as the estimated value of action $a$ at time step $t$. The fundamental goal is to find such $Q_t(a)$ that is as close as possible to the $q_\*(a)$. It is commonly known as the *true value* by community.

To estimate the values of each action, which we collectively call as the *action-value methods*, we can use the sample-average method to update the estimated value of action $a$ at time step $t$ as follows:

$$Q_{t}(a)={{\text{sum of rewards when $a$ taken prior to $t$}} \over {\text{number of times $a$ taken prior to $t$}}}.$$

This method simply takes the average of all the rewards received when action $a$ is taken prior to time step $t$. To simplify the notation, we focus on a single action. We denoted $R_i$ as the reward received the $i$-th time of this action is taken, and $n$ as the number of times action $a$ is taken prior to time step $t$. Logically, we can let $Q_n$ denote the estimate of its action value after it has been taken $n-1$ times. Therefore, we can rewrite the update rule as follows:

$$Q_n = \frac{\sum_{i=1}^{n-1}R_i}{n-1} = \frac{R_1+R_2+\ldots+R_{n-1}}{n-1}.$$

As the number of times of the action, $n$ increases, the obvious wat to update the estimate is to recalculate the average by summing up all the previous rewards and dividing it by $n-1$. However, as the number of times of the action increases to a large number, this method becomes progressively more expensive as we need to store all the previos rewards and recalculate the sum every time we need to update the estimate. 

But is there a better way to update the estimate without storing all the previous rewards? The answer is yes. We devise the incremental formulas for updating the estimate by

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

This incremental formula allows us to update the estimate $Q_n$ to $Q_{n+1}$ by only using the most recent reward $R_n$ and the previous estimate $Q_n$, without the need to store all the previous rewards. The term $\frac{1}{n}$ serves as the step size, which decreases as $n$ increases, ensuring that the estimate converges to the true value over time.

Even in $n=1$, we can still obtain $Q_2 = R_1$ for arbitrary initial estimate $Q_1$. In this case, the initial estimate $Q_1$ is completely ignored after the first update, as it should be. In processing the $n$th reward, the estimate is adjusted by a fraction of the error term $[R_n - Q_n]$, which is the difference between the received reward and the current estimate. This adjustment is scaled by the step size $\frac{1}{n}$, which ensures that as more data is collected, the updates become smaller, allowing the estimate to stabilize around the true value. Note that the step size here is not constant, it decreases as the number of times of the action increases.

Back to the bandit problem, the proposed simulation in for pseudo-code is as follows:

{% detail(title="Bandit Problem with Incremental Step Size", default_open=false) %}
```python
Initialize Q(a) arbitrarily for all actions a
For each time step t = 1, 2, ...
    Select action A_t using a policy derived from Q (e.g., ε-greedy)
    Take action A_t and observe reward R_t
    Update the estimate Q(A_t) using:
        n = number of times action A_t has been taken prior to time t
        Q(A_t) = Q(A_t) + (1/n) * [R_t - Q(A_t)]
End For
```
{% end %}



In the end of this post, we derived the incremental step size method for updating the aciton-value estimates which extensively applied in reinforcement learning. This method is computationally efficient as it does not require storing all previous rewards, and it ensures convergence to the true action values over time. 

{{ figure(src="https://m.media-amazon.com/images/I/81EBg4xmLgL._UF1000,1000_QL80_.jpg", alt="Reinforcement Learning: An Introduction", caption="Reinforcement Learning: An Introduction") }}

I want to express my gratitude to Sutton and Barto for their excellent book [Reinforcement Learning: An Introduction](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf) that provides a comprehensive introduction to the concepts and algorithms of reinforcement learning.

References:
- Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd ed.). MIT Press. [https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)