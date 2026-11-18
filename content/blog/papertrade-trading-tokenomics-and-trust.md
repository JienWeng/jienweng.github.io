+++
title = "Trying to Understand PaperTrade's Tokenomics"
description = "How PaperTrade pays winners, rewards losses with PAPER, and gets people to participate."
date = 2026-10-21
updated = 2026-10-21
draft = false

[taxonomies]
categories = ["2026"]
tags = ["web3", "product management"]

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

PaperTrade caught my attention because losing traders receive PAPER, which they can stake for USDC rewards. You could lose on a trade and still come out ahead. I wanted to know how, where the USDC comes from, and why the next person would join.

Some people trade to profit from price moves; others may accept losses to accumulate PAPER. The mint rate also changes, so an early and a later participant can lose the same amount and receive different amounts of PAPER. Who benefits as more people join, and do the rewards keep attracting activity once they become less generous?

So I looked at how the LP pays winners, how losses become tokens, what stakers can claim, and the relayer, since a trader who can't close a position can't realize any of it.

I worked through this in a [ChatGPT conversation](https://chatgpt.com/share/6ad8ae3a-5e88-83ec-a5e7-59d6fe144fd3), then checked the linked documentation and Guardian review. These notes cover the published design as of 21 October 2026, not every deployed contract or its live balances.

## Who pays when you win?

PaperTrade creates synthetic trades against its own liquidity pool (LP), priced at the midpoint of Hyperliquid's best bid and ask. Your position doesn't become an order on Hyperliquid's perpetual order book; the LP takes the other side. The documentation describes BTC and ETH positions with multipliers up to 1,000×. [Trading and pricing](https://papertrade.network/docs/learn/trades-pricing/)

Say you put $100 into a position at 100×, giving $10,000 of exposure. If the price moves 0.5% your way, the linear gross profit is $50. But PaperTrade applies an asymmetric impact adjustment to profitable closes, and that sum ignores liquidation and the other settlement rules, so it isn't what gets credited.

The LP needs USDC to pay that profit. PaperTrade's Martingaler mechanism lets the pool start without seed capital and build its bankroll from trading losses. If it cannot cover winning payouts, those payouts can wait. [Martingaler overview](https://papertrade.network/docs/martingaler/overview/)

So a profitable trade can leave you waiting for money. The documentation splits the accounting into three parts:

| State | What it records |
| --- | --- |
| Treasury | Tracked LP funds under the settlement rules |
| sideBucket | Proceeds parked while the payout queue is active |
| Payout queue | Unpaid winning profits, with older claims paid first |

On a winning close, your margin returns to your available balance separately. Profit that cannot be funded goes into the queue, and later backing can pay those claims through a harvest process. [Solvency and queue](https://papertrade.network/docs/how/solvency-queue/)

In a simplified case, you're owed $5,000 of profit and only $1,000 can be paid now. The other $4,000 is still owed, but the queue doesn't create the USDC; you wait for backing.

## Losing a trade earns PAPER

Eligible realized losses mint PAPER. The documented starting rate is 100 PAPER per dollar of eligible loss basis while tracked LP is below $2 million. Above that threshold, the rate decays using a high-water mark, so distributing funds out of the LP doesn't reset it to the earlier rate. [Mint curve](https://papertrade.network/docs/how/mint-curve/)

The same eligible loss can earn different amounts of PAPER depending on timing. “Eligible” matters: the mint basis can differ from what a trader loses under the settlement rules.

Staked PAPER earns a share of eligible USDC distributions. The standard model has no lockup or cooldown, and rewards can be claimed into the Exchange balance before withdrawal. [Staking and claims](https://papertrade.network/docs/paper/staking/)

A stake that stays at 1% of the pool while $50,000 is distributed receives $500. Compare that with what you spent acquiring PAPER. Your share can shrink as others stake, and one distribution doesn't predict the next.

This changes how I read volume. One person trades expecting BTC to rise; another accepts a loss to get PAPER. Both add volume for different reasons.

Guardian lists farming on gross losses, including hedged strategies, as a retained economic risk. A losing position can qualify for tokens while another position offsets some of that loss. [Guardian security review](https://www.guardian.security/portfolio/papertrade/protocol-review-2026-10-09/)

## The liquidation rule needs a separate read

Liquidation through PaperTrade's hard-bust trigger takes the full isolated margin, even where a voluntary close at the trigger could still return some equity. The documentation describes a buffer of roughly five basis points of price. [Liquidations](https://papertrade.network/docs/learn/liquidations/)

With a large position relative to margin, a small price difference can take much of your money. The ordinary closing calculation won't tell you what comes back after liquidation; the paths follow different rules.

## Who submits the trades?

The user signs an instruction, and the relayer and batch executor submit it to the Exchange. Session-key and contract checks validate the authority behind it. [Architecture](https://papertrade.network/docs/how/architecture/)

I can inspect what reaches the contract, not what happened to a request before that. Was it delayed? Rejected? Could I submit it another way?

Guardian's review flags relayer dependence and price bounds on signed instructions, and describes upgrade authority. The off-chain relayer, sweeper, and keepers were out of scope, so the review doesn't prove the submission service is fair or always available. [Guardian security review](https://www.guardian.security/portfolio/papertrade/protocol-review-2026-10-09/)

The protocol also documents a risk in using the instantaneous best-bid/ask midpoint: quote changes can move its reference price. Open-interest caps and adjustments to winning PnL limit exposure but don't remove the risk. [Risk documentation](https://papertrade.network/docs/how/risk/)

If the authorized relayer stopped submitting requests, how would I close my position? I'd want to see that fallback demonstrated.

## Why would people join?

Early arrivals can earn PAPER at the earlier mint rate, stake it, and potentially receive USDC. If they share those rewards, others have a reason to look too. That's my reading; I don't know the team's marketing plan. I've left out the paid-promotion claims, launch figures, and wallet earnings from the original chat because I haven't verified them.

What I want to know is whether people keep trading once earning PAPER is less attractive. I would look at repeat participation after rewards decline, how concentrated the distributions are, and how much volume comes from identifiable farming. Counting wallets isn't enough, because one person can use several addresses.
