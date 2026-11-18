+++
title = "A Design Checklist You Can Give Your AI"
description = "How to use my design guide, what it asks an agent to check, and what three review trials showed."
date = 2026-11-12
updated = 2026-11-12
draft = false

[taxonomies]
categories = ["2026"]
tags = ["AI", "product management"]

[extra]
toc = true
topic = "Applied AI"
+++

I wanted a link I could paste into an AI conversation to have it check an interface, explain what needs work, and suggest fixes.

[Design Guide for AI](@/design.md) is that link. It has 138 checklists and 908 items from Checklist Design, plus instructions for choosing checks and reporting what the agent can verify.

## Give the agent a starting point

Open the [guide page](@/design.md), copy the review prompt, and add your website, screenshots, or project files. The assistant needs the interface as well as the guide.

A shorter prompt:

> Read https://jienweng.github.io/design/llms.txt and follow its review protocol. Review this interface using the relevant checklists. Account for every selected item, cite evidence, and separate observed problems from checks you cannot verify. Suggest fixes before changing anything.

Then add the interface, narrowed where you can: “Review this sign-up form” works better than “Check my app.”

The [LLM entry point](/design/llms.txt) has the review instructions and links to each checklist, so an agent fetches only what it needs. The [complete text guide](/design/guide.txt) holds everything, for offline use or assistants that cannot follow links. If it cannot open links at all, paste in the relevant text.

## What the agent should return

First, the agent should say which checklists it selected and why. A form might need the input-field, button, submission, and validation checklists; an empty-state screenshot needs a different set.

Each item gets a status: Present, Partial, Missing, Not applicable, or Unverified. The report gives evidence and location, proposes fixes, reconciles item counts, and lists anything skipped.

A screenshot can show that an email field has no visible label. It cannot show how a screen reader announces the field. The report should separate the two and name the test still needed.

Optional elements are similar. A checklist might mention an illustration, but a small utility form may not need one. The agent should say so rather than add decoration to satisfy a list.

## Where the checklists come from

[Checklist Design](https://www.checklist.design/) publishes an [official agent-skill repository](https://github.com/Checklist-Design/skills) under the MIT license. I used that bundle rather than scrape the website.

The items, descriptions, and tips are their work. I added the website presentation, shareable text files, review protocol, and checks for incomplete reports. The [license](/design/LICENSE.txt) and [source manifest](/design/manifest.json) credit the original authors and pin the source commit.

It covers design systems, web apps, mobile apps, websites, and user flows. It is a snapshot; source changes need review before import.

## What I tested

I ran three fresh agent reviews, each with different evidence: a form’s source code, an empty-state screenshot, and a modal’s source with recorded browser observations. The reviewers did not see the expected answers.

They reported all 37 selected items and matched the expected outcomes in 19 checks. They found the four planted problems: a missing field label, missing supporting text, no modal close action, and a modal that overflowed on mobile. They left unseen behavior unverified and respected the request to omit decorative illustrations.

These were three controlled cases with one model, not proof of how every model handles a large product or an ambiguous screenshot. The report validator checks item IDs, missing rows, totals, and completion claims. A person still judges whether the evidence supports the findings and the fixes help.

To try it, [copy the prompt from the guide](@/design.md) and start with one screen or flow you can inspect yourself.
