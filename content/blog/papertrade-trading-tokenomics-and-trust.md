+++
title = "Trying to Understand PaperTrade's Tokenomics"
description = "How PaperTrade pays winners, rewards losses with PAPER, and gets people to participate."
date = 2026-10-21
updated = 2026-10-21
draft = false

[taxonomies]
categories = ["2026"]
tags = ["web3", "product management", "tokenomics", "defi"]

[extra]
lang = "en"
toc = true
comment = true
copy = false
outdate_alert = true
outdate_alert_days = 30
math = false
mermaid = false
featured = false
reaction = true
topic = "Web3"
+++

PaperTrade caught my attention because losing traders receive PAPER, which they can stake for USDC rewards. Someone could lose money on a trade and still come out ahead through the rewards. I wanted to understand how that works, where the USDC comes from, and why the next person would join.

The tokenomics give people more than one reason to trade. Some want to profit from price movements; others may accept trading losses to accumulate PAPER. The mint rate also changes over time, so an early participant and a later participant can pay the same amount in losses for different amounts of PAPER. That made me curious about who benefits as more people join, and whether the rewards can keep attracting activity once earning tokens becomes less generous.

To work through that, I needed to understand how the LP pays winners, how losses become tokens, and what stakers can claim. I also looked at the relayer because being able to close a position affects whether a trader can realize those outcomes.

I worked through these questions in a [ChatGPT conversation](https://chatgpt.com/share/6ad8ae3a-5e88-83ec-a5e7-59d6fe144fd3), then checked the linked documentation and Guardian review. These notes cover the published design as of 21 October 2026. I haven't checked every deployed contract or reconstructed its live balances.

## Who pays when you win?

PaperTrade uses Hyperliquid's prices to create synthetic trades against its own liquidity pool, or LP. It reads the best bid and ask and takes their midpoint. Your position doesn't become an order on Hyperliquid's perpetual order book. The LP takes the other side. The documentation describes BTC and ETH positions with multipliers up to 1,000×. [Trading and pricing](https://papertrade.network/docs/learn/trades-pricing/)

Say you put $100 into a position at 100×. You now have $10,000 of exposure. If the price moves 0.5% in your direction, the linear gross profit is $50. PaperTrade applies an asymmetric impact adjustment to profitable closes, so that calculation alone doesn't tell you what gets credited. It also leaves out liquidation and the other settlement rules.

The LP needs USDC to pay that profit. PaperTrade's Martingaler mechanism allows the pool to start without upfront seed capital and build its bankroll from trading losses. If it cannot cover winning payouts, those payouts can wait. [Martingaler overview](https://papertrade.network/docs/martingaler/overview/)

That was where I needed to slow down. A profitable trade can leave you waiting for money.

The documentation splits the accounting into three parts:

| State | What it records |
| --- | --- |
| Treasury | Tracked LP funds under the settlement rules |
| sideBucket | Proceeds parked while the payout queue is active |
| Payout queue | Unpaid winning profits, with older claims paid first |

On an ordinary winning close, your original margin returns to your available balance separately. Any profit that cannot be funded goes into the queue. Later backing can pay the claims through a harvest process. [Solvency and queue](https://papertrade.network/docs/how/solvency-queue/)

For a simplified example, suppose you're owed $5,000 of profit and only $1,000 can be paid immediately. The remaining $4,000 is still owed to you. Putting it in a queue doesn't create the missing USDC. You have to wait for backing to arrive.

## Losing a trade earns PAPER

Eligible realized losses mint PAPER. The documented starting rate is 100 PAPER per dollar of eligible loss basis while tracked LP is below $2 million. After the threshold, the rate decays using a high-water mark. Distributing funds out of the LP doesn't reset it to the earlier rate. [Mint curve](https://papertrade.network/docs/how/mint-curve/)

So the same eligible loss can earn different amounts of PAPER depending on when it happens. I say “eligible loss” because the mint basis can differ from the gross amount a trader loses under the settlement rules.

You can stake PAPER for a share of eligible USDC distributions. The standard documented staking model has no lockup or cooldown, and rewards can be claimed into the Exchange balance before withdrawal. [Staking and claims](https://papertrade.network/docs/paper/staking/)

Suppose your stake stays at 1% of the pool while $50,000 is distributed. You would receive $500. But you still need to compare that with what you spent acquiring PAPER, and your share can shrink as other people stake. One distribution doesn't tell you how much the next one will pay.

This also changes how I would read the trading volume. Someone might trade because they expect BTC to rise. Someone else might accept a loss because they want PAPER. Both add volume, but they are doing different things.

Guardian identifies farming on gross losses, including hedged strategies, as a retained economic risk. A trader's losing position can qualify for tokens while another position offsets some of that loss. [Guardian security review](https://www.guardian.security/portfolio/papertrade/protocol-review-2026-10-09/)

## The liquidation rule needs a separate read

PaperTrade has a hard-bust trigger. Liquidation through that path takes the full isolated margin, even where a voluntary close at the trigger could still return some equity. The documentation describes a buffer of roughly five basis points of price. [Liquidations](https://papertrade.network/docs/learn/liquidations/)

With a large position relative to your margin, a small price difference can take a large share of your money. I wouldn't use the ordinary closing calculation to estimate what comes back after liquidation. The two paths follow different rules.

## Who submits the trades?

The user signs an instruction, and the relayer and batch executor submit it to the Exchange. Session-key and contract checks validate the authority behind it. [Architecture](https://papertrade.network/docs/how/architecture/)

I can inspect what reaches the contract. That still leaves me asking what happened to a request before it got there. Was it delayed? Rejected? Could I submit it another way?

Guardian's review records concerns about relayer dependence and price bounds on signed instructions. It also describes upgrade authority, while the off-chain relayer, sweeper, and keepers were outside the review's scope. I can't treat that contract review as proof that the submission service is fair or always available. [Guardian security review](https://www.guardian.security/portfolio/papertrade/protocol-review-2026-10-09/)

The protocol also documents a risk from using the instantaneous best-bid/ask midpoint. Changes to those quotes can affect its reference price. Open-interest caps and adjustments to winning PnL can limit exposure, but they don't remove the risk. [Risk documentation](https://papertrade.network/docs/how/risk/)

I also want to know how I would close my position if the authorized relayer stopped submitting requests. I'd want to see that fallback demonstrated.

## Why would people join?

The reward design gives people a reason to arrive early. They can earn PAPER at the earlier mint rate, stake it, and potentially receive USDC. If they share those rewards, other people have a reason to look into it too.

That's how I read the incentive loop. I don't know the team's internal marketing plan. I also haven't verified the paid-promotion claims, launch figures, or wallet earnings discussed in the original chat, so I'm leaving them out.

What interests me is whether people keep trading when earning PAPER becomes less attractive. I would look at repeat participation after rewards decline, how concentrated the distributions are, and how much volume comes from identifiable farming. Counting wallets wouldn't be enough because one person can use several addresses.

## What I still haven't answered

I also haven't reconciled the money. I'd need the recoverable USDC, trader balances, locked margin, queued profits, accrued rewards, and open-position exposure. Those numbers need to follow the contract's accounting so I don't count the same liability twice.

Then I'd check what happens when many open positions become profitable together, especially after funds have already been distributed to stakers. How much USDC remains to pay them? How old are the unpaid claims?

For now, I'd want the public dashboard to show available balances, queued profits, queue age, and completed withdrawals separately. If I'm waiting for $4,000, I want to know how long people ahead of me have been waiting and what funds are available to pay us.
