+++
title = "Why Can't Time Flow Backwards? Entropy, Yu Deng, and What the Mathematics Actually Proves"
description = "A first-principles look at why reversible particle collisions can produce an irreversible Boltzmann equation, how entropy enters mathematically, and what Yu Deng's Fields Medal work with Zaher Hani and Xiao Ma actually proved."
date = 2026-08-02
updated = 2026-08-02
draft = false
aliases = ["/posts/entropy-time-arrow-yu-deng/"]

[taxonomies]
categories = ["2026"]
tags = ["math", "entropy", "arrow of time", "boltzmann equation", "statistical mechanics", "partial differential equations"]

[extra]
topic = "Mathematical Physics"
lang = "en"
toc = true
comment = true
copy = true
outdate_alert = false
outdate_alert_days = 120
math = true
mermaid = false
featured = false
reaction = true
+++

Most explanations of entropy start from the ending. They tell us that disorder increases, broken eggs do not rebuild themselves, and time only moves forward. That sounds intuitive, but it hides the mathematical problem.

The microscopic laws do not seem to know which direction is forward.

Imagine a box of hard spheres moving and colliding elastically. If I record every position and velocity, stop the recording, reverse every velocity, and run the same laws again, the particles retrace their paths. Newton's equations allow the movie to run in either direction. Yet a gas placed in one corner spreads through the box and does not spontaneously gather itself back into that corner.

So where did the direction come from?

