+++
title = "Why Agents With Less Information Cooperate More"
description = "The intuition behind a paper under review: in the Public Goods Game, what agents can observe matters far more for cooperation than which RL algorithm trains them."
date = 2026-07-03
draft = true

[taxonomies]
categories = ["2026"]
tags = ["reinforcement learning", "multi-agent", "cooperation", "information design", "public goods game"]

[extra]
topic = "Reinforcement Learning"
lang = "en"
toc = false
comment = true
math = true
+++

The Public Goods Game is the cleanest version of a familiar problem. Everyone is better off if everyone contributes to a shared pot, but each individual is better off free-riding on the others. Train reinforcement learning agents to play it and you get a laboratory for a question I care about: what actually makes cooperation emerge?

The instinct, mine included at the start, is that the algorithm matters. Better credit assignment, better cooperation. So with my coauthors I ran a full-factorial experiment: vary the information regime (what each agent can observe), the incentive strength, and the learning algorithm, all crossed with each other, and measure cooperation rates.

The algorithm barely matters. Information regime and incentive strength together explain 85.8% of the variance in cooperation rates. Algorithm choice explains 3.8%.

The stranger result is the direction. The agents with the *least* information cooperated the most: 83% cooperation under the most restricted regime, against 42% under full observation.

<!-- TODO(Jien): sanity-check the framing of this paragraph against the paper's own explanation before publishing. -->

The explanation we give is state-space compression. Free-riding, as a learned behaviour, is conditional: defect when you can get away with it, which means defect *based on what you see others doing*. That policy needs input features to condition on. Take the observations away and the policy space collapses toward unconditional strategies, and with meaningful incentives, unconditional contribution is the one that survives training. An agent that cannot watch others cannot learn to exploit them. Seeing more lets an agent learn to defect more precisely.

We attributed the variance with TreeSHAP and a Shapley-variance decomposition, and both point the same way: information structure, not algorithm selection, is the primary design lever for cooperation.

The design lesson is the part I keep coming back to, and it is the thread that runs through most of my work: decide what your agents can see before you argue about how they learn. In this game, the observation space was the mechanism. The algorithm was a detail.

The paper, with Wei Lun Tan, Ying Loong Lee, and Ming Fai Chow, is under review at IEEE Social Computation. This note is only the public intuition; I will link the full version once it is out.
