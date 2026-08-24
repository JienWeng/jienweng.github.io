+++
title = "An Internal CRM Is a Business Transformation Project"
description = "What building an internal CRM taught me about requirements, adoption, and the gap between a workflow and a system."
date = 2026-05-25
updated = 2026-05-25
draft = false
aliases = ["/posts/quandatics-crm-business-transformation/"]

[taxonomies]
categories = ["2026"]
tags = ["business transformation", "product management", "CRM", "automation"]

[extra]
lang = "en"
toc = true
comment = true
copy = false
outdate_alert = false
outdate_alert_days = 120
math = false
mermaid = false
featured = false
reaction = true
topic = "Business Transformation"
+++

An internal CRM can look like a software project from the outside. The harder part is usually understanding how the team already works, where information gets lost, and which decisions are being made from incomplete data.

That is the problem I am working on with Quandatics. The CRM connects sales, finance, and project teams, but the system is only useful if it matches the work those teams actually do.

## Start with the workflow

The first temptation is to start with screens. A dashboard, a customer table, and a few status fields look like progress, but they do not answer the real questions.

- Who owns the next action?
- Which information does finance need before an invoice can move?
- What does sales promise before a project is handed over?
- Where does a project manager look when the original context is missing?

These questions connect to the larger finance processes around order-to-cash, procure-to-pay, and record-to-report. The CRM does not replace those processes. It gives the people involved a shared place to see what is happening and what still needs attention.

## Requirements are decisions

Good requirements do more than describe a field or a button. They record a decision about how the organisation wants work to move.

For example, “add a project status” is incomplete. The team still needs to agree on who changes the status, what each status means, what happens when a project is blocked, and which other team should be notified.

That is where business transformation and product work overlap. I translate the operating problem into requirements, work with the people who will use the system, and turn the agreed workflow into something that can be built and tested.

## Build, deploy, support

The work covers more than development. I am involved across requirements, design, implementation, production deployment, and support.

Each stage changes the system in a different way.

- Requirements expose the assumptions in the current process.
- Design makes those assumptions visible to the people who use them.
- Development turns the agreed flow into a working tool.
- Deployment introduces the tool to the real operating environment.
- Support shows where the original model was incomplete.

The last part is easy to underestimate. A workflow that looks correct in a meeting may fail when someone has an unusual customer, a late approval, or missing information from another team. Support is where those cases become the next product decision.

## The lesson so far

An internal CRM should not be judged by how many screens it contains. It should reduce the amount of context people have to reconstruct before they can act.

That means the system has to follow the work, not force every team into a generic pipeline. The useful design is the one that makes ownership, handover, and missing information easier to see.

This is a generalised case study. Client-specific workflows, implementation details, and operational results remain confidential.