I came back to this question after seeing a recent explanation of entropy and then reading the work recognised in [Yu Deng's 2026 Fields Medal citation](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026). The citation includes his work with Zaher Hani and Xiao Ma on deriving the Boltzmann equation from hard-sphere dynamics. What caught me was not simply that they proved entropy increases. Boltzmann had already built that idea into kinetic theory in the nineteenth century. The deeper achievement was showing, over the relevant lifespan of the solution, how an irreversible statistical equation can genuinely emerge from reversible particle mechanics.

That is a more precise and more interesting statement than saying, “time cannot go backwards.”

## Start with the Reversible Movie

Suppose the complete microscopic state of $N$ hard spheres is

$$
Z_N(t) = \big(x_1(t),v_1(t),\ldots,x_N(t),v_N(t)\big).
$$

Between collisions, each sphere moves in a straight line. At a collision, the velocities change while momentum and kinetic energy are conserved. If $Z_N(t)$ is a valid trajectory, reversing all velocities produces another valid trajectory:

$$
\mathcal{R}Z_N(t)
= \big(x_1(t),-v_1(t),\ldots,x_N(t),-v_N(t)\big).
$$

There is no microscopic instruction saying that one direction is the future. In principle, the exact state carries enough information to reverse the movie.

But this state is far too detailed for the questions we normally ask about a gas. We do not track $6N$ coordinates. We ask for a distribution $f(t,x,v)$, where $f$ describes how likely we are to find a particle near position $x$ with velocity $v$ at time $t$.

The first change is the move from one exact many-particle trajectory to a one-particle statistical description:

$$
Z_N(t) \quad\longrightarrow\quad f(t,x,v).
$$

The Boltzmann equation evolves that density:

$$
\frac{\partial f}{\partial t} + v\cdot\nabla_x f = Q(f,f).
$$

The left side transports particles through space. The collision operator $Q(f,f)$ accounts for how pairs of velocities are redistributed by collisions. The equation is not trying to remember every particle. It keeps the level of information needed to describe the gas statistically.

This is also where the arrow of time becomes visible.

## What Entropy Increase Means Mathematically

Boltzmann introduced the functional

$$
H[f] = \int f\log f \mathrm{d}x \mathrm{d}v.
$$

For sufficiently regular solutions of the Boltzmann equation,

$$
\frac{dH}{dt} \leq 0.
$$

Physical entropy uses the opposite sign:

$$
S[f] = -k_B H[f],
$$

so

$$
\boxed{\frac{dS}{dt} \geq 0.}
$$

This is the H-theorem. The inequality is not added as a separate law. It follows from the collision structure inside the Boltzmann equation.

The proof uses the elementary inequality:

$$
(a-b)\log\left(\frac{a}{b}\right) \geq 0
\qquad \text{for } a,b>0.
$$

After pairing every collision with its reverse and symmetrising the collision integral, the change in $H$ can be written schematically as

$$
\frac{dH}{dt}
= -\frac14\int B
\big(f'f_{\ast}'-ff_{\ast}\big)
\log\left(\frac{f'f_{\ast}'}{ff_{\ast}}\right)
\mathrm{d}\Gamma
\leq 0.
$$

Here $f$ and $f_{\ast}$ describe two particles before a collision, $f'$ and $f_{\ast}'$ describe them after it, $B$ is the collision rate, and $\mathrm{d}\Gamma$ collects the position, velocity, and collision-direction variables. Since the integrand multiplying the minus sign is nonnegative, $H$ cannot increase. Equality is reached at the Maxwellian equilibrium distribution.

That is the clean mathematical proof of entropy increase inside Boltzmann's theory.

But there is a catch.

The H-theorem belongs to the Boltzmann equation. It does not directly say that the full $N$-particle Newtonian state has forgotten how to reverse. The exact state still follows reversible mechanics. The real problem is therefore to justify why the one-particle density should obey Boltzmann's irreversible equation in the first place.

## The Missing Bridge

This gap is sometimes hidden behind the phrase *molecular chaos*. Before a collision, the velocities of two incoming particles are treated as approximately independent, so a two-particle density behaves like a product:

$$
f_{2}(t,x,v,x,v_{\ast}) \approx f(t,x,v)f(t,x,v_{\ast}).
$$

That approximation closes the equation. Without it, the evolution of one-particle statistics depends on two-particle correlations, which depend on three-particle correlations, and so on. We end up with an entire hierarchy rather than one usable kinetic equation.

The objection is obvious. Collisions create correlations. Why are we allowed to neglect them later, especially over long times?

This is where the mathematics becomes difficult. A particle can collide, separate, and then become indirectly connected to an earlier particle through a long chain of later collisions. The number of possible histories grows quickly. A short-time approximation may work before these histories become too complicated, but extending it is not a small technical improvement. It means controlling the accumulated memory of the system.

In 1975, Oscar Lanford rigorously derived the Boltzmann equation from hard-sphere mechanics, but only for a sufficiently short time. That was a landmark result and also the barrier that remained for roughly fifty years.

## What Deng, Hani, and Ma Proved

Yu Deng, Zaher Hani, and Xiao Ma broke that long-time barrier in [*Long time derivation of the Boltzmann equation from hard sphere dynamics*](https://doi.org/10.48550/arXiv.2408.07818).

Their setting is precise. The particles are hard spheres in a rarefied gas. The number of particles $N$ tends to infinity while their diameter $\varepsilon$ tends to zero under the Boltzmann-Grad scaling. Roughly, the gas becomes made of more and more, smaller and smaller particles while the collision rate remains meaningful.

Within this regime, they derive the Boltzmann equation for arbitrarily long finite times, as long as the corresponding strong solution to the Boltzmann equation exists. If that solution is global, their derivation covers every fixed finite time and even times that grow slowly in the limit.

The phrase “as long as the solution exists” matters. This is not a theorem for every material, every density, or every imaginable initial state. It is a rigorous bridge for a specific model and scaling regime. Still, it goes far beyond the previous short-time result.

The proof has an idea I find quite visual. Instead of pretending that collision histories disappear, the authors keep track of them through cumulants. They encode the relevant histories as diagrams they call **molecules**. An atom in one of these mathematical molecules represents a collision, and the bonds record how particle histories connect.

The difficulty is then converted into a combinatorial and analytic question: which complicated collision diagrams contribute a meaningful amount, and which become negligible as $\varepsilon\to0$?

Their cutting algorithm breaks a large molecule into elementary pieces that can be estimated. In simple language, they do not assume away every correlation. They organise the correlations, follow their history across time layers, and prove that the troublesome accumulated pieces remain small enough for the Boltzmann description to survive.

A companion paper, [*Hilbert's sixth problem: derivation of fluid equations via Boltzmann's kinetic theory*](https://doi.org/10.48550/arXiv.2503.01800), extends the argument to a periodic setting in dimensions two and three and connects the kinetic limit to fluid equations. The route is

$$
\text{Newtonian hard spheres}
\longrightarrow
\text{Boltzmann equation}
\longrightarrow
\text{Euler and Navier-Stokes-Fourier equations}.
$$

This is the part of Hilbert's sixth problem concerned with deriving macroscopic fluid equations from microscopic mechanics through kinetic theory.

## So Why Can't Time Flow Backwards?

At the microscopic level, the equations still permit reversal. Nothing in the theorem deletes the reversed trajectory.

What changes is the description.

The full state $Z_N$ contains the exact correlations needed to reverse one special movie. The density $f$ does not label every particle or retain every collision detail. It describes what is typical for an ensemble of microscopic states compatible with the same macroscopic observation. In the dilute-gas limit studied by Deng, Hani, and Ma, that reduced description converges to the Boltzmann equation, whose H-theorem has a preferred direction.

My way of understanding it is this: irreversibility is not a new microscopic force. It appears when a lower-dimensional statistical description becomes accurate enough to stand on its own.

To make the gas return to one corner, we would need an extraordinarily special arrangement of positions and velocities, including fine correlations that the one-particle density does not record. Reversing every velocity in the exact microscopic state creates such an arrangement. Choosing a typical state with the same visible density does not.

So entropy increase is not saying that the reverse movie is logically forbidden. It says that the forward Boltzmann evolution is the effective law for the statistical states covered by the derivation, while the reversed movie depends on microscopic coordination that is invisible at that level.

This also explains why I would not summarise the result as “mathematics proves time cannot go backwards.” The theorem proves something sharper:

> A time-irreversible kinetic equation can emerge rigorously from a time-reversible particle system, over long times and under a defined dilute-gas limit.

That distinction is not a weakness. It is the whole point.

## References

1. Ludwig Boltzmann, [“Weitere Studien über das Wärmegleichgewicht unter Gas-molekülen”](https://doi.org/10.1017/CBO9781139381420.023), 1872.
2. Yu Deng, Zaher Hani, and Xiao Ma, [“Long time derivation of the Boltzmann equation from hard sphere dynamics”](https://doi.org/10.48550/arXiv.2408.07818), arXiv:2408.07818.
3. Yu Deng, Zaher Hani, and Xiao Ma, [“Hilbert's sixth problem: derivation of fluid equations via Boltzmann's kinetic theory”](https://doi.org/10.48550/arXiv.2503.01800), arXiv:2503.01800.
4. International Mathematical Union, [“Fields Medals 2026”](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026).
