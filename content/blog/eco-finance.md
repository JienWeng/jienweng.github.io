+++
title = "Eco Finance: A PayHack Prototype"
description = "A carbon-footprint and financial-literacy prototype built during PayHack 2024 with OpenFinance APIs."
date = 2024-12-29
updated = 2024-12-29
draft = false
aliases = ["/posts/eco-finance/"]

[taxonomies]
categories = ["2024"]
tags = ["hackathons", "sustainability"]

[extra]
lang = "en"
toc = true
comment = true
copy = false
outdate_alert = true
outdate_alert_days = 120
math = false
mermaid = false
featured = false
reaction = false
+++

Eco Finance shows estimated carbon emissions alongside everyday spending. We built it at PayHack 2024 as a 24-hour prototype using OpenFinance transaction data and dummy emission factors.

{{ figure(src="https://cdn.cosmos.so/3034bd0a-9dae-4078-80a9-a641c747b58a?format=jpeg", alt="Eco Finance interface", caption="The Eco Finance interface.") }}

## Estimating a transaction’s footprint

The proposed calculation multiplies the amount spent by an emission factor for the merchant category code (MCC). With a dummy factor of 0.5 kg CO₂ per RM, a RM 100 transaction comes to 50 kg CO₂.

Real use would need researched factors per merchant category. We considered surveys and work with DOSM; the hackathon version did not validate the estimates.

## The proposed business model

We explored pooling estimated savings, certifying carbon credits, selling them to companies, and rewarding users, with Bursa Carbon Exchange as the market reference. This was a proposal to investigate, not an implemented or validated credit system.

{{ figure(src="https://cdn.cosmos.so/f54512bd-f014-43ac-a1b1-39628b5990d7?format=jpeg", alt="The Eco Finance business plan", caption="The proposed business plan.") }}

## What we built

We made a customer interface and an admin view. The demo is no longer maintained, so these screenshots are the record.

{{ figure(src="https://cdn.cosmos.so/7ee8a2c3-551c-4726-9551-f7d6ab743391?format=jpeg", alt="Admin dashboard", caption="The admin dashboard.") }}

We didn’t make the final round T.T. I wrote more about the build, mentoring, and deadline problems in [my first hackathon experience](@/blog/first-hackathon-experience.md).
