+++
title = "Eco Finance: A PayHack Prototype"
description = "A carbon-footprint and financial-literacy prototype built during PayHack 2024 with OpenFinance APIs."
date = 2024-12-29
updated = 2024-12-29
draft = false
aliases = ["/posts/eco-finance/"]

[taxonomies]
categories = ["2024"]
tags = ["hackathon"]

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

We built Eco Finance during PayHack 2024 to show estimated carbon emissions alongside everyday spending. It was a 24-hour prototype using OpenFinance transaction data and dummy emission factors.

![Eco Finance Interface](https://cdn.cosmos.so/3034bd0a-9dae-4078-80a9-a641c747b58a?format=jpeg)

## Estimating a transaction’s footprint

The proposed calculation uses the merchant category code (MCC), an emission factor, and the amount spent. For example, a dummy factor of 0.5 kg CO₂ per RM gives an estimate of 50 kg CO₂ for a RM 100 transaction.

Real use would require research into the factors for each merchant category. We considered surveys and work with DOSM; the hackathon version did not validate those estimates.

## The proposed business model

We explored pooling users’ estimated savings, certifying carbon credits, selling them to companies, and rewarding users. Bursa Carbon Exchange was the market reference. This was a proposal to investigate, not an implemented or validated credit system.

![The whole business plan of eco-finance](https://cdn.cosmos.so/f54512bd-f014-43ac-a1b1-39628b5990d7?format=jpeg)

## What we built

We made a customer interface and an admin view. The demo is no longer maintained, so these screenshots record the prototype.

![Admin Dashboard](https://cdn.cosmos.so/7ee8a2c3-551c-4726-9551-f7d6ab743391?format=jpeg)

We didn’t make the final round T.T. I wrote more about the build, mentoring, and deadline problems in [my first hackathon experience](@/blog/first-hackathon-experience.md).
