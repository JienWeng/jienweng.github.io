+++
title = "PolyArb: Polymarket Arbitrage Platform in Rust"
description = "A Rust Polymarket arbitrage platform in production, with fee-aware checks, exposure limits, paper trading, and an activity dashboard."
template = "project-detail.html"
updated = 2026-11-12
[extra]
project_id = "polyarb"
toc = true
+++

## Production platform

PolyArb is a Rust Polymarket arbitrage platform now in production. It evaluates YES–NO pairs after fees and available order-book depth, checking quote freshness, order budgets, and exposure before execution.

## Paper trading and monitoring

PolyArb also supports paper trading with real prices and simulated orders. Paper balances persist across restarts, and paper trading does not need a wallet.

A React dashboard shows balance, exposure, market activity, and execution events. These records help separate detected opportunities from simulated fills. Paper results do not establish live returns.

## Availability

The source code is not publicly shared. Read [The Maths Behind PolyArb](@/blog/polyarb-arbitrage-math.md) for worked examples of fees, depth, and partial fills.
