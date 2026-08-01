+++
title = "Misc"
description = "Readings, essays, and a few durable side interests."
template = "section.html"
+++

Things I keep coming back to that do not belong anywhere else on the site.

## Books

- *Deep Learning*, by Goodfellow, Bengio, and Courville
- *Reinforcement Learning: An Introduction*, by Sutton and Barto

## Essays

- [The Bitter Lesson](http://incompleteideas.net/IncIdeas/BitterLesson.html)
- [The Unreasonable Effectiveness of RNNs](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/)

## Talks and lectures

- [3Blue1Brown: Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)
- [Andrej Karpathy on YouTube](https://www.youtube.com/@AndrejKarpathy)

## Questions I keep coming back to

- What information does an agent actually need to coordinate well?
- Should we try to mimic a human way of thinking, or let a system learn by exploration without building that structure in first?

## Two viewpoints

Richard Sutton's argument in [The Bitter Lesson](http://incompleteideas.net/IncIdeas/BitterLesson.html) is still one of the clearest warnings against overvaluing hand-designed structure. Compute and search scale; most of our clever constructions do not survive contact with systems that keep learning from more experience. I come back to it because it cuts against a common instinct. When a system feels more interpretable or more human-designed, we tend to assume it is more principled. Sutton says this can be exactly backwards.

Andrej Karpathy's [Animals vs Ghosts](https://karpathy.bearblog.dev/animals-vs-ghosts/) pushes back from another side. His framing is that current frontier systems may not be "animals" in Sutton's sense at all but "ghosts": saturated with human text, human priors, and human engineering, and still able to do real work in the world. Which leaves an honest open question. Do we imitate a human way of thinking, or let a system earn its competence through exploration, even if the internal route looks nothing like us?

I do not think the two cancel out. Sutton warns against trusting handcrafted stories too much. Karpathy warns against pretending today's engineered systems are already the bitter lesson carried to its limit. I find the tension useful, for reinforcement learning and for modelling generally. Often the real question is not what the most human-looking way to do something is, but what structure is actually necessary and what can be left to learning.
