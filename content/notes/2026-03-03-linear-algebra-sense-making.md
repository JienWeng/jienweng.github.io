+++
title = "Making Linear Algebra Make Sense with Gemini CLI"
description = "How I used Gemini CLI to help an adult learner master linear algebra through sense-making and interactive intuition building."
date = 2026-03-03
updated = 2026-03-03
draft = true
aliases = ["/posts/2026-03-03-linear-algebra-sense-making/"]

[taxonomies]
categories = ["2026"]
tags = ["math", "linear algebra", "ai", "gemini-cli"]

[extra]
topic = "Machine Learning"
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
hero_image = "/static/img/posts/linear-algebra-sense-making-hero.png"
author = "Jien Weng"
+++

Teaching linear algebra works better when the learner can picture the operation before meeting the notation. This note starts with geometric intuition, then moves to vectors, linear maps, and matrix multiplication once the picture is useful.

Linear algebra appears in AI and 3D graphics, but many adult learners meet it as a dry sequence of matrix operations. Textbooks often assume there is plenty of time to work through the notation. My learner had a job and limited time, so we started with the question behind row-by-column multiplication.

Last weekend I tried something different. I used Gemini CLI to help a learner who was stuck on the traditional formula-first path. The goal was simple. Find the sweet spot between math and common sense. We moved away from the rigid structure of a classroom. We treated the math like a puzzle to solve together.

## Why Gemini CLI

Standard textbooks are a one-way street. You read, struggle, and wait for the explanation to click. Gemini CLI gave us an interactive loop between the symbols and the intuition behind them.

When my learner hit a wall, we did not re-read the same definitions. We asked Gemini to explain each concept through things he already knew. We could switch explanations quickly; in one session, we tried five analogies in five minutes and kept working while the question was still fresh.

## Balancing Math and Meaning

The biggest hurdle is the gap between symbols and significance. Computing a dot product is easy. Explaining why it matters is the hard part. Many people can do the math but few can see the picture.

Gemini worked as a teaching assistant. We followed a specific flow.
1.  **Iterate on Intuition:** Start with a simple analogy. Maybe we talk about how light hits a surface or how similar two songs are. Then we tighten it with math.
2.  **Real-Time Context:** Instantly see where these concepts live in the real world. We would ask for a Python snippet that used the concept we just discussed.
3.  **Bridge the Gap:** Translate intuition back into formal notation. Once the learner understands the why the how becomes trivial.

The math is not the enemy. The lack of context is. By bringing the math into the CLI we made it tangible. We made it something you can poke and prod until it makes sense.

## What changed

The breakthrough happened during our last session. He was no longer following a recipe; he could explain the logic, see the vectors moving, and describe the transformation in the space.

Using an LLM to build a mental model changed the session from repeated explanation to shared exploration. The learner could challenge an analogy, ask for a different one, and decide when the formal notation finally matched the picture.

## Final note

Linear algebra does not have to begin with a slog through notation. Start with the operation, connect it to a picture, and introduce the formal expression when the picture is doing useful work.

## Get the Sense-Maker's Playbook

I have compiled the method and Gemini CLI prompts I used with my learner into a short PDF.

**The Linear Algebra Sense-Maker's PDF includes:**
*   A roadmap for intuitive linear algebra.
*   Prompt templates for your own sense-making CLI.
*   The eigenvector and dot product case studies.

[Download the PDF here.](https://checkya.com/jienweng/offers/31145)
