+++
title = "Why I’m Still Learning Maths"
description = "OpenAI’s Navier–Stokes and ETH announcements, the unexpected uses of pure maths, and why I think this is a good time to start learning."
date = 2026-11-16
updated = 2026-11-16
draft = false

[taxonomies]
categories = ["2026"]
tags = ["mathematics", "AI", "reflections"]

[extra]
toc = false
topic = "Applied AI"
cover = "img/blog/maths-with-ai/video-thumbnail.jpg"
+++

I studied Applied Maths and Computing, so whether maths is still worth learning is a personal question for me.

OpenAI’s announcements about [Navier–Stokes](https://openai.com/index/navier-stokes-solution/) and the [Exponential Time Hypothesis](https://openai.com/index/building-scientific-understanding-with-academic-communities/) make it easy to wonder where humans fit. If you are about to spend years studying mathematics, what are you working towards when machines produce results like these?

The Navier–Stokes equations describe fluid motion. OpenAI claimed a proof that, under a smooth external force, initially smooth three-dimensional motion can develop a singularity in finite time. Researchers have since [questioned whether the Lean formalization matches the written proof](https://www.kcl.ac.uk/news/openais-navier-stokes-proof-called-into-question). That does not make the result false, but the computer-checked version cannot yet be treated as verification of the written argument.

The ETH announcement is a different kind of problem. The hypothesis says, roughly, that deciding whether a 3-SAT Boolean formula can be satisfied takes exponential time in the worst case. OpenAI’s [published notes](https://github.com/openai/math/blob/main/lean/docs/378.md) describe a subexponential algorithm. Its bound is still superpolynomial, so it does not settle P versus NP or give us a fast everyday tool.

I want to understand those details. Reading that a problem is solved tells me little about the assumptions, the method, or what someone could build from it. Even judging how much weight an announcement deserves takes some knowledge of the maths.

Grant Sanderson’s [video on AI and mathematics](https://www.youtube.com/watch?v=LKrwhjOI8Nc) compares practising maths to going to the gym. A machine can do the work faster, but doing it yourself still builds your own ability.

{{ youtube(id="LKrwhjOI8Nc", caption="3Blue1Brown · There’s never been a better time to go into math") }}

[Watch the full video on YouTube](https://www.youtube.com/watch?v=LKrwhjOI8Nc).

That matches how I build software with AI. I want to understand the assumptions behind an answer, follow the reasoning, and check whether it applies to my problem. An answer I cannot explain leaves me dependent on whoever, or whatever, produced it.

It is tempting to stop once the code runs. If an AI suggests an algorithm, I want to know why it works and which inputs might cause trouble. If it proposes a mathematical model, I want to know what it assumes about the thing it represents. A convincing explanation can still leave out a condition that matters.

That takes practice. Following a solution is easier than reconstructing it later. Working the problem myself shows me where I am confused: sometimes a definition I have used too loosely, sometimes algebra I followed without seeing why anyone chose that approach.

That is part of what makes maths useful beyond a particular course or theorem. It trains me to be precise about a question, keep track of assumptions, and find where an argument stops working. I want those habits when I use AI too.

I also like how maths finds uses far from the questions people started with. Elliptic curves appear in [Wiles’s proof of Fermat’s Last Theorem](https://abelprize.no/sites/default/files/2021-09/The%20Abel%20Prize%202013-2017_Full.pdf) and in cryptographic systems such as ECDSA. Elliptic-curve cryptography predates Wiles’s proof, so one did not come from the other. Both build on an older body of mathematics.

To follow the connection, I need to know what an elliptic curve is, how its points can be added, and how changing the number system changes the arithmetic. The picture below shows the real-number case. Cryptography takes that arithmetic into finite fields, where the points are discrete.

ECDSA uses elliptic-curve arithmetic to create and verify digital signatures. I could use a library without knowing any of that. Learning the maths lets me understand the design, read its assumptions, and ask better questions about it, even if I never prove a new theorem about elliptic curves.

{{ figure(src="img/blog/maths-with-ai/elliptic-curve-addition.svg", alt="Point addition on an elliptic curve: a line meets the curve, and reflection gives the sum.", caption="Point addition on a real elliptic curve.", credit="<a href='https://commons.wikimedia.org/wiki/File:EllipticCurveAddition.svg'>Googolplexian1221, Wikimedia Commons</a>, <a href='https://creativecommons.org/licenses/by-sa/4.0/'>CC BY-SA 4.0</a>") }}

Try the curve in [Desmos](https://www.desmos.com/calculator/t0neeko2lj), explore [finite-field arithmetic](https://ecdsa.com/tools/curve-playground), or read the [cryptography reference](https://www.rfc-editor.org/rfc/rfc6090.html).

Complex numbers have a similar story. They emerged through work on [algebraic equations](https://mathshistory.st-andrews.ac.uk/HistTopics/Quadratic_etc_equations/) and later became part of the language of [quantum mechanics](https://interactivetextbooks.tudelft.nl/introduction-to-quantum-mechanics/content/complexnumbers.html). Geometry beyond Euclid became part of how [general relativity describes gravity](https://www.einstein-online.info/en/GeomGravity/). The people working on the original questions could not have laid out those later uses.

So I am reluctant to judge maths only by its immediate applications. The methods developed along the way, or a link to another subject, may prove useful. When AI produces a new result, I want to understand what else we might do with the ideas behind it. Explaining those ideas, testing their limits, and finding where they apply could be years of worthwhile work.

I would not claim that asking questions or building theories will always be uniquely human, and Grant considers that too. His argument leaves room for much more capable machines while still valuing the experience of learning maths.

He also argues this is a good time to enter the field. The community knows it needs to change, so newcomers have a chance to influence how mathematics is explained and how contributions are recognised. I like that his answer has room for people who enjoy teaching, visualising, applying, or understanding mathematics, not only proving theorems.

I do not take that as a promise that a maths career will be easy or that academic life will survive unchanged. I can see a reason to learn without knowing what jobs or research will look like in ten years. I want to understand more of the systems I work with, and maths keeps giving me things to understand.

That makes this a good time to keep learning. I can ask AI about a step I do not follow, request a smaller example, or explore a connection. I can ask for the same idea algebraically and geometrically, then compare both with a textbook or another source.

I also need to leave myself enough work to learn from. A complete solution given too early makes it hard to tell whether I could have found the next step myself. I would rather try the problem, ask for a hint when I get stuck, and spend time with the part that confused me.

So: try a problem before reading the solution. Use AI when I get stuck. Then close the answer and see whether I can explain the reasoning without it.
