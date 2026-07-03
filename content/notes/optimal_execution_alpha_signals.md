+++
title = "Optimal Execution with Alpha Signals, Explained from Almgren-Chriss"
description = "The idea behind my SSRN paper: add a mean-reverting alpha signal to the optimal liquidation problem and a closed-form trading rule falls out of the HJB equation."
date = 2026-07-03
draft = true

[taxonomies]
categories = ["2026"]
tags = ["quantitative finance", "optimal execution", "stochastic control", "hjb"]

[extra]
topic = "Stochastic Modelling"
lang = "en"
toc = false
comment = true
math = true
+++

Suppose you have to sell a large position. Sell it fast and your own trading pushes the price down against you. Sell it slowly and the price has time to drift away before you are done. Almgren and Chriss (2001) made this tradeoff precise, and their framework is still what execution desks reason with.

Their model assumes the price is a martingale: no predictable drift, so the only enemies are impact and variance. The optimal schedule can then be computed once, in advance, and it is deterministic. But desks do have short-term predictors. The whole point of an alpha signal is that the price is locally *not* a martingale. My paper on SSRN asks what the optimal schedule looks like when you admit that.

The one ingredient added is a mean-reverting signal. Let $\alpha_t$ be the expected short-term drift, modelled as an Ornstein-Uhlenbeck process:

$$
d\alpha_t = -\kappa\, \alpha_t\, dt + \sigma_\alpha\, dW_t^{\alpha},
$$

and let the price drift with it, $dS_t = \alpha_t\, dt + \sigma\, dW_t$. The signal decays at rate $\kappa$: a fast-decaying signal is a rumour, a slow one is a view.

Because the signal is random, the schedule can no longer be precomputed. The problem becomes one of stochastic optimal control: the trading rate must react to the signal as it evolves. Writing down the value function and its Hamilton-Jacobi-Bellman equation, a quadratic ansatz goes through, and the optimal trading rate comes out in closed form, **affine in the two things you can observe**: your remaining inventory $q_t$ and the current signal $\alpha_t$,

$$
v_t^{*} = a(t)\, q_t + b(t)\, \alpha_t .
$$

<!-- TODO(Jien): if you want the coefficient ODEs for a(t), b(t) here, lift them from the paper. The note works without them. -->

The first term is the familiar liquidation clock: it plays the same role as the Almgren-Chriss trajectory and reduces to it when the signal is switched off. The second term tilts execution toward the signal, trading faster when the drift is against you and more patiently when it is with you. And because $\alpha$ mean-reverts, the tilt is weighted by how long the signal lives: as $\kappa$ grows, $b(t)$ shrinks, and a rumour barely moves the schedule.

I think the closed form is the real point. Desks are rightly suspicious of black-box execution. An affine rule is auditable, and it is additive: it sits on top of the schedule a desk already runs, rather than replacing it.

The full derivation, with the cost model and the verification argument, is in the paper: [Optimal Execution with Alpha Signals](https://doi.org/10.2139/ssrn.6323159) (SSRN, 2026).
