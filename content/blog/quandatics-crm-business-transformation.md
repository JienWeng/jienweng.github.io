+++
title = "Why We Built an Internal CRM After Trying Salesforce"
description = "A personal case study on adapting a CRM to the way a team actually works."
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

The obvious question is why we did not use an outside CRM. The team had already tried Salesforce.

Salesforce was not a bad product. The problem was the fit. The team had to keep adjusting its own workflow to match the way Salesforce expected the work to be organised. After a while, the CRM became another process to work around instead of a place that helped people do the work.

That was the starting point for the internal CRM I am working on with Quandatics. It connects sales, finance, and project teams, but the first job was not to build a dashboard. It was to understand what actually happens between those teams.

## The workflow comes first

Sales may start with a customer conversation. Finance needs different information before money can move. A project team needs to know what was promised, who owns the next action, and whether something is blocked.

Those details do not always fit neatly into one generic pipeline. The CRM needs to follow the handover between teams, including the parts that people currently keep in messages, spreadsheets, or memory.

This is also why a project status is not just a dropdown. Someone has to own the status, the team has to agree on what it means, and the next person needs to know what to do with it. Otherwise, we have built a nicer-looking place to store ambiguity.

## My part in the work

I work across the requirements, design, development, production deployment, and support. I speak with the people using the process, translate the awkward parts into requirements, and then work through what can actually be built.

Some decisions are straightforward. Others need a few rounds because sales, finance, and project teams are looking at the same customer from different points in the process. A field that looks unnecessary to one person may be the thing another person needs before they can raise an invoice or start delivery.

The support work is where the real gaps appear. A workflow can look complete in a meeting and still fail when a customer changes scope, an approval arrives late, or information is missing from the previous handover. Those cases become the next product decision.

## What I have taken from it

The point of an internal CRM is not to have more screens than Salesforce. It is to reduce the amount of context people have to reconstruct before they can act.

Sometimes an established tool is the right answer. Sometimes the cost is not the licence. It is the amount of work required to make the organisation behave like the tool.

This is a generalised case study. Client-specific workflows, implementation details, and operational results remain confidential.
