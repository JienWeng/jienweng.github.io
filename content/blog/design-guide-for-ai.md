+++
title = "A Design Checklist You Can Give Your AI"
description = "How to use my design guide, what it asks an agent to check, and what three review trials showed."
date = 2026-11-12
updated = 2026-11-12
draft = false

[taxonomies]
categories = ["2026"]
tags = ["design", "AI", "user experience"]

[extra]
toc = true
topic = "Applied AI"
+++

I wanted a link I could paste into an AI conversation and say: use this to check the interface, explain what needs work, and suggest fixes.

I assembled [Design Guide for AI](@/design.md) around that idea. It includes 138 checklists and 908 individual items from Checklist Design, with instructions for choosing the relevant checks and reporting what the agent can verify.

## Give the agent a starting point

Open the [guide page](@/design.md), copy the review prompt, and add your website, screenshots, or project files. The assistant needs access to the interface as well as the guide.

For a shorter prompt, use:

> Read https://jienweng.github.io/design/llms.txt and follow its review protocol. Review this interface using the relevant checklists. Account for every selected item, cite evidence, and separate observed problems from checks you cannot verify. Suggest fixes before changing anything.

Then add the interface you want reviewed. You can narrow the request to a screen, component, or flow: “Review this sign-up form” gives the agent a clearer scope than “Check my app.”

The [LLM entry point](/design/llms.txt) contains the review instructions and links to individual checklists. An agent can fetch the ones it needs. The [complete text guide](/design/guide.txt) contains the whole collection for offline use or an assistant that cannot follow the individual links. If it cannot open links at all, paste the relevant text into the conversation.

## What the agent should return

Before reviewing, the agent should explain which checklists it selected and why. A form might need the input-field, button, submission, and validation checklists. A screenshot of an empty state calls for a different selection.

Each selected item gets a status: Present, Partial, Missing, Not applicable, or Unverified. The report should include the evidence and location, then propose fixes for observed problems. It also has to reconcile its item counts and list anything it skipped.

For example, a screenshot can show that an email field has no visible label. It cannot establish how a screen reader announces the field. The report should separate those observations and say what test is still needed.

The same applies to optional elements. A checklist might mention an illustration, but a small utility form may have no use for one. The agent should explain that decision rather than recommend adding decoration to satisfy a list.

## Where the checklists come from

[Checklist Design](https://www.checklist.design/) publishes an [official agent-skill repository](https://github.com/Checklist-Design/skills) under the MIT license. I used its published bundle rather than scrape the website page by page.

The checklist items, descriptions, and tips are their work. I added the website presentation, shareable text files, review protocol, and checks for incomplete reports. The [license](/design/LICENSE.txt) and [source manifest](/design/manifest.json) identify the original authors and the pinned source commit.

The collection covers design systems, web apps, mobile apps, websites, and user flows. It is a snapshot; future changes to the source need to be reviewed and imported.

## What I tested

I ran three fresh agent reviews with different evidence: a form’s source code, an empty-state screenshot, and a modal’s source plus recorded browser observations. The reviewers were not given the expected answers.

Across their selected checklists, they reported all 37 items and matched the expected outcomes in 19 checks. They found the four planted problems: a missing field label, missing supporting text, no modal close action, and a modal that overflowed on mobile. They left unseen behavior unverified and respected the request to omit decorative illustrations.

These were three controlled cases using one model. They do not establish how every model will handle a large product or an ambiguous screenshot. The report validator checks item IDs, missing rows, totals, and completion claims. Someone still needs to assess whether the evidence supports the findings and whether the suggested fixes help.

To try it, [copy the prompt from the guide](@/design.md) and start with one screen or flow you can inspect yourself.
