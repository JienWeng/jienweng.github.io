+++
title = "Eco Finance: A Sustainable Future Prototype"
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

Eco Finance started with a problem we could explain quickly, people could not see the carbon cost hidden inside ordinary spending. We built the prototype during PayHack 2024 and used it to test the idea under hackathon constraints.

PayHack 2024 was our first physical hackathon, with teams building under a tight deadline.

Our project, Eco Finance, focuses on a carbon tax expected in 2026. Although it initially targets specific industries, the same idea could eventually apply to everyday spending in Malaysia. Read more about the 2026 carbon tax here.

European countries are already applying ESG policies in industries such as automobiles. We wanted to look more closely at what a similar idea could mean for everyday spending in Malaysia.

![Eco Finance Interface](https://cdn.cosmos.so/3034bd0a-9dae-4078-80a9-a641c747b58a?format=jpeg)

## Understanding the idea

How much carbon is attached to a Shopee parcel or a drive to work? Most people do not see that information in their payment history. The prototype tried to make the estimate visible alongside the transaction. According to Visa, 80% of Malaysians are aware of the environmental impact of consumption, but awareness does not provide a number for a particular purchase.

## How it works

The OpenFinance API can connect to people's transaction details, allowing us to aggregate transactions and estimate their carbon footprints. The calculation would multiply the emission factor by the amount spent.

For example, if the emission factor for a specific merchant category is 0.5 kg CO2 per RM, and a person spends RM 100, the carbon footprint would be 0.5 kg CO2/RM * 100 RM = 50 kg CO2.

There's an established merchant category code (MCC) in transaction details, where we only need to fine-tune and investigate the actual emission factors for each merchant code. This could be done by collaborating with the Department of Statistics Malaysia (DOSM) to conduct surveys and research among Malaysians. In this project, we are using dummy variables based on this ideology only.

## A possible business model

The proposed model would pool the estimated surplus from users' activity and trade the resulting carbon credits. We used the Worldometer estimate of 8 tonnes of carbon emissions per person per year as a baseline. Bursa Carbon Exchange (BCX), established on 9 December 2022, provided the market reference for the idea. [Read more about BCX here](https://www.allenandgledhill.com/perspectives/publications/bulletins-malaysia/2023/bursa-malaysia-launches-voluntary-carbon-market-exchange/).

<YouTube id="1QKwHFVsEXE" />

From [Petronas](https://www.petronas.com/sustainability/delivering-net-zero), it's evident that their future plan aims for net-zero carbon emission by 2050. This proves there is a market in Malaysia, and more people will enter the market and participate.

## Encouraging Eco-Friendly Practices

How do we encourage eco-friendly spending habits in Malaysia? We aim to attract more people, even those who are not initially interested in eco-friendly practices, to join us. We can make Malaysia greener and more sustainable, at least in the sense of ESG. We choose to reward users with healthy spending habits in terms of eco-friendly spending and reward them with cash for being environmentally friendly.

![The whole business plan of eco-finance](https://cdn.cosmos.so/f54512bd-f014-43ac-a1b1-39628b5990d7?format=jpeg)

## Sustainable Business Model

We can summarize the business circulation here and make it sustainable as well, where we can become self-sustaining:


1. Collect carbon credits from users
2. Pool up carbon credits
3. Certify carbon credits with Bursa Carbon Exchange (BCX)
4. Sell carbon credits to companies who need them
5. Reward users to encourage eco-friendly spending habits.


## Project Random Thingy

Now, it's about the random thingys of the project. We have the project hosted at this link. Although it is not fully complete, it serves as a prototype and is yet to be an MVP. Considering we had only 24 hours to complete this from idea to execution, I mean, it's good for a first-timer. Right...?

This was a 24-hour hackathon prototype. The hosted demo is no longer maintained, so I have kept the screenshots here as an archive of what we built. Email me if you want to discuss the product or implementation.

The admin view looked like this:

![Admin Dashboard](https://cdn.cosmos.so/7ee8a2c3-551c-4726-9551-f7d6ab743391?format=jpeg)


## Wrap-Up

Eco Finance was our attempt to make carbon footprints visible through a familiar object, a payment history. The carbon-credit idea gave the prototype a possible business model, although we did not make it to the final round T.T

Hope you guys like it :D

Oh btw! Once again.. You can read the full story [here](@/blog/first-hackathon-experience.md).
