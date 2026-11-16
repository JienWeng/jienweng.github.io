+++
title = "Why I’m Still Learning Maths"
description = "OpenAI’s Navier–Stokes and ETH announcements, the unexpected uses of pure maths, and why I think this is a good time to start learning."
date = 2026-11-16
updated = 2026-11-16
draft = false

[taxonomies]
categories = ["2026"]
tags = ["mathematics", "AI", "learning", "cryptography"]

[extra]
toc = false
topic = "Applied AI"
cover = "img/blog/maths-with-ai/video-thumbnail.jpg"
+++

Coming from an Applied Math and Computing background, I find the question of whether maths is still worth learning quite personal.

OpenAI’s announcements about [Navier–Stokes](https://openai.com/index/navier-stokes-solution/) and the [Exponential Time Hypothesis](https://openai.com/index/building-scientific-understanding-with-academic-communities/) make it easy to wonder where humans fit. If you are about to spend several years studying mathematics, it is reasonable to ask what you are working towards when machines can produce results at this level.

The Navier–Stokes equations describe fluid motion. OpenAI claimed a proof that, under a smooth external force, initially smooth three-dimensional motion can develop a singularity in finite time. Researchers have since [questioned whether the Lean formalization matches the written proof](https://www.kcl.ac.uk/news/openais-navier-stokes-proof-called-into-question). That does not establish that the result is false, but it leaves work to do before treating the computer-checked version as verification of the written argument.

The ETH announcement concerns a different kind of problem. The hypothesis says, roughly, that deciding whether a Boolean formula in 3-SAT can be satisfied requires exponential time in the worst case. OpenAI’s [published notes](https://github.com/openai/math/blob/main/lean/docs/378.md) describe a subexponential algorithm. Its bound is still superpolynomial, so this does not settle P versus NP or immediately give us a fast tool for everyday use.

I want to understand those details. Reading that a problem has been solved tells me very little about the assumptions, the method, or what someone could build from it. Even deciding how much weight to give an announcement takes some knowledge of the mathematics involved.

Grant Sanderson’s [video on AI and mathematics](https://www.youtube.com/watch?v=LKrwhjOI8Nc) gave me a useful way to think about it. He compares practising maths to going to the gym. A machine can do the work faster, but going through it yourself still develops your own ability.

{{ youtube(id="LKrwhjOI8Nc", caption="3Blue1Brown · There’s never been a better time to go into math") }}

[Watch the full video on YouTube](https://www.youtube.com/watch?v=LKrwhjOI8Nc).

That makes sense to me when I think about building software with AI. I still want to understand the assumptions behind an answer, follow the reasoning, and work out whether it applies to the problem in front of me. An answer I cannot explain leaves me dependent on whoever, or whatever, produced it.

With software, it is tempting to stop once something runs. I want to be able to go further than that. If an AI suggests an algorithm, I want to understand why it works and which inputs might cause trouble. If it proposes a mathematical model, I want to know what the model assumes about the thing it represents. A convincing explanation can still leave out a condition that matters in the application.

That takes practice. Following a solution while it is in front of me is easier than reconstructing it later. Working through the problem myself gives me a better sense of where I am confused. Sometimes the part I cannot explain is a definition I have been using too loosely. Sometimes I have followed the algebra without understanding why anyone chose that approach.

I think that is part of what makes maths useful beyond a particular course or theorem. It gives me practice being precise about a question, keeping track of assumptions, and finding out where an argument stops working. I want those habits when I use AI too.

I also like how maths finds uses far from the questions people started with. Elliptic curves appear in [Wiles’s proof of Fermat’s Last Theorem](https://abelprize.no/sites/default/files/2021-09/The%20Abel%20Prize%202013-2017_Full.pdf) and in cryptographic systems such as ECDSA. Elliptic-curve cryptography predates Wiles’s proof, so one did not come from the other. Both use an older body of mathematics that people found different ways to build on.

For me, the interesting part is how much there is to learn around the result. To understand the connection, I need to learn what an elliptic curve is, how its points can be added, and how changing the number system changes the arithmetic. The picture below helps with the real-number case. Cryptography takes that arithmetic into finite fields, where the points are discrete.

ECDSA uses elliptic-curve arithmetic to create and verify digital signatures. I could use a library without understanding much of that background. Learning the maths gives me a way to understand the design, read its assumptions, and ask more useful questions about it. That is a reason to study it even if I never prove a new theorem about elliptic curves.

{{ figure(src="img/blog/maths-with-ai/elliptic-curve-addition.svg", alt="Point addition on an elliptic curve: a line intersects the curve, and reflection gives the sum.", caption="Point addition on a real elliptic curve. Cryptographic curves use points over finite fields.") }}

Image by [Googolplexian1221, via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:EllipticCurveAddition.svg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), unchanged. [Original image](https://upload.wikimedia.org/wikipedia/commons/e/e5/EllipticCurveAddition.svg).

[Try the curve in Desmos](https://www.desmos.com/calculator/t0neeko2lj) · [Explore finite-field arithmetic](https://ecdsa.com/tools/curve-playground) · [Cryptography reference](https://www.rfc-editor.org/rfc/rfc6090.html)

Complex numbers have a similar story. They emerged through work on [algebraic equations](https://mathshistory.st-andrews.ac.uk/HistTopics/Quadratic_etc_equations/) and later became part of the language of [quantum mechanics](https://interactivetextbooks.tudelft.nl/introduction-to-quantum-mechanics/content/complexnumbers.html). Geometry beyond Euclid became part of how [general relativity describes gravity](https://www.einstein-online.info/en/GeomGravity/). People working on the original questions could not have laid out all those later uses.

This makes me reluctant to judge mathematics only by whether I can see an immediate application. There may be something useful in the methods developed along the way, or in a connection to another subject. When AI produces a new result, I want to understand what else we might do with the ideas behind it. There could be years of worthwhile work in explaining those ideas, testing their limits, and finding where they apply.

I would be careful about claiming that asking questions or building theories will always be uniquely human. Grant considers those possibilities too. His argument leaves room for much more capable machines while still valuing the experience of learning maths.

Grant also gives a reason for thinking this is a good time to enter the field. The community knows it needs to change, which gives newcomers a chance to influence how mathematics is explained and how contributions are recognised. I like that there is room in his answer for people who enjoy teaching, visualising, applying, or understanding mathematics, as well as people who want to prove theorems.

I do not take that as a promise that a maths career will be easy or that every part of academic life will survive unchanged. I can still see a reason to learn without knowing exactly what the job market or research process will look like in ten years. I want to understand more of the systems I work with, and maths keeps giving me things I want to understand.

I think that makes this a good time to keep learning. I can ask AI about a step I do not understand, request a smaller example, or get help exploring a connection. I can ask it to explain the same idea algebraically and geometrically, then compare the explanations with a textbook or another source.

I also need to leave myself enough work to learn from. Getting a complete solution too early can make it hard to tell whether I could have found the next step myself. I would rather try the problem, ask for a hint when I get stuck, and spend some time with the part that confused me.

So I want to keep doing some of the work myself. Try a problem before reading the solution. Use AI when I get stuck. Then close the answer and see whether I can explain the reasoning without it.
