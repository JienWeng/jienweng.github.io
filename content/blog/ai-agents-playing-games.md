+++
title = "Watching AI Agents Work Together in Games"
description = "YC Labs’ Minecraft and Mindustry experiments reminded me of studying MARL: changing policies, shared rewards, and the difficulty of coordinating agents."
date = 2026-11-16
draft = false

[taxonomies]
categories = ["2026"]
tags = ["AI", "reinforcement learning"]

[extra]
toc = false
topic = "Applied AI"
+++

[YC Labs’ experiments with AI agents in games](https://labs.ycombinator.com/projects/games/index.html) reminded me of the multi-agent reinforcement learning (MARL) I used to study. I liked that I could follow what the agents did, mistakes included.

## Minecraft: a civilisation in three hours

<figure class="wide">
<iframe src="https://labs.ycombinator.com/replay/v1/viewer-v17.html?scene=vera-first-night-v8&amp;follow=Vera&amp;cut=1" title="Interactive 3D first-night Minecraft scene from YC Labs, following Vera" loading="lazy" allow="fullscreen" allowfullscreen style="display:block;width:100%;height:clamp(320px,55vw,520px);border:1px solid var(--rule)"></iframe>
<figcaption><span class="fig-caption">The first night, following Vera. Drag to rotate, scroll to zoom.</span><small class="fig-credit"><a href="https://labs.ycombinator.com/projects/games/index.html#opening-clip">YC Labs, original replay</a></small></figcaption>
</figure>

In one run, 50 agents had three hours to build a civilisation. They formed a hierarchy, rationed food, and sent about 5,900 messages. After a hard first night, they grew cautious and sheltered more. Their shared files held food queues and rules about who could take supplies.

One detail stayed with me: an agent picking up food did not mean the recipient had it. The agents had to check who had eaten before calling a delivery complete.

<figure class="wide">
<iframe src="https://labs.ycombinator.com/replay/v1/viewer-v17.html?scene=ines-v2&amp;cut=1" title="Interactive 3D Minecraft refuge scene from YC Labs, following Ines" loading="lazy" allow="fullscreen" allowfullscreen style="display:block;width:100%;height:clamp(320px,55vw,520px);border:1px solid var(--rule)"></iframe>
<figcaption><span class="fig-caption">The refuge scene at its first recorded moment.</span><small class="fig-credit"><a href="https://labs.ycombinator.com/projects/games/index.html#ines-replay">YC Labs, full replay with timeline and chat</a> · <a href="https://labs.ycombinator.com/replay/v1/viewer-v17.html?scene=ines-v2&amp;cut=1">fullscreen</a></small></figcaption>
</figure>

This is a software handoff problem. A message saying a task is done can drift from the actual state, and the next agent may act on the message without checking. When several agents rely on the same wrong report, a small error spreads.

## Competitive games: Bed Wars and Mindustry

YC also recorded competitive Minecraft games, such as Bed Wars.

<figure class="wide">
<iframe src="https://labs.ycombinator.com/replay/v1/bw-felix-pearl/viewer-v17.html" title="Interactive 3D Bed Wars scene from YC Labs, following Felix" loading="lazy" allow="fullscreen" allowfullscreen style="display:block;width:100%;height:clamp(320px,55vw,520px);border:1px solid var(--rule)"></iframe>
<figcaption><span class="fig-caption">Bed Wars, following Felix.</span><small class="fig-credit"><a href="https://labs.ycombinator.com/projects/games/index.html#bw-felix-pearl-figure">YC Labs, replay with timeline</a></small></figcaption>
</figure>

In Mindustry, teams competed. YC reported that the GPT agents split ownership into smaller pieces, while the Claude agents relied more on a leader. The GPT team won the seven-game series 6–1. That score describes this setup, not how the models compare on other tasks. See the [interactive Mindustry replay](https://replay.olamlabs.ai/?g=2&t=2850&seat=81&follow&play=1&speed=10).

The replays make the coordination easy to follow. A team must divide responsibilities, share resources, and react when a plan fails. Those choices shape what each agent can do, even with one shared objective.

## Why MARL felt harder

What made MARL hard for me was that an agent’s best action depends on what the others do, while they are also learning and changing.

Game theory describes incentives, strategies, and equilibria. MARL adds how agents learn to act from experience, often with incomplete information, so there is a learning process to account for as well as a solution. That was the part I found more involved. Game theory itself can be extremely difficult; I am comparing with fixed optimisation, not ranking the two subjects.

In simple optimisation, the objective and constraints are fixed and you search for a good solution. In a multi-agent setting, an action’s outcome depends on other agents’ actions, and in MARL those agents may adapt at the same time. A strategy that beat yesterday’s behaviour may fail against today’s.

An equilibrium describes a relationship between strategies. It does not explain how agents with limited observations and finite experience reach it; exploration, learning rules, and information all shape that path.

{{ figure(src="img/blog/agents-in-games/learning-process.png", width=1600, height=527, alt="A joint policy produces interaction histories in a game, which a learning algorithm uses to update that policy.", caption="The learning loop: policies generate experience that updates the policies.", credit="Albrecht, Christianos and Schäfer, <a href='https://github.com/marl-book/slides'>MARL book slides</a>, <a href='/img/blog/agents-in-games/MARL-SLIDES-LICENSE.txt'>MIT licence</a> (<a href='/img/blog/agents-in-games/learning-process.pdf'>PDF</a>)") }}

## Changing policies

One issue is non-stationarity. To one learner, the other learners are part of the environment. As their policies change, earlier experience loses value. Lowe and colleagues discuss this in [Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments](https://arxiv.org/abs/1706.02275).

The textbook example below (not YC data) shows two agents learning Rock–Paper–Scissors with WoLF-PHC, each adapting to the other.

{{ figure(src="img/blog/agents-in-games/changing-policies.png", width=1600, height=1531, alt="Blue and orange trajectories show two agents changing their Rock-Paper-Scissors action probabilities over learning, approaching starred policies.", caption="Two agents’ action probabilities shifting during Rock–Paper–Scissors learning.", credit="Albrecht, Christianos and Schäfer, <a href='https://github.com/marl-book/slides'>MARL book slides</a>, <a href='/img/blog/agents-in-games/MARL-SLIDES-LICENSE.txt'>MIT licence</a> (<a href='/img/blog/agents-in-games/changing-policies.pdf'>PDF</a>)") }}

## Credit and partial information

Then there is credit. A shared reward tells the team it succeeded, not which actions helped. A team can win because one agent acted well much earlier, another kept a supply chain going, or an opponent blundered; the final score does not separate these. This is the credit-assignment problem tackled by methods such as [counterfactual multi-agent policy gradients](https://ojs.aaai.org/index.php/AAAI/article/view/11794). Delayed rewards also force the algorithm to link outcomes to actions further back in time.

Partial observation adds more. An agent may see only locally and must act without knowing what teammates know, so two agents with aligned goals can decide differently. Messages help, but can be late, incomplete, or outdated. The free textbook [Multi-Agent Reinforcement Learning: Foundations and Modern Approaches](https://www.marl-book.com/) covers these questions alongside the game-theoretic foundations.

{{ figure(src="img/blog/agents-in-games/speaker-listener.png", width=1581, height=1600, alt="A speaker communicates a diamond target to a listener, which moves towards the matching landmark among several shapes.", caption="Speaker–listener task: one agent names the target, another acts on it.", credit="Albrecht, Christianos and Schäfer, <a href='https://github.com/marl-book/slides'>MARL book slides</a>, <a href='/img/blog/agents-in-games/MARL-SLIDES-LICENSE.txt'>MIT licence</a> (<a href='/img/blog/agents-in-games/speaker-listener.pdf'>PDF</a>)") }}

## Coordination without online learning

I see related coordination questions in YC’s experiments, but the runs are not evidence of online reinforcement learning. The report describes coding agents using tools, messages, scripts, and memory. Revising a plan or script mid-match does not update a model’s weights.

This matters when reading adaptation. A coding agent can read an error, change a script, and retry while the model stays fixed. In MARL training, the learner updates the policy itself from experience. Both change the next interaction, by different mechanisms.

The overlap is the coordination problem. Who has the information a decision needs? How does one agent’s action change another’s options? Does a local success help the team? These apply whether agents talk in natural language, use learned policies, or both.

Coordination also costs something. More agents mean more interactions and more demand on shared resources. A team may get more done, or spend its effort on conflicts and updates. Message volume alone cannot tell you which; compare the result with the resources used.

The [original report has replays, messages, and links to the code](https://labs.ycombinator.com/projects/games/index.html). The food-delivery records show a failed handoff up close; the Mindustry matches show coordination under competition. Together, they made MARL easier to picture than a win rate alone.

The diagrams are reproduced without redrawing from the authors’ [original lecture materials](https://github.com/marl-book/slides) for [Multi-Agent Reinforcement Learning: Foundations and Modern Approaches](https://www.marl-book.com/), with the [MIT licence and copyright notice](/img/blog/agents-in-games/MARL-SLIDES-LICENSE.txt).
