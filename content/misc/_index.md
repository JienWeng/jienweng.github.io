+++
title = "Misc"
description = "Readings, essays, and a few durable side interests."
template = "section.html"
+++

This page is for material that is useful to return to but does not belong in the formal research record.

# Reading Notes and Papers Worth Re-reading

- *Deep Learning* — Goodfellow, Bengio, Courville
- *Reinforcement Learning: An Introduction* — Sutton and Barto

## Essays Worth Returning To

- [The Bitter Lesson](http://incompleteideas.net/IncIdeas/BitterLesson.html)
- [The Unreasonable Effectiveness of RNNs](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/)

## Talks and Lectures Worth Watching

- [3Blue1Brown: Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)
- [Andrej Karpathy on YouTube](https://www.youtube.com/@AndrejKarpathy)

## Questions I Keep Returning To

- What information does an agent actually need to coordinate well?
- When does prediction improve control, and when does it only decorate the model?
- Which parts of finance are genuinely sequential decision problems?
- When do simpler systems outperform richer ones because the regime is specified correctly?
- Should we try to mimic a human way of thinking, or should we let a system learn by exploration without building that structure in first?

## Viewpoints Worth Keeping Around

Richard Sutton's argument in [The Bitter Lesson](http://incompleteideas.net/IncIdeas/BitterLesson.html) is still one of the clearest warnings against overvaluing hand-designed structure. The broad point is not only that compute and search scale well, but that many of our favorite clever constructions do not survive contact with systems that can keep learning, predicting, and improving from larger experience. I keep returning to that because it cuts against a common instinct: if a system feels more interpretable or more human-designed, we often assume it is more principled. Sutton's argument is that this can be exactly backwards.

Andrej Karpathy's [Animals vs Ghosts](https://karpathy.bearblog.dev/animals-vs-ghosts/) adds another distinction that is useful to keep around. His framing is that present-day frontier systems may not be "animals" in Sutton's sense at all. They may instead be "ghosts", systems saturated with human text, human priors, and human engineering, yet still capable of doing real work in the world. That matters because it raises a genuine question for AI research. Should we try to imitate a human-like way of thinking, or should we let a system acquire competence through exploration and interaction without insisting that the internal route look familiar to us?

I do not think these viewpoints cancel each other out. Sutton is a useful corrective against premature attachment to human-crafted structure. Karpathy is a useful corrective against pretending that current systems are already clean examples of the bitter lesson carried through to its limit. One viewpoint says not to trust handcrafted stories too much; the other says not to confuse today's engineered systems with the final form of learnable intelligence.

It's worth keeping the tension alive. It matters for reinforcement learning, for agent design, and even for mathematical modelling more generally. Sometimes the right question is not "what is the most human-looking way to do this?" but "what structure is actually necessary, and what should be left to learning?"
